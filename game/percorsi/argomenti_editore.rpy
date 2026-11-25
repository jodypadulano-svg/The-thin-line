## GENERATO da tools/telefono/componi.py: si modifica tools/telefono/editore.txt.

init python:
    discorso("editore_t1", "editore", ESTRANEI, argomento="Your card", se="fatto('ep1_d13_biglietto') and not fatto('ep2_pagine_magnus')")
    discorso("editore_t2", "editore", ESTRANEI, argomento="The pages I sent", se="fatto('ep2_pagine_magnus') and giorno < 23")
    discorso("editore_t3", "editore", ESTRANEI, argomento="Your two questions", se="fatto('ep1_d13_magnus_pagine')")
    discorso("editore_c1", "editore", COMPLICI, flirt=True)
    discorso("editore_c2", "editore", COMPLICI, flirt=True)
    discorso("editore_d1", "editore", INTIMI, flirt=True)
    discorso("editore_d2", "editore", INTIMI, flirt=True)
    discorso("editore_n1", "editore", COMPLICI, flirt=True, ricambiato=False)
    discorso("editore_n2", "editore", INTIMI, flirt=True, ricambiato=False)


## --- Your card

label chat_editore_t1:
    label tel_chat_editore_t1_1:
    if telefono_minuti_blocco("tel_chat_editore_t1_1", "invia", 1):
        return
    $ msg("sara", "I keep your card in my notebook. I've read the back of it more than the front.")
    return

label chat_editore_t1_entrata:
    label tel_chat_editore_t1_entrata_1:
    if telefono_minuti_blocco("tel_chat_editore_t1_entrata_1", "ricevi", 1):
        return
    $ msg("editore", "I have been wondering what became of my card. M.")
    label tel_chat_editore_t1_entrata_2:
    if telefono_minuti_blocco("tel_chat_editore_t1_entrata_2", "invia", 1):
        return
    $ msg("sara", "It's in my notebook. I've read the back of it more than the front.")
    return

label chat_editore_t1_1:
    label tel_chat_editore_t1_1_1:
    if telefono_minuti_blocco("tel_chat_editore_t1_1_1", "ricevi", 1):
        return
    $ msg("editore", "The front is for the post office. The back is for you. M.")
    label tel_chat_editore_t1_1_2:
    if telefono_minuti_blocco("tel_chat_editore_t1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "««You're not allowed to hide.» How did you know I was?»":
            label tel_chat_editore_t1_1_3:
            if telefono_minuti_blocco("tel_chat_editore_t1_1_3", "invia", 1):
                return
            $ msg("sara", "«You're not allowed to hide.» How did you know I was?")
            $ caldo()
            label tel_chat_editore_t1_1_4:
            if telefono_minuti_blocco("tel_chat_editore_t1_1_4", "ricevi", 1):
                return
            $ msg("editore", "You stood beside every door in that house. People who are not hiding stand beside the food. M.")
        "«Why fifty?»":
            label tel_chat_editore_t1_1_5:
            if telefono_minuti_blocco("tel_chat_editore_t1_1_5", "invia", 1):
                return
            $ msg("sara", "Why fifty?")
            label tel_chat_editore_t1_1_6:
            if telefono_minuti_blocco("tel_chat_editore_t1_1_6", "ricevi", 1):
                return
            $ msg("editore", "At thirty a writer is still clearing her throat. At seventy she has begun to like the sound of it. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_t1_2:
    label tel_chat_editore_t1_2_1:
    if telefono_minuti_blocco("tel_chat_editore_t1_2_1", "ricevi", 1):
        return
    $ msg("editore", "May I ask what you are doing to them, at this moment? You are doing something. I can hear the rustling.")
    label tel_chat_editore_t1_2_2:
    if telefono_minuti_blocco("tel_chat_editore_t1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Moving one sentence back and forth.»":
            label tel_chat_editore_t1_2_3:
            if telefono_minuti_blocco("tel_chat_editore_t1_2_3", "invia", 1):
                return
            $ msg("sara", "Moving one sentence back and forth.")
            $ caldo()
            label tel_chat_editore_t1_2_4:
            if telefono_minuti_blocco("tel_chat_editore_t1_2_4", "ricevi", 1):
                return
            $ msg("editore", "Then it is the one. Leave it where it frightens you. M.")
        "«Taking out the bits I'm ashamed of.»":
            label tel_chat_editore_t1_2_5:
            if telefono_minuti_blocco("tel_chat_editore_t1_2_5", "invia", 1):
                return
            $ msg("sara", "Taking out the bits I'm ashamed of.")
            label tel_chat_editore_t1_2_6:
            if telefono_minuti_blocco("tel_chat_editore_t1_2_6", "ricevi", 1):
                return
            $ msg("editore", "Kindly put them back. I can buy modesty anywhere. M.")
        "«Nothing. I'm afraid to open the file.»":
            label tel_chat_editore_t1_2_7:
            if telefono_minuti_blocco("tel_chat_editore_t1_2_7", "invia", 1):
                return
            $ msg("sara", "Nothing. I'm afraid to open the file.")
            label tel_chat_editore_t1_2_8:
            if telefono_minuti_blocco("tel_chat_editore_t1_2_8", "ricevi", 1):
                return
            $ msg("editore", "Open it and change one comma. The rest will think you mean business. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_t1_3:
    label tel_chat_editore_t1_3_1:
    if telefono_minuti_blocco("tel_chat_editore_t1_3_1", "ricevi", 1):
        return
    $ msg("editore", "You will be told, by kind people, that they are wonderful. Thank them, and do not listen.")
    label tel_chat_editore_t1_3_2:
    if telefono_minuti_blocco("tel_chat_editore_t1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Who should I listen to, then?»":
            label tel_chat_editore_t1_3_3:
            if telefono_minuti_blocco("tel_chat_editore_t1_3_3", "invia", 1):
                return
            $ msg("sara", "Who should I listen to, then?")
            label tel_chat_editore_t1_3_4:
            if telefono_minuti_blocco("tel_chat_editore_t1_3_4", "ricevi", 1):
                return
            $ msg("editore", "To whoever falls silent. M.")
        "«You sound as if you've been told that yourself.»":
            label tel_chat_editore_t1_3_5:
            if telefono_minuti_blocco("tel_chat_editore_t1_3_5", "invia", 1):
                return
            $ msg("sara", "You sound as if you've been told that yourself.")
            label tel_chat_editore_t1_3_6:
            if telefono_minuti_blocco("tel_chat_editore_t1_3_6", "ricevi", 1):
                return
            $ msg("editore", "Once, for eleven years, by a charming man. I have not written a line since he died. Good night, Sara. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The pages I sent

label chat_editore_t2:
    label tel_chat_editore_t2_1:
    if telefono_minuti_blocco("tel_chat_editore_t2_1", "invia", 1):
        return
    $ msg("sara", "I promised myself I wouldn't ask if you'd started.")
    return

label chat_editore_t2_entrata:
    label tel_chat_editore_t2_entrata_1:
    if telefono_minuti_blocco("tel_chat_editore_t2_entrata_1", "ricevi", 1):
        return
    $ msg("editore", "You have been admirably silent. M.")
    label tel_chat_editore_t2_entrata_2:
    if telefono_minuti_blocco("tel_chat_editore_t2_entrata_2", "invia", 1):
        return
    $ msg("sara", "I promised myself I wouldn't ask if you'd started.")
    return

label chat_editore_t2_1:
    label tel_chat_editore_t2_1_1:
    if telefono_minuti_blocco("tel_chat_editore_t2_1_1", "ricevi", 1):
        return
    $ msg("editore", "And you have kept your word beautifully. You have merely informed me that you are not asking. M.")
    label tel_chat_editore_t2_1_2:
    if telefono_minuti_blocco("tel_chat_editore_t2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Is it working?»":
            label tel_chat_editore_t2_1_3:
            if telefono_minuti_blocco("tel_chat_editore_t2_1_3", "invia", 1):
                return
            $ msg("sara", "Is it working?")
            $ caldo()
            label tel_chat_editore_t2_1_4:
            if telefono_minuti_blocco("tel_chat_editore_t2_1_4", "ricevi", 1):
                return
            $ msg("editore", "I am seventy-one. I have been not-asked by experts. M.")
        "«I'm sorry. I'll go away.»":
            label tel_chat_editore_t2_1_5:
            if telefono_minuti_blocco("tel_chat_editore_t2_1_5", "invia", 1):
                return
            $ msg("sara", "I'm sorry. I'll go away.")
            label tel_chat_editore_t2_1_6:
            if telefono_minuti_blocco("tel_chat_editore_t2_1_6", "ricevi", 1):
                return
            $ msg("editore", "Please do not apologise. It is a good sign. Bad writers are never curious. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_t2_2:
    label tel_chat_editore_t2_2_1:
    if telefono_minuti_blocco("tel_chat_editore_t2_2_1", "ricevi", 1):
        return
    $ msg("editore", "I can tell you how I read, if it would help you to sleep. I print them. I sit by a window with no telephone. I begin only when I have nothing to do afterwards.")
    label tel_chat_editore_t2_2_2:
    if telefono_minuti_blocco("tel_chat_editore_t2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«How long does it take you?»":
            label tel_chat_editore_t2_2_3:
            if telefono_minuti_blocco("tel_chat_editore_t2_2_3", "invia", 1):
                return
            $ msg("sara", "How long does it take you?")
            label tel_chat_editore_t2_2_4:
            if telefono_minuti_blocco("tel_chat_editore_t2_2_4", "ricevi", 1):
                return
            $ msg("editore", "As long as it deserves. I have finished some manuscripts between two floors, in a lift. M.")
        "«So they're being read by daylight.»":
            label tel_chat_editore_t2_2_5:
            if telefono_minuti_blocco("tel_chat_editore_t2_2_5", "invia", 1):
                return
            $ msg("sara", "So they're being read by daylight.")
            $ caldo()
            label tel_chat_editore_t2_2_6:
            if telefono_minuti_blocco("tel_chat_editore_t2_2_6", "ricevi", 1):
                return
            $ msg("editore", "By nothing else. Lamps are for people who already know how it ends. M.")
            sp "He prints them. He sits by a window with me in his hands."
        "«That makes it worse.»":
            label tel_chat_editore_t2_2_7:
            if telefono_minuti_blocco("tel_chat_editore_t2_2_7", "invia", 1):
                return
            $ msg("sara", "That makes it worse.")
            label tel_chat_editore_t2_2_8:
            if telefono_minuti_blocco("tel_chat_editore_t2_2_8", "ricevi", 1):
                return
            $ msg("editore", "I expect it does. Good. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_t2_3:
    label tel_chat_editore_t2_3_1:
    if telefono_minuti_blocco("tel_chat_editore_t2_3_1", "ricevi", 1):
        return
    $ msg("editore", "While you wait, do not touch page fifty-one. Let it come to the fence by itself.")
    label tel_chat_editore_t2_3_2:
    if telefono_minuti_blocco("tel_chat_editore_t2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It already has.»":
            label tel_chat_editore_t2_3_3:
            if telefono_minuti_blocco("tel_chat_editore_t2_3_3", "invia", 1):
                return
            $ msg("sara", "It already has.")
            label tel_chat_editore_t2_3_4:
            if telefono_minuti_blocco("tel_chat_editore_t2_3_4", "ricevi", 1):
                return
            $ msg("editore", "Then do not look it in the eye. M.")
        "«I changed the ending the night I sent them.»":
            label tel_chat_editore_t2_3_5:
            if telefono_minuti_blocco("tel_chat_editore_t2_3_5", "invia", 1):
                return
            $ msg("sara", "I changed the ending the night I sent them.")
            label tel_chat_editore_t2_3_6:
            if telefono_minuti_blocco("tel_chat_editore_t2_3_6", "ricevi", 1):
                return
            $ msg("editore", "I know. The ink is different. I do not mean the ink. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Your two questions

label chat_editore_t3:
    label tel_chat_editore_t3_1:
    if telefono_minuti_blocco("tel_chat_editore_t3_1", "invia", 1):
        return
    $ msg("sara", "You asked me who's telling it, and whether she wants to be found. I've changed my mind about the second.")
    return

label chat_editore_t3_1:
    label tel_chat_editore_t3_1_1:
    if telefono_minuti_blocco("tel_chat_editore_t3_1_1", "ricevi", 1):
        return
    $ msg("editore", "How splendid. I ask it of everyone. You are the first to send in a correction. M.")
    label tel_chat_editore_t3_1_2:
    if telefono_minuti_blocco("tel_chat_editore_t3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I said «not yet». I think she does.»":
            label tel_chat_editore_t3_1_3:
            if telefono_minuti_blocco("tel_chat_editore_t3_1_3", "invia", 1):
                return
            $ msg("sara", "I said «not yet». I think she does.")
            $ caldo()
            label tel_chat_editore_t3_1_4:
            if telefono_minuti_blocco("tel_chat_editore_t3_1_4", "ricevi", 1):
                return
            $ msg("editore", "By whom? That is the third question. I never ask it in the same evening. M.")
        "«I think she wants to be looked for.»":
            label tel_chat_editore_t3_1_5:
            if telefono_minuti_blocco("tel_chat_editore_t3_1_5", "invia", 1):
                return
            $ msg("sara", "I think she wants to be looked for.")
            label tel_chat_editore_t3_1_6:
            if telefono_minuti_blocco("tel_chat_editore_t3_1_6", "ricevi", 1):
                return
            $ msg("editore", "Ah. That is a different animal. It sleeps in the day. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_t3_2:
    label tel_chat_editore_t3_2_1:
    if telefono_minuti_blocco("tel_chat_editore_t3_2_1", "ricevi", 1):
        return
    $ msg("editore", "Does she know it herself?")
    label tel_chat_editore_t3_2_2:
    if telefono_minuti_blocco("tel_chat_editore_t3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«She's the last to know.»":
            label tel_chat_editore_t3_2_3:
            if telefono_minuti_blocco("tel_chat_editore_t3_2_3", "invia", 1):
                return
            $ msg("sara", "She's the last to know.")
            label tel_chat_editore_t3_2_4:
            if telefono_minuti_blocco("tel_chat_editore_t3_2_4", "ricevi", 1):
                return
            $ msg("editore", "Then keep her ignorant a little longer. It is becoming, in a heroine, up to about page two hundred. M.")
        "«She's starting to. It's in how she stands.»":
            label tel_chat_editore_t3_2_5:
            if telefono_minuti_blocco("tel_chat_editore_t3_2_5", "invia", 1):
                return
            $ msg("sara", "She's starting to. It's in how she stands.")
            $ caldo()
            label tel_chat_editore_t3_2_6:
            if telefono_minuti_blocco("tel_chat_editore_t3_2_6", "ricevi", 1):
                return
            $ msg("editore", "Yes. Bodies are such gossips. M.")
        "«I'd rather not say.»":
            label tel_chat_editore_t3_2_7:
            if telefono_minuti_blocco("tel_chat_editore_t3_2_7", "invia", 1):
                return
            $ msg("sara", "I'd rather not say.")
            label tel_chat_editore_t3_2_8:
            if telefono_minuti_blocco("tel_chat_editore_t3_2_8", "ricevi", 1):
                return
            $ msg("editore", "Quite right. Never tell an editor anything you have not yet told the page. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_t3_3:
    label tel_chat_editore_t3_3_1:
    if telefono_minuti_blocco("tel_chat_editore_t3_3_1", "ricevi", 1):
        return
    $ msg("editore", "I shall be frank. I do not much care for plots. People want things, and then they reach for them. Everything else is furniture.")
    label tel_chat_editore_t3_3_2:
    if telefono_minuti_blocco("tel_chat_editore_t3_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And if she reaches?»":
            label tel_chat_editore_t3_3_3:
            if telefono_minuti_blocco("tel_chat_editore_t3_3_3", "invia", 1):
                return
            $ msg("sara", "And if she reaches?")
            label tel_chat_editore_t3_3_4:
            if telefono_minuti_blocco("tel_chat_editore_t3_3_4", "ricevi", 1):
                return
            $ msg("editore", "Then I shall turn the page rather quickly, for a man of my age. M.")
        "«And if she doesn't?»":
            label tel_chat_editore_t3_3_5:
            if telefono_minuti_blocco("tel_chat_editore_t3_3_5", "invia", 1):
                return
            $ msg("sara", "And if she doesn't?")
            label tel_chat_editore_t3_3_6:
            if telefono_minuti_blocco("tel_chat_editore_t3_3_6", "ricevi", 1):
                return
            $ msg("editore", "Then you will have written a very well-furnished room. Good night. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t3_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_t3_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: una musa

label chat_editore_c1:
    label tel_chat_editore_c1_1:
    if telefono_minuti_blocco("tel_chat_editore_c1_1", "invia", 1):
        return
    $ msg("sara", "Have you ever been somebody's muse?")
    return

label chat_editore_c1_1:
    label tel_chat_editore_c1_1_1:
    if telefono_minuti_blocco("tel_chat_editore_c1_1_1", "ricevi", 1):
        return
    $ msg("editore", "Twice. One painted me as a lamp. I was very good-looking at the time, and it is a fair likeness. M.")
    label tel_chat_editore_c1_1_2:
    if telefono_minuti_blocco("tel_chat_editore_c1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And yours? Who were they?»":
            label tel_chat_editore_c1_1_3:
            if telefono_minuti_blocco("tel_chat_editore_c1_1_3", "invia", 1):
                return
            $ msg("sara", "And yours? Who were they?")
            $ caldo()
            label tel_chat_editore_c1_1_4:
            if telefono_minuti_blocco("tel_chat_editore_c1_1_4", "ricevi", 1):
                return
            $ msg("editore", "They would not wish to be a list. Each was an only copy. M.")
        "«I can't picture it.»":
            label tel_chat_editore_c1_1_5:
            if telefono_minuti_blocco("tel_chat_editore_c1_1_5", "invia", 1):
                return
            $ msg("sara", "I can't picture it.")
            label tel_chat_editore_c1_1_6:
            if telefono_minuti_blocco("tel_chat_editore_c1_1_6", "ricevi", 1):
                return
            $ msg("editore", "Nobody can, now. It is one of the liberties of age. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_c1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_c1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_c1_2:
    label tel_chat_editore_c1_2_1:
    if telefono_minuti_blocco("tel_chat_editore_c1_2_1", "ricevi", 1):
        return
    $ msg("editore", "You ask because somebody has told you that you might be one. Or because you would like to be told.")
    label tel_chat_editore_c1_2_2:
    if telefono_minuti_blocco("tel_chat_editore_c1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«The second.»":
            label tel_chat_editore_c1_2_3:
            if telefono_minuti_blocco("tel_chat_editore_c1_2_3", "invia", 1):
                return
            $ msg("sara", "The second.")
            $ caldo()
            label tel_chat_editore_c1_2_4:
            if telefono_minuti_blocco("tel_chat_editore_c1_2_4", "ricevi", 1):
                return
            $ msg("editore", "Then I will tell you. A muse is not beautiful. She is attentive, and one becomes interesting in her presence. You have that. It is rather ruinous. M.")
        "«Neither. I want to write one.»":
            label tel_chat_editore_c1_2_5:
            if telefono_minuti_blocco("tel_chat_editore_c1_2_5", "invia", 1):
                return
            $ msg("sara", "Neither. I want to write one.")
            label tel_chat_editore_c1_2_6:
            if telefono_minuti_blocco("tel_chat_editore_c1_2_6", "ricevi", 1):
                return
            $ msg("editore", "Then give her bad shoes and a will of her own. M.")
        "«I'd rather be the one with the pen.»":
            label tel_chat_editore_c1_2_7:
            if telefono_minuti_blocco("tel_chat_editore_c1_2_7", "invia", 1):
                return
            $ msg("sara", "I'd rather be the one with the pen.")
            label tel_chat_editore_c1_2_8:
            if telefono_minuti_blocco("tel_chat_editore_c1_2_8", "ricevi", 1):
                return
            $ msg("editore", "My dear, you already are. I am the one sitting still. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_c1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_c1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_c1_3:
    label tel_chat_editore_c1_3_1:
    if telefono_minuti_blocco("tel_chat_editore_c1_3_1", "ricevi", 1):
        return
    $ msg("editore", "You must not think I am courting you. I gave it up, as one gives up stairs.")
    label tel_chat_editore_c1_3_2:
    if telefono_minuti_blocco("tel_chat_editore_c1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I might be. Courting you.»":
            label tel_chat_editore_c1_3_3:
            if telefono_minuti_blocco("tel_chat_editore_c1_3_3", "invia", 1):
                return
            $ msg("sara", "I might be. Courting you.")
            label tel_chat_editore_c1_3_4:
            if telefono_minuti_blocco("tel_chat_editore_c1_3_4", "ricevi", 1):
                return
            $ msg("editore", "Then I shall put on the better jacket and say nothing at all. M.")
        "«I know. That's what's restful about it.»":
            label tel_chat_editore_c1_3_5:
            if telefono_minuti_blocco("tel_chat_editore_c1_3_5", "invia", 1):
                return
            $ msg("sara", "I know. That's what's restful about it.")
            label tel_chat_editore_c1_3_6:
            if telefono_minuti_blocco("tel_chat_editore_c1_3_6", "ricevi", 1):
                return
            $ msg("editore", "Restful. I have been called worse by handsomer women, though not recently. M.")
        "«Good night, Magnus.»":
            label tel_chat_editore_c1_3_7:
            if telefono_minuti_blocco("tel_chat_editore_c1_3_7", "invia", 1):
                return
            $ msg("sara", "Good night, Magnus.")
            $ frena()
            label tel_chat_editore_c1_3_8:
            if telefono_minuti_blocco("tel_chat_editore_c1_3_8", "ricevi", 1):
                return
            $ msg("editore", "Good night, Sara. You see? One may stop in the middle of a line. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_c1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_c1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: un incontro privato

label chat_editore_c2:
    label tel_chat_editore_c2_1:
    if telefono_minuti_blocco("tel_chat_editore_c2_1", "invia", 1):
        return
    $ msg("sara", "Would you let me see the library, one day? Only the library.")
    return

label chat_editore_c2_1:
    label tel_chat_editore_c2_1_1:
    if telefono_minuti_blocco("tel_chat_editore_c2_1_1", "ricevi", 1):
        return
    $ msg("editore", "It is the only room in the house that has never been tidied for guests. I should have to think who you would be. M.")
    label tel_chat_editore_c2_1_2:
    if telefono_minuti_blocco("tel_chat_editore_c2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«A reader.»":
            label tel_chat_editore_c2_1_3:
            if telefono_minuti_blocco("tel_chat_editore_c2_1_3", "invia", 1):
                return
            $ msg("sara", "A reader.")
            $ caldo()
            label tel_chat_editore_c2_1_4:
            if telefono_minuti_blocco("tel_chat_editore_c2_1_4", "ricevi", 1):
                return
            $ msg("editore", "Then there is a chair by the second window. Nobody has sat there since a lady who corrected my Greek. M.")
        "«Not a guest, then.»":
            label tel_chat_editore_c2_1_5:
            if telefono_minuti_blocco("tel_chat_editore_c2_1_5", "invia", 1):
                return
            $ msg("sara", "Not a guest, then.")
            label tel_chat_editore_c2_1_6:
            if telefono_minuti_blocco("tel_chat_editore_c2_1_6", "ricevi", 1):
                return
            $ msg("editore", "No. I rather thought not. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_c2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_c2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_c2_2:
    label tel_chat_editore_c2_2_1:
    if telefono_minuti_blocco("tel_chat_editore_c2_2_1", "ricevi", 1):
        return
    $ msg("editore", "You would have to be quiet. I read aloud, when I am alone, and I do not stop for company.")
    label tel_chat_editore_c2_2_2:
    if telefono_minuti_blocco("tel_chat_editore_c2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What would you read me?»":
            label tel_chat_editore_c2_2_3:
            if telefono_minuti_blocco("tel_chat_editore_c2_2_3", "invia", 1):
                return
            $ msg("sara", "What would you read me?")
            $ caldo()
            label tel_chat_editore_c2_2_4:
            if telefono_minuti_blocco("tel_chat_editore_c2_2_4", "ricevi", 1):
                return
            $ msg("editore", "Something improper, in a very proper voice. It is the only way to hear the grammar. M.")
        "«I'm very good at quiet.»":
            label tel_chat_editore_c2_2_5:
            if telefono_minuti_blocco("tel_chat_editore_c2_2_5", "invia", 1):
                return
            $ msg("sara", "I'm very good at quiet.")
            label tel_chat_editore_c2_2_6:
            if telefono_minuti_blocco("tel_chat_editore_c2_2_6", "ricevi", 1):
                return
            $ msg("editore", "I had noticed. I have wondered what it costs you. M.")
        "«On second thoughts, I'd better not.»":
            label tel_chat_editore_c2_2_7:
            if telefono_minuti_blocco("tel_chat_editore_c2_2_7", "invia", 1):
                return
            $ msg("sara", "On second thoughts, I'd better not.")
            $ frena()
            label tel_chat_editore_c2_2_8:
            if telefono_minuti_blocco("tel_chat_editore_c2_2_8", "ricevi", 1):
                return
            $ msg("editore", "Second thoughts are the best edition. The chair is patient. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_c2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_c2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_c2_3:
    label tel_chat_editore_c2_3_1:
    if telefono_minuti_blocco("tel_chat_editore_c2_3_1", "ricevi", 1):
        return
    $ msg("editore", "There would be tea. There might be a fire. I make no other promises, and I ask for none.")
    label tel_chat_editore_c2_3_2:
    if telefono_minuti_blocco("tel_chat_editore_c2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'd bring nothing but a pencil.»":
            label tel_chat_editore_c2_3_3:
            if telefono_minuti_blocco("tel_chat_editore_c2_3_3", "invia", 1):
                return
            $ msg("sara", "I'd bring nothing but a pencil.")
            label tel_chat_editore_c2_3_4:
            if telefono_minuti_blocco("tel_chat_editore_c2_3_4", "ricevi", 1):
                return
            $ msg("editore", "Then you will be overdressed for the occasion. I mean the pencil. M.")
        "«And if I fell asleep in the chair?»":
            label tel_chat_editore_c2_3_5:
            if telefono_minuti_blocco("tel_chat_editore_c2_3_5", "invia", 1):
                return
            $ msg("sara", "And if I fell asleep in the chair?")
            label tel_chat_editore_c2_3_6:
            if telefono_minuti_blocco("tel_chat_editore_c2_3_6", "ricevi", 1):
                return
            $ msg("editore", "I should mark the place. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_c2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_c2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: confessioni

label chat_editore_d1:
    label tel_chat_editore_d1_1:
    if telefono_minuti_blocco("tel_chat_editore_d1_1", "invia", 1):
        return
    $ msg("sara", "I tried to write about it, and I couldn't find a verb.")
    return

label chat_editore_d1_1:
    label tel_chat_editore_d1_1_1:
    if telefono_minuti_blocco("tel_chat_editore_d1_1_1", "ricevi", 1):
        return
    $ msg("editore", "There is only ever one, and everyone has used it. Try a noun. M.")
    label tel_chat_editore_d1_1_2:
    if telefono_minuti_blocco("tel_chat_editore_d1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Warmth.»":
            label tel_chat_editore_d1_1_3:
            if telefono_minuti_blocco("tel_chat_editore_d1_1_3", "invia", 1):
                return
            $ msg("sara", "Warmth.")
            $ caldo()
            label tel_chat_editore_d1_1_4:
            if telefono_minuti_blocco("tel_chat_editore_d1_1_4", "ricevi", 1):
                return
            $ msg("editore", "Good. Go on. Do not explain it. M.")
        "«Silk. The sleeve of your jacket.»":
            label tel_chat_editore_d1_1_5:
            if telefono_minuti_blocco("tel_chat_editore_d1_1_5", "invia", 1):
                return
            $ msg("sara", "Silk. The sleeve of your jacket.")
            label tel_chat_editore_d1_1_6:
            if telefono_minuti_blocco("tel_chat_editore_d1_1_6", "ricevi", 1):
                return
            $ msg("editore", "It is a very old jacket. It has not been spoken of so kindly in years. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_d1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_d1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_d1_2:
    label tel_chat_editore_d1_2_1:
    if telefono_minuti_blocco("tel_chat_editore_d1_2_1", "ricevi", 1):
        return
    $ msg("editore", "I shall set you an exercise. Describe only what you can hear. I shall do the same, from here.")
    label tel_chat_editore_d1_2_2:
    if telefono_minuti_blocco("tel_chat_editore_d1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«My own breath. The sheet. The clock, too slow.»":
            label tel_chat_editore_d1_2_3:
            if telefono_minuti_blocco("tel_chat_editore_d1_2_3", "invia", 1):
                return
            $ msg("sara", "My own breath. The sheet. The clock, too slow.")
            $ caldo()
            label tel_chat_editore_d1_2_4:
            if telefono_minuti_blocco("tel_chat_editore_d1_2_4", "ricevi", 1):
                return
            $ msg("editore", "A fire going down. A page I have not turned for twenty minutes. My heart, which is being rather vulgar. M.")
        "«You, reading. In that very proper voice.»":
            label tel_chat_editore_d1_2_5:
            if telefono_minuti_blocco("tel_chat_editore_d1_2_5", "invia", 1):
                return
            $ msg("sara", "You, reading. In that very proper voice.")
            label tel_chat_editore_d1_2_6:
            if telefono_minuti_blocco("tel_chat_editore_d1_2_6", "ricevi", 1):
                return
            $ msg("editore", "Then lie still, and I shall read. It is not a long passage, but I take my time. M.")
        "«I'd rather you described me.»":
            label tel_chat_editore_d1_2_7:
            if telefono_minuti_blocco("tel_chat_editore_d1_2_7", "invia", 1):
                return
            $ msg("sara", "I'd rather you described me.")
            label tel_chat_editore_d1_2_8:
            if telefono_minuti_blocco("tel_chat_editore_d1_2_8", "ricevi", 1):
                return
            $ msg("editore", "From memory, then. The light was on your left. I began at the collar. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_d1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_d1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_d1_3:
    label tel_chat_editore_d1_3_1:
    if telefono_minuti_blocco("tel_chat_editore_d1_3_1", "ricevi", 1):
        return
    $ msg("editore", "You have stopped writing. I shall assume that the exercise is going well.")
    label tel_chat_editore_d1_3_2:
    if telefono_minuti_blocco("tel_chat_editore_d1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I lost the pencil.»":
            label tel_chat_editore_d1_3_3:
            if telefono_minuti_blocco("tel_chat_editore_d1_3_3", "invia", 1):
                return
            $ msg("sara", "I lost the pencil.")
            label tel_chat_editore_d1_3_4:
            if telefono_minuti_blocco("tel_chat_editore_d1_3_4", "ricevi", 1):
                return
            $ msg("editore", "They roll. Leave it where it is. M.")
        "«I'm still listening.»":
            label tel_chat_editore_d1_3_5:
            if telefono_minuti_blocco("tel_chat_editore_d1_3_5", "invia", 1):
                return
            $ msg("sara", "I'm still listening.")
            label tel_chat_editore_d1_3_6:
            if telefono_minuti_blocco("tel_chat_editore_d1_3_6", "ricevi", 1):
                return
            $ msg("editore", "And I am still reading. Good night, my dear. Do not revise a word of it. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_d1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_d1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: desiderio e anni

label chat_editore_d2:
    label tel_chat_editore_d2_1:
    if telefono_minuti_blocco("tel_chat_editore_d2_1", "invia", 1):
        return
    $ msg("sara", "Does it bother you? The years between us?")
    return

label chat_editore_d2_1:
    label tel_chat_editore_d2_1_1:
    if telefono_minuti_blocco("tel_chat_editore_d2_1_1", "ricevi", 1):
        return
    $ msg("editore", "They do not bother me. I was there for all of them. Do they bother you? M.")
    label tel_chat_editore_d2_1_2:
    if telefono_minuti_blocco("tel_chat_editore_d2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«No. It's the patience I can't get over.»":
            label tel_chat_editore_d2_1_3:
            if telefono_minuti_blocco("tel_chat_editore_d2_1_3", "invia", 1):
                return
            $ msg("sara", "No. It's the patience I can't get over.")
            $ caldo()
            label tel_chat_editore_d2_1_4:
            if telefono_minuti_blocco("tel_chat_editore_d2_1_4", "ricevi", 1):
                return
            $ msg("editore", "It is not patience. It is knowing what one is waiting for. M.")
        "«Only on stairs.»":
            label tel_chat_editore_d2_1_5:
            if telefono_minuti_blocco("tel_chat_editore_d2_1_5", "invia", 1):
                return
            $ msg("sara", "Only on stairs.")
            label tel_chat_editore_d2_1_6:
            if telefono_minuti_blocco("tel_chat_editore_d2_1_6", "ricevi", 1):
                return
            $ msg("editore", "Wretched girl. I shall have a lift put in. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_d2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_d2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_d2_2:
    label tel_chat_editore_d2_2_1:
    if telefono_minuti_blocco("tel_chat_editore_d2_2_1", "ricevi", 1):
        return
    $ msg("editore", "A young man wants to arrive. I have arrived nearly everywhere. I find I should like to look out of the window on the way.")
    label tel_chat_editore_d2_2_2:
    if telefono_minuti_blocco("tel_chat_editore_d2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What can you see?»":
            label tel_chat_editore_d2_2_3:
            if telefono_minuti_blocco("tel_chat_editore_d2_2_3", "invia", 1):
                return
            $ msg("sara", "What can you see?")
            $ caldo()
            label tel_chat_editore_d2_2_4:
            if telefono_minuti_blocco("tel_chat_editore_d2_2_4", "ricevi", 1):
                return
            $ msg("editore", "A shoulder. A strap that has given up. You, pretending that you have not noticed. M.")
        "«Then take the long road.»":
            label tel_chat_editore_d2_2_5:
            if telefono_minuti_blocco("tel_chat_editore_d2_2_5", "invia", 1):
                return
            $ msg("sara", "Then take the long road.")
            label tel_chat_editore_d2_2_6:
            if telefono_minuti_blocco("tel_chat_editore_d2_2_6", "ricevi", 1):
                return
            $ msg("editore", "I know of no other. Put out the lamp, and I shall begin with your wrist. M.")
        "«You make it sound like a train.»":
            label tel_chat_editore_d2_2_7:
            if telefono_minuti_blocco("tel_chat_editore_d2_2_7", "invia", 1):
                return
            $ msg("sara", "You make it sound like a train.")
            label tel_chat_editore_d2_2_8:
            if telefono_minuti_blocco("tel_chat_editore_d2_2_8", "ricevi", 1):
                return
            $ msg("editore", "The slow one, along the coast. One has the compartment to oneself. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_d2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_d2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_d2_3:
    label tel_chat_editore_d2_3_1:
    if telefono_minuti_blocco("tel_chat_editore_d2_3_1", "ricevi", 1):
        return
    $ msg("editore", "You ought to know that I expect nothing. It leaves one's hands free.")
    label tel_chat_editore_d2_3_2:
    if telefono_minuti_blocco("tel_chat_editore_d2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's the most indecent thing you've ever said.»":
            label tel_chat_editore_d2_3_3:
            if telefono_minuti_blocco("tel_chat_editore_d2_3_3", "invia", 1):
                return
            $ msg("sara", "That's the most indecent thing you've ever said.")
            label tel_chat_editore_d2_3_4:
            if telefono_minuti_blocco("tel_chat_editore_d2_3_4", "ricevi", 1):
                return
            $ msg("editore", "It was intended as a courtesy. The two are often confused. M.")
        "«Good. Because I expect a great deal.»":
            label tel_chat_editore_d2_3_5:
            if telefono_minuti_blocco("tel_chat_editore_d2_3_5", "invia", 1):
                return
            $ msg("sara", "Good. Because I expect a great deal.")
            label tel_chat_editore_d2_3_6:
            if telefono_minuti_blocco("tel_chat_editore_d2_3_6", "ricevi", 1):
                return
            $ msg("editore", "Then I shall try to live up to the edition. Good night. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_d2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_d2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Non ricambiato: una virgola

label chat_editore_n1:
    label tel_chat_editore_n1_1:
    if telefono_minuti_blocco("tel_chat_editore_n1_1", "invia", 1):
        return
    $ msg("sara", "Has anyone ever told you that you've got a beautiful voice?")
    return

label chat_editore_n1_1:
    label tel_chat_editore_n1_1_1:
    if telefono_minuti_blocco("tel_chat_editore_n1_1_1", "ricevi", 1):
        return
    $ msg("editore", "Several people, and one of them was a surgeon holding a knife. What would you like it to say? M.")
    label tel_chat_editore_n1_1_2:
    if telefono_minuti_blocco("tel_chat_editore_n1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Nothing. I just wanted to tell you.»":
            label tel_chat_editore_n1_1_3:
            if telefono_minuti_blocco("tel_chat_editore_n1_1_3", "invia", 1):
                return
            $ msg("sara", "Nothing. I just wanted to tell you.")
            $ caldo()
            label tel_chat_editore_n1_1_4:
            if telefono_minuti_blocco("tel_chat_editore_n1_1_4", "ricevi", 1):
                return
            $ msg("editore", "Then I have been told, and I shall carry it about all day, like a flower in a book. M.")
        "«Anything.»":
            label tel_chat_editore_n1_1_5:
            if telefono_minuti_blocco("tel_chat_editore_n1_1_5", "invia", 1):
                return
            $ msg("sara", "Anything.")
            label tel_chat_editore_n1_1_6:
            if telefono_minuti_blocco("tel_chat_editore_n1_1_6", "ricevi", 1):
                return
            $ msg("editore", "A dangerous commission. I decline it with regret. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_n1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_n1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_n1_2:
    label tel_chat_editore_n1_2_1:
    if telefono_minuti_blocco("tel_chat_editore_n1_2_1", "ricevi", 1):
        return
    $ msg("editore", "You are wondering whether I have understood. I have. I am merely in no hurry to be the one who did.")
    label tel_chat_editore_n1_2_2:
    if telefono_minuti_blocco("tel_chat_editore_n1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Is that a no?»":
            label tel_chat_editore_n1_2_3:
            if telefono_minuti_blocco("tel_chat_editore_n1_2_3", "invia", 1):
                return
            $ msg("sara", "Is that a no?")
            $ caldo()
            label tel_chat_editore_n1_2_4:
            if telefono_minuti_blocco("tel_chat_editore_n1_2_4", "ricevi", 1):
                return
            $ msg("editore", "It is a comma. M.")
        "«Now I'm embarrassed.»":
            label tel_chat_editore_n1_2_5:
            if telefono_minuti_blocco("tel_chat_editore_n1_2_5", "invia", 1):
                return
            $ msg("sara", "Now I'm embarrassed.")
            label tel_chat_editore_n1_2_6:
            if telefono_minuti_blocco("tel_chat_editore_n1_2_6", "ricevi", 1):
                return
            $ msg("editore", "Pray do not be. It is the nicest thing to have happened since the post. M.")
        "«I shouldn't have said it.»":
            label tel_chat_editore_n1_2_7:
            if telefono_minuti_blocco("tel_chat_editore_n1_2_7", "invia", 1):
                return
            $ msg("sara", "I shouldn't have said it.")
            label tel_chat_editore_n1_2_8:
            if telefono_minuti_blocco("tel_chat_editore_n1_2_8", "ricevi", 1):
                return
            $ msg("editore", "On the contrary. One should always have said it. What follows is another matter. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_n1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_n1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_n1_3:
    label tel_chat_editore_n1_3_1:
    if telefono_minuti_blocco("tel_chat_editore_n1_3_1", "ricevi", 1):
        return
    $ msg("editore", "I shall be exactly the same tomorrow. You will find that either restful or maddening.")
    label tel_chat_editore_n1_3_2:
    if telefono_minuti_blocco("tel_chat_editore_n1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Both, I think.»":
            label tel_chat_editore_n1_3_3:
            if telefono_minuti_blocco("tel_chat_editore_n1_3_3", "invia", 1):
                return
            $ msg("sara", "Both, I think.")
            label tel_chat_editore_n1_3_4:
            if telefono_minuti_blocco("tel_chat_editore_n1_3_4", "ricevi", 1):
                return
            $ msg("editore", "Then you are reading me correctly. Good night. M.")
        "«I'll get used to it.»":
            label tel_chat_editore_n1_3_5:
            if telefono_minuti_blocco("tel_chat_editore_n1_3_5", "invia", 1):
                return
            $ msg("sara", "I'll get used to it.")
            label tel_chat_editore_n1_3_6:
            if telefono_minuti_blocco("tel_chat_editore_n1_3_6", "ricevi", 1):
                return
            $ msg("editore", "I do hope not entirely. Good night. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_n1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_n1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Non ricambiato: camomilla

label chat_editore_n2:
    label tel_chat_editore_n2_1:
    if telefono_minuti_blocco("tel_chat_editore_n2_1", "invia", 1):
        return
    $ msg("sara", "If I told you what I was thinking, would you blush?")
    return

label chat_editore_n2_1:
    label tel_chat_editore_n2_1_1:
    if telefono_minuti_blocco("tel_chat_editore_n2_1_1", "ricevi", 1):
        return
    $ msg("editore", "I have not blushed in forty years, and that was the heat. You may try. M.")
    label tel_chat_editore_n2_1_2:
    if telefono_minuti_blocco("tel_chat_editore_n2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I was thinking about your hands, turning a page.»":
            label tel_chat_editore_n2_1_3:
            if telefono_minuti_blocco("tel_chat_editore_n2_1_3", "invia", 1):
                return
            $ msg("sara", "I was thinking about your hands, turning a page.")
            $ caldo()
            label tel_chat_editore_n2_1_4:
            if telefono_minuti_blocco("tel_chat_editore_n2_1_4", "ricevi", 1):
                return
            $ msg("editore", "They have been informed. They are pretending not to care. M.")
        "«Perhaps I'd better not.»":
            label tel_chat_editore_n2_1_5:
            if telefono_minuti_blocco("tel_chat_editore_n2_1_5", "invia", 1):
                return
            $ msg("sara", "Perhaps I'd better not.")
            label tel_chat_editore_n2_1_6:
            if telefono_minuti_blocco("tel_chat_editore_n2_1_6", "ricevi", 1):
                return
            $ msg("editore", "As you like. I enjoy a locked drawer almost as much. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_n2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_n2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_n2_2:
    label tel_chat_editore_n2_2_1:
    if telefono_minuti_blocco("tel_chat_editore_n2_2_1", "ricevi", 1):
        return
    $ msg("editore", "Tonight I am an old man with a cup of camomile. I should make you a poor accomplice.")
    label tel_chat_editore_n2_2_2:
    if telefono_minuti_blocco("tel_chat_editore_n2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I don't mind camomile.»":
            label tel_chat_editore_n2_2_3:
            if telefono_minuti_blocco("tel_chat_editore_n2_2_3", "invia", 1):
                return
            $ msg("sara", "I don't mind camomile.")
            $ caldo()
            label tel_chat_editore_n2_2_4:
            if telefono_minuti_blocco("tel_chat_editore_n2_2_4", "ricevi", 1):
                return
            $ msg("editore", "Then drink yours, and I shall drink mine, and we shall say nothing. You would be surprised what that does. M.")
        "«Another night, then.»":
            label tel_chat_editore_n2_2_5:
            if telefono_minuti_blocco("tel_chat_editore_n2_2_5", "invia", 1):
                return
            $ msg("sara", "Another night, then.")
            label tel_chat_editore_n2_2_6:
            if telefono_minuti_blocco("tel_chat_editore_n2_2_6", "ricevi", 1):
                return
            $ msg("editore", "The very words I should have chosen. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_n2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_n2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_editore_n2_3:
    label tel_chat_editore_n2_3_1:
    if telefono_minuti_blocco("tel_chat_editore_n2_3_1", "ricevi", 1):
        return
    $ msg("editore", "Keep the thought. Do not write it down yet. They improve when they have been slept on.")
    label tel_chat_editore_n2_3_2:
    if telefono_minuti_blocco("tel_chat_editore_n2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You always make me wait.»":
            label tel_chat_editore_n2_3_3:
            if telefono_minuti_blocco("tel_chat_editore_n2_3_3", "invia", 1):
                return
            $ msg("sara", "You always make me wait.")
            label tel_chat_editore_n2_3_4:
            if telefono_minuti_blocco("tel_chat_editore_n2_3_4", "ricevi", 1):
                return
            $ msg("editore", "I make everyone wait. You are the first to do it well. M.")
        "«Good night, Magnus.»":
            label tel_chat_editore_n2_3_5:
            if telefono_minuti_blocco("tel_chat_editore_n2_3_5", "invia", 1):
                return
            $ msg("sara", "Good night, Magnus.")
            label tel_chat_editore_n2_3_6:
            if telefono_minuti_blocco("tel_chat_editore_n2_3_6", "ricevi", 1):
                return
            $ msg("editore", "Good night, my dear. M.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_n2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_editore_n2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return
