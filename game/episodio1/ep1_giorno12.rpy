## =============================================================================
## EPISODE 1 — DAY 12 (Friday)
## =============================================================================
## Calendar: docs/mese-1.md, day 12. Work: Sara's first piece comes out; a moment
## of joy, pride and relief that she savours before sharing it (decision 18/11).
## Who gets it first: Josh (Josh +1) or Joanie (Joanie +1). Evening: a phone call
## with Joanie, who pushes her: talk about Simon (Simon +1, Joanie +1), Daniel
## (Daniel +1, Joanie +1) or only work (—); Joanie's advice: take it (Corr +1,
## Joanie +1) or laugh at it (—).
## Decisions with Jody:
## - 21/11: the piece is the one Sara chose on day 3: the Riverside cinema if she
##   proposed it, the Fourth Street car park if she took what she was given.
## - 21/11: Howard meets her on the landing and invites her in (visit ladder):
##   step 2 (the new cups) if she turned him down on day 11, step 3 (the light
##   bulb and the stepladder, his first body joke) if she went in. A refusal is
##   rifiuto_howard=True. With the Savior Complex she can't say no to everyday
##   requests (taking her shoes off for the ladder), and it feels like a dream.
## Draft by Claude, 21/11/2026: to review with Jody.
## Game text in English; comments in Italian.
## CG: docs/prompt-immagini/inquadrature-giorno-12.md. Finché mancano,
## compare la didascalia [CG].

label ep1_d12:
    call nuovo_giorno(12, "Friday")
    ## La pagina del pezzo: il cinema a pagina 7, il parcheggio a pagina 11.
    $ pagina_articolo = "7" if fatto("ep1_d3_proposta_cinema") else "11"
    call ep1_d12_articolo
    call ep1_d12_howard
    call ep1_d12_josh
    call ep1_d12_telefonata
    return


## --- Lavoro: esce il primo pezzo (decisione 18/11) ------------------------------------------

label ep1_d12_articolo:
    $ vai("redazione", "The newsroom — 8:40 a.m.")
    $ musica("redazione")
    $ ambiente("redazione")
    $ cg("The newsroom early on Friday morning", "images/cg/ep1/redazione_base.webp")
    n "Friday. Sara is in twenty minutes early, which has never happened in eight months."
    n "She tells herself it's because of the traffic. There was no traffic."
    $ cg("The folded newspaper and Barbara's yellow note on Sara's desk", "images/cg/ep1/d12_giornale_piegato_postit.webp")
    n "On her desk, folded in half, today's paper. Someone has put it there before her. A yellow sticky note on the front page, in thick red felt-tip."
    if fatto("ep1_d3_proposta_cinema"):
        n "{i}Page 7. Delicious. Don't let it go to your head. — B.{/i}"
    else:
        n "{i}Page 11. You made concrete sexy. I'm almost impressed. — B.{/i}"
    sp "Don't open it too fast. Don't open it too fast."
    n "She opens it too fast."

    $ cg("Early morning in the empty newsroom: Sara at her desk with the newspaper open in front of her, one fingertip resting on the byline under a headline, a soft, incredulous smile; a yellow sticky note beside the coffee", "images/cg/ep1/d12_01_giornale.webp")
    if fatto("ep1_d3_proposta_cinema"):
        n "{i}SIXTY YEARS IN THE DARK. Love stories from the Riverside, before the lights go up for good.{/i}"
        n "Half a page. A photo of the old red seats. And Ada and Walter, married fifty-one years, who met in row F in 1973 during a film neither of them remembers."
    else:
        n "{i}FOURTH STREET: THE CAR PARK THAT WAITS. Six floors of concrete, and the lives that will pass through them.{/i}"
        n "A quarter of a page. A photo of the grey ramp in the rain. And the old attendant, Mr Bello, who has named every pillar after a jazz singer."
    sp "Page [pagina_articolo]. Not twenty-six. Page [pagina_articolo]."
    n "And under the headline, in small capitals, a name."
    n "Hers."
    sp "That's me. That's my name. In print. In a real newspaper that real people are reading over real breakfast right now."
    n "She touches it. The ink comes off a little on her fingertip, grey, and she doesn't wipe it away."
    sp "Eight months of cheese festivals. Eight months of «Sara, darling, somebody has to do it»."
    if fatto("ep1_d3_proposta_cinema"):
        sp "And I said it. In front of eleven people. And she said yes. And I wrote it until two in the morning, and here it is."
    else:
        sp "Eight hundred words on a car park, and I made it good. Nobody asked me to make it good. I did it anyway."
    n "She reads the first line. Then the last. Then the first again, slowly, as if it had been written by somebody else and she wanted to know if it was any good."
    n "It is. She can tell. It's good."
    sp "Don't cry in the newsroom. Do {i}not{/i} cry in the newsroom."
    n "She doesn't. She just sits there with her coffee going cold, smiling at a piece of paper like an idiot, for a full five minutes."
    n "Nobody else is in yet. Nobody to tell. For five minutes it's only hers, and that's the best part."

    $ cg("Close-up of Sara's hands holding her phone over the open newspaper: a photo of the article on the screen, her thumb hovering over the send button, a grey ink smudge on her fingertip", "images/cg/ep1/d12_02_telefono.webp")
    n "Then she takes a photo of the page. Then another, because in the first one her thumb is in it."
    sp "Who first?"

    menu:
        sp "Who gets it first?"
        "Send it to [nome_compagno] first.":
            $ interest("josh", 1, "Sara sends her first article to [nome_compagno] first.")
            $ segna("ep1_d12_primo_josh")
            $ suono("notifica")
            n "{i}Page [pagina_articolo]. Look who's in the paper.{/i}"
            n "The reply arrives in under a minute. He's supposed to be in a meeting."
            c "{i}OH MY GOD{/i}"
            c "{i}I'm in a meeting. I'm reading it under the table. I'm going to cry in front of the sales team.{/i}"
            c "{i}I'm so proud of you I could burst. Printing it. Putting it on my monitor. Everybody is going to see it.{/i}"
            sp "He's going to make everybody in that office read it. Even the ones who don't read."
            n "She sends it to Joanie a minute later. Joanie replies with eleven exclamation marks and a voice message that is mostly screaming."
        "Send it to Joanie first.":
            $ interest("amica", 1, "Sara sends her first article to Joanie first.")
            $ segna("ep1_d12_prima_joanie")
            $ suono("notifica")
            n "{i}Page [pagina_articolo]. Don't laugh.{/i}"
            n "Fourteen seconds. A voice message. Sara holds the phone a good ten centimetres from her ear."
            ch "{i}WHO'S LAUGHING? WHO IS LAUGHING? I'm buying ten copies. I'm buying the newsagent. I'm framing it in my bathroom!{/i}"
            ch "{i}My best friend is a JOURNALIST. A real one. With a NAME.{/i}"
            sp "She's been telling me I could do this since we were at school."
            n "Then she sends it to [nome_compagno]. He's in a meeting, so it's a few minutes before he answers: {i}AMAZING. Printing it. So proud of you.{/i}"
    $ nota_sara("capa", "My first real piece came out. Barbara left a note on it: she liked it, and she'll never say so out loud.")

    $ vai("redazione", "The newsroom — 11:30 a.m.")
    $ cg("Roberta brings Sara a cappuccino with a cinnamon heart, the newspaper open on her desk", "images/cg/ep1/d12_roberta_cappuccino_articolo.webp")
    n "The rest of the morning, people stop at her desk. Not many. Enough."
    n "Jessica claps with little quick hands. Roberta brings a cappuccino with a heart drawn in the cinnamon and says nothing at all, only smiles."
    $ cg("Through the glass of her office, Barbara quietly rereads the newspaper", "images/cg/ep1/d12_barbara_rilegge_dietro_vetro.webp")
    n "Barbara doesn't come out of her office. But at eleven-thirty, through the glass door, Sara sees her holding the paper open at page [pagina_articolo], reading, a red nail tapping slowly on the margin."
    sp "She's reading it again."
    sp "Don't let it go to your head, Sara."
    sp "...Too late."
    return


## --- Sera: Howard sul pianerottolo, l'invito (scala delle visite, 21/11) ---------------------

label ep1_d12_howard:
    $ vai("pianerottolo", "The landing — 6:30 p.m.")
    $ ambiente(None)
    $ musica(None)
    $ suono("telefono_vibra")
    show expression Transform("images/cg/ep1/d8_rientro_citofono.webp", crop=(980, 150, 1664, 936), xysize=(config.screen_width, config.screen_height)) as cg_corrente
    with dissolve
    n "On the stairs, a message from [nome_compagno]: {i}Daniel wants the big contract signed before his party tomorrow. Eight o'clock. Then I'm ALL yours, Miss Front Page.{/i}"
    sp "Page [pagina_articolo]. But I'll take Front Page."
    n "She's taking out her keys, her own keys, when the green door opens."
    $ musica("howard")
    $ cg("The landing at dusk: Howard in the doorway of his green door, beaming, holding up three copies of the same newspaper fanned out like a winning hand of cards", "images/cg/ep1/d12_03_howard_giornali.webp")
    ho "Sara! There she is. There's the famous one."
    n "He holds up three copies of the paper, fanned out like a winning hand of cards."
    ho "I read the paper every morning, page by page, for thirty years. And this morning, page [pagina_articolo]... I nearly dropped my cup."
    ho "So I went back down and bought two more. One to keep, one to frame. And one just in case."
    s "Howard... you bought three?"
    ho "I'd have bought ten, but the newsagent was looking at me."
    if fatto("ep1_d3_proposta_cinema"):
        ho "Row F. Ada and Walter. I took my mother to the Riverside, you know, every Sunday, until her knees went. I read it twice."
    else:
        ho "That attendant. The pillars with the singers' names. I've parked there, you know, and I never noticed. You noticed. I read it twice."
    n "He's not being polite. His eyes are wet, and this time, Sara is sure, it's real."
    sp "He read it twice. He bought three copies."
    sp "The first person I don't know who read it... no. I do know him. My neighbour."

    ## L'invito: ogni incontro, un invito (21/11). Lo step dipende da howard_visite.
    ho "Come in. Just for a moment. We have to celebrate. I've got a bottle of something that's been waiting since 1990 for a good reason."
    n "He says it looking at his slippers, with the hopeful face of a dog that already knows it's going to be told to get off the sofa."
    if fatto("ep1_d11_rifiuta_invito"):
        ho "And the cups. The new ones. They're still waiting too."

    menu:
        sp "Celebrate at Howard's?"
        "Go in and celebrate.":
            if howard_visite >= 2:
                call ep1_d12_scaletta
            else:
                call ep1_d12_tazze
        "«Not tonight, Howard. I'm dead on my feet.»" (rifiuto_howard=True):
            $ segna("ep1_d12_rifiuta_invito")
            ho "Of course. Of course. Not tonight. The bottle has waited thirty years, it can wait a few more days."
            n "He presses one of the three papers into her hands, the one to keep, and closes the green door very gently."
            if fatto("ep1_d11_rifiuta_invito"):
                ## Due rifiuti di fila: il retroscena mostra la strategia (21/11).
                call inizio_retroscena
                $ cg("Retroscena: Howard's untidy kitchen, a cheap wall calendar by the fridge with small pencil marks on many days; Howard writing on it with a stubby pencil, back to the viewer", "images/cg/ep1/d12_07_calendario.webp")
                rs "In Howard's kitchen, next to the fridge, there's a calendar from the chemist's. Free, with a kitten for every month."
                rs "On some days there's a small pencil mark. A «J» and a time. «J 21». «J 20». «J 19:30»."
                rs "Every evening [nome_compagno] has come home late this month, through the wall, on the stairs. Howard has written it down."
                rs "Tonight he writes «J 20». Then he smiles at the kitten. No hurry. There'll be another late evening. There always is."
                $ retroscena("howard", "He keeps a calendar of the evenings Josh comes home late. He's in no hurry.")
                call fine_retroscena
    return


## --- Step 2 della scala, se al giorno 11 aveva rifiutato: le tazze nuove ---------------------

label ep1_d12_tazze:
    $ howard_visite += 1
    $ segna("ep1_d12_visita")
    $ vai("casa_howard", "Howard's flat — 6:40 p.m.")
    $ ambiente("tv_howard")
    $ cg("Howard's living room a little tidier than before: newspapers stacked in a corner, two brand-new white cups with price stickers on the table; Sara on the sofa reading the newspaper aloud, Howard in his armchair listening, hands clasped", "images/cg/ep1/d12_08_tazze_lettura.webp")
    n "The flat is different from Tuesday. Not clean, not really. But the newspapers are stacked in a corner, and there's a window open a crack."
    n "On the table, two white cups, still with the price stickers on the bottom."
    ho "Bought them for guests. Well. For a guest. They've been sitting there since yesterday, looking at me."
    ## Niente Complesso qui: col Complesso al giorno 11 non poteva rifiutare il caffè.
    n "The bottle from 1990 turns out to be sweet sherry. They drink it from the new cups, because Howard doesn't own two matching glasses."
    ho "Read it to me. Out loud. I want to hear it in your voice."
    n "So she reads him her own article, sitting on his sofa, the paper on her knees. Howard listens without moving, his cup halfway to his mouth."
    ho "You're a special girl, Sara. I don't say that to everyone. I don't say anything to anyone, actually."

    menu:
        sp "Another sherry?"
        "Another glass.":
            $ interest("howard", 2, "Sara stayed to celebrate with him.")
            n "The second sherry lasts half an hour. He tells her about Lorna, who almost married him in 1987, and about his mother's cat."
            n "Sara laughs more than she expected to. It's a strange place to celebrate. It's not a bad one."
        "«I'd better go, really.»" (rifiuto_howard=True):
            $ interest("howard", 1, "A sherry at Howard's.")
            ho "Of course. Of course. You've had a big day."
            n "He doesn't insist. He never insists. He just looks at her, grateful, until she feels guilty for leaving."
    $ ambiente(None)
    $ nota_sara("howard", "He bought three copies of my article and made me read it to him. Sherry from 1990, in his new cups.")
    call ep1_d12_ritaglio
    call ep1_d12_ritorno
    return


## --- Step 3 della scala: la lampadina e la scaletta (bozza 21/11) ----------------------------

label ep1_d12_scaletta:
    $ howard_visite += 1
    $ segna("ep1_d12_visita")
    $ segna("ep1_d12_scaletta")
    $ vai("casa_howard", "Howard's flat — 6:40 p.m.")
    $ ambiente("tv_howard")
    if fatto("ep1_d11_pantofole"):
        $ cg("The pink slippers beside the paper bag in Howard's hall", "images/cg/ep1/d12_pantofole_restituite.webp")
        n "She has brought back his pink slippers, in a paper bag. Howard won't take them."
        ho "No, no. They live here now. By the door. For when you come."
        n "He puts them by his door, side by side, toes pointing in. As if they were waiting for someone."
    $ cg("Howard's dark corridor with the stepladder already open beneath the dead bulb", "images/cg/ep1/d12_corridoio_lampadina_spenta.webp")
    n "The corridor of Howard's flat is darker than usual. Pitch dark, in fact."
    ho "Ah. Yes. The bulb. It went on Wednesday. I've been living like a mole."
    ho "At my age, the ladder... my knees, my balance. My mother always did it. Then nobody."
    if fatto("ep1_d9_aiuto_pulire"):
        ho "And you did say, on Tuesday, that one day you'd help me with the house."
        sp "I did say that."
    n "There's a little three-step ladder already open under the dead bulb. And a new bulb waiting on the top step, still in its box."
    sp "Already open. Already waiting. As if he knew."
    s "Give it here. Hold the ladder."

    if complesso_crocerossina:
        ## Il Complesso (21/11): la richiesta quotidiana a cui non sa dire di no.
        ho "Not in those shoes, my dear. Heels on a ladder... I'd never forgive myself. Barefoot. Safer."
        sp "Barefoot. In Howard's corridor. Why would I..."
        n "She's already stepping out of her shoes. The floor is cold under her tights."
        sp "It's safer. He's right. It's nothing."
        $ segna("ep1_d12_scalza")
        $ cg("Howard's dim corridor: Sara barefoot on a small stepladder in her work skirt and blouse, stretching up to change a light bulb, her shoes left at the foot of the ladder; Howard below, both hands on the ladder, looking up at her", "images/cg/ep1/d12_04b_scaletta_scalza.webp")
    else:
        $ cg("Howard's dim corridor: Sara on a small stepladder in her work skirt and blouse, stretching up to change a light bulb; Howard below, both hands on the ladder, looking up at her", "images/cg/ep1/d12_04_scaletta.webp")
    n "She climbs. Three steps aren't much, but the ladder wobbles, and Howard's hands close on it at once, firm, just under her knees."
    n "She stretches up. The old bulb is stiff. She has to reach, on her toes, arms over her head."
    n "Below her, Howard has gone very quiet."

    ## Bonus (Jody, 21/11): il punto di vista di Howard dal fondo della scala, coi suoi
    ## pensieri. Solo per chi ha investito molto su Howard: Interest Howard 15 o più
    ## (massimo possibile qui: 18). Vale come segreto trovato.
    if valore_interest("howard") >= 15:
        call ep1_d12_bonus_pov

    ho "Careful, careful. I've got you."
    n "The old bulb comes out. The new one goes in. Light floods the corridor, yellow and sudden."
    n "And in the light, Sara looks down, and sees exactly where Howard is looking. It isn't the bulb."
    ho "Well. I was worried you'd tip over, you know."
    ho "All that weight at the top, and such little feet."
    n "For half a second, the corridor is perfectly silent."
    sp "He did not just say that."
    sp "He did. He said it. About my..."
    if fatto("ep1_d11_capisce_howard"):
        sp "Yesterday it was a joke on the landing. Today he's not even pretending it's a joke."
    else:
        sp "So that's how he looks at me. All this time. Oh, Howard."
    n "He's still holding the ladder. He's still looking up. He's pink to the ears and, unmistakably, very pleased with himself."

    menu:
        sp "All that weight at the top."
        "Laugh, and give it back to him.":
            $ corruption(1, "Sara laughs at Howard's joke, and gives it back.")
            $ interest("howard", 1, "Sara laughed at his joke.")
            $ segna("ep1_d12_ride_battuta")
            ## Col Complesso Sara è scalza: variante coi tacchi per terra.
            if fatto("ep1_d12_scalza"):
                $ cg("Howard's corridor in yellow light: Sara on the stepladder laughing, one hand on Howard's shoulder for balance, cheeks pink; Howard looking up at her, delighted; Sara barefoot in her tights, her heels on the floor", "images/cg/ep1/d12_05_ride_scalza.webp")
            else:
                $ cg("Howard's corridor in yellow light: Sara on the stepladder laughing, one hand on Howard's shoulder for balance, cheeks pink; Howard looking up at her, delighted", "images/cg/ep1/d12_05_ride.webp")
            n "And Sara laughs. Again. Like yesterday, like a hiccup, out of nowhere."
            s "Then you'd better hold the ladder tighter, Howard. If I fall, I'm falling on you."
            ho "Oh, my dear. Promises, promises."
            n "She puts a hand on his shoulder to climb down. She doesn't need it. She leaves it there one step longer than she needs to."
            sp "What am I doing? I'm joking with him. About {i}that{/i}."
            sp "And it's... funny. It's fun. Nobody makes jokes like that with me. Everybody either stares, or pretends not to."
            sp "He does neither. He just says it."
        "Climb down and change the subject.":
            $ interest("howard", 1, "Sara changed his light bulb.")
            $ segna("ep1_d12_cambia_discorso")
            ## Col Complesso Sara è scalza: variante coi tacchi per terra.
            if fatto("ep1_d12_scalza"):
                $ cg("Howard's corridor in yellow light: Sara stepping down from the stepladder with a polite, slightly stiff smile, holding the old bulb; Howard stepping back, contrite; Sara barefoot in her tights, her heels on the floor", "images/cg/ep1/d12_05b_scende_scalza.webp")
            else:
                $ cg("Howard's corridor in yellow light: Sara stepping down from the stepladder with a polite, slightly stiff smile, holding the old bulb; Howard stepping back, contrite", "images/cg/ep1/d12_05b_scende.webp")
            n "Sara climbs down, quickly, and hands him the old bulb."
            s "There. Let there be light. Now, where's this famous bottle?"
            n "Howard blinks. Then, at once, he's the old Howard again: a little bent, a little shy, apologetic in every line."
            ho "The bottle. Yes. Of course. This way, this way."
            sp "He knows. He knows he went too far, and he's pretending he didn't. Good."
            sp "...Is it good?"

    $ cg("Howard's sofa: two small glasses of dark sherry raised in a toast, the cut-out article lying on the coffee table between them; Sara laughing, Howard beaming", "images/cg/ep1/d12_06_brindisi.webp")
    n "The bottle from 1990 turns out to be sweet sherry. Howard owns two glasses that almost match."
    ho "To the writer."
    s "To the light bulb."
    ho "To both. To the light bulb, and to the writer, and to the day she came in and fixed my house."
    n "On the coffee table, the article. He has already cut it out, very carefully, with the scissors his mother used for her recipes."
    if fatto("ep1_d12_ride_battuta"):
        n "Twice more, while they drink, he makes a joke. Smaller. Testing. Twice more she laughs."
    $ ambiente(None)
    $ nota_sara("howard", "I changed his light bulb. From the bottom of the ladder he made a joke about my... about me. Out loud.")
    call ep1_d12_ritaglio
    call ep1_d12_ritorno
    return


## --- Bonus: dal fondo della scala, gli occhi di Howard (Jody, 21/11) --------------------------

label ep1_d12_bonus_pov:
    $ segna("ep1_d12_bonus_pov")
    call inizio_retroscena
    $ cg("Bonus, Howard's point of view from the foot of the ladder: looking up at Sara's chest in her grey-lilac blouse, buttoned, stretched tight as she reaches up, a faint outline of her nipples through the thin cotton with both arms, her chin and the ceiling lamp above; his own hands on the ladder at the bottom of the frame", "images/cg/ep1/d12_04c_pov_howard.webp")
    rs "From the bottom of the ladder, the world is very simple. Two hands on cold metal. And above him, her."
    rs "Thirty-one years at the factory. Forty years of looking at women from the other side of the street."
    rs "And now God changes a light bulb for him, in his own corridor, on his mother's ladder."
    rs "The buttons are holding. Brave little buttons. Every time she reaches up, they think about it."
    if fatto("ep1_d11_bottoni") == 2:
        rs "Yesterday she undid two of them. For him. Looking him in the eye."
    elif fatto("ep1_d11_bottoni"):
        rs "Yesterday she undid one of them. For him. Nobody asked her to."
    if complesso_crocerossina:
        rs "Barefoot, too. He only had to say «safer». She'll always do what's safer, if he's the one who says it."
    rs "He could stay like this all evening. He could buy a new bulb every day."
    rs "Patience, Howard. One bulb at a time."
    $ retroscena("howard", "From the bottom of the ladder, he wasn't looking at the bulb. «One bulb at a time.»")
    $ segreto_trovato("Howard's view from the bottom of the ladder.")
    call fine_retroscena
    return


## --- Retroscena: il ritaglio nel cassetto ----------------------------------------------------

label ep1_d12_ritaglio:
    call inizio_retroscena
    $ cg("Retroscena: Howard's bedside drawer at night under a yellow lamp: a neatly cut newspaper article laid on a folded square of pale pink lace, next to a shiny new brass key", "images/cg/ep1/d12_09_ritaglio.webp")
    rs "Later, when she's gone, Howard opens the drawer of his bedside table."
    rs "The pink lace. The new key. And now, folded once, her article, with her name in small capitals."
    rs "He reads her name with his finger, the way she did this morning. He doesn't know she did that. It doesn't matter."
    $ retroscena("howard", "He keeps Sara's article in his drawer, with the key and the pink lace.")
    call fine_retroscena
    return


## --- Ritorno a casa dopo la visita -------------------------------------------------------------

label ep1_d12_ritorno:
    $ vai("casa", "Home — 7:45 p.m.")
    $ musica("casa")
    if fatto("ep1_d12_scalza"):
        $ cg("Sara looks down at her stockinged feet, carrying her heels in the hallway", "images/cg/ep1/d12_rientro_scarpe_in_mano.webp")
    else:
        $ cg("Sara's keys back in the ceramic bowl by the door", "images/cg/ep1/d11_chiavi_ritrovate_ciotola.webp")
    n "She opens her own door with her own keys at a quarter to eight. The flat is quiet and smells of nothing at all after Howard's."
    if fatto("ep1_d12_scalza"):
        n "It's only in the hallway that she realises she's holding her shoes in her hand. She walked out of his flat, and across the landing, barefoot."
        sp "When did I take them off? On the ladder. He said it was safer."
        sp "Strange evening. Like a dream you can't quite remember the middle of."
    elif fatto("ep1_d12_ride_battuta"):
        sp "I laughed. Again. I'm going to have to stop laughing at that man."
    return


## --- Sera: Josh torna e festeggia -------------------------------------------------------------

label ep1_d12_josh:
    if not fatto("ep1_d12_visita"):
        $ vai("casa", "Home — 6:35 p.m.")
        $ musica("casa")
        $ cg("The kitchen table where Sara leaves the newspaper open for Josh", "images/cg/ep1/casa_cucina_base.webp")
        n "She puts the paper Howard gave her on the kitchen table, open at page [pagina_articolo], where [nome_compagno] will see it as soon as he walks in."
    $ vai("casa", "Home — 8:10 p.m.")
    $ musica("casa")
    $ suono("chiave_serratura")
    $ cg("The kitchen in the evening: Josh just home in his work clothes, holding up a bag of Thai takeaway and a bunch of supermarket flowers still in the plastic; Sara laughing, the newspaper open on the table", "images/cg/ep1/d12_10_josh_fiori.webp")
    n "[nome_compagno] comes in at ten past eight with a bag of Thai takeaway in one hand and a bunch of supermarket flowers in the other, still in the plastic, still with the price on."
    c "For the writer. They had roses, but they looked depressed."
    s "They're perfect. They're absolutely perfect."
    c "It's on my monitor. Printed, in colour. The whole floor has read it."
    c "And Daniel walked past, stopped, and asked who wrote it. I said: my girlfriend. He read the whole thing standing up."
    sp "Daniel read it."
    c "He said: «Not bad.» From Daniel, that's practically a medal."
    if fatto("ep1_d12_prima_joanie"):
        c "Joanie had already put it on her story, by the way, with about forty hearts. I found out from Joanie's story that my own girlfriend is famous."
        s "I sent it to you two minutes later!"
        c "Two minutes is a long time in journalism."
        n "He's laughing. He kisses her forehead, and the forehead is forgiven."
    n "They eat on the sofa, straight from the boxes. He makes her read the best bits out loud, then the worst bits, then the bits in between."
    c "Tomorrow, the party. Daniel's villa. Everybody who matters. And now I get to say «my girlfriend, the journalist»."
    sp "Tomorrow. Daniel's villa. I still haven't got a dress."
    return


## --- Sera: la telefonata con Joanie -----------------------------------------------------------

label ep1_d12_telefonata:
    $ vai("casa", "Home — 10:40 p.m.")
    $ musica("notte")
    $ cg("The living room at night, one lamp on: Sara curled up on the sofa under a blanket in her pyjamas, on the phone, the newspaper on the cushion beside her", "images/cg/ep1/d12_11_telefonata.webp")
    n "By half past ten [nome_compagno] is asleep, done in by the contract and the curry. Sara takes the phone and the blanket to the sofa."
    $ suono("telefono_vibra")
    n "Joanie, of course. Joanie never texts after ten. She calls."
    ch "Is the famous journalist still awake, or does she need her beauty sleep now?"
    s "The famous journalist is on the sofa in her pyjamas."
    ch "Good. Tomorrow, ten o'clock, I'm picking you up. You're not going to the villa of the year in your interview dress."
    ch "Now. Talk. I want news. Real news. Not cinemas and car parks."
    sp "Real news. With Joanie that only means one thing."

    menu:
        sp "What do I tell her?"
        "Tell her about Simon.":
            $ interest("simon", 1, "Sara talks to Joanie about Simon.")
            $ interest("amica", 1, "Sara confides in Joanie.")
            $ segna("ep1_d12_parla_simon")
            call ep1_d12_parla_simon
        "Tell her about Daniel.":
            $ interest("daniel", 1, "Sara talks to Joanie about Daniel.")
            $ interest("amica", 1, "Sara confides in Joanie.")
            $ segna("ep1_d12_parla_daniel")
            call ep1_d12_parla_daniel
        "Only work. Boring, safe work.":
            $ segna("ep1_d12_parla_lavoro")
            s "News? Barbara left a sticky note on my article. A nice one. In red."
            ch "Babe. I love you. That is the least interesting sentence ever spoken on a Friday night."
            s "She read it twice! Through the glass! I saw her!"
            ch "Okay, okay. Barbara is a witch, and the witch likes you. Noted. Moving on."

    ## Il consiglio di Joanie: la spinta (calendario, giorno 12).
    $ cg("Close-up of Sara on the phone at night, half-smiling, chin on her knees, listening, the lamplight warm on her face", "images/cg/ep1/d12_11b_telefonata_primo_piano.webp")
    ch "Listen to me. I'm going to say something serious, and then I'm going to hang up before you can argue."
    ch "You've been the good girl your whole life. Good daughter, good girlfriend, good little journalist doing the cheese festival."
    ch "And today your name's in the paper, and the world didn't end. So tomorrow, at that party..."
    if fatto("ep1_d12_parla_simon"):
        ch "...and tomorrow morning at the open gym, if a certain someone is there..."
    elif fatto("ep1_d12_parla_daniel"):
        ch "...when Mr Villa looks at you, you look back. And you don't look away first."
    ch "...you stop asking permission to take up space. You let me pick the dress. You let them look. You've earned it."

    menu:
        sp "Let them look."
        "Take her advice.":
            $ corruption(1, "Sara takes Joanie's advice: let them look.")
            $ interest("amica", 1, "Sara listens to Joanie.")
            $ segna("ep1_d12_consiglio_joanie")
            s "...Maybe. Maybe I will."
            ch "MAYBE. She said maybe. I'm recording this call."
            s "You are not."
            ch "Ten o'clock. Shave your legs. Love you. Bye!"
            sp "Let them look."
            sp "A whole life of buttoning everything up to the collar. One night wouldn't kill me."
        "Laugh at her.":
            $ segna("ep1_d12_ride_joanie")
            s "Jo. It's a work party with my boyfriend's boss. It's not the Oscars."
            ch "Everything's the Oscars if you wear the right dress. Ten o'clock. Love you. Bye!"
            sp "Let them look. Honestly."
            sp "I'll wear something nice. Nice. That's all."

    $ musica("notte")
    $ cg("The dark living room: Sara alone on the sofa under the blanket, the phone screen lighting her face, the article open on it, a quiet, private smile", "images/cg/ep1/d12_12_rilettura.webp")
    n "Before she goes to bed, she opens the photo of the article one more time. Just the last line."
    if fatto("ep1_d3_proposta_cinema"):
        n "{i}The Riverside closes on the thirtieth. The people it made will stay open.{/i}"
    else:
        n "{i}One day someone will park on the third floor, check their lipstick in the mirror, and walk out to meet the love of their life. Concrete doesn't care. But it waits.{/i}"
    sp "I wrote that."
    if fatto("ep1_d12_visita"):
        n "Through the wall, very faintly, a television. A quiz show. Canned laughter. Then nothing."
    n "Sara switches off the phone and goes to bed with ink still on her fingertip."
    return


## --- La telefonata: Simon ----------------------------------------------------------------------

label ep1_d12_parla_simon:
    s "...Okay. There might be a thing. A tiny, stupid, non-thing."
    ch "Muscles."
    s "Don't call him that."
    ch "You didn't say «who». You went straight to «don't call him that». Babe."
    if fatto("ep1_palestra_da_sola"):
        s "Monday, when you stood me up... he was nice. He fixed my shoulder. He's very... careful. With his hands."
    else:
        s "He's just... nice. At the gym. He remembers things. What I said, what I lift."
    if fatto("simon_numero"):
        ch "And he gave you his number."
        s "He gave everybody his number. It's on the card."
        ch "He gave {i}you{/i} his number, on the card, with his own hand."
    if fatto("ep1_d8_tace_simon"):
        s "And I didn't tell [nome_compagno] about the session. I don't even know why. There was nothing to tell."
        ch "That's exactly why you didn't tell him. When there's really nothing, you tell."
    if fatto("ep1_d9_zoom_simon"):
        ch "Also, I saw you zoom. On Tuesday. You took eleven seconds to answer my photo."
        s "You can't possibly know that."
        ch "I know everything."
    ## Seme del giorno 17 (21/11): Joanie e Simon. Una pausa, niente di più.
    n "On the line, for half a second, Joanie goes quiet. Just half a second too long."
    ch "...He is careful with his hands. That's true."
    n "Then she laughs, loud, the way she always does, and the half second is gone."
    sp "What was that?"
    sp "Nothing. It's late. It was nothing."
    $ nota_sara("simon", "I told Joanie about Simon. She knew already, before I said a word.")
    return


## --- La telefonata: Daniel ---------------------------------------------------------------------

label ep1_d12_parla_daniel:
    s "Daniel read my article."
    ch "WHAT. Back up. Daniel, the boss Daniel? Villa Daniel?"
    s "[nome_compagno] printed it and stuck it on his monitor, and Daniel stopped and read the whole thing standing up. And then he said «not bad»."
    ch "«Not bad». From a man like that, «not bad» is a marriage proposal."
    s "Jo!"
    if fatto("ep1_d5_risposta_daniel"):
        ch "First you answer him back in front of the whole office, now he's reading your stuff. He's {i}keeping track{/i} of you, babe."
        sp "«I remember everything. Especially the people who answer back.»"
    if fatto("ep1_d5_daniel_bello"):
        ch "And let's not forget: «he's not ugly». Your words. I have them engraved."
    s "He's an arrogant man who treats [nome_compagno] like a coat rack. That's all."
    ch "Mm-hm. And tomorrow you're going to his house in the dress I choose."
    sp "Tomorrow I'll be in his house."
    n "The thought arrives without being invited, and sits down, and makes itself comfortable."
    $ nota_sara("daniel", "Daniel read my article, standing up, in [nome_compagno]'s office. He said «not bad».")
    return
