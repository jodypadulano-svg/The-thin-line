## Giorno 23 · martedì. L'inchiesta si apre soltanto al giorno 22.
## Le CG mancanti usano il segnaposto di cg().
## Effetti approvati da Jody il 27/11: Magnus +2 e Conf +2 al responso, Josh +1 a cena, Conf +1 per la pista
## dell'inchiesta e per Scorpione, Simon +2 se invitato in palestra, Howard +1 se Sara si offre,
## +1 al contatto invitato al telefono. Niente Corruption: la dà l'uscita del 24.

default ep2_d24_appuntamento = None
default redazione_prossimo_evento = 0
default redazione_ultimo_tiro = 0

image bg commissariato = Solid("#26303b")

define REDAZIONE_EVENTI = ("redazione_evento_oroscopo",)

label ep2_d23:
    call nuovo_giorno(23, "In the Margins")
    $ fascia_corrente = FASCE.index("lavoro")
    call ep2_d23_redazione
    if fatto("ep2_d21_jacob_mercoledi"):
        $ ep2_d24_appuntamento = "ex"
    call barbara_convocazione
    if fatto("ep2_d22_inchiesta_accettata"):
        call ep2_d23_inchiesta
    else:
        call ep2_d23_lavoro_ordinario
        call redazione_evento_ordinario
        $ via_cg()

    $ fascia_corrente = FASCE.index("pranzo")
    call ep2_d23_magnus
    $ fascia_corrente = FASCE.index("lavoro")
    call ep2_d23_pomeriggio
    $ fascia_corrente = FASCE.index("sera")
    call ep2_d23_palestra
    call ep2_d23_rientro
    call ep2_d23_cena

    $ fascia_corrente = FASCE.index("notte")
    if ep2_d24_appuntamento is None:
        call ep2_d23_telefono
    $ via_cg()
    $ ambiente(None)
    $ musica(None)
    $ luogo_corrente = ""
    scene bg nero with fade
    return

label ep2_d23_redazione:
    $ vai("redazione", "The newsroom — Tuesday, 9 a.m.")
    $ musica("redazione")
    $ ambiente("redazione")
    $ cg("Sara at her newsroom desk, taking off her coat; Roberta passes with two mugs. Frame from the shoulders up, keeping Sara's blouse out of shot.", "images/cg/ep2/d23_a1_redazione.webp")
    ro "Tea. I remembered which one was yours this time."
    s "What happened last time?"
    ro "You drank mine. You were very polite about it."
    if fatto("ep2_d22_scollatura_domani"):
        n "When Roberta turns away, Sara runs her thumb over the button she left open. It stays open."
    elif fatto("ep2_d22_abito_solito"):
        sp "The cardigan again. At least Roberta knows how I take my tea."
    if fatto("ep2_d22_targa"):
        n "Sara takes the mug with both hands. The receipt is still in the zipped pocket of her bag."
    elif fatto("ep2_d22_inchiesta_rifiutata"):
        n "Barbara's door is open. Sara can see the top drawer from here, if she leans. She opens the proofs instead."
    $ via_cg()
    return

label ep2_d23_lavoro_ordinario:
    $ vai("redazione", "The newsroom — Tuesday morning")
    $ musica("redazione")
    $ cg("Close-up of Sara's pencil moving down a column of local listings, her mug leaving a ring on the desk", "images/cg/ep2/d23_a3_lavoro.webp")
    n "The library has changed its opening hours again. Sara has three emails about it, each more certain than the last, each giving a different time."
    s "Roberta? What time does the library open?"
    ro "Which branch?"
    n "Sara looks back at the emails. For the first time that morning, all three of them make sense."
    $ via_cg()
    return

label redazione_evento_ordinario:
    if redazione_ultimo_tiro == giorno or redazione_prossimo_evento >= len(REDAZIONE_EVENTI):
        return
    $ redazione_ultimo_tiro = giorno
    if renpy.random.random() < 0.25:
        call expression REDAZIONE_EVENTI[redazione_prossimo_evento]
        $ redazione_prossimo_evento += 1
    return

label redazione_evento_oroscopo:
    $ vai("redazione", "The newsroom — Morning proofs")
    $ musica("redazione")
    $ cg("Overhead close-up of a horoscope proof, two identical lines circled in Sara's pencil, and Roberta's hand holding the edge flat", "images/cg/ep2/d23_a2_oroscopo.webp")
    $ suono("d23_pagina_bozze")
    n "Scorpio and Libra have been advised to leave a difficult conversation until after lunch. Word for word. Even the comma is in the same place."
    s "Can two signs have the same Tuesday?"
    ro "Only if one of them's prepared to pay for it."
    $ via_cg()
    $ cg("Roberta looking up from the proofs as she realises why Sara wants to keep the prediction, Sara's clothes out of frame", "images/cg/ep2/d23_a4_roberta.webp")
    s "I rather like this one."
    ro "What's your birthday again?"
    s "Eleventh of November."
    ro "You'd better give it to Libra, then. Think what people would say."
    menu:
        "Leave it with Scorpio.":
            $ confidence(1, "Sara kept the good horoscope for herself.")
            s "I'm keeping it. I have a difficult conversation at lunch."
            ro "Then you'd better eat first. It's there in black and white."
        "Give it to Libra.":
            s "Libra can have it. I'll take my chances."
            ro "That's the spirit. What are you giving Scorpio?"
            s "Something about checking the small print."
    $ via_cg()
    return

label ep2_d23_inchiesta:
    $ vai("redazione", "The newsroom — Before lunch")
    $ ambiente("redazione")
    $ musica("inchiesta")
    $ cg("Sara's notebook open beside her bag; a corner of the folded supermarket receipt just visible in the zipped pocket", "images/cg/ep2/d23_b1_taccuino.webp")
    if fatto("ep2_d22_dawn_fiducia"):
        sp "A shop with her name over the door. I keep seeing the sign, and I don't even know what it said."
    elif fatto("ep2_d22_dawn_fatti"):
        sp "She saw something. I keep writing those three words as if a fourth might come."
    menu:
        sp "I've got time for one thing before lunch. What can I actually check?"
        "Trace the newspaper brief in the archive.":
            call ep2_d23_archivio
        "Ask at the police station.":
            call ep2_d23_commissariato
        "Try the supermarket on the receipt." if fatto("ep2_d22_targa"):
            call ep2_d23_supermercato
    $ confidence(1, "Sara followed a lead on her own.")
    return

label ep2_d23_archivio:
    $ vai("redazione", "The newspaper archive — Tuesday morning")
    $ musica("inchiesta")
    $ cg("Sara's hands sorting a press clipping and its source sheet under a desk lamp, address out of focus", "images/cg/ep2/d23_b2_archivio.webp")
    $ suono("d23_pagina_bozze")
    n "Page nineteen. Under the weather. Four lines in a typeface that gets smaller the longer she looks at it."
    sp "There's no name on the page. Look for the words they did print."
    n "She finds the source sheet behind the proofs for that edition. The wording is almost identical, down to the woman's age."
    $ via_cg()
    $ cg("Close-up of Sara's pencil stopping beneath the line omitted from the newspaper brief", "images/cg/ep2/d23_b5_riga_omessa.webp")
    n "One line didn't make the paper. It gives the address where the body was found."
    sp "That's somewhere I could go. It doesn't tell me where she got into the car."
    $ segna("ep2_d23_nadia_luogo_ritrovamento")
    $ via_cg()
    return

label ep2_d23_commissariato:
    $ vai("commissariato", "Police station — Press desk")
    $ ambiente(None)
    $ musica("inchiesta")
    $ cg("Wide view of the police station waiting room, with Sara standing at the press counter in her closed coat", "images/cg/ep2/d23_b3_commissariato.webp")
    s "I'm checking a short item we ran. Nadia Reyes, twenty-six. What did you release when the case was closed?"
    $ via_cg()
    $ cg("Close view of Sara asking about Nadia at the press counter, with the clerk's hands and the sheet visible below the glass", "images/cg/ep2/d23_b3b_commissariato_vicino.webp")
    n "The clerk asks for the spelling. Sara gives it twice. Behind the glass, a printer pulls in a sheet of paper and waits."
    $ via_cg()
    $ cg("Reverse angle on the press officer behind the counter, with only Sara's notebook in the foreground", "images/cg/ep2/d23_b6_addetto.webp")
    "Press officer" "This is the statement we issued at the time. You can take a copy."
    s "Was there a follow-up?"
    "Press officer" "That's the release I have for you."
    $ via_cg()
    $ cg("Close-up of the freshly printed statement by the printer tray, Sara's hand reaching for the sheet", "images/cg/ep2/d23_b7_comunicato.webp")
    n "Sara puts the statement in her notebook and leaves the zipped pocket alone. This gives her a version she can check against the letter."
    $ segna("ep2_d23_nadia_versione_ufficiale")
    $ via_cg()
    return

label ep2_d23_supermercato:
    $ vai("negozio", "The supermarket — Tuesday morning")
    $ ambiente(None)
    $ musica("inchiesta")
    $ cg("Sara's hand with the printed face of a supermarket receipt at the customer-service counter, the pencilled reverse hidden", "images/cg/ep2/d23_b4_supermercato.webp")
    s "Do you remember a big dark car outside? It might have stopped by the corner."
    "Shop assistant" "The corner by the deliveries?"
    s "I don't know. I was hoping you might."
    "Shop assistant" "Sorry, love. I'm looking at the tills most of the day."
    n "The assistant goes back to a roll of returns stickers. Sara folds the receipt along its old crease. Dawn wrote on the back of what she had."
    $ segna("ep2_d23_nadia_supermercato")
    $ via_cg()
    return

label ep2_d23_magnus:
    $ vai("casa_editrice", "The publishing house — Lunch")
    $ ambiente(None)
    $ musica("magnus")
    $ cg("Magnus facing Sara across the low table at the publishing house, the stack of fifty pages between them; Sara seen from behind above the shoulders", "images/cg/ep2/d23_c1_magnus.webp")
    ed "I'd like to read the rest."
    $ via_cg()
    $ cg("Close-up of Sara's face as Magnus's words register, her cup just entering the frame", "images/cg/ep2/d23_c3_sara.webp")
    s "The rest of what?"
    ed "The book, Sara."
    n "She puts down the cup. She hasn't taken a sip yet."
    if fatto("ep2_d20_magnus_migliora"):
        ed "You came here on Saturday wanting to know what to change. There'll be plenty. I thought I'd tell you this first."
    elif fatto("ep2_d20_magnus_ascolta"):
        ed "On Saturday you let me talk for far too long. I should have said that before I let you go."
    s "When you asked which of them it was about, I went home and tried to answer. I got as far as putting both names at the top of a page."
    ed "And then?"
    s "I was annoyed. She'd done all the work and I'd put their names on it."
    $ via_cg()
    $ cg("Close reverse angle on Magnus listening, one hand turning the stack back towards Sara", "images/cg/ep2/d23_c2_magnus_controcampo.webp")
    ed "That's a better answer than either name."
    s "You could have told me that on Saturday."
    ed "I could have told you what I thought. You've just told me what you think."
    s "So what would you change?"
    ed "Read the last page aloud. There's a point where she stops sounding like herself. I think you'll hear it."
    s "And if I like it the way it is?"
    ed "Then leave it. But read it out loud first."
    n "He rests a finger on the papers until she takes them. This time she picks up the cup, too."
    $ segna("ep2_d23_magnus_responso")
    $ interest("editore", 2, "Magnus wants to read the rest.")
    $ confidence(2, "Magnus wants to read the whole book.")
    $ via_cg()
    return

label ep2_d23_pomeriggio:
    $ vai("redazione", "The newsroom — Tuesday afternoon")
    $ musica("redazione")
    $ ambiente("redazione")
    $ cg("Editorial proofs on Sara's desk in afternoon light, with Magnus's pages tucked under the edge of the pile", "images/cg/ep2/d23_d1_pomeriggio.webp")
    n "Back at her desk, Sara changes {i}will take place{/i} to {i}takes place{/i} seven times. She leaves the eighth one. The sentence has earned a little furniture."
    if fatto("ep2_d23_nadia_luogo_ritrovamento"):
        n "Before she packs up, she checks the address she copied against the source sheet. She got the number right."
    elif fatto("ep2_d23_nadia_versione_ufficiale"):
        n "The police statement goes in a separate pocket from the receipt. She wants to remember which came from whom."
    elif fatto("ep2_d23_nadia_supermercato"):
        n "She unfolds the receipt again. On the back, the ink is exactly where it was this morning."
    $ via_cg()
    return

label ep2_d23_palestra:
    $ vai("palestra", "The gym — After work")
    $ ambiente("palestra")
    $ musica("palestra")
    $ cg("Sara in training clothes at the bench, Simon returning a small weight to the rack beside her", "images/cg/ep2/d23_e1_palestra.webp")
    si "How many?"
    s "Eight."
    if fatto("ep2_d20_palestra"):
        si "You said eight on Saturday and did nine."
        s "I know. It took me two days to be able to take my coat off."
    else:
        si "Eight. You sound very sure."
        s "I'd like to be able to take my coat off tomorrow."
    si "Eight it is. I'm very easily persuaded by medical evidence."
    if fatto("ep2_d19_sa_di_simon"):
        n "A message lights up his phone. He turns it over before she's read the name. Sara notices he noticed her noticing."
    $ via_cg()
    $ cg("Sara finishing the eighth repetition, with Simon beside the head of the bench ready to catch the bar", "images/cg/ep2/d23_e3_ultima_ripetizione.webp")
    n "On eight he catches the bar as she guides it back. He waits for her to sit up before he moves away."
    if ep2_d24_appuntamento is None and valore_interest("simon") >= 16 and not percorso("simon").chiuso:
        $ via_cg()
        $ cg("Simon at the end of the bench with Sara's water bottle held out to her", "images/cg/ep2/d23_e2_simon_controcampo.webp")
        menu:
            sp "Tomorrow there's a whole evening. I could ask him now."
            "Ask Simon if he's free tomorrow.":
                s "Do you do anything on Wednesdays that doesn't involve telling people to breathe?"
                si "Sometimes I eat. Does that count?"
                s "It would if you did it with me."
                si "Yeah. Tomorrow? I'd like that."
                $ ep2_d24_appuntamento = "simon"
                $ interest("simon", 2, "Sara asked him out for Wednesday.")
            "Leave it there.":
                s "Thanks for stopping at eight."
                si "Any time. You can ask for seven, you know."
    $ via_cg()
    $ ambiente(None)
    return

label ep2_d23_rientro:
    if valore_interest("howard") <= 50 or percorso("howard").chiuso:
        return
    $ vai("pianerottolo", "The landing — After the gym")
    $ musica("casa")
    $ cg("Howard at his open front door as Sara comes up the stairs with her gym bag", "images/cg/ep2/d23_f1_howard.webp")
    ho "Evening, Sara."
    s "Evening, Howard."
    menu:
        sp "He's in. I have time before dinner if I want to stop."
        "Offer to help Howard.":
            $ interest("howard", 1, "Sara offered to help.")
            $ via_cg()
            call howard_faccende_dopo_lavoro(True, True, False, alla_porta=True)
            if not _return:
                ho "That's kind. But I'm all right tonight. Go and have your dinner."
        "Go home.":
            $ via_cg()
    return

label ep2_d23_cena:
    $ vai("casa", "Home — Tuesday evening")
    $ musica("casa")
    $ cg("Josh with two plates at the kitchen table and his folded character sheet by the salt; Sara's chair in the foreground", "images/cg/ep2/d23_g1_cena.webp")
    c "I told Mark I'd bring something tomorrow. How many people does a packet of biscuits feed?"
    s "Four people. One dwarf."
    c "Good. I'll get two."
    if fatto("ep2_d22_consola_josh"):
        c "I remembered what you said. About missing me a reasonable amount."
        s "I'll set a timer."
    elif fatto("ep2_d22_josh_dnd"):
        c "You were quiet when I said I'd go."
        s "I was thinking about other things. I'm glad you're going."
    c "How was the book?"
    s "He wants to read the rest."
    $ via_cg()
    $ cg("Reverse angle on Josh at dinner, his fork halfway up as he answers with quiet certainty", "images/cg/ep2/d23_g2_josh.webp")
    c "Of course he does."
    n "He says it with his mouth full, as if it's the least surprising thing either of them has said all evening."
    $ interest("josh", 1, "He never doubted it.")
    $ via_cg()
    return

label ep2_d23_telefono:
    $ vai("camera", "Home — Tuesday night")
    $ musica("notte")
    $ cg("Sara on the edge of the bed with her phone in both hands, the bedside lamp picking out the screen", "images/cg/ep2/d23_h1_telefono.webp")
    menu:
        sp "If I want to ask someone about tomorrow, this is a good moment."
        "Text Joanie." if "amica" in contatti() and valore_interest("amica") >= 12:
            call ep2_d23_invito("amica", "Are you free for a bit tomorrow evening?", "Yes. Let me know when you're coming.")
        "Text Darius." if "amico" in contatti() and valore_interest("amico") >= 12:
            call ep2_d23_invito("amico", "Do you fancy a coffee tomorrow evening?", "I'd like that. I'll even let you pick the biscuits.")
        "Text Daniel." if "daniel" in contatti() and valore_interest("daniel") >= 24:
            call ep2_d23_invito("daniel", "Would you like to go out tomorrow evening?", "Yes. I'll see you tomorrow.")
        "Text Howard." if "howard" in contatti() and valore_interest("howard") >= 14:
            call ep2_d23_invito("howard", "Would it be all right if I came round tomorrow evening?", "Of course. Come to mine.")
        "Put the phone down.":
            n "She leaves the phone face down beside the lamp."
    $ via_cg()
    return

label ep2_d23_invito(contatto, invito, risposta):
    $ ep2_d24_appuntamento = contatto
    $ interest(contatto, 1, "Sara invited them for Wednesday.")
    $ chat_aperta = contatto
    show screen telefono_chat(contatto)
    $ msg("sara", invito, premia_avvio=False)
    $ via_cg()
    $ cg("Close-up of the light from the phone on Sara's fingers at the moment the reply arrives, the chat overlay supplying the text", "images/cg/ep2/d23_h2_risposta.webp")
    $ msg(contatto, risposta, premia_avvio=False)
    hide screen telefono_chat
    $ chat_aperta = None
    if contatto == "daniel":
        $ via_cg()
        $ cg("Sara's excited expression as she reads Daniel's reply", "images/cg/ep2/d23_h3_risposta_daniel.webp")
        pause
    return
