init python:
    def _test_menu_giorno15(scelte):
        def scegli(items, **kwargs):
            voluta = scelte.pop(0)
            for testo, azione in items:
                if testo == voluta and azione is not None:
                    return getattr(azione, "value", azione)
            raise AssertionError("Missing day 15 choice: " + voluta)
        store.menu = scegli

label test_giorno15:
    call ep2_d15
    $ segna("test_giorno15_finito")
    pause
    return

testsuite giorno15:
    testcase bivi:
        parameter ramo = ["extra", "guided", "decline"]
        $ _test_menu_giorno15(["Keep listening.", "Look down, smiling.", "I'm done for today.", "Let it go."] if ramo == "decline" else ["Pitch a follow-up.", "Play along." if ramo == "guided" else "Ask for one more rep.", "Show me.", "Rack the handles." if ramo == "guided" else "Let him see one more.", "Tell him he had no right to read it."])
        $ _d15_josh = valore_interest("josh")
        $ _d15_simon = valore_interest("simon")
        $ _d15_magnus = valore_interest("editore")
        $ _d15_daniel = valore_interest("daniel")
        $ _d15_conf = sara_confidence
        $ _d15_corr = sara_corruption
        $ _d15_chat_start = len(chat_log.get("daniel", []))
        $ segna("test_giorno15_finito", False)
        $ segna("ep2_d18_pranzo_daniel_confermato", False)
        $ discorso_aperto["daniel"] = {"premio_avvio": True}
        $ telefono_minuti_riprese["daniel"] = "tel_chat_daniel_intro_1"
        $ telefono_minuti_inbox["daniel"] = {"arrivo": 22000, "bolle": 2, "notificata": False}
        run Jump("test_giorno15")
        advance until eval fatto("test_giorno15_finito") timeout 120.0
        assert eval ha_numero("simon") and fatto("ep2_d15_josh_letto_di_nascosto")
        assert eval fatto("ep2_d15_manoscritto_rivisto") and fatto("ep2_pagine_magnus")
        assert eval valore_interest("editore") == _d15_magnus + 1
        assert eval valore_interest("simon") == _d15_simon + (0 if ramo == "decline" else 2)
        assert eval sara_corruption == _d15_corr + {"decline": 0, "guided": 1, "extra": 2}[ramo]
        assert eval sara_confidence == _d15_conf + (-8 if ramo == "decline" else 3)
        assert eval valore_interest("josh") == _d15_josh - (3 if ramo == "decline" else 7)
        assert eval fatto("ep2_d18_pranzo_daniel_confermato") == (ramo != "decline")
        assert eval [m[0] for m in chat_log.get("daniel", [])[_d15_chat_start:]] == ([] if ramo == "decline" else ["sara", "daniel"])
        assert eval valore_interest("daniel") == _d15_daniel and discorso_aperto["daniel"]["premio_avvio"]
        assert eval telefono_minuti_inbox["daniel"]["arrivo"] == 22000 and telefono_minuti_riprese["daniel"] == "tel_chat_daniel_intro_1"
