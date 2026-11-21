## =============================================================================
## EPISODE 1 — DAY 11 (Thursday)
## =============================================================================
## Calendar: docs/mese-1.md, day 11. Lunch: with Roberta (decision 18/11, instead
## of Jessica: caring, discreet, slightly odd, nothing revealed) or alone (Conf +1).
## Evening: Howard «finds» the keys (I20) and gives them back; retroscena: he had a
## copy made. Thank him with a handshake (Howard +1) or a hug (Howard +1).
## Decisions with Jody:
## - 19/11 Q&A: with the hug Howard holds her a beat too long and makes a bold
##   but light joke; Sara blushes and laughs: the first time she understands that
##   he desires her. With the handshake the line is softer and she half-misses it.
## - Howard's number arrives today, with the keys (telefono doc, 18/11). It's his
##   proposal: refusing is marked rifiuto_howard=True (Savior Complex, day 9).
## - 21/11: Howard's visit ladder. Every meeting brings an invitation; today's is
##   the first real one (step 2: the new cups). With the Savior Complex Sara can't
##   say no to everyday requests (slippers, texting Josh) and it feels like a dream.
## - Day 10: Sara wrote in the Taurus horoscope that something lost would come
##   back «and not alone».
## Reviewed with Jody on 21/11/2026 (invented details and Barbara's folder kept;
## stats kept, ladder gates raised; Howard's line after a refusal softened).
## Game text in English; comments in Italian.
## CG: docs/prompt-immagini/inquadrature-giorno-11.md. Finché mancano,
## compare la didascalia [CG].

label ep1_d11:
    call nuovo_giorno(11, "Thursday")
    call ep1_d11_pranzo
    call ep1_d11_chiavi
    call ep1_d11_retroscena
    return


## --- Pausa pranzo: Roberta o da sola (decisione 18/11) ----------------------------------

label ep1_d11_pranzo:
    $ vai("redazione", "The newsroom — 12:55 p.m.")
    $ musica("redazione")
    $ ambiente("redazione")
    n "Thursday. The horoscopes came out this morning. Nobody has said anything about them, which Sara chooses to take as a compliment."
    n "At five to one, a pastel-pink cardigan appears at the edge of her desk."
    $ cg("Roberta at the edge of Sara's desk at lunchtime, pastel cardigan, gold heart pendant, holding two paper bags from the deli and smiling a little too wide", "images/cg/ep1/d11_01_roberta_invito.webp")
    ro "Lunch? I got you one already. Tuna, no onions, extra lemon."
    s "That's... exactly what I always get."
    ro "I know. I notice people."
    sp "She said that on Monday too. The first day. It was sweet then."

    menu:
        sp "Lunch with Roberta?"
        "Eat with Roberta.":
            $ segna("ep1_d11_pranzo_roberta")
            $ cg("The small newsroom kitchen: Sara and Roberta at a little table with deli sandwiches, Roberta leaning in attentively, chin on her hand, the gold heart at her throat", "images/cg/ep1/d11_02_pranzo_roberta.webp")
            n "They eat in the little kitchen behind the copy desk. Roberta has brought napkins, two lemons and a tiny salt shaker shaped like a cat."
            ro "I've been here six years, you know. Longer than anyone except her."
            n "«Her». Not Barbara. Just «her», as if there were only one."
            ro "Your horoscopes were lovely. Taurus especially. Something lost that comes back... she read it out loud to me. Twice."
            s "She read my horoscopes out loud?"
            ro "She reads everything you write. She has a folder."
            n "Roberta says it the way you'd mention someone's birthday. Kindly. As if it were the most normal thing in the world."
            if fatto("ep1_d10_bottone_aperto"):
                ro "And yesterday, your blouse. She noticed. She was so pleased with you."
                sp "One button. She noticed one button. And she told Roberta."
                n "Sara's hand goes up to her collar before she can stop it."
            if fatto("ep1_d10_jessica_chiesto"):
                ro "Jess told me you asked her what happened to her. That's sweet. You worry about people."
                ro "But she's happy now. People are so much happier when they stop... pulling against things."
            ro "Anyway! Eat. You're too thin when you work too hard."
            sp "I'm not. I'm really, really not."
            n "Roberta watches her eat every bite, smiling. When Sara finishes, she clears the plates before Sara can move, and touches the little gold heart at her throat."
            $ nota_sara("capa", "Roberta: «She reads everything you write. She has a folder.»")
        "Eat alone, and write.":
            $ confidence(1, "Sara takes an hour for her novel.")
            $ segna("ep1_d11_pranzo_sola")
            s "That's so kind, Roberta. But I promised myself an hour with the novel today."
            ro "Of course. Of course you did. I'll leave it on your desk, then."
            n "She puts the paper bag down next to Sara's keyboard, very precisely, and goes."
            $ cg("A bench in a small square at lunchtime: Sara with a notebook on her knees, writing, a paper deli bag beside her, autumn leaves on the ground", "images/cg/ep1/d11_03_panchina.webp")
            n "Sara takes the sandwich to the bench in the little square across the road. Tuna, no onions, extra lemon."
            n "She writes four pages. Her heroine, in the warm room full of someone else's things, finds a drawer that isn't hers. She opens it."
            sp "Good. That's good. I don't know what's in the drawer yet, but that's good."
            n "When she looks up, there's a pink cardigan at the newsroom window on the second floor. It's gone before she can be sure."
    return


## --- Sera: Howard «ritrova» le chiavi (I20) ---------------------------------------------

label ep1_d11_chiavi:
    $ vai("pianerottolo", "The landing — 6:20 p.m.")
    $ ambiente(None)
    $ musica(None)
    $ suono("telefono_vibra")
    n "On the stairs, a message from [nome_compagno]: {i}Daniel strikes again. An hour late, maybe more. Sorry sorry sorry. Your doorman owes you.{/i}"
    sp "An hour on the doormat. Again."
    n "She has barely put her bag down when the green door next to hers opens."
    $ musica("howard")
    $ cg("The landing at dusk: Howard in the doorway of his green door, beaming, holding up Sara's ring of keys with the little silver fountain pen dangling from his finger", "images/cg/ep1/d11_04_howard_chiavi.webp")
    ho "Sara! Sara, Sara. Look. Look what I've got."
    n "He holds them up on one finger, like a magician. Her keys. The ring, the two keys, the little silver pen swinging and catching the light."
    s "My keys! Howard! Where...?"
    ho "Downstairs. Behind the post boxes, in the hall. I was getting my paper and there they were, winking at me."
    ho "You must have dropped them on Saturday, with all those bags."
    sp "Behind the post boxes. Of course. With the shopping. I'm such an idiot."
    sp "«Something you thought you had lost will come back to you sooner than you expect.» I wrote that. Yesterday."
    if fatto("ep1_howard_caffe") == "no":
        ho "I know you're very busy. I thought, at least I can do this for her."
    else:
        ho "I thought: Sara's going to be so happy. I've been listening for you on the stairs all afternoon."
    n "He holds them out. When she takes them, the metal is warm, as if it had been in his hand for a long time."
    s "Howard, thank you. Really. You have no idea."

    menu:
        sp "How do I thank him?"
        "A handshake.":
            $ interest("howard", 1, "Howard found Sara's keys.")
            $ segna("ep1_d11_stretta")
            $ cg("The landing: Howard holding Sara's hand in both of his, a little too long, smiling up at her; Sara smiling politely, the keys in her other hand", "images/cg/ep1/d11_05b_stretta.webp")
            n "She holds out her hand. Howard takes it in both of his, soft and warm and slightly damp, and doesn't let go straight away."
            ho "Such a small hand. You should be more careful with it. With everything."
            ho "Next time you lose something... you know where to knock."
            sp "Was that... a joke? It sounded like half of one."
            n "He lets go. Sara decides it was a joke. It's easier."
            $ nota_sara("howard", "He found the keys. Kind, clumsy, a little too attentive.")
        "A hug.":
            $ interest("howard", 1, "Howard found Sara's keys.")
            $ segna("ep1_d11_abbraccio")
            $ segna("ep1_d11_capisce_howard")
            $ cg("The landing: Sara hugging Howard in gratitude; Howard holding her a beat too long, his face close to her hair, a sly, pleased little smile; Sara's eyes wide over his shoulder, cheeks pink, about to laugh", "images/cg/ep1/d11_05_abbraccio.webp")
            n "She hugs him, quickly, the way you hug someone who has just saved your evening."
            n "Except that Howard doesn't make it quick. His arms close around her and stay there, one breath, two. She can feel him breathe in."
            if complesso_crocerossina:
                n "His hand settles at the small of her back, low, exactly where it was on Tuesday. Exactly as if it remembered the way."
            ho "Well, well."
            ho "If this is how I get paid every time I find something of yours..."
            ho "...I'll have to start looking very, very carefully."
            n "For a second Sara doesn't understand. Then she does, all at once, and her face goes hot from her collar to her hairline."
            sp "Oh."
            sp "Oh. Howard. He... he likes me. Like {i}that{/i}."
            n "And instead of being shocked, she laughs. A real laugh, surprised out of her, while she steps back out of his arms."
            s "Howard! Do you always think about these things?"
            ho "Only on good days, my dear. And this is a very good day."
            n "He smiles, pink to the ears, delighted with himself, like a boy who has said a rude word in church and got away with it."
            if fatto("ep1_d9_abbraccio"):
                sp "He's sixty-three. He lives next door. He cried in my arms on Tuesday."
            else:
                sp "He's sixty-three. He lives next door. He cried in his armchair on Tuesday."
            sp "And I'm laughing. Why am I laughing?"
            $ nota_sara("howard", "He found the keys. And when I hugged him, he made a joke... he likes me. Like that. I laughed.")

    ## Il numero di Howard (telefono, 18/11): è una sua proposta.
    ho "Listen. Let me give you my number. In case you lose something else. Or you're locked out. Or... anything."
    ho "I'm always in. You know that."

    menu:
        sp "His number."
        "Save it.":
            $ segna("ep1_d11_numero_howard")
            $ da_numero("howard")
            n "He reads it out slowly, twice, and watches her type it, as if he wanted to be sure she'd put it somewhere safe."
            n "She saves him as «Howard (next door)». He looks over her shoulder at the screen and seems absurdly pleased with the brackets."
        "«I'll just knock, Howard. It's quicker.»" (rifiuto_howard=True):
            ho "Of course. Of course. Knock. Anytime."
            n "He says it lightly. But his eyes go to the phone in her hand, and stay there a moment too long."

    ## La scala delle visite (21/11): ogni incontro, un invito. Qui il primo vero.
    ho "And... you said he's going to be an hour. Come in. Just for a coffee. To celebrate the keys."
    n "He says it looking at his slippers, with the hopeful face of a dog that already knows it's going to be told to get off the sofa."
    ho "I've got... I bought new cups. For guests."

    menu:
        sp "Coffee at Howard's?"
        "Go in for a coffee.":
            call ep1_d11_visita
        "«Another time, Howard. I'm shattered.»" (rifiuto_howard=True):
            $ segna("ep1_d11_rifiuta_invito")
            ho "Of course. Of course. Another time. The cups aren't going anywhere."
            n "He smiles, nods twice, and closes the green door very gently, as if not to disturb her."
            $ vai("casa", "Home — 6:35 p.m.")
            $ musica("casa")
            n "For the first time in five days, Sara opens her own door with her own keys. It feels absurdly good."
            n "She drops them into the bowl by the door. The little silver pen clinks against the ceramic, the way it always did."
            call inizio_retroscena
            rs "Behind the green door, Howard puts the two new cups back in the cupboard, side by side, very carefully."
            rs "He isn't disappointed. A no today is a yes another day. He has all the time in the world. And she has such a kind heart."
            $ retroscena("howard", "Sara turned down his invitation. He didn't mind: he can wait.")
            call fine_retroscena

    ## Josh arriva e ringrazia Howard.
    $ vai("pianerottolo", "The landing — 7:30 p.m.")
    $ musica("howard")
    $ suono("chiave_serratura")
    n "At half past seven [nome_compagno] runs up the stairs, out of breath, tie loosened."
    $ cg("The landing: Josh, out of breath in his work clothes, shaking Howard's hand enthusiastically; Sara between them holding up her keys; the brown and the green doors side by side", "images/cg/ep1/d11_06_josh_howard.webp")
    if fatto("ep1_d11_visita"):
        n "He knocks on the green door to collect her."
        if fatto("ep1_d11_bottoni"):
            n "At the knock, Sara's hands fly to her blouse. She does the buttons up so fast she gets one wrong, and doesn't notice."
        n "Howard opens the door with Sara just behind him."
    else:
        n "Sara shows him the keys before he can even say hello. He knocks on the green door at once."
    c "Howard found them? Behind the post boxes? No way. Howard, you legend. Come here."
    n "[nome_compagno] shakes his hand with both of his, the way he shakes hands with clients he likes. Howard lets himself be shaken, beaming."
    c "I told you they'd turn up. Didn't I tell you? Saved us a locksmith. We owe you a beer. Several beers."
    ho "Oh, no, no. It was nothing. That's what neighbours are for."
    if fatto("ep1_d11_capisce_howard"):
        n "Over [nome_compagno]'s shoulder, Howard's eyes find Sara's for a moment. Then he looks away, shy, like a boy."
        sp "He knows I know. And [nome_compagno] is offering him beers."
        sp "It was a joke. It was just a silly old man's joke."
    $ vai("casa", "Home — 7:40 p.m.")
    $ musica("casa")
    if fatto("ep1_d11_pantofole"):
        n "It's only in their own hallway, while [nome_compagno] hangs up his jacket, that Sara looks down."
        n "She's still wearing Howard's slippers. Pink. Brand new. A size too big. She walked out in them and didn't notice."
        c "Nice slippers."
        s "They're... Howard's. I'll give them back tomorrow."
        n "She puts them neatly by the door, next to her own shoes, and doesn't think about them again."
        sp "Strange evening. Like a dream you can't quite remember the middle of."
    if fatto("ep1_d11_bottoni") and not fatto("ep1_d11_pantofole"):
        n "In the hallway mirror she sees her blouse buttoned one hole off, crooked. She fixes it without thinking."
        sp "Strange evening. Like a dream you can't quite remember the middle of."
    sp "Something lost comes back. And not alone."
    sp "Madame Celeste would be proud of me."
    return


## --- La visita: step 2 della scala (bozza 21/11) -------------------------------------------

label ep1_d11_visita:
    $ howard_visite += 1
    $ segna("ep1_d11_visita")
    $ vai("casa_howard", "Howard's flat — 6:40 p.m.")
    $ ambiente("tv_howard")
    $ cg("Howard's living room a little tidier than before: the newspapers stacked in one corner, two brand-new white cups on the table; Howard pouring coffee, Sara on the sofa with her coat off", "images/cg/ep1/d11_08_tazze_nuove.webp")
    n "The flat is different. Not clean, not really. But the newspapers have been stacked in one corner, the plates are gone, and there's a window open a crack."
    n "On the table, two white cups, still with the price stickers on the bottom."
    ho "I tidied up a bit. Not for you. Well. A bit for you."
    s "Howard, it looks... much better."
    ho "Sit, sit. Not there, the spring's gone. There. Yes."

    if complesso_crocerossina:
        ## Il Complesso (decisione 21/11): non sa dire di no; lui chiede un passo alla volta.
        ho "And take your boots off. Your feet must be frozen. Here."
        n "He puts a pair of slippers in front of her. Pink, fluffy, brand new, the label still on. A size too big."
        sp "Slippers. He bought me slippers. Why would I put on his... slippers..."
        n "She's already unzipping her boots."
        sp "Oh, whatever. It's not a big deal. My feet {i}are{/i} cold."
        $ segna("ep1_d11_pantofole")

    n "Howard makes the coffee and asks about the novel. Not to be polite. He actually wants to know."
    ho "Read me a bit. Go on. Just a paragraph. I've never had a writer in my house."
    if fatto("ep1_d11_pranzo_sola"):
        n "So she reads him what she wrote at lunch: her heroine in the warm room full of someone else's things, opening a drawer that isn't hers."
        n "Howard listens without moving, his cup halfway to his mouth. When she finishes, he's quiet for a long moment."
        ho "And what's in the drawer?"
        s "I don't know yet."
        ho "No. You don't. Not yet."
    else:
        n "So she reads him a page from her phone, the one with the door. Howard listens without moving, his cup halfway to his mouth."
        ho "Beautiful. Beautiful. You've got a gift, you know. Everybody can see it. Your face, your... everything."
    ho "You're a special girl, Sara. I don't say that to everyone. I don't say anything to anyone, actually."

    if complesso_crocerossina:
        ho "Text him. [nome_compagno]. Tell him you're here, so he doesn't worry. Tell him I'll feed you."
        n "She takes out her phone. She types. {i}I'm at Howard's, he found my keys!! Having a coffee, see you in a bit.{/i}"
        sp "Why am I telling him what Howard told me to tell him?"
        sp "It's the truth, anyway. It's nothing."
    else:
        n "She sends [nome_compagno] a quick message, so he won't find the landing empty: {i}Howard found my keys!! Having a coffee next door.{/i}"

    menu:
        sp "Another coffee?"
        "Stay for a second coffee.":
            $ interest("howard", 2, "Sara stayed for a second coffee.")
            n "The second coffee lasts forty minutes. He tells her about his mother's cat, about the factory canteen, about a woman named Lorna who almost married him in 1987."
            n "Sara laughs more than she expected to. The flat smells a little less of closed rooms, and a little more of coffee."
            if fatto("ep1_d11_capisce_howard"):
                ## I due sguardi e i bottoni (Jody, 21/11): ogni bottone Corr +1,
                ## Josh -1, Howard +1. Col Complesso non si può evitare.
                $ cg("Howard's sofa: Howard talking, his eyes resting on Sara's chest instead of her face; Sara, coffee cup in hand, has just noticed", "images/cg/ep1/d11_09_sguardo.webp")
                n "Halfway through Lorna, she catches his eyes resting on her. Not on her face."
                n "He doesn't look away at once. He finishes his sentence first."
                menu:
                    sp "He's looking. Right there."
                    "Undo a button of her blouse.":
                        $ corruption(1, "Sara undoes a button for Howard.")
                        $ interest("josh", -1, "Sara undoes a button for another man.")
                        $ interest("howard", 1, "Sara undid a button for him.")
                        $ segna("ep1_d11_bottoni", 1)
                        n "Her fingers find the top button of her blouse, as if they'd decided on their own. It slips open."
                        sp "What am I doing? It's warm in here. It's the coffee. It's..."
                        sp "No. It's that he's looking. And I want him to keep looking. It's one button. It's nothing."
                        n "Howard's sentence stops in the middle. Then it starts again, a little hoarse."
                    "Pretend not to notice." (rifiuto_howard=True):
                        n "She pretends not to notice. She asks what happened to Lorna."
                n "A little later, while he's pouring the last of the coffee, it happens again. His eyes, the same place, slower this time."
                $ cg("Howard's sofa: Howard pouring coffee, his eyes lingering on Sara's open collar; Sara holding his gaze, cheeks pink, a small smile", "images/cg/ep1/d11_09b_sguardo.webp")
                menu:
                    sp "Again."
                    "Undo another button.":
                        $ corruption(1, "Sara undoes another button for Howard.")
                        $ interest("josh", -1, "Sara undoes a button for another man.")
                        $ interest("howard", 1, "Sara undid another button for him.")
                        $ segna("ep1_d11_bottoni", (fatto("ep1_d11_bottoni") or 0) + 1)
                        n "Another button. She does it slowly this time, and she watches his face while she does it."
                        if fatto("ep1_d11_bottoni") == 2:
                            sp "Two buttons. Sara, what on earth... in Howard's living room, with [nome_compagno] on his way home..."
                        else:
                            sp "Now? Why now, why for him? Sara, what on earth..."
                        sp "But look at him. Nobody has ever looked at me like that. As if I were a miracle."
                        sp "It's just a blouse. I'll do it up before I go. It doesn't count."
                        n "Howard puts the coffee pot down very carefully, as if it might break. He doesn't say a word. He doesn't need to."
                    "Pretend not to notice." (rifiuto_howard=True):
                        n "Once again she pretends not to notice. It's getting harder."
        "«I should go, really.»" (rifiuto_howard=True):
            $ interest("howard", 1, "A coffee at Howard's.")
            ho "Of course. Of course. You've had a long day."
            n "He doesn't insist. He never insists. He just looks at her with those wet, grateful eyes until she feels guilty for leaving a minute early."
    $ ambiente(None)
    $ nota_sara("howard", "Coffee at his flat. He'd tidied up for me, and bought new cups. He listened to my novel.")
    call inizio_retroscena
    rs "Later, when she's gone, Howard washes one cup. Only one."
    rs "The other, with the faint mark of her lips on the rim, he puts away in the cupboard just as it is."
    $ retroscena("howard", "He kept the cup Sara drank from, unwashed.")
    call fine_retroscena
    return


## --- Retroscena: la copia ------------------------------------------------------------------

label ep1_d11_retroscena:
    $ luogo_corrente = ""
    scene bg nero with fade
    $ musica("notte")
    call inizio_retroscena
    $ cg("Retroscena: Howard's bedside table at night under a yellow lamp: a single shiny, newly cut brass key lying on a folded piece of pale pink lace, the drawer half open", "images/cg/ep1/d11_07_copia.webp")
    rs "Yesterday afternoon, at the key-cutting kiosk by the station, the man asked him: «Just the one copy?»"
    rs "Just the one. He didn't need more."
    rs "Now it lies on his bedside table, new and shining, on a small square of pale pink lace."
    rs "He doesn't plan to use it. Not tonight. Perhaps not for a long time."
    if fatto("ep1_d11_capisce_howard"):
        rs "She laughed. She didn't push him away. She laughed."
        rs "Howard turns the key over in his fingers and smiles at the wall, the one with her bed on the other side."
    else:
        rs "It's enough to know he can. Howard turns the key over in his fingers and smiles at the wall, the one with her bed on the other side."
    $ retroscena("howard", "He gave Sara her keys back, but first he had a copy made. He keeps it in his bedside drawer, on her pink lace.")
    call fine_retroscena
    return
