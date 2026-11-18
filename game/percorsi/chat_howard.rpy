## =============================================================================
## HOWARD — discorsi al telefono: introduzione, A (conoscenti), B (confidenza)
## =============================================================================
## Tono (Q&A 18/11/2026): il disagio si vede SEMPRE dal modo di scrivere
## (troppi messaggi, troppo presto, sa cose che non dovrebbe sapere, battute fuori
## luogo). In circa una chat su tre (intro, A5, A8, B3, B4) un breve retroscena
## testuale dal suo lato. Sara non nota niente: per lei è un vicino solo e gentile.

init python:
    discorso("howard_intro", "howard", ESTRANEI)
    discorso("howard_a1", "howard", CONOSCENTI)
    discorso("howard_a2", "howard", CONOSCENTI)
    discorso("howard_a3", "howard", CONOSCENTI)
    discorso("howard_a4", "howard", CONOSCENTI)
    discorso("howard_a5", "howard", CONOSCENTI)
    discorso("howard_a6", "howard", CONOSCENTI)
    discorso("howard_a7", "howard", CONOSCENTI)
    discorso("howard_a8", "howard", CONOSCENTI)
    discorso("howard_b1", "howard", CONFIDENZA)
    discorso("howard_b2", "howard", CONFIDENZA)
    discorso("howard_b3", "howard", CONFIDENZA)
    discorso("howard_b4", "howard", CONFIDENZA)
    discorso("howard_b5", "howard", CONFIDENZA)

## Retroscena breve alla fine di una chat (la chat si chiude prima).
label howard_retroscena_chat(testo_rs, testo_diario):
    hide screen telefono_chat
    call inizio_retroscena
    rs "[testo_rs]"
    $ retroscena("howard", testo_diario)
    call fine_retroscena
    return


## --- Introduzione: grazie per le chiavi --------------------------------------

label chat_howard_intro:
    $ msg("sara", "Hi Howard, it's Sara. Thank you again for finding my keys. You saved my life.")
    return

label chat_howard_intro_1:
    $ msg("howard", "Sara!")
    $ msg("howard", "Oh you don't have to thank me. I was so happy to find them.")
    $ msg("howard", "Under the stairs, can you believe it. Right under our feet all that time.")
    $ msg("howard", "I'm glad you have my number now. For anything. Anything at all. I'm always home.")
    menu (screen="scelta_telefono"):
        "«That's very kind of you.»":
            $ msg("sara", "That's very kind of you.")
            $ msg("howard", "It's nothing. It's what neighbours are for.")
        "«You're a lifesaver, really.»":
            $ msg("sara", "You're a lifesaver, really.")
            $ caldo()
            $ msg("howard", "A lifesaver. Nobody ever called me that.")
            $ msg("howard", "I'm going to remember that.")
    return

label chat_howard_intro_2:
    $ msg("howard", "Did [nome_compagno] get home ok last night? I heard your door very late.")
    sp "He heard our door?"
    menu (screen="scelta_telefono"):
        "«Yes, a long shift. Sorry about the noise.»":
            $ msg("sara", "Yes, a long shift. Sorry about the noise.")
            $ msg("howard", "No noise at all! I just sleep very light. Goodnight Sara.")
        "«You hear everything through those walls, huh :)»":
            $ msg("sara", "You hear everything through those walls, huh :)")
            $ caldo()
            $ msg("howard", "Oh no no. Only the door. Only sometimes.")
            $ msg("howard", "Goodnight Sara.")
    call howard_retroscena_chat("Howard puts the phone down and opens the drawer by the door. Next to his own keys, a new one, still shiny. The copy works perfectly.", "After the chat Howard checked the copy of Sara's key. It works.")
    return


## --- A1: la vita condominiale ------------------------------------------------

label chat_howard_a1:
    $ msg("sara", "Howard, do you know who's dragging furniture upstairs at midnight?")
    return

label chat_howard_a1_1:
    $ msg("howard", "The Kowalskis. Third floor. They rearrange the living room every Tuesday.")
    $ msg("howard", "And the boy on the fourth floor plays drums on Sundays from 4 to 6.")
    $ msg("howard", "And Mrs. Dean takes the bins out at 6:10 every morning. Like a clock.")
    sp "He knows everyone's schedule. That's... very thorough."
    menu (screen="scelta_telefono"):
        "«You know everything about this building.»":
            $ msg("sara", "You know everything about this building.")
            $ caldo()
            $ msg("howard", "I've been here a long time. You notice things.")
        "«Thanks. I'll survive until Wednesday then.»":
            $ msg("sara", "Thanks. I'll survive until Wednesday then.")
            $ msg("howard", "Ha! Yes. Wednesday is quiet.")
    return

label chat_howard_a1_2:
    $ msg("howard", "You leave at 8:20, right? The Kowalskis' cat sits on the landing at that time. Watch your step.")
    sp "8:20. Exactly 8:20."
    menu (screen="scelta_telefono"):
        "«How do you know when I leave?»":
            $ msg("sara", "How do you know when I leave?")
            $ msg("howard", "Oh, I hear your heels on the stairs. Every morning. Very regular.")
            $ msg("howard", "It's a nice sound. It means the day is starting.")
        "«Thanks for the warning :)»":
            $ msg("sara", "Thanks for the warning :)")
            $ caldo()
            $ msg("howard", "Anytime. I'll keep an eye out.")
    return


## --- A2: problemi domestici --------------------------------------------------

label chat_howard_a2:
    $ msg("sara", "Random question: do you know a good plumber? The kitchen tap is dripping all night.")
    return

label chat_howard_a2_1:
    $ msg("howard", "A plumber? No no no. Don't waste money.")
    $ msg("howard", "It's the washer. Ten minutes. I can fix it.")
    $ msg("howard", "I have all the tools. I could come tomorrow afternoon.")
    menu (screen="scelta_telefono"):
        "«Are you sure? I don't want to bother you.»":
            $ msg("sara", "Are you sure? I don't want to bother you.")
            $ msg("howard", "Bother! You could never bother me.")
        "«That would be amazing, thank you.»":
            $ msg("sara", "That would be amazing, thank you.")
            $ caldo()
            $ msg("howard", "Wonderful. It will be a pleasure.")
    return

label chat_howard_a2_2:
    $ msg("howard", "What time is [nome_compagno] at work tomorrow? So I know when to come.")
    $ msg("howard", "I mean, so I don't disturb you both. Two people at home and a man under the sink, it's crowded.")
    sp "That's thoughtful of him. I think."
    menu (screen="scelta_telefono"):
        "«He's out until seven. Come at four?»":
            $ msg("sara", "He's out until seven. Come at four?")
            $ msg("howard", "Four. Perfect. I'll be there at four.")
            $ segna("howard_rubinetto")
        "«Come when we're both home, it's fine.»":
            $ msg("sara", "Come when we're both home, it's fine.")
            $ msg("howard", "Oh. Of course. Of course. Saturday then.")
    return


## --- A3: cucina casalinga ----------------------------------------------------

label chat_howard_a3:
    $ msg("sara", "Howard, the whole stairwell smells amazing. Is that you?")
    return

label chat_howard_a3_entrata:
    $ msg("howard", "I made too much lasagna. I always make too much. Old habit.")
    $ msg("sara", "So that's what smells so good in the stairwell!")
    return

label chat_howard_a3_1:
    $ msg("howard", "Lasagna. My mother's recipe. It takes four hours.")
    $ msg("howard", "But I always make it for six people and there's only me.")
    menu (screen="scelta_telefono"):
        "«Four hours! You're patient.»":
            $ msg("sara", "Four hours! You're patient.")
            $ msg("howard", "I have time. That's the one thing I have.")
        "«Your mother would be proud.»":
            $ msg("sara", "Your mother would be proud.")
            $ caldo()
            $ msg("howard", "She would. She always said I'd make some woman very happy.")
            $ msg("howard", "She was wrong about that.")
    return

label chat_howard_a3_2:
    $ msg("howard", "Can I bring you a plate? For you and [nome_compagno]. Mostly for you. You're too thin.")
    sp "Too thin. Nobody has ever told me that."
    menu (screen="scelta_telefono"):
        "«Yes please, that's so sweet.»":
            $ msg("sara", "Yes please, that's so sweet.")
            $ caldo()
            $ msg("howard", "I'll leave it at your door in ten minutes. Still warm.")
            $ segna("howard_lasagna")
        "«Thank you, but we already ate.»":
            $ msg("sara", "Thank you, but we already ate.")
            $ msg("howard", "Tomorrow then. Lasagna is better the day after.")
    return


## --- A4: film in televisione -------------------------------------------------

label chat_howard_a4:
    $ msg("sara", "Do you know any good old films? I want something that isn't a superhero.")
    return

label chat_howard_a4_1:
    $ msg("howard", "Oh! Yes. Yes. Old films are my passion.")
    $ msg("howard", "«Last Train Home». Black and white. A woman, married, meets a man at a train station.")
    $ msg("howard", "Nothing happens and everything happens. You'll cry.")
    menu (screen="scelta_telefono"):
        "«A married woman and a stranger? Sounds dangerous.»":
            $ msg("sara", "A married woman and a stranger? Sounds dangerous.")
            $ caldo()
            $ msg("howard", "The most beautiful things are a little dangerous.")
        "«I'll try it this weekend.»":
            $ msg("sara", "I'll try it this weekend.")
            $ msg("howard", "Tell me what you think. I want to know everything you think.")
    return

label chat_howard_a4_2:
    $ msg("howard", "Last night you were watching the one with the boat, right? I could hear the music.")
    $ msg("howard", "The walls are thin. I don't mind. I like hearing you two laugh.")
    sp "I didn't think the TV was that loud."
    menu (screen="scelta_telefono"):
        "«Sorry! I'll turn it down.»":
            $ msg("sara", "Sorry! I'll turn it down.")
            $ msg("howard", "No! Don't. Please. It keeps me company.")
        "«You should come watch one with us sometime.»":
            $ msg("sara", "You should come watch one with us sometime.")
            $ caldo()
            $ msg("howard", "Really? You'd let me?")
            $ msg("howard", "I'll bring snacks. Anything you want.")
    return


## --- A5: animali domestici (retroscena) --------------------------------------

label chat_howard_a5:
    $ msg("sara", "Howard, was there a cat in your flat once? I keep finding grey hairs on the landing.")
    return

label chat_howard_a5_1:
    $ msg("howard", "Duchess. Grey Persian. She died two years ago.")
    $ msg("howard", "Fourteen years together. Longer than any of my relationships. Ha.")
    menu (screen="scelta_telefono"):
        "«I'm so sorry.»":
            $ msg("sara", "I'm so sorry.")
            $ caldo()
            $ msg("howard", "Thank you. You're the first person who said that.")
        "«Fourteen years is a good long life.»":
            $ msg("sara", "Fourteen years is a good long life.")
            $ msg("howard", "It is. She was spoiled. She slept on my pillow.")
    return

label chat_howard_a5_2:
    $ msg("howard", "You remind me of her a little.")
    $ msg("howard", "Elegant. A bit shy. She only came to me when she wanted something.")
    $ msg("howard", "But when she came, she stayed.")
    sp "That's... a strange compliment. He means it kindly."
    menu (screen="scelta_telefono"):
        "«I'll take that as a compliment :)»":
            $ msg("sara", "I'll take that as a compliment :)")
            $ msg("howard", "It is. The biggest one I have.")
        "«Maybe you should get another cat.»":
            $ msg("sara", "Maybe you should get another cat.")
            $ msg("howard", "Maybe. Or maybe I just need better company.")
    call howard_retroscena_chat("In Howard's living room, on the armrest next to him, folded with care, there is a piece of lace that does not belong to him. He strokes it while he types.", "Howard keeps Sara's stolen underwear close while he writes to her.")
    return


## --- A6: piccoli favori ------------------------------------------------------

label chat_howard_a6:
    $ msg("sara", "Howard, did a courier leave a parcel with you? The tracking says «delivered to neighbour».")
    return

label chat_howard_a6_entrata:
    $ msg("howard", "Sara, the courier left a parcel for you. I have it safe. Very safe.")
    $ msg("sara", "Oh thank you! I was looking for it.")
    return

label chat_howard_a6_1:
    $ msg("howard", "Yes! It's here. I put it on the kitchen table so nobody steps on it.")
    $ msg("howard", "It's light. Soft. Clothes?")
    sp "Did he shake it?"
    menu (screen="scelta_telefono"):
        "«Just a top. Nothing exciting.»":
            $ msg("sara", "Just a top. Nothing exciting.")
            $ msg("howard", "I'm sure it will look lovely on you.")
        "«Curious, aren't you? :)»":
            $ msg("sara", "Curious, aren't you? :)")
            $ caldo()
            $ msg("howard", "Guilty. I don't get many parcels. I live through other people's.")
    return

label chat_howard_a6_2:
    $ msg("howard", "Come get it whenever. I'll make tea. I have the good biscuits.")
    menu (screen="scelta_telefono"):
        "«I'll come after work. Five minutes.»":
            $ msg("sara", "I'll come after work. Five minutes.")
            $ caldo()
            $ msg("howard", "Five minutes. Wonderful. The kettle will be ready.")
            $ segna("howard_pacco_tea")
        "«Could you leave it at my door? I'm in a rush.»":
            $ msg("sara", "Could you leave it at my door? I'm in a rush.")
            $ msg("howard", "Of course. Of course. At your door.")
    return


## --- A7: abitudini quotidiane ------------------------------------------------

label chat_howard_a7:
    $ msg("sara", "How do you fill your days, Howard? I never asked.")
    return

label chat_howard_a7_1:
    $ msg("howard", "Oh, a very boring routine. You'll laugh.")
    $ msg("howard", "Up at 6. Coffee. Radio. Crossword. Walk to the market.")
    $ msg("howard", "At 7:40 the pipes start singing, that means you're in the shower and the building is awake.")
    sp "He knows when I shower?"
    menu (screen="scelta_telefono"):
        "«The pipes? Really?»":
            $ msg("sara", "The pipes? Really?")
            $ msg("howard", "Old building. Everything echoes. I'm used to all your noises.")
            $ msg("howard", "All the building's noises, I mean.")
        "«Sounds peaceful, actually.»":
            $ msg("sara", "Sounds peaceful, actually.")
            $ caldo()
            $ msg("howard", "Peaceful. Yes. Quiet. Too quiet, sometimes.")
    return

label chat_howard_a7_2:
    $ msg("howard", "In the evening I cook, I watch a film, I wait for the day to end.")
    $ msg("howard", "The best part of the day is when I see you on the stairs. Honestly.")
    menu (screen="scelta_telefono"):
        "«That's sweet. And a bit sad.»":
            $ msg("sara", "That's sweet. And a bit sad.")
            $ caldo()
            $ msg("howard", "A bit sad. Yes. You see me. Not many people do.")
        "«You should join a club or something.»":
            $ msg("sara", "You should join a club or something.")
            $ msg("howard", "Maybe. Clubs are full of strangers. You're not a stranger.")
    return


## --- A8: la solitudine del weekend (retroscena) ------------------------------

label chat_howard_a8:
    $ msg("sara", "Busy weekend, Howard?")
    return

label chat_howard_a8_entrata:
    $ msg("howard", "Are you two home this weekend? Just asking. No reason.")
    $ msg("sara", "Probably. Why?")
    return

label chat_howard_a8_1:
    $ msg("howard", "Me? Oh, the usual. Nobody calls on Saturdays.")
    $ msg("howard", "Sunday is the worst. The whole building goes out and I stay. Like a guard.")
    menu (screen="scelta_telefono"):
        "«That sounds lonely.»":
            $ msg("sara", "That sounds lonely.")
            $ msg("howard", "It is. But I'm used to it.")
        "«Come over for coffee on Sunday.»":
            $ msg("sara", "Come over for coffee on Sunday.")
            $ caldo()
            $ msg("howard", "Really? Really really?")
            $ msg("howard", "What time? I'll be there. I'll bring the biscuits. The good ones.")
            $ segna("howard_caffe_domenica")
    return

label chat_howard_a8_2:
    $ msg("howard", "You're the kindest person in this building, Sara. Maybe in this city.")
    sp "Poor Howard. He has nobody."
    menu (screen="scelta_telefono"):
        "«Don't exaggerate :)»":
            $ msg("sara", "Don't exaggerate :)")
            $ msg("howard", "I never exaggerate about you.")
        "«You deserve a bit of company.»":
            $ msg("sara", "You deserve a bit of company.")
            $ caldo()
            $ msg("howard", "I'm starting to believe it.")
    call howard_retroscena_chat("On the kitchen calendar Howard circles Sunday in red. He writes «S.» inside the circle, then a second time, more slowly.", "Howard marks every possible meeting with Sara on his calendar.")
    return


## --- B1: il desiderio di una famiglia ----------------------------------------

label chat_howard_b1:
    $ msg("sara", "Howard, can I ask you something personal? Did you ever want children?")
    return

label chat_howard_b1_entrata:
    $ msg("howard", "I saw a family on the bus today. Mum, dad, two little ones. I stared like a fool.")
    $ msg("sara", "Did you ever want one? A family?")
    return

label chat_howard_b1_1:
    $ msg("howard", "More than anything.")
    $ msg("howard", "A wife who waits for me. Someone to cook for. Someone who needs me.")
    $ msg("howard", "It never happened. Women never saw me. I was always the friend, the neighbour.")
    menu (screen="scelta_telefono"):
        "«It's not too late, Howard.»":
            $ msg("sara", "It's not too late, Howard.")
            $ caldo()
            $ msg("howard", "You really think so?")
        "«I'm sorry. That must hurt.»":
            $ msg("sara", "I'm sorry. That must hurt.")
            $ msg("howard", "Every day. But talking to you helps.")
    return

label chat_howard_b1_2:
    $ msg("howard", "You and [nome_compagno] will have beautiful children.")
    $ msg("howard", "He's a lucky man. I hope he knows it. I hope he never leaves you alone too much.")
    sp "Why does that sound like a warning?"
    menu (screen="scelta_telefono"):
        "«He knows. Don't worry.»":
            $ msg("sara", "He knows. Don't worry.")
            $ interest("josh", 1)
            $ msg("howard", "Good. Good.")
        "«He works a lot, lately.»":
            $ msg("sara", "He works a lot, lately.")
            $ msg("howard", "I know. I hear him leave early and come back late.")
            $ msg("howard", "If you ever feel alone in there, I'm here. Just a wall away.")
    return


## --- B2: le occasioni perdute ------------------------------------------------

label chat_howard_b2:
    $ msg("sara", "Was there ever someone special, Howard?")
    return

label chat_howard_b2_1:
    $ msg("howard", "Once. Margaret. Thirty years ago. She worked at the post office.")
    $ msg("howard", "I bought stamps every day for a year. I had three thousand stamps.")
    $ msg("howard", "I never asked her out. She married a mechanic.")
    menu (screen="scelta_telefono"):
        "«Three thousand stamps! Howard!»":
            $ msg("sara", "Three thousand stamps! Howard!")
            $ caldo()
            $ msg("howard", "I still have them. I can't throw them away.")
        "«Why didn't you ask?»":
            $ msg("sara", "Why didn't you ask?")
            $ msg("howard", "Because I knew the answer. I always know the answer.")
    return

label chat_howard_b2_2:
    $ msg("howard", "I promised myself: next time I won't wait. I'll do something.")
    $ msg("howard", "Even if it's small. Even if nobody notices.")
    sp "I hope he finds someone. He really deserves it."
    menu (screen="scelta_telefono"):
        "«Good. Don't wait anymore.»":
            $ msg("sara", "Good. Don't wait anymore.")
            $ caldo()
            $ msg("howard", "I won't. Thank you, Sara. You give me courage.")
        "«Small things count.»":
            $ msg("sara", "Small things count.")
            $ msg("howard", "They do. They count a lot.")
    return


## --- B3: la paura di invecchiare solo (retroscena) ---------------------------

label chat_howard_b3:
    $ msg("sara", "You were very quiet on the stairs today. Are you ok?")
    return

label chat_howard_b3_entrata:
    $ msg("howard", "Sorry to write so late. I can't sleep.")
    $ msg("sara", "It's ok. What's wrong?")
    return

label chat_howard_b3_1:
    $ msg("howard", "I went to the doctor. Nothing serious. Blood pressure.")
    $ msg("howard", "But in the waiting room they asked «who should we call in case of emergency».")
    $ msg("howard", "And I had nobody to write. Nobody, Sara.")
    menu (screen="scelta_telefono"):
        "«Write my name.»":
            $ msg("sara", "Write my name.")
            $ caldo()
            $ msg("howard", "...")
            $ msg("howard", "Do you mean it?")
            $ msg("sara", "Of course. We're neighbours.")
            $ segna("howard_contatto_emergenza")
        "«Oh Howard. I'm so sorry.»":
            $ msg("sara", "Oh Howard. I'm so sorry.")
            $ msg("howard", "Don't be. It's my life. I chose it. Or it chose me.")
    return

label chat_howard_b3_2:
    $ msg("howard", "I'm afraid of dying in this flat and nobody noticing for weeks.")
    $ msg("howard", "Sorry. Sorry. I'm crying like an idiot. Forget it.")
    sp "He's crying. Alone, next door."
    menu (screen="scelta_telefono"):
        "«I would notice. I promise.»":
            $ msg("sara", "I would notice. I promise.")
            $ caldo()
            $ msg("howard", "Thank you. Goodnight, Sara. You're an angel.")
        "«Try to sleep. We'll talk tomorrow.»":
            $ msg("sara", "Try to sleep. We'll talk tomorrow.")
            $ msg("howard", "Tomorrow. Yes. Goodnight.")
    call howard_retroscena_chat("Howard's eyes are perfectly dry. He reads her last message twice, smiles, and switches off the lamp. «An angel.»", "Howard's tears in the chat were fake: he was smiling.")
    return


## --- B4: sentirsi finalmente ascoltato (retroscena) --------------------------

label chat_howard_b4:
    $ msg("sara", "How are you today, Howard? Better?")
    return

label chat_howard_b4_1:
    $ msg("howard", "Better. Because you asked.")
    $ msg("howard", "Do you know you're the only person who asks me how I am?")
    $ msg("howard", "Forty years in this city and you're the only one.")
    menu (screen="scelta_telefono"):
        "«That can't be true.»":
            $ msg("sara", "That can't be true.")
            $ msg("howard", "It is. I counted.")
        "«Then I'll keep asking.»":
            $ msg("sara", "Then I'll keep asking.")
            $ caldo()
            $ msg("howard", "Every day?")
            $ msg("sara", "Every day you want.")
    return

label chat_howard_b4_2:
    $ msg("howard", "I read our messages again sometimes. When the evening is long.")
    $ msg("howard", "Is that strange? Tell me if it's strange.")
    sp "It is a little strange. But he's lonely."
    menu (screen="scelta_telefono"):
        "«It's not strange. It's sweet.»":
            $ msg("sara", "It's not strange. It's sweet.")
            $ caldo()
            $ msg("howard", "Sweet. I'll remember that word too.")
        "«A little strange :) But ok.»":
            $ msg("sara", "A little strange :) But ok.")
            $ msg("howard", "Ha. I'll try to be less strange. For you.")
    call howard_retroscena_chat("On Howard's computer a folder called «S» grows every night: every message, every photo she has ever posted, sorted by date.", "Howard archives everything Sara writes and posts, in a folder called «S».")
    return


## --- B5: Sara come presenza rassicurante -------------------------------------

label chat_howard_b5:
    $ msg("sara", "I'm working late tonight. Could you tell me if the courier comes? Sorry to ask.")
    return

label chat_howard_b5_1:
    $ msg("howard", "Of course! I'll stand by the door. Don't worry about anything.")
    $ msg("howard", "It's nice to be useful to someone. To you.")
    menu (screen="scelta_telefono"):
        "«What would I do without you?»":
            $ msg("sara", "What would I do without you?")
            $ caldo()
            $ msg("howard", "You'd manage. But I'm glad you don't have to.")
        "«Thank you, Howard.»":
            $ msg("sara", "Thank you, Howard.")
            $ msg("howard", "Always.")
    return

label chat_howard_b5_2:
    $ msg("howard", "Can I tell you something? When I know you're home, I sleep better.")
    $ msg("howard", "It's like having a light on in the corridor.")
    sp "Like a light in the corridor. He needs someone so badly."
    menu (screen="scelta_telefono"):
        "«I'm glad I help. Really.»":
            $ msg("sara", "I'm glad I help. Really.")
            $ caldo()
            $ msg("howard", "You help more than you know.")
            $ segna("howard_luce_corridoio")
        "«You should meet more people, Howard. Not just me.»":
            $ msg("sara", "You should meet more people, Howard. Not just me.")
            $ msg("howard", "...")
            $ msg("howard", "You're right. Of course. Goodnight.")
            sp "Did I hurt him?"
    return
