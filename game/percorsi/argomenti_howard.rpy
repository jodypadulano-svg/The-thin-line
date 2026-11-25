## GENERATO da tools/telefono/componi.py: si modifica tools/telefono/howard.txt.

init python:
    discorso("howard_t1", "howard", CONOSCENTI, argomento="The sauce on the blouse", se="fatto('ep2_d18_cena_reggiseno')")
    discorso("howard_t2", "howard", CONOSCENTI, argomento="Tidying your flat", se="fatto('ep1_d9_aiuto_pulire')")
    discorso("howard_t3", "howard", CONOSCENTI, argomento="What you said about my keys", se="fatto('ep1_d11_capisce_howard')")
    discorso("howard_t4", "howard", CONOSCENTI, argomento="Three copies of the paper", se="fatto('ep1_d12_visita') or fatto('ep1_d12_rifiuta_invito')")
    discorso("howard_t5", "howard", CONOSCENTI, argomento="The light bulb", se="fatto('ep1_d12_scaletta')")
    discorso("howard_t6", "howard", CONOSCENTI, argomento="The pink slippers", se="fatto('ep1_d12_scaletta') and fatto('ep1_d11_pantofole')")
    discorso("howard_t7", "howard", CONOSCENTI, argomento="That second coffee", se="fatto('ep1_d11_bottoni')")
    discorso("howard_t8", "howard", CONOSCENTI, argomento="The mother in my book", se="giorno in (18, 19) and fatto('ep2_d18_visita_howard') and howard_visite == 2")
    discorso("howard_t9", "howard", CONOSCENTI, argomento="The bathroom bulb", se="giorno in (18, 19) and fatto('ep2_d18_visita_howard') and howard_visite == 3")
    discorso("howard_t10", "howard", CONOSCENTI, argomento="The jar of ragù", se="fatto('ep2_d18_visita_howard') and howard_visite >= 4 and not fatto('ep2_d18_cena_reggiseno')")
    discorso("howard_t11", "howard", CONOSCENTI, argomento="Saying no on the landing", se="fatto('ep2_d18_rifiuta_howard')")
    discorso("howard_t12", "howard", CONOSCENTI, argomento="The parcel you weighed", se="fatto('ep2_d17_ritiro_howard')")
    discorso("howard_t13", "howard", CONFIDENZA, argomento="The housework", se="sara_cameriera")
    discorso("howard_c1", "howard", COMPLICI, flirt=True)
    discorso("howard_c2", "howard", COMPLICI, flirt=True)
    discorso("howard_c3", "howard", COMPLICI, flirt=True)
    discorso("howard_d1", "howard", INTIMI, flirt=True)
    discorso("howard_d2", "howard", INTIMI, flirt=True)


## --- The sauce on the blouse

label chat_howard_t1:
    label tel_chat_howard_t1_1:
    if telefono_minuti_blocco("tel_chat_howard_t1_1", "invia", 1):
        return
    $ msg("sara", "Howard. We need to talk about the blouse.")
    return

label chat_howard_t1_entrata:
    label tel_chat_howard_t1_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_t1_entrata_1", "ricevi", 2):
        return
    $ msg("howard", "Sara. I've been meaning to ask.")
    $ msg("howard", "The blouse. How is it?")
    label tel_chat_howard_t1_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_t1_entrata_2", "invia", 1):
        return
    $ msg("sara", "It's had an eventful evening, Howard.")
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


## --- Tidying your flat

label chat_howard_t2:
    label tel_chat_howard_t2_1:
    if telefono_minuti_blocco("tel_chat_howard_t2_1", "invia", 1):
        return
    $ msg("sara", "I haven't forgotten, you know. I said I'd help you with the flat.")
    return

label chat_howard_t2_entrata:
    label tel_chat_howard_t2_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_t2_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "I bought something today. I'll say no more.")
    label tel_chat_howard_t2_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_t2_entrata_2", "invia", 1):
        return
    $ msg("sara", "Is this about tidying the flat? I haven't forgotten.")
    return

label chat_howard_t2_1:
    label tel_chat_howard_t2_1_1:
    if telefono_minuti_blocco("tel_chat_howard_t2_1_1", "ricevi", 3):
        return
    $ msg("howard", "You remembered!")
    $ msg("howard", "I didn't want to bring it up. I've been not bringing it up ever since.")
    $ msg("howard", "I bought two pairs of rubber gloves. One's small.")
    label tel_chat_howard_t2_1_2:
    if telefono_minuti_blocco("tel_chat_howard_t2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You bought me gloves?»":
            label tel_chat_howard_t2_1_3:
            if telefono_minuti_blocco("tel_chat_howard_t2_1_3", "invia", 1):
                return
            $ msg("sara", "You bought me gloves?")
            $ caldo()
            label tel_chat_howard_t2_1_4:
            if telefono_minuti_blocco("tel_chat_howard_t2_1_4", "ricevi", 1):
                return
            $ msg("howard", "Yellow ones. The lady at the shop asked who they were for. I said a friend.")
        "«Two hours, Howard. That's what I promised.»":
            label tel_chat_howard_t2_1_5:
            if telefono_minuti_blocco("tel_chat_howard_t2_1_5", "invia", 1):
                return
            $ msg("sara", "Two hours, Howard. That's what I promised.")
            label tel_chat_howard_t2_1_6:
            if telefono_minuti_blocco("tel_chat_howard_t2_1_6", "ricevi", 1):
                return
            $ msg("howard", "Two hours. I've written it down so I won't be greedy.")
        "«We could get someone in to do it.»":
            label tel_chat_howard_t2_1_7:
            if telefono_minuti_blocco("tel_chat_howard_t2_1_7", "invia", 1):
                return
            $ msg("sara", "We could get someone in to do it.")
            label tel_chat_howard_t2_1_8:
            if telefono_minuti_blocco("tel_chat_howard_t2_1_8", "ricevi", 1):
                return
            $ msg("howard", "A stranger? Going through Mother's things? Oh no. I'd sooner leave it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t2_2:
    label tel_chat_howard_t2_2_1:
    if telefono_minuti_blocco("tel_chat_howard_t2_2_1", "ricevi", 2):
        return
    $ msg("howard", "I've made a start, so you won't be shocked. The newspapers are tied up with string.")
    $ msg("howard", "I found one from the week I moved in. There was a picture of this street. It had more trees.")
    label tel_chat_howard_t2_2_2:
    if telefono_minuti_blocco("tel_chat_howard_t2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Keep that one.»":
            label tel_chat_howard_t2_2_3:
            if telefono_minuti_blocco("tel_chat_howard_t2_2_3", "invia", 1):
                return
            $ msg("sara", "Keep that one.")
            $ caldo()
            label tel_chat_howard_t2_2_4:
            if telefono_minuti_blocco("tel_chat_howard_t2_2_4", "ricevi", 1):
                return
            $ msg("howard", "I kept it. It's on the kitchen table, under the good lamp. You can see it when you come.")
        "«How many are there altogether?»":
            label tel_chat_howard_t2_2_5:
            if telefono_minuti_blocco("tel_chat_howard_t2_2_5", "invia", 1):
                return
            $ msg("sara", "How many are there altogether?")
            label tel_chat_howard_t2_2_6:
            if telefono_minuti_blocco("tel_chat_howard_t2_2_6", "ricevi", 1):
                return
            $ msg("howard", "I stopped counting at four hundred. It sounds worse than it is. The recent ones are thin.")
            sp "Four hundred."
        "«Just bin the lot, Howard.»":
            label tel_chat_howard_t2_2_7:
            if telefono_minuti_blocco("tel_chat_howard_t2_2_7", "invia", 1):
                return
            $ msg("sara", "Just bin the lot, Howard.")
            label tel_chat_howard_t2_2_8:
            if telefono_minuti_blocco("tel_chat_howard_t2_2_8", "ricevi", 1):
                return
            $ msg("howard", "You're right. You're right. I'll do it as soon as there's somebody here to make me.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t2_3:
    label tel_chat_howard_t2_3_1:
    if telefono_minuti_blocco("tel_chat_howard_t2_3_1", "ricevi", 1):
        return
    $ msg("howard", "When would suit you? He's late on Thursdays, isn't he? Your [nome_compagno].")
    sp "How does he... well, everyone knows that. He's always late."
    label tel_chat_howard_t2_3_2:
    if telefono_minuti_blocco("tel_chat_howard_t2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«One evening after work, maybe.»":
            label tel_chat_howard_t2_3_3:
            if telefono_minuti_blocco("tel_chat_howard_t2_3_3", "invia", 1):
                return
            $ msg("sara", "One evening after work, maybe.")
            label tel_chat_howard_t2_3_4:
            if telefono_minuti_blocco("tel_chat_howard_t2_3_4", "ricevi", 1):
                return
            $ msg("howard", "An evening. I'm in all of them. You just choose which one.")
        "«Some weekend. [nome_compagno] can help too.»":
            label tel_chat_howard_t2_3_5:
            if telefono_minuti_blocco("tel_chat_howard_t2_3_5", "invia", 1):
                return
            $ msg("sara", "Some weekend. [nome_compagno] can help too.")
            label tel_chat_howard_t2_3_6:
            if telefono_minuti_blocco("tel_chat_howard_t2_3_6", "ricevi", 2):
                return
            $ msg("howard", "The three of us. Yes. Of course. I'll get another pair of gloves.")
            $ msg("howard", "Big ones.")
        "«Let me look at my week.»":
            label tel_chat_howard_t2_3_7:
            if telefono_minuti_blocco("tel_chat_howard_t2_3_7", "invia", 1):
                return
            $ msg("sara", "Let me look at my week.")
            label tel_chat_howard_t2_3_8:
            if telefono_minuti_blocco("tel_chat_howard_t2_3_8", "ricevi", 1):
                return
            $ msg("howard", "You look. The dust isn't going anywhere.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t2_4:
    label tel_chat_howard_t2_4_1:
    if telefono_minuti_blocco("tel_chat_howard_t2_4_1", "ricevi", 1):
        return
    $ msg("howard", "Thank you for remembering. People say things like that and then they don't.")
    label tel_chat_howard_t2_4_2:
    if telefono_minuti_blocco("tel_chat_howard_t2_4_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm not people. I'm next door.»":
            label tel_chat_howard_t2_4_3:
            if telefono_minuti_blocco("tel_chat_howard_t2_4_3", "invia", 1):
                return
            $ msg("sara", "I'm not people. I'm next door.")
            label tel_chat_howard_t2_4_4:
            if telefono_minuti_blocco("tel_chat_howard_t2_4_4", "ricevi", 1):
                return
            $ msg("howard", "You are. I sometimes put my hand on the wall, just to be sure it's still there.")
            sp "That's... lonely. God, that's lonely."
        "«Goodnight, Howard.»":
            label tel_chat_howard_t2_4_5:
            if telefono_minuti_blocco("tel_chat_howard_t2_4_5", "invia", 1):
                return
            $ msg("sara", "Goodnight, Howard.")
            label tel_chat_howard_t2_4_6:
            if telefono_minuti_blocco("tel_chat_howard_t2_4_6", "ricevi", 1):
                return
            $ msg("howard", "Goodnight, Sara. I'll leave the gloves by the sink.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t2_4_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t2_4_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- What you said about my keys

label chat_howard_t3:
    label tel_chat_howard_t3_1:
    if telefono_minuti_blocco("tel_chat_howard_t3_1", "invia", 1):
        return
    $ msg("sara", "That joke you made on the landing, Howard. When I hugged you.")
    return

label chat_howard_t3_1:
    label tel_chat_howard_t3_1_1:
    if telefono_minuti_blocco("tel_chat_howard_t3_1_1", "ricevi", 3):
        return
    $ msg("howard", "Oh dear.")
    $ msg("howard", "I've been waiting to hear about that one.")
    $ msg("howard", "Was it too much? I don't get the practice. You say a thing and then it's out.")
    label tel_chat_howard_t3_1_2:
    if telefono_minuti_blocco("tel_chat_howard_t3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It made me laugh. You know it did.»":
            label tel_chat_howard_t3_1_3:
            if telefono_minuti_blocco("tel_chat_howard_t3_1_3", "invia", 1):
                return
            $ msg("sara", "It made me laugh. You know it did.")
            $ caldo()
            label tel_chat_howard_t3_1_4:
            if telefono_minuti_blocco("tel_chat_howard_t3_1_4", "ricevi", 1):
                return
            $ msg("howard", "I did hear a laugh. I thought I might have imagined it. I've played it back a few times, to be sure.")
        "«It was a bit much, yes.»":
            label tel_chat_howard_t3_1_5:
            if telefono_minuti_blocco("tel_chat_howard_t3_1_5", "invia", 1):
                return
            $ msg("sara", "It was a bit much, yes.")
            label tel_chat_howard_t3_1_6:
            if telefono_minuti_blocco("tel_chat_howard_t3_1_6", "ricevi", 1):
                return
            $ msg("howard", "I thought so. I said to the kettle, Howard, that was a bit much. The kettle agreed.")
        "«I'd just like to know if you meant it.»":
            label tel_chat_howard_t3_1_7:
            if telefono_minuti_blocco("tel_chat_howard_t3_1_7", "invia", 1):
                return
            $ msg("sara", "I'd just like to know if you meant it.")
            label tel_chat_howard_t3_1_8:
            if telefono_minuti_blocco("tel_chat_howard_t3_1_8", "ricevi", 1):
                return
            $ msg("howard", "At my age you mean everything. There isn't time for the other thing.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t3_2:
    label tel_chat_howard_t3_2_1:
    if telefono_minuti_blocco("tel_chat_howard_t3_2_1", "ricevi", 1):
        return
    $ msg("howard", "May I say how it felt from this side? Or is that a bit much as well?")
    label tel_chat_howard_t3_2_2:
    if telefono_minuti_blocco("tel_chat_howard_t3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Say it.»":
            label tel_chat_howard_t3_2_3:
            if telefono_minuti_blocco("tel_chat_howard_t3_2_3", "invia", 1):
                return
            $ msg("sara", "Say it.")
            label tel_chat_howard_t3_2_4:
            if telefono_minuti_blocco("tel_chat_howard_t3_2_4", "ricevi", 2):
                return
            $ msg("howard", "It's a long while since anybody put their arms round me when I wasn't being helped up off something.")
            $ msg("howard", "I wasn't in a hurry for it to stop. That's all. That's the whole crime.")
        "«Briefly.»":
            label tel_chat_howard_t3_2_5:
            if telefono_minuti_blocco("tel_chat_howard_t3_2_5", "invia", 1):
                return
            $ msg("sara", "Briefly.")
            $ caldo()
            label tel_chat_howard_t3_2_6:
            if telefono_minuti_blocco("tel_chat_howard_t3_2_6", "ricevi", 2):
                return
            $ msg("howard", "Warm.")
            $ msg("howard", "That was brief, wasn't it?")
        "«Perhaps tell that one to the kettle.»":
            label tel_chat_howard_t3_2_7:
            if telefono_minuti_blocco("tel_chat_howard_t3_2_7", "invia", 1):
                return
            $ msg("sara", "Perhaps tell that one to the kettle.")
            label tel_chat_howard_t3_2_8:
            if telefono_minuti_blocco("tel_chat_howard_t3_2_8", "ricevi", 1):
                return
            $ msg("howard", "I'll put it back on the shelf, then.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t3_3:
    label tel_chat_howard_t3_3_1:
    if telefono_minuti_blocco("tel_chat_howard_t3_3_1", "ricevi", 1):
        return
    $ msg("howard", "If you lose anything else, I'm told I've got a good eye.")
    label tel_chat_howard_t3_3_2:
    if telefono_minuti_blocco("tel_chat_howard_t3_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«From now on I'm keeping them on a string.»":
            label tel_chat_howard_t3_3_3:
            if telefono_minuti_blocco("tel_chat_howard_t3_3_3", "invia", 1):
                return
            $ msg("sara", "From now on I'm keeping them on a string.")
            label tel_chat_howard_t3_3_4:
            if telefono_minuti_blocco("tel_chat_howard_t3_3_4", "ricevi", 1):
                return
            $ msg("howard", "Round your neck? Then I'd always know where to look.")
            sp "Howard!"
        "«I'm not losing anything else.»":
            label tel_chat_howard_t3_3_5:
            if telefono_minuti_blocco("tel_chat_howard_t3_3_5", "invia", 1):
                return
            $ msg("sara", "I'm not losing anything else.")
            label tel_chat_howard_t3_3_6:
            if telefono_minuti_blocco("tel_chat_howard_t3_3_6", "ricevi", 1):
                return
            $ msg("howard", "No. That's a pity for me and very sensible of you.")
        "«You'd only want paying.»":
            label tel_chat_howard_t3_3_7:
            if telefono_minuti_blocco("tel_chat_howard_t3_3_7", "invia", 1):
                return
            $ msg("sara", "You'd only want paying.")
            label tel_chat_howard_t3_3_8:
            if telefono_minuti_blocco("tel_chat_howard_t3_3_8", "ricevi", 1):
                return
            $ msg("howard", "I've never sent a bill in my life. I take whatever people leave.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t3_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t3_3_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t3_4:
    label tel_chat_howard_t3_4_1:
    if telefono_minuti_blocco("tel_chat_howard_t3_4_1", "ricevi", 1):
        return
    $ msg("howard", "You're not cross, then. I'll sleep tonight.")
    label tel_chat_howard_t3_4_2:
    if telefono_minuti_blocco("tel_chat_howard_t3_4_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm not cross.»":
            label tel_chat_howard_t3_4_3:
            if telefono_minuti_blocco("tel_chat_howard_t3_4_3", "invia", 1):
                return
            $ msg("sara", "I'm not cross.")
            label tel_chat_howard_t3_4_4:
            if telefono_minuti_blocco("tel_chat_howard_t3_4_4", "ricevi", 1):
                return
            $ msg("howard", "I can hear that you're not. Even written down.")
        "«Just mind your manners.»":
            label tel_chat_howard_t3_4_5:
            if telefono_minuti_blocco("tel_chat_howard_t3_4_5", "invia", 1):
                return
            $ msg("sara", "Just mind your manners.")
            label tel_chat_howard_t3_4_6:
            if telefono_minuti_blocco("tel_chat_howard_t3_4_6", "ricevi", 2):
                return
            $ msg("howard", "I'll mind them. They've been sitting about doing nothing for years.")
            $ msg("howard", "Goodnight, my dear.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t3_4_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t3_4_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Three copies of the paper

label chat_howard_t4:
    label tel_chat_howard_t4_1:
    if telefono_minuti_blocco("tel_chat_howard_t4_1", "invia", 1):
        return
    $ msg("sara", "Did you really buy three copies of the paper?")
    return

label chat_howard_t4_entrata:
    label tel_chat_howard_t4_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_t4_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "There's a parcel come for you. Well. For me. But it's you that's in it.")
    label tel_chat_howard_t4_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_t4_entrata_2", "invia", 1):
        return
    $ msg("sara", "Howard, is this about the newspaper?")
    return

label chat_howard_t4_1:
    label tel_chat_howard_t4_1_1:
    if telefono_minuti_blocco("tel_chat_howard_t4_1_1", "ricevi", 2):
        return
    $ msg("howard", "The newsagent still looks at me.")
    $ msg("howard", "The frame came, by the way. It's oak. A bit big, so there's a nice margin all round you.")
    label tel_chat_howard_t4_1_2:
    if telefono_minuti_blocco("tel_chat_howard_t4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You framed it!»":
            label tel_chat_howard_t4_1_3:
            if telefono_minuti_blocco("tel_chat_howard_t4_1_3", "invia", 1):
                return
            $ msg("sara", "You framed it!")
            $ caldo()
            label tel_chat_howard_t4_1_4:
            if telefono_minuti_blocco("tel_chat_howard_t4_1_4", "ricevi", 1):
                return
            $ msg("howard", "It's in the hall, where the light's good. You see it as you come in.")
        "«Round my article, you mean.»":
            label tel_chat_howard_t4_1_5:
            if telefono_minuti_blocco("tel_chat_howard_t4_1_5", "invia", 1):
                return
            $ msg("sara", "Round my article, you mean.")
            label tel_chat_howard_t4_1_6:
            if telefono_minuti_blocco("tel_chat_howard_t4_1_6", "ricevi", 1):
                return
            $ msg("howard", "Round your article. What did I say?")
        "«You're making me shy.»":
            label tel_chat_howard_t4_1_7:
            if telefono_minuti_blocco("tel_chat_howard_t4_1_7", "invia", 1):
                return
            $ msg("sara", "You're making me shy.")
            label tel_chat_howard_t4_1_8:
            if telefono_minuti_blocco("tel_chat_howard_t4_1_8", "ricevi", 1):
                return
            $ msg("howard", "Good. It suits you. Some people go blotchy.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t4_2:
    label tel_chat_howard_t4_2_1:
    if telefono_minuti_blocco("tel_chat_howard_t4_2_1", "ricevi", 2):
        return
    $ msg("howard", "I've got a question about it, if you don't mind one from a reader.")
    $ msg("howard", "The people nobody notices. How do you know what they're thinking?")
    label tel_chat_howard_t4_2_2:
    if telefono_minuti_blocco("tel_chat_howard_t4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I look at them for a long time.»":
            label tel_chat_howard_t4_2_3:
            if telefono_minuti_blocco("tel_chat_howard_t4_2_3", "invia", 1):
                return
            $ msg("sara", "I look at them for a long time.")
            $ caldo()
            label tel_chat_howard_t4_2_4:
            if telefono_minuti_blocco("tel_chat_howard_t4_2_4", "ricevi", 2):
                return
            $ msg("howard", "I do that. I thought it was only me.")
            $ msg("howard", "It's a great comfort to find out it's a profession.")
        "«I make it up.»":
            label tel_chat_howard_t4_2_5:
            if telefono_minuti_blocco("tel_chat_howard_t4_2_5", "invia", 1):
                return
            $ msg("sara", "I make it up.")
            label tel_chat_howard_t4_2_6:
            if telefono_minuti_blocco("tel_chat_howard_t4_2_6", "ricevi", 1):
                return
            $ msg("howard", "Then you make it up very close to the truth. Closer than most people would like.")
        "«I ask them.»":
            label tel_chat_howard_t4_2_7:
            if telefono_minuti_blocco("tel_chat_howard_t4_2_7", "invia", 1):
                return
            $ msg("sara", "I ask them.")
            label tel_chat_howard_t4_2_8:
            if telefono_minuti_blocco("tel_chat_howard_t4_2_8", "ricevi", 1):
                return
            $ msg("howard", "You ask! I never thought of asking. I generally just wait.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t4_3:
    label tel_chat_howard_t4_3_1:
    if telefono_minuti_blocco("tel_chat_howard_t4_3_1", "ricevi", 1):
        return
    $ msg("howard", "I tried it the other day, from the window. Looking at people your way.")
    label tel_chat_howard_t4_3_2:
    if telefono_minuti_blocco("tel_chat_howard_t4_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And what did you see?»":
            label tel_chat_howard_t4_3_3:
            if telefono_minuti_blocco("tel_chat_howard_t4_3_3", "invia", 1):
                return
            $ msg("sara", "And what did you see?")
            label tel_chat_howard_t4_3_4:
            if telefono_minuti_blocco("tel_chat_howard_t4_3_4", "ricevi", 1):
                return
            $ msg("howard", "A man in a grey coat who checks his pocket every ten steps. I think it's a letter. I think he hasn't opened it.")
            sp "That's good. That's really good, actually."
        "«Careful, or I'll steal it.»":
            label tel_chat_howard_t4_3_5:
            if telefono_minuti_blocco("tel_chat_howard_t4_3_5", "invia", 1):
                return
            $ msg("sara", "Careful, or I'll steal it.")
            label tel_chat_howard_t4_3_6:
            if telefono_minuti_blocco("tel_chat_howard_t4_3_6", "ricevi", 1):
                return
            $ msg("howard", "Steal it. I'd like to be in there somewhere, even as a coat.")
        "«People might not like being watched.»":
            label tel_chat_howard_t4_3_7:
            if telefono_minuti_blocco("tel_chat_howard_t4_3_7", "invia", 1):
                return
            $ msg("sara", "People might not like being watched.")
            label tel_chat_howard_t4_3_8:
            if telefono_minuti_blocco("tel_chat_howard_t4_3_8", "ricevi", 1):
                return
            $ msg("howard", "No. You have to be very quiet about it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t4_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t4_3_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t4_4:
    label tel_chat_howard_t4_4_1:
    if telefono_minuti_blocco("tel_chat_howard_t4_4_1", "ricevi", 1):
        return
    $ msg("howard", "Will there be another one? I've told him to keep me three again.")
    label tel_chat_howard_t4_4_2:
    if telefono_minuti_blocco("tel_chat_howard_t4_4_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«One copy's enough, you know.»":
            label tel_chat_howard_t4_4_3:
            if telefono_minuti_blocco("tel_chat_howard_t4_4_3", "invia", 1):
                return
            $ msg("sara", "One copy's enough, you know.")
            label tel_chat_howard_t4_4_4:
            if telefono_minuti_blocco("tel_chat_howard_t4_4_4", "ricevi", 1):
                return
            $ msg("howard", "For one person, perhaps. I like to have you in more than one room.")
            sp "He means the article."
        "«If my boss lets me.»":
            label tel_chat_howard_t4_4_5:
            if telefono_minuti_blocco("tel_chat_howard_t4_4_5", "invia", 1):
                return
            $ msg("sara", "If my boss lets me.")
            label tel_chat_howard_t4_4_6:
            if telefono_minuti_blocco("tel_chat_howard_t4_4_6", "ricevi", 2):
                return
            $ msg("howard", "She'd be a fool not to. I'd write her a letter. I've got the paper for it.")
            $ msg("howard", "I'm reading it again tonight before I turn in. It does more for me than the pills.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t4_4_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t4_4_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The light bulb

label chat_howard_t5:
    label tel_chat_howard_t5_1:
    if telefono_minuti_blocco("tel_chat_howard_t5_1", "invia", 1):
        return
    $ msg("sara", "How's the new bulb in your hall holding up?")
    return

label chat_howard_t5_entrata:
    label tel_chat_howard_t5_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_t5_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "It's lit up like Christmas in here.")
    label tel_chat_howard_t5_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_t5_entrata_2", "invia", 1):
        return
    $ msg("sara", "The new bulb's holding up, then?")
    return

label chat_howard_t5_1:
    label tel_chat_howard_t5_1_1:
    if telefono_minuti_blocco("tel_chat_howard_t5_1_1", "ricevi", 2):
        return
    $ msg("howard", "Beautifully. I switch it on just to look at it.")
    $ msg("howard", "I kept the old one. It's silly. It was the last one Mother put in.")
    label tel_chat_howard_t5_1_2:
    if telefono_minuti_blocco("tel_chat_howard_t5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's not silly at all.»":
            label tel_chat_howard_t5_1_3:
            if telefono_minuti_blocco("tel_chat_howard_t5_1_3", "invia", 1):
                return
            $ msg("sara", "That's not silly at all.")
            $ caldo()
            label tel_chat_howard_t5_1_4:
            if telefono_minuti_blocco("tel_chat_howard_t5_1_4", "ricevi", 1):
                return
            $ msg("howard", "You say that as if you meant it. I wrapped it in a sock.")
        "«Howard, it doesn't work.»":
            label tel_chat_howard_t5_1_5:
            if telefono_minuti_blocco("tel_chat_howard_t5_1_5", "invia", 1):
                return
            $ msg("sara", "Howard, it doesn't work.")
            label tel_chat_howard_t5_1_6:
            if telefono_minuti_blocco("tel_chat_howard_t5_1_6", "ricevi", 1):
                return
            $ msg("howard", "No. Well. Neither do I, strictly speaking.")
        "«Did the ladder go back in its cupboard?»":
            label tel_chat_howard_t5_1_7:
            if telefono_minuti_blocco("tel_chat_howard_t5_1_7", "invia", 1):
                return
            $ msg("sara", "Did the ladder go back in its cupboard?")
            label tel_chat_howard_t5_1_8:
            if telefono_minuti_blocco("tel_chat_howard_t5_1_8", "ricevi", 1):
                return
            $ msg("howard", "Not yet. You never know what might go next.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t5_2:
    label tel_chat_howard_t5_2_1:
    if telefono_minuti_blocco("tel_chat_howard_t5_2_1", "ricevi", 2):
        return
    $ msg("howard", "I've been thinking about what I said. From down there.")
    $ msg("howard", "About the weight at the top.")
    label tel_chat_howard_t5_2_2:
    if telefono_minuti_blocco("tel_chat_howard_t5_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I've been trying not to.»":
            label tel_chat_howard_t5_2_3:
            if telefono_minuti_blocco("tel_chat_howard_t5_2_3", "invia", 1):
                return
            $ msg("sara", "I've been trying not to.")
            $ caldo()
            label tel_chat_howard_t5_2_4:
            if telefono_minuti_blocco("tel_chat_howard_t5_2_4", "ricevi", 2):
                return
            $ msg("howard", "Have you managed?")
            $ msg("howard", "I haven't.")
        "«You should have been looking at the bulb.»":
            label tel_chat_howard_t5_2_5:
            if telefono_minuti_blocco("tel_chat_howard_t5_2_5", "invia", 1):
                return
            $ msg("sara", "You should have been looking at the bulb.")
            label tel_chat_howard_t5_2_6:
            if telefono_minuti_blocco("tel_chat_howard_t5_2_6", "ricevi", 1):
                return
            $ msg("howard", "I'd seen the bulb. It was sixty watts. There was nothing left to learn.")
        "«Let's call it your sense of humour.»":
            label tel_chat_howard_t5_2_7:
            if telefono_minuti_blocco("tel_chat_howard_t5_2_7", "invia", 1):
                return
            $ msg("sara", "Let's call it your sense of humour.")
            label tel_chat_howard_t5_2_8:
            if telefono_minuti_blocco("tel_chat_howard_t5_2_8", "ricevi", 1):
                return
            $ msg("howard", "Mother always said I hadn't got one. She'd be astonished.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t5_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t5_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t5_3:
    label tel_chat_howard_t5_3_1:
    if telefono_minuti_blocco("tel_chat_howard_t5_3_1", "ricevi", 1):
        return
    $ msg("howard", "You didn't tell [nome_compagno], did you? He'd think me a rude old man.")
    label tel_chat_howard_t5_3_2:
    if telefono_minuti_blocco("tel_chat_howard_t5_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It's between me and the ladder.»":
            label tel_chat_howard_t5_3_3:
            if telefono_minuti_blocco("tel_chat_howard_t5_3_3", "invia", 1):
                return
            $ msg("sara", "It's between me and the ladder.")
            label tel_chat_howard_t5_3_4:
            if telefono_minuti_blocco("tel_chat_howard_t5_3_4", "ricevi", 1):
                return
            $ msg("howard", "And me. I was holding it.")
        "«He'd only laugh.»":
            label tel_chat_howard_t5_3_5:
            if telefono_minuti_blocco("tel_chat_howard_t5_3_5", "invia", 1):
                return
            $ msg("sara", "He'd only laugh.")
            label tel_chat_howard_t5_3_6:
            if telefono_minuti_blocco("tel_chat_howard_t5_3_6", "ricevi", 1):
                return
            $ msg("howard", "Would he? He's a generous boy. I don't know that I would, in his shoes.")
        "«I tell him most things.»":
            label tel_chat_howard_t5_3_7:
            if telefono_minuti_blocco("tel_chat_howard_t5_3_7", "invia", 1):
                return
            $ msg("sara", "I tell him most things.")
            label tel_chat_howard_t5_3_8:
            if telefono_minuti_blocco("tel_chat_howard_t5_3_8", "ricevi", 1):
                return
            $ msg("howard", "Most things. That's a good healthy amount.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t5_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t5_3_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t5_4:
    label tel_chat_howard_t5_4_1:
    if telefono_minuti_blocco("tel_chat_howard_t5_4_1", "ricevi", 1):
        return
    $ msg("howard", "The kitchen one's begun to flicker. I only mention it.")
    label tel_chat_howard_t5_4_2:
    if telefono_minuti_blocco("tel_chat_howard_t5_4_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Of course it has.»":
            label tel_chat_howard_t5_4_3:
            if telefono_minuti_blocco("tel_chat_howard_t5_4_3", "invia", 1):
                return
            $ msg("sara", "Of course it has.")
            label tel_chat_howard_t5_4_4:
            if telefono_minuti_blocco("tel_chat_howard_t5_4_4", "ricevi", 1):
                return
            $ msg("howard", "It does it in the evenings, mostly. After six.")
        "«Buy two, this time.»":
            label tel_chat_howard_t5_4_5:
            if telefono_minuti_blocco("tel_chat_howard_t5_4_5", "invia", 1):
                return
            $ msg("sara", "Buy two, this time.")
            label tel_chat_howard_t5_4_6:
            if telefono_minuti_blocco("tel_chat_howard_t5_4_6", "ricevi", 1):
                return
            $ msg("howard", "I bought six. They come out cheaper.")
        "«Get an electrician, Howard.»":
            label tel_chat_howard_t5_4_7:
            if telefono_minuti_blocco("tel_chat_howard_t5_4_7", "invia", 1):
                return
            $ msg("sara", "Get an electrician, Howard.")
            label tel_chat_howard_t5_4_8:
            if telefono_minuti_blocco("tel_chat_howard_t5_4_8", "ricevi", 2):
                return
            $ msg("howard", "For a bulb? He'd want to hold his own ladder.")
            $ msg("howard", "Goodnight, my dear. I'll leave the hall on.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t5_4_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t5_4_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The pink slippers

label chat_howard_t6:
    label tel_chat_howard_t6_1:
    if telefono_minuti_blocco("tel_chat_howard_t6_1", "invia", 1):
        return
    $ msg("sara", "Are my slippers still by your door?")
    return

label chat_howard_t6_entrata:
    label tel_chat_howard_t6_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_t6_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "There's something of yours at mine, in case you were missing them.")
    label tel_chat_howard_t6_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_t6_entrata_2", "invia", 1):
        return
    $ msg("sara", "My slippers. Where did you put them?")
    return

label chat_howard_t6_1:
    label tel_chat_howard_t6_1_1:
    if telefono_minuti_blocco("tel_chat_howard_t6_1_1", "ricevi", 2):
        return
    $ msg("howard", "Side by side. Toes in, so you can step straight into them.")
    $ msg("howard", "I gave them a brush. They pick up fluff.")
    label tel_chat_howard_t6_1_2:
    if telefono_minuti_blocco("tel_chat_howard_t6_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You brushed my slippers?»":
            label tel_chat_howard_t6_1_3:
            if telefono_minuti_blocco("tel_chat_howard_t6_1_3", "invia", 1):
                return
            $ msg("sara", "You brushed my slippers?")
            $ caldo()
            label tel_chat_howard_t6_1_4:
            if telefono_minuti_blocco("tel_chat_howard_t6_1_4", "ricevi", 1):
                return
            $ msg("howard", "They were looking a bit neglected.")
        "«They're a size too big, you know.»":
            label tel_chat_howard_t6_1_5:
            if telefono_minuti_blocco("tel_chat_howard_t6_1_5", "invia", 1):
                return
            $ msg("sara", "They're a size too big, you know.")
            label tel_chat_howard_t6_1_6:
            if telefono_minuti_blocco("tel_chat_howard_t6_1_6", "ricevi", 1):
                return
            $ msg("howard", "I had to guess. Bare feet are hard to judge through a wall.")
            sp "Through a wall. He's so odd."
        "«They're very pink, Howard.»":
            label tel_chat_howard_t6_1_7:
            if telefono_minuti_blocco("tel_chat_howard_t6_1_7", "invia", 1):
                return
            $ msg("sara", "They're very pink, Howard.")
            label tel_chat_howard_t6_1_8:
            if telefono_minuti_blocco("tel_chat_howard_t6_1_8", "ricevi", 1):
                return
            $ msg("howard", "The girl said, is it for a lady? I said yes. She went straight to the pink.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t6_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t6_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t6_2:
    label tel_chat_howard_t6_2_1:
    if telefono_minuti_blocco("tel_chat_howard_t6_2_1", "ricevi", 2):
        return
    $ msg("howard", "It's a curious thing. A pair of slippers makes a hall look lived in.")
    $ msg("howard", "The man came to read the meter and he noticed. He said, got company? I said, now and then.")
    label tel_chat_howard_t6_2_2:
    if telefono_minuti_blocco("tel_chat_howard_t6_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What did you tell him that for?»":
            label tel_chat_howard_t6_2_3:
            if telefono_minuti_blocco("tel_chat_howard_t6_2_3", "invia", 1):
                return
            $ msg("sara", "What did you tell him that for?")
            label tel_chat_howard_t6_2_4:
            if telefono_minuti_blocco("tel_chat_howard_t6_2_4", "ricevi", 1):
                return
            $ msg("howard", "It was true. And he seemed the sort who needs something to think about.")
        "««Now and then» is about right.»":
            label tel_chat_howard_t6_2_5:
            if telefono_minuti_blocco("tel_chat_howard_t6_2_5", "invia", 1):
                return
            $ msg("sara", "«Now and then» is about right.")
            $ caldo()
            label tel_chat_howard_t6_2_6:
            if telefono_minuti_blocco("tel_chat_howard_t6_2_6", "ricevi", 1):
                return
            $ msg("howard", "We've had then. I'm quite ready for now.")
        "«You should have said they were mine.»":
            label tel_chat_howard_t6_2_7:
            if telefono_minuti_blocco("tel_chat_howard_t6_2_7", "invia", 1):
                return
            $ msg("sara", "You should have said they were mine.")
            label tel_chat_howard_t6_2_8:
            if telefono_minuti_blocco("tel_chat_howard_t6_2_8", "ricevi", 1):
                return
            $ msg("howard", "I nearly did. I liked having it to myself.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t6_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t6_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t6_3:
    label tel_chat_howard_t6_3_1:
    if telefono_minuti_blocco("tel_chat_howard_t6_3_1", "ricevi", 1):
        return
    $ msg("howard", "You'd tell me, if you thought it was odd?")
    label tel_chat_howard_t6_3_2:
    if telefono_minuti_blocco("tel_chat_howard_t6_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I think it's sweet.»":
            label tel_chat_howard_t6_3_3:
            if telefono_minuti_blocco("tel_chat_howard_t6_3_3", "invia", 1):
                return
            $ msg("sara", "I think it's sweet.")
            label tel_chat_howard_t6_3_4:
            if telefono_minuti_blocco("tel_chat_howard_t6_3_4", "ricevi", 1):
                return
            $ msg("howard", "Sweet. I'll take that to bed with me.")
        "«I don't really think about it.»":
            label tel_chat_howard_t6_3_5:
            if telefono_minuti_blocco("tel_chat_howard_t6_3_5", "invia", 1):
                return
            $ msg("sara", "I don't really think about it.")
            label tel_chat_howard_t6_3_6:
            if telefono_minuti_blocco("tel_chat_howard_t6_3_6", "ricevi", 1):
                return
            $ msg("howard", "No. That's the nicest part. You just step out of your shoes.")
            sp "I do, don't I? When did I start doing that?"
        "«Shoes off at the door is normal.»":
            label tel_chat_howard_t6_3_7:
            if telefono_minuti_blocco("tel_chat_howard_t6_3_7", "invia", 1):
                return
            $ msg("sara", "Shoes off at the door is normal.")
            label tel_chat_howard_t6_3_8:
            if telefono_minuti_blocco("tel_chat_howard_t6_3_8", "ricevi", 1):
                return
            $ msg("howard", "Perfectly normal. It's exactly what I tell myself.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t6_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t6_3_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t6_4:
    label tel_chat_howard_t6_4_1:
    if telefono_minuti_blocco("tel_chat_howard_t6_4_1", "ricevi", 1):
        return
    $ msg("howard", "I'll move them by the radiator of an evening. Then they'll be warm if you come.")
    label tel_chat_howard_t6_4_2:
    if telefono_minuti_blocco("tel_chat_howard_t6_4_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm not promising, Howard.»":
            label tel_chat_howard_t6_4_3:
            if telefono_minuti_blocco("tel_chat_howard_t6_4_3", "invia", 1):
                return
            $ msg("sara", "I'm not promising, Howard.")
            label tel_chat_howard_t6_4_4:
            if telefono_minuti_blocco("tel_chat_howard_t6_4_4", "ricevi", 1):
                return
            $ msg("howard", "Nobody's asked you to. They're only slippers.")
        "«Warm slippers. You spoil me.»":
            label tel_chat_howard_t6_4_5:
            if telefono_minuti_blocco("tel_chat_howard_t6_4_5", "invia", 1):
                return
            $ msg("sara", "Warm slippers. You spoil me.")
            label tel_chat_howard_t6_4_6:
            if telefono_minuti_blocco("tel_chat_howard_t6_4_6", "ricevi", 2):
                return
            $ msg("howard", "I'm only just getting the hang of it.")
            $ msg("howard", "Goodnight, my dear.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t6_4_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t6_4_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- That second coffee

label chat_howard_t7:
    label tel_chat_howard_t7_1:
    if telefono_minuti_blocco("tel_chat_howard_t7_1", "invia", 1):
        return
    $ msg("sara", "I keep thinking about that second coffee, at yours.")
    return

label chat_howard_t7_1:
    label tel_chat_howard_t7_1_1:
    if telefono_minuti_blocco("tel_chat_howard_t7_1_1", "ricevi", 2):
        return
    $ msg("howard", "I let mine go cold. I've never minded a cold coffee less.")
    $ msg("howard", "We don't have to say anything about it.")
    label tel_chat_howard_t7_1_2:
    if telefono_minuti_blocco("tel_chat_howard_t7_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«No. We don't.»":
            label tel_chat_howard_t7_1_3:
            if telefono_minuti_blocco("tel_chat_howard_t7_1_3", "invia", 1):
                return
            $ msg("sara", "No. We don't.")
            label tel_chat_howard_t7_1_4:
            if telefono_minuti_blocco("tel_chat_howard_t7_1_4", "ricevi", 1):
                return
            $ msg("howard", "It's rather nice, though. Not saying it together.")
        "«It was warm in there. That's all it was.»":
            label tel_chat_howard_t7_1_5:
            if telefono_minuti_blocco("tel_chat_howard_t7_1_5", "invia", 1):
                return
            $ msg("sara", "It was warm in there. That's all it was.")
            label tel_chat_howard_t7_1_6:
            if telefono_minuti_blocco("tel_chat_howard_t7_1_6", "ricevi", 1):
                return
            $ msg("howard", "It was very warm. I've kept the window shut ever since, in case.")
        "«You stopped in the middle of a sentence.»":
            label tel_chat_howard_t7_1_7:
            if telefono_minuti_blocco("tel_chat_howard_t7_1_7", "invia", 1):
                return
            $ msg("sara", "You stopped in the middle of a sentence.")
            $ caldo()
            label tel_chat_howard_t7_1_8:
            if telefono_minuti_blocco("tel_chat_howard_t7_1_8", "ricevi", 1):
                return
            $ msg("howard", "Did I? I was telling you about Lorna. I've no idea what became of her after that. Nobody has.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t7_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t7_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t7_2:
    label tel_chat_howard_t7_2_1:
    if telefono_minuti_blocco("tel_chat_howard_t7_2_1", "ricevi", 2):
        return
    $ msg("howard", "I'm not a man who expects things. I'd like you to know that.")
    $ msg("howard", "I never asked you. You'll remember that I never asked.")
    label tel_chat_howard_t7_2_2:
    if telefono_minuti_blocco("tel_chat_howard_t7_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«No. You didn't ask.»":
            label tel_chat_howard_t7_2_3:
            if telefono_minuti_blocco("tel_chat_howard_t7_2_3", "invia", 1):
                return
            $ msg("sara", "No. You didn't ask.")
            $ caldo()
            label tel_chat_howard_t7_2_4:
            if telefono_minuti_blocco("tel_chat_howard_t7_2_4", "ricevi", 1):
                return
            $ msg("howard", "That's the part I keep coming back to.")
        "«I know. It was me.»":
            label tel_chat_howard_t7_2_5:
            if telefono_minuti_blocco("tel_chat_howard_t7_2_5", "invia", 1):
                return
            $ msg("sara", "I know. It was me.")
            label tel_chat_howard_t7_2_6:
            if telefono_minuti_blocco("tel_chat_howard_t7_2_6", "ricevi", 1):
                return
            $ msg("howard", "It was you. I've turned that over so many times it's gone quite smooth.")
        "«You did look, a little.»":
            label tel_chat_howard_t7_2_7:
            if telefono_minuti_blocco("tel_chat_howard_t7_2_7", "invia", 1):
                return
            $ msg("sara", "You did look, a little.")
            label tel_chat_howard_t7_2_8:
            if telefono_minuti_blocco("tel_chat_howard_t7_2_8", "ricevi", 1):
                return
            $ msg("howard", "I looked a great deal. I'd be lying to you if I said a little.")
            sp "He always just says it."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t7_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t7_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t7_3:
    label tel_chat_howard_t7_3_1:
    if telefono_minuti_blocco("tel_chat_howard_t7_3_1", "ricevi", 1):
        return
    $ msg("howard", "Would you like me to pretend it didn't happen? I'm told I've a blank sort of face.")
    label tel_chat_howard_t7_3_2:
    if telefono_minuti_blocco("tel_chat_howard_t7_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Pretend, please.»":
            label tel_chat_howard_t7_3_3:
            if telefono_minuti_blocco("tel_chat_howard_t7_3_3", "invia", 1):
                return
            $ msg("sara", "Pretend, please.")
            label tel_chat_howard_t7_3_4:
            if telefono_minuti_blocco("tel_chat_howard_t7_3_4", "ricevi", 1):
                return
            $ msg("howard", "Pretend what? There. You see?")
        "«You'd be hopeless at it.»":
            label tel_chat_howard_t7_3_5:
            if telefono_minuti_blocco("tel_chat_howard_t7_3_5", "invia", 1):
                return
            $ msg("sara", "You'd be hopeless at it.")
            label tel_chat_howard_t7_3_6:
            if telefono_minuti_blocco("tel_chat_howard_t7_3_6", "ricevi", 1):
                return
            $ msg("howard", "I would. I went pink just writing that.")
        "«You don't have to pretend with me.»":
            label tel_chat_howard_t7_3_7:
            if telefono_minuti_blocco("tel_chat_howard_t7_3_7", "invia", 1):
                return
            $ msg("sara", "You don't have to pretend with me.")
            label tel_chat_howard_t7_3_8:
            if telefono_minuti_blocco("tel_chat_howard_t7_3_8", "ricevi", 1):
                return
            $ msg("howard", "No. I hoped I mightn't.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t7_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t7_3_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t7_4:
    label tel_chat_howard_t7_4_1:
    if telefono_minuti_blocco("tel_chat_howard_t7_4_1", "ricevi", 1):
        return
    $ msg("howard", "Shall I put the kettle on, next time you're passing? It's only coffee.")
    label tel_chat_howard_t7_4_2:
    if telefono_minuti_blocco("tel_chat_howard_t7_4_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It's only coffee.»":
            label tel_chat_howard_t7_4_3:
            if telefono_minuti_blocco("tel_chat_howard_t7_4_3", "invia", 1):
                return
            $ msg("sara", "It's only coffee.")
            label tel_chat_howard_t7_4_4:
            if telefono_minuti_blocco("tel_chat_howard_t7_4_4", "ricevi", 1):
                return
            $ msg("howard", "That's what I'll tell the cups.")
        "«I'll keep my coat on.»":
            label tel_chat_howard_t7_4_5:
            if telefono_minuti_blocco("tel_chat_howard_t7_4_5", "invia", 1):
                return
            $ msg("sara", "I'll keep my coat on.")
            label tel_chat_howard_t7_4_6:
            if telefono_minuti_blocco("tel_chat_howard_t7_4_6", "ricevi", 1):
                return
            $ msg("howard", "You do that. I'll see to the radiator.")
            sp "He's terrible. Why am I smiling at my phone?"
        "«Let's leave it there, Howard.»" (rifiuto_howard=True):
            label tel_chat_howard_t7_4_7:
            if telefono_minuti_blocco("tel_chat_howard_t7_4_7", "invia", 1):
                return
            $ msg("sara", "Let's leave it there, Howard.")
            $ frena()
            label tel_chat_howard_t7_4_8:
            if telefono_minuti_blocco("tel_chat_howard_t7_4_8", "ricevi", 1):
                return
            $ msg("howard", "Of course. Of course. Not another word. I'm very good at not another word.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t7_4_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t7_4_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The mother in my book

label chat_howard_t8:
    label tel_chat_howard_t8_1:
    if telefono_minuti_blocco("tel_chat_howard_t8_1", "invia", 1):
        return
    $ msg("sara", "What you said about my heroine's mother. Did you mean it?")
    return

label chat_howard_t8_entrata:
    label tel_chat_howard_t8_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_t8_entrata_1", "ricevi", 2):
        return
    $ msg("howard", "I've been thinking about your lady.")
    $ msg("howard", "The mother, I mean.")
    label tel_chat_howard_t8_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_t8_entrata_2", "invia", 1):
        return
    $ msg("sara", "Did you mean what you said about her?")
    return

label chat_howard_t8_1:
    label tel_chat_howard_t8_1_1:
    if telefono_minuti_blocco("tel_chat_howard_t8_1_1", "ricevi", 2):
        return
    $ msg("howard", "That I could pick her out on a bus? Every word.")
    $ msg("howard", "I had a look for her from the window, after you'd gone. Three women got off. None of them was her.")
    label tel_chat_howard_t8_1_2:
    if telefono_minuti_blocco("tel_chat_howard_t8_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I always thought she was the weakest part.»":
            label tel_chat_howard_t8_1_3:
            if telefono_minuti_blocco("tel_chat_howard_t8_1_3", "invia", 1):
                return
            $ msg("sara", "I always thought she was the weakest part.")
            $ caldo()
            label tel_chat_howard_t8_1_4:
            if telefono_minuti_blocco("tel_chat_howard_t8_1_4", "ricevi", 1):
                return
            $ msg("howard", "Then you've been reading it to the wrong people.")
        "«What gave her away?»":
            label tel_chat_howard_t8_1_5:
            if telefono_minuti_blocco("tel_chat_howard_t8_1_5", "invia", 1):
                return
            $ msg("sara", "What gave her away?")
            label tel_chat_howard_t8_1_6:
            if telefono_minuti_blocco("tel_chat_howard_t8_1_6", "ricevi", 1):
                return
            $ msg("howard", "Her hands. You say what she does with her hands when nobody's talking to her.")
        "«You were being kind.»":
            label tel_chat_howard_t8_1_7:
            if telefono_minuti_blocco("tel_chat_howard_t8_1_7", "invia", 1):
                return
            $ msg("sara", "You were being kind.")
            label tel_chat_howard_t8_1_8:
            if telefono_minuti_blocco("tel_chat_howard_t8_1_8", "ricevi", 1):
                return
            $ msg("howard", "I'm not kind about books. I've left two on a train on purpose.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t8_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t8_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t8_2:
    label tel_chat_howard_t8_2_1:
    if telefono_minuti_blocco("tel_chat_howard_t8_2_1", "ricevi", 1):
        return
    $ msg("howard", "Is she anybody real? Or am I not supposed to ask that?")
    label tel_chat_howard_t8_2_2:
    if telefono_minuti_blocco("tel_chat_howard_t8_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«A bit of everyone's.»":
            label tel_chat_howard_t8_2_3:
            if telefono_minuti_blocco("tel_chat_howard_t8_2_3", "invia", 1):
                return
            $ msg("sara", "A bit of everyone's.")
            label tel_chat_howard_t8_2_4:
            if telefono_minuti_blocco("tel_chat_howard_t8_2_4", "ricevi", 1):
                return
            $ msg("howard", "That'll be why I knew her, then.")
        "«She started as someone else, and then she wouldn't leave.»":
            label tel_chat_howard_t8_2_5:
            if telefono_minuti_blocco("tel_chat_howard_t8_2_5", "invia", 1):
                return
            $ msg("sara", "She started as someone else, and then she wouldn't leave.")
            label tel_chat_howard_t8_2_6:
            if telefono_minuti_blocco("tel_chat_howard_t8_2_6", "ricevi", 1):
                return
            $ msg("howard", "They don't. Mine's been gone a good while, and she still chooses the biscuits.")
        "«You're not supposed to ask that.»":
            label tel_chat_howard_t8_2_7:
            if telefono_minuti_blocco("tel_chat_howard_t8_2_7", "invia", 1):
                return
            $ msg("sara", "You're not supposed to ask that.")
            label tel_chat_howard_t8_2_8:
            if telefono_minuti_blocco("tel_chat_howard_t8_2_8", "ricevi", 1):
                return
            $ msg("howard", "I apologise. Nobody gave me the rules.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t8_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t8_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t8_3:
    label tel_chat_howard_t8_3_1:
    if telefono_minuti_blocco("tel_chat_howard_t8_3_1", "ricevi", 1):
        return
    $ msg("howard", "I've started noticing what I do with mine. My hands. Since you read it.")
    label tel_chat_howard_t8_3_2:
    if telefono_minuti_blocco("tel_chat_howard_t8_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And what do they do?»":
            label tel_chat_howard_t8_3_3:
            if telefono_minuti_blocco("tel_chat_howard_t8_3_3", "invia", 1):
                return
            $ msg("sara", "And what do they do?")
            $ caldo()
            label tel_chat_howard_t8_3_4:
            if telefono_minuti_blocco("tel_chat_howard_t8_3_4", "ricevi", 1):
                return
            $ msg("howard", "They fold the tea towel. Then they unfold it, so there's something to fold.")
            sp "I'm using that."
        "«Now I've made you self-conscious.»":
            label tel_chat_howard_t8_3_5:
            if telefono_minuti_blocco("tel_chat_howard_t8_3_5", "invia", 1):
                return
            $ msg("sara", "Now I've made you self-conscious.")
            label tel_chat_howard_t8_3_6:
            if telefono_minuti_blocco("tel_chat_howard_t8_3_6", "ricevi", 1):
                return
            $ msg("howard", "It's the most attention anyone's paid them in years.")
        "«It's only a paragraph, Howard.»":
            label tel_chat_howard_t8_3_7:
            if telefono_minuti_blocco("tel_chat_howard_t8_3_7", "invia", 1):
                return
            $ msg("sara", "It's only a paragraph, Howard.")
            label tel_chat_howard_t8_3_8:
            if telefono_minuti_blocco("tel_chat_howard_t8_3_8", "ricevi", 1):
                return
            $ msg("howard", "It was a very good paragraph. It's followed me about all evening.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t8_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t8_3_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t8_4:
    label tel_chat_howard_t8_4_1:
    if telefono_minuti_blocco("tel_chat_howard_t8_4_1", "ricevi", 1):
        return
    $ msg("howard", "Would you read me the next bit? When there is one. I'd get the cups out.")
    label tel_chat_howard_t8_4_2:
    if telefono_minuti_blocco("tel_chat_howard_t8_4_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«When it's ready.»":
            label tel_chat_howard_t8_4_3:
            if telefono_minuti_blocco("tel_chat_howard_t8_4_3", "invia", 1):
                return
            $ msg("sara", "When it's ready.")
            label tel_chat_howard_t8_4_4:
            if telefono_minuti_blocco("tel_chat_howard_t8_4_4", "ricevi", 1):
                return
            $ msg("howard", "I'd take it unready. I'm not particular.")
        "«There's a queue.»":
            label tel_chat_howard_t8_4_5:
            if telefono_minuti_blocco("tel_chat_howard_t8_4_5", "invia", 1):
                return
            $ msg("sara", "There's a queue.")
            label tel_chat_howard_t8_4_6:
            if telefono_minuti_blocco("tel_chat_howard_t8_4_6", "ricevi", 2):
                return
            $ msg("howard", "Then I'll bring a chair.")
            $ msg("howard", "Goodnight, Sara. If she gets off the next one, I'll give her your love.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t8_4_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t8_4_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The bathroom bulb

label chat_howard_t9:
    label tel_chat_howard_t9_1:
    if telefono_minuti_blocco("tel_chat_howard_t9_1", "invia", 1):
        return
    $ msg("sara", "I hope you're enjoying your bathroom, now you can see it.")
    return

label chat_howard_t9_entrata:
    label tel_chat_howard_t9_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_t9_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "Let there be light, eh?")
    label tel_chat_howard_t9_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_t9_entrata_2", "invia", 1):
        return
    $ msg("sara", "Enjoying your bathroom, Howard?")
    return

label chat_howard_t9_1:
    label tel_chat_howard_t9_1_1:
    if telefono_minuti_blocco("tel_chat_howard_t9_1_1", "ricevi", 2):
        return
    $ msg("howard", "I've been in there twice for no reason.")
    $ msg("howard", "It's cruel, a new bulb. It shows you the tiles.")
    label tel_chat_howard_t9_1_2:
    if telefono_minuti_blocco("tel_chat_howard_t9_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Better than the ceiling, though?»":
            label tel_chat_howard_t9_1_3:
            if telefono_minuti_blocco("tel_chat_howard_t9_1_3", "invia", 1):
                return
            $ msg("sara", "Better than the ceiling, though?")
            $ caldo()
            label tel_chat_howard_t9_1_4:
            if telefono_minuti_blocco("tel_chat_howard_t9_1_4", "ricevi", 2):
                return
            $ msg("howard", "Ah.")
            $ msg("howard", "You understood that, then.")
        "«You were supposed to be holding me up.»":
            label tel_chat_howard_t9_1_5:
            if telefono_minuti_blocco("tel_chat_howard_t9_1_5", "invia", 1):
                return
            $ msg("sara", "You were supposed to be holding me up.")
            label tel_chat_howard_t9_1_6:
            if telefono_minuti_blocco("tel_chat_howard_t9_1_6", "ricevi", 1):
                return
            $ msg("howard", "I was. Both hands. It's only the eyes that weren't needed.")
        "«Get yourself a proper step. You'll break your neck on that bath.»":
            label tel_chat_howard_t9_1_7:
            if telefono_minuti_blocco("tel_chat_howard_t9_1_7", "invia", 1):
                return
            $ msg("sara", "Get yourself a proper step. You'll break your neck on that bath.")
            label tel_chat_howard_t9_1_8:
            if telefono_minuti_blocco("tel_chat_howard_t9_1_8", "ricevi", 1):
                return
            $ msg("howard", "If I had a proper step I'd never need anybody.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t9_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t9_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t9_2:
    label tel_chat_howard_t9_2_1:
    if telefono_minuti_blocco("tel_chat_howard_t9_2_1", "ricevi", 1):
        return
    $ msg("howard", "I've got quite a grip, for my age. Was it too firm?")
    label tel_chat_howard_t9_2_2:
    if telefono_minuti_blocco("tel_chat_howard_t9_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You wouldn't have dropped me.»":
            label tel_chat_howard_t9_2_3:
            if telefono_minuti_blocco("tel_chat_howard_t9_2_3", "invia", 1):
                return
            $ msg("sara", "You wouldn't have dropped me.")
            $ caldo()
            label tel_chat_howard_t9_2_4:
            if telefono_minuti_blocco("tel_chat_howard_t9_2_4", "ricevi", 1):
                return
            $ msg("howard", "Not for anything. I'd have gone down first, and you'd have had something soft to land on.")
        "«It was a bit firm, yes.»":
            label tel_chat_howard_t9_2_5:
            if telefono_minuti_blocco("tel_chat_howard_t9_2_5", "invia", 1):
                return
            $ msg("sara", "It was a bit firm, yes.")
            label tel_chat_howard_t9_2_6:
            if telefono_minuti_blocco("tel_chat_howard_t9_2_6", "ricevi", 1):
                return
            $ msg("howard", "I thought so. I could still feel it in my palms at eight o'clock.")
        "«I was thinking about the electricity.»":
            label tel_chat_howard_t9_2_7:
            if telefono_minuti_blocco("tel_chat_howard_t9_2_7", "invia", 1):
                return
            $ msg("sara", "I was thinking about the electricity.")
            label tel_chat_howard_t9_2_8:
            if telefono_minuti_blocco("tel_chat_howard_t9_2_8", "ricevi", 1):
                return
            $ msg("howard", "Very wise. One of us should be.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t9_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t9_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t9_3:
    label tel_chat_howard_t9_3_1:
    if telefono_minuti_blocco("tel_chat_howard_t9_3_1", "ricevi", 1):
        return
    $ msg("howard", "There are eleven bulbs in this flat, you know. I went round and counted.")
    label tel_chat_howard_t9_3_2:
    if telefono_minuti_blocco("tel_chat_howard_t9_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And how many are about to go?»":
            label tel_chat_howard_t9_3_3:
            if telefono_minuti_blocco("tel_chat_howard_t9_3_3", "invia", 1):
                return
            $ msg("sara", "And how many are about to go?")
            label tel_chat_howard_t9_3_4:
            if telefono_minuti_blocco("tel_chat_howard_t9_3_4", "ricevi", 1):
                return
            $ msg("howard", "It's hard to say. They go when they feel like it. I could ring you.")
        "«I'm charging for the next one.»":
            label tel_chat_howard_t9_3_5:
            if telefono_minuti_blocco("tel_chat_howard_t9_3_5", "invia", 1):
                return
            $ msg("sara", "I'm charging for the next one.")
            label tel_chat_howard_t9_3_6:
            if telefono_minuti_blocco("tel_chat_howard_t9_3_6", "ricevi", 1):
                return
            $ msg("howard", "Name it. I've got a pension and nobody to spend it on.")
        "«You'll have to wait your turn.»":
            label tel_chat_howard_t9_3_7:
            if telefono_minuti_blocco("tel_chat_howard_t9_3_7", "invia", 1):
                return
            $ msg("sara", "You'll have to wait your turn.")
            label tel_chat_howard_t9_3_8:
            if telefono_minuti_blocco("tel_chat_howard_t9_3_8", "ricevi", 1):
                return
            $ msg("howard", "I'm very good at it. I did thirty-one years, with a hooter at each end.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t9_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t9_3_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t9_4:
    label tel_chat_howard_t9_4_1:
    if telefono_minuti_blocco("tel_chat_howard_t9_4_1", "ricevi", 1):
        return
    $ msg("howard", "I've left it on, if you're wondering what the light is under my door.")
    label tel_chat_howard_t9_4_2:
    if telefono_minuti_blocco("tel_chat_howard_t9_4_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I wasn't wondering.»":
            label tel_chat_howard_t9_4_3:
            if telefono_minuti_blocco("tel_chat_howard_t9_4_3", "invia", 1):
                return
            $ msg("sara", "I wasn't wondering.")
            label tel_chat_howard_t9_4_4:
            if telefono_minuti_blocco("tel_chat_howard_t9_4_4", "ricevi", 1):
                return
            $ msg("howard", "No. But you'd have looked, and then you would have.")
        "«It's company, isn't it? A light.»":
            label tel_chat_howard_t9_4_5:
            if telefono_minuti_blocco("tel_chat_howard_t9_4_5", "invia", 1):
                return
            $ msg("sara", "It's company, isn't it? A light.")
            label tel_chat_howard_t9_4_6:
            if telefono_minuti_blocco("tel_chat_howard_t9_4_6", "ricevi", 2):
                return
            $ msg("howard", "It is. I'll tell it you said so.")
            $ msg("howard", "Goodnight, my dear.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t9_4_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t9_4_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The jar of ragù

label chat_howard_t10:
    label tel_chat_howard_t10_1:
    if telefono_minuti_blocco("tel_chat_howard_t10_1", "invia", 1):
        return
    $ msg("sara", "Your mother's ragù is in our fridge, and I keep opening the door to look at it.")
    return

label chat_howard_t10_entrata:
    label tel_chat_howard_t10_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_t10_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "Is my mother in your fridge? The sauce, I mean.")
    label tel_chat_howard_t10_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_t10_entrata_2", "invia", 1):
        return
    $ msg("sara", "Second shelf. I keep opening the door to look at it.")
    return

label chat_howard_t10_1:
    label tel_chat_howard_t10_1_1:
    if telefono_minuti_blocco("tel_chat_howard_t10_1_1", "ricevi", 2):
        return
    $ msg("howard", "Don't leave it too long. It sulks.")
    $ msg("howard", "Low heat, lid off. And stir it the way I told you.")
    label tel_chat_howard_t10_1_2:
    if telefono_minuti_blocco("tel_chat_howard_t10_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Like I'm telling it a secret.»":
            label tel_chat_howard_t10_1_3:
            if telefono_minuti_blocco("tel_chat_howard_t10_1_3", "invia", 1):
                return
            $ msg("sara", "Like I'm telling it a secret.")
            $ caldo()
            label tel_chat_howard_t10_1_4:
            if telefono_minuti_blocco("tel_chat_howard_t10_1_4", "ricevi", 1):
                return
            $ msg("howard", "You were listening! I thought you were only being polite.")
        "«How long for?»":
            label tel_chat_howard_t10_1_5:
            if telefono_minuti_blocco("tel_chat_howard_t10_1_5", "invia", 1):
                return
            $ msg("sara", "How long for?")
            label tel_chat_howard_t10_1_6:
            if telefono_minuti_blocco("tel_chat_howard_t10_1_6", "ricevi", 1):
                return
            $ msg("howard", "Until you've run out of secrets. Twenty minutes, for most people.")
        "«I was going to microwave it.»":
            label tel_chat_howard_t10_1_7:
            if telefono_minuti_blocco("tel_chat_howard_t10_1_7", "invia", 1):
                return
            $ msg("sara", "I was going to microwave it.")
            label tel_chat_howard_t10_1_8:
            if telefono_minuti_blocco("tel_chat_howard_t10_1_8", "ricevi", 1):
                return
            $ msg("howard", "Sara. I'll pretend the signal went.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t10_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t10_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t10_2:
    label tel_chat_howard_t10_2_1:
    if telefono_minuti_blocco("tel_chat_howard_t10_2_1", "ricevi", 1):
        return
    $ msg("howard", "It's pleasant, two people at one stove. I'd forgotten you have to take turns breathing.")
    label tel_chat_howard_t10_2_2:
    if telefono_minuti_blocco("tel_chat_howard_t10_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It smelled like somebody's childhood.»":
            label tel_chat_howard_t10_2_3:
            if telefono_minuti_blocco("tel_chat_howard_t10_2_3", "invia", 1):
                return
            $ msg("sara", "It smelled like somebody's childhood.")
            $ caldo()
            label tel_chat_howard_t10_2_4:
            if telefono_minuti_blocco("tel_chat_howard_t10_2_4", "ricevi", 1):
                return
            $ msg("howard", "It was mine. You're welcome to it.")
        "«It's a very small kitchen.»":
            label tel_chat_howard_t10_2_5:
            if telefono_minuti_blocco("tel_chat_howard_t10_2_5", "invia", 1):
                return
            $ msg("sara", "It's a very small kitchen.")
            label tel_chat_howard_t10_2_6:
            if telefono_minuti_blocco("tel_chat_howard_t10_2_6", "ricevi", 1):
                return
            $ msg("howard", "It is. I've never once thought of that as a fault.")
        "«I still smell of onions.»":
            label tel_chat_howard_t10_2_7:
            if telefono_minuti_blocco("tel_chat_howard_t10_2_7", "invia", 1):
                return
            $ msg("sara", "I still smell of onions.")
            label tel_chat_howard_t10_2_8:
            if telefono_minuti_blocco("tel_chat_howard_t10_2_8", "ricevi", 1):
                return
            $ msg("howard", "It'll be gone by morning. If it isn't, come and complain.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t10_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t10_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t10_3:
    label tel_chat_howard_t10_3_1:
    if telefono_minuti_blocco("tel_chat_howard_t10_3_1", "ricevi", 1):
        return
    $ msg("howard", "What did [nome_compagno] say, when he saw the jar?")
    label tel_chat_howard_t10_3_2:
    if telefono_minuti_blocco("tel_chat_howard_t10_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I told him the neighbour made it.»":
            label tel_chat_howard_t10_3_3:
            if telefono_minuti_blocco("tel_chat_howard_t10_3_3", "invia", 1):
                return
            $ msg("sara", "I told him the neighbour made it.")
            label tel_chat_howard_t10_3_4:
            if telefono_minuti_blocco("tel_chat_howard_t10_3_4", "ricevi", 1):
                return
            $ msg("howard", "There. That's all he needs to know.")
        "«He hasn't seen it yet. It's at the back.»":
            label tel_chat_howard_t10_3_5:
            if telefono_minuti_blocco("tel_chat_howard_t10_3_5", "invia", 1):
                return
            $ msg("sara", "He hasn't seen it yet. It's at the back.")
            label tel_chat_howard_t10_3_6:
            if telefono_minuti_blocco("tel_chat_howard_t10_3_6", "ricevi", 1):
                return
            $ msg("howard", "Behind the milk? That's where I'd have put it.")
        "«He'll love it.»":
            label tel_chat_howard_t10_3_7:
            if telefono_minuti_blocco("tel_chat_howard_t10_3_7", "invia", 1):
                return
            $ msg("sara", "He'll love it.")
            label tel_chat_howard_t10_3_8:
            if telefono_minuti_blocco("tel_chat_howard_t10_3_8", "ricevi", 1):
                return
            $ msg("howard", "I'm sure he will. He'll eat it in front of the television and tell you it was nice.")
            sp "He would, too. Those exact words."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t10_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t10_3_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t10_4:
    label tel_chat_howard_t10_4_1:
    if telefono_minuti_blocco("tel_chat_howard_t10_4_1", "ricevi", 1):
        return
    $ msg("howard", "I'm making it again before long. It's no trouble, I can only make it for four.")
    label tel_chat_howard_t10_4_2:
    if telefono_minuti_blocco("tel_chat_howard_t10_4_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I might hold you to that.»":
            label tel_chat_howard_t10_4_3:
            if telefono_minuti_blocco("tel_chat_howard_t10_4_3", "invia", 1):
                return
            $ msg("sara", "I might hold you to that.")
            label tel_chat_howard_t10_4_4:
            if telefono_minuti_blocco("tel_chat_howard_t10_4_4", "ricevi", 1):
                return
            $ msg("howard", "Hold away.")
        "«We'll see, Howard.»":
            label tel_chat_howard_t10_4_5:
            if telefono_minuti_blocco("tel_chat_howard_t10_4_5", "invia", 1):
                return
            $ msg("sara", "We'll see, Howard.")
            label tel_chat_howard_t10_4_6:
            if telefono_minuti_blocco("tel_chat_howard_t10_4_6", "ricevi", 2):
                return
            $ msg("howard", "We will. I'll keep you the good chair. Not the one that wobbles.")
            $ msg("howard", "Goodnight, my dear.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t10_4_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t10_4_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Saying no on the landing

label chat_howard_t11:
    label tel_chat_howard_t11_1:
    if telefono_minuti_blocco("tel_chat_howard_t11_1", "invia", 1):
        return
    $ msg("sara", "I hope I wasn't rude on the landing, Howard.")
    return

label chat_howard_t11_entrata:
    label tel_chat_howard_t11_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_t11_entrata_1", "ricevi", 2):
        return
    $ msg("howard", "It's only me.")
    $ msg("howard", "I wanted to say, no hard feelings about the landing.")
    label tel_chat_howard_t11_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_t11_entrata_2", "invia", 1):
        return
    $ msg("sara", "I was worried I'd been rude.")
    return

label chat_howard_t11_1:
    label tel_chat_howard_t11_1_1:
    if telefono_minuti_blocco("tel_chat_howard_t11_1_1", "ricevi", 2):
        return
    $ msg("howard", "Rude! You couldn't be rude with a manual.")
    $ msg("howard", "I put one cup back. It's no trouble. It was a clean cup.")
    sp "One cup."
    label tel_chat_howard_t11_1_2:
    if telefono_minuti_blocco("tel_chat_howard_t11_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Oh, Howard. I'm sorry.»":
            label tel_chat_howard_t11_1_3:
            if telefono_minuti_blocco("tel_chat_howard_t11_1_3", "invia", 1):
                return
            $ msg("sara", "Oh, Howard. I'm sorry.")
            $ caldo()
            label tel_chat_howard_t11_1_4:
            if telefono_minuti_blocco("tel_chat_howard_t11_1_4", "ricevi", 1):
                return
            $ msg("howard", "Now don't. If you're sorry, I'll feel I've done something.")
        "«You'd got everything ready?»":
            label tel_chat_howard_t11_1_5:
            if telefono_minuti_blocco("tel_chat_howard_t11_1_5", "invia", 1):
                return
            $ msg("sara", "You'd got everything ready?")
            label tel_chat_howard_t11_1_6:
            if telefono_minuti_blocco("tel_chat_howard_t11_1_6", "ricevi", 1):
                return
            $ msg("howard", "Only the kettle. It's got nowhere else to be.")
        "«I'd had a long day.»":
            label tel_chat_howard_t11_1_7:
            if telefono_minuti_blocco("tel_chat_howard_t11_1_7", "invia", 1):
                return
            $ msg("sara", "I'd had a long day.")
            label tel_chat_howard_t11_1_8:
            if telefono_minuti_blocco("tel_chat_howard_t11_1_8", "ricevi", 1):
                return
            $ msg("howard", "I could tell. You come up slower when you have.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t11_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t11_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t11_2:
    label tel_chat_howard_t11_2_1:
    if telefono_minuti_blocco("tel_chat_howard_t11_2_1", "ricevi", 2):
        return
    $ msg("howard", "You mustn't come because you think you ought to. I'd hate that.")
    $ msg("howard", "I'd sooner have ten minutes you wanted than a whole evening you didn't.")
    label tel_chat_howard_t11_2_2:
    if telefono_minuti_blocco("tel_chat_howard_t11_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Then I'll come when I want to.»":
            label tel_chat_howard_t11_2_3:
            if telefono_minuti_blocco("tel_chat_howard_t11_2_3", "invia", 1):
                return
            $ msg("sara", "Then I'll come when I want to.")
            $ caldo()
            label tel_chat_howard_t11_2_4:
            if telefono_minuti_blocco("tel_chat_howard_t11_2_4", "ricevi", 1):
                return
            $ msg("howard", "That's the one. I'll listen out.")
        "«That's good of you.»":
            label tel_chat_howard_t11_2_5:
            if telefono_minuti_blocco("tel_chat_howard_t11_2_5", "invia", 1):
                return
            $ msg("sara", "That's good of you.")
            label tel_chat_howard_t11_2_6:
            if telefono_minuti_blocco("tel_chat_howard_t11_2_6", "ricevi", 1):
                return
            $ msg("howard", "It isn't, really. It's arithmetic. I've got more evenings than you have.")
        "«I just need a few evenings to myself.»":
            label tel_chat_howard_t11_2_7:
            if telefono_minuti_blocco("tel_chat_howard_t11_2_7", "invia", 1):
                return
            $ msg("sara", "I just need a few evenings to myself.")
            label tel_chat_howard_t11_2_8:
            if telefono_minuti_blocco("tel_chat_howard_t11_2_8", "ricevi", 1):
                return
            $ msg("howard", "Of course you do. I've plenty, if you run short.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t11_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t11_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t11_3:
    label tel_chat_howard_t11_3_1:
    if telefono_minuti_blocco("tel_chat_howard_t11_3_1", "ricevi", 1):
        return
    $ msg("howard", "Did you do something nice instead?")
    label tel_chat_howard_t11_3_2:
    if telefono_minuti_blocco("tel_chat_howard_t11_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Sat on the sofa with the television off.»":
            label tel_chat_howard_t11_3_3:
            if telefono_minuti_blocco("tel_chat_howard_t11_3_3", "invia", 1):
                return
            $ msg("sara", "Sat on the sofa with the television off.")
            label tel_chat_howard_t11_3_4:
            if telefono_minuti_blocco("tel_chat_howard_t11_3_4", "ricevi", 1):
                return
            $ msg("howard", "I know that one. I can recommend the second half.")
        "«Waited for [nome_compagno].»":
            label tel_chat_howard_t11_3_5:
            if telefono_minuti_blocco("tel_chat_howard_t11_3_5", "invia", 1):
                return
            $ msg("sara", "Waited for [nome_compagno].")
            label tel_chat_howard_t11_3_6:
            if telefono_minuti_blocco("tel_chat_howard_t11_3_6", "ricevi", 1):
                return
            $ msg("howard", "I heard him come in. He takes the last three stairs together when he's hungry.")
        "«Not really.»":
            label tel_chat_howard_t11_3_7:
            if telefono_minuti_blocco("tel_chat_howard_t11_3_7", "invia", 1):
                return
            $ msg("sara", "Not really.")
            label tel_chat_howard_t11_3_8:
            if telefono_minuti_blocco("tel_chat_howard_t11_3_8", "ricevi", 1):
                return
            $ msg("howard", "No. Nor me. We might have done it together.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t11_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t11_3_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t11_4:
    label tel_chat_howard_t11_4_1:
    if telefono_minuti_blocco("tel_chat_howard_t11_4_1", "ricevi", 1):
        return
    $ msg("howard", "I'm not keeping you up?")
    label tel_chat_howard_t11_4_2:
    if telefono_minuti_blocco("tel_chat_howard_t11_4_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«A little.»":
            label tel_chat_howard_t11_4_3:
            if telefono_minuti_blocco("tel_chat_howard_t11_4_3", "invia", 1):
                return
            $ msg("sara", "A little.")
            label tel_chat_howard_t11_4_4:
            if telefono_minuti_blocco("tel_chat_howard_t11_4_4", "ricevi", 1):
                return
            $ msg("howard", "Then I'll stop. I'm stopping. That was me, stopping.")
        "«No. I wanted to be sure you were all right.»":
            label tel_chat_howard_t11_4_5:
            if telefono_minuti_blocco("tel_chat_howard_t11_4_5", "invia", 1):
                return
            $ msg("sara", "No. I wanted to be sure you were all right.")
            label tel_chat_howard_t11_4_6:
            if telefono_minuti_blocco("tel_chat_howard_t11_4_6", "ricevi", 2):
                return
            $ msg("howard", "I am now. I'll put the cup away properly.")
            $ msg("howard", "Goodnight, Sara.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t11_4_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t11_4_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The parcel you weighed

label chat_howard_t12:
    label tel_chat_howard_t12_1:
    if telefono_minuti_blocco("tel_chat_howard_t12_1", "invia", 1):
        return
    $ msg("sara", "Thank you again for taking my parcel in.")
    return

label chat_howard_t12_entrata:
    label tel_chat_howard_t12_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_t12_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "Did the parcel get home safely? It's a long way, next door.")
    label tel_chat_howard_t12_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_t12_entrata_2", "invia", 1):
        return
    $ msg("sara", "Safe and sound. Thank you for taking it in.")
    return

label chat_howard_t12_1:
    label tel_chat_howard_t12_1_1:
    if telefono_minuti_blocco("tel_chat_howard_t12_1_1", "ricevi", 2):
        return
    $ msg("howard", "It was no trouble. I was standing by the door anyway.")
    $ msg("howard", "I did hold it up to the light. Only to see which way up it went.")
    label tel_chat_howard_t12_1_2:
    if telefono_minuti_blocco("tel_chat_howard_t12_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Howard!»":
            label tel_chat_howard_t12_1_3:
            if telefono_minuti_blocco("tel_chat_howard_t12_1_3", "invia", 1):
                return
            $ msg("sara", "Howard!")
            $ caldo()
            label tel_chat_howard_t12_1_4:
            if telefono_minuti_blocco("tel_chat_howard_t12_1_4", "ricevi", 1):
                return
            $ msg("howard", "I didn't open it. I'd like that understood. A man has to stop somewhere.")
        "«It was a top. From Joanie.»":
            label tel_chat_howard_t12_1_5:
            if telefono_minuti_blocco("tel_chat_howard_t12_1_5", "invia", 1):
                return
            $ msg("sara", "It was a top. From Joanie.")
            label tel_chat_howard_t12_1_6:
            if telefono_minuti_blocco("tel_chat_howard_t12_1_6", "ricevi", 1):
                return
            $ msg("howard", "A top. There must be a good deal of it missing, going by the weight.")
        "«And which way up did it go?»":
            label tel_chat_howard_t12_1_7:
            if telefono_minuti_blocco("tel_chat_howard_t12_1_7", "invia", 1):
                return
            $ msg("sara", "And which way up did it go?")
            label tel_chat_howard_t12_1_8:
            if telefono_minuti_blocco("tel_chat_howard_t12_1_8", "ricevi", 1):
                return
            $ msg("howard", "I couldn't tell you. It seemed to be mostly air.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t12_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t12_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t12_2:
    label tel_chat_howard_t12_2_1:
    if telefono_minuti_blocco("tel_chat_howard_t12_2_1", "ricevi", 1):
        return
    $ msg("howard", "Is it for an occasion? You needn't say.")
    label tel_chat_howard_t12_2_2:
    if telefono_minuti_blocco("tel_chat_howard_t12_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I haven't decided if I'm brave enough.»":
            label tel_chat_howard_t12_2_3:
            if telefono_minuti_blocco("tel_chat_howard_t12_2_3", "invia", 1):
                return
            $ msg("sara", "I haven't decided if I'm brave enough.")
            $ caldo()
            label tel_chat_howard_t12_2_4:
            if telefono_minuti_blocco("tel_chat_howard_t12_2_4", "ricevi", 1):
                return
            $ msg("howard", "You're braver than you think. It's the rest of us who aren't ready.")
        "«It's a joke between friends.»":
            label tel_chat_howard_t12_2_5:
            if telefono_minuti_blocco("tel_chat_howard_t12_2_5", "invia", 1):
                return
            $ msg("sara", "It's a joke between friends.")
            label tel_chat_howard_t12_2_6:
            if telefono_minuti_blocco("tel_chat_howard_t12_2_6", "ricevi", 1):
                return
            $ msg("howard", "Some of the best clothes start out that way.")
        "«It's not the sort of thing you wear on the stairs.»":
            label tel_chat_howard_t12_2_7:
            if telefono_minuti_blocco("tel_chat_howard_t12_2_7", "invia", 1):
                return
            $ msg("sara", "It's not the sort of thing you wear on the stairs.")
            label tel_chat_howard_t12_2_8:
            if telefono_minuti_blocco("tel_chat_howard_t12_2_8", "ricevi", 1):
                return
            $ msg("howard", "That's a shame. The stairs could do with it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t12_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t12_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t12_3:
    label tel_chat_howard_t12_3_1:
    if telefono_minuti_blocco("tel_chat_howard_t12_3_1", "ricevi", 1):
        return
    $ msg("howard", "If you ever want an opinion before you go out in it, I'm only next door. I'd be honest.")
    label tel_chat_howard_t12_3_2:
    if telefono_minuti_blocco("tel_chat_howard_t12_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You'd say it was lovely whatever it was.»":
            label tel_chat_howard_t12_3_3:
            if telefono_minuti_blocco("tel_chat_howard_t12_3_3", "invia", 1):
                return
            $ msg("sara", "You'd say it was lovely whatever it was.")
            label tel_chat_howard_t12_3_4:
            if telefono_minuti_blocco("tel_chat_howard_t12_3_4", "ricevi", 1):
                return
            $ msg("howard", "Then we'd both have had a nice evening.")
        "«I've got a mirror, thank you.»":
            label tel_chat_howard_t12_3_5:
            if telefono_minuti_blocco("tel_chat_howard_t12_3_5", "invia", 1):
                return
            $ msg("sara", "I've got a mirror, thank you.")
            label tel_chat_howard_t12_3_6:
            if telefono_minuti_blocco("tel_chat_howard_t12_3_6", "ricevi", 1):
                return
            $ msg("howard", "Mirrors only tell you what you already think.")
        "«That's what Joanie's for.»":
            label tel_chat_howard_t12_3_7:
            if telefono_minuti_blocco("tel_chat_howard_t12_3_7", "invia", 1):
                return
            $ msg("sara", "That's what Joanie's for.")
            label tel_chat_howard_t12_3_8:
            if telefono_minuti_blocco("tel_chat_howard_t12_3_8", "ricevi", 1):
                return
            $ msg("howard", "Of course. She's got an eye. I've got two, but they're old.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t12_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t12_3_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t12_4:
    label tel_chat_howard_t12_4_1:
    if telefono_minuti_blocco("tel_chat_howard_t12_4_1", "ricevi", 1):
        return
    $ msg("howard", "I'll take in anything they send you, mind. Any hour. I sign very neatly.")
    label tel_chat_howard_t12_4_2:
    if telefono_minuti_blocco("tel_chat_howard_t12_4_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«My personal post office.»":
            label tel_chat_howard_t12_4_3:
            if telefono_minuti_blocco("tel_chat_howard_t12_4_3", "invia", 1):
                return
            $ msg("sara", "My personal post office.")
            label tel_chat_howard_t12_4_4:
            if telefono_minuti_blocco("tel_chat_howard_t12_4_4", "ricevi", 1):
                return
            $ msg("howard", "I'd want a little window. And a bell you'd have to ring.")
        "«I'll try to be in, next time.»":
            label tel_chat_howard_t12_4_5:
            if telefono_minuti_blocco("tel_chat_howard_t12_4_5", "invia", 1):
                return
            $ msg("sara", "I'll try to be in, next time.")
            label tel_chat_howard_t12_4_6:
            if telefono_minuti_blocco("tel_chat_howard_t12_4_6", "ricevi", 2):
                return
            $ msg("howard", "Don't go out of your way. I like having something of yours on the table.")
            $ msg("howard", "Goodnight, Sara.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t12_4_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t12_4_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The housework

label chat_howard_t13:
    label tel_chat_howard_t13_1:
    if telefono_minuti_blocco("tel_chat_howard_t13_1", "invia", 1):
        return
    $ msg("sara", "My arms ache, Howard, and it's entirely your fault.")
    return

label chat_howard_t13_1:
    label tel_chat_howard_t13_1_1:
    if telefono_minuti_blocco("tel_chat_howard_t13_1_1", "ricevi", 2):
        return
    $ msg("howard", "That's honest work, my dear. It's the good kind of ache.")
    $ msg("howard", "I've been walking about with my hands behind my back, so as not to spoil anything.")
    label tel_chat_howard_t13_1_2:
    if telefono_minuti_blocco("tel_chat_howard_t13_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It did come up well, didn't it?»":
            label tel_chat_howard_t13_1_3:
            if telefono_minuti_blocco("tel_chat_howard_t13_1_3", "invia", 1):
                return
            $ msg("sara", "It did come up well, didn't it?")
            $ caldo()
            label tel_chat_howard_t13_1_4:
            if telefono_minuti_blocco("tel_chat_howard_t13_1_4", "ricevi", 1):
                return
            $ msg("howard", "It came up like a church. I felt I ought to whisper.")
        "«You could do it yourself next time.»":
            label tel_chat_howard_t13_1_5:
            if telefono_minuti_blocco("tel_chat_howard_t13_1_5", "invia", 1):
                return
            $ msg("sara", "You could do it yourself next time.")
            label tel_chat_howard_t13_1_6:
            if telefono_minuti_blocco("tel_chat_howard_t13_1_6", "ricevi", 1):
                return
            $ msg("howard", "I could. It wouldn't be half so nice to look at.")
        "«You just sat there.»":
            label tel_chat_howard_t13_1_7:
            if telefono_minuti_blocco("tel_chat_howard_t13_1_7", "invia", 1):
                return
            $ msg("sara", "You just sat there.")
            label tel_chat_howard_t13_1_8:
            if telefono_minuti_blocco("tel_chat_howard_t13_1_8", "ricevi", 1):
                return
            $ msg("howard", "I was supervising. It's very tiring, concentrating that hard.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t13_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t13_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t13_2:
    label tel_chat_howard_t13_2_1:
    if telefono_minuti_blocco("tel_chat_howard_t13_2_1", "ricevi", 1):
        return
    $ msg("howard", "And the dress fits, then.")
    label tel_chat_howard_t13_2_2:
    if telefono_minuti_blocco("tel_chat_howard_t13_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You guessed my size.»":
            label tel_chat_howard_t13_2_3:
            if telefono_minuti_blocco("tel_chat_howard_t13_2_3", "invia", 1):
                return
            $ msg("sara", "You guessed my size.")
            label tel_chat_howard_t13_2_4:
            if telefono_minuti_blocco("tel_chat_howard_t13_2_4", "ricevi", 1):
                return
            $ msg("howard", "I'd had it in my head for a while.")
        "«It's a bit much for housework.»":
            label tel_chat_howard_t13_2_5:
            if telefono_minuti_blocco("tel_chat_howard_t13_2_5", "invia", 1):
                return
            $ msg("sara", "It's a bit much for housework.")
            $ caldo()
            label tel_chat_howard_t13_2_6:
            if telefono_minuti_blocco("tel_chat_howard_t13_2_6", "ricevi", 1):
                return
            $ msg("howard", "It's to save your own clothes. That's what I told them in the shop.")
        "«It's only to keep my things clean.»":
            label tel_chat_howard_t13_2_7:
            if telefono_minuti_blocco("tel_chat_howard_t13_2_7", "invia", 1):
                return
            $ msg("sara", "It's only to keep my things clean.")
            label tel_chat_howard_t13_2_8:
            if telefono_minuti_blocco("tel_chat_howard_t13_2_8", "ricevi", 1):
                return
            $ msg("howard", "That's all it is. We're both very practical people.")
            sp "It's a kindness. He can't manage on his own."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t13_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t13_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t13_3:
    label tel_chat_howard_t13_3_1:
    if telefono_minuti_blocco("tel_chat_howard_t13_3_1", "ricevi", 1):
        return
    $ msg("howard", "I've started a list. It's only short. It goes over the page.")
    label tel_chat_howard_t13_3_2:
    if telefono_minuti_blocco("tel_chat_howard_t13_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Read me the first line.»":
            label tel_chat_howard_t13_3_3:
            if telefono_minuti_blocco("tel_chat_howard_t13_3_3", "invia", 1):
                return
            $ msg("sara", "Read me the first line.")
            label tel_chat_howard_t13_3_4:
            if telefono_minuti_blocco("tel_chat_howard_t13_3_4", "ricevi", 1):
                return
            $ msg("howard", "It says «Sara». I haven't got any further.")
        "«One thing at a time, Howard.»":
            label tel_chat_howard_t13_3_5:
            if telefono_minuti_blocco("tel_chat_howard_t13_3_5", "invia", 1):
                return
            $ msg("sara", "One thing at a time, Howard.")
            label tel_chat_howard_t13_3_6:
            if telefono_minuti_blocco("tel_chat_howard_t13_3_6", "ricevi", 1):
                return
            $ msg("howard", "One at a time. I wouldn't want to run out.")
        "«You're spoiling yourself.»":
            label tel_chat_howard_t13_3_7:
            if telefono_minuti_blocco("tel_chat_howard_t13_3_7", "invia", 1):
                return
            $ msg("sara", "You're spoiling yourself.")
            label tel_chat_howard_t13_3_8:
            if telefono_minuti_blocco("tel_chat_howard_t13_3_8", "ricevi", 1):
                return
            $ msg("howard", "Somebody had to, in the end.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t13_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t13_3_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_t13_4:
    label tel_chat_howard_t13_4_1:
    if telefono_minuti_blocco("tel_chat_howard_t13_4_1", "ricevi", 1):
        return
    $ msg("howard", "Does it bother you, being looked at while you work?")
    label tel_chat_howard_t13_4_2:
    if telefono_minuti_blocco("tel_chat_howard_t13_4_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I forget you're there.»":
            label tel_chat_howard_t13_4_3:
            if telefono_minuti_blocco("tel_chat_howard_t13_4_3", "invia", 1):
                return
            $ msg("sara", "I forget you're there.")
            label tel_chat_howard_t13_4_4:
            if telefono_minuti_blocco("tel_chat_howard_t13_4_4", "ricevi", 1):
                return
            $ msg("howard", "That's the nicest thing you could have said. And I'm always there.")
        "«A bit. Then it doesn't.»":
            label tel_chat_howard_t13_4_5:
            if telefono_minuti_blocco("tel_chat_howard_t13_4_5", "invia", 1):
                return
            $ msg("sara", "A bit. Then it doesn't.")
            label tel_chat_howard_t13_4_6:
            if telefono_minuti_blocco("tel_chat_howard_t13_4_6", "ricevi", 1):
                return
            $ msg("howard", "That's how it was at the factory, with the foreman. Only he never made anybody tea.")
        "«You'd look anyway.»":
            label tel_chat_howard_t13_4_7:
            if telefono_minuti_blocco("tel_chat_howard_t13_4_7", "invia", 1):
                return
            $ msg("sara", "You'd look anyway.")
            label tel_chat_howard_t13_4_8:
            if telefono_minuti_blocco("tel_chat_howard_t13_4_8", "ricevi", 2):
                return
            $ msg("howard", "I would. But it's good manners to ask.")
            $ msg("howard", "Rest your arms. I'll wash my own cup tonight.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t13_4_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_t13_4_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: quanto gli manca

label chat_howard_c1:
    label tel_chat_howard_c1_1:
    if telefono_minuti_blocco("tel_chat_howard_c1_1", "invia", 1):
        return
    $ msg("sara", "It was quiet today. I didn't hear your door once.")
    return

label chat_howard_c1_entrata:
    label tel_chat_howard_c1_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_c1_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "Very quiet today, on your side.")
    label tel_chat_howard_c1_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_c1_entrata_2", "invia", 1):
        return
    $ msg("sara", "It was quiet on yours. I didn't hear your door once.")
    return

label chat_howard_c1_1:
    label tel_chat_howard_c1_1_1:
    if telefono_minuti_blocco("tel_chat_howard_c1_1_1", "ricevi", 2):
        return
    $ msg("howard", "I was keeping still. I was listening for yours.")
    $ msg("howard", "So there we were. Two people being quiet at each other.")
    label tel_chat_howard_c1_1_2:
    if telefono_minuti_blocco("tel_chat_howard_c1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I missed you, I think.»":
            label tel_chat_howard_c1_1_3:
            if telefono_minuti_blocco("tel_chat_howard_c1_1_3", "invia", 1):
                return
            $ msg("sara", "I missed you, I think.")
            $ caldo()
            label tel_chat_howard_c1_1_4:
            if telefono_minuti_blocco("tel_chat_howard_c1_1_4", "ricevi", 1):
                return
            $ msg("howard", "You think. I'll take a thought. I'll put it on the shelf with the sherry.")
        "«You should go out more.»":
            label tel_chat_howard_c1_1_5:
            if telefono_minuti_blocco("tel_chat_howard_c1_1_5", "invia", 1):
                return
            $ msg("sara", "You should go out more.")
            label tel_chat_howard_c1_1_6:
            if telefono_minuti_blocco("tel_chat_howard_c1_1_6", "ricevi", 1):
                return
            $ msg("howard", "I did. I went as far as the landing and came back for my glasses.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_c1_2:
    label tel_chat_howard_c1_2_1:
    if telefono_minuti_blocco("tel_chat_howard_c1_2_1", "ricevi", 1):
        return
    $ msg("howard", "It's a funny word, missing. You'd think it would go down with practice.")
    label tel_chat_howard_c1_2_2:
    if telefono_minuti_blocco("tel_chat_howard_c1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What do you miss? Be specific.»":
            label tel_chat_howard_c1_2_3:
            if telefono_minuti_blocco("tel_chat_howard_c1_2_3", "invia", 1):
                return
            $ msg("sara", "What do you miss? Be specific.")
            $ caldo()
            label tel_chat_howard_c1_2_4:
            if telefono_minuti_blocco("tel_chat_howard_c1_2_4", "ricevi", 2):
                return
            $ msg("howard", "Your heels on the third stair. The way you breathe out before you find your keys. A certain green jumper, going away.")
            $ msg("howard", "It's got a very good back to it, that jumper.")
        "«You see me every other day, Howard.»":
            label tel_chat_howard_c1_2_5:
            if telefono_minuti_blocco("tel_chat_howard_c1_2_5", "invia", 1):
                return
            $ msg("sara", "You see me every other day, Howard.")
            label tel_chat_howard_c1_2_6:
            if telefono_minuti_blocco("tel_chat_howard_c1_2_6", "ricevi", 1):
                return
            $ msg("howard", "I do. It's the one in between that's the trouble.")
        "«That's enough for tonight.»" (rifiuto_howard=True):
            label tel_chat_howard_c1_2_7:
            if telefono_minuti_blocco("tel_chat_howard_c1_2_7", "invia", 1):
                return
            $ msg("sara", "That's enough for tonight.")
            $ frena()
            label tel_chat_howard_c1_2_8:
            if telefono_minuti_blocco("tel_chat_howard_c1_2_8", "ricevi", 1):
                return
            $ msg("howard", "Quite right. I'd got carried away. Goodnight, my dear.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_c1_3:
    label tel_chat_howard_c1_3_1:
    if telefono_minuti_blocco("tel_chat_howard_c1_3_1", "ricevi", 1):
        return
    $ msg("howard", "I shan't ask you for anything. I only wanted it said to somebody.")
    label tel_chat_howard_c1_3_2:
    if telefono_minuti_blocco("tel_chat_howard_c1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Come and knock, next time. Instead of listening.»":
            label tel_chat_howard_c1_3_3:
            if telefono_minuti_blocco("tel_chat_howard_c1_3_3", "invia", 1):
                return
            $ msg("sara", "Come and knock, next time. Instead of listening.")
            label tel_chat_howard_c1_3_4:
            if telefono_minuti_blocco("tel_chat_howard_c1_3_4", "ricevi", 2):
                return
            $ msg("howard", "I'd have to have a reason.")
            $ msg("howard", "I've three ready. One of them's a fuse.")
        "«Make one up. You're good at it.»":
            label tel_chat_howard_c1_3_5:
            if telefono_minuti_blocco("tel_chat_howard_c1_3_5", "invia", 1):
                return
            $ msg("sara", "Make one up. You're good at it.")
            sp "He is good at it, isn't he?"
            label tel_chat_howard_c1_3_6:
            if telefono_minuti_blocco("tel_chat_howard_c1_3_6", "ricevi", 1):
                return
            $ msg("howard", "Goodnight, my dear. I'll start on one in the morning.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: abitudini condivise

label chat_howard_c2:
    label tel_chat_howard_c2_1:
    if telefono_minuti_blocco("tel_chat_howard_c2_1", "invia", 1):
        return
    $ msg("sara", "I caught myself making two cups of tea.")
    return

label chat_howard_c2_entrata:
    label tel_chat_howard_c2_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_c2_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "Are you still up? I can see your light under the door.")
    label tel_chat_howard_c2_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_c2_entrata_2", "invia", 1):
        return
    $ msg("sara", "I'm up. I made two cups of tea by mistake.")
    return

label chat_howard_c2_1:
    label tel_chat_howard_c2_1_1:
    if telefono_minuti_blocco("tel_chat_howard_c2_1_1", "ricevi", 1):
        return
    $ msg("howard", "Did you drink the other one?")
    label tel_chat_howard_c2_1_2:
    if telefono_minuti_blocco("tel_chat_howard_c2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I nearly brought it round.»":
            label tel_chat_howard_c2_1_3:
            if telefono_minuti_blocco("tel_chat_howard_c2_1_3", "invia", 1):
                return
            $ msg("sara", "I nearly brought it round.")
            $ caldo()
            label tel_chat_howard_c2_1_4:
            if telefono_minuti_blocco("tel_chat_howard_c2_1_4", "ricevi", 1):
                return
            $ msg("howard", "Nearly! I'd my hand on the latch. I don't know why. I just felt like holding it.")
        "«I poured it on the plant.»":
            label tel_chat_howard_c2_1_5:
            if telefono_minuti_blocco("tel_chat_howard_c2_1_5", "invia", 1):
                return
            $ msg("sara", "I poured it on the plant.")
            label tel_chat_howard_c2_1_6:
            if telefono_minuti_blocco("tel_chat_howard_c2_1_6", "ricevi", 1):
                return
            $ msg("howard", "Lucky plant.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_c2_2:
    label tel_chat_howard_c2_2_1:
    if telefono_minuti_blocco("tel_chat_howard_c2_2_1", "ricevi", 1):
        return
    $ msg("howard", "I've a habit of my own, if we're owning up. When you put your light out, I put mine out.")
    label tel_chat_howard_c2_2_2:
    if telefono_minuti_blocco("tel_chat_howard_c2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Every night?»":
            label tel_chat_howard_c2_2_3:
            if telefono_minuti_blocco("tel_chat_howard_c2_2_3", "invia", 1):
                return
            $ msg("sara", "Every night?")
            $ caldo()
            label tel_chat_howard_c2_2_4:
            if telefono_minuti_blocco("tel_chat_howard_c2_2_4", "ricevi", 1):
                return
            $ msg("howard", "Every night you're in. I say goodnight to the wall. I've never told anybody that.")
        "«And if I read till two?»":
            label tel_chat_howard_c2_2_5:
            if telefono_minuti_blocco("tel_chat_howard_c2_2_5", "invia", 1):
                return
            $ msg("sara", "And if I read till two?")
            label tel_chat_howard_c2_2_6:
            if telefono_minuti_blocco("tel_chat_howard_c2_2_6", "ricevi", 1):
                return
            $ msg("howard", "Then I'm a bit of a wreck in the mornings.")
        "«I wish you hadn't told me that one.»" (rifiuto_howard=True):
            label tel_chat_howard_c2_2_7:
            if telefono_minuti_blocco("tel_chat_howard_c2_2_7", "invia", 1):
                return
            $ msg("sara", "I wish you hadn't told me that one.")
            $ frena()
            label tel_chat_howard_c2_2_8:
            if telefono_minuti_blocco("tel_chat_howard_c2_2_8", "ricevi", 1):
                return
            $ msg("howard", "Then I haven't. It's gone. I'll leave mine on tonight.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_c2_3:
    label tel_chat_howard_c2_3_1:
    if telefono_minuti_blocco("tel_chat_howard_c2_3_1", "ricevi", 1):
        return
    $ msg("howard", "I used to think I'd got set in my ways. It turns out I was only waiting for some better ones.")
    label tel_chat_howard_c2_3_2:
    if telefono_minuti_blocco("tel_chat_howard_c2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Goodnight, then. Count to ten and I'll do the lamp.»":
            label tel_chat_howard_c2_3_3:
            if telefono_minuti_blocco("tel_chat_howard_c2_3_3", "invia", 1):
                return
            $ msg("sara", "Goodnight, then. Count to ten and I'll do the lamp.")
            label tel_chat_howard_c2_3_4:
            if telefono_minuti_blocco("tel_chat_howard_c2_3_4", "ricevi", 1):
                return
            $ msg("howard", "One. I'm going to go slowly.")
        "«You could knock on the wall.»":
            label tel_chat_howard_c2_3_5:
            if telefono_minuti_blocco("tel_chat_howard_c2_3_5", "invia", 1):
                return
            $ msg("sara", "You could knock on the wall.")
            label tel_chat_howard_c2_3_6:
            if telefono_minuti_blocco("tel_chat_howard_c2_3_6", "ricevi", 1):
                return
            $ msg("howard", "Twice. Softly. And you needn't do anything about it.")
            sp "Two knocks. I'm lying here, listening for two knocks."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: sentirsi a casa

label chat_howard_c3:
    label tel_chat_howard_c3_1:
    if telefono_minuti_blocco("tel_chat_howard_c3_1", "invia", 1):
        return
    $ msg("sara", "I sat in your chair the other day as if I'd bought it.")
    return

label chat_howard_c3_entrata:
    label tel_chat_howard_c3_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_c3_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "The chair's still warm, would you believe.")
    label tel_chat_howard_c3_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_c3_entrata_2", "invia", 1):
        return
    $ msg("sara", "I did rather sit in it as if I'd bought it.")
    return

label chat_howard_c3_1:
    label tel_chat_howard_c3_1_1:
    if telefono_minuti_blocco("tel_chat_howard_c3_1_1", "ricevi", 1):
        return
    $ msg("howard", "I noticed. I went into the kitchen so as not to make a thing of it.")
    label tel_chat_howard_c3_1_2:
    if telefono_minuti_blocco("tel_chat_howard_c3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You made a thing of it. I heard you humming.»":
            label tel_chat_howard_c3_1_3:
            if telefono_minuti_blocco("tel_chat_howard_c3_1_3", "invia", 1):
                return
            $ msg("sara", "You made a thing of it. I heard you humming.")
            $ caldo()
            label tel_chat_howard_c3_1_4:
            if telefono_minuti_blocco("tel_chat_howard_c3_1_4", "ricevi", 1):
                return
            $ msg("howard", "It's the extractor fan. ...It was me.")
        "«It's just a habit.»":
            label tel_chat_howard_c3_1_5:
            if telefono_minuti_blocco("tel_chat_howard_c3_1_5", "invia", 1):
                return
            $ msg("sara", "It's just a habit.")
            label tel_chat_howard_c3_1_6:
            if telefono_minuti_blocco("tel_chat_howard_c3_1_6", "ricevi", 1):
                return
            $ msg("howard", "That's what I was humming about.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_c3_2:
    label tel_chat_howard_c3_2_1:
    if telefono_minuti_blocco("tel_chat_howard_c3_2_1", "ricevi", 1):
        return
    $ msg("howard", "You've a way of sitting in it now. Legs under you. As if you'd been poured.")
    label tel_chat_howard_c3_2_2:
    if telefono_minuti_blocco("tel_chat_howard_c3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And where do you look, when I'm poured?»":
            label tel_chat_howard_c3_2_3:
            if telefono_minuti_blocco("tel_chat_howard_c3_2_3", "invia", 1):
                return
            $ msg("sara", "And where do you look, when I'm poured?")
            $ caldo()
            label tel_chat_howard_c3_2_4:
            if telefono_minuti_blocco("tel_chat_howard_c3_2_4", "ricevi", 1):
                return
            $ msg("howard", "I start at the feet, to be polite. Then I give up being polite.")
        "«It's a comfy chair.»":
            label tel_chat_howard_c3_2_5:
            if telefono_minuti_blocco("tel_chat_howard_c3_2_5", "invia", 1):
                return
            $ msg("sara", "It's a comfy chair.")
            label tel_chat_howard_c3_2_6:
            if telefono_minuti_blocco("tel_chat_howard_c3_2_6", "ricevi", 1):
                return
            $ msg("howard", "It wasn't, before. I've sat in it. It's you that does it.")
        "«I'd better go home earlier, next time.»" (rifiuto_howard=True):
            label tel_chat_howard_c3_2_7:
            if telefono_minuti_blocco("tel_chat_howard_c3_2_7", "invia", 1):
                return
            $ msg("sara", "I'd better go home earlier, next time.")
            $ frena()
            label tel_chat_howard_c3_2_8:
            if telefono_minuti_blocco("tel_chat_howard_c3_2_8", "ricevi", 1):
                return
            $ msg("howard", "You go when you like. I'm only glad of the chair.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_c3_3:
    label tel_chat_howard_c3_3_1:
    if telefono_minuti_blocco("tel_chat_howard_c3_3_1", "ricevi", 1):
        return
    $ msg("howard", "May I say the thing I oughtn't?")
    label tel_chat_howard_c3_3_2:
    if telefono_minuti_blocco("tel_chat_howard_c3_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You always do.»":
            label tel_chat_howard_c3_3_3:
            if telefono_minuti_blocco("tel_chat_howard_c3_3_3", "invia", 1):
                return
            $ msg("sara", "You always do.")
            label tel_chat_howard_c3_3_4:
            if telefono_minuti_blocco("tel_chat_howard_c3_3_4", "ricevi", 1):
                return
            $ msg("howard", "You look more at home at mine than at yours. I said I oughtn't.")
            sp "It's an awful thing to say. And it's a bit true."
        "«No. Let me guess it.»":
            label tel_chat_howard_c3_3_5:
            if telefono_minuti_blocco("tel_chat_howard_c3_3_5", "invia", 1):
                return
            $ msg("sara", "No. Let me guess it.")
            label tel_chat_howard_c3_3_6:
            if telefono_minuti_blocco("tel_chat_howard_c3_3_6", "ricevi", 2):
                return
            $ msg("howard", "You'd be right first time. You generally are, about me.")
            $ msg("howard", "Goodnight, my dear. Your cup's on the drainer, upside down, the way you leave it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c3_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_c3_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: importanti l'uno per l'altra

label chat_howard_d1:
    label tel_chat_howard_d1_1:
    if telefono_minuti_blocco("tel_chat_howard_d1_1", "invia", 1):
        return
    $ msg("sara", "Can you hear me through the wall, when I'm quiet?")
    return

label chat_howard_d1_1:
    label tel_chat_howard_d1_1_1:
    if telefono_minuti_blocco("tel_chat_howard_d1_1_1", "ricevi", 1):
        return
    $ msg("howard", "I can hear you being quiet. It's got a different sound from empty.")
    label tel_chat_howard_d1_1_2:
    if telefono_minuti_blocco("tel_chat_howard_d1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What am I doing, then?»":
            label tel_chat_howard_d1_1_3:
            if telefono_minuti_blocco("tel_chat_howard_d1_1_3", "invia", 1):
                return
            $ msg("sara", "What am I doing, then?")
            $ caldo()
            label tel_chat_howard_d1_1_4:
            if telefono_minuti_blocco("tel_chat_howard_d1_1_4", "ricevi", 1):
                return
            $ msg("howard", "You're lying on your side. You've got the phone under the sheet. I'm guessing. I'm hoping.")
        "«Good. I like that you can.»":
            label tel_chat_howard_d1_1_5:
            if telefono_minuti_blocco("tel_chat_howard_d1_1_5", "invia", 1):
                return
            $ msg("sara", "Good. I like that you can.")
            label tel_chat_howard_d1_1_6:
            if telefono_minuti_blocco("tel_chat_howard_d1_1_6", "ricevi", 1):
                return
            $ msg("howard", "Then I'll leave my hand where it is. It's flat on the paper. On the roses.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_d1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_d1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_d1_2:
    label tel_chat_howard_d1_2_1:
    if telefono_minuti_blocco("tel_chat_howard_d1_2_1", "ricevi", 1):
        return
    $ msg("howard", "I'm not used to being wanted, Sara. You'll have to tell me how it goes.")
    label tel_chat_howard_d1_2_2:
    if telefono_minuti_blocco("tel_chat_howard_d1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Slowly. And you tell me everything you're thinking of.»":
            label tel_chat_howard_d1_2_3:
            if telefono_minuti_blocco("tel_chat_howard_d1_2_3", "invia", 1):
                return
            $ msg("sara", "Slowly. And you tell me everything you're thinking of.")
            $ caldo()
            label tel_chat_howard_d1_2_4:
            if telefono_minuti_blocco("tel_chat_howard_d1_2_4", "ricevi", 1):
                return
            $ msg("howard", "I've the lamp on and my eyes shut. I'm looking up at you, only there isn't any bulb.")
        "«You start. You're better at it than you think.»":
            label tel_chat_howard_d1_2_5:
            if telefono_minuti_blocco("tel_chat_howard_d1_2_5", "invia", 1):
                return
            $ msg("sara", "You start. You're better at it than you think.")
            label tel_chat_howard_d1_2_6:
            if telefono_minuti_blocco("tel_chat_howard_d1_2_6", "ricevi", 1):
                return
            $ msg("howard", "I'd ask for your hand first. I'd want to look at it. I'd work my way along.")
        "«You talk, and I'll try not to make a sound.»":
            label tel_chat_howard_d1_2_7:
            if telefono_minuti_blocco("tel_chat_howard_d1_2_7", "invia", 1):
                return
            $ msg("sara", "You talk, and I'll try not to make a sound.")
            label tel_chat_howard_d1_2_8:
            if telefono_minuti_blocco("tel_chat_howard_d1_2_8", "ricevi", 1):
                return
            $ msg("howard", "Make one. Just one. I've lived next door to silence for thirty years.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_d1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_d1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_d1_3:
    label tel_chat_howard_d1_3_1:
    if telefono_minuti_blocco("tel_chat_howard_d1_3_1", "ricevi", 1):
        return
    $ msg("howard", "Was that you?")
    label tel_chat_howard_d1_3_2:
    if telefono_minuti_blocco("tel_chat_howard_d1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That was me.»":
            label tel_chat_howard_d1_3_3:
            if telefono_minuti_blocco("tel_chat_howard_d1_3_3", "invia", 1):
                return
            $ msg("sara", "That was me.")
            label tel_chat_howard_d1_3_4:
            if telefono_minuti_blocco("tel_chat_howard_d1_3_4", "ricevi", 1):
                return
            $ msg("howard", "I've sat up in bed. I've got my glasses on, and I don't know what for.")
        "«Knock twice.»":
            label tel_chat_howard_d1_3_5:
            if telefono_minuti_blocco("tel_chat_howard_d1_3_5", "invia", 1):
                return
            $ msg("sara", "Knock twice.")
            label tel_chat_howard_d1_3_6:
            if telefono_minuti_blocco("tel_chat_howard_d1_3_6", "ricevi", 2):
                return
            $ msg("howard", "There. Did you feel it? I did, right up the arm.")
            $ msg("howard", "God bless you, my dear.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_d1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_d1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: una quotidianità comune

label chat_howard_d2:
    label tel_chat_howard_d2_1:
    if telefono_minuti_blocco("tel_chat_howard_d2_1", "invia", 1):
        return
    $ msg("sara", "If I lived at yours, what would a Sunday be like?")
    return

label chat_howard_d2_1:
    label tel_chat_howard_d2_1_1:
    if telefono_minuti_blocco("tel_chat_howard_d2_1_1", "ricevi", 1):
        return
    $ msg("howard", "I'd be up at six, so as to come back to bed at seven and find you in it.")
    label tel_chat_howard_d2_1_2:
    if telefono_minuti_blocco("tel_chat_howard_d2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And I'd be cross.»":
            label tel_chat_howard_d2_1_3:
            if telefono_minuti_blocco("tel_chat_howard_d2_1_3", "invia", 1):
                return
            $ msg("sara", "And I'd be cross.")
            $ caldo()
            label tel_chat_howard_d2_1_4:
            if telefono_minuti_blocco("tel_chat_howard_d2_1_4", "ricevi", 1):
                return
            $ msg("howard", "You'd be warm and cross. I've thought about it a good deal. I've thought about the warm.")
        "«And then?»":
            label tel_chat_howard_d2_1_5:
            if telefono_minuti_blocco("tel_chat_howard_d2_1_5", "invia", 1):
                return
            $ msg("sara", "And then?")
            label tel_chat_howard_d2_1_6:
            if telefono_minuti_blocco("tel_chat_howard_d2_1_6", "ricevi", 1):
                return
            $ msg("howard", "Then I wouldn't go and get the paper. For the first time in thirty years, I'd let it lie.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_d2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_d2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_d2_2:
    label tel_chat_howard_d2_2_1:
    if telefono_minuti_blocco("tel_chat_howard_d2_2_1", "ricevi", 1):
        return
    $ msg("howard", "You'd have one of my shirts on. The blue. It'd be buttoned wrong.")
    label tel_chat_howard_d2_2_2:
    if telefono_minuti_blocco("tel_chat_howard_d2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You'd want to do it up properly.»":
            label tel_chat_howard_d2_2_3:
            if telefono_minuti_blocco("tel_chat_howard_d2_2_3", "invia", 1):
                return
            $ msg("sara", "You'd want to do it up properly.")
            $ caldo()
            label tel_chat_howard_d2_2_4:
            if telefono_minuti_blocco("tel_chat_howard_d2_2_4", "ricevi", 1):
                return
            $ msg("howard", "I'd have to undo it first, to get it straight. You can't hurry a thing like that.")
        "«There'd be nothing under it.»":
            label tel_chat_howard_d2_2_5:
            if telefono_minuti_blocco("tel_chat_howard_d2_2_5", "invia", 1):
                return
            $ msg("sara", "There'd be nothing under it.")
            label tel_chat_howard_d2_2_6:
            if telefono_minuti_blocco("tel_chat_howard_d2_2_6", "ricevi", 1):
                return
            $ msg("howard", "I'd put the kettle on. I'd need something to hold.")
        "«I'd let you look all morning.»":
            label tel_chat_howard_d2_2_7:
            if telefono_minuti_blocco("tel_chat_howard_d2_2_7", "invia", 1):
                return
            $ msg("sara", "I'd let you look all morning.")
            label tel_chat_howard_d2_2_8:
            if telefono_minuti_blocco("tel_chat_howard_d2_2_8", "ricevi", 1):
                return
            $ msg("howard", "Oh, my dear. I'd look as if there were going to be a test.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_d2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_d2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_d2_3:
    label tel_chat_howard_d2_3_1:
    if telefono_minuti_blocco("tel_chat_howard_d2_3_1", "ricevi", 1):
        return
    $ msg("howard", "I've let my tea go cold again. I seem to do it whenever it matters.")
    label tel_chat_howard_d2_3_2:
    if telefono_minuti_blocco("tel_chat_howard_d2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You could come and have mine.»":
            label tel_chat_howard_d2_3_3:
            if telefono_minuti_blocco("tel_chat_howard_d2_3_3", "invia", 1):
                return
            $ msg("sara", "You could come and have mine.")
            label tel_chat_howard_d2_3_4:
            if telefono_minuti_blocco("tel_chat_howard_d2_3_4", "ricevi", 1):
                return
            $ msg("howard", "It's nine steps to your door. I've counted them, for no reason.")
        "«Nine isn't many.»":
            label tel_chat_howard_d2_3_5:
            if telefono_minuti_blocco("tel_chat_howard_d2_3_5", "invia", 1):
                return
            $ msg("sara", "Nine isn't many.")
            label tel_chat_howard_d2_3_6:
            if telefono_minuti_blocco("tel_chat_howard_d2_3_6", "ricevi", 2):
                return
            $ msg("howard", "It's the longest walk in the building. I'll start now, and you can tell me to stop.")
            $ msg("howard", "I'll listen for you not saying it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_d2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_d2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return
