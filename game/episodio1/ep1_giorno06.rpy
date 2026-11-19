## =============================================================================
## EPISODE 1 — DAY 6 (Saturday)
## =============================================================================
## Calendar: docs/mese-1.md, day 6. Morning: the shopping, Howard 2, and the
## behind-the-scenes theft (underwear from the clothes horse + Sara's keys from
## the bowl by the door, decided 16/11). Afternoon: getting ready for the night,
## Joanie and the short dress; Sara can't find her pink knickers. Evening: a bar
## with Joanie and [nome_compagno], Simon 3 (Simon is different outside the gym).
## Seeds: from tonight it's always [nome_compagno] who opens the door, so Sara
## doesn't notice the missing keys until day 9.
## Draft for Jody's review. Game text in English; comments in Italian.
## CG: docs/prompt-immagini/inquadrature-giorno-06.md. Finché mancano,
## compare la didascalia [CG].

init python:
    def vestito_d6(nome):
        """CG del locale con Sara in vista: variante «_corto» se ha il vestito di
        Joanie e l'immagine esiste; altrimenti quella col vestito grigio."""
        base = "images/cg/ep1/d6_%s.webp" % nome
        corto = "images/cg/ep1/d6_%s_corto.webp" % nome
        if fatto("ep1_d6_vestito_corto") and renpy.loadable(corto):
            return corto
        return base


label ep1_d6:
    call nuovo_giorno(6, "Saturday")
    call ep1_d6_spesa
    call ep1_d6_pomeriggio
    call ep1_d6_locale
    return


## --- Mattina: la spesa, Howard 2 ----------------------------------------------------

label ep1_d6_spesa:
    $ vai("pianerottolo", "The landing — 10:10 a.m.")
    $ ambiente(None)
    $ musica("casa")
    $ cg("The stairwell: Sara climbing the last flight with four heavy shopping bags, out of breath, a baguette sticking out of one bag", "images/cg/ep1/d6_01_scale_borse.webp")
    n "Saturday is [nome_compagno]'s one lie-in. Sara left him asleep, diagonally, with the whole bed to himself."
    n "Four shopping bags. Three flights of stairs. No lift."
    sp "Next time we go together. Next time he carries the water."
    $ musica("howard")
    $ cg("The landing: Howard hurrying out of his green door in a cardigan and slippers, arms already held out towards Sara's shopping bags", "images/cg/ep1/d6_02_howard_aiuta.webp")
    ho "Let me, let me! Give those here."
    s "Howard, really, it's fine..."
    ho "Nonsense. What are neighbours for?"
    if fatto("ep1_d5_howard_minuto"):
        ho "Two days in a row I get to see you. Lucky me."
    n "He takes three bags out of four before she can say no. They are heavier than he expected; he doesn't let it show. Almost."

    $ vai("casa", "Home — 10:15 a.m.")
    $ suono("chiavi_ciotola")
    $ cg("The hall: Sara dropping her keys into the ceramic bowl on the cabinet; the keyring is a small silver fountain pen; behind her, a clothes horse with drying laundry by the radiator", "images/cg/ep1/d6_03_chiavi_ciotola.webp")
    n "Sara drops her keys into the bowl by the door, the way she always does. The little silver fountain pen clinks against the ceramic."
    ho "Oh, look at that. A pen! For the writer."
    s "[nome_compagno] gave it to me. When I started the novel."
    ho "Lovely. Lovely thing."
    n "Howard carries the bags into the kitchen and puts them on the table, one by one, very carefully. His eyes go to the closed bedroom door."
    ho "He's sleeping? On a Saturday morning, while you carry the shopping? Ha. Young men."
    s "He works hard all week."
    ho "Of course. Of course he does."

    menu:
        sp "He carried three bags up three flights. At his age."
        "Thank him.":
            $ interest("howard", 1)
            s "Thank you, Howard. Really. You saved my arms."
            ho "Anytime. You know where I am."
            n "Sara turns to the fridge and starts putting things away: milk, yoghurt, the cheese [nome_compagno] likes. Behind her, Howard takes his time to say goodbye."
        "Insist on making him a coffee.":
            $ interest("howard", 2, "Howard will remember that coffee.")
            $ segna("ep1_d6_caffe_howard")
            s "At least let me make you a coffee. I insist."
            ho "Oh, no, no, I couldn't... well. If you insist."
            $ cg("The kitchen: Sara at the stove with her back to the room, filling a moka pot; Howard sitting at the kitchen table, his cardigan buttoned wrong, looking around", "images/cg/ep1/d6_04_moka.webp")
            n "Sara fills the moka and puts it on the stove, her back to the room. Howard sits at the kitchen table and looks around as if he were in a museum."
            ho "So tidy. So bright. Mine is... well. You've never seen mine."
            n "The moka starts to gurgle. Howard gets up. To stretch his legs, he says."

    call inizio_retroscena
    $ cg("Behind the scenes: the hall seen from the kitchen doorway; Howard's hand slipping something small and pale pink from the clothes horse into his cardigan pocket, his other hand hovering over the key bowl", "images/cg/ep1/d6_05_furto.webp")
    rs "Sara has her back to him. Howard's eyes go to the clothes horse by the radiator."
    rs "A quick movement. Something small, pale pink and lacy disappears into the pocket of his cardigan."
    rs "Then his eyes go down to the bowl. The ring with the little silver pen follows the same way, without a sound."
    rs "When Sara turns around, he's already back in the doorway, with his awkward smile."
    $ retroscena("howard", "He stole a piece of Sara's underwear from the clothes horse in the hall.")
    $ retroscena("howard", "He also stole Sara's house keys, the ring with the silver pen, from the bowl by the door.")
    $ via_cg()
    call fine_retroscena

    if fatto("ep1_d6_caffe_howard"):
        n "Howard drinks his coffee in three sips, burns his tongue, and says it's the best coffee he's had in years."
        ho "You'll make someone very happy, you know. Well. You already do. Of course."
    ho "Have a good Saturday, Sara. Really... a good Saturday."
    n "The door closes. On the landing, Howard's slippers don't move for a while. Then his green door closes too."
    $ nota_sara("howard", "He helped with the shopping. Lonely, a bit clumsy, a good heart.")
    $ tappa("howard", 2)
    return


## --- Pomeriggio: prepararsi, Joanie e il vestito -------------------------------------

label ep1_d6_pomeriggio:
    $ vai("camera", "The bedroom — 5:30 p.m.")
    $ musica("casa")
    $ cg("The bedroom: the bed covered with dresses; Joanie sitting cross-legged among them holding up a short emerald green satin dress; Sara in a bathrobe, hair wet, laughing", "images/cg/ep1/d6_06_vestiti_letto.webp")
    n "Joanie arrives at half past five with a bottle of prosecco, a bag of make-up and a plan."
    ch "Tonight we go out like it's ten years ago. Mark's at his brother's, [nome_compagno] is coming, and you are wearing something that isn't navy."
    if fatto("ep1_d5_joanie"):
        ch "Two nights out in a row, Sara. I'm so proud I could cry."
    s "We're going to a bar, Jo. Not the Oscars."
    ch "Every night is the Oscars if you dress right."
    n "Sara digs through the drawer, then the clothes horse in the hall, then the drawer again."
    ch "Lost something?"
    s "My good knickers. The pale pink ones, with the lace. I washed them on Thursday, I'm sure."
    ch "Tragic. Wear the black ones. Nobody's going to check."
    sp "They were on the clothes horse. I'm sure they were."
    sp "Must be still in the washing machine. Or stuck in a sheet. Or I put them somewhere stupid."
    sp "Never mind."

    n "Joanie holds up two dresses: one in each hand, like a judge at a fair."
    ch "Option one: the grey one. Pretty, decent, perfect for a funeral."
    ch "Option two: this. Short. Green. Mine. Fits you better than me, which I will never forgive."

    menu:
        sp "Joanie's dress is... very short."
        "The grey dress.":
            $ segna("ep1_d6_vestito_sobrio")
            s "The grey one. I want to dance, not to be arrested."
            ch "Funeral it is. At least let me do your eyes."
            $ cg("Sara in front of the bedroom mirror in a simple knee-length grey dress, Joanie behind her doing her eyeliner, both smiling", "images/cg/ep1/d6_07_vestito_grigio.webp")
            n "In the mirror, Sara looks like Sara. Pretty, Joanie says, and almost means it as a compliment."
        "The short dress Joanie picked.":
            $ corruption(1, "Sara likes how she looks in Joanie's dress.")
            $ confidence(1, "Sara dares a little.")
            $ segna("ep1_d6_vestito_corto")
            s "...Give me the green one. Before I change my mind."
            $ cg("Sara in front of the bedroom mirror in Joanie's short emerald green satin dress, surprised by herself, tugging the hem down; Joanie behind her clapping silently", "images/cg/ep1/d6_08_vestito_corto.webp")
            n "Sara tugs the hem down. It goes back up. She tugs it down again."
            ch "Stop pulling. It's supposed to be there. That's the whole point."
            sp "That's a lot of leg. That's... all the leg."
            sp "I look like someone who goes out on Saturday nights."
            $ cg("The bedroom doorway: Josh in his shirt, freezing mid-step at the sight of Sara in the short green dress, mouth slightly open", "images/cg/ep1/d6_09_josh_vede.webp")
            c "Wow. I mean... wow. Is that legal?"
            ch "Barely. You're welcome."
    return


## --- Sera: il locale, Simon 3 --------------------------------------------------------

label ep1_d6_locale:
    $ vai("casa", "Home — 9:15 p.m.")
    n "At the door, out of habit, Sara's hand reaches for the bowl."
    c "Leave it, I've got mine. Come on, Joanie's already downstairs shouting."
    $ cg("Close-up of the ceramic key bowl on the hall cabinet: only one set of keys left inside, Josh's hand lifting it out", "images/cg/ep1/d6_10_ciotola.webp")
    n "[nome_compagno] scoops his keys out of the bowl and locks the door behind them. Sara doesn't look down."

    $ vai("locale", "The Lantern — 10:00 p.m.")
    $ ambiente("locale")
    $ musica("locale")
    $ cg("A busy bar on Saturday night: warm lights, a small dance floor at the back; Sara, Josh and Joanie at a high table with three drinks", vestito_d6("11_locale"))
    n "The Lantern is loud, warm and crowded: a long bar, a dance floor the size of a living room, music that makes the glasses hum."
    n "They've just got their drinks when someone calls Joanie's name from the bar."
    si "Hey! My athletes!"
    $ cg("Simon at the bar in a fitted dark shirt with the sleeves rolled up, a beer in hand, grinning and waving: relaxed, nothing like the trainer at the gym", "images/cg/ep1/d6_12_simon_bancone.webp")
    $ incontra("simon")
    n "It takes Sara a second to recognise him. No tracksuit, no whistle-voice. A dark shirt with the sleeves rolled up, a beer, a grin."
    ch "Simon! Come here! This is [nome_compagno], Sara's boyfriend."
    si "Nice to meet you, man. Keep an eye on her: at the gym she's got scary potential."
    c "Really? She didn't tell me."
    s "Because it isn't true."
    si "Trust a professional."

    if fatto("ep1_d6_vestito_corto"):
        if fatto("ep1_top_joanie"):
            si "Didn't recognise you without the black top. Joanie's dresses too, huh?"
        else:
            si "Didn't recognise you without the tent."
        n "His eyes stay on the green dress for a moment. Just a moment. Then they come back to her face, and stay there."
        sp "He looked. And then he looked at me. Those are two different things."
    else:
        if fatto("ep1_top_joanie"):
            si "Didn't recognise you without the black top."
        else:
            si "Didn't recognise you without the tent."
        s "The tent is resting. It had a hard week."

    $ cg("Simon leaning on the high table telling a story with big gestures; Joanie doubled over laughing, Josh laughing too, Sara watching Simon with curiosity", vestito_d6("13_simon_racconta"))
    n "Simon stays for a round. He tells them about the client who brings his cat to the gym in a backpack, about the old lady who out-squats the bodybuilders, about the time he fell off a treadmill in front of a whole class."
    n "He makes fun of himself before anyone else can. He makes [nome_compagno] laugh. He makes Joanie laugh far too much."
    sp "At the gym he's all «chest up» and «weight on your heels». Here he's someone else."
    sp "Looser. Funnier. As if he'd left the trainer in his locker."
    c "He's... big, isn't he. Your trainer."
    s "He's not my trainer. He's the gym's trainer."
    c "He's very big."
    $ nota_sara("simon", "Outside the gym he's spontaneous and funny. A different man.")

    $ cg("The dance floor lit up in warm colours; Josh at the edge of it holding out his hand to Sara, a little shy; Simon at the table behind her, mid-sentence", vestito_d6("14_ballare"))
    n "The DJ puts on a song everybody knows. Joanie shrieks. [nome_compagno] holds out his hand, a little shy, the way he did at their first party."
    c "Dance with me? I'll be terrible. I promise."
    si "Go, go. I was just about to tell the story of the protein shake and the fire alarm."

    menu:
        sp "The song, or the story?"
        "Dance with [nome_compagno].":
            $ interest("josh", 2, "Sara dances with him.")
            $ segna("ep1_d6_balla_josh")
            $ cg("Sara and Josh dancing badly and happily in the middle of the crowd, Sara laughing with her head thrown back", vestito_d6("15_ballo_josh"))
            n "[nome_compagno] dances like a man assembling furniture without the instructions. Sara laughs so hard she has to hold on to him."
            c "I told you. Terrible."
            s "Perfectly terrible."
            n "When the song ends she looks back towards the table. Simon is telling Joanie something, and Joanie is laughing with her hand on his arm."
        "Stay and talk with Simon.":
            $ interest("simon", 2, "Simon liked talking to you.")
            $ segna("ep1_d6_parla_simon")
            s "Go with Joanie, I want to hear about the fire alarm."
            c "Traitor."
            $ cg("Sara and Simon at the high table, talking; Simon listening with his chin propped on his fist, Sara gesturing as she speaks; the dance floor blurred behind them", vestito_d6("16_sara_simon"))
            n "The fire alarm story lasts two minutes. Then, somehow, they're talking about her."
            si "So what do you do, when you're not dying on my mats?"
            s "I write. For a paper. And... a novel. Slowly."
            si "A novel? Seriously? That's cool. I can barely write a workout plan."
            si "Bet you're the type who gives up on page fifty, though. Like on the treadmill at minute ten."
            s "Excuse me? Minute twelve."
            si "Prove it. Monday. No excuses."
            sp "He remembers how long I lasted on the treadmill."
        "Laugh a little too much at Simon's jokes.":
            $ interest("simon", 3, "Simon liked making you laugh.")
            $ corruption(1, "Sara forgets herself for a moment.")
            $ suspicion(1, "[nome_compagno] noticed.")
            $ segna("ep1_d6_ride_simon")
            s "Go ahead, I'll be right there. I need to hear this."
            $ cg("Sara at the high table laughing helplessly at Simon's story, one hand on his forearm; in the background, Josh standing alone at the edge of the dance floor, looking at them", vestito_d6("17_ride_simon"))
            n "She isn't right there. The protein shake story gets better and better, and Sara laughs until her eyes water, one hand on Simon's forearm."
            n "It's a very solid forearm. She notices that, and then she notices that she noticed."
            n "At the edge of the dance floor, [nome_compagno] stands alone for the whole song, his drink in his hand."
            c "You two get on well."
            s "He's funny."
            c "I'm funny."
            s "You are. You're very funny."
            sp "He's not angry. He's just... watching me. As if he were trying to remember something."

    si "Right, I'm off, my friends are waiting. Sara: Monday, no excuses."
    if fatto("ep1_d6_parla_simon"):
        si "And bring me page fifty-one."
    ch "She'll be there. I'll drag her."
    n "Simon disappears into the crowd, his shoulders parting it like a door. Sara follows him with her eyes, just for a second. Then she looks for [nome_compagno]."
    $ tappa("simon", 2)

    $ vai("pianerottolo", "The landing — 1:40 a.m.")
    $ ambiente(None)
    $ musica("notte")
    n "They climb the stairs in silence, giggling, her shoes in her hand. [nome_compagno] opens the door with his keys."
    n "On the landing, the line of light under Howard's green door goes out as they pass."
    sp "He's still awake. At this hour. Poor man, he can't sleep either."
    if fatto("ep1_d6_ride_simon"):
        sp "I laughed too much tonight. Did I? It was just a funny story."
        sp "[nome_compagno] was quiet in the taxi. He's tired. That's all."
    elif fatto("ep1_d6_parla_simon"):
        sp "Page fifty-one. He was joking. Of course he was joking."
    else:
        sp "Perfectly terrible. I'd forgotten how much I like dancing with him."
    return
