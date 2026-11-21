## =============================================================================
## EPISODE 1 — DAY 5 (Friday)
## =============================================================================
## Calendar: docs/mese-1.md, day 5. Before work: Howard on the landing (Howard 1),
## [nome_compagno]'s driving licence forgotten on the hall cabinet. Lunch break:
## [nome_compagno]'s office, Daniel 2. Evening: [nome_compagno] is tired, a film
## on the sofa or out with Joanie (decision 18/11: Joanie asks about the company
## dinner and teases Sara about Daniel, no new choices or scores).
## Seeds: the key bowl by the door (Howard steals the keys on day 6), Howard
## knows Sara's timetable, Daniel crosses the floor to be in that doorway.
## Draft for Jody's review. Game text in English; comments in Italian.
## CG: docs/prompt-immagini/inquadrature-giorno-05.md. Finché mancano,
## compare la didascalia [CG].

label ep1_d5:
    call nuovo_giorno(5, "Friday")
    call ep1_d5_mattina
    call ep1_d5_howard
    call ep1_d5_ufficio
    call ep1_d5_sera
    return


## --- Prima del lavoro: la patente ------------------------------------------------

label ep1_d5_mattina:
    $ vai("casa", "Home — 8:25 a.m.")
    $ ambiente(None)
    $ musica("casa")
    $ cg("The hall of the flat: a small cabinet by the front door, a ceramic bowl full of keys, and a driving licence left beside it", "images/cg/ep1/d5_01_patente.webp")
    n "[nome_compagno] left at seven, a slice of toast in his mouth and his tie in his pocket."
    n "His driving licence did not leave with him. It's on the hall cabinet, next to the bowl where they both drop their keys."
    sp "He drives the company car this afternoon. Without this he's stuck."
    $ suono("telefono_vibra")
    n "Sara sends him a photo of it. The answer comes back in four seconds."
    c "NO."
    c "You are an angel. A saint. Lunch? My office is ten minutes from yours. I'll buy you the bad coffee from the machine."
    s "Deal. The bad coffee had better be good."
    $ suono("chiavi_ciotola")
    n "She slips the licence into her bag, takes her keys from the bowl, and opens the door."
    return


## --- Howard 1: il pianerottolo -----------------------------------------------------

label ep1_d5_howard:
    $ vai("pianerottolo", "The landing — 8:30 a.m.")
    $ musica("howard")
    $ cg("The landing: Howard in a faded dressing gown at his half-open door, a folded newspaper in his hand, smiling awkwardly at Sara as she locks her door", "images/cg/ep1/d5_02_howard_pianerottolo.webp")
    $ incontra("howard")
    n "The door next to theirs is already open. It usually is, at this hour."
    ho "Oh! Good morning, Sara. Sorry, sorry... did I startle you?"
    s "Morning, Howard. No, I'm just in a rush."
    ho "You're late today. You usually leave at twenty past."
    n "He says it kindly, as if he were talking about the weather."
    sp "Does he time me?"
    sp "No. He's retired. He has nothing to do but notice things. Poor man."
    ho "Always running, you young people. Me, I have all the time in the world."
    n "He laughs at his own joke, a little too long. Then he stops, and looks at her as if he were waiting for something."

    menu:
        sp "He wants to chat. He always wants to chat."
        "Stop for a minute.":
            $ interest("howard", 2, "Howard treasured your minute.")
            $ segna("ep1_d5_howard_minuto")
            $ cg("Close-up of Howard, delighted, clutching his newspaper to his chest like a schoolboy, his eyes shining a little too much", "images/cg/ep1/d5_03_howard_felice.webp")
            s "How's your back?"
            ho "You remembered! Better, much better. You're always so kind, you are."
            if fatto("ep1_aperitivo_accettato"):
                ho "You came home late last night. I heard your shoes on the stairs. In your hand, weren't they? Ha!"
                sp "He heard me take my shoes off?"
            elif fatto("ep1_d4_capitolo_tre"):
                ho "Your kitchen light was on until after midnight. Working hard, eh? The novel?"
                sp "How does he know about the novel?"
                sp "...I must have told him. At some point. I tell everybody."
            else:
                ho "A quiet evening, last night. Television. I could hear it a little, through the wall. Nice, a quiet evening."
            ho "If you need anything, anything at all, I'm right here. Next door. Day or night."
            s "That's sweet, Howard. Thank you."
            ho "Sweet. Ha. Nobody's called me sweet since... well."
        "Cut it short: she's late.":
            s "Sorry, Howard, I really have to run!"
            ho "Of course, of course... off you go."
            $ cg("The empty stairwell seen from above: Sara running down the stairs, and on the landing Howard still standing at his door, the newspaper closed in his hand", "images/cg/ep1/d5_04_howard_scale.webp")
            n "When Sara turns at the corner of the stairs, he's still there on the landing, the newspaper closed in his hand."
            n "His door doesn't close until she's out of the building."

    $ nota_sara("howard", "The neighbour. A bit odd. Lonely, but kind.")
    $ tappa("howard", 1)
    return


## --- Pausa pranzo: Daniel 2, la patente ---------------------------------------------

label ep1_d5_ufficio:
    $ vai("ufficio_compagno", "[nome_compagno]'s office — 1:05 p.m.")
    $ musica("casa")
    $ ambiente("ufficio")
    $ cg("An open-plan corporate office with glass walls: Josh at his desk among spreadsheets, jumping up with relief as Sara arrives holding up the driving licence", "images/cg/ep1/d5_05_josh_patente.webp")
    n "[nome_compagno]'s floor smells of carpet and printer toner. Rows of desks, glass walls, a coffee machine that has been broken since spring."
    c "My hero."
    s "Your licence. And you owe me a coffee."
    c "The machine's broken. I owe you a coffee in a place with a machine that works. Tonight, maybe? I'll be..."
    $ cg("Daniel leaning against the frame of a glass door, a paper coffee cup in hand, amused, watching the two of them", "images/cg/ep1/d5_06_daniel_stipite.webp")
    $ musica("daniel")
    da "He'll be here until seven, I'm afraid. Good afternoon, Sara."
    n "Nobody heard him arrive. He's leaning against the frame of the glass door, a coffee in his hand. A coffee from somewhere else."
    da "Did you come all this way to bring him his licence? That's devotion."
    da "Do you know, Sara, how many times a week your [nome_compagno] gets behind the wheel for this company? Five. And today he forgot how."
    c "It happened once, Daniel..."
    da "Once is how it starts. Lucky there's someone at home who thinks for two."
    n "Two colleagues at the nearest desks laugh, then look down at their screens very quickly."
    $ cg("Close-up of Sara holding Josh's arm, her jaw tight, looking straight at Daniel", "images/cg/ep1/d5_07_sara_daniel.webp")
    sp "Again. In front of everybody. And in front of me."

    menu:
        sp "Say something?"
        "Ignore him.":
            n "Sara turns her back to the door and fixes [nome_compagno]'s collar, which didn't need fixing."
            s "Seven o'clock, then. I'll wait for you for dinner."
            da "Silence. Very elegant. You're wasted on the culture pages, Sara."
            sp "How arrogant can one man be on a Friday?"
        "«At least he doesn't forget people.»" (confidence=24):
            $ interest("daniel", 2, "Daniel enjoys being answered back.")
            $ confidence(1, "Sara stood up for him.")
            $ segna("ep1_d5_risposta_daniel")
            s "At least he doesn't forget people. Only licences."
            n "For a second nobody breathes. Then Daniel laughs: a real laugh, surprised, almost delighted."
            if fatto("ep1_d3_risposta_daniel"):
                da "Twice in one week. Careful, Sara. I could get used to it."
            else:
                da "Touché. I'll remember that."
            da "I remember everything, you know. Especially the people who answer back."
            $ cg("Close-up of Josh, half proud and half terrified, glancing from Sara to his boss", "images/cg/ep1/d5_08_josh_imbarazzo.webp")
            c "Sara..."
            sp "He's proud of me. And scared to death. Both at once."

    n "Daniel raises his cup to them both, like a toast, and walks away down the corridor without hurrying."
    c "Sorry. He's like that with everyone."
    s "Not with everyone. With you."
    $ nota_sara("daniel", "Arrogant in daylight too. He never misses a chance.")

    call inizio_retroscena
    $ cg("Behind the scenes: Daniel in his glass corner office, standing at the window with his coffee, watching Sara leave the building on the street below", "images/cg/ep1/d5_09_daniel_finestra.webp")
    rs "Ten minutes earlier, from his corner office, Daniel saw Sara cross the street with something small in her hand."
    rs "He picked up his coffee, crossed the whole floor and leaned in that doorway. He had nothing to do there."
    rs "Now he watches her from the window until she turns the corner."
    $ retroscena("daniel", "Daniel humiliates [nome_compagno] above all when Sara is there to see it.")
    call fine_retroscena
    return


## --- Sera: film con Josh o fuori con Joanie ------------------------------------------

label ep1_d5_sera:
    $ vai("casa", "Home — 7:40 p.m.")
    $ ambiente(None)
    $ musica("casa")
    $ cg("Josh slumped on the sofa still in his work shirt, tie loosened, eyes closed, a remote in his hand; Sara in the doorway with her phone", "images/cg/ep1/d5_10_josh_stanco.webp")
    n "[nome_compagno] comes home at a quarter past seven and drops onto the sofa as if someone had cut his strings."
    c "Third version of the spreadsheet. Then the car. Then the fourth version of the spreadsheet."
    c "I want a film. A stupid one. With explosions. And you, under a blanket."
    $ suono("notifica")
    n "Sara's phone lights up. Joanie."
    ch "FRIDAY!!! Wine? I need wine and gossip. Mostly gossip. Yours."
    sp "A stupid film with him. Or wine with her."

    menu:
        sp "Friday night."
        "A film on the sofa with [nome_compagno].":
            $ interest("josh", 2, "A Friday night together.")
            $ segna("ep1_d5_film_josh")
            call ep1_d5_film
        "Go out with Joanie.":
            $ interest("amica", 1)
            $ segna("ep1_d5_joanie")
            call ep1_d5_joanie
    return

label ep1_d5_film:
    s "Sorry, Jo. He's had a terrible day. Next week, promise."
    ch "Booooring. Kiss him from me. Then tell me everything anyway."
    $ cg("The sofa at night: Sara and Josh under one blanket, a bowl of popcorn between them, both laughing at the TV (screen not visible)", "images/cg/ep1/d5_11_film_divano.webp")
    n "The film is terrible. Something explodes every four minutes; the hero never loses his sunglasses."
    n "[nome_compagno] laughs at all the wrong moments, and Sara laughs at him laughing."
    c "Thank you for today. The licence. And for... you know. Daniel."
    s "He doesn't get to talk to you like that."
    c "He's my boss. He gets to talk to me however he likes."
    sp "No. He doesn't."
    n "Halfway through the second explosion, [nome_compagno]'s head finds her shoulder. Sara doesn't move until the credits."
    return

label ep1_d5_joanie:
    s "Go, I'll be quick. Promise. One glass."
    c "Have fun. Say hi to Joanie. I'll be here. Horizontal."
    $ vai("enoteca", "A wine bar — 9:00 p.m.")
    $ ambiente("enoteca")
    $ musica("enoteca")
    $ cg("A small, crowded wine bar: Sara and Joanie at a tiny table by the wall, two glasses of red, Joanie leaning forward, chin on her hands, eager for gossip", "images/cg/ep1/d5_12_enoteca_joanie.webp")
    ch "So. The famous company dinner. Talk."
    s "There's nothing to talk about. It was a dinner. Risotto. Speeches."
    ch "Sara. I've known you forever. Your left eyebrow is lying to me right now."
    s "Fine. His boss was... a lot."
    ch "The boss. Daniel, right? The one [nome_compagno] complains about. What's he like?"

    if fatto("ep1_d3_audace"):
        s "I wore the red dress, by the way. The one you made me buy and I never wear."
        ch "You wore THE red dress? To a work dinner? Who are you and what have you done with my friend?"
        ch "And did he notice? The boss?"
        sp "Of course she asks that first."
        s "...He might have noticed."
        ch "Good."
    elif fatto("ep1_d3_nero"):
        ch "And what did you wear? The black one? The one [nome_compagno] likes?"
        s "The black one."
        ch "Safe. Pretty. Safe."
    else:
        ch "And what did you wear? Tell me you didn't go in the navy thing."
        s "I went in something nice."
        ch "That means the navy thing."

    s "He spent the whole evening needling [nome_compagno]. Little jokes. In front of everyone."
    if fatto("ep1_d3_risposta_daniel") or fatto("ep1_d5_risposta_daniel"):
        s "So I answered him back."
        $ cg("Close-up of Joanie laughing with delight, one hand on Sara's wrist across the little table", "images/cg/ep1/d5_13_joanie_ride.webp")
        ch "You did NOT."
        if fatto("ep1_d3_risposta_daniel") and fatto("ep1_d5_risposta_daniel"):
            s "Twice, actually. Once at the dinner, once today at his office."
        elif fatto("ep1_d5_risposta_daniel"):
            s "Today, at his office. In front of the whole floor."
        else:
            s "At the dinner. In front of the whole table."
        ch "Oh, I love this. And what did he do?"
        s "He laughed. As if I'd given him a present."
        ch "Of course he did. Men like that are bored to death, Sara. Everybody says yes to them. Then one day someone says no..."
        n "Joanie doesn't finish the sentence. She just smiles into her glass."
    else:
        s "And [nome_compagno] just... took it. Smiled. Like he always does."
        ch "And you?"
        s "I squeezed his hand under the table."
        ch "Sweet."
        n "Joanie says it the way you'd say «cute» about someone else's dog."

    if fatto("ep1_d3_romanzo_daniel"):
        s "He asked about the novel. He actually listened. Chin on his hand, like it mattered."
        ch "Huh. When was the last time [nome_compagno] asked you what happens in chapter three?"
        s "He's proud of the novel. He tells everybody."
        ch "Telling everybody isn't the same as asking you."
        sp "That's not fair. Is it?"

    ch "Look, I'm not saying anything. I'm just saying."
    ch "[nome_compagno] is a sweetheart. The sweetest. But you light up when you're annoyed, you know that? You've been glowing for twenty minutes."
    s "I'm not glowing. It's the wine."
    ch "It's half a glass, Sara."
    $ cg("Close-up of Sara at the wine bar table, cheeks pink, laughing and shaking her head, her glass still half full", "images/cg/ep1/d5_14_sara_enoteca.webp")
    sp "She does this. She takes something small and turns it under the light until it shines."
    sp "Daniel is an arrogant man who humiliates [nome_compagno]. That's all."
    sp "...That's all."
    ch "Next time he says something, I want a full report. Word for word."

    ## Corr +1 aggiunta il 21/11 (Jody): rende raggiungibile la soglia del giorno 8.
    menu:
        sp "A full report. On Daniel."
        "«There won't be a next time.»":
            s "There won't be a next time."
            ch "Mm-hm."
        "«...He's not ugly. I'll give you that much.»":
            $ corruption(1, "Sara admits, out loud, that Daniel is attractive.")
            $ segna("ep1_d5_daniel_bello")
            s "...Fine. He's not ugly. I'll give you that much."
            ch "THERE she is."
            n "Joanie slaps the table hard enough to make the glasses jump. Two people at the bar turn round."
            s "It's an observation. A journalist observes."
            ch "Observe all you like, babe. Looking is free."
            sp "I said it out loud. Half a glass of wine and I said it out loud."

    $ vai("casa", "Home — 11:20 p.m.")
    $ ambiente(None)
    $ musica("notte")
    n "When Sara gets home, the television is talking to nobody. [nome_compagno] is asleep on the sofa, a cushion over his face, still in his work shirt."
    n "She covers him with the blanket and turns off the TV."
    sp "Men like that are bored to death. Then one day someone says no."
    sp "Why do I keep thinking about it?"
    return
