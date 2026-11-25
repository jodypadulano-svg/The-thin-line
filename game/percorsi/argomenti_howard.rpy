## GENERATO da tools/telefono/componi.py: si modifica tools/telefono/howard.txt.

init python:
    discorso("howard_t1", "howard", CONOSCENTI, argomento="The sauce on the blouse", se="fatto('ep2_d18_cena_reggiseno')")


## --- The sauce on the blouse

label chat_howard_t1:
    label tel_chat_howard_t1_1:
    if telefono_minuti_blocco("tel_chat_howard_t1_1", "invia", 1):
        return
    $ msg("sara", "Howard. We need to talk about the blouse.")
    return

label chat_howard_t1_1:
    label tel_chat_howard_t1_1_1:
    if telefono_minuti_blocco("tel_chat_howard_t1_1_1", "ricevi", 3):
        return
    $ msg("howard", "Is it ruined?")
    $ msg("howard", "It's ruined. I knew it. I've thought of nothing else since you closed the door.")
    $ msg("howard", "I can get you another one. Same make. I saw the label.")
    sp "He saw the label?"
    label tel_chat_howard_t1_1_2:
    if telefono_minuti_blocco("tel_chat_howard_t1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It's not ruined. It's got a little pink cloud on it.»":
            label tel_chat_howard_t1_1_3:
            if telefono_minuti_blocco("tel_chat_howard_t1_1_3", "invia", 1):
                return
            $ msg("sara", "It's not ruined. It's got a little pink cloud on it.")
            $ caldo()
            label tel_chat_howard_t1_1_4:
            if telefono_minuti_blocco("tel_chat_howard_t1_1_4", "ricevi", 1):
                return
            $ msg("howard", "A pink cloud. Only you could be kind about a stain.")
        "«You don't have to buy me anything.»":
            label tel_chat_howard_t1_1_5:
            if telefono_minuti_blocco("tel_chat_howard_t1_1_5", "invia", 1):
                return
            $ msg("sara", "You don't have to buy me anything.")
            label tel_chat_howard_t1_1_6:
            if telefono_minuti_blocco("tel_chat_howard_t1_1_6", "ricevi", 1):
                return
            $ msg("howard", "No. Of course not. You're independent. I admire that.")
        "«You read the label on my blouse?»":
            label tel_chat_howard_t1_1_7:
            if telefono_minuti_blocco("tel_chat_howard_t1_1_7", "invia", 1):
                return
            $ msg("sara", "You read the label on my blouse?")
            label tel_chat_howard_t1_1_8:
            if telefono_minuti_blocco("tel_chat_howard_t1_1_8", "ricevi", 1):
                return
            $ msg("howard", "It was drying on my radiator, my dear. A man reads what's put in front of him.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t1_2:
    label tel_chat_howard_t1_2_1:
    if telefono_minuti_blocco("tel_chat_howard_t1_2_1", "ricevi", 2):
        return
    $ msg("howard", "My mother swore by white vinegar and cold water. Never hot. Hot is how you lose a blouse.")
    $ msg("howard", "Where's the mark, exactly? So I can advise.")
    label tel_chat_howard_t1_2_2:
    if telefono_minuti_blocco("tel_chat_howard_t1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Right in the middle. You've got very good aim.»":
            label tel_chat_howard_t1_2_3:
            if telefono_minuti_blocco("tel_chat_howard_t1_2_3", "invia", 1):
                return
            $ msg("sara", "Right in the middle. You've got very good aim.")
            $ caldo()
            label tel_chat_howard_t1_2_4:
            if telefono_minuti_blocco("tel_chat_howard_t1_2_4", "ricevi", 2):
                return
            $ msg("howard", "Aim! Ask anyone. Clumsiest man in the building.")
            $ msg("howard", "It was a lovely dinner, though. Even allowing for the blouse.")
        "«By the second button. You can hardly see it.»":
            label tel_chat_howard_t1_2_5:
            if telefono_minuti_blocco("tel_chat_howard_t1_2_5", "invia", 1):
                return
            $ msg("sara", "By the second button. You can hardly see it.")
            label tel_chat_howard_t1_2_6:
            if telefono_minuti_blocco("tel_chat_howard_t1_2_6", "ricevi", 1):
                return
            $ msg("howard", "The second button. Yes. I remember the second button.")
            sp "He's got such a good memory. Bless him."
        "«I'll try the vinegar. Thank you.»":
            label tel_chat_howard_t1_2_7:
            if telefono_minuti_blocco("tel_chat_howard_t1_2_7", "invia", 1):
                return
            $ msg("sara", "I'll try the vinegar. Thank you.")
            label tel_chat_howard_t1_2_8:
            if telefono_minuti_blocco("tel_chat_howard_t1_2_8", "ricevi", 1):
                return
            $ msg("howard", "Two spoons. Then tell me how it went. Any time. I'm up.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t1_3:
    label tel_chat_howard_t1_3_1:
    if telefono_minuti_blocco("tel_chat_howard_t1_3_1", "ricevi", 1):
        return
    $ msg("howard", "Can I say something without you being cross with me?")
    label tel_chat_howard_t1_3_2:
    if telefono_minuti_blocco("tel_chat_howard_t1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Depends what it is.»":
            label tel_chat_howard_t1_3_3:
            if telefono_minuti_blocco("tel_chat_howard_t1_3_3", "invia", 1):
                return
            $ msg("sara", "Depends what it is.")
            label tel_chat_howard_t1_3_4:
            if telefono_minuti_blocco("tel_chat_howard_t1_3_4", "ricevi", 2):
                return
            $ msg("howard", "Sensible. My mother would have liked you.")
            $ msg("howard", "You sat down at that table as if it were the most ordinary thing in the world. No fuss at all. I thought, there's a woman who feels at home.")
        "«Go on.»":
            label tel_chat_howard_t1_3_5:
            if telefono_minuti_blocco("tel_chat_howard_t1_3_5", "invia", 1):
                return
            $ msg("sara", "Go on.")
            $ caldo()
            label tel_chat_howard_t1_3_6:
            if telefono_minuti_blocco("tel_chat_howard_t1_3_6", "ricevi", 2):
                return
            $ msg("howard", "I'd forgotten what it's like, hearing someone laugh with her mouth full in that kitchen.")
            $ msg("howard", "I left your chair where it was.")
        "«You were staring, Howard.»":
            label tel_chat_howard_t1_3_7:
            if telefono_minuti_blocco("tel_chat_howard_t1_3_7", "invia", 1):
                return
            $ msg("sara", "You were staring, Howard.")
            label tel_chat_howard_t1_3_8:
            if telefono_minuti_blocco("tel_chat_howard_t1_3_8", "ricevi", 1):
                return
            $ msg("howard", "I was. I said so at the time. I'd sooner be honest than polite.")
            sp "You can't even be angry with him. He's like a child at a shop window."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t1_4:
    label tel_chat_howard_t1_4_1:
    if telefono_minuti_blocco("tel_chat_howard_t1_4_1", "ricevi", 1):
        return
    $ msg("howard", "Did [nome_compagno] say anything? About the mark, I mean.")
    label tel_chat_howard_t1_4_2:
    if telefono_minuti_blocco("tel_chat_howard_t1_4_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«He didn't notice the blouse at all.»":
            label tel_chat_howard_t1_4_3:
            if telefono_minuti_blocco("tel_chat_howard_t1_4_3", "invia", 1):
                return
            $ msg("sara", "He didn't notice the blouse at all.")
            $ caldo()
            label tel_chat_howard_t1_4_4:
            if telefono_minuti_blocco("tel_chat_howard_t1_4_4", "ricevi", 1):
                return
            $ msg("howard", "No. Well. You stop looking at the good china when you eat off it every day.")
        "«I told him it was sauce. It was sauce.»":
            label tel_chat_howard_t1_4_5:
            if telefono_minuti_blocco("tel_chat_howard_t1_4_5", "invia", 1):
                return
            $ msg("sara", "I told him it was sauce. It was sauce.")
            label tel_chat_howard_t1_4_6:
            if telefono_minuti_blocco("tel_chat_howard_t1_4_6", "ricevi", 1):
                return
            $ msg("howard", "It was sauce. I always say, if the truth's that small, you might as well tell it.")
        "«He loved the jar.»":
            label tel_chat_howard_t1_4_7:
            if telefono_minuti_blocco("tel_chat_howard_t1_4_7", "invia", 1):
                return
            $ msg("sara", "He loved the jar.")
            label tel_chat_howard_t1_4_8:
            if telefono_minuti_blocco("tel_chat_howard_t1_4_8", "ricevi", 1):
                return
            $ msg("howard", "Did he? Good lad. There's another one with his name on it. You'd have to come and collect it, of course.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t1_4_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t1_4_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t1_5:
    label tel_chat_howard_t1_5_1:
    if telefono_minuti_blocco("tel_chat_howard_t1_5_1", "ricevi", 1):
        return
    $ msg("howard", "I'll be making it again. I thought I'd hold the ladle with both hands this time.")
    label tel_chat_howard_t1_5_2:
    if telefono_minuti_blocco("tel_chat_howard_t1_5_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'll bring an apron.»":
            label tel_chat_howard_t1_5_3:
            if telefono_minuti_blocco("tel_chat_howard_t1_5_3", "invia", 1):
                return
            $ msg("sara", "I'll bring an apron.")
            $ caldo()
            label tel_chat_howard_t1_5_4:
            if telefono_minuti_blocco("tel_chat_howard_t1_5_4", "ricevi", 2):
                return
            $ msg("howard", "You bring whatever you like. Or don't bring anything. It's only next door.")
            $ msg("howard", "Sleep well, Sara. I'll hear you put the light out.")
            sp "The walls really are thin."
        "«We'll see, Howard.»":
            label tel_chat_howard_t1_5_5:
            if telefono_minuti_blocco("tel_chat_howard_t1_5_5", "invia", 1):
                return
            $ msg("sara", "We'll see, Howard.")
            label tel_chat_howard_t1_5_6:
            if telefono_minuti_blocco("tel_chat_howard_t1_5_6", "ricevi", 2):
                return
            $ msg("howard", "«We'll see» isn't no. I'll keep the good chair free.")
            $ msg("howard", "Goodnight, Sara.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t1_5_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t1_5_2"
            $ telefono_minuti_chiudi = True
            return
    return
