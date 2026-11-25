## GENERATO da tools/telefono/componi.py: si modifica tools/telefono/capa.txt.

init python:
    discorso("capa_t1", "capa", ESTRANEI, argomento="The website portrait", se="fatto('ep2_d18_resta_barbara')")
    discorso("capa_t2", "capa", ESTRANEI, argomento="The dark lipstick", se="fatto('ep2_d17_glamour')")
    discorso("capa_t3", "capa", ESTRANEI, argomento="The horoscopes", se="fatto('ep1_d10_non_mio_compito')")
    discorso("capa_t4", "capa", CONOSCENTI, argomento="The armchair", se="fatto('barbara_missione_02_fatta')")
    discorso("capa_t5", "capa", CONOSCENTI, argomento="What I signed", se="sara_stagista")
    discorso("capa_c1", "capa", COMPLICI, flirt=True)
    discorso("capa_c2", "capa", COMPLICI, flirt=True)
    discorso("capa_c3", "capa", COMPLICI, flirt=True)
    discorso("capa_d1", "capa", INTIMI, flirt=True)
    discorso("capa_d2", "capa", INTIMI, flirt=True)


## --- The website portrait

label chat_capa_t1:
    label tel_chat_capa_t1_1:
    if telefono_minuti_blocco("tel_chat_capa_t1_1", "invia", 1):
        return
    $ msg("sara", "Is the portrait online yet? I'm afraid to look.")
    return

label chat_capa_t1_entrata:
    label tel_chat_capa_t1_entrata_1:
    if telefono_minuti_blocco("tel_chat_capa_t1_entrata_1", "ricevi", 1):
        return
    $ msg("capa", "Your face is on my newspaper.")
    label tel_chat_capa_t1_entrata_2:
    if telefono_minuti_blocco("tel_chat_capa_t1_entrata_2", "invia", 1):
        return
    $ msg("sara", "The portrait? I'm afraid to look.")
    return

label chat_capa_t1_1:
    label tel_chat_capa_t1_1_1:
    if telefono_minuti_blocco("tel_chat_capa_t1_1_1", "ricevi", 1):
        return
    $ msg("capa", "It's been up since nine. I've looked for you.")
    label tel_chat_capa_t1_1_2:
    if telefono_minuti_blocco("tel_chat_capa_t1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And?»":
            label tel_chat_capa_t1_1_3:
            if telefono_minuti_blocco("tel_chat_capa_t1_1_3", "invia", 1):
                return
            $ msg("sara", "And?")
            $ caldo()
            label tel_chat_capa_t1_1_4:
            if telefono_minuti_blocco("tel_chat_capa_t1_1_4", "ricevi", 1):
                return
            $ msg("capa", "You look like a woman who knows something. Nobody needs to find out what.")
        "«Is it too late to change it?»":
            label tel_chat_capa_t1_1_5:
            if telefono_minuti_blocco("tel_chat_capa_t1_1_5", "invia", 1):
                return
            $ msg("sara", "Is it too late to change it?")
            label tel_chat_capa_t1_1_6:
            if telefono_minuti_blocco("tel_chat_capa_t1_1_6", "ricevi", 1):
                return
            $ msg("capa", "It was too late when I chose it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_t1_2:
    label tel_chat_capa_t1_2_1:
    if telefono_minuti_blocco("tel_chat_capa_t1_2_1", "ricevi", 1):
        return
    $ msg("capa", "You picked the first one. Before you were posing. Do you know why that interested me?")
    label tel_chat_capa_t1_2_2:
    if telefono_minuti_blocco("tel_chat_capa_t1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Because I look like myself.»":
            label tel_chat_capa_t1_2_3:
            if telefono_minuti_blocco("tel_chat_capa_t1_2_3", "invia", 1):
                return
            $ msg("sara", "Because I look like myself.")
            label tel_chat_capa_t1_2_4:
            if telefono_minuti_blocco("tel_chat_capa_t1_2_4", "ricevi", 1):
                return
            $ msg("capa", "Because you recognised yourself. Most women choose the photograph of somebody else.")
        "«Because you'd have picked it too.»":
            label tel_chat_capa_t1_2_5:
            if telefono_minuti_blocco("tel_chat_capa_t1_2_5", "invia", 1):
                return
            $ msg("sara", "Because you'd have picked it too.")
            $ caldo()
            label tel_chat_capa_t1_2_6:
            if telefono_minuti_blocco("tel_chat_capa_t1_2_6", "ricevi", 1):
                return
            $ msg("capa", "Good girl. Never say a thing like that unless it's true. This one was.")
        "«There was a sixth one.»":
            label tel_chat_capa_t1_2_7:
            if telefono_minuti_blocco("tel_chat_capa_t1_2_7", "invia", 1):
                return
            $ msg("sara", "There was a sixth one.")
            label tel_chat_capa_t1_2_8:
            if telefono_minuti_blocco("tel_chat_capa_t1_2_8", "ricevi", 1):
                return
            $ msg("capa", "Was there? I only remember laying out five.")
            sp "She turned it face down. I saw her do it."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_t1_3:
    label tel_chat_capa_t1_3_1:
    if telefono_minuti_blocco("tel_chat_capa_t1_3_1", "ricevi", 1):
        return
    $ msg("capa", "Roberta has asked me whether you've done something with your hair. You haven't. You've done something with your chin.")
    label tel_chat_capa_t1_3_2:
    if telefono_minuti_blocco("tel_chat_capa_t1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Is that good?»":
            label tel_chat_capa_t1_3_3:
            if telefono_minuti_blocco("tel_chat_capa_t1_3_3", "invia", 1):
                return
            $ msg("sara", "Is that good?")
            label tel_chat_capa_t1_3_4:
            if telefono_minuti_blocco("tel_chat_capa_t1_3_4", "ricevi", 1):
                return
            $ msg("capa", "It's up. Keep it there. I've told people it's always been like that.")
        "«I'll lower it, then.»":
            label tel_chat_capa_t1_3_5:
            if telefono_minuti_blocco("tel_chat_capa_t1_3_5", "invia", 1):
                return
            $ msg("sara", "I'll lower it, then.")
            label tel_chat_capa_t1_3_6:
            if telefono_minuti_blocco("tel_chat_capa_t1_3_6", "ricevi", 1):
                return
            $ msg("capa", "You'll do nothing of the kind, darling. It took me six weeks.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The dark lipstick

label chat_capa_t2:
    label tel_chat_capa_t2_1:
    if telefono_minuti_blocco("tel_chat_capa_t2_1", "invia", 1):
        return
    $ msg("sara", "What was that lipstick called? The dark one?")
    return

label chat_capa_t2_entrata:
    label tel_chat_capa_t2_entrata_1:
    if telefono_minuti_blocco("tel_chat_capa_t2_entrata_1", "ricevi", 1):
        return
    $ msg("capa", "I passed your colour in a window today.")
    label tel_chat_capa_t2_entrata_2:
    if telefono_minuti_blocco("tel_chat_capa_t2_entrata_2", "invia", 1):
        return
    $ msg("sara", "The dark lipstick? What was it called?")
    return

label chat_capa_t2_1:
    label tel_chat_capa_t2_1_1:
    if telefono_minuti_blocco("tel_chat_capa_t2_1_1", "ricevi", 1):
        return
    $ msg("capa", "Why? Have you come to your senses?")
    label tel_chat_capa_t2_1_2:
    if telefono_minuti_blocco("tel_chat_capa_t2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I keep seeing it in shop windows.»":
            label tel_chat_capa_t2_1_3:
            if telefono_minuti_blocco("tel_chat_capa_t2_1_3", "invia", 1):
                return
            $ msg("sara", "I keep seeing it in shop windows.")
            $ caldo()
            label tel_chat_capa_t2_1_4:
            if telefono_minuti_blocco("tel_chat_capa_t2_1_4", "ricevi", 1):
                return
            $ msg("capa", "It sees you too. Buy it on a weekday. Never on a Saturday. One buys sensibly on Saturdays.")
        "«I'm only curious.»":
            label tel_chat_capa_t2_1_5:
            if telefono_minuti_blocco("tel_chat_capa_t2_1_5", "invia", 1):
                return
            $ msg("sara", "I'm only curious.")
            label tel_chat_capa_t2_1_6:
            if telefono_minuti_blocco("tel_chat_capa_t2_1_6", "ricevi", 1):
                return
            $ msg("capa", "Curiosity is how it starts. Then one owns four.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_t2_2:
    label tel_chat_capa_t2_2_1:
    if telefono_minuti_blocco("tel_chat_capa_t2_2_1", "ricevi", 1):
        return
    $ msg("capa", "You'd always put it back, you said. Who told you it wasn't for you?")
    label tel_chat_capa_t2_2_2:
    if telefono_minuti_blocco("tel_chat_capa_t2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Nobody. I just assumed.»":
            label tel_chat_capa_t2_2_3:
            if telefono_minuti_blocco("tel_chat_capa_t2_2_3", "invia", 1):
                return
            $ msg("sara", "Nobody. I just assumed.")
            label tel_chat_capa_t2_2_4:
            if telefono_minuti_blocco("tel_chat_capa_t2_2_4", "ricevi", 1):
                return
            $ msg("capa", "Then you can just stop.")
        "«My mother, I think.»":
            label tel_chat_capa_t2_2_5:
            if telefono_minuti_blocco("tel_chat_capa_t2_2_5", "invia", 1):
                return
            $ msg("sara", "My mother, I think.")
            label tel_chat_capa_t2_2_6:
            if telefono_minuti_blocco("tel_chat_capa_t2_2_6", "ricevi", 1):
                return
            $ msg("capa", "Mothers protect us from everything. Including mirrors.")
        "«Me.»":
            label tel_chat_capa_t2_2_7:
            if telefono_minuti_blocco("tel_chat_capa_t2_2_7", "invia", 1):
                return
            $ msg("sara", "Me.")
            $ caldo()
            label tel_chat_capa_t2_2_8:
            if telefono_minuti_blocco("tel_chat_capa_t2_2_8", "ricevi", 1):
                return
            $ msg("capa", "Well. At least you know where she lives.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_t2_3:
    label tel_chat_capa_t2_3_1:
    if telefono_minuti_blocco("tel_chat_capa_t2_3_1", "ricevi", 1):
        return
    $ msg("capa", "Come in wearing it on Monday. I shan't say a word.")
    label tel_chat_capa_t2_3_2:
    if telefono_minuti_blocco("tel_chat_capa_t2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You'll say a word.»":
            label tel_chat_capa_t2_3_3:
            if telefono_minuti_blocco("tel_chat_capa_t2_3_3", "invia", 1):
                return
            $ msg("sara", "You'll say a word.")
            label tel_chat_capa_t2_3_4:
            if telefono_minuti_blocco("tel_chat_capa_t2_3_4", "ricevi", 1):
                return
            $ msg("capa", "One. I'm choosing it now.")
        "«I'd feel like I was pretending.»":
            label tel_chat_capa_t2_3_5:
            if telefono_minuti_blocco("tel_chat_capa_t2_3_5", "invia", 1):
                return
            $ msg("sara", "I'd feel like I was pretending.")
            label tel_chat_capa_t2_3_6:
            if telefono_minuti_blocco("tel_chat_capa_t2_3_6", "ricevi", 1):
                return
            $ msg("capa", "Everyone's pretending, darling. The trick is to pretend upwards.")
        "«I'd rather not. Not to the office.»":
            label tel_chat_capa_t2_3_7:
            if telefono_minuti_blocco("tel_chat_capa_t2_3_7", "invia", 1):
                return
            $ msg("sara", "I'd rather not. Not to the office.")
            label tel_chat_capa_t2_3_8:
            if telefono_minuti_blocco("tel_chat_capa_t2_3_8", "ricevi", 1):
                return
            $ msg("capa", "Then wear it home. I only want to know it's out of the shop.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The horoscopes

label chat_capa_t3:
    label tel_chat_capa_t3_1:
    if telefono_minuti_blocco("tel_chat_capa_t3_1", "invia", 1):
        return
    $ msg("sara", "You said you like it when I bite. I've been wondering if you meant it.")
    return

label chat_capa_t3_1:
    label tel_chat_capa_t3_1_1:
    if telefono_minuti_blocco("tel_chat_capa_t3_1_1", "ricevi", 1):
        return
    $ msg("capa", "I never say things to fill the air. That's what the staff are for.")
    label tel_chat_capa_t3_1_2:
    if telefono_minuti_blocco("tel_chat_capa_t3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Then I'd like to stop doing horoscopes.»":
            label tel_chat_capa_t3_1_3:
            if telefono_minuti_blocco("tel_chat_capa_t3_1_3", "invia", 1):
                return
            $ msg("sara", "Then I'd like to stop doing horoscopes.")
            $ caldo()
            label tel_chat_capa_t3_1_4:
            if telefono_minuti_blocco("tel_chat_capa_t3_1_4", "ricevi", 1):
                return
            $ msg("capa", "There! Teeth. You may stop in a month.")
        "«I was rude.»":
            label tel_chat_capa_t3_1_5:
            if telefono_minuti_blocco("tel_chat_capa_t3_1_5", "invia", 1):
                return
            $ msg("sara", "I was rude.")
            label tel_chat_capa_t3_1_6:
            if telefono_minuti_blocco("tel_chat_capa_t3_1_6", "ricevi", 1):
                return
            $ msg("capa", "You were polite with a knife in it. It's my favourite kind.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_t3_2:
    label tel_chat_capa_t3_2_1:
    if telefono_minuti_blocco("tel_chat_capa_t3_2_1", "ricevi", 1):
        return
    $ msg("capa", "Do you know how many people in this building have told me something wasn't their job?")
    label tel_chat_capa_t3_2_2:
    if telefono_minuti_blocco("tel_chat_capa_t3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Two?»":
            label tel_chat_capa_t3_2_3:
            if telefono_minuti_blocco("tel_chat_capa_t3_2_3", "invia", 1):
                return
            $ msg("sara", "Two?")
            label tel_chat_capa_t3_2_4:
            if telefono_minuti_blocco("tel_chat_capa_t3_2_4", "ricevi", 1):
                return
            $ msg("capa", "You. The other one was a plumber.")
        "«More than one, I hope.»":
            label tel_chat_capa_t3_2_5:
            if telefono_minuti_blocco("tel_chat_capa_t3_2_5", "invia", 1):
                return
            $ msg("sara", "More than one, I hope.")
            $ caldo()
            label tel_chat_capa_t3_2_6:
            if telefono_minuti_blocco("tel_chat_capa_t3_2_6", "ricevi", 1):
                return
            $ msg("capa", "None who stayed. You stayed. And you handed them in at ten to four.")
        "«What happened to them?»":
            label tel_chat_capa_t3_2_7:
            if telefono_minuti_blocco("tel_chat_capa_t3_2_7", "invia", 1):
                return
            $ msg("sara", "What happened to them?")
            label tel_chat_capa_t3_2_8:
            if telefono_minuti_blocco("tel_chat_capa_t3_2_8", "ricevi", 1):
                return
            $ msg("capa", "They're very happy, I'm told. In smaller buildings.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_t3_3:
    label tel_chat_capa_t3_3_1:
    if telefono_minuti_blocco("tel_chat_capa_t3_3_1", "ricevi", 1):
        return
    $ msg("capa", "They're good, by the way. The horoscopes. Somebody rang to ask who Madame Celeste was.")
    label tel_chat_capa_t3_3_2:
    if telefono_minuti_blocco("tel_chat_capa_t3_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What did you say?»":
            label tel_chat_capa_t3_3_3:
            if telefono_minuti_blocco("tel_chat_capa_t3_3_3", "invia", 1):
                return
            $ msg("sara", "What did you say?")
            label tel_chat_capa_t3_3_4:
            if telefono_minuti_blocco("tel_chat_capa_t3_3_4", "ricevi", 1):
                return
            $ msg("capa", "That she's young, and that she's mine.")
            sp "Hers. She says it the way you'd say it of a chair."
        "«Please don't tell anyone.»":
            label tel_chat_capa_t3_3_5:
            if telefono_minuti_blocco("tel_chat_capa_t3_3_5", "invia", 1):
                return
            $ msg("sara", "Please don't tell anyone.")
            label tel_chat_capa_t3_3_6:
            if telefono_minuti_blocco("tel_chat_capa_t3_3_6", "ricevi", 1):
                return
            $ msg("capa", "I'd sooner sell the building. Back to work, darling.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t3_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t3_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The armchair

label chat_capa_t4:
    label tel_chat_capa_t4_1:
    if telefono_minuti_blocco("tel_chat_capa_t4_1", "invia", 1):
        return
    $ msg("sara", "How are your shoulders?")
    return

label chat_capa_t4_entrata:
    label tel_chat_capa_t4_entrata_1:
    if telefono_minuti_blocco("tel_chat_capa_t4_entrata_1", "ricevi", 1):
        return
    $ msg("capa", "I have slept.")
    label tel_chat_capa_t4_entrata_2:
    if telefono_minuti_blocco("tel_chat_capa_t4_entrata_2", "invia", 1):
        return
    $ msg("sara", "How are your shoulders?")
    return

label chat_capa_t4_1:
    label tel_chat_capa_t4_1_1:
    if telefono_minuti_blocco("tel_chat_capa_t4_1_1", "ricevi", 1):
        return
    $ msg("capa", "Where you left them. Lower than they've been since March.")
    label tel_chat_capa_t4_1_2:
    if telefono_minuti_blocco("tel_chat_capa_t4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I could feel something give.»":
            label tel_chat_capa_t4_1_3:
            if telefono_minuti_blocco("tel_chat_capa_t4_1_3", "invia", 1):
                return
            $ msg("sara", "I could feel something give.")
            $ caldo()
            label tel_chat_capa_t4_1_4:
            if telefono_minuti_blocco("tel_chat_capa_t4_1_4", "ricevi", 1):
                return
            $ msg("capa", "So could I. I hadn't authorised it.")
        "«I was afraid of hurting you.»":
            label tel_chat_capa_t4_1_5:
            if telefono_minuti_blocco("tel_chat_capa_t4_1_5", "invia", 1):
                return
            $ msg("sara", "I was afraid of hurting you.")
            label tel_chat_capa_t4_1_6:
            if telefono_minuti_blocco("tel_chat_capa_t4_1_6", "ricevi", 1):
                return
            $ msg("capa", "Nobody's hurt me in years. They don't press hard enough.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_t4_2:
    label tel_chat_capa_t4_2_1:
    if telefono_minuti_blocco("tel_chat_capa_t4_2_1", "ricevi", 1):
        return
    $ msg("capa", "You asked me nothing, for ten minutes. Do you know how rare that is?")
    label tel_chat_capa_t4_2_2:
    if telefono_minuti_blocco("tel_chat_capa_t4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I was thinking about my chapter.»":
            label tel_chat_capa_t4_2_3:
            if telefono_minuti_blocco("tel_chat_capa_t4_2_3", "invia", 1):
                return
            $ msg("sara", "I was thinking about my chapter.")
            label tel_chat_capa_t4_2_4:
            if telefono_minuti_blocco("tel_chat_capa_t4_2_4", "ricevi", 1):
                return
            $ msg("capa", "I know. I could feel it, in your thumbs. The lie's coming along.")
        "«I didn't want it to stop.»":
            label tel_chat_capa_t4_2_5:
            if telefono_minuti_blocco("tel_chat_capa_t4_2_5", "invia", 1):
                return
            $ msg("sara", "I didn't want it to stop.")
            $ caldo()
            label tel_chat_capa_t4_2_6:
            if telefono_minuti_blocco("tel_chat_capa_t4_2_6", "ricevi", 1):
                return
            $ msg("capa", "No. Nor did I, and I've a reputation.")
        "«You held my hand.»":
            label tel_chat_capa_t4_2_7:
            if telefono_minuti_blocco("tel_chat_capa_t4_2_7", "invia", 1):
                return
            $ msg("sara", "You held my hand.")
            label tel_chat_capa_t4_2_8:
            if telefono_minuti_blocco("tel_chat_capa_t4_2_8", "ricevi", 1):
                return
            $ msg("capa", "I was keeping my balance. One can fall out of a chair.")
            sp "Ten seconds. I counted them."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_t4_3:
    label tel_chat_capa_t4_3_1:
    if telefono_minuti_blocco("tel_chat_capa_t4_3_1", "ricevi", 1):
        return
    $ msg("capa", "I'll call you when I need you again. I'm not going to tell you when.")
    label tel_chat_capa_t4_3_2:
    if telefono_minuti_blocco("tel_chat_capa_t4_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'll come.»":
            label tel_chat_capa_t4_3_3:
            if telefono_minuti_blocco("tel_chat_capa_t4_3_3", "invia", 1):
                return
            $ msg("sara", "I'll come.")
            label tel_chat_capa_t4_3_4:
            if telefono_minuti_blocco("tel_chat_capa_t4_3_4", "ricevi", 1):
                return
            $ msg("capa", "I know. That wasn't the question. It was a courtesy.")
        "«And if I'm busy?»":
            label tel_chat_capa_t4_3_5:
            if telefono_minuti_blocco("tel_chat_capa_t4_3_5", "invia", 1):
                return
            $ msg("sara", "And if I'm busy?")
            label tel_chat_capa_t4_3_6:
            if telefono_minuti_blocco("tel_chat_capa_t4_3_6", "ricevi", 1):
                return
            $ msg("capa", "Then you'll say so, and I'll be charming about it. You've seen me be charming.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t4_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t4_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- What I signed

label chat_capa_t5:
    label tel_chat_capa_t5_1:
    if telefono_minuti_blocco("tel_chat_capa_t5_1", "invia", 1):
        return
    $ msg("sara", "I keep thinking about what I signed.")
    return

label chat_capa_t5_1:
    label tel_chat_capa_t5_1_1:
    if telefono_minuti_blocco("tel_chat_capa_t5_1_1", "ricevi", 1):
        return
    $ msg("capa", "With regret? Be quick, I'm between telephone calls.")
    label tel_chat_capa_t5_1_2:
    if telefono_minuti_blocco("tel_chat_capa_t5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«No. With surprise.»":
            label tel_chat_capa_t5_1_3:
            if telefono_minuti_blocco("tel_chat_capa_t5_1_3", "invia", 1):
                return
            $ msg("sara", "No. With surprise.")
            $ caldo()
            label tel_chat_capa_t5_1_4:
            if telefono_minuti_blocco("tel_chat_capa_t5_1_4", "ricevi", 1):
                return
            $ msg("capa", "That's as it should be. A signature ought to startle the hand.")
        "«A little.»":
            label tel_chat_capa_t5_1_5:
            if telefono_minuti_blocco("tel_chat_capa_t5_1_5", "invia", 1):
                return
            $ msg("sara", "A little.")
            label tel_chat_capa_t5_1_6:
            if telefono_minuti_blocco("tel_chat_capa_t5_1_6", "ricevi", 1):
                return
            $ msg("capa", "Then come and say so to my face. I tear things up beautifully. I'd do it without a word.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_t5_2:
    label tel_chat_capa_t5_2_1:
    if telefono_minuti_blocco("tel_chat_capa_t5_2_1", "ricevi", 1):
        return
    $ msg("capa", "I'll tell you what I saw. You read it all. Both sides. And then you put down the pen, and picked it up again.")
    label tel_chat_capa_t5_2_2:
    if telefono_minuti_blocco("tel_chat_capa_t5_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I wanted to be sure it was me doing it.»":
            label tel_chat_capa_t5_2_3:
            if telefono_minuti_blocco("tel_chat_capa_t5_2_3", "invia", 1):
                return
            $ msg("sara", "I wanted to be sure it was me doing it.")
            label tel_chat_capa_t5_2_4:
            if telefono_minuti_blocco("tel_chat_capa_t5_2_4", "ricevi", 1):
                return
            $ msg("capa", "It was. I was watching for anybody else.")
        "«You were very patient.»":
            label tel_chat_capa_t5_2_5:
            if telefono_minuti_blocco("tel_chat_capa_t5_2_5", "invia", 1):
                return
            $ msg("sara", "You were very patient.")
            $ caldo()
            label tel_chat_capa_t5_2_6:
            if telefono_minuti_blocco("tel_chat_capa_t5_2_6", "ricevi", 1):
                return
            $ msg("capa", "I was nothing of the kind. I was holding the edge of the desk.")
        "«You'd already decided I would.»":
            label tel_chat_capa_t5_2_7:
            if telefono_minuti_blocco("tel_chat_capa_t5_2_7", "invia", 1):
                return
            $ msg("sara", "You'd already decided I would.")
            label tel_chat_capa_t5_2_8:
            if telefono_minuti_blocco("tel_chat_capa_t5_2_8", "ricevi", 1):
                return
            $ msg("capa", "I'd hoped, darling. It's a thing I do in private.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t5_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t5_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_t5_3:
    label tel_chat_capa_t5_3_1:
    if telefono_minuti_blocco("tel_chat_capa_t5_3_1", "ricevi", 1):
        return
    $ msg("capa", "It's not a chain, you understand. It's a door with your name on the inside.")
    label tel_chat_capa_t5_3_2:
    if telefono_minuti_blocco("tel_chat_capa_t5_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And I can walk out of it?»":
            label tel_chat_capa_t5_3_3:
            if telefono_minuti_blocco("tel_chat_capa_t5_3_3", "invia", 1):
                return
            $ msg("sara", "And I can walk out of it?")
            label tel_chat_capa_t5_3_4:
            if telefono_minuti_blocco("tel_chat_capa_t5_3_4", "ricevi", 1):
                return
            $ msg("capa", "Whenever you like. That's why it's worth having you in.")
        "«I like that it's only between us.»":
            label tel_chat_capa_t5_3_5:
            if telefono_minuti_blocco("tel_chat_capa_t5_3_5", "invia", 1):
                return
            $ msg("sara", "I like that it's only between us.")
            label tel_chat_capa_t5_3_6:
            if telefono_minuti_blocco("tel_chat_capa_t5_3_6", "ricevi", 1):
                return
            $ msg("capa", "So do I. I've kept it in the good drawer. With the sixth photograph.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t5_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_t5_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: complimenti personali

label chat_capa_c1:
    label tel_chat_capa_c1_1:
    if telefono_minuti_blocco("tel_chat_capa_c1_1", "invia", 1):
        return
    $ msg("sara", "You looked at me for a long time in the meeting today.")
    return

label chat_capa_c1_1:
    label tel_chat_capa_c1_1_1:
    if telefono_minuti_blocco("tel_chat_capa_c1_1_1", "ricevi", 1):
        return
    $ msg("capa", "I was counting buttons. You'd one more done up than yesterday.")
    label tel_chat_capa_c1_1_2:
    if telefono_minuti_blocco("tel_chat_capa_c1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I was cold.»":
            label tel_chat_capa_c1_1_3:
            if telefono_minuti_blocco("tel_chat_capa_c1_1_3", "invia", 1):
                return
            $ msg("sara", "I was cold.")
            $ caldo()
            label tel_chat_capa_c1_1_4:
            if telefono_minuti_blocco("tel_chat_capa_c1_1_4", "ricevi", 1):
                return
            $ msg("capa", "Then I'll see to the heating.")
        "«Did anyone notice?»":
            label tel_chat_capa_c1_1_5:
            if telefono_minuti_blocco("tel_chat_capa_c1_1_5", "invia", 1):
                return
            $ msg("sara", "Did anyone notice?")
            label tel_chat_capa_c1_1_6:
            if telefono_minuti_blocco("tel_chat_capa_c1_1_6", "ricevi", 1):
                return
            $ msg("capa", "Everyone notices what I look at. It's how I run the paper.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_c1_2:
    label tel_chat_capa_c1_2_1:
    if telefono_minuti_blocco("tel_chat_capa_c1_2_1", "ricevi", 1):
        return
    $ msg("capa", "Shall I tell you what I was thinking? You may say no. I'd enjoy that too.")
    label tel_chat_capa_c1_2_2:
    if telefono_minuti_blocco("tel_chat_capa_c1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Tell me.»":
            label tel_chat_capa_c1_2_3:
            if telefono_minuti_blocco("tel_chat_capa_c1_2_3", "invia", 1):
                return
            $ msg("sara", "Tell me.")
            $ caldo()
            label tel_chat_capa_c1_2_4:
            if telefono_minuti_blocco("tel_chat_capa_c1_2_4", "ricevi", 1):
                return
            $ msg("capa", "That you've no idea what you do to a blouse. And that I'd be sorry if you ever found out.")
        "«No.»":
            label tel_chat_capa_c1_2_5:
            if telefono_minuti_blocco("tel_chat_capa_c1_2_5", "invia", 1):
                return
            $ msg("sara", "No.")
            label tel_chat_capa_c1_2_6:
            if telefono_minuti_blocco("tel_chat_capa_c1_2_6", "ricevi", 1):
                return
            $ msg("capa", "Delicious. Say it again tomorrow, in front of Roberta.")
        "«Let's keep it to the paper, Barbara.»":
            label tel_chat_capa_c1_2_7:
            if telefono_minuti_blocco("tel_chat_capa_c1_2_7", "invia", 1):
                return
            $ msg("sara", "Let's keep it to the paper, Barbara.")
            $ frena()
            label tel_chat_capa_c1_2_8:
            if telefono_minuti_blocco("tel_chat_capa_c1_2_8", "ricevi", 1):
                return
            $ msg("capa", "Of course. Page four's yours. Goodbye, darling.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_c1_3:
    label tel_chat_capa_c1_3_1:
    if telefono_minuti_blocco("tel_chat_capa_c1_3_1", "ricevi", 1):
        return
    $ msg("capa", "Wear the green on Thursday.")
    label tel_chat_capa_c1_3_2:
    if telefono_minuti_blocco("tel_chat_capa_c1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Is that an order?»":
            label tel_chat_capa_c1_3_3:
            if telefono_minuti_blocco("tel_chat_capa_c1_3_3", "invia", 1):
                return
            $ msg("sara", "Is that an order?")
            label tel_chat_capa_c1_3_4:
            if telefono_minuti_blocco("tel_chat_capa_c1_3_4", "ricevi", 1):
                return
            $ msg("capa", "It's a wish. I have so few. They tend to come true.")
        "«I was going to anyway.»":
            label tel_chat_capa_c1_3_5:
            if telefono_minuti_blocco("tel_chat_capa_c1_3_5", "invia", 1):
                return
            $ msg("sara", "I was going to anyway.")
            label tel_chat_capa_c1_3_6:
            if telefono_minuti_blocco("tel_chat_capa_c1_3_6", "ricevi", 1):
                return
            $ msg("capa", "I know. I only wanted to have asked.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: la vita privata di Barbara

label chat_capa_c2:
    label tel_chat_capa_c2_1:
    if telefono_minuti_blocco("tel_chat_capa_c2_1", "invia", 1):
        return
    $ msg("sara", "What do you do when you get home?")
    return

label chat_capa_c2_1:
    label tel_chat_capa_c2_1_1:
    if telefono_minuti_blocco("tel_chat_capa_c2_1_1", "ricevi", 1):
        return
    $ msg("capa", "I take my rings off. All of them. Then I'm nobody for an hour. It's heaven.")
    label tel_chat_capa_c2_1_2:
    if telefono_minuti_blocco("tel_chat_capa_c2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'd like to see that.»":
            label tel_chat_capa_c2_1_3:
            if telefono_minuti_blocco("tel_chat_capa_c2_1_3", "invia", 1):
                return
            $ msg("sara", "I'd like to see that.")
            $ caldo()
            label tel_chat_capa_c2_1_4:
            if telefono_minuti_blocco("tel_chat_capa_c2_1_4", "ricevi", 1):
                return
            $ msg("capa", "No one has. My husband used to be in the other room with the football.")
        "«I can't imagine it.»":
            label tel_chat_capa_c2_1_5:
            if telefono_minuti_blocco("tel_chat_capa_c2_1_5", "invia", 1):
                return
            $ msg("sara", "I can't imagine it.")
            label tel_chat_capa_c2_1_6:
            if telefono_minuti_blocco("tel_chat_capa_c2_1_6", "ricevi", 1):
                return
            $ msg("capa", "That's because I've never let you. I'm wondering why I've just started.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_c2_2:
    label tel_chat_capa_c2_2_1:
    if telefono_minuti_blocco("tel_chat_capa_c2_2_1", "ricevi", 1):
        return
    $ msg("capa", "I pour one glass. I put on something that isn't black. I dance a little. Badly.")
    label tel_chat_capa_c2_2_2:
    if telefono_minuti_blocco("tel_chat_capa_c2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You don't do anything badly.»":
            label tel_chat_capa_c2_2_3:
            if telefono_minuti_blocco("tel_chat_capa_c2_2_3", "invia", 1):
                return
            $ msg("sara", "You don't do anything badly.")
            $ caldo()
            label tel_chat_capa_c2_2_4:
            if telefono_minuti_blocco("tel_chat_capa_c2_2_4", "ricevi", 1):
                return
            $ msg("capa", "I do that badly on purpose. It's the only thing all day that isn't a decision.")
        "«On your own?»":
            label tel_chat_capa_c2_2_5:
            if telefono_minuti_blocco("tel_chat_capa_c2_2_5", "invia", 1):
                return
            $ msg("sara", "On your own?")
            label tel_chat_capa_c2_2_6:
            if telefono_minuti_blocco("tel_chat_capa_c2_2_6", "ricevi", 1):
                return
            $ msg("capa", "With a lamp. He leads.")
        "«You don't have to tell me this.»":
            label tel_chat_capa_c2_2_7:
            if telefono_minuti_blocco("tel_chat_capa_c2_2_7", "invia", 1):
                return
            $ msg("sara", "You don't have to tell me this.")
            $ frena()
            label tel_chat_capa_c2_2_8:
            if telefono_minuti_blocco("tel_chat_capa_c2_2_8", "ricevi", 1):
                return
            $ msg("capa", "No. I don't have to do anything. How restful of you to remind me. Good night.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_c2_3:
    label tel_chat_capa_c2_3_1:
    if telefono_minuti_blocco("tel_chat_capa_c2_3_1", "ricevi", 1):
        return
    $ msg("capa", "If you ever repeat it, I'll deny the lamp.")
    label tel_chat_capa_c2_3_2:
    if telefono_minuti_blocco("tel_chat_capa_c2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'd never.»":
            label tel_chat_capa_c2_3_3:
            if telefono_minuti_blocco("tel_chat_capa_c2_3_3", "invia", 1):
                return
            $ msg("sara", "I'd never.")
            label tel_chat_capa_c2_3_4:
            if telefono_minuti_blocco("tel_chat_capa_c2_3_4", "ricevi", 1):
                return
            $ msg("capa", "I know. You've a face like a locked drawer. I do like knowing what's in it.")
        "«Next time, put on something that isn't black and think of me.»":
            label tel_chat_capa_c2_3_5:
            if telefono_minuti_blocco("tel_chat_capa_c2_3_5", "invia", 1):
                return
            $ msg("sara", "Next time, put on something that isn't black and think of me.")
            label tel_chat_capa_c2_3_6:
            if telefono_minuti_blocco("tel_chat_capa_c2_3_6", "ricevi", 1):
                return
            $ msg("capa", "Darling. What do you suppose I've been doing?")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: fuori dall'ufficio

label chat_capa_c3:
    label tel_chat_capa_c3_1:
    if telefono_minuti_blocco("tel_chat_capa_c3_1", "invia", 1):
        return
    $ msg("sara", "Do you ever go out with people from the paper?")
    return

label chat_capa_c3_1:
    label tel_chat_capa_c3_1_1:
    if telefono_minuti_blocco("tel_chat_capa_c3_1_1", "ricevi", 1):
        return
    $ msg("capa", "I go to dinners. People from the paper are under the same roof at the time.")
    label tel_chat_capa_c3_1_2:
    if telefono_minuti_blocco("tel_chat_capa_c3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's not the same thing.»":
            label tel_chat_capa_c3_1_3:
            if telefono_minuti_blocco("tel_chat_capa_c3_1_3", "invia", 1):
                return
            $ msg("sara", "That's not the same thing.")
            $ caldo()
            label tel_chat_capa_c3_1_4:
            if telefono_minuti_blocco("tel_chat_capa_c3_1_4", "ricevi", 1):
                return
            $ msg("capa", "No. The other thing I haven't done in years. I might have lost the recipe.")
        "«I'd be terrified.»":
            label tel_chat_capa_c3_1_5:
            if telefono_minuti_blocco("tel_chat_capa_c3_1_5", "invia", 1):
                return
            $ msg("sara", "I'd be terrified.")
            label tel_chat_capa_c3_1_6:
            if telefono_minuti_blocco("tel_chat_capa_c3_1_6", "ricevi", 1):
                return
            $ msg("capa", "Yes. You'd wear it very well.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_c3_2:
    label tel_chat_capa_c3_2_1:
    if telefono_minuti_blocco("tel_chat_capa_c3_2_1", "ricevi", 1):
        return
    $ msg("capa", "There's a restaurant with no prices on the menu. The one they hand the lady.")
    label tel_chat_capa_c3_2_2:
    if telefono_minuti_blocco("tel_chat_capa_c3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Which of us would be the lady?»":
            label tel_chat_capa_c3_2_3:
            if telefono_minuti_blocco("tel_chat_capa_c3_2_3", "invia", 1):
                return
            $ msg("sara", "Which of us would be the lady?")
            label tel_chat_capa_c3_2_4:
            if telefono_minuti_blocco("tel_chat_capa_c3_2_4", "ricevi", 1):
                return
            $ msg("capa", "We'd both be handed the other one, and I'd enjoy his face.")
        "«What would we talk about?»":
            label tel_chat_capa_c3_2_5:
            if telefono_minuti_blocco("tel_chat_capa_c3_2_5", "invia", 1):
                return
            $ msg("sara", "What would we talk about?")
            $ caldo()
            label tel_chat_capa_c3_2_6:
            if telefono_minuti_blocco("tel_chat_capa_c3_2_6", "ricevi", 1):
                return
            $ msg("capa", "You. I'd say hardly anything. You'd hear yourself getting cleverer.")
        "«I'd better not, Barbara.»":
            label tel_chat_capa_c3_2_7:
            if telefono_minuti_blocco("tel_chat_capa_c3_2_7", "invia", 1):
                return
            $ msg("sara", "I'd better not, Barbara.")
            $ frena()
            label tel_chat_capa_c3_2_8:
            if telefono_minuti_blocco("tel_chat_capa_c3_2_8", "ricevi", 1):
                return
            $ msg("capa", "Then you've better sense than I have. It won't happen often. Good night.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_c3_3:
    label tel_chat_capa_c3_3_1:
    if telefono_minuti_blocco("tel_chat_capa_c3_3_1", "ricevi", 1):
        return
    $ msg("capa", "I'd send a car. I don't like you on buses. They don't deserve you.")
    label tel_chat_capa_c3_3_2:
    if telefono_minuti_blocco("tel_chat_capa_c3_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'd come by bus anyway.»":
            label tel_chat_capa_c3_3_3:
            if telefono_minuti_blocco("tel_chat_capa_c3_3_3", "invia", 1):
                return
            $ msg("sara", "I'd come by bus anyway.")
            label tel_chat_capa_c3_3_4:
            if telefono_minuti_blocco("tel_chat_capa_c3_3_4", "ricevi", 1):
                return
            $ msg("capa", "Of course you would. And I'd be standing at the stop, in these shoes, like a fool.")
        "«Seven o'clock?»":
            label tel_chat_capa_c3_3_5:
            if telefono_minuti_blocco("tel_chat_capa_c3_3_5", "invia", 1):
                return
            $ msg("sara", "Seven o'clock?")
            label tel_chat_capa_c3_3_6:
            if telefono_minuti_blocco("tel_chat_capa_c3_3_6", "ricevi", 1):
                return
            $ msg("capa", "I said «if», darling. ...Half past. I need the hour with no rings.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c3_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_c3_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: ammettere un'attrazione

label chat_capa_d1:
    label tel_chat_capa_d1_1:
    if telefono_minuti_blocco("tel_chat_capa_d1_1", "invia", 1):
        return
    $ msg("sara", "I've still got your lipstick on my cuff.")
    return

label chat_capa_d1_1:
    label tel_chat_capa_d1_1_1:
    if telefono_minuti_blocco("tel_chat_capa_d1_1_1", "ricevi", 1):
        return
    $ msg("capa", "Leave it. I like to think of it going through the wash with everyone's shirts.")
    label tel_chat_capa_d1_1_2:
    if telefono_minuti_blocco("tel_chat_capa_d1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I haven't washed it.»":
            label tel_chat_capa_d1_1_3:
            if telefono_minuti_blocco("tel_chat_capa_d1_1_3", "invia", 1):
                return
            $ msg("sara", "I haven't washed it.")
            $ caldo()
            label tel_chat_capa_d1_1_4:
            if telefono_minuti_blocco("tel_chat_capa_d1_1_4", "ricevi", 1):
                return
            $ msg("capa", "No. I rather thought you'd be the kind.")
        "«What do I tell people?»":
            label tel_chat_capa_d1_1_5:
            if telefono_minuti_blocco("tel_chat_capa_d1_1_5", "invia", 1):
                return
            $ msg("sara", "What do I tell people?")
            label tel_chat_capa_d1_1_6:
            if telefono_minuti_blocco("tel_chat_capa_d1_1_6", "ricevi", 1):
                return
            $ msg("capa", "That you're an untidy eater.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_d1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_d1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_d1_2:
    label tel_chat_capa_d1_2_1:
    if telefono_minuti_blocco("tel_chat_capa_d1_2_1", "ricevi", 1):
        return
    $ msg("capa", "I'm in my office. The blind is down. I have eleven minutes. Amuse me.")
    label tel_chat_capa_d1_2_2:
    if telefono_minuti_blocco("tel_chat_capa_d1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Where are your hands?»":
            label tel_chat_capa_d1_2_3:
            if telefono_minuti_blocco("tel_chat_capa_d1_2_3", "invia", 1):
                return
            $ msg("sara", "Where are your hands?")
            $ caldo()
            label tel_chat_capa_d1_2_4:
            if telefono_minuti_blocco("tel_chat_capa_d1_2_4", "ricevi", 1):
                return
            $ msg("capa", "On the desk. Where you can see them. Where would you like them?")
            sp "My heart's in my mouth. I'm the one being asked."
        "«Only eleven?»":
            label tel_chat_capa_d1_2_5:
            if telefono_minuti_blocco("tel_chat_capa_d1_2_5", "invia", 1):
                return
            $ msg("sara", "Only eleven?")
            label tel_chat_capa_d1_2_6:
            if telefono_minuti_blocco("tel_chat_capa_d1_2_6", "ricevi", 1):
                return
            $ msg("capa", "Ten, now. You see what your cleverness costs.")
        "«You tell me what to do. I like it when you do.»":
            label tel_chat_capa_d1_2_7:
            if telefono_minuti_blocco("tel_chat_capa_d1_2_7", "invia", 1):
                return
            $ msg("sara", "You tell me what to do. I like it when you do.")
            label tel_chat_capa_d1_2_8:
            if telefono_minuti_blocco("tel_chat_capa_d1_2_8", "ricevi", 1):
                return
            $ msg("capa", "Then sit up. Chin. Now the second button, and take all of a minute over it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_d1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_d1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_d1_3:
    label tel_chat_capa_d1_3_1:
    if telefono_minuti_blocco("tel_chat_capa_d1_3_1", "ricevi", 1):
        return
    $ msg("capa", "Good girl. Not a word. I can hear you not saying it.")
    label tel_chat_capa_d1_3_2:
    if telefono_minuti_blocco("tel_chat_capa_d1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Somebody's coming down the corridor.»":
            label tel_chat_capa_d1_3_3:
            if telefono_minuti_blocco("tel_chat_capa_d1_3_3", "invia", 1):
                return
            $ msg("sara", "Somebody's coming down the corridor.")
            label tel_chat_capa_d1_3_4:
            if telefono_minuti_blocco("tel_chat_capa_d1_3_4", "ricevi", 1):
                return
            $ msg("capa", "Let them. You're reading a message from your editor.")
        "«Was that ten minutes?»":
            label tel_chat_capa_d1_3_5:
            if telefono_minuti_blocco("tel_chat_capa_d1_3_5", "invia", 1):
                return
            $ msg("sara", "Was that ten minutes?")
            label tel_chat_capa_d1_3_6:
            if telefono_minuti_blocco("tel_chat_capa_d1_3_6", "ricevi", 1):
                return
            $ msg("capa", "It was nineteen. I've kept the Mayor waiting. Back to work, darling.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_d1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_d1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: esclusività e dedizione

label chat_capa_d2:
    label tel_chat_capa_d2_1:
    if telefono_minuti_blocco("tel_chat_capa_d2_1", "invia", 1):
        return
    $ msg("sara", "Do you have this with anyone else?")
    return

label chat_capa_d2_1:
    label tel_chat_capa_d2_1_1:
    if telefono_minuti_blocco("tel_chat_capa_d2_1_1", "ricevi", 1):
        return
    $ msg("capa", "What a very good question. Are you asking as my writer, or as my Sara?")
    label tel_chat_capa_d2_1_2:
    if telefono_minuti_blocco("tel_chat_capa_d2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«As your Sara.»":
            label tel_chat_capa_d2_1_3:
            if telefono_minuti_blocco("tel_chat_capa_d2_1_3", "invia", 1):
                return
            $ msg("sara", "As your Sara.")
            $ caldo()
            label tel_chat_capa_d2_1_4:
            if telefono_minuti_blocco("tel_chat_capa_d2_1_4", "ricevi", 1):
                return
            $ msg("capa", "Then no. I've people who adore me. It isn't at all the same.")
        "«As someone who'd mind.»":
            label tel_chat_capa_d2_1_5:
            if telefono_minuti_blocco("tel_chat_capa_d2_1_5", "invia", 1):
                return
            $ msg("sara", "As someone who'd mind.")
            label tel_chat_capa_d2_1_6:
            if telefono_minuti_blocco("tel_chat_capa_d2_1_6", "ricevi", 1):
                return
            $ msg("capa", "Would you? How delicious. Mind a little longer.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_d2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_d2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_d2_2:
    label tel_chat_capa_d2_2_1:
    if telefono_minuti_blocco("tel_chat_capa_d2_2_1", "ricevi", 1):
        return
    $ msg("capa", "I'm going to say something I shall deny. I think about you with my rings off.")
    label tel_chat_capa_d2_2_2:
    if telefono_minuti_blocco("tel_chat_capa_d2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What am I doing, when you think of me?»":
            label tel_chat_capa_d2_2_3:
            if telefono_minuti_blocco("tel_chat_capa_d2_2_3", "invia", 1):
                return
            $ msg("sara", "What am I doing, when you think of me?")
            $ caldo()
            label tel_chat_capa_d2_2_4:
            if telefono_minuti_blocco("tel_chat_capa_d2_2_4", "ricevi", 1):
                return
            $ msg("capa", "What you're told. And then, at the end, something I didn't ask for.")
        "«Tell me what you'd ask for.»":
            label tel_chat_capa_d2_2_5:
            if telefono_minuti_blocco("tel_chat_capa_d2_2_5", "invia", 1):
                return
            $ msg("sara", "Tell me what you'd ask for.")
            label tel_chat_capa_d2_2_6:
            if telefono_minuti_blocco("tel_chat_capa_d2_2_6", "ricevi", 1):
                return
            $ msg("capa", "Your hair down. Your eyes open. And every single thing said aloud.")
        "«I'm on my knees just reading that.»":
            label tel_chat_capa_d2_2_7:
            if telefono_minuti_blocco("tel_chat_capa_d2_2_7", "invia", 1):
                return
            $ msg("sara", "I'm on my knees just reading that.")
            label tel_chat_capa_d2_2_8:
            if telefono_minuti_blocco("tel_chat_capa_d2_2_8", "ricevi", 1):
                return
            $ msg("capa", "I hadn't asked for that. You see? That's precisely what I mean. Stay there.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_d2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_d2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_d2_3:
    label tel_chat_capa_d2_3_1:
    if telefono_minuti_blocco("tel_chat_capa_d2_3_1", "ricevi", 1):
        return
    $ msg("capa", "You may stop, darling. You've been very thorough.")
    label tel_chat_capa_d2_3_2:
    if telefono_minuti_blocco("tel_chat_capa_d2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I don't want to stop.»":
            label tel_chat_capa_d2_3_3:
            if telefono_minuti_blocco("tel_chat_capa_d2_3_3", "invia", 1):
                return
            $ msg("sara", "I don't want to stop.")
            label tel_chat_capa_d2_3_4:
            if telefono_minuti_blocco("tel_chat_capa_d2_3_4", "ricevi", 1):
                return
            $ msg("capa", "No. I'm stopping so that you'll want to tomorrow. It's called editing.")
        "«And you? Are you all right?»":
            label tel_chat_capa_d2_3_5:
            if telefono_minuti_blocco("tel_chat_capa_d2_3_5", "invia", 1):
                return
            $ msg("sara", "And you? Are you all right?")
            label tel_chat_capa_d2_3_6:
            if telefono_minuti_blocco("tel_chat_capa_d2_3_6", "ricevi", 1):
                return
            $ msg("capa", "Nobody's ever asked me that afterwards. I'll need a moment. Good night, Sara.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_d2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_d2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return
