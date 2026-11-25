import runpy
from pathlib import Path
import unittest
from types import SimpleNamespace
from textwrap import dedent

MODULE = Path(__file__).resolve().parents[1] / "game" / "python-packages" / "phone_rules.py"


class PhoneRulesTests(unittest.TestCase):
    def rules(self):
        self.assertTrue(MODULE.exists(), "Phone rules have not been implemented")
        return runpy.run_path(str(MODULE))

    def test_register_thresholds(self):
        allowed = self.rules()["register_open"]
        for register, interest, kiss, expected in (
            ("Casual", 0, False, True), ("Friendly", 5, False, False),
            ("Friendly", 6, False, True), ("Flirt", 15, False, False),
            ("Flirt", 16, False, True), ("Romantic", 100, False, False),
            ("Sexy", 0, True, True),
        ):
            with self.subTest(register=register, interest=interest):
                self.assertEqual(allowed(register, interest, kiss), expected)

    def test_keywords_inside_phrases(self):
        matches = self.rules()["matches_keyword"]
        self.assertTrue(matches("Did she send an anonymous LETTER?", ("anonymous letter",)))
        self.assertFalse(matches("A newsletter?", ("letter",)))


class PhoneCatalogTests(unittest.TestCase):
    def setUp(self):
        core = MODULE.parents[1] / "core"
        self.runtime = {"__name__": "phone_test"}
        namespace = self.runtime
        catalog = (core / "telefono_catalogo.rpy").read_text(encoding="utf-8-sig")
        exec(dedent(catalog.split("init python:\n", 1)[1]), namespace)
        source = (core / "telefono_nuovo.rpy").read_text(encoding="utf-8-sig")
        python = source.split("init python:\n", 1)[1].split("\nlabel ", 1)[0]
        namespace.update(
            phone_rules=SimpleNamespace(**runpy.run_path(str(MODULE))),
            giorno=14, sara_stagista=False, phone_kisses=set(), phone_used=set(),
            phone_register_day={}, phone_previews={}, phone_open={}, chat_log={},
            phone_notebook={}, phone_reply_due={}, phone_investigation=False,
            fatto=lambda fact: False, valore_interest=lambda contact: 20,
            renpy=SimpleNamespace(random=SimpleNamespace(choice=lambda lines: lines[0])),
        )
        exec(dedent(python).replace("import phone_rules\n", "", 1), namespace)

    def test_catalog_covers_routes_and_josh_with_unique_ids(self):
        lines = self.runtime["PHONE_LINES"]
        self.assertEqual(len({line["id"] for line in lines}), len(lines))
        self.assertEqual(
            {line["contact"] for line in lines if line["mode"] == "register"},
            {"howard", "ex", "amica", "daniel", "capa", "editore", "simon", "amico", "josh"},
        )

    def test_preview_is_reused_and_sending_consumes_daily_slot(self):
        engine = self.runtime
        preview = engine["phone_preview"]("howard", "Casual")
        self.assertIs(preview, engine["phone_preview"]("howard", "Casual"))
        self.assertEqual(engine["chat_log"], {})
        engine["phone_select"]("howard", preview)
        self.assertIn(preview["id"], engine["phone_used"])
        self.assertIsNone(engine["phone_preview"]("howard", "Friendly"))
        engine["giorno"] += 1
        self.assertIsNotNone(engine["phone_preview"]("howard", "Friendly"))
        self.assertNotEqual(engine["phone_preview"]("howard", "Casual")["id"], preview["id"])

    def test_delayed_reply_is_delivered_once_after_day_changes(self):
        engine = self.runtime
        line = engine["phone_preview"]("editore", "Casual")
        engine["phone_select"]("editore", line)
        self.assertEqual(len(engine["chat_log"]["editore"]), 1)
        self.assertFalse(engine["phone_pending"]("editore"))
        engine["giorno"] += 1
        self.assertTrue(engine["phone_pending"]("editore"))
        self.assertTrue(engine["phone_pending"]("editore"))
        self.assertEqual(len(engine["chat_log"]["editore"]), 2)


    def test_topics_require_the_event_even_after_its_day(self):
        engine = self.runtime
        engine["giorno"] = 19
        facts = set()
        engine["fatto"] = facts.__contains__

        def topic_ids(contact):
            return {line["id"] for line in engine["phone_available"](contact, "topic")}

        self.assertNotIn("simon-cables", topic_ids("simon"))
        self.assertNotIn("ex-dance", topic_ids("ex"))
        facts.update(("phone_d15_gym_squad", "jacob_tornato"))
        self.assertIn("simon-training", topic_ids("simon"))
        self.assertNotIn("simon-cables", topic_ids("simon"))
        self.assertIn("ex-lantern", topic_ids("ex"))
        self.assertNotIn("ex-dance", topic_ids("ex"))
        facts.update(("phone_d15_simon_cables", "ep2_d19_ballo_jacob"))
        self.assertIn("simon-cables", topic_ids("simon"))
        self.assertIn("ex-dance", topic_ids("ex"))

    def test_all_playable_topics_have_an_event_recorded_in_the_story(self):
        game = MODULE.parents[1]
        story = "\n".join(
            path.read_text(encoding="utf-8-sig")
            for folder in ("episodio1", "episodio2", "percorsi")
            for path in (game / folder).glob("*.rpy")
        )
        topics = [
            line for line in self.runtime["PHONE_LINES"]
            if line["mode"] == "topic" and line["day"] <= 19
        ]
        for line in topics:
            with self.subTest(topic=line["id"]):
                self.assertTrue(line["requires"])
                for fact in line["requires"]:
                    self.assertTrue('segna("' + fact + '"' in story, f"Missing story fact {fact}")


    def test_advanced_topics_follow_the_first_answer_and_resume(self):
        engine = self.runtime
        engine["giorno"] = 19
        facts = set()
        engine["fatto"] = facts.__contains__
        for contact, topic, fact in (
            ("daniel", "daniel-seen-happy", "ep2_d18_ragazzina"),
            ("howard", "howard-sauce-stain", "ep2_d18_cena_reggiseno"),
            ("amica", "amica-private-confidence", "ep2_d19_fantasia_joanie"),
            ("capa", "capa-chapter-advice", "barbara_missione_02_fatta"),
        ):
            with self.subTest(topic=topic):
                available = lambda: {
                    line["id"]: line for line in engine["phone_available"](contact, "topic")
                }
                self.assertNotIn(topic, available())
                facts.add(fact)
                line = available()[topic]
                engine["phone_select"](contact, line)
                self.assertEqual(engine["phone_pending"](contact), line["choices"])
                engine["phone_advance"](contact, 1)
                engine["giorno"] += 1
                self.assertNotEqual(line["followups"][0], line["followups"][1])
                choices = engine["phone_pending"](contact)
                self.assertEqual(choices, line["followups"][1])
                engine["phone_advance"](contact, 0)
                self.assertEqual(engine["chat_log"][contact][-1], (contact, choices[0][1]))
                self.assertFalse(engine["phone_pending"](contact))
                self.assertNotIn(topic, available())


    def test_generic_pool_offers_multiple_casual_and_friendly_conversations_per_contact(self):
        engine = self.runtime
        engine["giorno"] = 19
        for contact in ("howard", "ex", "amica", "daniel", "capa", "editore", "simon", "amico"):
            with self.subTest(contact=contact):
                lines = engine["phone_available"](contact, "register")
                for register in ("Casual", "Friendly"):
                    openings = {line["opening"] for line in lines if line["name"] == register}
                    self.assertGreaterEqual(len(openings), 2)
                self.assertTrue(all(line["name"] not in ("Romantic", "Sexy") for line in lines))

    def test_later_generic_lines_do_not_enter_the_pool_early(self):
        engine = self.runtime
        ids = lambda: {line["id"] for line in engine["phone_available"]("amico", "register")}
        self.assertNotIn("amico-register-wrong-turn", ids())
        engine["giorno"] = 17
        self.assertIn("amico-register-wrong-turn", ids())


    def test_generic_pool_outlasts_the_playable_phone_sessions(self):
        engine = self.runtime
        engine["giorno"] = 19
        for contact in ("howard", "ex", "amica", "daniel", "capa", "editore", "simon", "amico"):
            with self.subTest(contact=contact):
                lines = engine["phone_available"](contact, "register")
                counts = {register: sum(line["name"] == register for line in lines)
                          for register in ("Casual", "Friendly", "Flirt")}
                casual_minimum = 4 if contact in ("ex", "daniel") else 6
                self.assertGreaterEqual(counts["Casual"], casual_minimum)
                self.assertGreaterEqual(counts["Friendly"], 4)
                if contact in ("ex", "daniel", "simon"):
                    self.assertGreaterEqual(counts["Flirt"], 4)

        engine["giorno"] = 14
        for mode in ["Casual", "Friendly"]:
            self.assertIsNotNone(engine["phone_preview"]("amica", mode))


    def test_flirt_and_sexy_are_authored_and_unlock_separately(self):
        engine = self.runtime
        engine["giorno"] = 60
        facts = {"darius_romantic_opt_in"}
        engine["fatto"] = facts.__contains__
        for contact in ("howard", "ex", "amica", "daniel", "capa", "editore", "simon", "amico"):
            with self.subTest(contact=contact):
                def count(register):
                    return sum(line["name"] == register
                               for line in engine["phone_available"](contact, "register"))

                engine["valore_interest"] = lambda _: 15
                self.assertEqual(count("Flirt"), 0)
                self.assertEqual(count("Sexy"), 0)
                engine["valore_interest"] = lambda _: 16
                self.assertGreaterEqual(count("Flirt"), 4)
                self.assertEqual(count("Sexy"), 0)
                engine["phone_kisses"].add(contact)
                engine["valore_interest"] = lambda _: 0
                self.assertEqual(count("Sexy"), 2)

        facts.clear()
        engine["valore_interest"] = lambda _: 100
        self.assertFalse(any(line["name"] == "Flirt"
                             for line in engine["phone_available"]("amico", "register")))


    def test_josh_uses_the_existing_chat_without_joining_the_route_rubrica(self):
        engine = self.runtime
        engine["contatti"] = lambda: ["amica", "simon"]
        self.assertEqual(engine["telefono_nuovi_contatti"](), ["josh", "amica", "simon"])
        engine["chat_log"]["josh"] = [("josh", "Love you!")]
        line = engine["phone_preview"]("josh", "Casual")
        engine["phone_select"]("josh", line)
        self.assertEqual(engine["chat_log"]["josh"][0], ("josh", "Love you!"))
        self.assertEqual(engine["chat_log"]["josh"][-1], ("josh", line["reply"]))

    def test_josh_topics_follow_disclosures_and_sexy_requires_a_kiss(self):
        engine = self.runtime
        engine["giorno"] = 19
        facts = set()
        engine["fatto"] = facts.__contains__

        def ids(mode):
            return {line["id"] for line in engine["phone_available"]("josh", mode)}

        self.assertNotIn("josh-daniel-lunch", ids("topic"))
        self.assertNotIn("josh-draft-boundary", ids("topic"))
        self.assertNotIn("josh-register-goodnight", ids("register"))
        facts.add("ep2_d18_josh_avvisato")
        self.assertNotIn("josh-daniel-lunch", ids("topic"))
        facts.update(("ep2_d18_pranzo_daniel", "ep2_d15_litigio_josh", "ep1_d7_iniziativa"))
        self.assertIn("josh-daniel-lunch", ids("topic"))
        self.assertIn("josh-draft-boundary", ids("topic"))
        self.assertIn("josh-register-goodnight", ids("register"))


if __name__ == "__main__":
    unittest.main()
