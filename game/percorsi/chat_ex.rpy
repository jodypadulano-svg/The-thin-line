## =============================================================================
## JACOB (chiave "ex") — discorsi al telefono: introduzione, A, B
## =============================================================================
## Tono (Q&A 18/11/2026): scrive di notte, minuscole, sicuro, sfacciato ma in A
## SOLO nostalgia. Allusioni al passato fisico da B: ricordare con un sorriso =
## calda, lasciar cadere = neutra, chiudere = «Jacob. Don't.» Sul tradimento NON
## chiede mai scusa davvero: per lui conta l'orgoglio ferito.

init python:
    discorso("ex_intro", "ex", ESTRANEI)
    discorso("ex_a1", "ex", CONOSCENTI)
    discorso("ex_a2", "ex", CONOSCENTI)
    discorso("ex_a3", "ex", CONOSCENTI)
    discorso("ex_a4", "ex", CONOSCENTI)
    discorso("ex_a5", "ex", CONOSCENTI)
    discorso("ex_a6", "ex", CONOSCENTI)
    discorso("ex_a7", "ex", CONOSCENTI)
    discorso("ex_a8", "ex", CONOSCENTI)
    discorso("ex_b1", "ex", CONFIDENZA)
    discorso("ex_b2", "ex", CONFIDENZA)
    discorso("ex_b3", "ex", CONFIDENZA)
    discorso("ex_b4", "ex", CONFIDENZA)
    discorso("ex_b5", "ex", CONFIDENZA)


## --- Introduzione: ritrovarsi dopo tanto tempo -------------------------------

label chat_ex_intro:
    label tel_chat_ex_intro_1:
    if telefono_minuti_blocco("tel_chat_ex_intro_1", "invia", 1):
        return
    $ msg("sara", "It was strange seeing you at the bar.")
    return

label chat_ex_intro_1:
    label tel_chat_ex_intro_1_1:
    if telefono_minuti_blocco("tel_chat_ex_intro_1_1", "ricevi", 1):
        return
    $ msg("ex", "strange good or strange bad")
    label tel_chat_ex_intro_1_2:
    if telefono_minuti_blocco("tel_chat_ex_intro_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Just strange.»":
            label tel_chat_ex_intro_1_3:
            if telefono_minuti_blocco("tel_chat_ex_intro_1_3", "invia", 1):
                return
            $ msg("sara", "Just strange.")
            label tel_chat_ex_intro_1_4:
            if telefono_minuti_blocco("tel_chat_ex_intro_1_4", "ricevi", 1):
                return
            $ msg("ex", "fair. four years is a long time")
        "«Strange good. I think.»":
            label tel_chat_ex_intro_1_5:
            if telefono_minuti_blocco("tel_chat_ex_intro_1_5", "invia", 1):
                return
            $ msg("sara", "Strange good. I think.")
            $ caldo()
            label tel_chat_ex_intro_1_6:
            if telefono_minuti_blocco("tel_chat_ex_intro_1_6", "ricevi", 1):
                return
            $ msg("ex", "i'll take «i think». it's more than i expected")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_intro_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_intro_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_intro_2:
    label tel_chat_ex_intro_2_1:
    if telefono_minuti_blocco("tel_chat_ex_intro_2_1", "ricevi", 2):
        return
    $ msg("ex", "you look good sara. happy. it suits you")
    $ msg("ex", "is he good to you?")
    sp "Why does he care?"
    label tel_chat_ex_intro_2_2:
    if telefono_minuti_blocco("tel_chat_ex_intro_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Very. [nome_compagno] is wonderful.»":
            label tel_chat_ex_intro_2_3:
            if telefono_minuti_blocco("tel_chat_ex_intro_2_3", "invia", 1):
                return
            $ msg("sara", "Very. [nome_compagno] is wonderful.")
            $ interest("josh", 1)
            label tel_chat_ex_intro_2_4:
            if telefono_minuti_blocco("tel_chat_ex_intro_2_4", "ricevi", 1):
                return
            $ msg("ex", "good. you deserve wonderful")
        "«He's good. Goodnight, Jacob.»":
            label tel_chat_ex_intro_2_5:
            if telefono_minuti_blocco("tel_chat_ex_intro_2_5", "invia", 1):
                return
            $ msg("sara", "He's good. Goodnight, Jacob.")
            label tel_chat_ex_intro_2_6:
            if telefono_minuti_blocco("tel_chat_ex_intro_2_6", "ricevi", 1):
                return
            $ msg("ex", "goodnight sara")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_intro_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_intro_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A1: vecchi amici --------------------------------------------------------

label chat_ex_a1:
    label tel_chat_ex_a1_1:
    if telefono_minuti_blocco("tel_chat_ex_a1_1", "invia", 1):
        return
    $ msg("sara", "Do you still see anyone from the old group?")
    return

label chat_ex_a1_1:
    label tel_chat_ex_a1_1_1:
    if telefono_minuti_blocco("tel_chat_ex_a1_1_1", "ricevi", 2):
        return
    $ msg("ex", "tony and the twins come by the club every friday")
    $ msg("ex", "lucy got married. to a vet. she's unbearable now. very happy and unbearable")
    label tel_chat_ex_a1_1_2:
    if telefono_minuti_blocco("tel_chat_ex_a1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Lucy married? No way!»":
            label tel_chat_ex_a1_1_3:
            if telefono_minuti_blocco("tel_chat_ex_a1_1_3", "invia", 1):
                return
            $ msg("sara", "Lucy married? No way!")
            $ caldo()
            label tel_chat_ex_a1_1_4:
            if telefono_minuti_blocco("tel_chat_ex_a1_1_4", "ricevi", 1):
                return
            $ msg("ex", "way. three kids. she sends me christmas cards. with all three in matching sweaters")
        "«I lost touch with all of them.»":
            label tel_chat_ex_a1_1_5:
            if telefono_minuti_blocco("tel_chat_ex_a1_1_5", "invia", 1):
                return
            $ msg("sara", "I lost touch with all of them.")
            label tel_chat_ex_a1_1_6:
            if telefono_minuti_blocco("tel_chat_ex_a1_1_6", "ricevi", 1):
                return
            $ msg("ex", "they ask about you. all the time")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_a1_2:
    label tel_chat_ex_a1_2_1:
    if telefono_minuti_blocco("tel_chat_ex_a1_2_1", "ricevi", 1):
        return
    $ msg("ex", "come on a friday. they'd go crazy to see you")
    label tel_chat_ex_a1_2_2:
    if telefono_minuti_blocco("tel_chat_ex_a1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Maybe. With [nome_compagno].»":
            label tel_chat_ex_a1_2_3:
            if telefono_minuti_blocco("tel_chat_ex_a1_2_3", "invia", 1):
                return
            $ msg("sara", "Maybe. With [nome_compagno].")
            label tel_chat_ex_a1_2_4:
            if telefono_minuti_blocco("tel_chat_ex_a1_2_4", "ricevi", 1):
                return
            $ msg("ex", "sure. bring him")
        "«That would be fun.»":
            label tel_chat_ex_a1_2_5:
            if telefono_minuti_blocco("tel_chat_ex_a1_2_5", "invia", 1):
                return
            $ msg("sara", "That would be fun.")
            $ caldo()
            label tel_chat_ex_a1_2_6:
            if telefono_minuti_blocco("tel_chat_ex_a1_2_6", "ricevi", 1):
                return
            $ msg("ex", "it would. like old times")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A2: ricordi divertenti --------------------------------------------------

label chat_ex_a2:
    label tel_chat_ex_a2_1:
    if telefono_minuti_blocco("tel_chat_ex_a2_1", "invia", 1):
        return
    $ msg("sara", "I was thinking about the time we got lost driving to the coast. Seven hours for a two-hour trip.")
    return

label chat_ex_a2_entrata:
    label tel_chat_ex_a2_entrata_1:
    if telefono_minuti_blocco("tel_chat_ex_a2_entrata_1", "ricevi", 1):
        return
    $ msg("ex", "remember the time we got locked out of the hostel in the rain")
    label tel_chat_ex_a2_entrata_2:
    if telefono_minuti_blocco("tel_chat_ex_a2_entrata_2", "invia", 1):
        return
    $ msg("sara", "Oh no. Don't remind me.")
    return

label chat_ex_a2_1:
    label tel_chat_ex_a2_1_1:
    if telefono_minuti_blocco("tel_chat_ex_a2_1_1", "ricevi", 2):
        return
    $ msg("ex", "haha you refused to look at the map because «the sun is in the west»")
    $ msg("ex", "the sun was not in the west")
    label tel_chat_ex_a2_1_2:
    if telefono_minuti_blocco("tel_chat_ex_a2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It was a cloudy day! Not my fault.»":
            label tel_chat_ex_a2_1_3:
            if telefono_minuti_blocco("tel_chat_ex_a2_1_3", "invia", 1):
                return
            $ msg("sara", "It was a cloudy day! Not my fault.")
            $ caldo()
            label tel_chat_ex_a2_1_4:
            if telefono_minuti_blocco("tel_chat_ex_a2_1_4", "ricevi", 1):
                return
            $ msg("ex", "you still say that. four years later. incredible")
        "«We were so young and stupid.»":
            label tel_chat_ex_a2_1_5:
            if telefono_minuti_blocco("tel_chat_ex_a2_1_5", "invia", 1):
                return
            $ msg("sara", "We were so young and stupid.")
            label tel_chat_ex_a2_1_6:
            if telefono_minuti_blocco("tel_chat_ex_a2_1_6", "ricevi", 1):
                return
            $ msg("ex", "young yes. stupid only you")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_a2_2:
    label tel_chat_ex_a2_2_1:
    if telefono_minuti_blocco("tel_chat_ex_a2_2_1", "ricevi", 1):
        return
    $ msg("ex", "best trip of my life though. honestly")
    sp "Mine too. I'm not telling him that."
    return


## --- A3: la musica del passato -----------------------------------------------

label chat_ex_a3:
    label tel_chat_ex_a3_1:
    if telefono_minuti_blocco("tel_chat_ex_a3_1", "invia", 1):
        return
    $ msg("sara", "They played that song on the radio today. You know which one.")
    return

label chat_ex_a3_1:
    label tel_chat_ex_a3_1_1:
    if telefono_minuti_blocco("tel_chat_ex_a3_1_1", "ricevi", 2):
        return
    $ msg("ex", "the one from the concert in the park?")
    $ msg("ex", "you sang it so badly a guy asked you to stop")
    label tel_chat_ex_a3_1_2:
    if telefono_minuti_blocco("tel_chat_ex_a3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I sang beautifully. He was jealous.»":
            label tel_chat_ex_a3_1_3:
            if telefono_minuti_blocco("tel_chat_ex_a3_1_3", "invia", 1):
                return
            $ msg("sara", "I sang beautifully. He was jealous.")
            $ caldo()
            label tel_chat_ex_a3_1_4:
            if telefono_minuti_blocco("tel_chat_ex_a3_1_4", "ricevi", 1):
                return
            $ msg("ex", "he was something. jealous wasn't it")
        "«I'd forgotten that.»":
            label tel_chat_ex_a3_1_5:
            if telefono_minuti_blocco("tel_chat_ex_a3_1_5", "invia", 1):
                return
            $ msg("sara", "I'd forgotten that.")
            label tel_chat_ex_a3_1_6:
            if telefono_minuti_blocco("tel_chat_ex_a3_1_6", "ricevi", 1):
                return
            $ msg("ex", "i didn't")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_a3_2:
    label tel_chat_ex_a3_2_1:
    if telefono_minuti_blocco("tel_chat_ex_a3_2_1", "ricevi", 1):
        return
    $ msg("ex", "i still have the playlist we made. never deleted it")
    sp "He kept it. Four years."
    return


## --- A4: il locale del primo incontro ----------------------------------------

label chat_ex_a4:
    label tel_chat_ex_a4_1:
    if telefono_minuti_blocco("tel_chat_ex_a4_1", "invia", 1):
        return
    $ msg("sara", "So what kind of place do you run? You never said.")
    return

label chat_ex_a4_1:
    label tel_chat_ex_a4_1_1:
    if telefono_minuti_blocco("tel_chat_ex_a4_1_1", "ricevi", 3):
        return
    $ msg("ex", "a strip club. two years now. don't make that face")
    sp "I'm making that face."
    $ msg("ex", "remember the place where we met? the one with the broken jukebox")
    $ msg("ex", "it closed. i bought the jukebox. it's in my club now. still broken")
    label tel_chat_ex_a4_1_2:
    if telefono_minuti_blocco("tel_chat_ex_a4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You bought the jukebox?!»":
            label tel_chat_ex_a4_1_3:
            if telefono_minuti_blocco("tel_chat_ex_a4_1_3", "invia", 1):
                return
            $ msg("sara", "You bought the jukebox?!")
            $ caldo()
            label tel_chat_ex_a4_1_4:
            if telefono_minuti_blocco("tel_chat_ex_a4_1_4", "ricevi", 1):
                return
            $ msg("ex", "had to. some things you don't let go")
        "«That's very sentimental of you.»":
            label tel_chat_ex_a4_1_5:
            if telefono_minuti_blocco("tel_chat_ex_a4_1_5", "invia", 1):
                return
            $ msg("sara", "That's very sentimental of you.")
            label tel_chat_ex_a4_1_6:
            if telefono_minuti_blocco("tel_chat_ex_a4_1_6", "ricevi", 1):
                return
            $ msg("ex", "don't tell anyone. i have a reputation")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_a4_2:
    label tel_chat_ex_a4_2_1:
    if telefono_minuti_blocco("tel_chat_ex_a4_2_1", "ricevi", 1):
        return
    $ msg("ex", "come see it. it only plays one song. guess which")
    label tel_chat_ex_a4_2_2:
    if telefono_minuti_blocco("tel_chat_ex_a4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I can guess.»":
            label tel_chat_ex_a4_2_3:
            if telefono_minuti_blocco("tel_chat_ex_a4_2_3", "invia", 1):
                return
            $ msg("sara", "I can guess.")
            label tel_chat_ex_a4_2_4:
            if telefono_minuti_blocco("tel_chat_ex_a4_2_4", "ricevi", 1):
                return
            $ msg("ex", "yeah. you can")
        "«Don't tell me. I'll come and hear it.»":
            label tel_chat_ex_a4_2_5:
            if telefono_minuti_blocco("tel_chat_ex_a4_2_5", "invia", 1):
                return
            $ msg("sara", "Don't tell me. I'll come and hear it.")
            $ caldo()
            label tel_chat_ex_a4_2_6:
            if telefono_minuti_blocco("tel_chat_ex_a4_2_6", "ricevi", 1):
                return
            $ msg("ex", "deal")
            $ segna("jacob_jukebox")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A5: come sono cambiati --------------------------------------------------

label chat_ex_a5:
    label tel_chat_ex_a5_1:
    if telefono_minuti_blocco("tel_chat_ex_a5_1", "invia", 1):
        return
    $ msg("sara", "You've changed. More... sure of yourself. If that's even possible.")
    return

label chat_ex_a5_1:
    label tel_chat_ex_a5_1_1:
    if telefono_minuti_blocco("tel_chat_ex_a5_1_1", "ricevi", 2):
        return
    $ msg("ex", "haha. you've changed too")
    $ msg("ex", "you used to hide behind your hair when you laughed. you don't anymore")
    label tel_chat_ex_a5_1_2:
    if telefono_minuti_blocco("tel_chat_ex_a5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I grew up.»":
            label tel_chat_ex_a5_1_3:
            if telefono_minuti_blocco("tel_chat_ex_a5_1_3", "invia", 1):
                return
            $ msg("sara", "I grew up.")
            label tel_chat_ex_a5_1_4:
            if telefono_minuti_blocco("tel_chat_ex_a5_1_4", "ricevi", 1):
                return
            $ msg("ex", "you did")
        "«You noticed that?»":
            label tel_chat_ex_a5_1_5:
            if telefono_minuti_blocco("tel_chat_ex_a5_1_5", "invia", 1):
                return
            $ msg("sara", "You noticed that?")
            $ caldo()
            label tel_chat_ex_a5_1_6:
            if telefono_minuti_blocco("tel_chat_ex_a5_1_6", "ricevi", 1):
                return
            $ msg("ex", "i notice everything about you. always did")
            sp "That shouldn't make me feel anything."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_a5_2:
    label tel_chat_ex_a5_2_1:
    if telefono_minuti_blocco("tel_chat_ex_a5_2_1", "ricevi", 1):
        return
    $ msg("ex", "i'm the same though. just with a club and better shoes")
    return


## --- A6: vacanze passate -----------------------------------------------------

label chat_ex_a6:
    label tel_chat_ex_a6_1:
    if telefono_minuti_blocco("tel_chat_ex_a6_1", "invia", 1):
        return
    $ msg("sara", "Where do you go on holiday now? Still the islands?")
    return

label chat_ex_a6_1:
    label tel_chat_ex_a6_1_1:
    if telefono_minuti_blocco("tel_chat_ex_a6_1_1", "ricevi", 2):
        return
    $ msg("ex", "every august. same beach. same little hotel with the blue doors")
    $ msg("ex", "the old lady still asks where the girl with the big hat is")
    label tel_chat_ex_a6_1_2:
    if telefono_minuti_blocco("tel_chat_ex_a6_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«She remembers me?»":
            label tel_chat_ex_a6_1_3:
            if telefono_minuti_blocco("tel_chat_ex_a6_1_3", "invia", 1):
                return
            $ msg("sara", "She remembers me?")
            $ caldo()
            label tel_chat_ex_a6_1_4:
            if telefono_minuti_blocco("tel_chat_ex_a6_1_4", "ricevi", 1):
                return
            $ msg("ex", "everyone remembers you sara")
        "«Tell her I'm fine.»":
            label tel_chat_ex_a6_1_5:
            if telefono_minuti_blocco("tel_chat_ex_a6_1_5", "invia", 1):
                return
            $ msg("sara", "Tell her I'm fine.")
            label tel_chat_ex_a6_1_6:
            if telefono_minuti_blocco("tel_chat_ex_a6_1_6", "ricevi", 1):
                return
            $ msg("ex", "i'll tell her you're married to a nice guy. she'll be disappointed")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a6_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a6_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_a6_2:
    label tel_chat_ex_a6_2_1:
    if telefono_minuti_blocco("tel_chat_ex_a6_2_1", "ricevi", 1):
        return
    $ msg("ex", "best sunsets in the world. you used to fall asleep before they ended")
    return


## --- A7: le rispettive vite --------------------------------------------------

label chat_ex_a7:
    label tel_chat_ex_a7_1:
    if telefono_minuti_blocco("tel_chat_ex_a7_1", "invia", 1):
        return
    $ msg("sara", "So, what's your life like now? Apart from work.")
    return

label chat_ex_a7_1:
    label tel_chat_ex_a7_1_1:
    if telefono_minuti_blocco("tel_chat_ex_a7_1_1", "ricevi", 2):
        return
    $ msg("ex", "club till 3. gym. sleep. repeat. no complaints")
    $ msg("ex", "and you? still writing?")
    label tel_chat_ex_a7_1_2:
    if telefono_minuti_blocco("tel_chat_ex_a7_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Still writing. A novel, maybe.»":
            label tel_chat_ex_a7_1_3:
            if telefono_minuti_blocco("tel_chat_ex_a7_1_3", "invia", 1):
                return
            $ msg("sara", "Still writing. A novel, maybe.")
            $ caldo()
            label tel_chat_ex_a7_1_4:
            if telefono_minuti_blocco("tel_chat_ex_a7_1_4", "ricevi", 1):
                return
            $ msg("ex", "knew it. you always had a notebook. even at the beach")
        "«I work at a newspaper now. Real job.»":
            label tel_chat_ex_a7_1_5:
            if telefono_minuti_blocco("tel_chat_ex_a7_1_5", "invia", 1):
                return
            $ msg("sara", "I work at a newspaper now. Real job.")
            label tel_chat_ex_a7_1_6:
            if telefono_minuti_blocco("tel_chat_ex_a7_1_6", "ricevi", 1):
                return
            $ msg("ex", "real job. look at you")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a7_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a7_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_a7_2:
    label tel_chat_ex_a7_2_1:
    if telefono_minuti_blocco("tel_chat_ex_a7_2_1", "ricevi", 1):
        return
    $ msg("ex", "and him? what does he do")
    label tel_chat_ex_a7_2_2:
    if telefono_minuti_blocco("tel_chat_ex_a7_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«He works in an office. He's great at it.»":
            label tel_chat_ex_a7_2_3:
            if telefono_minuti_blocco("tel_chat_ex_a7_2_3", "invia", 1):
                return
            $ msg("sara", "He works in an office. He's great at it.")
            $ interest("josh", 1)
            label tel_chat_ex_a7_2_4:
            if telefono_minuti_blocco("tel_chat_ex_a7_2_4", "ricevi", 1):
                return
            $ msg("ex", "office. good. stable")
        "«Office stuff. Long hours.»":
            label tel_chat_ex_a7_2_5:
            if telefono_minuti_blocco("tel_chat_ex_a7_2_5", "invia", 1):
                return
            $ msg("sara", "Office stuff. Long hours.")
            label tel_chat_ex_a7_2_6:
            if telefono_minuti_blocco("tel_chat_ex_a7_2_6", "ricevi", 1):
                return
            $ msg("ex", "long hours. so you're alone a lot")
            sp "That's not what I said. Is it?"
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a7_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a7_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A8: nostalgia della giovinezza ------------------------------------------

label chat_ex_a8:
    label tel_chat_ex_a8_1:
    if telefono_minuti_blocco("tel_chat_ex_a8_1", "invia", 1):
        return
    $ msg("sara", "Do you ever miss being twenty-two?")
    return

label chat_ex_a8_1:
    label tel_chat_ex_a8_1_1:
    if telefono_minuti_blocco("tel_chat_ex_a8_1_1", "ricevi", 2):
        return
    $ msg("ex", "every day. nothing mattered and everything mattered")
    $ msg("ex", "you?")
    label tel_chat_ex_a8_1_2:
    if telefono_minuti_blocco("tel_chat_ex_a8_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Sometimes. Life was simpler.»":
            label tel_chat_ex_a8_1_3:
            if telefono_minuti_blocco("tel_chat_ex_a8_1_3", "invia", 1):
                return
            $ msg("sara", "Sometimes. Life was simpler.")
            label tel_chat_ex_a8_1_4:
            if telefono_minuti_blocco("tel_chat_ex_a8_1_4", "ricevi", 1):
                return
            $ msg("ex", "simpler. and louder")
        "«I miss how alive everything felt.»":
            label tel_chat_ex_a8_1_5:
            if telefono_minuti_blocco("tel_chat_ex_a8_1_5", "invia", 1):
                return
            $ msg("sara", "I miss how alive everything felt.")
            $ caldo()
            label tel_chat_ex_a8_1_6:
            if telefono_minuti_blocco("tel_chat_ex_a8_1_6", "ricevi", 1):
                return
            $ msg("ex", "yeah. i know exactly what you mean")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a8_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_a8_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_a8_2:
    label tel_chat_ex_a8_2_1:
    if telefono_minuti_blocco("tel_chat_ex_a8_2_1", "ricevi", 1):
        return
    $ msg("ex", "we were good at being young sara. really good")
    sp "We were."
    return


## --- B1: ricordi della relazione (prima allusione) ---------------------------

label chat_ex_b1:
    label tel_chat_ex_b1_1:
    if telefono_minuti_blocco("tel_chat_ex_b1_1", "invia", 1):
        return
    $ msg("sara", "I found an old photo of us today. At the lake.")
    return

label chat_ex_b1_entrata:
    label tel_chat_ex_b1_entrata_1:
    if telefono_minuti_blocco("tel_chat_ex_b1_entrata_1", "ricevi", 1):
        return
    $ msg("ex", "can't sleep. thinking about the lake")
    label tel_chat_ex_b1_entrata_2:
    if telefono_minuti_blocco("tel_chat_ex_b1_entrata_2", "invia", 1):
        return
    $ msg("sara", "The lake? Why?")
    return

label chat_ex_b1_1:
    label tel_chat_ex_b1_1_1:
    if telefono_minuti_blocco("tel_chat_ex_b1_1_1", "ricevi", 2):
        return
    $ msg("ex", "the lake weekend")
    $ msg("ex", "you remember. the cabin with no curtains")
    sp "I remember. I remember all of it."
    label tel_chat_ex_b1_1_2:
    if telefono_minuti_blocco("tel_chat_ex_b1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I remember :)»":
            label tel_chat_ex_b1_1_3:
            if telefono_minuti_blocco("tel_chat_ex_b1_1_3", "invia", 1):
                return
            $ msg("sara", "I remember :)")
            $ caldo()
            label tel_chat_ex_b1_1_4:
            if telefono_minuti_blocco("tel_chat_ex_b1_1_4", "ricevi", 1):
                return
            $ msg("ex", "good. i didn't want to be the only one")
            $ segna("jacob_lago")
        "(Let it drop.) «The lake was beautiful.»":
            label tel_chat_ex_b1_1_5:
            if telefono_minuti_blocco("tel_chat_ex_b1_1_5", "invia", 1):
                return
            $ msg("sara", "The lake was beautiful.")
            label tel_chat_ex_b1_1_6:
            if telefono_minuti_blocco("tel_chat_ex_b1_1_6", "ricevi", 1):
                return
            $ msg("ex", "it was. among other things")
        "«Jacob. Don't.»":
            label tel_chat_ex_b1_1_7:
            if telefono_minuti_blocco("tel_chat_ex_b1_1_7", "invia", 1):
                return
            $ msg("sara", "Jacob. Don't.")
            $ frena()
            label tel_chat_ex_b1_1_8:
            if telefono_minuti_blocco("tel_chat_ex_b1_1_8", "ricevi", 1):
                return
            $ msg("ex", "ok ok. sorry. goodnight")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_b1_2:
    label tel_chat_ex_b1_2_1:
    if telefono_minuti_blocco("tel_chat_ex_b1_2_1", "ricevi", 1):
        return
    $ msg("ex", "best weekend of my life. not even close")
    return


## --- B2: perché si sono lasciati ---------------------------------------------

label chat_ex_b2:
    label tel_chat_ex_b2_1:
    if telefono_minuti_blocco("tel_chat_ex_b2_1", "invia", 1):
        return
    $ msg("sara", "Do you ever think about why it ended?")
    return

label chat_ex_b2_1:
    label tel_chat_ex_b2_1_1:
    if telefono_minuti_blocco("tel_chat_ex_b2_1_1", "ricevi", 2):
        return
    $ msg("ex", "you left. that's why it ended")
    $ msg("ex", "nobody ever left me before. you were the first")
    sp "That's what he remembers. That I left. Not why."
    label tel_chat_ex_b2_1_2:
    if telefono_minuti_blocco("tel_chat_ex_b2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I left because you gave me a reason.»":
            label tel_chat_ex_b2_1_3:
            if telefono_minuti_blocco("tel_chat_ex_b2_1_3", "invia", 1):
                return
            $ msg("sara", "I left because you gave me a reason.")
            $ confidence(1)
            label tel_chat_ex_b2_1_4:
            if telefono_minuti_blocco("tel_chat_ex_b2_1_4", "ricevi", 1):
                return
            $ msg("ex", "yeah yeah. i know")
        "«It still hurts, you know.»":
            label tel_chat_ex_b2_1_5:
            if telefono_minuti_blocco("tel_chat_ex_b2_1_5", "invia", 1):
                return
            $ msg("sara", "It still hurts, you know.")
            $ caldo()
            label tel_chat_ex_b2_1_6:
            if telefono_minuti_blocco("tel_chat_ex_b2_1_6", "ricevi", 1):
                return
            $ msg("ex", "for me too. more than you think")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_b2_2:
    label tel_chat_ex_b2_2_1:
    if telefono_minuti_blocco("tel_chat_ex_b2_2_1", "ricevi", 1):
        return
    $ msg("ex", "you were the only one who could walk away from me. i respected that. still do")
    return


## --- B3: il tradimento (nessuna vera scusa) ----------------------------------

label chat_ex_b3:
    label tel_chat_ex_b3_1:
    if telefono_minuti_blocco("tel_chat_ex_b3_1", "invia", 1):
        return
    $ msg("sara", "Can we talk about it? What you did. I never heard your side.")
    return

label chat_ex_b3_1:
    label tel_chat_ex_b3_1_1:
    if telefono_minuti_blocco("tel_chat_ex_b3_1_1", "ricevi", 3):
        return
    $ msg("ex", "my side. ok")
    $ msg("ex", "it was one night. it meant nothing. i was stupid and she was there")
    $ msg("ex", "you found out and you were gone in an hour. you didn't even shout")
    label tel_chat_ex_b3_1_2:
    if telefono_minuti_blocco("tel_chat_ex_b3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Are you sorry?»":
            label tel_chat_ex_b3_1_3:
            if telefono_minuti_blocco("tel_chat_ex_b3_1_3", "invia", 1):
                return
            $ msg("sara", "Are you sorry?")
            label tel_chat_ex_b3_1_4:
            if telefono_minuti_blocco("tel_chat_ex_b3_1_4", "ricevi", 1):
                return
            $ msg("ex", "i'm sorry you found out like that")
            sp "Not «I'm sorry I did it». Never that."
        "«It meant something to me.»":
            label tel_chat_ex_b3_1_5:
            if telefono_minuti_blocco("tel_chat_ex_b3_1_5", "invia", 1):
                return
            $ msg("sara", "It meant something to me.")
            label tel_chat_ex_b3_1_6:
            if telefono_minuti_blocco("tel_chat_ex_b3_1_6", "ricevi", 2):
                return
            $ msg("ex", "i know. i know it did")
            $ msg("ex", "but you have to admit, leaving without a word was brutal too")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_b3_2:
    label tel_chat_ex_b3_2_1:
    if telefono_minuti_blocco("tel_chat_ex_b3_2_1", "ricevi", 1):
        return
    $ msg("ex", "anyway. old story. we're different people now")
    sp "He's not different. Not about this."
    label tel_chat_ex_b3_2_2:
    if telefono_minuti_blocco("tel_chat_ex_b3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Some things don't change, Jacob.»":
            label tel_chat_ex_b3_2_3:
            if telefono_minuti_blocco("tel_chat_ex_b3_2_3", "invia", 1):
                return
            $ msg("sara", "Some things don't change, Jacob.")
            $ confidence(1)
            label tel_chat_ex_b3_2_4:
            if telefono_minuti_blocco("tel_chat_ex_b3_2_4", "ricevi", 1):
                return
            $ msg("ex", "maybe. maybe some things shouldn't")
        "«You're right. Old story.»":
            label tel_chat_ex_b3_2_5:
            if telefono_minuti_blocco("tel_chat_ex_b3_2_5", "invia", 1):
                return
            $ msg("sara", "You're right. Old story.")
            $ caldo()
            label tel_chat_ex_b3_2_6:
            if telefono_minuti_blocco("tel_chat_ex_b3_2_6", "ricevi", 1):
                return
            $ msg("ex", "exactly. glad we cleared it up")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B4: cosa gli manca di Sara (allusione) ----------------------------------

label chat_ex_b4:
    label tel_chat_ex_b4_1:
    if telefono_minuti_blocco("tel_chat_ex_b4_1", "invia", 1):
        return
    $ msg("sara", "What do you miss about us? Honestly.")
    return

label chat_ex_b4_entrata:
    label tel_chat_ex_b4_entrata_1:
    if telefono_minuti_blocco("tel_chat_ex_b4_entrata_1", "ricevi", 1):
        return
    $ msg("ex", "you know what i miss?")
    label tel_chat_ex_b4_entrata_2:
    if telefono_minuti_blocco("tel_chat_ex_b4_entrata_2", "invia", 1):
        return
    $ msg("sara", "What?")
    return

label chat_ex_b4_1:
    label tel_chat_ex_b4_1_1:
    if telefono_minuti_blocco("tel_chat_ex_b4_1_1", "ricevi", 2):
        return
    $ msg("ex", "the way you laughed in the morning. half asleep. hair everywhere")
    $ msg("ex", "and the way you never wanted to get out of bed on sundays. we didn't, either")
    label tel_chat_ex_b4_1_2:
    if telefono_minuti_blocco("tel_chat_ex_b4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Those Sundays... :)»":
            label tel_chat_ex_b4_1_3:
            if telefono_minuti_blocco("tel_chat_ex_b4_1_3", "invia", 1):
                return
            $ msg("sara", "Those Sundays... :)")
            $ caldo()
            label tel_chat_ex_b4_1_4:
            if telefono_minuti_blocco("tel_chat_ex_b4_1_4", "ricevi", 1):
                return
            $ msg("ex", "yeah. those sundays")
            sp "I shouldn't be smiling at my phone like this."
        "(Let it drop.) «I'm a morning person now.»":
            label tel_chat_ex_b4_1_5:
            if telefono_minuti_blocco("tel_chat_ex_b4_1_5", "invia", 1):
                return
            $ msg("sara", "I'm a morning person now.")
            label tel_chat_ex_b4_1_6:
            if telefono_minuti_blocco("tel_chat_ex_b4_1_6", "ricevi", 1):
                return
            $ msg("ex", "liar")
        "«Jacob. Don't.»":
            label tel_chat_ex_b4_1_7:
            if telefono_minuti_blocco("tel_chat_ex_b4_1_7", "invia", 1):
                return
            $ msg("sara", "Jacob. Don't.")
            $ frena()
            label tel_chat_ex_b4_1_8:
            if telefono_minuti_blocco("tel_chat_ex_b4_1_8", "ricevi", 1):
                return
            $ msg("ex", "ok. you asked though")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_b4_2:
    label tel_chat_ex_b4_2_1:
    if telefono_minuti_blocco("tel_chat_ex_b4_2_1", "ricevi", 1):
        return
    $ msg("ex", "and you? you miss anything?")
    label tel_chat_ex_b4_2_2:
    if telefono_minuti_blocco("tel_chat_ex_b4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«No. I have everything I need.»":
            label tel_chat_ex_b4_2_3:
            if telefono_minuti_blocco("tel_chat_ex_b4_2_3", "invia", 1):
                return
            $ msg("sara", "No. I have everything I need.")
            $ interest("josh", 1)
            label tel_chat_ex_b4_2_4:
            if telefono_minuti_blocco("tel_chat_ex_b4_2_4", "ricevi", 1):
                return
            $ msg("ex", "good. that's good")
        "«...Some things.»":
            label tel_chat_ex_b4_2_5:
            if telefono_minuti_blocco("tel_chat_ex_b4_2_5", "invia", 1):
                return
            $ msg("sara", "...Some things.")
            $ caldo()
            label tel_chat_ex_b4_2_6:
            if telefono_minuti_blocco("tel_chat_ex_b4_2_6", "ricevi", 1):
                return
            $ msg("ex", "i knew it")
            $ segna("jacob_le_manca_qualcosa")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B5: le differenze fra ieri e oggi ---------------------------------------

label chat_ex_b5:
    label tel_chat_ex_b5_1:
    if telefono_minuti_blocco("tel_chat_ex_b5_1", "invia", 1):
        return
    $ msg("sara", "Is it weird that talking to you feels so normal?")
    return

label chat_ex_b5_1:
    label tel_chat_ex_b5_1_1:
    if telefono_minuti_blocco("tel_chat_ex_b5_1_1", "ricevi", 2):
        return
    $ msg("ex", "not weird. we were always easy together")
    $ msg("ex", "is it easy with him? like this?")
    sp "It's different. It's... careful."
    label tel_chat_ex_b5_1_2:
    if telefono_minuti_blocco("tel_chat_ex_b5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It's different. It's real.»":
            label tel_chat_ex_b5_1_3:
            if telefono_minuti_blocco("tel_chat_ex_b5_1_3", "invia", 1):
                return
            $ msg("sara", "It's different. It's real.")
            $ interest("josh", 1)
            label tel_chat_ex_b5_1_4:
            if telefono_minuti_blocco("tel_chat_ex_b5_1_4", "ricevi", 1):
                return
            $ msg("ex", "real. ok")
        "«It's different. Quieter.»":
            label tel_chat_ex_b5_1_5:
            if telefono_minuti_blocco("tel_chat_ex_b5_1_5", "invia", 1):
                return
            $ msg("sara", "It's different. Quieter.")
            $ caldo()
            label tel_chat_ex_b5_1_6:
            if telefono_minuti_blocco("tel_chat_ex_b5_1_6", "ricevi", 1):
                return
            $ msg("ex", "quieter. you used to hate quiet")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_b5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_b5_2:
    label tel_chat_ex_b5_2_1:
    if telefono_minuti_blocco("tel_chat_ex_b5_2_1", "ricevi", 2):
        return
    $ msg("ex", "we were fire sara. fire burns out but it's never boring")
    $ msg("ex", "goodnight")
    sp "Fire. And then nothing left. I remember that part too."
    return
