## =============================================================================
## MAGNUS (chiave "editore") — discorsi al telefono: introduzione, A, B
## =============================================================================
## Tono (Q&A 18/11/2026): messaggi lunghi ed eleganti, niente emoticon, firma «M.».
## Esercizi di scrittura già da A: Sara sceglie fra versione pudica (niente),
## sensoriale (Confidence +1) e audace (requisito di Confidence, risposta calda).
## In B gli esercizi diventano più sensuali. Il seme: il suo vero talento è
## un'altra voce, quella che il finale del percorso rivela.
## Due introduzioni alternative: «le cinquanta pagine» (flag ep2_pagine_magnus,
## giorno 15) oppure «sto ancora aspettando quelle pagine». Se ne gioca una sola.

init python:
    discorso("editore_intro_pagine", "editore", ESTRANEI, se="fatto('ep2_pagine_magnus')")
    discorso("editore_intro_attesa", "editore", ESTRANEI, se="not fatto('ep2_pagine_magnus')", scrive_lui=True)
    discorso("editore_a1", "editore", CONOSCENTI)
    discorso("editore_a2", "editore", CONOSCENTI)
    discorso("editore_a3", "editore", CONOSCENTI)
    discorso("editore_a4", "editore", CONOSCENTI)
    discorso("editore_a5", "editore", CONOSCENTI)
    discorso("editore_a6", "editore", CONOSCENTI)
    discorso("editore_a7", "editore", CONOSCENTI)
    discorso("editore_a8", "editore", CONOSCENTI)
    discorso("editore_b1", "editore", CONFIDENZA)
    discorso("editore_b2", "editore", CONFIDENZA)
    discorso("editore_b3", "editore", CONFIDENZA)
    discorso("editore_b4", "editore", CONFIDENZA)
    discorso("editore_b5", "editore", CONFIDENZA)


## --- Introduzione A: le cinquanta pagine -------------------------------------

label chat_editore_intro_pagine:
    label tel_chat_editore_intro_pagine_1:
    if telefono_minuti_blocco("tel_chat_editore_intro_pagine_1", "invia", 1):
        return
    $ msg("sara", "Good evening, Mr. Magnus. It's Sara. I just wanted to make sure the pages arrived.")
    return

label chat_editore_intro_pagine_entrata:
    label tel_chat_editore_intro_pagine_entrata_1:
    if telefono_minuti_blocco("tel_chat_editore_intro_pagine_entrata_1", "ricevi", 1):
        return
    $ msg("editore", "Dear Sara, I read your fifty pages in one sitting, which has not happened to me in some years. M.")
    label tel_chat_editore_intro_pagine_entrata_2:
    if telefono_minuti_blocco("tel_chat_editore_intro_pagine_entrata_2", "invia", 1):
        return
    $ msg("sara", "Oh. Thank you. I didn't expect you to read them so soon.")
    return

label chat_editore_intro_pagine_1:
    label tel_chat_editore_intro_pagine_1_1:
    if telefono_minuti_blocco("tel_chat_editore_intro_pagine_1_1", "ricevi", 2):
        return
    $ msg("editore", "They arrived, and I read them twice. Please, just Magnus. «Mr.» makes me feel like my own father, and he was a dreadful man.")
    $ msg("editore", "Your sentences are careful. Too careful, in places. As if you were writing with someone reading over your shoulder. M.")
    sp "That's exactly how it feels when I write."
    label tel_chat_editore_intro_pagine_1_2:
    if telefono_minuti_blocco("tel_chat_editore_intro_pagine_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Is that bad?»":
            label tel_chat_editore_intro_pagine_1_3:
            if telefono_minuti_blocco("tel_chat_editore_intro_pagine_1_3", "invia", 1):
                return
            $ msg("sara", "Is that bad?")
            label tel_chat_editore_intro_pagine_1_4:
            if telefono_minuti_blocco("tel_chat_editore_intro_pagine_1_4", "ricevi", 1):
                return
            $ msg("editore", "It is a habit. Habits can be broken, if one wishes. M.")
        "«You noticed that from fifty pages?»":
            label tel_chat_editore_intro_pagine_1_5:
            if telefono_minuti_blocco("tel_chat_editore_intro_pagine_1_5", "invia", 1):
                return
            $ msg("sara", "You noticed that from fifty pages?")
            $ caldo()
            label tel_chat_editore_intro_pagine_1_6:
            if telefono_minuti_blocco("tel_chat_editore_intro_pagine_1_6", "ricevi", 1):
                return
            $ msg("editore", "From the first five. I have read forty years of manuscripts. Fear has a smell. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_intro_pagine_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_intro_pagine_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_intro_pagine_2:
    label tel_chat_editore_intro_pagine_2_1:
    if telefono_minuti_blocco("tel_chat_editore_intro_pagine_2_1", "ricevi", 2):
        return
    $ msg("editore", "Chapter three, the woman alone in the kitchen at night. That is where you stop being careful. Write more of her.")
    $ msg("editore", "Good night, Sara. M.")
    $ segna("magnus_capitolo_tre")
    label tel_chat_editore_intro_pagine_2_2:
    if telefono_minuti_blocco("tel_chat_editore_intro_pagine_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I will. Thank you, Magnus.»":
            label tel_chat_editore_intro_pagine_2_3:
            if telefono_minuti_blocco("tel_chat_editore_intro_pagine_2_3", "invia", 1):
                return
            $ msg("sara", "I will. Thank you, Magnus.")
            $ caldo()
        "«Good night.»":
            label tel_chat_editore_intro_pagine_2_4:
            if telefono_minuti_blocco("tel_chat_editore_intro_pagine_2_4", "invia", 1):
                return
            $ msg("sara", "Good night.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_intro_pagine_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_intro_pagine_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Introduzione B: sto ancora aspettando quelle pagine ---------------------

label chat_editore_intro_attesa:
    label tel_chat_editore_intro_attesa_1:
    if telefono_minuti_blocco("tel_chat_editore_intro_attesa_1", "invia", 1):
        return
    $ msg("sara", "Good evening, Mr. Magnus. It's Sara, from Daniel's party.")
    return

label chat_editore_intro_attesa_entrata:
    label tel_chat_editore_intro_attesa_entrata_1:
    if telefono_minuti_blocco("tel_chat_editore_intro_attesa_entrata_1", "ricevi", 1):
        return
    $ msg("editore", "Dear Sara, your pages have arrived. I look forward to reading them. M." if fatto("ep2_pagine_magnus") else "Dear Sara, I am still waiting for those pages. I am a patient man, but I am not a young one. M.")
    label tel_chat_editore_intro_attesa_entrata_2:
    if telefono_minuti_blocco("tel_chat_editore_intro_attesa_entrata_2", "invia", 1):
        return
    $ msg("sara", "Thank you for letting me know." if fatto("ep2_pagine_magnus") else "I'm sorry. I wasn't sure they were good enough.")
    return

label chat_editore_intro_attesa_1:
    label tel_chat_editore_intro_attesa_1_1:
    if telefono_minuti_blocco("tel_chat_editore_intro_attesa_1_1", "ricevi", 2):
        return
    $ msg("editore", "I remember you. You talked about your novel the way people talk about a lover they are ashamed of.")
    $ msg("editore", "I have your pages now. Whether they are good is my problem, not yours. M." if fatto("ep2_pagine_magnus") else "I am still waiting for those pages. Whether they are good is my problem, not yours. M.")
    label tel_chat_editore_intro_attesa_1_2:
    if telefono_minuti_blocco("tel_chat_editore_intro_attesa_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm afraid you'll hate them.»":
            label tel_chat_editore_intro_attesa_1_3:
            if telefono_minuti_blocco("tel_chat_editore_intro_attesa_1_3", "invia", 1):
                return
            $ msg("sara", "I'm afraid you'll hate them.")
            label tel_chat_editore_intro_attesa_1_4:
            if telefono_minuti_blocco("tel_chat_editore_intro_attesa_1_4", "ricevi", 1):
                return
            $ msg("editore", "Then I will tell you why, and you will write better ones. That is the whole profession. M.")
        "«I'll send them this week. I promise.»" if not fatto("ep2_pagine_magnus"):
            label tel_chat_editore_intro_attesa_1_5:
            if telefono_minuti_blocco("tel_chat_editore_intro_attesa_1_5", "invia", 1):
                return
            $ msg("sara", "I sent them on Monday, as promised." if fatto("ep2_pagine_magnus") else "I'll send them this week. I promise.")
            $ caldo()
            label tel_chat_editore_intro_attesa_1_6:
            if telefono_minuti_blocco("tel_chat_editore_intro_attesa_1_6", "ricevi", 1):
                return
            $ msg("editore", "I have them. Thank you for keeping your promise. M." if fatto("ep2_pagine_magnus") else "A promise to an old man is a serious thing. I will hold you to it. M.")
            $ segna("magnus_promessa_pagine")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_intro_attesa_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_intro_attesa_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_intro_attesa_2:
    label tel_chat_editore_intro_attesa_2_1:
    if telefono_minuti_blocco("tel_chat_editore_intro_attesa_2_1", "ricevi", 1):
        return
    $ msg("editore", "Writers who wait for permission never get it. Writers who don't, sometimes do. Good night. M.")
    sp "He's right. I've been waiting for permission my whole life."
    return


## --- A1: scrittori preferiti -------------------------------------------------

label chat_editore_a1:
    label tel_chat_editore_a1_1:
    if telefono_minuti_blocco("tel_chat_editore_a1_1", "invia", 1):
        return
    $ msg("sara", "Magnus, can I ask which writers you love? Not publish. Love.")
    return

label chat_editore_a1_1:
    label tel_chat_editore_a1_1_1:
    if telefono_minuti_blocco("tel_chat_editore_a1_1_1", "ricevi", 2):
        return
    $ msg("editore", "A dangerous question, because the answer changes with age. At twenty I loved the angry ones. At forty, the cruel ones.")
    $ msg("editore", "Now I love only those who are honest about desire. There are fewer than you would think. M.")
    label tel_chat_editore_a1_1_2:
    if telefono_minuti_blocco("tel_chat_editore_a1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Desire? Not love?»":
            label tel_chat_editore_a1_1_3:
            if telefono_minuti_blocco("tel_chat_editore_a1_1_3", "invia", 1):
                return
            $ msg("sara", "Desire? Not love?")
            $ caldo()
            label tel_chat_editore_a1_1_4:
            if telefono_minuti_blocco("tel_chat_editore_a1_1_4", "ricevi", 1):
                return
            $ msg("editore", "Love is what we write about when we are afraid to write about desire. M.")
        "«I mostly read the classics. The safe ones.»":
            label tel_chat_editore_a1_1_5:
            if telefono_minuti_blocco("tel_chat_editore_a1_1_5", "invia", 1):
                return
            $ msg("sara", "I mostly read the classics. The safe ones.")
            label tel_chat_editore_a1_1_6:
            if telefono_minuti_blocco("tel_chat_editore_a1_1_6", "ricevi", 1):
                return
            $ msg("editore", "No classic is safe. They were only made safe by teachers. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_a1_2:
    label tel_chat_editore_a1_2_1:
    if telefono_minuti_blocco("tel_chat_editore_a1_2_1", "ricevi", 1):
        return
    $ msg("editore", "And yours? Tell me the book you would be embarrassed to be seen reading on a train. M.")
    label tel_chat_editore_a1_2_2:
    if telefono_minuti_blocco("tel_chat_editore_a1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'd rather not say.»":
            label tel_chat_editore_a1_2_3:
            if telefono_minuti_blocco("tel_chat_editore_a1_2_3", "invia", 1):
                return
            $ msg("sara", "I'd rather not say.")
            label tel_chat_editore_a1_2_4:
            if telefono_minuti_blocco("tel_chat_editore_a1_2_4", "ricevi", 1):
                return
            $ msg("editore", "That is an answer, and a revealing one. M.")
        "«A romance with a very bad cover. I read it three times.»":
            label tel_chat_editore_a1_2_5:
            if telefono_minuti_blocco("tel_chat_editore_a1_2_5", "invia", 1):
                return
            $ msg("sara", "A romance with a very bad cover. I read it three times.")
            $ caldo()
            label tel_chat_editore_a1_2_6:
            if telefono_minuti_blocco("tel_chat_editore_a1_2_6", "ricevi", 1):
                return
            $ msg("editore", "Three times. Then it was not the cover you were reading. M.")
            sp "Why did I tell him that?"
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A2: libri controversi ---------------------------------------------------

label chat_editore_a2:
    label tel_chat_editore_a2_1:
    if telefono_minuti_blocco("tel_chat_editore_a2_1", "invia", 1):
        return
    $ msg("sara", "Is it true you published that novel everyone wanted banned? Joanie told me.")
    return

label chat_editore_a2_1:
    label tel_chat_editore_a2_1_1:
    if telefono_minuti_blocco("tel_chat_editore_a2_1_1", "ricevi", 2):
        return
    $ msg("editore", "I have published four of them. Each time the critics were outraged and each time the book sold out in a week.")
    $ msg("editore", "People condemn in public what they read in bed. M.")
    label tel_chat_editore_a2_1_2:
    if telefono_minuti_blocco("tel_chat_editore_a2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Did it ever make you feel guilty?»":
            label tel_chat_editore_a2_1_3:
            if telefono_minuti_blocco("tel_chat_editore_a2_1_3", "invia", 1):
                return
            $ msg("sara", "Did it ever make you feel guilty?")
            label tel_chat_editore_a2_1_4:
            if telefono_minuti_blocco("tel_chat_editore_a2_1_4", "ricevi", 1):
                return
            $ msg("editore", "Guilt is for people who don't believe in what they do. I always did. M.")
        "«I'd love to read one.»":
            label tel_chat_editore_a2_1_5:
            if telefono_minuti_blocco("tel_chat_editore_a2_1_5", "invia", 1):
                return
            $ msg("sara", "I'd love to read one.")
            $ caldo()
            label tel_chat_editore_a2_1_6:
            if telefono_minuti_blocco("tel_chat_editore_a2_1_6", "ricevi", 1):
                return
            $ msg("editore", "I will have a copy sent to you. Read it slowly. Not on the train. M.")
            $ segna("magnus_libro_regalo")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_a2_2:
    label tel_chat_editore_a2_2_1:
    if telefono_minuti_blocco("tel_chat_editore_a2_2_1", "ricevi", 1):
        return
    $ msg("editore", "A book is controversial only when it says aloud what everyone thinks in silence. Remember that when you write. M.")
    return


## --- A3: scrivere ogni giorno (esercizio) ------------------------------------

label chat_editore_a3:
    label tel_chat_editore_a3_1:
    if telefono_minuti_blocco("tel_chat_editore_a3_1", "invia", 1):
        return
    $ msg("sara", "Do you have any advice? I only manage to write on weekends.")
    return

label chat_editore_a3_1:
    label tel_chat_editore_a3_1_1:
    if telefono_minuti_blocco("tel_chat_editore_a3_1_1", "ricevi", 2):
        return
    $ msg("editore", "Write every day. Three lines, if that is all you have. A writer is a muscle, not a mood.")
    $ msg("editore", "Let us begin now. Describe, in three lines, the moment you knew you wanted to write. M.")
    label tel_chat_editore_a3_1_2:
    if telefono_minuti_blocco("tel_chat_editore_a3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "(Shy) «I was eleven. I wrote a poem for my mother. She corrected the spelling.»":
            label tel_chat_editore_a3_1_3:
            if telefono_minuti_blocco("tel_chat_editore_a3_1_3", "invia", 1):
                return
            $ msg("sara", "I was eleven. I wrote a poem for my mother. She corrected the spelling.")
            label tel_chat_editore_a3_1_4:
            if telefono_minuti_blocco("tel_chat_editore_a3_1_4", "ricevi", 1):
                return
            $ msg("editore", "Honest, and sad. Your mother corrected the spelling and missed the poem. M.")
        "(Sensory) «The smell of a new notebook. The pen scratching. The house asleep around me.»":
            label tel_chat_editore_a3_1_5:
            if telefono_minuti_blocco("tel_chat_editore_a3_1_5", "invia", 1):
                return
            $ msg("sara", "The smell of a new notebook. The pen scratching. The house asleep around me.")
            $ confidence(1)
            label tel_chat_editore_a3_1_6:
            if telefono_minuti_blocco("tel_chat_editore_a3_1_6", "ricevi", 1):
                return
            $ msg("editore", "Better. Now I am in the room with you. M.")
        "(Bold) «When I realised I could say things on paper I'd never dare say aloud.»" (confidence=30):
            label tel_chat_editore_a3_1_7:
            if telefono_minuti_blocco("tel_chat_editore_a3_1_7", "invia", 1):
                return
            $ msg("sara", "When I realised I could say things on paper I'd never dare say aloud.")
            $ caldo()
            label tel_chat_editore_a3_1_8:
            if telefono_minuti_blocco("tel_chat_editore_a3_1_8", "ricevi", 1):
                return
            $ msg("editore", "There she is. That is the writer I want to read. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_a3_2:
    label tel_chat_editore_a3_2_1:
    if telefono_minuti_blocco("tel_chat_editore_a3_2_1", "ricevi", 1):
        return
    $ msg("editore", "Three lines a day. Send them to me if you wish. I will not correct the spelling. M.")
    sp "Three lines a day. I can do that."
    return


## --- A4: cinema e letteratura ------------------------------------------------

label chat_editore_a4:
    label tel_chat_editore_a4_1:
    if telefono_minuti_blocco("tel_chat_editore_a4_1", "invia", 1):
        return
    $ msg("sara", "Do you prefer books or films? Daniel says you hate cinema.")
    return

label chat_editore_a4_1:
    label tel_chat_editore_a4_1_1:
    if telefono_minuti_blocco("tel_chat_editore_a4_1_1", "ricevi", 2):
        return
    $ msg("editore", "Daniel exaggerates everything except his own virtues, which he understates by a small margin.")
    $ msg("editore", "I love cinema. But a film shows you a woman. A book makes you become her. M.")
    label tel_chat_editore_a4_1_2:
    if telefono_minuti_blocco("tel_chat_editore_a4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's beautiful.»":
            label tel_chat_editore_a4_1_3:
            if telefono_minuti_blocco("tel_chat_editore_a4_1_3", "invia", 1):
                return
            $ msg("sara", "That's beautiful.")
            $ caldo()
            label tel_chat_editore_a4_1_4:
            if telefono_minuti_blocco("tel_chat_editore_a4_1_4", "ricevi", 1):
                return
            $ msg("editore", "It is merely true. Beauty is a side effect. M.")
        "«I still like films better on a Friday night.»":
            label tel_chat_editore_a4_1_5:
            if telefono_minuti_blocco("tel_chat_editore_a4_1_5", "invia", 1):
                return
            $ msg("sara", "I still like films better on a Friday night.")
            label tel_chat_editore_a4_1_6:
            if telefono_minuti_blocco("tel_chat_editore_a4_1_6", "ricevi", 1):
                return
            $ msg("editore", "Friday nights are for being lazy. I approve. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_a4_2:
    label tel_chat_editore_a4_2_1:
    if telefono_minuti_blocco("tel_chat_editore_a4_2_1", "ricevi", 1):
        return
    $ msg("editore", "Which woman would you like to become, if you could choose any book? M.")
    label tel_chat_editore_a4_2_2:
    if telefono_minuti_blocco("tel_chat_editore_a4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Someone brave.»":
            label tel_chat_editore_a4_2_3:
            if telefono_minuti_blocco("tel_chat_editore_a4_2_3", "invia", 1):
                return
            $ msg("sara", "Someone brave.")
            label tel_chat_editore_a4_2_4:
            if telefono_minuti_blocco("tel_chat_editore_a4_2_4", "ricevi", 1):
                return
            $ msg("editore", "Bravery is the most overrated quality in fiction and the most underrated in life. M.")
        "«Someone who doesn't apologise.»" (confidence=25):
            label tel_chat_editore_a4_2_5:
            if telefono_minuti_blocco("tel_chat_editore_a4_2_5", "invia", 1):
                return
            $ msg("sara", "Someone who doesn't apologise.")
            $ caldo()
            label tel_chat_editore_a4_2_6:
            if telefono_minuti_blocco("tel_chat_editore_a4_2_6", "ricevi", 1):
                return
            $ msg("editore", "Then stop apologising in your chapters. Start there. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A5: viaggi culturali ----------------------------------------------------

label chat_editore_a5:
    label tel_chat_editore_a5_1:
    if telefono_minuti_blocco("tel_chat_editore_a5_1", "invia", 1):
        return
    $ msg("sara", "Your assistant said you're travelling. Somewhere interesting?")
    return

label chat_editore_a5_1:
    label tel_chat_editore_a5_1_1:
    if telefono_minuti_blocco("tel_chat_editore_a5_1_1", "ricevi", 2):
        return
    $ msg("editore", "An old city by the sea, for a book fair. Dull meetings by day. By night, a library that has not changed in three centuries.")
    $ msg("editore", "I sat there until they closed the doors. The silence of old paper is the best company I know. M.")
    label tel_chat_editore_a5_1_2:
    if telefono_minuti_blocco("tel_chat_editore_a5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I envy you.»":
            label tel_chat_editore_a5_1_3:
            if telefono_minuti_blocco("tel_chat_editore_a5_1_3", "invia", 1):
                return
            $ msg("sara", "I envy you.")
            label tel_chat_editore_a5_1_4:
            if telefono_minuti_blocco("tel_chat_editore_a5_1_4", "ricevi", 1):
                return
            $ msg("editore", "Envy is a good start. It tells you what you want. M.")
        "«Take me with you next time. Joking.»" (confidence=25):
            label tel_chat_editore_a5_1_5:
            if telefono_minuti_blocco("tel_chat_editore_a5_1_5", "invia", 1):
                return
            $ msg("sara", "Take me with you next time. Joking.")
            $ caldo()
            label tel_chat_editore_a5_1_6:
            if telefono_minuti_blocco("tel_chat_editore_a5_1_6", "ricevi", 1):
                return
            $ msg("editore", "I never joke about libraries. M.")
            sp "He didn't say no."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_a5_2:
    label tel_chat_editore_a5_2_1:
    if telefono_minuti_blocco("tel_chat_editore_a5_2_1", "ricevi", 1):
        return
    $ msg("editore", "Travel is where we discover that our ordinary life was a choice, not a destiny. M.")
    return


## --- A6: collezionismo -------------------------------------------------------

label chat_editore_a6:
    label tel_chat_editore_a6_1:
    if telefono_minuti_blocco("tel_chat_editore_a6_1", "invia", 1):
        return
    $ msg("sara", "Daniel says your house is full of first editions. Is it a museum?")
    return

label chat_editore_a6_1:
    label tel_chat_editore_a6_1_1:
    if telefono_minuti_blocco("tel_chat_editore_a6_1_1", "ricevi", 2):
        return
    $ msg("editore", "Not a museum. A collection. A museum is for the public. A collection is private, and much more honest.")
    $ msg("editore", "I collect first editions, letters, photographs. Things that remember someone. M.")
    label tel_chat_editore_a6_1_2:
    if telefono_minuti_blocco("tel_chat_editore_a6_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Photographs of what?»":
            label tel_chat_editore_a6_1_3:
            if telefono_minuti_blocco("tel_chat_editore_a6_1_3", "invia", 1):
                return
            $ msg("sara", "Photographs of what?")
            label tel_chat_editore_a6_1_4:
            if telefono_minuti_blocco("tel_chat_editore_a6_1_4", "ricevi", 1):
                return
            $ msg("editore", "Of moments that deserved to stay. Perhaps one day I will show you. M.")
            $ segna("magnus_collezione_foto")
            sp "Why does that sentence give me a shiver?"
        "«I'd love to see the books.»":
            label tel_chat_editore_a6_1_5:
            if telefono_minuti_blocco("tel_chat_editore_a6_1_5", "invia", 1):
                return
            $ msg("sara", "I'd love to see the books.")
            $ caldo()
            label tel_chat_editore_a6_1_6:
            if telefono_minuti_blocco("tel_chat_editore_a6_1_6", "ricevi", 1):
                return
            $ msg("editore", "You will. Everyone I respect eventually does. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a6_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a6_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_a6_2:
    label tel_chat_editore_a6_2_1:
    if telefono_minuti_blocco("tel_chat_editore_a6_2_1", "ricevi", 1):
        return
    $ msg("editore", "Every collector is a little in love with what he keeps. Remember that, if you ever become part of someone's collection. M.")
    sp "What a strange thing to say."
    return


## --- A7: la vita editoriale --------------------------------------------------

label chat_editore_a7:
    label tel_chat_editore_a7_1:
    if telefono_minuti_blocco("tel_chat_editore_a7_1", "invia", 1):
        return
    $ msg("sara", "What's a normal day for a publisher? I imagine you reading in an armchair all day.")
    return

label chat_editore_a7_1:
    label tel_chat_editore_a7_1_1:
    if telefono_minuti_blocco("tel_chat_editore_a7_1_1", "ricevi", 2):
        return
    $ msg("editore", "Mornings: lawyers, printers, bankers. Afternoons: authors, who are worse.")
    $ msg("editore", "The armchair comes at night. It is the only part of the day that belongs to me. M.")
    label tel_chat_editore_a7_1_2:
    if telefono_minuti_blocco("tel_chat_editore_a7_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And what do you read at night?»":
            label tel_chat_editore_a7_1_3:
            if telefono_minuti_blocco("tel_chat_editore_a7_1_3", "invia", 1):
                return
            $ msg("sara", "And what do you read at night?")
            $ caldo()
            label tel_chat_editore_a7_1_4:
            if telefono_minuti_blocco("tel_chat_editore_a7_1_4", "ricevi", 1):
                return
            $ msg("editore", "Lately, fifty pages by a young woman who is afraid of her own talent. M." if fatto("ep2_pagine_magnus") else "Old manuscripts, mostly. You learn more from an early draft than from a finished book. M.")
        "«It sounds exhausting.»":
            label tel_chat_editore_a7_1_5:
            if telefono_minuti_blocco("tel_chat_editore_a7_1_5", "invia", 1):
                return
            $ msg("sara", "It sounds exhausting.")
            label tel_chat_editore_a7_1_6:
            if telefono_minuti_blocco("tel_chat_editore_a7_1_6", "ricevi", 1):
                return
            $ msg("editore", "It is. That is why I chose it. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a7_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a7_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_a7_2:
    label tel_chat_editore_a7_2_1:
    if telefono_minuti_blocco("tel_chat_editore_a7_2_1", "ricevi", 1):
        return
    $ msg("editore", "Most manuscripts I reject in a page. A few I keep for a lifetime. The difference is never technique. It is courage. M.")
    return


## --- A8: il talento di Sara (esercizio) --------------------------------------

label chat_editore_a8:
    label tel_chat_editore_a8_1:
    if telefono_minuti_blocco("tel_chat_editore_a8_1", "invia", 1):
        return
    $ msg("sara", "I wrote my three lines every day this week. Is that a good start?")
    return

label chat_editore_a8_1:
    label tel_chat_editore_a8_1_1:
    if telefono_minuti_blocco("tel_chat_editore_a8_1_1", "ricevi", 1):
        return
    $ msg("editore", "It is the only start. Now, an exercise. Describe a room you know well, but through a single sense. Not sight. M.")
    label tel_chat_editore_a8_1_2:
    if telefono_minuti_blocco("tel_chat_editore_a8_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "(Shy) «My kitchen. The fridge humming. The clock. Nothing else.»":
            label tel_chat_editore_a8_1_3:
            if telefono_minuti_blocco("tel_chat_editore_a8_1_3", "invia", 1):
                return
            $ msg("sara", "My kitchen. The fridge humming. The clock. Nothing else.")
            label tel_chat_editore_a8_1_4:
            if telefono_minuti_blocco("tel_chat_editore_a8_1_4", "ricevi", 1):
                return
            $ msg("editore", "Correct and lonely. The loneliness is the interesting part. M.")
        "(Sensory) «The bathroom after a shower. Warm air, wet tiles under my feet, the mirror misted over.»":
            label tel_chat_editore_a8_1_5:
            if telefono_minuti_blocco("tel_chat_editore_a8_1_5", "invia", 1):
                return
            $ msg("sara", "The bathroom after a shower. Warm air, wet tiles under my feet, the mirror misted over.")
            $ confidence(1)
            label tel_chat_editore_a8_1_6:
            if telefono_minuti_blocco("tel_chat_editore_a8_1_6", "ricevi", 1):
                return
            $ msg("editore", "Touch. You chose touch. Interesting. M.")
        "(Bold) «My bedroom at night. The sheets, his breathing, and me awake, wanting something I can't name.»" (confidence=30):
            label tel_chat_editore_a8_1_7:
            if telefono_minuti_blocco("tel_chat_editore_a8_1_7", "invia", 1):
                return
            $ msg("sara", "My bedroom at night. The sheets, his breathing, and me awake, wanting something I can't name.")
            $ caldo()
            label tel_chat_editore_a8_1_8:
            if telefono_minuti_blocco("tel_chat_editore_a8_1_8", "ricevi", 1):
                return
            $ msg("editore", "That, Sara, is a first line. Keep it. M.")
            $ segna("magnus_prima_riga")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a8_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a8_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_a8_2:
    label tel_chat_editore_a8_2_1:
    if telefono_minuti_blocco("tel_chat_editore_a8_2_1", "ricevi", 1):
        return
    $ msg("editore", "You have talent. Not the decorative kind. The dangerous kind. It will ask things of you. M.")
    sp "The dangerous kind."
    label tel_chat_editore_a8_2_2:
    if telefono_minuti_blocco("tel_chat_editore_a8_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What kind of things?»":
            label tel_chat_editore_a8_2_3:
            if telefono_minuti_blocco("tel_chat_editore_a8_2_3", "invia", 1):
                return
            $ msg("sara", "What kind of things?")
            $ caldo()
            label tel_chat_editore_a8_2_4:
            if telefono_minuti_blocco("tel_chat_editore_a8_2_4", "ricevi", 1):
                return
            $ msg("editore", "Honesty, mostly. The rest follows. M.")
        "«Thank you. Really.»":
            label tel_chat_editore_a8_2_5:
            if telefono_minuti_blocco("tel_chat_editore_a8_2_5", "invia", 1):
                return
            $ msg("sara", "Thank you. Really.")
            label tel_chat_editore_a8_2_6:
            if telefono_minuti_blocco("tel_chat_editore_a8_2_6", "ricevi", 1):
                return
            $ msg("editore", "Don't thank me. Write. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a8_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_a8_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B1: le sue esperienze passate -------------------------------------------

label chat_editore_b1:
    label tel_chat_editore_b1_1:
    if telefono_minuti_blocco("tel_chat_editore_b1_1", "invia", 1):
        return
    $ msg("sara", "Daniel says you never married. Was it a choice?")
    return

label chat_editore_b1_1:
    label tel_chat_editore_b1_1_1:
    if telefono_minuti_blocco("tel_chat_editore_b1_1_1", "ricevi", 2):
        return
    $ msg("editore", "Absolutely. Marriage asks a man to love one book forever. I have always preferred a library.")
    $ msg("editore", "I have loved many women. None of them ever regretted it, I believe. Several still dine with me. M.")
    label tel_chat_editore_b1_1_2:
    if telefono_minuti_blocco("tel_chat_editore_b1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Several? At the same table?»":
            label tel_chat_editore_b1_1_3:
            if telefono_minuti_blocco("tel_chat_editore_b1_1_3", "invia", 1):
                return
            $ msg("sara", "Several? At the same table?")
            $ caldo()
            label tel_chat_editore_b1_1_4:
            if telefono_minuti_blocco("tel_chat_editore_b1_1_4", "ricevi", 1):
                return
            $ msg("editore", "Often. They get along beautifully. Jealousy is a lack of imagination. M.")
            $ segna("magnus_cerchia_accenno")
        "«That sounds lonely, in the end.»":
            label tel_chat_editore_b1_1_5:
            if telefono_minuti_blocco("tel_chat_editore_b1_1_5", "invia", 1):
                return
            $ msg("sara", "That sounds lonely, in the end.")
            label tel_chat_editore_b1_1_6:
            if telefono_minuti_blocco("tel_chat_editore_b1_1_6", "ricevi", 1):
                return
            $ msg("editore", "You would be surprised how rarely I am alone. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_b1_2:
    label tel_chat_editore_b1_2_1:
    if telefono_minuti_blocco("tel_chat_editore_b1_2_1", "ricevi", 1):
        return
    $ msg("editore", "And you, Sara. One man, forever. Is that what you want, or what you were told to want? M.")
    sp "Nobody has ever asked me that."
    label tel_chat_editore_b1_2_2:
    if telefono_minuti_blocco("tel_chat_editore_b1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It's what I want.»":
            label tel_chat_editore_b1_2_3:
            if telefono_minuti_blocco("tel_chat_editore_b1_2_3", "invia", 1):
                return
            $ msg("sara", "It's what I want.")
            $ interest("josh", 1)
            label tel_chat_editore_b1_2_4:
            if telefono_minuti_blocco("tel_chat_editore_b1_2_4", "ricevi", 1):
                return
            $ msg("editore", "Then I am glad for you. Truly. M.")
        "«I've never asked myself.»":
            label tel_chat_editore_b1_2_5:
            if telefono_minuti_blocco("tel_chat_editore_b1_2_5", "invia", 1):
                return
            $ msg("sara", "I've never asked myself.")
            $ caldo()
            label tel_chat_editore_b1_2_6:
            if telefono_minuti_blocco("tel_chat_editore_b1_2_6", "ricevi", 1):
                return
            $ msg("editore", "Then do. Writers must ask the questions no one else will. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B2: la paura di non essere all'altezza (esercizio) ----------------------

label chat_editore_b2:
    label tel_chat_editore_b2_1:
    if telefono_minuti_blocco("tel_chat_editore_b2_1", "invia", 1):
        return
    $ msg("sara", "I read what I wrote today and I wanted to delete everything. Does that happen to you?")
    return

label chat_editore_b2_1:
    label tel_chat_editore_b2_1_1:
    if telefono_minuti_blocco("tel_chat_editore_b2_1_1", "ricevi", 2):
        return
    $ msg("editore", "It happens to everyone worth reading. The day it stops happening, worry.")
    $ msg("editore", "Tell me the sentence you wanted to delete most. Exactly as you wrote it. M.")
    label tel_chat_editore_b2_1_2:
    if telefono_minuti_blocco("tel_chat_editore_b2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "(Shy) «She looked at him and smiled.»":
            label tel_chat_editore_b2_1_3:
            if telefono_minuti_blocco("tel_chat_editore_b2_1_3", "invia", 1):
                return
            $ msg("sara", "She looked at him and smiled.")
            label tel_chat_editore_b2_1_4:
            if telefono_minuti_blocco("tel_chat_editore_b2_1_4", "ricevi", 1):
                return
            $ msg("editore", "Delete it. You were right. It is a sentence that wants to be invisible. M.")
        "(Sensory) «She could feel his eyes on her neck before she turned.»":
            label tel_chat_editore_b2_1_5:
            if telefono_minuti_blocco("tel_chat_editore_b2_1_5", "invia", 1):
                return
            $ msg("sara", "She could feel his eyes on her neck before she turned.")
            $ confidence(1)
            label tel_chat_editore_b2_1_6:
            if telefono_minuti_blocco("tel_chat_editore_b2_1_6", "ricevi", 1):
                return
            $ msg("editore", "Keep it. Why did you want to delete it? Because it is true? M.")
        "(Bold) «She didn't want him to stop, and she hated herself for it.»" (confidence=35):
            label tel_chat_editore_b2_1_7:
            if telefono_minuti_blocco("tel_chat_editore_b2_1_7", "invia", 1):
                return
            $ msg("sara", "She didn't want him to stop, and she hated herself for it.")
            $ caldo()
            label tel_chat_editore_b2_1_8:
            if telefono_minuti_blocco("tel_chat_editore_b2_1_8", "ricevi", 1):
                return
            $ msg("editore", "You wanted to delete the only sentence that is alive. Don't you dare. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_b2_2:
    label tel_chat_editore_b2_2_1:
    if telefono_minuti_blocco("tel_chat_editore_b2_2_1", "ricevi", 1):
        return
    $ msg("editore", "Your fear is not that you are bad. Your fear is that you are good at something you were taught to be ashamed of. M.")
    sp "He sees everything."
    return


## --- B3: bellezza e maturità -------------------------------------------------

label chat_editore_b3:
    label tel_chat_editore_b3_1:
    if telefono_minuti_blocco("tel_chat_editore_b3_1", "invia", 1):
        return
    $ msg("sara", "Do you ever feel old, Magnus? You never seem to.")
    return

label chat_editore_b3_1:
    label tel_chat_editore_b3_1_1:
    if telefono_minuti_blocco("tel_chat_editore_b3_1_1", "ricevi", 2):
        return
    $ msg("editore", "I feel old every morning and young every evening. At my age beauty is no longer something I have. It is something I recognise.")
    $ msg("editore", "Recognising it is a far rarer skill. Most men only possess. M.")
    label tel_chat_editore_b3_1_2:
    if telefono_minuti_blocco("tel_chat_editore_b3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What do you recognise?»":
            label tel_chat_editore_b3_1_3:
            if telefono_minuti_blocco("tel_chat_editore_b3_1_3", "invia", 1):
                return
            $ msg("sara", "What do you recognise?")
            $ caldo()
            label tel_chat_editore_b3_1_4:
            if telefono_minuti_blocco("tel_chat_editore_b3_1_4", "ricevi", 1):
                return
            $ msg("editore", "The moment a woman stops performing and becomes herself. It is brief. It is unforgettable. M.")
        "«You're wiser than most men half your age.»":
            label tel_chat_editore_b3_1_5:
            if telefono_minuti_blocco("tel_chat_editore_b3_1_5", "invia", 1):
                return
            $ msg("sara", "You're wiser than most men half your age.")
            label tel_chat_editore_b3_1_6:
            if telefono_minuti_blocco("tel_chat_editore_b3_1_6", "ricevi", 1):
                return
            $ msg("editore", "That is not a high bar, I'm afraid. But thank you. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_b3_2:
    label tel_chat_editore_b3_2_1:
    if telefono_minuti_blocco("tel_chat_editore_b3_2_1", "ricevi", 1):
        return
    $ msg("editore", "I saw that moment in you, once, at Daniel's party. For about four seconds. M.")
    sp "Four seconds. When?"
    label tel_chat_editore_b3_2_2:
    if telefono_minuti_blocco("tel_chat_editore_b3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«When?»":
            label tel_chat_editore_b3_2_3:
            if telefono_minuti_blocco("tel_chat_editore_b3_2_3", "invia", 1):
                return
            $ msg("sara", "When?")
            $ caldo()
            label tel_chat_editore_b3_2_4:
            if telefono_minuti_blocco("tel_chat_editore_b3_2_4", "ricevi", 1):
                return
            $ msg("editore", "When you laughed at something you should not have found funny. M.")
        "«I think you're flattering me.»":
            label tel_chat_editore_b3_2_5:
            if telefono_minuti_blocco("tel_chat_editore_b3_2_5", "invia", 1):
                return
            $ msg("sara", "I think you're flattering me.")
            label tel_chat_editore_b3_2_6:
            if telefono_minuti_blocco("tel_chat_editore_b3_2_6", "ricevi", 1):
                return
            $ msg("editore", "I am too old to flatter. It wastes time I no longer have. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B4: il potere delle parole (esercizio sensuale) -------------------------

label chat_editore_b4:
    label tel_chat_editore_b4_1:
    if telefono_minuti_blocco("tel_chat_editore_b4_1", "invia", 1):
        return
    $ msg("sara", "Give me another exercise. A hard one.")
    return

label chat_editore_b4_1:
    label tel_chat_editore_b4_1_1:
    if telefono_minuti_blocco("tel_chat_editore_b4_1_1", "ricevi", 1):
        return
    $ msg("editore", "As you wish. Describe a kiss without using the word «kiss». Four lines at most. M.")
    label tel_chat_editore_b4_1_2:
    if telefono_minuti_blocco("tel_chat_editore_b4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "(Shy) «Their lips touched. It was soft. Then it was over. She smiled.»":
            label tel_chat_editore_b4_1_3:
            if telefono_minuti_blocco("tel_chat_editore_b4_1_3", "invia", 1):
                return
            $ msg("sara", "Their lips touched. It was soft. Then it was over. She smiled.")
            label tel_chat_editore_b4_1_4:
            if telefono_minuti_blocco("tel_chat_editore_b4_1_4", "ricevi", 1):
                return
            $ msg("editore", "You described a postcard. Try again, one day, when no one is watching. M.")
        "(Sensory) «His breath first. Warm, slow. Then the taste of wine. She forgot the room.»":
            label tel_chat_editore_b4_1_5:
            if telefono_minuti_blocco("tel_chat_editore_b4_1_5", "invia", 1):
                return
            $ msg("sara", "His breath first. Warm, slow. Then the taste of wine. She forgot the room.")
            $ confidence(1)
            label tel_chat_editore_b4_1_6:
            if telefono_minuti_blocco("tel_chat_editore_b4_1_6", "ricevi", 1):
                return
            $ msg("editore", "She forgot the room. Good. Now make her forget her name. M.")
        "(Bold) «She meant to pull away. Her hands didn't. His mouth asked a question and her body answered before she could.»" (confidence=40):
            label tel_chat_editore_b4_1_7:
            if telefono_minuti_blocco("tel_chat_editore_b4_1_7", "invia", 1):
                return
            $ msg("sara", "She meant to pull away. Her hands didn't. His mouth asked a question and her body answered before she could.")
            $ caldo()
            $ corruption(1)
            label tel_chat_editore_b4_1_8:
            if telefono_minuti_blocco("tel_chat_editore_b4_1_8", "ricevi", 1):
                return
            $ msg("editore", "Sara. That is publishable. You have just written the first honest page of your career. M.")
            $ segna("magnus_bacio_scritto")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_b4_2:
    label tel_chat_editore_b4_2_1:
    if telefono_minuti_blocco("tel_chat_editore_b4_2_1", "ricevi", 1):
        return
    $ msg("editore", "Words can do to a reader what hands do to a body. Few writers dare to use them that way. M.")
    sp "I wrote that. Me."
    return


## --- B5: il bisogno di essere compresi ---------------------------------------

label chat_editore_b5:
    label tel_chat_editore_b5_1:
    if telefono_minuti_blocco("tel_chat_editore_b5_1", "invia", 1):
        return
    $ msg("sara", "Can I tell you something? You're the only person who reads me without wanting me to be different.")
    return

label chat_editore_b5_1:
    label tel_chat_editore_b5_1_1:
    if telefono_minuti_blocco("tel_chat_editore_b5_1_1", "ricevi", 2):
        return
    $ msg("editore", "Then everyone else in your life is wasting a remarkable opportunity.")
    $ msg("editore", "Does [nome_compagno] read you? M.")
    label tel_chat_editore_b5_1_2:
    if telefono_minuti_blocco("tel_chat_editore_b5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«He tries. He's not a reader.»":
            label tel_chat_editore_b5_1_3:
            if telefono_minuti_blocco("tel_chat_editore_b5_1_3", "invia", 1):
                return
            $ msg("sara", "He tries. He's not a reader.")
            label tel_chat_editore_b5_1_4:
            if telefono_minuti_blocco("tel_chat_editore_b5_1_4", "ricevi", 1):
                return
            $ msg("editore", "Trying is generous. It is also not the same thing. M.")
        "«He loves me. That's different.»":
            label tel_chat_editore_b5_1_5:
            if telefono_minuti_blocco("tel_chat_editore_b5_1_5", "invia", 1):
                return
            $ msg("sara", "He loves me. That's different.")
            $ interest("josh", 1)
            label tel_chat_editore_b5_1_6:
            if telefono_minuti_blocco("tel_chat_editore_b5_1_6", "ricevi", 1):
                return
            $ msg("editore", "It is different. Whether it is enough is a question only you can answer. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_b5_2:
    label tel_chat_editore_b5_2_1:
    if telefono_minuti_blocco("tel_chat_editore_b5_2_1", "ricevi", 1):
        return
    $ msg("editore", "To be understood is the rarest pleasure. Rarer than love. Rarer than desire. I offer it freely, and ask only honesty in return. M.")
    sp "Only honesty. That sounds easy. It isn't."
    label tel_chat_editore_b5_2_2:
    if telefono_minuti_blocco("tel_chat_editore_b5_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Then I'll be honest with you.»":
            label tel_chat_editore_b5_2_3:
            if telefono_minuti_blocco("tel_chat_editore_b5_2_3", "invia", 1):
                return
            $ msg("sara", "Then I'll be honest with you.")
            $ caldo()
            label tel_chat_editore_b5_2_4:
            if telefono_minuti_blocco("tel_chat_editore_b5_2_4", "ricevi", 1):
                return
            $ msg("editore", "I know. You already are, on the page. M.")
        "«Good night, Magnus.»":
            label tel_chat_editore_b5_2_5:
            if telefono_minuti_blocco("tel_chat_editore_b5_2_5", "invia", 1):
                return
            $ msg("sara", "Good night, Magnus.")
            label tel_chat_editore_b5_2_6:
            if telefono_minuti_blocco("tel_chat_editore_b5_2_6", "ricevi", 1):
                return
            $ msg("editore", "Good night, Sara. Write three lines before you sleep. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b5_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_b5_2_2"
            $ telefono_minuti_chiudi = True
            return
    return
