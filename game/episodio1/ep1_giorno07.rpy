## =============================================================================
## EPISODE 1 — DAY 7 (Sunday)
## =============================================================================
## Calendar: docs/mese-1.md, day 7. Morning: Darius drops by (first appearance,
## decided 18/11: an old friend of the couple, no flirting, no choices, no stats).
## Afternoon: writing or a walk by the river with [nome_compagno]. Evening: in bed.
## Seeds: [nome_compagno] buzzes Darius in and keeps opening the door himself
## (Sara still hasn't noticed her keys are gone); «next week is going to be bad,
## Daniel wants me on the late shift» prepares day 9 (I14). Darius and
## [nome_compagno] talk about «a proper night with everyone» (day 16).
## Reviewed with Jody on 21/11/2026 (invented details confirmed).
## Game text in English; comments in Italian.
## CG: docs/prompt-immagini/inquadrature-giorno-07.md. Finché mancano,
## compare la didascalia [CG].

label ep1_d7:
    call nuovo_giorno(7, "Sunday")
    call ep1_d7_darius
    call ep1_d7_pomeriggio
    call ep1_d7_sera
    return


## --- Mattina: Darius passa a trovarli ----------------------------------------------

label ep1_d7_darius:
    $ vai("casa", "Home — 11:20 a.m.")
    $ ambiente(None)
    $ musica("casa")
    $ cg("The living room on a lazy Sunday morning: Josh in a T-shirt and pyjama bottoms, hair a mess, pressing the intercom button by the door; Sara on the sofa with a mug, wrapped in a cardigan", "images/cg/ep1/d7_01_citofono.webp")
    n "Sunday. The flat smells of coffee and of last night's perfume. [nome_compagno] has been awake for twenty minutes and is still not entirely convinced about it."
    $ suono("citofono")
    n "The intercom buzzes. Twice, then once more, long."
    c "That's Darius. Only Darius rings like that."
    s "Did you invite him?"
    c "He invited himself. He does that. It's his best quality."
    n "[nome_compagno] buzzes him up and leaves the door ajar. Sara looks down at her pyjamas, then decides she doesn't care. It's Darius."

    $ cg("The front door: Darius in streetwear, a paper bag of pastries in one hand, pulling Josh into a back-slapping hug; Sara in the background with her mug, smiling", "images/cg/ep1/d7_02_abbraccio.webp")
    $ incontra("amico")
    dr "Room service! Croissants for the hungover and the elderly."
    c "I'm not hungover."
    dr "Then you're elderly. Come here."
    n "The hug lasts the usual three back-slaps. They've been doing it since they were sixteen, Sara thinks; nobody has ever taught them another way."
    dr "Sara. Looking good for someone who went out last night."
    s "How do you know we went out?"
    dr "Joanie posted a video. [nome_compagno] was dancing. I've watched it eleven times."
    c "Delete it."
    dr "I'll be buried with it."

    $ vai("casa", "The kitchen — 11:40 a.m.")
    $ cg("The kitchen table: Sara, Josh and Darius around a paper bag of croissants and three mismatched mugs, laughing; Sunday light through the window", "images/cg/ep1/d7_03_colazione.webp")
    n "They eat the croissants straight out of the bag, around the kitchen table, with the crumbs going everywhere."
    n "Darius and [nome_compagno] talk the way they always do: half in sentences, half in old jokes Sara stopped asking about years ago."
    dr "Remember the chemistry lab? The eyebrows?"
    c "We agreed we'd never talk about the eyebrows."
    s "What eyebrows?"
    c "There were no eyebrows. Nothing happened. Darius is a liar."
    dr "He had none for a month. He drew them on with his mum's pencil."
    n "Sara laughs so hard she has to put her mug down. [nome_compagno] throws a piece of croissant at his best friend, who catches it and eats it."
    dr "How's the novel? Still stuck on that door?"
    s "...He told you about the door?"
    dr "He tells everyone about the door. He's very proud of you. It's a bit embarrassing, honestly."
    c "It's not embarrassing. It's a good door."
    sp "He talks about my novel. Even to Darius. Even when I'm not there."

    if fatto("ep1_d6_ride_simon"):
        c "Sara's got a personal trainer now. Huge guy. Very funny, apparently."
        n "He says it lightly. A little too lightly, maybe; or maybe Sara is the one listening too hard."
        s "He's not my trainer. He's the gym's trainer."
        dr "A writer with a trainer. Next thing you know she'll be famous and we'll have to book an appointment."
    elif fatto("ep1_d6_parla_simon"):
        c "Sara's got a fan at the gym. He wants to read page fifty-one."
        dr "Only fifty-one? I'd want the whole thing."
        s "Nobody gets the whole thing. Not even [nome_compagno]."
    else:
        dr "And you two? Still disgustingly happy?"
        c "Disgustingly."

    n "Darius looks at the clock and swears softly: he's promised his sister he'd help her move a wardrobe."
    dr "We need a proper night. All of us, Joanie, her guy, everyone. Like before."
    c "You say that every time."
    dr "And every time you're working. That Daniel works you like a mule, mate."
    c "Daniel's just... demanding. It's a good job."
    dr "He's a mule-driver, that's what he is. One of these weekends. I'm serious."
    $ cg("The front door: Darius leaving with a two-finger salute, Josh leaning on the door frame, a croissant crumb still on his T-shirt", "images/cg/ep1/d7_04_darius_saluta.webp")
    n "He leaves the way he came: loud, quick, a two-finger salute from the stairs. [nome_compagno] closes the door himself."
    n "The flat feels a little emptier, the way it always does after Darius."
    $ nota_sara("amico", "[nome_compagno]'s best friend since school. Loud, kind, almost family.")
    return


## --- Pomeriggio: scrivere o uscire con il compagno -----------------------------------

label ep1_d7_pomeriggio:
    $ vai("casa", "Home — 2:30 p.m.")
    $ cg("Sunday sunlight in the living room: Sara turns from her laptop as Josh suggests a walk by the river", "images/cg/ep1/d7_pomeriggio_scelta.webp")
    n "After lunch the sun comes out, unexpected, as if it had changed its mind."
    c "It's nice out. We could walk down to the river. Ice cream. Ducks. Old people on benches. The full Sunday."
    sp "Or I could finally sit down and open that door."

    menu:
        sp "The afternoon."
        "Write.":
            $ confidence(2, "Sara writes a whole scene, and it works.")
            $ segna("ep1_d7_scrive")
            s "Can I have the afternoon? I think I'm close. With the door."
            c "Go. I'll be on the sofa, being elderly."
            $ cg("Sara writing at the table by the window in the afternoon light, completely absorbed; in the background Josh asleep on the sofa with a game controller on his chest", "images/cg/ep1/d7_05_scrivere.webp")
            n "She writes for three hours without looking up. Her heroine opens the door at a quarter past four."
            n "On the other side there's a room Sara didn't know she'd imagined: warm, full of someone else's things, and with no way to tell how long she's been standing there."
            sp "Oh. That's it. That's what was behind the door."
            n "And in the room, by the window, someone is waiting for her heroine. A man. He hasn't turned round yet."

            ## Corr +1 aggiunta il 21/11 (Jody): rende raggiungibile la soglia del giorno 8.
            menu:
                sp "What does she do?"
                "She asks him who he is.":
                    n "Her heroine asks his name, and he tells her, and the scene becomes a conversation. A good one. Careful, clever, safe."
                "She lets him come closer, without asking his name.":
                    $ corruption(1, "Sara writes a scene she wouldn't read aloud.")
                    $ segna("ep1_d7_scena_audace")
                    n "Her heroine doesn't ask. She lets him cross the room."
                    $ cg("Inside Sara's novel, from the heroine's point of view: her hand against the doorframe, the man close enough to see the weave of his shirt, his face out of frame", "images/cg/ep1/d7_05b_romanzo_soglia.webp")
                    n "She lets him stand close enough to feel the warmth of him, and the scene doesn't need a name."
                    $ cg("Sara writing at the table by the window in the afternoon light, completely absorbed; in the background Josh asleep on the sofa with a game controller on his chest", "images/cg/ep1/d7_05_scrivere.webp")
                    n "Sara writes it in one breath. When she reads it back her cheeks are burning, and she glances at the sofa as if she'd been caught."
                    sp "It's fiction. It's {i}her{/i}, not me."
                    sp "...I'm not reading this one to anybody."
            if fatto("ep1_d6_parla_simon"):
                sp "Page fifty-one. I'm well past it now."
                sp "Not that I'm going to bring it to anyone. Obviously."
            n "When she finally stretches, [nome_compagno] is asleep on the sofa, the controller rising and falling on his chest."
        "A walk by the river with [nome_compagno].":
            $ interest("josh", 2, "A Sunday just for the two of them.")
            $ segna("ep1_d7_gita")
            s "Ice cream. Ducks. The full Sunday. Let's go."
            $ vai("fiume", "The river path — 3:30 p.m.")
            $ ambiente("fiume")
            $ cg("A riverside path on a sunny autumn afternoon: Sara and Josh walking hand in hand with two ice-cream cones, Josh pointing at a group of ducks", "images/cg/ep1/d7_06_fiume.webp")
            n "The river path is full of families, dogs and couples doing exactly what they're doing. Sara doesn't mind. Today she likes being one of many."
            c "That duck is judging me."
            s "That duck has seen you dance."
            c "Everyone has seen me dance. Darius has a video."
            $ cg("A bench by the river at golden hour: Sara with her head on Josh's shoulder, eyes half closed, Josh looking at the water", "images/cg/ep1/d7_07_panchina.webp")
            n "They end up on a bench, her head on his shoulder, the ice cream long gone."
            c "When the novel comes out, we'll come here and read the reviews out loud. To the ducks."
            s "And if they're bad?"
            c "Then the ducks will be wrong."
            sp "This. This is what I'd write, if anyone believed in happy endings anymore."
    return


## --- Sera: a letto ---------------------------------------------------------------

label ep1_d7_sera:
    $ vai("camera", "The bedroom — 11:15 p.m.")
    $ ambiente(None)
    $ musica("notte")
    $ cg("The bedroom at night, the bedside lamp on: Josh lying on his back staring at the ceiling, Sara on her side next to him, propped on one elbow, listening", "images/cg/ep1/d7_08_letto.webp")
    n "In bed, with the lamp still on, [nome_compagno] stares at the ceiling the way he does when Monday is getting close."
    c "Next week's going to be bad."
    s "Bad how?"
    c "Daniel wants me on the late shift. Tuesday for sure, maybe more. «The team needs leadership», he says."
    sp "Daniel. Always Daniel."
    if fatto("ep1_d5_risposta_daniel"):
        sp "«At least he doesn't forget people. Only licences.» I said that to his face. I hope he hasn't taken it out on [nome_compagno]."
    c "It's fine. It's good, actually. It means he trusts me."
    s "Or it means he likes having you there until nine."
    c "...Or that."
    if fatto("ep1_d6_ride_simon"):
        c "Your trainer's funny, by the way."
        s "He's not my trainer."
        c "I know. I'm just saying. He's funny."
        sp "He's been holding that sentence since last night."

    menu:
        sp "He's tired. He's worried. And he's right here."
        "Take the initiative." (josh=30):
            $ interest("josh", 2, "Sara chose him tonight.")
            $ confidence(1, "Sara dared to start it herself.")
            $ segna("ep1_d7_iniziativa")
            n "Sara reaches over and switches off the lamp. Then she doesn't move back to her side of the bed."
            c "Oh. Hello."
            s "Hello. Stop thinking about Daniel."
            c "Who's Daniel?"
            $ cg("Darkness, only the streetlight through the curtains: Sara leaning over Josh and kissing him, smiling against his mouth, his hands in her hair", "images/cg/ep1/d7_09_iniziativa.webp")
            n "She kisses him, and she's smiling while she does it, because he's laughing softly against her mouth, surprised and grateful at the same time."
            ## Decisione del 19/11 con Jody: la scena non sfuma sul nero. Sara si
            ## spoglia, e Josh, per la prima volta (lo stress di Daniel), finisce
            ## appena si sfiorano. Sensuale, non esplicita: niente LM Studio.
            n "Then she sits up, astride him, the duvet sliding off her shoulders."
            $ cg("Darkness, cool streetlight through the curtains: Sara astride Josh on the bed, pulling her white T-shirt off over her head, topless, her red curls falling down her back, smiling down at him; Josh beneath her, glasses off, looking up at her in awe", "images/cg/ep1/d7_11_maglietta.webp")
            n "She pulls the T-shirt over her head and lets it fall somewhere on the floor. The streetlight draws a pale line along her ribs."
            n "[nome_compagno] looks at her the way he did the first time, years ago, as if he can't quite believe he's allowed."
            c "God. Sara."
            s "Shh. Stop thinking."
            n "She leans down over him, slowly, enjoying it: the warmth of his skin against hers, his breath catching, his hands on her hips."
            n "And then, before anything has really begun, he goes rigid beneath her. A sharp breath. A sound that isn't pleasure so much as surprise."
            n "Then nothing. Just his heart, hammering under her palm."
            c "...Oh no."
            c "Oh no, no. Sara, I'm sorry. That's never... that's never happened. I don't know what..."
            $ cg("Darkness, cool streetlight: Josh lying back with his forearm over his eyes, mortified; Sara beside him, the duvet held to her chest, smiling gently at him and stroking his curls", "images/cg/ep1/d7_12_scusa.webp")
            n "Sara looks at him for a moment. Then she smiles, because he looks so stricken, and because it's [nome_compagno]."
            s "Hey. It's fine. It happens."
            s "It's Daniel. It's this week. Come here."
            n "She pulls him against her, his head on her chest, and runs her fingers through his curls until his breathing slows."
            c "I'll make it up to you. I promise."
            s "I know. Sleep."
            $ segna("ep1_d7_josh_precoce")
            scene bg nero with fade
            $ cg("Sara lies awake in the cool streetlight while Josh sleeps beside her", "images/cg/ep1/d7_notte_sara_sveglia.webp")
            n "In a few minutes he's asleep, heavy and warm, one arm across her."
            n "Sara stays awake, staring at the ceiling in the dark."
            sp "I started it. I don't usually start it."
            sp "It's nothing. It's stress. It happens to everyone, the internet says so, and the internet knows everything."
            n "And yet there's something under her skin that won't settle: a warmth with nowhere to go, and a small, strange feeling she doesn't have a name for."
            sp "It's nothing."
        "She's tired: sleep.":
            $ segna("ep1_d7_dorme")
            s "Come here. Sleep. Monday can wait until Monday."
            $ cg("The bedroom in the dark: Sara and Josh asleep, spooning, his face in her hair; the streetlight drawing a thin line across the duvet", "images/cg/ep1/d7_10_dormono.webp")
            n "She switches off the lamp and curls into him. In five minutes he's breathing slow and deep."
            sp "Tomorrow: work. Then the gym. Simon said no excuses."
            sp "Joanie will drag me. Joanie always drags me."

    show expression Transform("images/cg/ep1/d6_rientro_notte_pianerottolo.webp", crop=(380, 105, 400, 225), xysize=(config.screen_width, config.screen_height)) as cg_corrente
    with dissolve
    n "Next door, behind a green door, a light stays on long after theirs goes out."
    return
