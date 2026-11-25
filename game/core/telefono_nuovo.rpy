## Stato salvabile delle conversazioni libere dell'episodio 2.
default phone_open = {}
default phone_used = set()
default phone_previews = {}
default phone_register_day = {}

default phone_kisses = set()
default phone_notebook = {}
default phone_show_register = False
default phone_investigation = False
default phone_reply_due = {}

init python:
    import phone_rules

    def telefono_nuovi_contatti():
        return ["josh"] + contatti()

    def phone_available(contact, mode):
        now = giorno
        kissed = (
            contact in phone_kisses
            or (contact == "capa" and sara_stagista)
            or (contact == "josh" and fatto("ep1_d7_iniziativa"))
        )
        return [
            line for line in PHONE_LINES
            if line["contact"] == contact and line["mode"] == mode
            and line["id"] not in phone_used
            and line["day"] <= now
            and (line["until"] is None or now <= line["until"])
            and all(fatto(fact) for fact in line["requires"])
            and (mode != "register" or (
                phone_register_day.get(contact) != now
                and phone_rules.register_open(line["name"], valore_interest(contact), kissed)
            ))
            and (mode != "investigation" or phone_investigation or fatto("inquiry_accepted"))
        ]

    def phone_preview(contact, register):
        candidates = [line for line in phone_available(contact, "register") if line["name"] == register]
        if not candidates:
            return None
        cached = phone_previews.get((contact, register))
        if cached and cached[0] == giorno:
            for line in candidates:
                if line["id"] == cached[1]:
                    return line
        selected = renpy.random.choice(candidates)
        phone_previews[contact, register] = (giorno, selected["id"])
        return selected

    def phone_message(contact, speaker, message):
        chat_log.setdefault(contact, []).append((speaker, message.replace("{", "{{")))

    def phone_interrupt(contact):
        previous = phone_open.pop(contact, None)
        phone_reply_due.pop(contact, None)
        if previous:
            preceding = chat_log.get(contact, [])
            last = preceding[-1][1] if preceding else ""
            if last.endswith("?"):
                raccordo = "Sorry to leave that hanging. Can I ask you something else?"
            elif last:
                raccordo = "While I have you, there's something else."
            if last:
                phone_message(contact, "sara", raccordo)

    def phone_select(contact, line, question=None):
        if line not in phone_available(contact, line["mode"]):
            return
        phone_interrupt(contact)
        phone_used.add(line["id"])
        if line["mode"] == "register":
            phone_register_day[contact] = giorno
        phone_message(contact, "sara", question or line["opening"])
        phone_open[contact] = (line["id"], 0)
        delay = line.get("delay_days", 0)
        if delay:
            phone_reply_due[contact] = giorno + delay
        else:
            phone_advance(contact)

    def phone_node_choices(line, node):
        if node <= 1:
            return line["choices"]
        return line["followups"][node - 2]

    def phone_advance(contact, answer=None):
        line_id, node = phone_open[contact]
        line = PHONE_BY_ID[line_id]
        if node > 0 and answer is not None:
            text, reply = phone_node_choices(line, node)[answer]
            phone_message(contact, "sara", text)
            phone_message(contact, contact, reply)
            if node == 1 and line.get("followups"):
                phone_open[contact] = (line_id, answer + 2)
            else:
                phone_open.pop(contact)
            return
        phone_message(contact, contact, line["reply"])
        if line["mode"] == "investigation":
            phone_notebook[line_id] = (contact, line["reply"])
        if line["choices"]:
            phone_open[contact] = (line_id, 1)
        else:
            phone_open.pop(contact)

    def phone_receive(contact):
        incoming = phone_available(contact, "incoming")
        if not incoming:
            return
        line = incoming[0]
        if contact in phone_open:
            phone_message(contact, contact, "Sorry to cut across that. There's something I wanted to tell you.")
        phone_open.pop(contact, None)
        phone_reply_due.pop(contact, None)
        phone_used.add(line["id"])
        phone_message(contact, contact, line["opening"])
        if line["choices"]:
            phone_open[contact] = (line["id"], 1)

    def phone_pending(contact):
        active = phone_open.get(contact)
        if active:
            line = PHONE_BY_ID[active[0]]
            if line["until"] is None or giorno <= line["until"]:
                if active[1] == 0:
                    if phone_reply_due.get(contact, giorno) > giorno:
                        return ()
                    phone_reply_due.pop(contact, None)
                    phone_advance(contact)
                    return line["choices"]
                return phone_node_choices(line, active[1])
            phone_open.pop(contact)
            phone_reply_due.pop(contact, None)
        return ()

label telefono_nuovo_sessione(uscita="Put the phone down"):
    $ renpy.stop_skipping()
    while True:
        $ _phone_contacts = [(nome_mittente(k), k) for k in telefono_nuovi_contatti()]
        $ _phone_contacts.append(("Hide response registers" if phone_show_register else "Show response registers", "__registers__"))
        if phone_notebook:
            $ _phone_contacts.append(("Investigation notebook", "__notebook__"))
        $ _phone_contact = renpy.display_menu(_phone_contacts + [(uscita, "__exit__")])
        if _phone_contact == "__exit__":
            return
        if _phone_contact == "__registers__":
            $ phone_show_register = not phone_show_register
        elif _phone_contact == "__notebook__":
            call screen telefono_taccuino
        else:
            call telefono_nuovo_chat(_phone_contact)

label telefono_nuovo_chat(k):
    $ phone_receive(k)
    show screen telefono_chat(k)
    while True:
        $ _phone_choices = phone_pending(k)
        $ _phone_items = [(c[0], ("answer", i)) for i, c in enumerate(_phone_choices)]
        if k in phone_reply_due:
            $ _phone_items.insert(0, ("Waiting for a reply", None))
        $ _phone_registers = dict.fromkeys(line["name"] for line in phone_available(k, "register"))
        $ _phone_items += [(reg, ("register", reg)) for reg in _phone_registers]
        $ _phone_items += [(line["name"], ("topic", line)) for line in phone_available(k, "topic")]
        if phone_show_register and _phone_choices:
            $ _active_register = PHONE_BY_ID[phone_open[k][0]]["name"]
            if PHONE_BY_ID[phone_open[k][0]]["mode"] == "register":
                $ _phone_items = [("({}) {}".format(_active_register, title), action) if action and action[0] == "answer" else (title, action) for title, action in _phone_items]
        if phone_investigation or fatto("inquiry_accepted"):
            $ _phone_items.append(("Ask about the investigation", ("investigate", None)))
        if k in phone_open:
            $ _phone_items.append(("Say goodbye", ("goodbye", None)))
        $ _phone_action, _phone_value = renpy.display_menu(_phone_items + [("Back to contacts", ("back", None))], screen="scelta_telefono")
        if _phone_action == "back":
            hide screen telefono_chat
            return
        if _phone_action == "answer":
            $ phone_advance(k, _phone_value)
        elif _phone_action == "goodbye":
            $ phone_message(k, "sara", "I've got to go. Talk later.")
            $ phone_open.pop(k, None)
            $ phone_reply_due.pop(k, None)
        elif _phone_action == "register":
            $ _phone_line = phone_preview(k, _phone_value)
            if _phone_line:
                $ _phone_confirm = renpy.display_menu([(_phone_line["opening"], True), ("Cancel", False)], screen="scelta_telefono")
                if _phone_confirm:
                    $ phone_select(k, _phone_line)
        elif _phone_action == "topic":
            $ phone_select(k, _phone_value)
        elif _phone_action == "investigate":
            $ _phone_question = renpy.input("What do you want to ask about?", length=150).strip()
            if _phone_question:
                $ _phone_line = next((line for line in phone_available(k, "investigation") if phone_rules.matches_keyword(_phone_question, line["keywords"])), None)
                if _phone_line:
                    $ phone_select(k, _phone_line, _phone_question)
                else:
                    $ phone_interrupt(k)
                    $ phone_message(k, "sara", _phone_question)
                    $ phone_message(k, k, "I don't know anything about that.")






screen telefono_taccuino():
    modal True
    frame:
        align (0.5, 0.5)
        xysize (960, 730)
        padding (36, 30)
        vbox:
            spacing 18
            text "Investigation notebook" style "tel_testo" size 36
            viewport:
                ysize 545
                mousewheel True
                draggable True
                vbox:
                    spacing 22
                    for contact, testimony in phone_notebook.values():
                        text nome_mittente(contact) style "tel_testo" color "#ffb3c1"
                        text testimony style "tel_testo"
            textbutton "Back" action Return()
