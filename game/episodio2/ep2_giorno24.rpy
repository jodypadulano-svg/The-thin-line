## Giorno 24 · mercoledì · «Dice Night». Primo D&D di Josh da Mark (19:30-23:30).
## Blocco 1 (Jody, 27/11/2026): pranzo con Darius, pomeriggio, serata di Josh, rischi del mercoledì,
## romanzo a casa, Jacob (incontro #1, in game/percorsi/jacob_incontri.rpy).
## Blocco 2 (stessa sessione): Simon, Daniel (jazz club), Joanie, Darius, Howard (film, fuori dalla scala).
## Effetti approvati: Darius +1 al pranzo, +2 se Sara gli dà le pagine; romanzo Confidence +1;
## uscita Corruption +1 e segreto nel Diario senza Suspicion; «One more…» +1 al contatto ma
## rientro dopo Josh (Susp +2); Howard la vede uscire al 50% (Interest 5+ tace, sotto lo dice: Susp +3);
## Mark parla al 25% se Joanie non la copre (Susp +2).

default ep2_d24_coperta = False
default ep2_d24_tiri_forzati = {}
default ep2_d24_raccontati = []
default ep2_d24_howard_passi = 0

init python:
    def ep2_d24_tiro(nome, probabilita):
        """Tiro dei rischi del mercoledì. I test possono forzarne l'esito."""
        if nome in store.ep2_d24_tiri_forzati:
            return store.ep2_d24_tiri_forzati[nome]
        return renpy.random.random() < probabilita

label ep2_d24:
    call nuovo_giorno(24, "Dice Night")
    $ fascia_corrente = FASCE.index("lavoro")
    call ep2_d24_mattina
    call barbara_convocazione

    $ fascia_corrente = FASCE.index("pranzo")
    call ep2_d24_darius

    $ fascia_corrente = FASCE.index("lavoro")
    if fatto("ep2_d22_inchiesta_accettata"):
        call ep2_d24_inchiesta
    else:
        call ep2_d24_lavoro_ordinario
        call redazione_evento_ordinario
        $ via_cg()

    $ fascia_corrente = FASCE.index("sera")
    if ep2_d24_appuntamento != "howard":
        call ep2_d24_rientro_lavoro
    call ep2_d24_josh_esce
    if ep2_d24_appuntamento is None:
        call ep2_d24_romanzo
    else:
        call ep2_d24_uscita

    $ fascia_corrente = FASCE.index("notte")
    call ep2_d24_notte
    $ via_cg()
    $ ambiente(None)
    $ musica(None)
    $ luogo_corrente = ""
    scene bg nero with fade
    return


## --- Mattina -----------------------------------------------------------------------------

label ep2_d24_mattina:
    $ vai("redazione", "The newsroom — Wednesday, 9 a.m.")
    $ musica("redazione")
    $ ambiente("redazione")
    $ cg("Sara at her newsroom desk on Wednesday morning, phone face down beside the keyboard, glancing at the clock", "images/cg/ep2/d24_a1_mattina.webp")
    n "Wednesday has a shape before it has started. Work, lunch, work, and then the evening, which is the part she keeps looking at."
    if ep2_d24_appuntamento is None:
        sp "A whole evening with nobody needing anything. Me and the page."
    else:
        sp "Tonight. I haven't said a word to him about it. Not one."
    $ via_cg()
    return


## --- Pranzo · Darius e la passione comune ------------------------------------------------
## Libro inventato: «The Quiet Room». Nessun flirt. Le pagine: flag per il riscontro del 31,
## che deciderà allora se Darius le ha lette davvero.

label ep2_d24_darius:
    $ vai("strada", "The café opposite the newsroom — Lunch")
    $ ambiente("caffe")
    $ musica("darius_caffe")
    $ cg("The café opposite the newsroom at lunchtime: Darius alone at a window table, streetwear, a dog-eared paperback open with pencil notes in the margins; Sara at the counter with a sandwich, spotting him", "images/cg/ep2/d24_b1_darius_libro.webp")
    n "Darius is at the window table with a paperback. He's holding a pencil. He's using it."
    s "Darius. You read."
    dr "Rude. Sit down before you say anything else rude."
    n "The cover says {i}The Quiet Room{/i}. The margins are grey with his handwriting."
    dr "Third time. It's about the rooms people keep shut. Not from other people. From themselves."
    s "That's my whole book."
    dr "Your book's about a door. [nome_compagno] never shuts up about the door."
    s "The door's a room. Sort of. She knows what's behind it and pretends she doesn't."
    $ via_cg()
    $ cg("Darius leaning across the café table, pencil pointing discreetly at a couple at the next table; Sara turning her head to look, trying not to laugh", "images/cg/ep2/d24_b2_gioco.webp")
    dr "Do the thing. The couple behind you. Don't turn round."
    s "What thing?"
    dr "What they're not saying. I do it on the bus. It's the only way to survive the number nine."
    n "Sara looks in the dark of the window instead. A woman stirring a coffee she isn't drinking. A man explaining something with both hands."
    s "She's already decided. He thinks they're still discussing it."
    dr "See, that's annoying. That's what I was going to say."
    n "They go on for the whole sandwich. People, and why they do what they do. Nobody has played this game with her since university."
    $ interest("amico", 1, "Darius and Sara found something they both love.")
    $ via_cg()
    $ cg("Close-up of Sara's hand resting on the folded stack of fifty pages in her open bag, Darius's paperback on the table beside it", "images/cg/ep2/d24_b3_pagine.webp")
    sp "Magnus's fifty pages are in my bag. With his fingerprints on the last one."
    menu:
        sp "He'd read them like that. With a pencil."
        "Give him the fifty pages.":
            $ segna("ep2_d24_darius_pagine")
            $ interest("amico", 2, "Sara trusted Darius with her pages.")
            s "You can tell me what she isn't saying. If you like."
            dr "Seriously?"
            dr "I'll read them properly. With the pencil. You'll hate the pencil."
            s "I'll hate it next Wednesday."
            dr "And don't tell [nome_compagno] I read. It ruins my whole image."
        "Keep them for now.":
            s "When it's ready, you're first. After an editor and a man who reads it for a living."
            dr "Third. Fine. I'm used to being third. I've got two older brothers."
    $ via_cg()
    return


## --- Pomeriggio --------------------------------------------------------------------------
## Inchiesta pochissimo invasiva (Jody, 27/11): una CG e due o tre righe secondo la pista del 23.

label ep2_d24_inchiesta:
    $ vai("redazione", "The newsroom — Wednesday afternoon")
    $ ambiente("redazione")
    $ musica("inchiesta")
    if fatto("ep2_d23_nadia_luogo_ritrovamento"):
        $ cg("A lamppost on a quiet street corner with a bunch of dried flowers tied to it with string, a small unsigned card tucked in; Sara's hand not quite touching it", "images/cg/ep2/d24_c1_lampione.webp")
        n "On the way back from lunch, she takes the long way past the address. Dried flowers on a lamppost, tied with string. A card with no name."
        sp "Somebody still comes here."
        $ segna("ep2_d24_nadia_fiori")
    elif fatto("ep2_d23_nadia_versione_ufficiale"):
        $ cg("The police statement and the anonymous letter side by side on Sara's desk, her pencil resting between two dates", "images/cg/ep2/d24_c2_date.webp")
        n "She lays the police statement next to the letter. Line by line. Everything matches, except the day. One of them is a day late."
        $ segna("ep2_d24_nadia_date")
    elif fatto("ep2_d23_nadia_supermercato"):
        $ cg("View from the newsroom window of dark cars parked along the street, the folded receipt in Sara's hand at the bottom of the frame", "images/cg/ep2/d24_c3_finestra.webp")
        n "From the window she checks the dark cars parked along the street against half a number plate. None of them. She does it twice more before five."
        $ segna("ep2_d24_nadia_auto")
    else:
        $ cg("The anonymous letter on Sara's desk, her pencil resting on it", "images/cg/ep2/d24_c4_lettera.webp")
        n "She reads the letter again. Four lines. They haven't changed."
    $ via_cg()
    return

label ep2_d24_lavoro_ordinario:
    $ vai("redazione", "The newsroom — Wednesday afternoon")
    $ musica("redazione")
    $ ambiente("redazione")
    $ cg("Sara at her desk in late afternoon light, ticking off the last item on a list of corrections, coat already on the back of the chair", "images/cg/ep2/d24_c5_lavoro.webp")
    n "Eleven corrections, one obituary that spells the same name two ways, and a reader who wants to know why the crossword has changed. By five, Sara has answered all of them, and only the crossword man is still unhappy."
    $ via_cg()
    return


## --- Rientro: eventuale faccenda di Howard (non se la sera esce con lui) -----------------

label ep2_d24_rientro_lavoro:
    if valore_interest("howard") <= 50 or percorso("howard").chiuso:
        return
    $ vai("pianerottolo", "The landing — After work")
    $ musica("casa")
    $ cg("Howard at his open front door as Sara comes up the stairs after work, keys in her hand", "images/cg/ep2/d24_d1_howard.webp")
    ho "Evening, Sara."
    s "Evening, Howard."
    menu:
        sp "He's in. I've got an hour before [nome_compagno] goes."
        "Offer to help Howard.":
            $ via_cg()
            call howard_faccende_dopo_lavoro(True, True, False, alla_porta=True)
            if not _return:
                ho "That's kind. But I'm all right tonight. Go on, you've got a look about you."
        "Go home.":
            $ via_cg()
    return


## --- Sera · Josh esce con lo zaino dei dadi ----------------------------------------------

label ep2_d24_josh_esce:
    $ vai("pianerottolo", "Home — 7:10 p.m.")
    $ musica("casa")
    $ cg("Josh at the open wooden front door on the landing, backpack of dice over one shoulder and two packets of biscuits under his arm; Sara leaning on the door frame", "images/cg/ep2/d24_e1_josh_esce.webp")
    $ suono("dadi")
    c "Dice. Sheet. Biscuits. Biscuits."
    s "Two packets."
    c "One's for the dwarf."
    if fatto("ep2_d22_consola_josh"):
        c "I'll miss you a reasonable amount."
        s "Timer's set."
    elif fatto("ep2_d22_irritata_josh"):
        c "I'll be back by half eleven. You won't even notice."
        s "Have fun. Really."
    else:
        c "Half eleven. Don't wait up if you're writing."
    n "He kisses her on the corner of the mouth because his hands are full, and takes the stairs two at a time like a boy let out of school."
    $ via_cg()
    $ cg("Sara alone in the hallway with the front door just closed, the flat quiet behind her", "images/cg/ep2/d24_e2_sola.webp")
    n "The door clicks. The flat makes the sound it makes when there's only one person in it."
    $ via_cg()
    return


## --- Romanzo · Sara resta a casa (Confidence +1) -----------------------------------------

label ep2_d24_romanzo:
    $ vai("casa", "Home — Wednesday evening")
    $ musica("notte")
    $ cg("Sara cross-legged on the sofa with the laptop on her knees and the printed last page in her hand, reading aloud to the empty room; the lamp on", "images/cg/ep2/d24_f1_legge.webp")
    if fatto("ep2_d23_magnus_responso"):
        n "Read the last page aloud, Magnus said. So she does, to the sofa cushions and the dark window."
        n "Halfway down, there it is. A sentence that sounds like somebody being careful. Not like her heroine at all."
        sp "That's me. That's me being polite on her behalf."
        n "She deletes it. She writes what the woman would actually say. It's ruder, and shorter, and it's true."
    else:
        n "She reads the last page aloud, to the sofa cushions and the dark window. It sounds better than it reads. Most of it."
    $ via_cg()
    $ cg("Close-up of Sara's face lit by the laptop screen, a small private smile, fingers on the keys", "images/cg/ep2/d24_f2_libera.webp")
    n "By eleven she has four new pages and doesn't hate any of them. She can't remember the last time that happened."
    $ segna("ep2_d24_romanzo")
    $ confidence(1, "Sara spent Wednesday night writing.")
    $ via_cg()
    return


## --- Uscita: copertura, rischi, effetti e scelta del rientro -----------------------------

label ep2_d24_uscita:
    $ _contatto = ep2_d24_appuntamento
    $ ep2_d24_coperta = _contatto == "amica"
    $ vai("camera", "Home — 7:30 p.m.")
    $ musica("notte")
    $ cg("Sara in front of the bedroom mirror putting in an earring, dressed to go out, phone on the dresser", "images/cg/ep2/d24_g1_specchio.webp")
    n "Earrings. Not the good ones. Then the good ones."
    if _contatto not in ("amica", "howard") and "amica" in contatti() and valore_interest("amica") >= 12:
        menu:
            sp "If anyone asks, I could be at Joanie's. If Joanie knew."
            "Text Joanie: «Cover for me tonight?»":
                $ ep2_d24_coperta = True
                $ segna("ep2_d24_joanie_copre")
                $ chat_aperta = "amica"
                show screen telefono_chat("amica")
                $ msg("sara", "Cover for me tonight?", premia_avvio=False)
                $ msg("amica", "OMG. Yes. You're here, we're watching something terrible. Tell me EVERYTHING after", premia_avvio=False)
                hide screen telefono_chat
                $ chat_aperta = None
                n "Three more messages arrive while she's doing her shoes. All of them are just exclamation marks."
            "Leave Joanie out of it.":
                pass
    $ via_cg()

    $ corruption(1, "Sara went out on Wednesday and kept it to herself.")
    $ segreto("ep2_d24_uscita", "Wednesday the 24th: out with {} while {} played D&D.".format(nome_percorso(percorso(_contatto)), nome_compagno), sospetto=0)

    if _contatto != "howard":
        if ep2_d24_tiro("howard", 0.5):
            call ep2_d24_howard_vede
        if not ep2_d24_coperta and ep2_d24_tiro("mark", 0.25):
            $ segna("ep2_d24_mark_parla")

    $ _serata_piena = False
    if _contatto == "ex":
        call jacob_incontro_1
        $ _serata_piena = _return
    else:
        call expression ("ep2_d24_uscita_" + _contatto)
        $ _serata_piena = _return

    if _serata_piena and _contatto != "amica":
        call ep2_d24_tardi(_contatto)
    if _contatto == "ex" and _serata_piena:
        call jacob_incontro_1_saluto
    return

label ep2_d24_howard_vede:
    $ vai("pianerottolo", "The landing — 7:40 p.m.")
    $ cg("Howard in his doorway in his cardigan, watching Sara come out dressed for the evening, his eyes going from her shoes to her face", "images/cg/ep2/d24_g2_howard_vede.webp")
    n "Howard's door is open a hand's width. Then two."
    if valore_interest("howard") >= 5:
        $ segna("ep2_d24_howard_tace")
        ho "Lovely evening for it."
        n "He doesn't ask for what. He looks at her shoes, then at her face, and closes the door very softly, as if they'd agreed on something."
    else:
        $ segna("ep2_d24_howard_dice")
        ho "Off out? On your own?"
        s "Just out."
        n "He nods for a long time after she's gone down the stairs. She can feel it in the back of her neck."
    $ via_cg()
    return

## «One more…» (Jody, 27/11): Interest +1 al contatto, ma Sara rientra dopo Josh.
label ep2_d24_tardi(contatto):
    menu:
        sp "It's nearly eleven. If I go now I'm home before him."
        "«One more…»":
            $ segna("ep2_d24_tardi")
            $ interest(contatto, 1, "Sara stayed a little longer.")
            if contatto == "ex":
                jacob "That's two. I'll count."
        "«I should get back.»":
            pass
    return

## ==========================================================================================
## Blocco 2 (Jody, 27/11/2026). Ogni uscita restituisce True: la serata è piena e il giorno
## offre «One more…» (Joanie esclusa, la sua serata è breve).
## ==========================================================================================

## --- Simon · hamburger sul muretto, la camicia blu -----------------------------------------
## Complimento sincero sulla camicia: Simon +1. Impegno in palestra: «Deal» Simon +2 e flag
## simon_palestra_frequente (dai prossimi giorni la palestra si propone più spesso).

label ep2_d24_uscita_simon:
    $ vai("fiume", "The riverside — 8 p.m.")
    $ ambiente("fiume_sera")
    $ musica("muretto")
    $ cg("Simon waiting on the low river wall in a crisp blue shirt instead of gym clothes, two paper bags of burgers beside him; Sara arriving along the path in the evening light", "images/cg/ep2/d24_s1_camicia.webp")
    n "For a second she walks straight past him. He's wearing a shirt. A blue one, with buttons, ironed by someone who meant it."
    si "Sara. Down here."
    s "You own a shirt."
    si "I own two. This is the good one."
    menu:
        sp "He looks like somebody else. Somebody's brother at a wedding."
        "«It suits you. Really.»":
            $ interest("simon", 1, "Sara liked the blue shirt.")
            s "It suits you. Really. You look like you're about to give a speech."
            si "I nearly did. In the mirror. It went badly."
        "«Who died?»":
            s "Who died?"
            si "My confidence, about four seconds ago. Sit down."
    $ via_cg()
    $ cg("Sara and Simon side by side on the river wall eating burgers out of paper, legs dangling, the water dark behind them", "images/cg/ep2/d24_s2_muretto.webp")
    $ suono("carta_hamburger")
    n "The burgers are enormous and slightly too hot. They eat them anyway, with their legs over the wall, like teenagers who haven't been told off yet."
    s "Why this? The gym. You could do anything, with a shirt like that."
    si "I was the skinny one. All through school. Arms like a coat hanger."
    si "Then a man at the old boxing gym told me I had good shoulders. Just that. Good shoulders. I went every day for a year to find out if he was lying."
    s "Was he?"
    si "Completely. But by then it didn't matter."
    $ via_cg()
    $ cg("Simon turned towards Sara on the wall, serious for once, counting something on his fingers", "images/cg/ep2/d24_s3_impegno.webp")
    si "So. Proposal."
    si "Three times a week. Proper programme. Not the eight-reps-and-a-coffee version. In two months you'd see it. Shoulders, back, legs. Everything."
    s "Everything?"
    si "You've got the frame for it. I'm not saying that to be nice. I say it to about one person a year."
    n "Sara looks at the river so he doesn't see she's pleased. It doesn't work. He's a trainer. He sees everything."
    menu:
        sp "Three times a week. That's a lot of evenings."
        "«Deal. I'll come more often.»":
            $ segna("simon_palestra_frequente")
            $ interest("simon", 2, "Sara promised to train more often.")
            s "Deal. But if I hate it, I'm blaming your shoulders."
            si "My shoulders can take it."
        "«I've got so much on. And I come enough already.»":
            s "I've got so much on. And I come enough already. Honestly."
            si "Fair. The offer stays on the table. Next to the protein bars."
    $ via_cg()
    return True


## --- Daniel · jazz club (aggiornamento 27/11) ----------------------------------------------
## Sara sceglie l'abito (solo con Daniel). Arrivano prima dello spettacolo, flirt; al ritorno dal
## bagno la sedia è presa: il grembo (Daniel +2). Spettacolo in video: la testa sulla spalla
## (Daniel +2) e il video del loro isolamento. Poi, con Corr 40 e Daniel 25, lo sfottò su Josh:
## stare al gioco (Daniel +2, Corr +1) o difenderlo (Josh +1). Con Corr 50 e Daniel 32, la
## provocazione: confessare (Daniel +10). Nessun bacio, nessun'altra escalation. Scelte normali.

label ep2_d24_uscita_daniel:
    call ep2_d24_daniel_abito
    $ vai("locale", "The jazz club — 8:30 p.m.")
    $ ambiente("jazz_club")
    $ musica("jazz_club")
    $ cg("A small elegant jazz club before the show: low lamps, an empty stage with a double bass on its stand, Daniel holding a chair out for Sara at a table near the front", "images/cg/ep2/d24_n1_jazz_arrivo.webp")
    n "The club is half empty, the way places are before something starts. A double bass leans on its stand like it's waiting for a bus."
    da "I like it before. You can hear people deciding what kind of evening it's going to be."
    s "And what kind is it going to be?"
    da "That depends on you. It usually does."
    if fatto("ep2_d24_abito_top"):
        n "His eyes go to the black top once. Only once. He's very good at once."
    $ via_cg()
    $ cg("Daniel and Sara at their small table, two glasses, Sara laughing at something he said, Daniel watching her with open amusement", "images/cg/ep2/d24_n2_flirt.webp")
    da "What would you be doing tonight, if you weren't here?"
    s "Writing. Or pretending to. Eating biscuits over the keyboard."
    da "That sounds like a very small life for a woman who writes like you do."
    s "It's a very nice small life. You'd hate it."
    da "I'd hate it in a week. You'd hate it in a year."
    sp "He says it like a weather forecast. Like he's already checked."
    n "She makes a joke about the tablecloth. He laughs at it, properly, and she realises she's been waiting all evening to hear him do that."
    $ via_cg()

    $ cg("The club now full: Sara coming back from the ladies' room to find an older woman in pearls sitting in her chair, Daniel lounging back with an amused look", "images/cg/ep2/d24_n3_sedia.webp")
    n "When she comes back from the ladies', the club has filled up and her chair has an older lady in it. Pearls. A gin. No intention of moving."
    da "I'm afraid you've been replaced."
    s "Already?"
    da "It's a tough room. But there's a seat."
    n "He pats his knee. Once. As if it were the most reasonable suggestion in the world."
    menu:
        sp "In front of all these people. In front of the pearls."
        "Sit on his knee.":
            $ segna("ep2_d24_grembo")
            $ interest("daniel", 2, "Sara sat on his knee at the jazz club.")
            $ via_cg()
            $ cg("Sara sitting sideways on Daniel's knee at the crowded table, back straight, glass in hand, both talking to the people around them; his hands in plain sight on the armrest", "images/cg/ep2/d24_n4_grembo.webp")
            n "She sits. Very straight, glass in hand, as if this were a perfectly normal chair that happened to breathe."
            n "Daniel goes on talking to the man on his left about a boat. His hands stay on the armrest. That's somehow worse."
            "Lady" "Oh, for heaven's sake. Have it back, dear. I can't bear to watch."
            n "The lady gives her the chair with a look that has seen everything twice. Sara gets up. Her knees are not entirely sure about it."
        "«I'll wait for the chair.»":
            s "I'll wait. I'm sure it'll free up."
            da "I'm sure it will."
            n "He smiles as if he's won anyway. Two minutes later the lady sighs, picks up her gin and gives the chair back."
            "Lady" "Here you are, dear. Life's too short to stand at a jazz club."
    $ via_cg()

    ## Lo spettacolo: video senza dialoghi (se manca, si salta).
    $ cg("The show: a singer at the microphone in a pool of warm light, the band behind her; Sara and Daniel side by side at their table in the dark, faces lit by the stage", "images/cg/ep2/d24_n5_spettacolo.webp")
    $ filmato("images/video/ep2/d24_jazz_spettacolo.webm", stop_music=True)
    n "The lights go down and the singer starts very low, as if she were telling the song a secret."
    menu:
        sp "His shoulder is right there. It would be so easy."
        "Rest her head on his shoulder.":
            $ segna("ep2_d24_spalla")
            $ interest("daniel", 2, "Sara rested her head on his shoulder.")
            call ep2_d24_daniel_incanto
        "Stay where she is.":
            n "She stays upright, her hands round her glass, and lets the music do all the leaning. It's enough. It's almost too much."
            $ suono("applausi_jazz")
    $ via_cg()
    $ cg("Outside the club at night: Daniel holding the car door open for Sara, the club sign glowing behind them (not readable)", "images/cg/ep2/d24_n9_uscita.webp")
    da "I'll drop you at the corner. Not the door. I know how these things work."
    s "Do you? How do they work?"
    da "Slowly. That's the only way they work properly."
    $ via_cg()
    return True

label ep2_d24_daniel_abito:
    $ vai("camera", "Home — 7:35 p.m.")
    $ cg("Sara at the open wardrobe holding up outfits for the evening, the dresser mirror behind her", "images/cg/ep2/d24_n0_armadio.webp")
    menu:
        sp "A jazz club. With Daniel. What on earth do you wear to that?"
        "Joanie's black top again." if fatto("ep2_d17_top_ricevuto"):
            $ segna("ep2_d24_abito_top")
            $ corruption(1, "Sara wore Joanie's sheer top for Daniel again.")
            n "The black top. The two dark circles, the sleeves like smoke. Last time there was a blazer. Tonight there is no blazer."
        "The good grey dress.":
            $ segna("ep2_d24_abito_grigio")
            n "The grey dress. Serious, and then a little more than serious, and she knows it."
        "The dark green dress.":
            $ segna("ep2_d24_abito_verde")
            n "The dark green one. It's never been out of the wardrobe at night. It seems pleased about it."
    $ via_cg()
    return

label ep2_d24_daniel_incanto:
    $ via_cg()
    $ cg("Close-up: Sara's head resting on Daniel's shoulder in the dark of the club, his lips touching her hair, her eyes closed", "images/cg/ep2/d24_n6_capelli.webp")
    n "She doesn't decide to do it. Her head just finds the place, the way a cat finds the one warm patch in a room."
    n "He turns and kisses her hair. Barely. She closes her eyes."
    $ filmato("images/video/ep2/d24_jazz_isolati.webm", stop_music=False)
    $ suono("applausi_jazz")
    n "For a whole song there's nobody else in the club. Then there is. Applause, glasses, the lady in pearls coughing."
    if sara_corruption < 40 or valore_interest("daniel") < 25:
        return
    $ via_cg()
    $ cg("Daniel leaning close to Sara's ear with a wicked half-smile as the applause dies down, her head still near his shoulder", "images/cg/ep2/d24_n7_sfotto.webp")
    da "Do you know what your boyfriend asked me today? Whether a spreadsheet could be too green."
    da "He meant the colour. He'd been worrying about it since Monday."
    menu:
        sp "Poor [nome_compagno]. It's not funny. It's a little bit funny."
        "Stay in the spell and play along.":
            $ segna("ep2_d24_gioco_daniel")
            $ interest("daniel", 2, "Sara laughed along about her boyfriend.")
            $ corruption(1, "Sara played along when Daniel teased her boyfriend.")
            s "What did you tell him?"
            da "That green is the colour of growth. He wrote it down."
            s "He'll have it on a mug by Friday."
            da "Then I'll have to think of something better to say next week."
            n "Daniel smiles. Not at the joke. At her, still leaning on him, still laughing. As if he's seen exactly where she is, and it's where he wanted her to be."
            if sara_corruption >= 50 and valore_interest("daniel") >= 32:
                call ep2_d24_daniel_provocazione
        "Defend [nome_compagno].":
            $ segna("ep2_d24_difende_josh")
            $ interest("josh", 1, "Sara stood up for him.")
            s "He cares about getting things right. Somebody in that office should."
            da "Touché."
            n "He says it lightly. But she's sitting up now, and the song is over, and something that was very warm a minute ago has a draught in it."
    return

label ep2_d24_daniel_provocazione:
    $ via_cg()
    $ cg("Daniel's face very close to Sara's, eyes amused and searching; Sara caught halfway between a laugh and a blush", "images/cg/ep2/d24_n8_provoca.webp")
    da "Shall I tell you what I think?"
    da "I think you like it. Being a bad girl for an evening. Talking about your boyfriend with his boss."
    menu:
        sp "Say no. Say something clever. Say no."
        "Admit it.":
            $ segna("ep2_d24_confessa_daniel")
            $ interest("daniel", 10, "Sara admitted she liked being bad with him.")
            s "...Maybe a little."
            $ via_cg()
            $ cg("Sara curled against Daniel's chest at the club table, her face hidden on his shoulder; his arm round her, chin resting on her hair, a satisfied smile", "images/cg/ep2/d24_n8b_coccole.webp")
            n "She hides her face against his shoulder again. He takes her in as if she'd always fitted there, one arm round her, his chin against her hair."
            da "Good. We're going to have a lot of fun, you and I."
        "Deny it.":
            s "You think a lot of things."
            da "I'm usually right about most of them."
    return


## --- Joanie · serata breve di confidenze ---------------------------------------------------
## Il menu torna finché Sara vuole: ogni confidenza (solo se il fatto è successo davvero)
## Joanie +1 e una riga in «Cosa sa Sara». Joanie si accende per le storie con altri uomini (G2).

label ep2_d24_uscita_amica:
    $ vai("casa_joanie", "Joanie's flat — 8 p.m.")
    $ ambiente(None)
    $ musica("casa")
    $ cg("Joanie's flat: Joanie cross-legged on the sofa with two glasses of wine, patting the cushion beside her; Sara taking off her coat", "images/cg/ep2/d24_j1_divano.webp")
    ch "Sit. Drink. Talk. In that order."
    ch "So. What's new? And don't say nothing, you've got your nothing face on and it's lying."
    $ ep2_d24_raccontati = []
    $ via_cg()
    $ cg("Joanie leaning in, chin on her hand, eyes bright, Sara talking with her glass held to her chest", "images/cg/ep2/d24_j2_confidenze.webp")
    call ep2_d24_joanie_menu
    $ via_cg()
    $ cg("Joanie at her door waving Sara off with her glass, Sara on the stairs smiling back", "images/cg/ep2/d24_j3_saluto.webp")
    ch "Go on, go home before your dwarf does. And next Wednesday, I want more. So much more."
    $ via_cg()
    return True

label ep2_d24_joanie_menu:
    menu:
        sp "What do I tell her?"
        "Daniel. The dance." if fatto("ep2_d18_ballo") and "daniel" not in ep2_d24_raccontati:
            $ ep2_d24_raccontati.append("daniel")
            call ep2_d24_confida("Sara told Joanie about the dance with Daniel.")
            s "Thursday, after lunch. Daniel and I... danced. There was music."
            ch "You DANCED? Sara Collins. Hands where?"
            s "Waist. Mostly."
            ch "Mostly. I'm going to need a diagram."
            jump ep2_d24_joanie_menu
        "Jacob's back." if fatto("jacob_tornato") and "jacob" not in ep2_d24_raccontati:
            $ ep2_d24_raccontati.append("jacob")
            call ep2_d24_confida("Sara talked to Joanie about Jacob coming back.")
            s "Jacob keeps writing. He wants to have a drink. Like friends."
            ch "Like friends. Jacob doesn't know what that word means. That's what's fun about him."
            n "Joanie's eyes are shining in a way Sara decides not to look at too closely."
            jump ep2_d24_joanie_menu
        "The story at work." if fatto("ep2_d22_inchiesta_accettata") and "inchiesta" not in ep2_d24_raccontati:
            $ ep2_d24_raccontati.append("inchiesta")
            call ep2_d24_confida("Sara told Joanie she's looking into a woman's death.")
            s "Barbara gave me something real. A woman who died. Nobody's asking questions."
            ch "So you are. Of course you are. Be careful, yeah? Text me where you go."
            jump ep2_d24_joanie_menu
        "Magnus wants the whole book." if fatto("ep2_d23_magnus_responso") and "magnus" not in ep2_d24_raccontati:
            $ ep2_d24_raccontati.append("magnus")
            call ep2_d24_confida("Sara told Joanie that Magnus wants to read the whole book.")
            s "Magnus wants to read the rest. All of it."
            ch "SARA. That's huge. That's the biggest thing you've said all night and you said it last."
            jump ep2_d24_joanie_menu
        "Lunch with Darius." if "darius" not in ep2_d24_raccontati:
            $ ep2_d24_raccontati.append("darius")
            call ep2_d24_confida("Sara told Joanie about lunch with Darius.")
            s "I had lunch with Darius. He reads. Properly. With a pencil."
            ch "Darius? Our Darius? I've known him six years and he's never shown me a pencil."
            jump ep2_d24_joanie_menu
        "«That's everything.»" if ep2_d24_raccontati:
            s "That's everything. I promise."
            ch "It's never everything. But it's a good start."
        "«Nothing, really. Tell me about you.»" if not ep2_d24_raccontati:
            s "Nothing, really. Tell me about you."
            ch "Liar. But fine. Let me tell you about the man at the bakery."
            n "Joanie talks for twenty minutes. Sara laughs in all the right places and tells her nothing, and Joanie lets her, which is its own kind of present."
    return

label ep2_d24_confida(nota):
    $ interest("amica", 1, "Sara confided in Joanie.")
    $ nota_sara("amica", nota)
    return


## --- Darius · il caffè dei biscotti, poi la via lunga (amichevole, nessuna avance) ----------
## Chiedergli di lui: Darius +1. Abbraccio all'angolo: Darius +1.

label ep2_d24_uscita_amico:
    $ vai("strada", "The café opposite the newsroom — 8 p.m.")
    $ ambiente("caffe")
    $ musica("darius_caffe")
    $ cg("The café opposite the newsroom in the evening, almost empty, Darius at the counter pointing at a jar of biscuits, Sara laughing beside him", "images/cg/ep2/d24_r1_biscotti.webp")
    dr "Twice in one day. People will talk."
    s "What people?"
    dr "Him. The barista. He's already talking. Look at his face."
    n "They choose biscuits like it's a matter of state. Darius wants the ones with jam. Sara wants the ones that don't fall apart. They get both."
    if fatto("ep2_d24_darius_pagine"):
        dr "I've started. Don't ask. Next Wednesday."
        s "I wasn't going to ask."
        dr "You were going to ask with your eyebrows."
    $ via_cg()
    $ cg("Sara and Darius walking the long way home along the river at night, a paper bag of biscuits between them, street lamps on the water", "images/cg/ep2/d24_r2_via_lunga.webp")
    $ ambiente("fiume_sera")
    n "They take the long way home without either of them suggesting it. Along the river, past the boathouse, past the bench where nobody ever sits."
    menu:
        sp "I've known him for years and I've never really asked him anything."
        "Ask him about himself.":
            $ interest("amico", 1, "Sara asked Darius about himself.")
            s "Tell me about the two older brothers."
            dr "One's a lawyer, one's in prison. Mum says it's a balanced portfolio."
            s "Darius."
            dr "Fine. One's a lawyer, one's an accountant. The prison one's more fun to say."
            n "He talks about his mum's kitchen, and the bunk bed he never got the top of. He's funnier about it than it probably was."
        "Talk about the book.":
            s "Can I tell you about the door? The one [nome_compagno] tells everyone about?"
            dr "Please. I want to know if it's as good as he says."
            n "She tells him. He asks three questions, all of them better than she expected."
    $ via_cg()
    $ cg("At the street corner near Sara's building under a lamp, Darius and Sara saying goodbye, Darius handing her the biscuit bag", "images/cg/ep2/d24_r3_angolo.webp")
    dr "This is your corner. I know the rules. Dice night, everybody home by half eleven."
    menu:
        sp "It's been a nice evening. Just nice."
        "Hug him goodbye.":
            $ interest("amico", 1, "Sara hugged Darius goodbye.")
            n "She hugs him. He smells of jam biscuits and cold air, and he pats her back twice, like a brother."
        "Wave and go.":
            n "She waves the biscuit bag at him. He salutes. Very seriously. Then he ruins it by laughing."
    $ via_cg()
    return True


## --- Howard · film sul divano (fuori dalla scala: howard_visite non sale) ------------------
## Tre momenti, Sara pensa sempre «poverino». Howard +1 per ogni momento accettato, +2 per il
## finale; nessuna Corruption. Col Complesso spostarsi è grigio. Il finale è solo suo: finge di
## dormire sul seno di Sara con un sorriso beato (retroscena nel Diario).

label ep2_d24_uscita_howard:
    $ vai("casa_howard", "Howard's flat — 8 p.m.")
    $ ambiente(None)
    $ musica("film_howard")
    $ cg("Howard's sofa in the blue light of an old television: Howard at one end, Sara at the other with a cushion between them, a bowl of crisps on the table", "images/cg/ep2/d24_o1_divano.webp")
    ho "It's an old one. {i}September Rain{/i}. I picked it at random."
    n "On the screen, a young woman meets a man with grey hair at a railway station. He carries her suitcase. She looks at him like he's the station clock."
    s "At random."
    ho "Completely. It was on top of the pile."
    sp "He's probably watched it a hundred times on his own. Poor thing."
    $ ep2_d24_howard_passi = 0
    $ via_cg()
    $ cg("Howard shuffling along the sofa with a tartan blanket, offering to share it with Sara", "images/cg/ep2/d24_o2_coperta.webp")
    ho "These old bones get cold. Would you mind? There's room under here for two."
    menu:
        sp "It's only a blanket."
        "Share the blanket.":
            $ ep2_d24_howard_passi = 1
            $ interest("howard", 1, "Sara shared his blanket.")
            n "He shuffles along. The cushion ends up on the floor. Neither of them picks it up."
            sp "He's freezing, poor man. That flat's never warm."
        "Pass him the blanket and stay put." (rifiuto_howard=True):
            s "You have it. I'm warm enough."
            ho "Of course. Of course."
    if ep2_d24_howard_passi == 1:
        $ via_cg()
        $ cg("Howard's arm stretched along the back of the sofa behind Sara's shoulders, his eyes on the television, Sara watching the film", "images/cg/ep2/d24_o3_braccio.webp")
        n "On the screen, the man with grey hair reads the girl a letter. Howard's arm goes along the back of the sofa, behind her. A long way behind. Then not so long."
        menu:
            sp "He's just stretching. Old men stretch. It means nothing."
            "Let it be.":
                $ ep2_d24_howard_passi = 2
                $ interest("howard", 1, "Sara let his arm stay.")
                sp "Poor thing. He just wants someone on the sofa."
            "Lean forward for the crisps and stay there." (rifiuto_howard=True):
                n "She leans forward for the crisps and stays there, elbows on her knees. The arm waits behind her for the rest of the film."
    if ep2_d24_howard_passi == 2:
        $ via_cg()
        $ cg("Late in the film, Howard slumped against Sara as if asleep, his head sliding down from her shoulder; Sara looking down at him tenderly", "images/cg/ep2/d24_o4_scivola.webp")
        n "Somewhere around the second train, Howard starts to breathe very slowly. His head tips onto her shoulder. Then it slides. It ends up where it ends up."
        menu:
            sp "He's asleep. He's completely worn out, the poor dear."
            "Let him sleep.":
                $ ep2_d24_howard_passi = 3
                $ segna("ep2_d24_howard_dorme")
                $ interest("howard", 2, "Sara let him sleep against her.")
                n "She doesn't move. She strokes his thin hair, very lightly, the way you would a cat that's finally settled."
                $ via_cg()
                $ cg("Close shot: Howard pretending to sleep with his cheek on Sara's chest, a blissful contented smile clearly visible, one eye just open; Sara above him, watching the film, unaware", "images/cg/ep2/d24_o5_finge.webp")
                n "On the screen the girl kisses the man with grey hair at the station. Sara watches it to the end, and doesn't look down."
                $ retroscena("howard", "During the film, Howard wasn't asleep at all. He smiled the whole time.")
            "Ease him back onto the cushion." (rifiuto_howard=True):
                n "She eases him back onto the cushion. He mumbles, and doesn't wake up. Or does a very good job of not waking up."
    $ via_cg()
    $ cg("Howard at his door seeing Sara out onto the landing, the tartan blanket round his shoulders like a cape", "images/cg/ep2/d24_o6_saluto.webp")
    ho "Thank you, Sara. I don't remember the last time I watched one with somebody."
    sp "Poor man. Twenty steps from his door to mine, and he still says goodbye like I'm catching a train."
    $ via_cg()
    return True


## --- Notte · rientro di Josh e domande ---------------------------------------------------

label ep2_d24_notte:
    $ vai("casa", "Home — 11:40 p.m.")
    $ musica("notte")
    if ep2_d24_appuntamento is None:
        $ cg("Josh coming in quietly with the empty backpack, Sara still on the sofa with the laptop, both smiling", "images/cg/ep2/d24_h1_josh_torna.webp")
        c "The dwarf survived. Mostly. Mark's cat ate a d20."
        s "Is that a thing that can happen?"
        c "It is now. How was the book?"
        s "Four pages. I like all of them."
        n "He sits down next to her with his coat still on, and listens to her read the first one. He doesn't understand why she's grinning, and doesn't need to."
        $ via_cg()
        return

    if fatto("ep2_d24_tardi"):
        $ cg("Josh on the sofa in the dark with only the TV light, turning as Sara comes in late with her coat still on", "images/cg/ep2/d24_h2_tardi.webp")
        n "The light's on. [nome_compagno] is on the sofa with the television muted, and he turns before she's closed the door."
        c "Hey. I got back and you weren't here."
        $ suspicion(2, "Sara came home after him.")
    else:
        $ cg("Sara on the sofa in comfortable clothes, hair down, as Josh comes in with the backpack; her shoes hidden under the sofa", "images/cg/ep2/d24_h3_in_tempo.webp")
        n "She's home at ten past eleven. By twenty past, the good earrings are back in the box and her shoes are under the sofa."
        c "The dwarf survived. Mostly. Mark's cat ate a d20."
        s "Is that a thing that can happen?"
        c "It is now."

    if fatto("ep2_d24_mark_parla"):
        $ suspicion(2, "Mark mentioned seeing Sara out.")
        c "Funny thing. Mark went out for beers and said he saw you. In town."
    if fatto("ep2_d24_howard_dice"):
        $ suspicion(3, "Howard mentioned that Sara went out.")
        c "And Howard was on the landing. Said you went out. All dressed up, he said."

    if fatto("ep2_d24_tardi") or fatto("ep2_d24_mark_parla") or fatto("ep2_d24_howard_dice"):
        menu:
            sp "Say something. Something boring."
            "«I was at Joanie's.»":
                $ segna("ep2_d24_scusa_joanie")
                s "I was at Joanie's. She's having a crisis about a bathroom tile."
                if ep2_d24_coperta:
                    n "Somewhere across town, Joanie's phone is ready to confirm it. With exclamation marks."
                c "A tile crisis. Right."
            "«Just a walk. I couldn't settle.»":
                $ segna("ep2_d24_scusa_passeggiata")
                s "Just a walk. I couldn't settle. The flat was too quiet."
                c "You should've texted. I'd have come back."
                s "That's why I didn't."
        n "He nods, and yawns, and starts telling her about the dwarf. She laughs in the right places. Some of them she means."
    $ via_cg()
    return
