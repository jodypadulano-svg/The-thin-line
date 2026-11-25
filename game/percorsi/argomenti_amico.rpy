## GENERATO da tools/telefono/componi.py: si modifica tools/telefono/amico.txt.

init python:
    discorso("amico_t1", "amico", ESTRANEI, argomento="The room beyond the door", se="giorno in (14, 15)")
    discorso("amico_t2", "amico", CONOSCENTI, argomento="Her minute", se="fatto('ep2_d16_minuto_darius')")
    discorso("amico_t3", "amico", CONOSCENTI, argomento="The blue packet", se="giorno >= 16")
    discorso("amico_c1", "amico", COMPLICI, flirt=True)
    discorso("amico_c2", "amico", COMPLICI, flirt=True)
    discorso("amico_c3", "amico", COMPLICI, flirt=True)
    discorso("amico_d1", "amico", INTIMI, flirt=True)
    discorso("amico_d2", "amico", INTIMI, flirt=True)


## --- The room beyond the door

label chat_amico_t1:
    label tel_chat_amico_t1_1:
    if telefono_minuti_blocco("tel_chat_amico_t1_1", "invia", 1):
        return
    $ msg("sara", "I wrote the first sentence of the room. On the way home from our coffee.")
    return

label chat_amico_t1_1:
    label tel_chat_amico_t1_1_1:
    if telefono_minuti_blocco("tel_chat_amico_t1_1_1", "ricevi", 1):
        return
    $ msg("amico", "No way. Between the café and your door? That's eight minutes")
    label tel_chat_amico_t1_1_2:
    if telefono_minuti_blocco("tel_chat_amico_t1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Seven. I walked fast.»":
            label tel_chat_amico_t1_1_3:
            if telefono_minuti_blocco("tel_chat_amico_t1_1_3", "invia", 1):
                return
            $ msg("sara", "Seven. I walked fast.")
            $ caldo()
            label tel_chat_amico_t1_1_4:
            if telefono_minuti_blocco("tel_chat_amico_t1_1_4", "ricevi", 1):
                return
            $ msg("amico", "Lol. Don't tell me it. Actually tell me it. No, don't")
        "«It came all at once.»":
            label tel_chat_amico_t1_1_5:
            if telefono_minuti_blocco("tel_chat_amico_t1_1_5", "invia", 1):
                return
            $ msg("sara", "It came all at once.")
            label tel_chat_amico_t1_1_6:
            if telefono_minuti_blocco("tel_chat_amico_t1_1_6", "ricevi", 1):
                return
            $ msg("amico", "Best kind. I get that with crosswords and it's nowhere near as useful")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_t1_2:
    label tel_chat_amico_t1_2_1:
    if telefono_minuti_blocco("tel_chat_amico_t1_2_1", "ricevi", 1):
        return
    $ msg("amico", "So does she get her minute on her own in there?")
    label tel_chat_amico_t1_2_2:
    if telefono_minuti_blocco("tel_chat_amico_t1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«She does. She sits on the bed and doesn't take her coat off.»":
            label tel_chat_amico_t1_2_3:
            if telefono_minuti_blocco("tel_chat_amico_t1_2_3", "invia", 1):
                return
            $ msg("sara", "She does. She sits on the bed and doesn't take her coat off.")
            label tel_chat_amico_t1_2_4:
            if telefono_minuti_blocco("tel_chat_amico_t1_2_4", "ricevi", 1):
                return
            $ msg("amico", "Yeah. That's exactly what she'd do. You don't take your coat off till you're sure")
        "«You're the reason she gets it.»":
            label tel_chat_amico_t1_2_5:
            if telefono_minuti_blocco("tel_chat_amico_t1_2_5", "invia", 1):
                return
            $ msg("sara", "You're the reason she gets it.")
            $ caldo()
            label tel_chat_amico_t1_2_6:
            if telefono_minuti_blocco("tel_chat_amico_t1_2_6", "ricevi", 1):
                return
            $ msg("amico", "Me? All I said was I'd want one")
            sp "Nobody else had said it, though."
        "«I haven't decided yet.»":
            label tel_chat_amico_t1_2_7:
            if telefono_minuti_blocco("tel_chat_amico_t1_2_7", "invia", 1):
                return
            $ msg("sara", "I haven't decided yet.")
            label tel_chat_amico_t1_2_8:
            if telefono_minuti_blocco("tel_chat_amico_t1_2_8", "ricevi", 1):
                return
            $ msg("amico", "Take your time. She's waited this long")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_t1_3:
    label tel_chat_amico_t1_3_1:
    if telefono_minuti_blocco("tel_chat_amico_t1_3_1", "ricevi", 1):
        return
    $ msg("amico", "Can I ask why you don't talk about it much? When we're all together")
    label tel_chat_amico_t1_3_2:
    if telefono_minuti_blocco("tel_chat_amico_t1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Because everyone's so nice about it.»":
            label tel_chat_amico_t1_3_3:
            if telefono_minuti_blocco("tel_chat_amico_t1_3_3", "invia", 1):
                return
            $ msg("sara", "Because everyone's so nice about it.")
            label tel_chat_amico_t1_3_4:
            if telefono_minuti_blocco("tel_chat_amico_t1_3_4", "ricevi", 1):
                return
            $ msg("amico", "Lol. Yeah. That's the worst. Nice is where things go to sleep")
        "«I don't know. I do with you, apparently.»":
            label tel_chat_amico_t1_3_5:
            if telefono_minuti_blocco("tel_chat_amico_t1_3_5", "invia", 1):
                return
            $ msg("sara", "I don't know. I do with you, apparently.")
            label tel_chat_amico_t1_3_6:
            if telefono_minuti_blocco("tel_chat_amico_t1_3_6", "ricevi", 2):
                return
            $ msg("amico", "Good. I've got room. Ask anyone, I'm mostly room")
            $ msg("amico", "See you Tuesday. I'm bringing the ones on the left")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Her minute

label chat_amico_t2:
    label tel_chat_amico_t2_1:
    if telefono_minuti_blocco("tel_chat_amico_t2_1", "invia", 1):
        return
    $ msg("sara", "You asked if she'd got her minute. At dinner. Nobody else heard.")
    return

label chat_amico_t2_1:
    label tel_chat_amico_t2_1_1:
    if telefono_minuti_blocco("tel_chat_amico_t2_1_1", "ricevi", 1):
        return
    $ msg("amico", "I was whispering. I'm a big lad, it takes effort")
    label tel_chat_amico_t2_1_2:
    if telefono_minuti_blocco("tel_chat_amico_t2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I liked that you remembered.»":
            label tel_chat_amico_t2_1_3:
            if telefono_minuti_blocco("tel_chat_amico_t2_1_3", "invia", 1):
                return
            $ msg("sara", "I liked that you remembered.")
            $ caldo()
            label tel_chat_amico_t2_1_4:
            if telefono_minuti_blocco("tel_chat_amico_t2_1_4", "ricevi", 1):
                return
            $ msg("amico", "It stuck. I've been thinking about that coat on the bed")
        "«It made my evening.»":
            label tel_chat_amico_t2_1_5:
            if telefono_minuti_blocco("tel_chat_amico_t2_1_5", "invia", 1):
                return
            $ msg("sara", "It made my evening.")
            label tel_chat_amico_t2_1_6:
            if telefono_minuti_blocco("tel_chat_amico_t2_1_6", "ricevi", 1):
                return
            $ msg("amico", "Yeah? That and the biscuit. Admit it")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_t2_2:
    label tel_chat_amico_t2_2_1:
    if telefono_minuti_blocco("tel_chat_amico_t2_2_1", "ricevi", 1):
        return
    $ msg("amico", "What was it like, sending it? I'd have hit the button and then thrown the laptop in the river")
    label tel_chat_amico_t2_2_2:
    if telefono_minuti_blocco("tel_chat_amico_t2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I opened the sent copy just to look at my name.»":
            label tel_chat_amico_t2_2_3:
            if telefono_minuti_blocco("tel_chat_amico_t2_2_3", "invia", 1):
                return
            $ msg("sara", "I opened the sent copy just to look at my name.")
            label tel_chat_amico_t2_2_4:
            if telefono_minuti_blocco("tel_chat_amico_t2_2_4", "ricevi", 1):
                return
            $ msg("amico", "Lol. I'd have printed that bit. Just the name")
        "«Like leaving a dog at the kennels.»":
            label tel_chat_amico_t2_2_5:
            if telefono_minuti_blocco("tel_chat_amico_t2_2_5", "invia", 1):
                return
            $ msg("sara", "Like leaving a dog at the kennels.")
            $ caldo()
            label tel_chat_amico_t2_2_6:
            if telefono_minuti_blocco("tel_chat_amico_t2_2_6", "ricevi", 1):
                return
            $ msg("amico", "Lol. And it looks back at you the whole way down the drive")
        "«Awful.»":
            label tel_chat_amico_t2_2_7:
            if telefono_minuti_blocco("tel_chat_amico_t2_2_7", "invia", 1):
                return
            $ msg("sara", "Awful.")
            label tel_chat_amico_t2_2_8:
            if telefono_minuti_blocco("tel_chat_amico_t2_2_8", "ricevi", 1):
                return
            $ msg("amico", "But you did it. Awful and done is a good combination")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_t2_3:
    label tel_chat_amico_t2_3_1:
    if telefono_minuti_blocco("tel_chat_amico_t2_3_1", "ricevi", 1):
        return
    $ msg("amico", "When I said I'd like to read it I wasn't being polite, by the way")
    label tel_chat_amico_t2_3_2:
    if telefono_minuti_blocco("tel_chat_amico_t2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I know. You don't do polite.»":
            label tel_chat_amico_t2_3_3:
            if telefono_minuti_blocco("tel_chat_amico_t2_3_3", "invia", 1):
                return
            $ msg("sara", "I know. You don't do polite.")
            label tel_chat_amico_t2_3_4:
            if telefono_minuti_blocco("tel_chat_amico_t2_3_4", "ricevi", 1):
                return
            $ msg("amico", "I do for your mum-in-law-to-be. Just about")
        "«I might let you. One day.»":
            label tel_chat_amico_t2_3_5:
            if telefono_minuti_blocco("tel_chat_amico_t2_3_5", "invia", 1):
                return
            $ msg("sara", "I might let you. One day.")
            label tel_chat_amico_t2_3_6:
            if telefono_minuti_blocco("tel_chat_amico_t2_3_6", "ricevi", 1):
                return
            $ msg("amico", "Whenever. And if it's rubbish I'll tell you it's got lovely margins")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The blue packet

label chat_amico_t3:
    label tel_chat_amico_t3_1:
    if telefono_minuti_blocco("tel_chat_amico_t3_1", "invia", 1):
        return
    $ msg("sara", "I'd like it on record that the biscuits on the left were the right ones.")
    return

label chat_amico_t3_1:
    label tel_chat_amico_t3_1_1:
    if telefono_minuti_blocco("tel_chat_amico_t3_1_1", "ricevi", 1):
        return
    $ msg("amico", "Objection. You picked them up without looking")
    label tel_chat_amico_t3_1_2:
    if telefono_minuti_blocco("tel_chat_amico_t3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Because I trusted you.»":
            label tel_chat_amico_t3_1_3:
            if telefono_minuti_blocco("tel_chat_amico_t3_1_3", "invia", 1):
                return
            $ msg("sara", "Because I trusted you.")
            $ caldo()
            label tel_chat_amico_t3_1_4:
            if telefono_minuti_blocco("tel_chat_amico_t3_1_4", "ricevi", 1):
                return
            $ msg("amico", "Lol. Nobody's ever trusted me with a biscuit")
        "«My hand knew.»":
            label tel_chat_amico_t3_1_5:
            if telefono_minuti_blocco("tel_chat_amico_t3_1_5", "invia", 1):
                return
            $ msg("sara", "My hand knew.")
            label tel_chat_amico_t3_1_6:
            if telefono_minuti_blocco("tel_chat_amico_t3_1_6", "ricevi", 1):
                return
            $ msg("amico", "You can't say «my hand knew» in a court of law")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_t3_2:
    label tel_chat_amico_t3_2_1:
    if telefono_minuti_blocco("tel_chat_amico_t3_2_1", "ricevi", 1):
        return
    $ msg("amico", "[nome_compagno] ate the last one, you know. I had my eye on it. He saw me looking and ate it in two goes")
    label tel_chat_amico_t3_2_2:
    if telefono_minuti_blocco("tel_chat_amico_t3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«He does that when he's happy.»":
            label tel_chat_amico_t3_2_3:
            if telefono_minuti_blocco("tel_chat_amico_t3_2_3", "invia", 1):
                return
            $ msg("sara", "He does that when he's happy.")
            label tel_chat_amico_t3_2_4:
            if telefono_minuti_blocco("tel_chat_amico_t3_2_4", "ricevi", 1):
                return
            $ msg("amico", "I know. Twenty years I've been losing biscuits to that man")
        "«I was saving it for you.»":
            label tel_chat_amico_t3_2_5:
            if telefono_minuti_blocco("tel_chat_amico_t3_2_5", "invia", 1):
                return
            $ msg("sara", "I was saving it for you.")
            $ caldo()
            label tel_chat_amico_t3_2_6:
            if telefono_minuti_blocco("tel_chat_amico_t3_2_6", "ricevi", 1):
                return
            $ msg("amico", "Don't tell me that now! It's gone, Sara. I'm grieving")
        "«You should've been quicker.»":
            label tel_chat_amico_t3_2_7:
            if telefono_minuti_blocco("tel_chat_amico_t3_2_7", "invia", 1):
                return
            $ msg("sara", "You should've been quicker.")
            label tel_chat_amico_t3_2_8:
            if telefono_minuti_blocco("tel_chat_amico_t3_2_8", "ricevi", 1):
                return
            $ msg("amico", "Story of my life")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_t3_3:
    label tel_chat_amico_t3_3_1:
    if telefono_minuti_blocco("tel_chat_amico_t3_3_1", "ricevi", 1):
        return
    $ msg("amico", "It was a good night though. I like it round yours. It's loud in the right way")
    label tel_chat_amico_t3_3_2:
    if telefono_minuti_blocco("tel_chat_amico_t3_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You always stay to do the glasses.»":
            label tel_chat_amico_t3_3_3:
            if telefono_minuti_blocco("tel_chat_amico_t3_3_3", "invia", 1):
                return
            $ msg("sara", "You always stay to do the glasses.")
            label tel_chat_amico_t3_3_4:
            if telefono_minuti_blocco("tel_chat_amico_t3_3_4", "ricevi", 1):
                return
            $ msg("amico", "It's when people talk. Everyone says the real stuff to a tea towel")
        "«Come whenever you want.»":
            label tel_chat_amico_t3_3_5:
            if telefono_minuti_blocco("tel_chat_amico_t3_3_5", "invia", 1):
                return
            $ msg("sara", "Come whenever you want.")
            label tel_chat_amico_t3_3_6:
            if telefono_minuti_blocco("tel_chat_amico_t3_3_6", "ricevi", 1):
                return
            $ msg("amico", "Careful. I'll turn up with a blue packet and a toothbrush")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t3_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_t3_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: un gioco di provocazioni

label chat_amico_c1:
    label tel_chat_amico_c1_1:
    if telefono_minuti_blocco("tel_chat_amico_c1_1", "invia", 1):
        return
    $ msg("sara", "You were staring at me when I was drying up.")
    return

label chat_amico_c1_1:
    label tel_chat_amico_c1_1_1:
    if telefono_minuti_blocco("tel_chat_amico_c1_1_1", "ricevi", 1):
        return
    $ msg("amico", "I was staring at the plate")
    label tel_chat_amico_c1_1_2:
    if telefono_minuti_blocco("tel_chat_amico_c1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I wasn't holding a plate.»":
            label tel_chat_amico_c1_1_3:
            if telefono_minuti_blocco("tel_chat_amico_c1_1_3", "invia", 1):
                return
            $ msg("sara", "I wasn't holding a plate.")
            $ caldo()
            label tel_chat_amico_c1_1_4:
            if telefono_minuti_blocco("tel_chat_amico_c1_1_4", "ricevi", 1):
                return
            $ msg("amico", "...Then I was staring at where the plate should have been")
        "«Which one?»":
            label tel_chat_amico_c1_1_5:
            if telefono_minuti_blocco("tel_chat_amico_c1_1_5", "invia", 1):
                return
            $ msg("sara", "Which one?")
            label tel_chat_amico_c1_1_6:
            if telefono_minuti_blocco("tel_chat_amico_c1_1_6", "ricevi", 1):
                return
            $ msg("amico", "The round one. Lol. Ok. Busted")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_c1_2:
    label tel_chat_amico_c1_2_1:
    if telefono_minuti_blocco("tel_chat_amico_c1_2_1", "ricevi", 1):
        return
    $ msg("amico", "I shouldn't say this. I'm going to put it like a joke so we can both pretend")
    label tel_chat_amico_c1_2_2:
    if telefono_minuti_blocco("tel_chat_amico_c1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Then I'll laugh, so you know it landed.»":
            label tel_chat_amico_c1_2_3:
            if telefono_minuti_blocco("tel_chat_amico_c1_2_3", "invia", 1):
                return
            $ msg("sara", "Then I'll laugh, so you know it landed.")
            $ caldo()
            label tel_chat_amico_c1_2_4:
            if telefono_minuti_blocco("tel_chat_amico_c1_2_4", "ricevi", 1):
                return
            $ msg("amico", "If you weren't his I'd have burnt the dinner just to stay longer")
            sp "It isn't a joke. He's written it like one, and it isn't."
        "«Say it straight.»":
            label tel_chat_amico_c1_2_5:
            if telefono_minuti_blocco("tel_chat_amico_c1_2_5", "invia", 1):
                return
            $ msg("sara", "Say it straight.")
            label tel_chat_amico_c1_2_6:
            if telefono_minuti_blocco("tel_chat_amico_c1_2_6", "ricevi", 1):
                return
            $ msg("amico", "I can't. I've known him too long. Straight's the one way I can't say it")
        "«Then don't, Darius.»":
            label tel_chat_amico_c1_2_7:
            if telefono_minuti_blocco("tel_chat_amico_c1_2_7", "invia", 1):
                return
            $ msg("sara", "Then don't, Darius.")
            $ frena()
            label tel_chat_amico_c1_2_8:
            if telefono_minuti_blocco("tel_chat_amico_c1_2_8", "ricevi", 1):
                return
            $ msg("amico", "Yeah. You're right. Forget it. I'll bring biscuits and behave")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_c1_3:
    label tel_chat_amico_c1_3_1:
    if telefono_minuti_blocco("tel_chat_amico_c1_3_1", "ricevi", 1):
        return
    $ msg("amico", "Are we ok?")
    label tel_chat_amico_c1_3_2:
    if telefono_minuti_blocco("tel_chat_amico_c1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«We're fine. I've kept it somewhere.»":
            label tel_chat_amico_c1_3_3:
            if telefono_minuti_blocco("tel_chat_amico_c1_3_3", "invia", 1):
                return
            $ msg("sara", "We're fine. I've kept it somewhere.")
            label tel_chat_amico_c1_3_4:
            if telefono_minuti_blocco("tel_chat_amico_c1_3_4", "ricevi", 1):
                return
            $ msg("amico", "Where?")
        "«With the coat on the bed.»":
            label tel_chat_amico_c1_3_5:
            if telefono_minuti_blocco("tel_chat_amico_c1_3_5", "invia", 1):
                return
            $ msg("sara", "With the coat on the bed.")
            label tel_chat_amico_c1_3_6:
            if telefono_minuti_blocco("tel_chat_amico_c1_3_6", "ricevi", 1):
                return
            $ msg("amico", "Oh, man. Goodnight, Sara")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: confronti con Josh

label chat_amico_c2:
    label tel_chat_amico_c2_1:
    if telefono_minuti_blocco("tel_chat_amico_c2_1", "invia", 1):
        return
    $ msg("sara", "Do you ever compare yourself with him?")
    return

label chat_amico_c2_1:
    label tel_chat_amico_c2_1_1:
    if telefono_minuti_blocco("tel_chat_amico_c2_1_1", "ricevi", 1):
        return
    $ msg("amico", "Since forever. He got the girl, the job and the good hair. I got tall")
    label tel_chat_amico_c2_1_2:
    if telefono_minuti_blocco("tel_chat_amico_c2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You got the hands.»":
            label tel_chat_amico_c2_1_3:
            if telefono_minuti_blocco("tel_chat_amico_c2_1_3", "invia", 1):
                return
            $ msg("sara", "You got the hands.")
            $ caldo()
            label tel_chat_amico_c2_1_4:
            if telefono_minuti_blocco("tel_chat_amico_c2_1_4", "ricevi", 1):
                return
            $ msg("amico", "Lol what? What's wrong with his hands")
            sp "Nothing. Nothing's wrong with them."
        "«You got the sense of humour.»":
            label tel_chat_amico_c2_1_5:
            if telefono_minuti_blocco("tel_chat_amico_c2_1_5", "invia", 1):
                return
            $ msg("sara", "You got the sense of humour.")
            label tel_chat_amico_c2_1_6:
            if telefono_minuti_blocco("tel_chat_amico_c2_1_6", "ricevi", 1):
                return
            $ msg("amico", "He's funny. He's just funny with a run-up")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_c2_2:
    label tel_chat_amico_c2_2_1:
    if telefono_minuti_blocco("tel_chat_amico_c2_2_1", "ricevi", 1):
        return
    $ msg("amico", "He's the best person I know. I need to say that before anything else")
    label tel_chat_amico_c2_2_2:
    if telefono_minuti_blocco("tel_chat_amico_c2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I know. So do I.»":
            label tel_chat_amico_c2_2_3:
            if telefono_minuti_blocco("tel_chat_amico_c2_2_3", "invia", 1):
                return
            $ msg("sara", "I know. So do I.")
            label tel_chat_amico_c2_2_4:
            if telefono_minuti_blocco("tel_chat_amico_c2_2_4", "ricevi", 1):
                return
            $ msg("amico", "Right. So we both know. And here we are at midnight anyway")
        "«Then say the anything else.»":
            label tel_chat_amico_c2_2_5:
            if telefono_minuti_blocco("tel_chat_amico_c2_2_5", "invia", 1):
                return
            $ msg("sara", "Then say the anything else.")
            $ caldo()
            label tel_chat_amico_c2_2_6:
            if telefono_minuti_blocco("tel_chat_amico_c2_2_6", "ricevi", 1):
                return
            $ msg("amico", "He'd have asked what the woman did next. I wanted to know how she felt. That's it. That's the whole difference")
        "«Let's stop while he's still the best person we know.»":
            label tel_chat_amico_c2_2_7:
            if telefono_minuti_blocco("tel_chat_amico_c2_2_7", "invia", 1):
                return
            $ msg("sara", "Let's stop while he's still the best person we know.")
            $ frena()
            label tel_chat_amico_c2_2_8:
            if telefono_minuti_blocco("tel_chat_amico_c2_2_8", "ricevi", 1):
                return
            $ msg("amico", "Yeah. Good place to stop. Night")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_c2_3:
    label tel_chat_amico_c2_3_1:
    if telefono_minuti_blocco("tel_chat_amico_c2_3_1", "ricevi", 1):
        return
    $ msg("amico", "You're hard to be mates with sometimes")
    label tel_chat_amico_c2_3_2:
    if telefono_minuti_blocco("tel_chat_amico_c2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Why?»":
            label tel_chat_amico_c2_3_3:
            if telefono_minuti_blocco("tel_chat_amico_c2_3_3", "invia", 1):
                return
            $ msg("sara", "Why?")
            label tel_chat_amico_c2_3_4:
            if telefono_minuti_blocco("tel_chat_amico_c2_3_4", "ricevi", 1):
                return
            $ msg("amico", "Because you listen with your whole face. A bloke can get ideas")
        "«You could have them quietly.»":
            label tel_chat_amico_c2_3_5:
            if telefono_minuti_blocco("tel_chat_amico_c2_3_5", "invia", 1):
                return
            $ msg("sara", "You could have them quietly.")
            label tel_chat_amico_c2_3_6:
            if telefono_minuti_blocco("tel_chat_amico_c2_3_6", "ricevi", 1):
                return
            $ msg("amico", "I've been having them quietly for ages. I thought you'd noticed")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: una complicità da nascondere

label chat_amico_c3:
    label tel_chat_amico_c3_1:
    if telefono_minuti_blocco("tel_chat_amico_c3_1", "invia", 1):
        return
    $ msg("sara", "I deleted our last chat. Then I felt guilty, and then I missed it.")
    return

label chat_amico_c3_1:
    label tel_chat_amico_c3_1_1:
    if telefono_minuti_blocco("tel_chat_amico_c3_1_1", "ricevi", 1):
        return
    $ msg("amico", "I've still got mine. I'm not proud of it")
    label tel_chat_amico_c3_1_2:
    if telefono_minuti_blocco("tel_chat_amico_c3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Do you read it back?»":
            label tel_chat_amico_c3_1_3:
            if telefono_minuti_blocco("tel_chat_amico_c3_1_3", "invia", 1):
                return
            $ msg("sara", "Do you read it back?")
            $ caldo()
            label tel_chat_amico_c3_1_4:
            if telefono_minuti_blocco("tel_chat_amico_c3_1_4", "ricevi", 1):
                return
            $ msg("amico", "The bit about the coat. Yeah")
        "«Your phone's not locked, Darius.»":
            label tel_chat_amico_c3_1_5:
            if telefono_minuti_blocco("tel_chat_amico_c3_1_5", "invia", 1):
                return
            $ msg("sara", "Your phone's not locked, Darius.")
            label tel_chat_amico_c3_1_6:
            if telefono_minuti_blocco("tel_chat_amico_c3_1_6", "ricevi", 1):
                return
            $ msg("amico", "It is now. First time in my life. My thumb's in shock")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_c3_2:
    label tel_chat_amico_c3_2_1:
    if telefono_minuti_blocco("tel_chat_amico_c3_2_1", "ricevi", 1):
        return
    $ msg("amico", "So what is this? I'm not being funny. For once")
    label tel_chat_amico_c3_2_2:
    if telefono_minuti_blocco("tel_chat_amico_c3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I don't know. I like who I am in it.»":
            label tel_chat_amico_c3_2_3:
            if telefono_minuti_blocco("tel_chat_amico_c3_2_3", "invia", 1):
                return
            $ msg("sara", "I don't know. I like who I am in it.")
            $ caldo()
            label tel_chat_amico_c3_2_4:
            if telefono_minuti_blocco("tel_chat_amico_c3_2_4", "ricevi", 1):
                return
            $ msg("amico", "Yeah. Me too. I'm quicker in it")
        "«Two friends who talk too late.»":
            label tel_chat_amico_c3_2_5:
            if telefono_minuti_blocco("tel_chat_amico_c3_2_5", "invia", 1):
                return
            $ msg("sara", "Two friends who talk too late.")
            label tel_chat_amico_c3_2_6:
            if telefono_minuti_blocco("tel_chat_amico_c3_2_6", "ricevi", 1):
                return
            $ msg("amico", "Too late's about right. In every sense")
        "«A mistake we can still not make.»":
            label tel_chat_amico_c3_2_7:
            if telefono_minuti_blocco("tel_chat_amico_c3_2_7", "invia", 1):
                return
            $ msg("sara", "A mistake we can still not make.")
            $ frena()
            label tel_chat_amico_c3_2_8:
            if telefono_minuti_blocco("tel_chat_amico_c3_2_8", "ricevi", 1):
                return
            $ msg("amico", "Ok. I hear you. I do. I'm putting the kettle on and the phone in the fridge")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_c3_3:
    label tel_chat_amico_c3_3_1:
    if telefono_minuti_blocco("tel_chat_amico_c3_3_1", "ricevi", 1):
        return
    $ msg("amico", "Next Tuesday I'm going to sit at the far end and not look at you once")
    label tel_chat_amico_c3_3_2:
    if telefono_minuti_blocco("tel_chat_amico_c3_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You won't last through the starter.»":
            label tel_chat_amico_c3_3_3:
            if telefono_minuti_blocco("tel_chat_amico_c3_3_3", "invia", 1):
                return
            $ msg("sara", "You won't last through the starter.")
            label tel_chat_amico_c3_3_4:
            if telefono_minuti_blocco("tel_chat_amico_c3_3_4", "ricevi", 1):
                return
            $ msg("amico", "I'll look at the salt. I'll give the salt everything I've got")
        "«Sit next to me.»":
            label tel_chat_amico_c3_3_5:
            if telefono_minuti_blocco("tel_chat_amico_c3_3_5", "invia", 1):
                return
            $ msg("sara", "Sit next to me.")
            label tel_chat_amico_c3_3_6:
            if telefono_minuti_blocco("tel_chat_amico_c3_3_6", "ricevi", 1):
                return
            $ msg("amico", "That'd be so much worse. ...Save me the chair")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c3_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_c3_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: cosa vogliamo davvero

label chat_amico_d1:
    label tel_chat_amico_d1_1:
    if telefono_minuti_blocco("tel_chat_amico_d1_1", "invia", 1):
        return
    $ msg("sara", "I'm not sorry. Are you?")
    return

label chat_amico_d1_1:
    label tel_chat_amico_d1_1_1:
    if telefono_minuti_blocco("tel_chat_amico_d1_1_1", "ricevi", 1):
        return
    $ msg("amico", "I've been trying to be. I've been sat here trying since ten")
    label tel_chat_amico_d1_1_2:
    if telefono_minuti_blocco("tel_chat_amico_d1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And?»":
            label tel_chat_amico_d1_1_3:
            if telefono_minuti_blocco("tel_chat_amico_d1_1_3", "invia", 1):
                return
            $ msg("sara", "And?")
            $ caldo()
            label tel_chat_amico_d1_1_4:
            if telefono_minuti_blocco("tel_chat_amico_d1_1_4", "ricevi", 1):
                return
            $ msg("amico", "And I keep smiling instead. I'm a terrible person with a great memory")
        "«You're allowed not to be.»":
            label tel_chat_amico_d1_1_5:
            if telefono_minuti_blocco("tel_chat_amico_d1_1_5", "invia", 1):
                return
            $ msg("sara", "You're allowed not to be.")
            label tel_chat_amico_d1_1_6:
            if telefono_minuti_blocco("tel_chat_amico_d1_1_6", "ricevi", 1):
                return
            $ msg("amico", "Say that again, slower")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_d1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_d1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_d1_2:
    label tel_chat_amico_d1_2_1:
    if telefono_minuti_blocco("tel_chat_amico_d1_2_1", "ricevi", 1):
        return
    $ msg("amico", "I think about it all the time. Not just the kiss. You. Saying what you want, in a normal voice")
    label tel_chat_amico_d1_2_2:
    if telefono_minuti_blocco("tel_chat_amico_d1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I want you to stop being careful with me.»":
            label tel_chat_amico_d1_2_3:
            if telefono_minuti_blocco("tel_chat_amico_d1_2_3", "invia", 1):
                return
            $ msg("sara", "I want you to stop being careful with me.")
            $ caldo()
            label tel_chat_amico_d1_2_4:
            if telefono_minuti_blocco("tel_chat_amico_d1_2_4", "ricevi", 1):
                return
            $ msg("amico", "I'm twice your size, careful's all I know")
            sp "I know. I've noticed. I've thought about very little else."
        "«I want to hear you. Not the jokes.»":
            label tel_chat_amico_d1_2_5:
            if telefono_minuti_blocco("tel_chat_amico_d1_2_5", "invia", 1):
                return
            $ msg("sara", "I want to hear you. Not the jokes.")
            label tel_chat_amico_d1_2_6:
            if telefono_minuti_blocco("tel_chat_amico_d1_2_6", "ricevi", 1):
                return
            $ msg("amico", "No jokes. Ok. I want my hands in your hair and all night to do it")
        "«I want you to ask.»":
            label tel_chat_amico_d1_2_7:
            if telefono_minuti_blocco("tel_chat_amico_d1_2_7", "invia", 1):
                return
            $ msg("sara", "I want you to ask.")
            label tel_chat_amico_d1_2_8:
            if telefono_minuti_blocco("tel_chat_amico_d1_2_8", "ricevi", 1):
                return
            $ msg("amico", "Can I? ...Yeah. Like that. Just like that")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_d1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_d1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_d1_3:
    label tel_chat_amico_d1_3_1:
    if telefono_minuti_blocco("tel_chat_amico_d1_3_1", "ricevi", 1):
        return
    $ msg("amico", "You've gone quiet. I'm picturing things")
    label tel_chat_amico_d1_3_2:
    if telefono_minuti_blocco("tel_chat_amico_d1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Picture the coat coming off.»":
            label tel_chat_amico_d1_3_3:
            if telefono_minuti_blocco("tel_chat_amico_d1_3_3", "invia", 1):
                return
            $ msg("sara", "Picture the coat coming off.")
            label tel_chat_amico_d1_3_4:
            if telefono_minuti_blocco("tel_chat_amico_d1_3_4", "ricevi", 1):
                return
            $ msg("amico", "I've been picturing that since the café, Sara")
        "«Keep going.»":
            label tel_chat_amico_d1_3_5:
            if telefono_minuti_blocco("tel_chat_amico_d1_3_5", "invia", 1):
                return
            $ msg("sara", "Keep going.")
            label tel_chat_amico_d1_3_6:
            if telefono_minuti_blocco("tel_chat_amico_d1_3_6", "ricevi", 1):
                return
            $ msg("amico", "I will. I've got room, remember? I'm mostly room")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_d1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_d1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: un equilibrio fra tre

label chat_amico_d2:
    label tel_chat_amico_d2_1:
    if telefono_minuti_blocco("tel_chat_amico_d2_1", "invia", 1):
        return
    $ msg("sara", "Can I tell you something that might frighten you?")
    return

label chat_amico_d2_1:
    label tel_chat_amico_d2_1_1:
    if telefono_minuti_blocco("tel_chat_amico_d2_1_1", "ricevi", 1):
        return
    $ msg("amico", "You've been frightening me since the biscuits. Go on")
    label tel_chat_amico_d2_1_2:
    if telefono_minuti_blocco("tel_chat_amico_d2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I don't want to lose either of you.»":
            label tel_chat_amico_d2_1_3:
            if telefono_minuti_blocco("tel_chat_amico_d2_1_3", "invia", 1):
                return
            $ msg("sara", "I don't want to lose either of you.")
            $ caldo()
            label tel_chat_amico_d2_1_4:
            if telefono_minuti_blocco("tel_chat_amico_d2_1_4", "ricevi", 1):
                return
            $ msg("amico", "...Ok. That one I've thought about too")
        "«Sometimes I think about the two of you.»":
            label tel_chat_amico_d2_1_5:
            if telefono_minuti_blocco("tel_chat_amico_d2_1_5", "invia", 1):
                return
            $ msg("sara", "Sometimes I think about the two of you.")
            label tel_chat_amico_d2_1_6:
            if telefono_minuti_blocco("tel_chat_amico_d2_1_6", "ricevi", 1):
                return
            $ msg("amico", "At once? Lol. Sorry. That was nerves. Go on")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_d2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_d2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_d2_2:
    label tel_chat_amico_d2_2_1:
    if telefono_minuti_blocco("tel_chat_amico_d2_2_1", "ricevi", 1):
        return
    $ msg("amico", "How does it go, in your head?")
    label tel_chat_amico_d2_2_2:
    if telefono_minuti_blocco("tel_chat_amico_d2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Nobody's lying. That's the strangest part.»":
            label tel_chat_amico_d2_2_3:
            if telefono_minuti_blocco("tel_chat_amico_d2_2_3", "invia", 1):
                return
            $ msg("sara", "Nobody's lying. That's the strangest part.")
            $ caldo()
            label tel_chat_amico_d2_2_4:
            if telefono_minuti_blocco("tel_chat_amico_d2_2_4", "ricevi", 1):
                return
            $ msg("amico", "Yeah. That's the part I can't picture. The rest I can picture fine")
        "«You're both there, and nobody's the one left outside.»":
            label tel_chat_amico_d2_2_5:
            if telefono_minuti_blocco("tel_chat_amico_d2_2_5", "invia", 1):
                return
            $ msg("sara", "You're both there, and nobody's the one left outside.")
            label tel_chat_amico_d2_2_6:
            if telefono_minuti_blocco("tel_chat_amico_d2_2_6", "ricevi", 1):
                return
            $ msg("amico", "I've always been the one outside. I wouldn't know where to put my feet")
        "«I look at him, and then I look at you, and you're both smiling.»":
            label tel_chat_amico_d2_2_7:
            if telefono_minuti_blocco("tel_chat_amico_d2_2_7", "invia", 1):
                return
            $ msg("sara", "I look at him, and then I look at you, and you're both smiling.")
            label tel_chat_amico_d2_2_8:
            if telefono_minuti_blocco("tel_chat_amico_d2_2_8", "ricevi", 1):
                return
            $ msg("amico", "I'd need a minute. On my own. With my coat on")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_d2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_d2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_d2_3:
    label tel_chat_amico_d2_3_1:
    if telefono_minuti_blocco("tel_chat_amico_d2_3_1", "ricevi", 1):
        return
    $ msg("amico", "It'd have to be his choice as well. All three. Or it's nothing")
    label tel_chat_amico_d2_3_2:
    if telefono_minuti_blocco("tel_chat_amico_d2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I know. I wouldn't want it any other way.»":
            label tel_chat_amico_d2_3_3:
            if telefono_minuti_blocco("tel_chat_amico_d2_3_3", "invia", 1):
                return
            $ msg("sara", "I know. I wouldn't want it any other way.")
            label tel_chat_amico_d2_3_4:
            if telefono_minuti_blocco("tel_chat_amico_d2_3_4", "ricevi", 1):
                return
            $ msg("amico", "Good. Then I can think about it without hating myself")
        "«Think about it with me. Tonight.»":
            label tel_chat_amico_d2_3_5:
            if telefono_minuti_blocco("tel_chat_amico_d2_3_5", "invia", 1):
                return
            $ msg("sara", "Think about it with me. Tonight.")
            label tel_chat_amico_d2_3_6:
            if telefono_minuti_blocco("tel_chat_amico_d2_3_6", "ricevi", 1):
                return
            $ msg("amico", "Yeah. Lie down. I'll tell you how I'd say hello")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_d2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_d2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return
