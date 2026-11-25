## Giorno 20 · sabato (docs/narrative/giorno20-scheda-2026-11-25.md).
## Magnus e la casa editrice, il pomeriggio a scelta (palestra, Joanie, scrivere),
## la cena con Josh. Il responso di Magnus arriva il 23.

init python:
    def d20_abito(nome):
        """Le CG in cui il vestito si vede per intero: grigioverde di Samantha, o blu."""
        colore = "verde" if fatto("ep2_d19_abito_samantha") else "blu"
        return "images/cg/ep2/d20_%s_%s.webp" % (nome, colore)

label ep2_d20:
    call nuovo_giorno(20, "Page Fifty")
    $ fascia_corrente = FASCE.index("mattina")
    call ep2_d20_vestito
    call ep2_d20_casa_editrice
    call ep2_d20_messaggio
    $ fascia_corrente = FASCE.index("pranzo")
    call ep2_d20_pomeriggio
    $ fascia_corrente = FASCE.index("sera")
    call ep2_d20_cena
    $ fascia_corrente = FASCE.index("notte")
    call ep2_d20_notte
    $ musica(None)
    $ luogo_corrente = ""
    scene bg nero with fade
    return


## --- Mattina: il vestito ---------------------------------------------------------------------

label ep2_d20_vestito:
    $ vai("casa", "Home — Saturday, 8:40 a.m.")
    $ musica("casa")
    $ cg("Sara at the hallway mirror in her dress; behind her Josh with a cardboard shield and a paintbrush", d20_abito("a1_specchio"))
    if fatto("ep2_d19_abito_samantha"):
        n "The grey-green dress has no zip and no opinion. Twice she forgets she's wearing it, and looks down to check."
    elif fatto("ep2_d19_abito_suo"):
        n "The blue is the one she'd have picked. She's picked it. It still surprises her, in the mirror, to be the person who did."
    else:
        n "«Wear something you can forget you're wearing.» She's had four things on. The one she's kept is the blue, from the back of the wardrobe, that she'd been saving for something without knowing what."
    n "[nome_compagno] comes out of the kitchen with a paintbrush in one hand and a cardboard shield in the other, and stops."
    c "Wow. Okay. Is it bad luck to say you look like an author?"
    s "It's only a chat. He might have hated it."
    c "He asked you in on a Saturday. People don't come in on a Saturday to hate something."
    if fatto("ep2_d15_litigio_josh"):
        n "He doesn't ask about the pages. He's been not asking since Monday, carefully, like a man carrying a full glass."
    menu:
        sp "He's got green paint on his chin. He wants to say the right thing so badly."
        "«Wish me luck.»":
            $ interest("josh", 1, "Sara let him be part of it.")
            s "Wish me luck."
            c "Luck. All of it. I'll manage without, I've got a shield."
        "«I'll tell you about it tonight.»":
            s "I'll tell you about it tonight."
            c "Tonight. I booked the place with the candles in bottles. I even ironed something."
    $ via_cg()
    $ cg("Josh kissing Sara's cheek in the hallway, a smear of green paint on her ear", d20_abito("a2_bacio"))
    n "He kisses her on the cheek so as not to spoil her mouth, and gets green paint on her ear."
    $ via_cg()
    return


## --- La casa editrice ------------------------------------------------------------------------
## Magnus ha letto le pagine due volte e non dice se sono buone: il responso è del 23.
## Non seduce: ascolta. Il segreto di Samantha non si rivela.

label ep2_d20_casa_editrice:
    $ vai("casa_editrice", "The publishing house — 10 a.m.")
    $ musica(None)
    $ musica("magnus")
    $ cg("Sara at the door of a tall narrow house with a worn brass plate", d20_abito("b1_portone"))
    n "It isn't what she expected. No glass, no lobby. A tall thin house with a brass plate so often polished that the name's nearly gone."
    n "She rubs at her ear with her thumb. It comes away green."
    $ via_cg()
    $ cg("The woman with the silver bob opening the door, smiling as if they were old friends", "images/cg/ep2/d20_b2_bob_argento.webp")
    n "She knows the woman who opens the door. The silver bob. The smile, at the end of the party."
    n "«You were standing beside a door,» the woman says. «I'm glad to see you've come through one.»"
    $ via_cg()
    $ cg("Sara climbing a narrow staircase lined with books to the ceiling", d20_abito("b3_scale"))
    n "The stairs are so narrow that they have to go up one behind the other. There are books all the way. On the third landing somebody's left a cup of tea on Balzac."
    sp "I could turn round. I could be home in half an hour. Nobody would even be cross."
    sp "I'd be cross."
    $ via_cg()

    $ cg("A high room with a window, two armchairs and no desk; fifty printed pages on a low table, the last one face down; Magnus by the fire", "images/cg/ep2/d20_b4_magnus_stanza.webp")
    ed "Sara. Sit wherever you would like to be listened to."
    if fatto("ep2_d19_abito_samantha"):
        n "He gets up to greet her, and for a moment he simply doesn't. He's looking at the dress. Then he is himself again, and holds out his hand."
        sp "Is there paint on it?"
    elif fatto("ep2_d19_abito_suo"):
        ed "Blue. I am always glad when a writer dresses herself."
    else:
        ed "Blue. Good. You have come dressed to sit down."
    n "There are two chairs. One faces the fire. One faces the window, and the whole town. She takes the window."
    n "On the low table between them are her pages. Real paper. The edges aren't straight any more. The last one is lying on its face."
    ed "I have read them. Twice. Once for you, and once for me. I shall not tell you today whether they are good."
    s "...Oh."
    ed "If I told you yes, you would stop listening. If I told you no, you would stop breathing. And I have a question which requires both."
    ed "Your heroine is standing where she can see two men. One is laughing behind the glass. The other has just been told where to meet her tomorrow. And there you leave her."
    $ via_cg()
    $ cg("Close-up of Magnus, page fifty held between two fingers", "images/cg/ep2/d20_b5_pagina_cinquanta.webp")
    n "He turns over the last page. He hasn't written anything on it at all."
    ed "Which of them is it about?"
    sp "Nobody's ever asked me that. I've never asked me that."
    if fatto("ep1_d13_magnus_pagine"):
        ed "You told me, at the party, that she did not want to be found. Not yet. I believed you. But somebody on page fifty has started leaving the lights on."
    menu:
        sp "He's waiting. He looks as if he could wait until it got dark."
        "Listen to him.":
            $ segna("ep2_d20_magnus_ascolta")
            $ interest("editore", 3, "Sara let him go on.")
            $ confidence(2, "Sara didn't fill the silence.")
            $ via_cg()
            $ cg("Sara wiping her eyes in the armchair by the window, Magnus courteously turned to the fire", "images/cg/ep2/d20_b6_ascolta.webp")
            n "She doesn't answer. It's the hardest thing she's done in a chair. She lets him go on."
            ed "It is about neither. It is about the glass. She has spent her life on one side of it, admiring the party. You have written forty-nine pages about a window, and one about a hand on the latch."
            sp "A hand on the latch."
            n "Her eyes are stinging. He has the courtesy to look at the fire until they stop."
        "Ask him how to make it better.":
            $ segna("ep2_d20_magnus_migliora")
            $ interest("editore", 2, "Sara came to work.")
            $ confidence(3, "Sara asked the question she was afraid of.")
            $ via_cg()
            $ cg("Sara bent over the pages with a pencil, Magnus pointing at a line", "images/cg/ep2/d20_b6_migliora.webp")
            s "I don't know yet. How do I make it better?"
            ed "Ah. She has come to work. Good."
            ed "Take out every sentence in which she explains herself. She is always apologising to the reader for wanting something. We did not ask."
            s "That's half the book."
            ed "It is a third. I counted. The other two thirds are alive."
    $ via_cg()
    $ cg("The high window over the town, the pages in the light, the silence of the house", "images/cg/ep2/d20_b7_lettura.webp")
    ed "One thing more, and then I shall give you back your Saturday. The last paragraph. Aloud."
    menu:
        sp "Aloud. In here. With the fire listening."
        "Read it to him.":
            $ segna("ep2_d20_legge_sara")
            $ confidence(1, "Sara read it out loud.")
            n "Her voice is small for a line and a half. After that it's somebody else's, lower, quite sure of where the commas are."
            n "When she stops, the house is very quiet. Two floors down, somebody has stopped typing."
            ed "Thank you. I wanted to know whether you had heard her."
        "Ask him to read it.":
            $ segna("ep2_d20_legge_magnus")
            $ interest("editore", 1, "Sara heard it in his voice.")
            s "You do it. Please. I want to hear it when it isn't me."
            n "He reads it as if he'd found it in a drawer. He makes no face at all. For the first time she hears what the woman is about to do."
            sp "It's indecent. It's really indecent. I wrote that at the kitchen table."
    $ tappa("editore", 2)
    $ nota_sara("editore", "He's read them twice. He wouldn't say if they're good. He asked me which man it's about.")
    $ via_cg()
    $ cg("The woman with the silver bob at the street door, her hand on Sara's arm", "images/cg/ep2/d20_b8_uscita.webp")
    n "«He didn't say yes,» says the woman with the silver bob, on the step."
    s "He didn't say anything."
    n "«He let you have the chair by the window. He's had ministers in the other one.»"
    $ via_cg()

    call inizio_retroscena
    $ cg("Retroscena: Magnus's hand laying page fifty in a drawer, beside an old photograph", "images/cg/ep2/d20_b9_cassetto.webp")
    rs "When the stairs are quiet, Magnus squares the edges of forty-nine pages. The fiftieth he keeps in his hand."
    rs "He opens a drawer. There's a photograph in it already. He lays the page beside it, face up, and doesn't close the drawer straight away."
    if fatto("ep2_d19_abito_samantha"):
        rs "From here only a corner of the photograph shows. A hem. A plain one, grey-green."
        $ retroscena("editore", "Magnus kept page fifty, in a drawer with an old photograph. In it there's a grey-green hem.")
    else:
        $ retroscena("editore", "Magnus kept page fifty. There's an old photograph in the same drawer.")
    call fine_retroscena
    $ via_cg()
    return


## --- Per strada: chi scrive dipende dal pranzo del 18 (chat di trama) -------------------------

label ep2_d20_messaggio:
    $ vai("strada", "The street — 11:50 a.m.")
    $ musica("casa")
    $ cg("Sara on the steps of the publishing house, phone in hand, laughing by herself", d20_abito("c1_gradini"))
    n "She gets as far as the bottom step and sits down on it. Her knees have just heard."
    $ suono("telefono_vibra")
    if fatto("ep2_d18_pranzo_daniel"):
        $ chat_aperta = "daniel"
        show screen telefono_chat("daniel")
        $ msg("daniel", "Well?")
        $ msg("sara", "He asked me a question.", premia_avvio=False)
        $ msg("daniel", "He's never asked me one.")
        if valore_interest("daniel") >= giorno:
            $ msg("daniel", "Lunch. When you've got the answer.")
        hide screen telefono_chat
        $ chat_aperta = None
        sp "He's jealous of a question. I didn't know you could do that to Daniel."
    else:
        $ chat_aperta = "amica"
        show screen telefono_chat("amica")
        $ msg("amica", "ALIVE??")
        $ msg("sara", "He didn't say yes.", premia_avvio=False)
        $ msg("amica", "did he say no")
        $ msg("sara", "No.", premia_avvio=False)
        $ msg("amica", "then WHY are we not screaming")
        hide screen telefono_chat
        $ chat_aperta = None
        n "Sara looks up the street, and down it, and does a very small scream."
    $ via_cg()
    return


## --- Il pomeriggio: tre strade ---------------------------------------------------------------

label ep2_d20_pomeriggio:
    menu:
        sp "The whole afternoon. Nobody needs me till eight."
        "The gym.":
            $ segna("ep2_d20_palestra")
            call ep2_d20_palestra
        "Joanie's.":
            $ segna("ep2_d20_da_joanie")
            call ep2_d20_joanie
        "Home. The book.":
            $ segna("ep2_d20_scrive")
            call ep2_d20_scrivere
    $ via_cg()
    $ ambiente(None)
    return

label ep2_d20_palestra:
    $ vai("palestra", "The gym — 3 p.m.")
    $ musica("palestra")
    $ ambiente("palestra")
    $ cg("The gym almost empty on a Saturday, Simon alone putting plates back on the rack", "images/cg/ep2/d20_d1a_simon_solo.webp")
    si "Saturday? Who are you and what have you done with Sara?"
    s "I've had a big morning. I need to lift something."
    si "Best reason there is. Come on. Bench."
    $ interest("simon", 2, "Sara came in on a Saturday.")
    $ via_cg()
    $ cg("Sara on the bench, Simon behind her, his hands an inch from the bar", "images/cg/ep2/d20_d1b_panca.webp")
    n "He spots her with his hands an inch from the bar, never touching it. She does six. She does seven, and eight, and has a small fight with nine."
    si "That's your best. By two. What happened this morning?"
    s "Somebody didn't tell me something."
    if fatto("ep2_d19_sa_di_simon"):
        n "He laughs, and then he's careful with her again. He's been a fraction too careful since she came in, as if she were a glass that somebody had told him about."
    else:
        n "He laughs and hands her the towel. He's got no idea what she saw on Wednesday. It's all over his nice open face that he's got no idea."
    menu:
        sp "Wednesday. Him and Joanie. I could just say it."
        "«I know about you and Joanie.»":
            $ confidence(1, "Sara said it straight out.")
            $ interest("simon", 1, "Sara didn't judge him.")
            s "I know about you and Joanie."
            si "...Right. Okay."
            si "Do you think I'm a terrible person?"
            s "I think you're a terrible hider."
            $ via_cg()
            $ cg("Simon laughing so hard that he has to put the weight down, Sara grinning on the bench", "images/cg/ep2/d20_d1c_risata.webp")
            n "He laughs so hard that he has to put the plate down."
            si "I'm not proud of it. I'm a bit proud of it. No. I'm not."
        "Say nothing.":
            n "She drinks some water instead. It isn't hers to say. She's surprised by how much she'd have enjoyed saying it."
    menu:
        si "You've got ten minutes left in you. Stretch, or home?"
        "Stay for a stretch." (corruption=12):
            $ interest("simon", 2, "Sara stayed for a stretch.")
            $ corruption(1, "Sara let the stretch last.")
            n "He kneels behind her on the mat and leans his weight into her shoulders, and she folds forward further than she thought she went."
            si "Breathe out. There. You've got more than you think."
            n "His hands stay after the count. Neither of them mentions that there isn't a count any more."
        "Shower. Dinner.":
            s "Home. I've got a date with a man who's ironed something."
            si "Ha. Then go. Never keep an ironed man waiting."
    return

label ep2_d20_joanie:
    $ vai("casa_joanie", "Joanie's flat — 3 p.m.")
    $ musica("casa")
    $ cg("Joanie in a dressing gown and sunglasses, holding out a mug of terrible coffee", "images/cg/ep2/d20_d2a_joanie_occhiali.webp")
    ch "Don't speak. Sit. Tell me everything. In that order."
    $ interest("amica", 2, "Sara told Joanie first.")
    n "She does Magnus. She does the chair and the window and the page on its face. Joanie takes her sunglasses off for it, which she hasn't done for the sun."
    s "And then he asked me which of them it's about. Which man."
    if sara_bad_girl:
        n "Joanie doesn't say a word. She just looks at her over the mug, and very slowly one eye closes."
        s "It's a {i}novel{/i}, Jo."
        ch "I never said anything. Did I say anything?"
    else:
        ch "And what did you say?"
        s "I didn't."
        ch "You didn't. You sat there with your hair and your mouth and didn't. I'd have paid money."
    $ via_cg()
    $ cg("Sara and Joanie lying on the bed with their feet up the wall, the damp stain like a rabbit on the ceiling", "images/cg/ep2/d20_d2b_coniglio.webp")
    n "They end up on the bed with their feet up the wall, the way they always have, under the stain that looks like a rabbit."
    menu:
        ch "So. Coffee man. Are we talking about him, or are we not talking about him?"
        "«We're talking about him.»":
            $ interest("ex", 1, "Sara talked about Jacob.")
            $ corruption(1, "Sara talked about Jacob and didn't change the subject.")
            s "We're talking about him."
            ch "Oh thank God. Start with the hands."
            n "Sara starts with the hands. It takes a while. The rabbit's heard worse."
        "«We're not talking about him.»":
            $ confidence(1, "Sara kept last night for herself.")
            s "We're not talking about him."
            ch "Fine. I can not talk about him for hours. I'm doing it now. Look at me go."
    return

label ep2_d20_scrivere:
    $ vai("casa", "Home — 3 p.m.")
    $ musica("casa")
    $ cg("Sara at the table by the window, page fifty-one blank on the screen", "images/cg/ep2/d20_d3a_pagina_bianca.webp")
    $ confidence(2, "Sara cut everything she'd apologised for.")
    n "[nome_compagno] has gone to set up his table for tomorrow. The flat's full of glue and quiet."
    n "She takes out every sentence in which her heroine explains herself. It takes an hour. It's like opening windows."
    n "Then page fifty-one is there, quite white, and the woman is still standing where she can see them both."
    menu:
        sp "She's got to go somewhere. She can't stand in a doorway for a whole novel."
        "She goes to the one outside.":
            $ segna("ep2_d20_romanzo_altro")
            $ corruption(1, "Sara's heroine went to him.")
            n "She goes to the one outside. Sara types it with her ears hot, and when she's finished she gets up and walks round the table, twice, as if somebody might be in."
        "She goes back in to the one who's laughing.":
            $ segna("ep2_d20_romanzo_fidanzato")
            $ interest("josh", 1, "In the book, she went back in.")
            n "She goes back in. He looks up and sees her, and the laugh changes into a different one, only for her. Sara knows exactly what it sounds like. She doesn't have to make anything up."
        "She goes home alone, and walks.":
            $ segna("ep2_d20_romanzo_sola")
            $ confidence(1, "Sara's heroine went home by herself.")
            n "She goes home on foot, with her shoes in her hand, and for two whole pages nobody looks at her at all. It's the best thing Sara's ever written. She's almost sure."
    $ via_cg()
    $ cg("Late light across the floor, printed pages everywhere, Sara's bare feet among them", "images/cg/ep2/d20_d3b_pagine_pavimento.webp")
    n "When she looks up, the light's gone orange and there are pages all over the floor."
    return


## --- La cena con Josh ------------------------------------------------------------------------

label ep2_d20_cena:
    $ vai("enoteca", "The place with the candles in bottles — 8:15 p.m.")
    $ musica("enoteca")
    $ ambiente("enoteca")
    $ cg("Josh on his feet in a badly ironed shirt, holding out a chair for Sara at the corner table", "images/cg/ep2/d20_e1_sedia.webp")
    c "I asked for the table where nobody walks past."
    n "He's nervous. He's known her for years and he's nervous, and there's something written on his hand."
    s "What's that?"
    c "Topics."
    $ via_cg()
    $ cg("Close-up of Josh's palm in the candlelight: «Magnus · shield · wed?» in smudged ink", "images/cg/ep2/d20_e2_argomenti.webp")
    c "So. Topic one. Magnus."
    if fatto("ep2_d20_magnus_ascolta"):
        s "He said it's about a window. He said I'd written one page about a hand on the latch."
        c "Whose hand?"
        s "Mine, I think."
        c "That's good. That's really good, Sara. I'd have just said I liked the bit with the dog."
        s "There isn't a dog."
        c "There was a dog in my head."
    else:
        s "He said a third of it's me apologising."
        c "Only a third? That's brilliant. For you that's brilliant."
        n "She laughs so loudly that a man two tables away looks round, pleased."
    if fatto("ep2_d20_legge_sara"):
        s "I read him the last page out loud. My voice went all low and sure of itself. I didn't know I had one of those."
        c "I'd like to hear that some time."
        n "He says it lightly, to the bread."
    elif fatto("ep2_d20_legge_magnus"):
        n "She doesn't tell him that Magnus read it to her. She'd have to say why she went red."
    c "Topic two is mostly glue. I'll skip to three. Mark's asked me to a thing on Wednesdays. Dungeons and Dragons. Dice, and doing voices. I said probably not."
    s "Why probably not?"
    c "You'd be on your own all evening."
    sp "All evening."
    n "It goes by like a car outside. She hears it all the way to the corner."
    s "I can be on my own, [nome_compagno]. I'd write."
    c "Yeah? ...I'll think about it."

    $ via_cg()
    menu:
        sp "He's looking at me as if I were the last page of something."
        "Be here, all the way." (josh=30):
            $ segna("ep2_d20_serata_romantica")
            $ interest("josh", 4, "Sara was with him, and nowhere else.")
            $ cg("Sara's hand over Josh's on the tablecloth, candles, both of them laughing", "images/cg/ep2/d20_e3_romantica.webp")
            n "She puts her hand over the list on his. For two hours she doesn't think of a single person who isn't at the table. It isn't even difficult. That's what surprises her."
            c "You're looking at me."
            s "I know. I'd forgotten what you do with your eyebrows."
        "Somewhere else.":
            $ segna("ep2_d20_serata_distratta")
            $ interest("josh", -2, "Sara was somewhere else.")
            $ corruption(1, "Sara spent the dinner at a window.")
            $ cg("Josh talking across the candles while Sara looks at her own reflection in the dark window", "images/cg/ep2/d20_e4_distratta.webp")
            n "He's telling her how you age cardboard with tea. She watches his mouth. She's on the other side of a window, with her hand on a latch."
            c "Sara?"
            s "Tea. Yes. Go on."
        "Listen to him, smiling.":
            $ cg("Josh on his feet in a badly ironed shirt, holding out a chair for Sara at the corner table", "images/cg/ep2/d20_e1_sedia.webp")
            n "She asks about the tea and the cardboard. She even remembers the answer. He tells the waiter it's a special occasion, and when the waiter asks which one he says «Saturday»."

    ## Il telefono a tavola: la Suspicion la dà il gesto, mai il messaggio (Jody, 25/11).
    $ suono("telefono_vibra")
    menu:
        n "In her bag, under the table, the phone goes. It goes three times."
        "Leave it in the bag.":
            $ via_cg()
            $ cg("The closed bag on the chair beside Sara; Josh smiling into his pudding", "images/cg/ep2/d20_e5_borsa.webp")
            n "[nome_compagno] looks at the bag, then at her, then back at his pudding, and gets a bit taller."
        "Look at it.":
            $ suspicion(2)
            $ via_cg()
            $ cg("The phone's light on Sara's face across the candles, Josh watching her", "images/cg/ep2/d20_e5_schermo.webp")
            if fatto("ep2_d18_pranzo_daniel"):
                n "{i}Still thinking about your question.{/i} Daniel. She puts it away. It was only a second. It's a very long second, from the other side of the table."
            else:
                n "{i}how's the candle place. is he doing the eyebrows{/i} Joanie. She puts it away. It was only a second. It's a very long second, from the other side of the table."
            c "Work?"
            if fatto("ep2_d18_pranzo_daniel"):
                s "Nothing."
            else:
                s "Joanie. It's nothing."
    $ via_cg()
    $ ambiente(None)
    $ musica("notte")
    $ vai("strada", "On the way home — 10:30 p.m.")
    if fatto("ep2_d20_serata_romantica"):
        n "He gives her his jacket. She puts it on and keeps hold of his hand inside the pocket, and on the stairs, on the second landing, one of them starts it and neither of them could say which."
        c "Wish me luck for tomorrow. I'm judging the shields."
        s "Tomorrow."
        call ep2_d20_camera
    else:
        n "They walk home the short way. He tells her about the judging, and which of the shields are going to be a problem."
        c "Wish me luck for tomorrow. I've got to be up at six."
        n "He's asleep before she's taken her earrings out. He's set the alarm already, and put his good trousers on the chair."
    return


## --- La camera: solo con la serata romantica (Jody, 25/11) --------------------------------------
## Sobria; la parte esplicita col brief docs/nsfw/brief/d20_josh.md.

label ep2_d20_camera:
    $ vai("camera", "The bedroom — 11 p.m.")
    $ musica("casa")
    $ cg("Sara and Josh in the bedroom doorway with their shoes in their hands, trying not to laugh", "images/cg/ep2/d20_e6_porta.webp")
    n "They come in with their shoes in their hands, because of the neighbours, and that's what does it. They have to hold on to the door frame."
    c "Lamp on or lamp off?"
    s "On."
    c "You always say off."
    s "I know what I always say."
    $ via_cg()
    $ cg("Sara and Josh sitting on the bed in the lamplight, her hand flat on his chest", "images/cg/ep2/d20_e7_mano.webp")
    if fatto("ep1_d7_josh_precoce"):
        n "He goes still, on the edge of the bed, with one sock on, and she can see him remembering."
        c "I did promise I'd make it up to you."
        s "There's no hurry. There isn't anything anywhere. Breathe."
        n "She puts her hand flat on his chest until he does."
    else:
        n "He looks at her the way he used to look at her across rooms, when he was still working out how to walk over."
        s "Come here. You're miles away."
        c "I'm really not."
        n "She puts her hand flat on his chest to check. He's right there."
    $ via_cg()
    call scena_nsfw("d20_josh")
    $ via_cg()
    $ cg("Afterwards: Sara and Josh forehead to forehead, the duvet on the floor, both smiling", "images/cg/ep2/d20_e8_dopo.webp")
    n "The ink on his hand has come off on her shoulder. «Wed?», backwards."
    c "You've got my topics on you."
    s "I'll read them in the mirror."
    n "He laughs into her hair, and goes on laughing for a bit after he's asleep."
    sp "That was lovely. It really was."
    n "She lies quite still, warm to the fingertips, with everything exactly where it belongs."
    $ via_cg()
    return


## --- Notte: il telefono -----------------------------------------------------------------------

label ep2_d20_notte:
    $ vai("casa", "Home — Saturday night")
    $ musica("notte")
    $ cg("Josh asleep, his ironed shirt on the chair; Sara at the window with her phone", "images/cg/ep2/d20_f1_finestra.webp")
    if fatto("ep2_d20_serata_romantica"):
        n "She ought to sleep. She's got the phone in her hand instead, at the window, in his T-shirt."
    else:
        n "She isn't tired. She stands at the window in the dark with her phone, and somebody else's headlights go round the ceiling."
    call telefono_minuti_sessione(23 * 60, 23 * 60 + 30, "Go to bed")
    sp "Which of them is it about?"
    n "She puts the light out. She leaves the lamp in the hall on. She doesn't know why."
    $ via_cg()
    return
