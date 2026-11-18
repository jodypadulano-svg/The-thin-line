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
    $ msg("sara", "It was strange seeing you at the bar.")
    return

label chat_ex_intro_1:
    $ msg("ex", "strange good or strange bad")
    menu (screen="scelta_telefono"):
        "«Just strange.»":
            $ msg("sara", "Just strange.")
            $ msg("ex", "fair. four years is a long time")
        "«Strange good. I think.»":
            $ msg("sara", "Strange good. I think.")
            $ caldo()
            $ msg("ex", "i'll take «i think». it's more than i expected")
    return

label chat_ex_intro_2:
    $ msg("ex", "you look good sara. happy. it suits you")
    $ msg("ex", "is he good to you?")
    sp "Why does he care?"
    menu (screen="scelta_telefono"):
        "«Very. [nome_compagno] is wonderful.»":
            $ msg("sara", "Very. [nome_compagno] is wonderful.")
            $ interest("josh", 1)
            $ msg("ex", "good. you deserve wonderful")
        "«He's good. Goodnight, Jacob.»":
            $ msg("sara", "He's good. Goodnight, Jacob.")
            $ msg("ex", "goodnight sara")
    return


## --- A1: vecchi amici --------------------------------------------------------

label chat_ex_a1:
    $ msg("sara", "Do you still see anyone from the old group?")
    return

label chat_ex_a1_1:
    $ msg("ex", "tony and the twins come to the bar every friday")
    $ msg("ex", "lucy got married. to a vet. she's unbearable now. very happy and unbearable")
    menu (screen="scelta_telefono"):
        "«Lucy married? No way!»":
            $ msg("sara", "Lucy married? No way!")
            $ caldo()
            $ msg("ex", "way. three kids. she sends me christmas cards. with all three in matching sweaters")
        "«I lost touch with all of them.»":
            $ msg("sara", "I lost touch with all of them.")
            $ msg("ex", "they ask about you. all the time")
    return

label chat_ex_a1_2:
    $ msg("ex", "come on a friday. they'd go crazy to see you")
    menu (screen="scelta_telefono"):
        "«Maybe. With [nome_compagno].»":
            $ msg("sara", "Maybe. With [nome_compagno].")
            $ msg("ex", "sure. bring him")
        "«That would be fun.»":
            $ msg("sara", "That would be fun.")
            $ caldo()
            $ msg("ex", "it would. like old times")
    return


## --- A2: ricordi divertenti --------------------------------------------------

label chat_ex_a2:
    $ msg("sara", "I was thinking about the time we got lost driving to the coast. Seven hours for a two-hour trip.")
    return

label chat_ex_a2_entrata:
    $ msg("ex", "remember the time we got locked out of the hostel in the rain")
    $ msg("sara", "Oh no. Don't remind me.")
    return

label chat_ex_a2_1:
    $ msg("ex", "haha you refused to look at the map because «the sun is in the west»")
    $ msg("ex", "the sun was not in the west")
    menu (screen="scelta_telefono"):
        "«It was a cloudy day! Not my fault.»":
            $ msg("sara", "It was a cloudy day! Not my fault.")
            $ caldo()
            $ msg("ex", "you still say that. four years later. incredible")
        "«We were so young and stupid.»":
            $ msg("sara", "We were so young and stupid.")
            $ msg("ex", "young yes. stupid only you")
    return

label chat_ex_a2_2:
    $ msg("ex", "best trip of my life though. honestly")
    sp "Mine too. I'm not telling him that."
    return


## --- A3: la musica del passato -----------------------------------------------

label chat_ex_a3:
    $ msg("sara", "They played that song on the radio today. You know which one.")
    return

label chat_ex_a3_1:
    $ msg("ex", "the one from the concert in the park?")
    $ msg("ex", "you sang it so badly a guy asked you to stop")
    menu (screen="scelta_telefono"):
        "«I sang beautifully. He was jealous.»":
            $ msg("sara", "I sang beautifully. He was jealous.")
            $ caldo()
            $ msg("ex", "he was something. jealous wasn't it")
        "«I'd forgotten that.»":
            $ msg("sara", "I'd forgotten that.")
            $ msg("ex", "i didn't")
    return

label chat_ex_a3_2:
    $ msg("ex", "i still have the playlist we made. never deleted it")
    sp "He kept it. Four years."
    return


## --- A4: il locale del primo incontro ----------------------------------------

label chat_ex_a4:
    $ msg("sara", "So you own a bar now. Since when?")
    return

label chat_ex_a4_1:
    $ msg("ex", "two years. remember the place where we met? the one with the broken jukebox")
    $ msg("ex", "it closed. i bought the jukebox. it's in my bar now. still broken")
    menu (screen="scelta_telefono"):
        "«You bought the jukebox?!»":
            $ msg("sara", "You bought the jukebox?!")
            $ caldo()
            $ msg("ex", "had to. some things you don't let go")
        "«That's very sentimental of you.»":
            $ msg("sara", "That's very sentimental of you.")
            $ msg("ex", "don't tell anyone. i have a reputation")
    return

label chat_ex_a4_2:
    $ msg("ex", "come see it. it only plays one song. guess which")
    menu (screen="scelta_telefono"):
        "«I can guess.»":
            $ msg("sara", "I can guess.")
            $ msg("ex", "yeah. you can")
        "«Don't tell me. I'll come and hear it.»":
            $ msg("sara", "Don't tell me. I'll come and hear it.")
            $ caldo()
            $ msg("ex", "deal")
            $ segna("jacob_jukebox")
    return


## --- A5: come sono cambiati --------------------------------------------------

label chat_ex_a5:
    $ msg("sara", "You've changed. More... sure of yourself. If that's even possible.")
    return

label chat_ex_a5_1:
    $ msg("ex", "haha. you've changed too")
    $ msg("ex", "you used to hide behind your hair when you laughed. you don't anymore")
    menu (screen="scelta_telefono"):
        "«I grew up.»":
            $ msg("sara", "I grew up.")
            $ msg("ex", "you did")
        "«You noticed that?»":
            $ msg("sara", "You noticed that?")
            $ caldo()
            $ msg("ex", "i notice everything about you. always did")
            sp "That shouldn't make me feel anything."
    return

label chat_ex_a5_2:
    $ msg("ex", "i'm the same though. just with a bar and better shoes")
    return


## --- A6: vacanze passate -----------------------------------------------------

label chat_ex_a6:
    $ msg("sara", "Where do you go on holiday now? Still the islands?")
    return

label chat_ex_a6_1:
    $ msg("ex", "every august. same beach. same little hotel with the blue doors")
    $ msg("ex", "the old lady still asks where the girl with the big hat is")
    menu (screen="scelta_telefono"):
        "«She remembers me?»":
            $ msg("sara", "She remembers me?")
            $ caldo()
            $ msg("ex", "everyone remembers you sara")
        "«Tell her I'm fine.»":
            $ msg("sara", "Tell her I'm fine.")
            $ msg("ex", "i'll tell her you're married to a nice guy. she'll be disappointed")
    return

label chat_ex_a6_2:
    $ msg("ex", "best sunsets in the world. you used to fall asleep before they ended")
    return


## --- A7: le rispettive vite --------------------------------------------------

label chat_ex_a7:
    $ msg("sara", "So, what's your life like now? Apart from the bar.")
    return

label chat_ex_a7_1:
    $ msg("ex", "bar till 3. gym. sleep. repeat. no complaints")
    $ msg("ex", "and you? still writing?")
    menu (screen="scelta_telefono"):
        "«Still writing. A novel, maybe.»":
            $ msg("sara", "Still writing. A novel, maybe.")
            $ caldo()
            $ msg("ex", "knew it. you always had a notebook. even at the beach")
        "«I work at a newspaper now. Real job.»":
            $ msg("sara", "I work at a newspaper now. Real job.")
            $ msg("ex", "real job. look at you")
    return

label chat_ex_a7_2:
    $ msg("ex", "and him? what does he do")
    menu (screen="scelta_telefono"):
        "«He works in an office. He's great at it.»":
            $ msg("sara", "He works in an office. He's great at it.")
            $ interest("josh", 1)
            $ msg("ex", "office. good. stable")
        "«Office stuff. Long hours.»":
            $ msg("sara", "Office stuff. Long hours.")
            $ msg("ex", "long hours. so you're alone a lot")
            sp "That's not what I said. Is it?"
    return


## --- A8: nostalgia della giovinezza ------------------------------------------

label chat_ex_a8:
    $ msg("sara", "Do you ever miss being twenty-five?")
    return

label chat_ex_a8_1:
    $ msg("ex", "every day. nothing mattered and everything mattered")
    $ msg("ex", "you?")
    menu (screen="scelta_telefono"):
        "«Sometimes. Life was simpler.»":
            $ msg("sara", "Sometimes. Life was simpler.")
            $ msg("ex", "simpler. and louder")
        "«I miss how alive everything felt.»":
            $ msg("sara", "I miss how alive everything felt.")
            $ caldo()
            $ msg("ex", "yeah. i know exactly what you mean")
    return

label chat_ex_a8_2:
    $ msg("ex", "we were good at being young sara. really good")
    sp "We were."
    return


## --- B1: ricordi della relazione (prima allusione) ---------------------------

label chat_ex_b1:
    $ msg("sara", "I found an old photo of us today. At the lake.")
    return

label chat_ex_b1_entrata:
    $ msg("ex", "can't sleep. thinking about the lake")
    $ msg("sara", "The lake? Why?")
    return

label chat_ex_b1_1:
    $ msg("ex", "the lake weekend")
    $ msg("ex", "you remember. the cabin with no curtains")
    sp "I remember. I remember all of it."
    menu (screen="scelta_telefono"):
        "«I remember :)»":
            $ msg("sara", "I remember :)")
            $ caldo()
            $ msg("ex", "good. i didn't want to be the only one")
            $ segna("jacob_lago")
        "(Let it drop.) «The lake was beautiful.»":
            $ msg("sara", "The lake was beautiful.")
            $ msg("ex", "it was. among other things")
        "«Jacob. Don't.»":
            $ msg("sara", "Jacob. Don't.")
            $ frena()
            $ msg("ex", "ok ok. sorry. goodnight")
    return

label chat_ex_b1_2:
    $ msg("ex", "best weekend of my life. not even close")
    return


## --- B2: perché si sono lasciati ---------------------------------------------

label chat_ex_b2:
    $ msg("sara", "Do you ever think about why it ended?")
    return

label chat_ex_b2_1:
    $ msg("ex", "you left. that's why it ended")
    $ msg("ex", "nobody ever left me before. you were the first")
    sp "That's what he remembers. That I left. Not why."
    menu (screen="scelta_telefono"):
        "«I left because you gave me a reason.»":
            $ msg("sara", "I left because you gave me a reason.")
            $ confidence(1)
            $ msg("ex", "yeah yeah. i know")
        "«It still hurts, you know.»":
            $ msg("sara", "It still hurts, you know.")
            $ caldo()
            $ msg("ex", "for me too. more than you think")
    return

label chat_ex_b2_2:
    $ msg("ex", "you were the only one who could walk away from me. i respected that. still do")
    return


## --- B3: il tradimento (nessuna vera scusa) ----------------------------------

label chat_ex_b3:
    $ msg("sara", "Can we talk about it? What you did. I never heard your side.")
    return

label chat_ex_b3_1:
    $ msg("ex", "my side. ok")
    $ msg("ex", "it was one night. it meant nothing. i was stupid and she was there")
    $ msg("ex", "you found out and you were gone in an hour. you didn't even shout")
    menu (screen="scelta_telefono"):
        "«Are you sorry?»":
            $ msg("sara", "Are you sorry?")
            $ msg("ex", "i'm sorry you found out like that")
            sp "Not «I'm sorry I did it». Never that."
        "«It meant something to me.»":
            $ msg("sara", "It meant something to me.")
            $ msg("ex", "i know. i know it did")
            $ msg("ex", "but you have to admit, leaving without a word was brutal too")
    return

label chat_ex_b3_2:
    $ msg("ex", "anyway. old story. we're different people now")
    sp "He's not different. Not about this."
    menu (screen="scelta_telefono"):
        "«Some things don't change, Jacob.»":
            $ msg("sara", "Some things don't change, Jacob.")
            $ confidence(1)
            $ msg("ex", "maybe. maybe some things shouldn't")
        "«You're right. Old story.»":
            $ msg("sara", "You're right. Old story.")
            $ caldo()
            $ msg("ex", "exactly. glad we cleared it up")
    return


## --- B4: cosa gli manca di Sara (allusione) ----------------------------------

label chat_ex_b4:
    $ msg("sara", "What do you miss about us? Honestly.")
    return

label chat_ex_b4_entrata:
    $ msg("ex", "you know what i miss?")
    $ msg("sara", "What?")
    return

label chat_ex_b4_1:
    $ msg("ex", "the way you laughed in the morning. half asleep. hair everywhere")
    $ msg("ex", "and the way you never wanted to get out of bed on sundays. we didn't, either")
    menu (screen="scelta_telefono"):
        "«Those Sundays... :)»":
            $ msg("sara", "Those Sundays... :)")
            $ caldo()
            $ msg("ex", "yeah. those sundays")
            sp "I shouldn't be smiling at my phone like this."
        "(Let it drop.) «I'm a morning person now.»":
            $ msg("sara", "I'm a morning person now.")
            $ msg("ex", "liar")
        "«Jacob. Don't.»":
            $ msg("sara", "Jacob. Don't.")
            $ frena()
            $ msg("ex", "ok. you asked though")
    return

label chat_ex_b4_2:
    $ msg("ex", "and you? you miss anything?")
    menu (screen="scelta_telefono"):
        "«No. I have everything I need.»":
            $ msg("sara", "No. I have everything I need.")
            $ interest("josh", 1)
            $ msg("ex", "good. that's good")
        "«...Some things.»":
            $ msg("sara", "...Some things.")
            $ caldo()
            $ msg("ex", "i knew it")
            $ segna("jacob_le_manca_qualcosa")
    return


## --- B5: le differenze fra ieri e oggi ---------------------------------------

label chat_ex_b5:
    $ msg("sara", "Is it weird that talking to you feels so normal?")
    return

label chat_ex_b5_1:
    $ msg("ex", "not weird. we were always easy together")
    $ msg("ex", "is it easy with him? like this?")
    sp "It's different. It's... careful."
    menu (screen="scelta_telefono"):
        "«It's different. It's real.»":
            $ msg("sara", "It's different. It's real.")
            $ interest("josh", 1)
            $ msg("ex", "real. ok")
        "«It's different. Quieter.»":
            $ msg("sara", "It's different. Quieter.")
            $ caldo()
            $ msg("ex", "quieter. you used to hate quiet")
    return

label chat_ex_b5_2:
    $ msg("ex", "we were fire sara. fire burns out but it's never boring")
    $ msg("ex", "goodnight")
    sp "Fire. And then nothing left. I remember that part too."
    return
