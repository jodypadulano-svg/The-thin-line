## GENERATO da tools/telefono/componi.py: si modifica tools/telefono/ex.txt.

init python:
    discorso("ex_t1", "ex", ESTRANEI, argomento="Seeing you again", se="fatto('jacob_tornato')")
    discorso("ex_t2", "ex", ESTRANEI, argomento="What I said to you", se="fatto('ep2_d19_detto_tradimento')")
    discorso("ex_t3", "ex", ESTRANEI, argomento="One song", se="fatto('ep2_d19_ballo_jacob')")
    discorso("ex_t4", "ex", ESTRANEI, argomento="Eleven coffees", se="fatto('ep2_d19_jacob_risata')")
    discorso("ex_c1", "ex", COMPLICI, flirt=True)
    discorso("ex_c2", "ex", COMPLICI, flirt=True)
    discorso("ex_d1", "ex", INTIMI, flirt=True)
    discorso("ex_d2", "ex", INTIMI, flirt=True)


## --- Seeing you again

label chat_ex_t1:
    label tel_chat_ex_t1_1:
    if telefono_minuti_blocco("tel_chat_ex_t1_1", "invia", 1):
        return
    $ msg("sara", "So you're back in the world.")
    return

label chat_ex_t1_entrata:
    label tel_chat_ex_t1_entrata_1:
    if telefono_minuti_blocco("tel_chat_ex_t1_entrata_1", "ricevi", 2):
        return
    $ msg("ex", "hey")
    $ msg("ex", "it's me. don't panic")
    label tel_chat_ex_t1_entrata_2:
    if telefono_minuti_blocco("tel_chat_ex_t1_entrata_2", "invia", 1):
        return
    $ msg("sara", "So you're back in the world.")
    return

label chat_ex_t1_1:
    label tel_chat_ex_t1_1_1:
    if telefono_minuti_blocco("tel_chat_ex_t1_1_1", "ricevi", 2):
        return
    $ msg("ex", "never left it. you did")
    $ msg("ex", "you looked good tonight. I'd planned to say something clever and then you turned round")
    label tel_chat_ex_t1_1_2:
    if telefono_minuti_blocco("tel_chat_ex_t1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What was the clever thing?»":
            label tel_chat_ex_t1_1_3:
            if telefono_minuti_blocco("tel_chat_ex_t1_1_3", "invia", 1):
                return
            $ msg("sara", "What was the clever thing?")
            $ caldo()
            label tel_chat_ex_t1_1_4:
            if telefono_minuti_blocco("tel_chat_ex_t1_1_4", "ricevi", 1):
                return
            $ msg("ex", "no idea. it's still on the bar somewhere")
        "«You've lost your hair.»":
            label tel_chat_ex_t1_1_5:
            if telefono_minuti_blocco("tel_chat_ex_t1_1_5", "invia", 1):
                return
            $ msg("sara", "You've lost your hair.")
            label tel_chat_ex_t1_1_6:
            if telefono_minuti_blocco("tel_chat_ex_t1_1_6", "ricevi", 1):
                return
            $ msg("ex", "it was holding me back")
        "«You didn't look surprised.»":
            label tel_chat_ex_t1_1_7:
            if telefono_minuti_blocco("tel_chat_ex_t1_1_7", "invia", 1):
                return
            $ msg("sara", "You didn't look surprised.")
            label tel_chat_ex_t1_1_8:
            if telefono_minuti_blocco("tel_chat_ex_t1_1_8", "ricevi", 1):
                return
            $ msg("ex", "I'm never surprised. it's the only talent I've got")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_t1_2:
    label tel_chat_ex_t1_2_1:
    if telefono_minuti_blocco("tel_chat_ex_t1_2_1", "ricevi", 1):
        return
    $ msg("ex", "joanie's the same")
    label tel_chat_ex_t1_2_2:
    if telefono_minuti_blocco("tel_chat_ex_t1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Joanie's always the same. Thank God.»":
            label tel_chat_ex_t1_2_3:
            if telefono_minuti_blocco("tel_chat_ex_t1_2_3", "invia", 1):
                return
            $ msg("sara", "Joanie's always the same. Thank God.")
            label tel_chat_ex_t1_2_4:
            if telefono_minuti_blocco("tel_chat_ex_t1_2_4", "ricevi", 1):
                return
            $ msg("ex", "she used to look after you like a lioness with a handbag")
        "«She arranged it, didn't she?»":
            label tel_chat_ex_t1_2_5:
            if telefono_minuti_blocco("tel_chat_ex_t1_2_5", "invia", 1):
                return
            $ msg("sara", "She arranged it, didn't she?")
            $ caldo()
            label tel_chat_ex_t1_2_6:
            if telefono_minuti_blocco("tel_chat_ex_t1_2_6", "ricevi", 1):
                return
            $ msg("ex", "I'm not a man who gives up his sources")
            sp "That's a yes."
        "«Let's leave Joanie out of it.»":
            label tel_chat_ex_t1_2_7:
            if telefono_minuti_blocco("tel_chat_ex_t1_2_7", "invia", 1):
                return
            $ msg("sara", "Let's leave Joanie out of it.")
            label tel_chat_ex_t1_2_8:
            if telefono_minuti_blocco("tel_chat_ex_t1_2_8", "ricevi", 1):
                return
            $ msg("ex", "nobody's ever managed that")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_t1_3:
    label tel_chat_ex_t1_3_1:
    if telefono_minuti_blocco("tel_chat_ex_t1_3_1", "ricevi", 1):
        return
    $ msg("ex", "one question and you can ignore it. were you happy to see me")
    label tel_chat_ex_t1_3_2:
    if telefono_minuti_blocco("tel_chat_ex_t1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«For about a second. Then I remembered.»":
            label tel_chat_ex_t1_3_3:
            if telefono_minuti_blocco("tel_chat_ex_t1_3_3", "invia", 1):
                return
            $ msg("sara", "For about a second. Then I remembered.")
            label tel_chat_ex_t1_3_4:
            if telefono_minuti_blocco("tel_chat_ex_t1_3_4", "ricevi", 1):
                return
            $ msg("ex", "I'll take the second")
        "«I don't know what I was.»":
            label tel_chat_ex_t1_3_5:
            if telefono_minuti_blocco("tel_chat_ex_t1_3_5", "invia", 1):
                return
            $ msg("sara", "I don't know what I was.")
            label tel_chat_ex_t1_3_6:
            if telefono_minuti_blocco("tel_chat_ex_t1_3_6", "ricevi", 1):
                return
            $ msg("ex", "that's the best answer anybody's given me all year")
        "«Goodnight, Jacob.»":
            label tel_chat_ex_t1_3_7:
            if telefono_minuti_blocco("tel_chat_ex_t1_3_7", "invia", 1):
                return
            $ msg("sara", "Goodnight, Jacob.")
            label tel_chat_ex_t1_3_8:
            if telefono_minuti_blocco("tel_chat_ex_t1_3_8", "ricevi", 1):
                return
            $ msg("ex", "see. there's a full stop. you never used to bother with those. night")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- What I said to you

label chat_ex_t2:
    label tel_chat_ex_t2_1:
    if telefono_minuti_blocco("tel_chat_ex_t2_1", "invia", 1):
        return
    $ msg("sara", "I meant it, you know. What I said at the bar.")
    return

label chat_ex_t2_1:
    label tel_chat_ex_t2_1_1:
    if telefono_minuti_blocco("tel_chat_ex_t2_1_1", "ricevi", 2):
        return
    $ msg("ex", "I know. you said it like the weather")
    $ msg("ex", "I've had it shouted at me. yours was worse")
    label tel_chat_ex_t2_1_2:
    if telefono_minuti_blocco("tel_chat_ex_t2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Good.»":
            label tel_chat_ex_t2_1_3:
            if telefono_minuti_blocco("tel_chat_ex_t2_1_3", "invia", 1):
                return
            $ msg("sara", "Good.")
            $ caldo()
            label tel_chat_ex_t2_1_4:
            if telefono_minuti_blocco("tel_chat_ex_t2_1_4", "ricevi", 1):
                return
            $ msg("ex", "yeah. I thought so too")
        "«I'd been saving it for four years.»":
            label tel_chat_ex_t2_1_5:
            if telefono_minuti_blocco("tel_chat_ex_t2_1_5", "invia", 1):
                return
            $ msg("sara", "I'd been saving it for four years.")
            label tel_chat_ex_t2_1_6:
            if telefono_minuti_blocco("tel_chat_ex_t2_1_6", "ricevi", 1):
                return
            $ msg("ex", "it kept well")
        "«I didn't do it to hurt you.»":
            label tel_chat_ex_t2_1_7:
            if telefono_minuti_blocco("tel_chat_ex_t2_1_7", "invia", 1):
                return
            $ msg("sara", "I didn't do it to hurt you.")
            label tel_chat_ex_t2_1_8:
            if telefono_minuti_blocco("tel_chat_ex_t2_1_8", "ricevi", 1):
                return
            $ msg("ex", "that's why it did")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_t2_2:
    label tel_chat_ex_t2_2_1:
    if telefono_minuti_blocco("tel_chat_ex_t2_2_1", "ricevi", 1):
        return
    $ msg("ex", "you want me to say something")
    label tel_chat_ex_t2_2_2:
    if telefono_minuti_blocco("tel_chat_ex_t2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You could say sorry.»":
            label tel_chat_ex_t2_2_3:
            if telefono_minuti_blocco("tel_chat_ex_t2_2_3", "invia", 1):
                return
            $ msg("sara", "You could say sorry.")
            label tel_chat_ex_t2_2_4:
            if telefono_minuti_blocco("tel_chat_ex_t2_2_4", "ricevi", 1):
                return
            $ msg("ex", "I could. you'd know. you always knew when I was reading off the card")
        "«No. I just wanted it said.»":
            label tel_chat_ex_t2_2_5:
            if telefono_minuti_blocco("tel_chat_ex_t2_2_5", "invia", 1):
                return
            $ msg("sara", "No. I just wanted it said.")
            $ caldo()
            label tel_chat_ex_t2_2_6:
            if telefono_minuti_blocco("tel_chat_ex_t2_2_6", "ricevi", 1):
                return
            $ msg("ex", "then it's said. I was there. I heard it")
            sp "He heard it. That's more than I thought I'd get."
        "«Why did you do it?»":
            label tel_chat_ex_t2_2_7:
            if telefono_minuti_blocco("tel_chat_ex_t2_2_7", "invia", 1):
                return
            $ msg("sara", "Why did you do it?")
            label tel_chat_ex_t2_2_8:
            if telefono_minuti_blocco("tel_chat_ex_t2_2_8", "ricevi", 1):
                return
            $ msg("ex", "because I wanted to. and because I thought you'd stay. both were true, that's what's wrong with me")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_t2_3:
    label tel_chat_ex_t2_3_1:
    if telefono_minuti_blocco("tel_chat_ex_t2_3_1", "ricevi", 1):
        return
    $ msg("ex", "here's a thing I can say without the card. nobody ever made that flat sound like you did")
    label tel_chat_ex_t2_3_2:
    if telefono_minuti_blocco("tel_chat_ex_t2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It was a tiny flat.»":
            label tel_chat_ex_t2_3_3:
            if telefono_minuti_blocco("tel_chat_ex_t2_3_3", "invia", 1):
                return
            $ msg("sara", "It was a tiny flat.")
            label tel_chat_ex_t2_3_4:
            if telefono_minuti_blocco("tel_chat_ex_t2_3_4", "ricevi", 1):
                return
            $ msg("ex", "you filled it. you'd sing with the hoover on and think nobody could hear")
        "«That's not an apology.»":
            label tel_chat_ex_t2_3_5:
            if telefono_minuti_blocco("tel_chat_ex_t2_3_5", "invia", 1):
                return
            $ msg("sara", "That's not an apology.")
            label tel_chat_ex_t2_3_6:
            if telefono_minuti_blocco("tel_chat_ex_t2_3_6", "ricevi", 2):
                return
            $ msg("ex", "no. it's just true. I've got a lot of those and nowhere to put them")
            $ msg("ex", "night sara")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- One song

label chat_ex_t3:
    label tel_chat_ex_t3_1:
    if telefono_minuti_blocco("tel_chat_ex_t3_1", "invia", 1):
        return
    $ msg("sara", "You kept your word. One song, and you didn't talk.")
    return

label chat_ex_t3_entrata:
    label tel_chat_ex_t3_entrata_1:
    if telefono_minuti_blocco("tel_chat_ex_t3_entrata_1", "ricevi", 1):
        return
    $ msg("ex", "one song. not a word. I'd like that noted")
    label tel_chat_ex_t3_entrata_2:
    if telefono_minuti_blocco("tel_chat_ex_t3_entrata_2", "invia", 1):
        return
    $ msg("sara", "Noted. You kept quiet the whole way through.")
    return

label chat_ex_t3_1:
    label tel_chat_ex_t3_1_1:
    if telefono_minuti_blocco("tel_chat_ex_t3_1_1", "ricevi", 2):
        return
    $ msg("ex", "nearly killed me")
    $ msg("ex", "I had things. I had a whole list")
    label tel_chat_ex_t3_1_2:
    if telefono_minuti_blocco("tel_chat_ex_t3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Like what?»":
            label tel_chat_ex_t3_1_3:
            if telefono_minuti_blocco("tel_chat_ex_t3_1_3", "invia", 1):
                return
            $ msg("sara", "Like what?")
            $ caldo()
            label tel_chat_ex_t3_1_4:
            if telefono_minuti_blocco("tel_chat_ex_t3_1_4", "ricevi", 1):
                return
            $ msg("ex", "like you still lead with your left")
        "«You counted under your breath.»":
            label tel_chat_ex_t3_1_5:
            if telefono_minuti_blocco("tel_chat_ex_t3_1_5", "invia", 1):
                return
            $ msg("sara", "You counted under your breath.")
            label tel_chat_ex_t3_1_6:
            if telefono_minuti_blocco("tel_chat_ex_t3_1_6", "ricevi", 1):
                return
            $ msg("ex", "somebody had to. you were miles away")
        "«I noticed the gap. Very proper.»":
            label tel_chat_ex_t3_1_7:
            if telefono_minuti_blocco("tel_chat_ex_t3_1_7", "invia", 1):
                return
            $ msg("sara", "I noticed the gap. Very proper.")
            label tel_chat_ex_t3_1_8:
            if telefono_minuti_blocco("tel_chat_ex_t3_1_8", "ricevi", 1):
                return
            $ msg("ex", "you could have driven a bus through it. I was showing off")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_t3_2:
    label tel_chat_ex_t3_2_1:
    if telefono_minuti_blocco("tel_chat_ex_t3_2_1", "ricevi", 1):
        return
    $ msg("ex", "your feet remember me")
    label tel_chat_ex_t3_2_2:
    if telefono_minuti_blocco("tel_chat_ex_t3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«My feet aren't in charge.»":
            label tel_chat_ex_t3_2_3:
            if telefono_minuti_blocco("tel_chat_ex_t3_2_3", "invia", 1):
                return
            $ msg("sara", "My feet aren't in charge.")
            label tel_chat_ex_t3_2_4:
            if telefono_minuti_blocco("tel_chat_ex_t3_2_4", "ricevi", 1):
                return
            $ msg("ex", "no. but they've got a vote")
        "«I noticed that as well.»":
            label tel_chat_ex_t3_2_5:
            if telefono_minuti_blocco("tel_chat_ex_t3_2_5", "invia", 1):
                return
            $ msg("sara", "I noticed that as well.")
            $ caldo()
            label tel_chat_ex_t3_2_6:
            if telefono_minuti_blocco("tel_chat_ex_t3_2_6", "ricevi", 1):
                return
            $ msg("ex", "I felt you notice. about the second verse")
            sp "He felt it. Of course he felt it."
        "«It was the song. Anyone's would.»":
            label tel_chat_ex_t3_2_7:
            if telefono_minuti_blocco("tel_chat_ex_t3_2_7", "invia", 1):
                return
            $ msg("sara", "It was the song. Anyone's would.")
            label tel_chat_ex_t3_2_8:
            if telefono_minuti_blocco("tel_chat_ex_t3_2_8", "ricevi", 1):
                return
            $ msg("ex", "sure. it's a very well known song for feet")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_t3_3:
    label tel_chat_ex_t3_3_1:
    if telefono_minuti_blocco("tel_chat_ex_t3_3_1", "ricevi", 1):
        return
    $ msg("ex", "I'm not asking for another one")
    label tel_chat_ex_t3_3_2:
    if telefono_minuti_blocco("tel_chat_ex_t3_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Good.»":
            label tel_chat_ex_t3_3_3:
            if telefono_minuti_blocco("tel_chat_ex_t3_3_3", "invia", 1):
                return
            $ msg("sara", "Good.")
            label tel_chat_ex_t3_3_4:
            if telefono_minuti_blocco("tel_chat_ex_t3_3_4", "ricevi", 1):
                return
            $ msg("ex", "I'm just telling you I know where they keep them")
        "«Not asking is how you ask.»":
            label tel_chat_ex_t3_3_5:
            if telefono_minuti_blocco("tel_chat_ex_t3_3_5", "invia", 1):
                return
            $ msg("sara", "Not asking is how you ask.")
            label tel_chat_ex_t3_3_6:
            if telefono_minuti_blocco("tel_chat_ex_t3_3_6", "ricevi", 2):
                return
            $ msg("ex", "you always were the clever one")
            $ msg("ex", "night. go and put them up")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t3_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t3_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Eleven coffees

label chat_ex_t4:
    label tel_chat_ex_t4_1:
    if telefono_minuti_blocco("tel_chat_ex_t4_1", "invia", 1):
        return
    $ msg("sara", "Eleven coffees. I'd managed to forget that for years.")
    return

label chat_ex_t4_entrata:
    label tel_chat_ex_t4_entrata_1:
    if telefono_minuti_blocco("tel_chat_ex_t4_entrata_1", "ricevi", 1):
        return
    $ msg("ex", "eleven")
    label tel_chat_ex_t4_entrata_2:
    if telefono_minuti_blocco("tel_chat_ex_t4_entrata_2", "invia", 1):
        return
    $ msg("sara", "Don't. I'd managed to forget those coffees for years.")
    return

label chat_ex_t4_1:
    label tel_chat_ex_t4_1_1:
    if telefono_minuti_blocco("tel_chat_ex_t4_1_1", "ricevi", 2):
        return
    $ msg("ex", "he put the tray down like he was serving a king")
    $ msg("ex", "and you said gracias eleven times. once each")
    label tel_chat_ex_t4_1_2:
    if telefono_minuti_blocco("tel_chat_ex_t4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I was being polite!»":
            label tel_chat_ex_t4_1_3:
            if telefono_minuti_blocco("tel_chat_ex_t4_1_3", "invia", 1):
                return
            $ msg("sara", "I was being polite!")
            $ caldo()
            label tel_chat_ex_t4_1_4:
            if telefono_minuti_blocco("tel_chat_ex_t4_1_4", "ricevi", 1):
                return
            $ msg("ex", "you were shaking by the fourth. I had to walk you round a fountain")
        "«You could have helped me drink them.»":
            label tel_chat_ex_t4_1_5:
            if telefono_minuti_blocco("tel_chat_ex_t4_1_5", "invia", 1):
                return
            $ msg("sara", "You could have helped me drink them.")
            label tel_chat_ex_t4_1_6:
            if telefono_minuti_blocco("tel_chat_ex_t4_1_6", "ricevi", 1):
                return
            $ msg("ex", "I was busy watching")
        "«We never did find out what I'd actually asked for.»":
            label tel_chat_ex_t4_1_7:
            if telefono_minuti_blocco("tel_chat_ex_t4_1_7", "invia", 1):
                return
            $ msg("sara", "We never did find out what I'd actually asked for.")
            label tel_chat_ex_t4_1_8:
            if telefono_minuti_blocco("tel_chat_ex_t4_1_8", "ricevi", 1):
                return
            $ msg("ex", "I looked it up after. you'd asked him for «one for everyone»")
            sp "One for everyone."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_t4_2:
    label tel_chat_ex_t4_2_1:
    if telefono_minuti_blocco("tel_chat_ex_t4_2_1", "ricevi", 1):
        return
    $ msg("ex", "I tell people that story. I leave your name out")
    label tel_chat_ex_t4_2_2:
    if telefono_minuti_blocco("tel_chat_ex_t4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What do you call me?»":
            label tel_chat_ex_t4_2_3:
            if telefono_minuti_blocco("tel_chat_ex_t4_2_3", "invia", 1):
                return
            $ msg("sara", "What do you call me?")
            $ caldo()
            label tel_chat_ex_t4_2_4:
            if telefono_minuti_blocco("tel_chat_ex_t4_2_4", "ricevi", 1):
                return
            $ msg("ex", "a girl I knew who couldn't hurt anybody's feelings")
            sp "It isn't even unkind. That's the worst of it."
        "«Why leave it out?»":
            label tel_chat_ex_t4_2_5:
            if telefono_minuti_blocco("tel_chat_ex_t4_2_5", "invia", 1):
                return
            $ msg("sara", "Why leave it out?")
            label tel_chat_ex_t4_2_6:
            if telefono_minuti_blocco("tel_chat_ex_t4_2_6", "ricevi", 1):
                return
            $ msg("ex", "so it stays mine")
        "«Do they laugh?»":
            label tel_chat_ex_t4_2_7:
            if telefono_minuti_blocco("tel_chat_ex_t4_2_7", "invia", 1):
                return
            $ msg("sara", "Do they laugh?")
            label tel_chat_ex_t4_2_8:
            if telefono_minuti_blocco("tel_chat_ex_t4_2_8", "ricevi", 1):
                return
            $ msg("ex", "every time. not like you did")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_t4_3:
    label tel_chat_ex_t4_3_1:
    if telefono_minuti_blocco("tel_chat_ex_t4_3_1", "ricevi", 1):
        return
    $ msg("ex", "you were loud tonight. for a second there the whole place turned round")
    label tel_chat_ex_t4_3_2:
    if telefono_minuti_blocco("tel_chat_ex_t4_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I know. I heard it too.»":
            label tel_chat_ex_t4_3_3:
            if telefono_minuti_blocco("tel_chat_ex_t4_3_3", "invia", 1):
                return
            $ msg("sara", "I know. I heard it too.")
            label tel_chat_ex_t4_3_4:
            if telefono_minuti_blocco("tel_chat_ex_t4_3_4", "ricevi", 1):
                return
            $ msg("ex", "don't put it away again")
        "«It was only a story about coffee.»":
            label tel_chat_ex_t4_3_5:
            if telefono_minuti_blocco("tel_chat_ex_t4_3_5", "invia", 1):
                return
            $ msg("sara", "It was only a story about coffee.")
            label tel_chat_ex_t4_3_6:
            if telefono_minuti_blocco("tel_chat_ex_t4_3_6", "ricevi", 2):
                return
            $ msg("ex", "yeah. it's always only something")
            $ msg("ex", "night")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t4_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_t4_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: un incontro da soli

label chat_ex_c1:
    label tel_chat_ex_c1_1:
    if telefono_minuti_blocco("tel_chat_ex_c1_1", "invia", 1):
        return
    $ msg("sara", "What's it like, your place, when it's empty?")
    return

label chat_ex_c1_entrata:
    label tel_chat_ex_c1_entrata_1:
    if telefono_minuti_blocco("tel_chat_ex_c1_entrata_1", "ricevi", 1):
        return
    $ msg("ex", "closing up. last one out")
    label tel_chat_ex_c1_entrata_2:
    if telefono_minuti_blocco("tel_chat_ex_c1_entrata_2", "invia", 1):
        return
    $ msg("sara", "What's it like, when it's empty?")
    return

label chat_ex_c1_1:
    label tel_chat_ex_c1_1_1:
    if telefono_minuti_blocco("tel_chat_ex_c1_1_1", "ricevi", 2):
        return
    $ msg("ex", "quiet. smells of lemon and last night")
    $ msg("ex", "you'd like it. there's a jukebox with a crack down the glass. plays what it wants")
    label tel_chat_ex_c1_1_2:
    if telefono_minuti_blocco("tel_chat_ex_c1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What does it want?»":
            label tel_chat_ex_c1_1_3:
            if telefono_minuti_blocco("tel_chat_ex_c1_1_3", "invia", 1):
                return
            $ msg("sara", "What does it want?")
            $ caldo()
            label tel_chat_ex_c1_1_4:
            if telefono_minuti_blocco("tel_chat_ex_c1_1_4", "ricevi", 1):
                return
            $ msg("ex", "slow stuff. it's older than it looks")
        "«I'm not asking to come.»":
            label tel_chat_ex_c1_1_5:
            if telefono_minuti_blocco("tel_chat_ex_c1_1_5", "invia", 1):
                return
            $ msg("sara", "I'm not asking to come.")
            label tel_chat_ex_c1_1_6:
            if telefono_minuti_blocco("tel_chat_ex_c1_1_6", "ricevi", 1):
                return
            $ msg("ex", "no. you're asking what it smells like")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_c1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_c1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_c1_2:
    label tel_chat_ex_c1_2_1:
    if telefono_minuti_blocco("tel_chat_ex_c1_2_1", "ricevi", 1):
        return
    $ msg("ex", "say you were here. where do you sit")
    label tel_chat_ex_c1_2_2:
    if telefono_minuti_blocco("tel_chat_ex_c1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«At the bar. Where I can see the door.»":
            label tel_chat_ex_c1_2_3:
            if telefono_minuti_blocco("tel_chat_ex_c1_2_3", "invia", 1):
                return
            $ msg("sara", "At the bar. Where I can see the door.")
            label tel_chat_ex_c1_2_4:
            if telefono_minuti_blocco("tel_chat_ex_c1_2_4", "ricevi", 1):
                return
            $ msg("ex", "smart. I'd stand where you couldn't see me and make you turn round")
        "«Nowhere. I walk about and touch everything.»":
            label tel_chat_ex_c1_2_5:
            if telefono_minuti_blocco("tel_chat_ex_c1_2_5", "invia", 1):
                return
            $ msg("sara", "Nowhere. I walk about and touch everything.")
            $ caldo()
            label tel_chat_ex_c1_2_6:
            if telefono_minuti_blocco("tel_chat_ex_c1_2_6", "ricevi", 1):
                return
            $ msg("ex", "that's the one. I'd leave you to it. I'd just listen to your shoes")
        "«I'm not there, Jacob.»":
            label tel_chat_ex_c1_2_7:
            if telefono_minuti_blocco("tel_chat_ex_c1_2_7", "invia", 1):
                return
            $ msg("sara", "I'm not there, Jacob.")
            $ frena()
            label tel_chat_ex_c1_2_8:
            if telefono_minuti_blocco("tel_chat_ex_c1_2_8", "ricevi", 1):
                return
            $ msg("ex", "no. ok. lights off then. night")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_c1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_c1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_c1_3:
    label tel_chat_ex_c1_3_1:
    if telefono_minuti_blocco("tel_chat_ex_c1_3_1", "ricevi", 1):
        return
    $ msg("ex", "I wouldn't try anything")
    label tel_chat_ex_c1_3_2:
    if telefono_minuti_blocco("tel_chat_ex_c1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Yes, you would.»":
            label tel_chat_ex_c1_3_3:
            if telefono_minuti_blocco("tel_chat_ex_c1_3_3", "invia", 1):
                return
            $ msg("sara", "Yes, you would.")
            label tel_chat_ex_c1_3_4:
            if telefono_minuti_blocco("tel_chat_ex_c1_3_4", "ricevi", 1):
                return
            $ msg("ex", "I'd try not to. it'd be interesting to watch")
        "«I'd be disappointed if you didn't.»":
            label tel_chat_ex_c1_3_5:
            if telefono_minuti_blocco("tel_chat_ex_c1_3_5", "invia", 1):
                return
            $ msg("sara", "I'd be disappointed if you didn't.")
            label tel_chat_ex_c1_3_6:
            if telefono_minuti_blocco("tel_chat_ex_c1_3_6", "ricevi", 1):
                return
            $ msg("ex", "careful. I save these")
            sp "Why did I send that?"
            label tel_chat_ex_c1_3_7:
            if telefono_minuti_blocco("tel_chat_ex_c1_3_7", "ricevi", 1):
                return
            $ msg("ex", "go to bed sara. I'll leave a stool out. doesn't mean anything. it's just a stool")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_c1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_c1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: l'attrazione che ritorna

label chat_ex_c2:
    label tel_chat_ex_c2_1:
    if telefono_minuti_blocco("tel_chat_ex_c2_1", "invia", 1):
        return
    $ msg("sara", "You still write to me at the worst possible hour.")
    return

label chat_ex_c2_entrata:
    label tel_chat_ex_c2_entrata_1:
    if telefono_minuti_blocco("tel_chat_ex_c2_entrata_1", "ricevi", 1):
        return
    $ msg("ex", "you up")
    label tel_chat_ex_c2_entrata_2:
    if telefono_minuti_blocco("tel_chat_ex_c2_entrata_2", "invia", 1):
        return
    $ msg("sara", "You still write at the worst possible hour.")
    return

label chat_ex_c2_1:
    label tel_chat_ex_c2_1_1:
    if telefono_minuti_blocco("tel_chat_ex_c2_1_1", "ricevi", 1):
        return
    $ msg("ex", "it's the only one with no one else in it")
    label tel_chat_ex_c2_1_2:
    if telefono_minuti_blocco("tel_chat_ex_c2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I should have been asleep.»":
            label tel_chat_ex_c2_1_3:
            if telefono_minuti_blocco("tel_chat_ex_c2_1_3", "invia", 1):
                return
            $ msg("sara", "I should have been asleep.")
            label tel_chat_ex_c2_1_4:
            if telefono_minuti_blocco("tel_chat_ex_c2_1_4", "ricevi", 1):
                return
            $ msg("ex", "you've never been asleep at one in the morning in your life")
        "«I was waiting to see if you would.»":
            label tel_chat_ex_c2_1_5:
            if telefono_minuti_blocco("tel_chat_ex_c2_1_5", "invia", 1):
                return
            $ msg("sara", "I was waiting to see if you would.")
            $ caldo()
            label tel_chat_ex_c2_1_6:
            if telefono_minuti_blocco("tel_chat_ex_c2_1_6", "ricevi", 1):
                return
            $ msg("ex", "say that again without the little pause before it")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_c2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_c2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_c2_2:
    label tel_chat_ex_c2_2_1:
    if telefono_minuti_blocco("tel_chat_ex_c2_2_1", "ricevi", 2):
        return
    $ msg("ex", "what are you wearing. I'm kidding")
    $ msg("ex", "I'm mostly kidding")
    label tel_chat_ex_c2_2_2:
    if telefono_minuti_blocco("tel_chat_ex_c2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«A jumper you'd hate.»":
            label tel_chat_ex_c2_2_3:
            if telefono_minuti_blocco("tel_chat_ex_c2_2_3", "invia", 1):
                return
            $ msg("sara", "A jumper you'd hate.")
            label tel_chat_ex_c2_2_4:
            if telefono_minuti_blocco("tel_chat_ex_c2_2_4", "ricevi", 1):
                return
            $ msg("ex", "down to the knees. sleeves over your hands. I don't hate it. I used to find it on chairs")
        "«Not much. It's hot up here.»":
            label tel_chat_ex_c2_2_5:
            if telefono_minuti_blocco("tel_chat_ex_c2_2_5", "invia", 1):
                return
            $ msg("sara", "Not much. It's hot up here.")
            $ caldo()
            label tel_chat_ex_c2_2_6:
            if telefono_minuti_blocco("tel_chat_ex_c2_2_6", "ricevi", 1):
                return
            $ msg("ex", "ok. I've put the phone down. I've picked it up again. that's where we are")
        "«Mind your own business.»":
            label tel_chat_ex_c2_2_7:
            if telefono_minuti_blocco("tel_chat_ex_c2_2_7", "invia", 1):
                return
            $ msg("sara", "Mind your own business.")
            label tel_chat_ex_c2_2_8:
            if telefono_minuti_blocco("tel_chat_ex_c2_2_8", "ricevi", 1):
                return
            $ msg("ex", "it was my business once. I was very good at it")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_c2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_c2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_c2_3:
    label tel_chat_ex_c2_3_1:
    if telefono_minuti_blocco("tel_chat_ex_c2_3_1", "ricevi", 1):
        return
    $ msg("ex", "do you ever think about it. not me. it")
    label tel_chat_ex_c2_3_2:
    if telefono_minuti_blocco("tel_chat_ex_c2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«More than I'd like.»":
            label tel_chat_ex_c2_3_3:
            if telefono_minuti_blocco("tel_chat_ex_c2_3_3", "invia", 1):
                return
            $ msg("sara", "More than I'd like.")
            label tel_chat_ex_c2_3_4:
            if telefono_minuti_blocco("tel_chat_ex_c2_3_4", "ricevi", 1):
                return
            $ msg("ex", "me too. more than I'd say out loud")
        "«I think about how loud I used to be.»":
            label tel_chat_ex_c2_3_5:
            if telefono_minuti_blocco("tel_chat_ex_c2_3_5", "invia", 1):
                return
            $ msg("sara", "I think about how loud I used to be.")
            label tel_chat_ex_c2_3_6:
            if telefono_minuti_blocco("tel_chat_ex_c2_3_6", "ricevi", 1):
                return
            $ msg("ex", "the neighbours moved")
            sp "They did. They actually moved."
        "«No, and nor should you.»":
            label tel_chat_ex_c2_3_7:
            if telefono_minuti_blocco("tel_chat_ex_c2_3_7", "invia", 1):
                return
            $ msg("sara", "No, and nor should you.")
            $ frena()
            label tel_chat_ex_c2_3_8:
            if telefono_minuti_blocco("tel_chat_ex_c2_3_8", "ricevi", 1):
                return
            $ msg("ex", "I'll try to be a better man by breakfast")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_c2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_c2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: desideri mai dimenticati

label chat_ex_d1:
    label tel_chat_ex_d1_1:
    if telefono_minuti_blocco("tel_chat_ex_d1_1", "invia", 1):
        return
    $ msg("sara", "I can still feel your hand on the back of my neck.")
    return

label chat_ex_d1_1:
    label tel_chat_ex_d1_1_1:
    if telefono_minuti_blocco("tel_chat_ex_d1_1_1", "ricevi", 1):
        return
    $ msg("ex", "it's still warm. I haven't washed it")
    label tel_chat_ex_d1_1_2:
    if telefono_minuti_blocco("tel_chat_ex_d1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Idiot.»":
            label tel_chat_ex_d1_1_3:
            if telefono_minuti_blocco("tel_chat_ex_d1_1_3", "invia", 1):
                return
            $ msg("sara", "Idiot.")
            $ caldo()
            label tel_chat_ex_d1_1_4:
            if telefono_minuti_blocco("tel_chat_ex_d1_1_4", "ricevi", 1):
                return
            $ msg("ex", "yours. occasionally")
        "«I keep going over it.»":
            label tel_chat_ex_d1_1_5:
            if telefono_minuti_blocco("tel_chat_ex_d1_1_5", "invia", 1):
                return
            $ msg("sara", "I keep going over it.")
            label tel_chat_ex_d1_1_6:
            if telefono_minuti_blocco("tel_chat_ex_d1_1_6", "ricevi", 1):
                return
            $ msg("ex", "where do you start")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_d1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_d1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_d1_2:
    label tel_chat_ex_d1_2_1:
    if telefono_minuti_blocco("tel_chat_ex_d1_2_1", "ricevi", 1):
        return
    $ msg("ex", "tell me what you want and I'll tell you what I remember. we'll see where they meet")
    label tel_chat_ex_d1_2_2:
    if telefono_minuti_blocco("tel_chat_ex_d1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I want it slow. You were always in a hurry.»":
            label tel_chat_ex_d1_2_3:
            if telefono_minuti_blocco("tel_chat_ex_d1_2_3", "invia", 1):
                return
            $ msg("sara", "I want it slow. You were always in a hurry.")
            $ caldo()
            label tel_chat_ex_d1_2_4:
            if telefono_minuti_blocco("tel_chat_ex_d1_2_4", "ricevi", 1):
                return
            $ msg("ex", "I'm older. I've learned to read the whole page")
        "«I want you to stop asking and tell me.»":
            label tel_chat_ex_d1_2_5:
            if telefono_minuti_blocco("tel_chat_ex_d1_2_5", "invia", 1):
                return
            $ msg("sara", "I want you to stop asking and tell me.")
            label tel_chat_ex_d1_2_6:
            if telefono_minuti_blocco("tel_chat_ex_d1_2_6", "ricevi", 1):
                return
            $ msg("ex", "lie back. put the phone by your ear. now you're mine till the battery goes")
        "«You first.»":
            label tel_chat_ex_d1_2_7:
            if telefono_minuti_blocco("tel_chat_ex_d1_2_7", "invia", 1):
                return
            $ msg("sara", "You first.")
            label tel_chat_ex_d1_2_8:
            if telefono_minuti_blocco("tel_chat_ex_d1_2_8", "ricevi", 1):
                return
            $ msg("ex", "you used to shut your eyes right before. I'd wait for it. I'd do anything to get there")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_d1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_d1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_d1_3:
    label tel_chat_ex_d1_3_1:
    if telefono_minuti_blocco("tel_chat_ex_d1_3_1", "ricevi", 1):
        return
    $ msg("ex", "you're being quiet")
    label tel_chat_ex_d1_3_2:
    if telefono_minuti_blocco("tel_chat_ex_d1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«There's someone asleep in the next room.»":
            label tel_chat_ex_d1_3_3:
            if telefono_minuti_blocco("tel_chat_ex_d1_3_3", "invia", 1):
                return
            $ msg("sara", "There's someone asleep in the next room.")
            label tel_chat_ex_d1_3_4:
            if telefono_minuti_blocco("tel_chat_ex_d1_3_4", "ricevi", 1):
                return
            $ msg("ex", "then bite something")
        "«I'm not going to be quiet for much longer.»":
            label tel_chat_ex_d1_3_5:
            if telefono_minuti_blocco("tel_chat_ex_d1_3_5", "invia", 1):
                return
            $ msg("sara", "I'm not going to be quiet for much longer.")
            label tel_chat_ex_d1_3_6:
            if telefono_minuti_blocco("tel_chat_ex_d1_3_6", "ricevi", 2):
                return
            $ msg("ex", "there she is. four years. there she is")
            $ msg("ex", "sleep now. I'll know if you don't")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_d1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_d1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: esclusività e libertà

label chat_ex_d2:
    label tel_chat_ex_d2_1:
    if telefono_minuti_blocco("tel_chat_ex_d2_1", "invia", 1):
        return
    $ msg("sara", "Are you on your own tonight?")
    return

label chat_ex_d2_1:
    label tel_chat_ex_d2_1_1:
    if telefono_minuti_blocco("tel_chat_ex_d2_1_1", "ricevi", 1):
        return
    $ msg("ex", "would it matter")
    label tel_chat_ex_d2_1_2:
    if telefono_minuti_blocco("tel_chat_ex_d2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«No. I was curious.»":
            label tel_chat_ex_d2_1_3:
            if telefono_minuti_blocco("tel_chat_ex_d2_1_3", "invia", 1):
                return
            $ msg("sara", "No. I was curious.")
            $ caldo()
            label tel_chat_ex_d2_1_4:
            if telefono_minuti_blocco("tel_chat_ex_d2_1_4", "ricevi", 1):
                return
            $ msg("ex", "you really are different. I like it. it's a bit frightening")
        "«A little.»":
            label tel_chat_ex_d2_1_5:
            if telefono_minuti_blocco("tel_chat_ex_d2_1_5", "invia", 1):
                return
            $ msg("sara", "A little.")
            label tel_chat_ex_d2_1_6:
            if telefono_minuti_blocco("tel_chat_ex_d2_1_6", "ricevi", 1):
                return
            $ msg("ex", "then yes. just me and the jukebox")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_d2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_d2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_d2_2:
    label tel_chat_ex_d2_2_1:
    if telefono_minuti_blocco("tel_chat_ex_d2_2_1", "ricevi", 1):
        return
    $ msg("ex", "you can ask me who and when and I'll tell you. that's new. I never used to")
    label tel_chat_ex_d2_2_2:
    if telefono_minuti_blocco("tel_chat_ex_d2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Tell me about the last one. Slowly.»":
            label tel_chat_ex_d2_2_3:
            if telefono_minuti_blocco("tel_chat_ex_d2_2_3", "invia", 1):
                return
            $ msg("sara", "Tell me about the last one. Slowly.")
            $ caldo()
            label tel_chat_ex_d2_2_4:
            if telefono_minuti_blocco("tel_chat_ex_d2_2_4", "ricevi", 1):
                return
            $ msg("ex", "you want that")
        "«I want to see if I mind.»":
            label tel_chat_ex_d2_2_5:
            if telefono_minuti_blocco("tel_chat_ex_d2_2_5", "invia", 1):
                return
            $ msg("sara", "I want to see if I mind.")
            sp "I don't mind. My heart's going like mad and I don't mind."
        "«I'd rather you told me about me.»":
            label tel_chat_ex_d2_2_6:
            if telefono_minuti_blocco("tel_chat_ex_d2_2_6", "invia", 1):
                return
            $ msg("sara", "I'd rather you told me about me.")
            label tel_chat_ex_d2_2_7:
            if telefono_minuti_blocco("tel_chat_ex_d2_2_7", "ricevi", 1):
                return
            $ msg("ex", "that's easier. that's a longer story. get comfortable")
        "«Not tonight. Just talk to me.»":
            label tel_chat_ex_d2_2_8:
            if telefono_minuti_blocco("tel_chat_ex_d2_2_8", "invia", 1):
                return
            $ msg("sara", "Not tonight. Just talk to me.")
            label tel_chat_ex_d2_2_9:
            if telefono_minuti_blocco("tel_chat_ex_d2_2_9", "ricevi", 1):
                return
            $ msg("ex", "all right. your shoulder. the left one. I'll work down from there")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_d2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_d2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_ex_d2_3:
    label tel_chat_ex_d2_3_1:
    if telefono_minuti_blocco("tel_chat_ex_d2_3_1", "ricevi", 1):
        return
    $ msg("ex", "so do you mind")
    label tel_chat_ex_d2_3_2:
    if telefono_minuti_blocco("tel_chat_ex_d2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Not the way I used to.»":
            label tel_chat_ex_d2_3_3:
            if telefono_minuti_blocco("tel_chat_ex_d2_3_3", "invia", 1):
                return
            $ msg("sara", "Not the way I used to.")
            label tel_chat_ex_d2_3_4:
            if telefono_minuti_blocco("tel_chat_ex_d2_3_4", "ricevi", 1):
                return
            $ msg("ex", "what's the way now")
        "«Come and find out, one of these nights.»":
            label tel_chat_ex_d2_3_5:
            if telefono_minuti_blocco("tel_chat_ex_d2_3_5", "invia", 1):
                return
            $ msg("sara", "Come and find out, one of these nights.")
            label tel_chat_ex_d2_3_6:
            if telefono_minuti_blocco("tel_chat_ex_d2_3_6", "ricevi", 2):
                return
            $ msg("ex", "I'll leave the side door. it's always been the side door with us")
            $ msg("ex", "night, loud girl")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_d2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_ex_d2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return
