## GENERATO da tools/telefono/componi.py: si modifica tools/telefono/simon.txt.

init python:
    discorso("simon_t1", "simon", CONOSCENTI, argomento="The cables", se="fatto('ep2_d15_cavi_simon')")
    discorso("simon_t2", "simon", CONOSCENTI, argomento="The evening I came alone", se="fatto('ep1_palestra_da_sola')")
    discorso("simon_t3", "simon", CONOSCENTI, argomento="Both shoulders", se="fatto('ep1_d8_seconda_spalla')")
    discorso("simon_t4", "simon", CONOSCENTI, argomento="Page fifty", se="fatto('ep1_d6_parla_simon')")
    discorso("simon_t5", "simon", CONOSCENTI, argomento="Gym squad", se="giorno >= 15")
    discorso("simon_c1", "simon", COMPLICI, flirt=True)
    discorso("simon_c2", "simon", COMPLICI, flirt=True)
    discorso("simon_c3", "simon", COMPLICI, flirt=True)
    discorso("simon_d1", "simon", INTIMI, flirt=True)
    discorso("simon_d2", "simon", INTIMI, flirt=True)


## --- The cables

label chat_simon_t1:
    label tel_chat_simon_t1_1:
    if telefono_minuti_blocco("tel_chat_simon_t1_1", "invia", 1):
        return
    $ msg("sara", "My arms are still shaking from the cables.")
    return

label chat_simon_t1_entrata:
    label tel_chat_simon_t1_entrata_1:
    if telefono_minuti_blocco("tel_chat_simon_t1_entrata_1", "ricevi", 1):
        return
    $ msg("simon", "Checking in on the new cable athlete. How are the arms?")
    label tel_chat_simon_t1_entrata_2:
    if telefono_minuti_blocco("tel_chat_simon_t1_entrata_2", "invia", 1):
        return
    $ msg("sara", "Still shaking.")
    return

label chat_simon_t1_1:
    label tel_chat_simon_t1_1_1:
    if telefono_minuti_blocco("tel_chat_simon_t1_1_1", "ricevi", 1):
        return
    $ msg("simon", "Ha. Good shaking or bad shaking?")
    label tel_chat_simon_t1_1_2:
    if telefono_minuti_blocco("tel_chat_simon_t1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Good. I think.»":
            label tel_chat_simon_t1_1_3:
            if telefono_minuti_blocco("tel_chat_simon_t1_1_3", "invia", 1):
                return
            $ msg("sara", "Good. I think.")
            $ caldo()
            label tel_chat_simon_t1_1_4:
            if telefono_minuti_blocco("tel_chat_simon_t1_1_4", "ricevi", 1):
                return
            $ msg("simon", "Good. Bad is when you can't hold the kettle.")
        "«I can't lift my toothbrush.»":
            label tel_chat_simon_t1_1_5:
            if telefono_minuti_blocco("tel_chat_simon_t1_1_5", "invia", 1):
                return
            $ msg("sara", "I can't lift my toothbrush.")
            label tel_chat_simon_t1_1_6:
            if telefono_minuti_blocco("tel_chat_simon_t1_1_6", "ricevi", 1):
                return
            $ msg("simon", "Switch hands. It's a workout for the other one.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_t1_2:
    label tel_chat_simon_t1_2_1:
    if telefono_minuti_blocco("tel_chat_simon_t1_2_1", "ricevi", 1):
        return
    $ msg("simon", "You rush the way back. Everybody does. The weight wants to win.")
    label tel_chat_simon_t1_2_2:
    if telefono_minuti_blocco("tel_chat_simon_t1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I was a bit distracted.»":
            label tel_chat_simon_t1_2_3:
            if telefono_minuti_blocco("tel_chat_simon_t1_2_3", "invia", 1):
                return
            $ msg("sara", "I was a bit distracted.")
            label tel_chat_simon_t1_2_4:
            if telefono_minuti_blocco("tel_chat_simon_t1_2_4", "ricevi", 1):
                return
            $ msg("simon", "Yeah. Me too. Sorry about that. I lost count on seven.")
            sp "He noticed. He noticed me noticing."
        "«Show me again next time?»":
            label tel_chat_simon_t1_2_5:
            if telefono_minuti_blocco("tel_chat_simon_t1_2_5", "invia", 1):
                return
            $ msg("sara", "Show me again next time?")
            $ caldo()
            label tel_chat_simon_t1_2_6:
            if telefono_minuti_blocco("tel_chat_simon_t1_2_6", "ricevi", 1):
                return
            $ msg("simon", "Sure. I'll stand behind you, so I can see the elbows.")
        "«I'll go slower.»":
            label tel_chat_simon_t1_2_7:
            if telefono_minuti_blocco("tel_chat_simon_t1_2_7", "invia", 1):
                return
            $ msg("sara", "I'll go slower.")
            label tel_chat_simon_t1_2_8:
            if telefono_minuti_blocco("tel_chat_simon_t1_2_8", "ricevi", 1):
                return
            $ msg("simon", "Half the weight, twice the time. You'll hate me by Thursday.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_t1_3:
    label tel_chat_simon_t1_3_1:
    if telefono_minuti_blocco("tel_chat_simon_t1_3_1", "ricevi", 1):
        return
    $ msg("simon", "Can I say one thing, as your trainer?")
    label tel_chat_simon_t1_3_2:
    if telefono_minuti_blocco("tel_chat_simon_t1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«As my trainer.»":
            label tel_chat_simon_t1_3_3:
            if telefono_minuti_blocco("tel_chat_simon_t1_3_3", "invia", 1):
                return
            $ msg("sara", "As my trainer.")
            label tel_chat_simon_t1_3_4:
            if telefono_minuti_blocco("tel_chat_simon_t1_3_4", "ricevi", 1):
                return
            $ msg("simon", "You stopped apologising to the machine. Progress.")
        "«Is it a nice thing?»":
            label tel_chat_simon_t1_3_5:
            if telefono_minuti_blocco("tel_chat_simon_t1_3_5", "invia", 1):
                return
            $ msg("sara", "Is it a nice thing?")
            label tel_chat_simon_t1_3_6:
            if telefono_minuti_blocco("tel_chat_simon_t1_3_6", "ricevi", 1):
                return
            $ msg("simon", "It's a true thing. You looked strong.")
        "«Only if it's about elbows.»":
            label tel_chat_simon_t1_3_7:
            if telefono_minuti_blocco("tel_chat_simon_t1_3_7", "invia", 1):
                return
            $ msg("sara", "Only if it's about elbows.")
            label tel_chat_simon_t1_3_8:
            if telefono_minuti_blocco("tel_chat_simon_t1_3_8", "ricevi", 1):
                return
            $ msg("simon", "It's entirely about elbows. They were excellent elbows.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The evening I came alone

label chat_simon_t2:
    label tel_chat_simon_t2_1:
    if telefono_minuti_blocco("tel_chat_simon_t2_1", "invia", 1):
        return
    $ msg("sara", "I nearly turned round and went home, that night Joanie didn't come.")
    return

label chat_simon_t2_entrata:
    label tel_chat_simon_t2_entrata_1:
    if telefono_minuti_blocco("tel_chat_simon_t2_entrata_1", "ricevi", 1):
        return
    $ msg("simon", "Was just thinking about the night you came on your own.")
    label tel_chat_simon_t2_entrata_2:
    if telefono_minuti_blocco("tel_chat_simon_t2_entrata_2", "invia", 1):
        return
    $ msg("sara", "I nearly turned round and went home.")
    return

label chat_simon_t2_1:
    label tel_chat_simon_t2_1_1:
    if telefono_minuti_blocco("tel_chat_simon_t2_1_1", "ricevi", 1):
        return
    $ msg("simon", "I know. I saw you through the glass. You read the timetable for five minutes.")
    label tel_chat_simon_t2_1_2:
    if telefono_minuti_blocco("tel_chat_simon_t2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It's a very complicated timetable.»":
            label tel_chat_simon_t2_1_3:
            if telefono_minuti_blocco("tel_chat_simon_t2_1_3", "invia", 1):
                return
            $ msg("sara", "It's a very complicated timetable.")
            $ caldo()
            label tel_chat_simon_t2_1_4:
            if telefono_minuti_blocco("tel_chat_simon_t2_1_4", "ricevi", 1):
                return
            $ msg("simon", "It's got four lines on it.")
        "«You could have come out.»":
            label tel_chat_simon_t2_1_5:
            if telefono_minuti_blocco("tel_chat_simon_t2_1_5", "invia", 1):
                return
            $ msg("sara", "You could have come out.")
            label tel_chat_simon_t2_1_6:
            if telefono_minuti_blocco("tel_chat_simon_t2_1_6", "ricevi", 1):
                return
            $ msg("simon", "I thought about it. Then you'd have had to come in for me. I wanted you to come in for you.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_t2_2:
    label tel_chat_simon_t2_2_1:
    if telefono_minuti_blocco("tel_chat_simon_t2_2_1", "ricevi", 1):
        return
    $ msg("simon", "First time through the door on your own is the heaviest thing in the building.")
    label tel_chat_simon_t2_2_2:
    if telefono_minuti_blocco("tel_chat_simon_t2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What was yours like?»":
            label tel_chat_simon_t2_2_3:
            if telefono_minuti_blocco("tel_chat_simon_t2_2_3", "invia", 1):
                return
            $ msg("sara", "What was yours like?")
            label tel_chat_simon_t2_2_4:
            if telefono_minuti_blocco("tel_chat_simon_t2_2_4", "ricevi", 1):
                return
            $ msg("simon", "I was twenty-two and twice this size. I walked round the block nine times. Tenth time it rained.")
        "«I've never told anyone how scared I was.»":
            label tel_chat_simon_t2_2_5:
            if telefono_minuti_blocco("tel_chat_simon_t2_2_5", "invia", 1):
                return
            $ msg("sara", "I've never told anyone how scared I was.")
            $ caldo()
            label tel_chat_simon_t2_2_6:
            if telefono_minuti_blocco("tel_chat_simon_t2_2_6", "ricevi", 1):
                return
            $ msg("simon", "I won't put it on the board.")
        "«Joanie did it on purpose, I think.»":
            label tel_chat_simon_t2_2_7:
            if telefono_minuti_blocco("tel_chat_simon_t2_2_7", "invia", 1):
                return
            $ msg("sara", "Joanie did it on purpose, I think.")
            label tel_chat_simon_t2_2_8:
            if telefono_minuti_blocco("tel_chat_simon_t2_2_8", "ricevi", 1):
                return
            $ msg("simon", "She might have. She's a good friend. Bit of a strategist.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_t2_3:
    label tel_chat_simon_t2_3_1:
    if telefono_minuti_blocco("tel_chat_simon_t2_3_1", "ricevi", 1):
        return
    $ msg("simon", "You stayed an hour and ten, you know. I'd have bet on twenty minutes.")
    label tel_chat_simon_t2_3_2:
    if telefono_minuti_blocco("tel_chat_simon_t2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You bet against me?»":
            label tel_chat_simon_t2_3_3:
            if telefono_minuti_blocco("tel_chat_simon_t2_3_3", "invia", 1):
                return
            $ msg("sara", "You bet against me?")
            label tel_chat_simon_t2_3_4:
            if telefono_minuti_blocco("tel_chat_simon_t2_3_4", "ricevi", 1):
                return
            $ msg("simon", "Never again. I owe myself a smoothie.")
        "«I liked it better on my own.»":
            label tel_chat_simon_t2_3_5:
            if telefono_minuti_blocco("tel_chat_simon_t2_3_5", "invia", 1):
                return
            $ msg("sara", "I liked it better on my own.")
            label tel_chat_simon_t2_3_6:
            if telefono_minuti_blocco("tel_chat_simon_t2_3_6", "ricevi", 1):
                return
            $ msg("simon", "Yeah? Come on a Tuesday, then. It's dead. You can have the whole mirror.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Both shoulders

label chat_simon_t3:
    label tel_chat_simon_t3_1:
    if telefono_minuti_blocco("tel_chat_simon_t3_1", "invia", 1):
        return
    $ msg("sara", "My left shoulder would like you to know it's behaving.")
    return

label chat_simon_t3_entrata:
    label tel_chat_simon_t3_entrata_1:
    if telefono_minuti_blocco("tel_chat_simon_t3_entrata_1", "ricevi", 1):
        return
    $ msg("simon", "Trainer question. How's that left shoulder?")
    label tel_chat_simon_t3_entrata_2:
    if telefono_minuti_blocco("tel_chat_simon_t3_entrata_2", "invia", 1):
        return
    $ msg("sara", "Behaving itself.")
    return

label chat_simon_t3_1:
    label tel_chat_simon_t3_1_1:
    if telefono_minuti_blocco("tel_chat_simon_t3_1_1", "ricevi", 1):
        return
    $ msg("simon", "Glad to hear it. And the right?")
    label tel_chat_simon_t3_1_2:
    if telefono_minuti_blocco("tel_chat_simon_t3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Jealous.»":
            label tel_chat_simon_t3_1_3:
            if telefono_minuti_blocco("tel_chat_simon_t3_1_3", "invia", 1):
                return
            $ msg("sara", "Jealous.")
            $ caldo()
            label tel_chat_simon_t3_1_4:
            if telefono_minuti_blocco("tel_chat_simon_t3_1_4", "ricevi", 1):
                return
            $ msg("simon", "Tell it to wait its turn. I treat them equally.")
        "«It creeps up when I type.»":
            label tel_chat_simon_t3_1_5:
            if telefono_minuti_blocco("tel_chat_simon_t3_1_5", "invia", 1):
                return
            $ msg("sara", "It creeps up when I type.")
            label tel_chat_simon_t3_1_6:
            if telefono_minuti_blocco("tel_chat_simon_t3_1_6", "ricevi", 1):
                return
            $ msg("simon", "Everyone's does. Drop it, breathe out. Better?")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_t3_2:
    label tel_chat_simon_t3_2_1:
    if telefono_minuti_blocco("tel_chat_simon_t3_2_1", "ricevi", 1):
        return
    $ msg("simon", "I should say. If I ever get too hands-on, just tell me. I'd rather know.")
    label tel_chat_simon_t3_2_2:
    if telefono_minuti_blocco("tel_chat_simon_t3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You asked first. I remember.»":
            label tel_chat_simon_t3_2_3:
            if telefono_minuti_blocco("tel_chat_simon_t3_2_3", "invia", 1):
                return
            $ msg("sara", "You asked first. I remember.")
            label tel_chat_simon_t3_2_4:
            if telefono_minuti_blocco("tel_chat_simon_t3_2_4", "ricevi", 1):
                return
            $ msg("simon", "Always. My old coach never did. I swore I would.")
        "«I'm the one who asked for the other one.»":
            label tel_chat_simon_t3_2_5:
            if telefono_minuti_blocco("tel_chat_simon_t3_2_5", "invia", 1):
                return
            $ msg("sara", "I'm the one who asked for the other one.")
            $ caldo()
            label tel_chat_simon_t3_2_6:
            if telefono_minuti_blocco("tel_chat_simon_t3_2_6", "ricevi", 1):
                return
            $ msg("simon", "You did. I thought about that on the bus home.")
            sp "He thought about it on the bus."
        "«I'd tell you.»":
            label tel_chat_simon_t3_2_7:
            if telefono_minuti_blocco("tel_chat_simon_t3_2_7", "invia", 1):
                return
            $ msg("sara", "I'd tell you.")
            label tel_chat_simon_t3_2_8:
            if telefono_minuti_blocco("tel_chat_simon_t3_2_8", "ricevi", 1):
                return
            $ msg("simon", "Good. That's all I need.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_t3_3:
    label tel_chat_simon_t3_3_1:
    if telefono_minuti_blocco("tel_chat_simon_t3_3_1", "ricevi", 1):
        return
    $ msg("simon", "Physio hat on: ten minutes a day, against a wall. Arms like a goalpost.")
    label tel_chat_simon_t3_3_2:
    if telefono_minuti_blocco("tel_chat_simon_t3_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'll look ridiculous.»":
            label tel_chat_simon_t3_3_3:
            if telefono_minuti_blocco("tel_chat_simon_t3_3_3", "invia", 1):
                return
            $ msg("sara", "I'll look ridiculous.")
            label tel_chat_simon_t3_3_4:
            if telefono_minuti_blocco("tel_chat_simon_t3_3_4", "ricevi", 1):
                return
            $ msg("simon", "You'll look like everyone I respect.")
        "«And if I do it wrong?»":
            label tel_chat_simon_t3_3_5:
            if telefono_minuti_blocco("tel_chat_simon_t3_3_5", "invia", 1):
                return
            $ msg("sara", "And if I do it wrong?")
            label tel_chat_simon_t3_3_6:
            if telefono_minuti_blocco("tel_chat_simon_t3_3_6", "ricevi", 1):
                return
            $ msg("simon", "Then I'll have to check. Professionally. Both sides ;)")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t3_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t3_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Page fifty

label chat_simon_t4:
    label tel_chat_simon_t4_1:
    if telefono_minuti_blocco("tel_chat_simon_t4_1", "invia", 1):
        return
    $ msg("sara", "You owe me an apology. I got past page fifty.")
    return

label chat_simon_t4_1:
    label tel_chat_simon_t4_1_1:
    if telefono_minuti_blocco("tel_chat_simon_t4_1_1", "ricevi", 1):
        return
    $ msg("simon", "No way. Really?")
    label tel_chat_simon_t4_1_2:
    if telefono_minuti_blocco("tel_chat_simon_t4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Fifty and a bit.»":
            label tel_chat_simon_t4_1_3:
            if telefono_minuti_blocco("tel_chat_simon_t4_1_3", "invia", 1):
                return
            $ msg("sara", "Fifty and a bit.")
            $ caldo()
            label tel_chat_simon_t4_1_4:
            if telefono_minuti_blocco("tel_chat_simon_t4_1_4", "ricevi", 1):
                return
            $ msg("simon", "I take it all back. Minute twelve on the treadmill AND page fifty.")
        "«It took me two years.»":
            label tel_chat_simon_t4_1_5:
            if telefono_minuti_blocco("tel_chat_simon_t4_1_5", "invia", 1):
                return
            $ msg("sara", "It took me two years.")
            label tel_chat_simon_t4_1_6:
            if telefono_minuti_blocco("tel_chat_simon_t4_1_6", "ricevi", 1):
                return
            $ msg("simon", "So? I've had people take two years to do one pull-up. We threw a party.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_t4_2:
    label tel_chat_simon_t4_2_1:
    if telefono_minuti_blocco("tel_chat_simon_t4_2_1", "ricevi", 1):
        return
    $ msg("simon", "What's it about? I should have asked you at the party. I was too busy being funny.")
    label tel_chat_simon_t4_2_2:
    if telefono_minuti_blocco("tel_chat_simon_t4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«A woman who walks into a room that isn't hers.»":
            label tel_chat_simon_t4_2_3:
            if telefono_minuti_blocco("tel_chat_simon_t4_2_3", "invia", 1):
                return
            $ msg("sara", "A woman who walks into a room that isn't hers.")
            label tel_chat_simon_t4_2_4:
            if telefono_minuti_blocco("tel_chat_simon_t4_2_4", "ricevi", 1):
                return
            $ msg("simon", "And does she leave?")
        "«Wanting things.»":
            label tel_chat_simon_t4_2_5:
            if telefono_minuti_blocco("tel_chat_simon_t4_2_5", "invia", 1):
                return
            $ msg("sara", "Wanting things.")
            $ caldo()
            label tel_chat_simon_t4_2_6:
            if telefono_minuti_blocco("tel_chat_simon_t4_2_6", "ricevi", 1):
                return
            $ msg("simon", "That'd be a long book, if I wrote it. Mostly about pizza.")
        "«I'm not allowed to say yet.»":
            label tel_chat_simon_t4_2_7:
            if telefono_minuti_blocco("tel_chat_simon_t4_2_7", "invia", 1):
                return
            $ msg("sara", "I'm not allowed to say yet.")
            label tel_chat_simon_t4_2_8:
            if telefono_minuti_blocco("tel_chat_simon_t4_2_8", "ricevi", 1):
                return
            $ msg("simon", "Fair. I don't show people my programmes either, till they work.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_t4_3:
    label tel_chat_simon_t4_3_1:
    if telefono_minuti_blocco("tel_chat_simon_t4_3_1", "ricevi", 1):
        return
    $ msg("simon", "I don't read much. I'd read that, though.")
    label tel_chat_simon_t4_3_2:
    if telefono_minuti_blocco("tel_chat_simon_t4_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You'd give up at page ten.»":
            label tel_chat_simon_t4_3_3:
            if telefono_minuti_blocco("tel_chat_simon_t4_3_3", "invia", 1):
                return
            $ msg("sara", "You'd give up at page ten.")
            label tel_chat_simon_t4_3_4:
            if telefono_minuti_blocco("tel_chat_simon_t4_3_4", "ricevi", 1):
                return
            $ msg("simon", "Minute ten. I walked into that.")
        "«I'll lend it to you when it's done.»":
            label tel_chat_simon_t4_3_5:
            if telefono_minuti_blocco("tel_chat_simon_t4_3_5", "invia", 1):
                return
            $ msg("sara", "I'll lend it to you when it's done.")
            label tel_chat_simon_t4_3_6:
            if telefono_minuti_blocco("tel_chat_simon_t4_3_6", "ricevi", 1):
                return
            $ msg("simon", "Deal. Write something in the front. Nothing about elbows.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t4_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t4_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Gym squad

label chat_simon_t5:
    label tel_chat_simon_t5_1:
    if telefono_minuti_blocco("tel_chat_simon_t5_1", "invia", 1):
        return
    $ msg("sara", "Has Joanie posted in Gym squad again?")
    return

label chat_simon_t5_entrata:
    label tel_chat_simon_t5_entrata_1:
    if telefono_minuti_blocco("tel_chat_simon_t5_entrata_1", "ricevi", 1):
        return
    $ msg("simon", "Have you seen Gym squad today?")
    label tel_chat_simon_t5_entrata_2:
    if telefono_minuti_blocco("tel_chat_simon_t5_entrata_2", "invia", 1):
        return
    $ msg("sara", "I'm scared to look. What's Joanie posted?")
    return

label chat_simon_t5_1:
    label tel_chat_simon_t5_1_1:
    if telefono_minuti_blocco("tel_chat_simon_t5_1_1", "ricevi", 1):
        return
    $ msg("simon", "Eleven photos. Nine are of the vending machine.")
    label tel_chat_simon_t5_1_2:
    if telefono_minuti_blocco("tel_chat_simon_t5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And the other two?»":
            label tel_chat_simon_t5_1_3:
            if telefono_minuti_blocco("tel_chat_simon_t5_1_3", "invia", 1):
                return
            $ msg("sara", "And the other two?")
            $ caldo()
            label tel_chat_simon_t5_1_4:
            if telefono_minuti_blocco("tel_chat_simon_t5_1_4", "ricevi", 1):
                return
            $ msg("simon", "You, mid-squat. It's a good one. Your back's dead straight.")
        "«Please tell me I'm not in any.»":
            label tel_chat_simon_t5_1_5:
            if telefono_minuti_blocco("tel_chat_simon_t5_1_5", "invia", 1):
                return
            $ msg("sara", "Please tell me I'm not in any.")
            label tel_chat_simon_t5_1_6:
            if telefono_minuti_blocco("tel_chat_simon_t5_1_6", "ricevi", 1):
                return
            $ msg("simon", "I could tell you that.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_t5_2:
    label tel_chat_simon_t5_2_1:
    if telefono_minuti_blocco("tel_chat_simon_t5_2_1", "ricevi", 1):
        return
    $ msg("simon", "She's put me down as «Head of Arms». I've asked for a transfer.")
    label tel_chat_simon_t5_2_2:
    if telefono_minuti_blocco("tel_chat_simon_t5_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What am I?»":
            label tel_chat_simon_t5_2_3:
            if telefono_minuti_blocco("tel_chat_simon_t5_2_3", "invia", 1):
                return
            $ msg("sara", "What am I?")
            label tel_chat_simon_t5_2_4:
            if telefono_minuti_blocco("tel_chat_simon_t5_2_4", "ricevi", 1):
                return
            $ msg("simon", "«The Novelist». With a little dumbbell.")
        "«It suits you.»":
            label tel_chat_simon_t5_2_5:
            if telefono_minuti_blocco("tel_chat_simon_t5_2_5", "invia", 1):
                return
            $ msg("sara", "It suits you.")
            $ caldo()
            label tel_chat_simon_t5_2_6:
            if telefono_minuti_blocco("tel_chat_simon_t5_2_6", "ricevi", 1):
                return
            $ msg("simon", "Yeah? I'll have cards printed.")
        "«She's in charge of everything now.»":
            label tel_chat_simon_t5_2_7:
            if telefono_minuti_blocco("tel_chat_simon_t5_2_7", "invia", 1):
                return
            $ msg("sara", "She's in charge of everything now.")
            label tel_chat_simon_t5_2_8:
            if telefono_minuti_blocco("tel_chat_simon_t5_2_8", "ricevi", 1):
                return
            $ msg("simon", "She always was. We just didn't have a group for it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t5_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t5_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_t5_3:
    label tel_chat_simon_t5_3_1:
    if telefono_minuti_blocco("tel_chat_simon_t5_3_1", "ricevi", 1):
        return
    $ msg("simon", "It helps, though. The daft messages. People turn up when someone's waiting.")
    label tel_chat_simon_t5_3_2:
    if telefono_minuti_blocco("tel_chat_simon_t5_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Is that why you let her?»":
            label tel_chat_simon_t5_3_3:
            if telefono_minuti_blocco("tel_chat_simon_t5_3_3", "invia", 1):
                return
            $ msg("sara", "Is that why you let her?")
            label tel_chat_simon_t5_3_4:
            if telefono_minuti_blocco("tel_chat_simon_t5_3_4", "ricevi", 1):
                return
            $ msg("simon", "That, and I'm a bit scared of her.")
        "«Are you waiting for me, then?»":
            label tel_chat_simon_t5_3_5:
            if telefono_minuti_blocco("tel_chat_simon_t5_3_5", "invia", 1):
                return
            $ msg("sara", "Are you waiting for me, then?")
            label tel_chat_simon_t5_3_6:
            if telefono_minuti_blocco("tel_chat_simon_t5_3_6", "ricevi", 1):
                return
            $ msg("simon", "Mondays and Wednesdays. From about ten to. Don't read into it. ...You can read into it a bit.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t5_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_t5_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: complimenti sul corpo

label chat_simon_c1:
    label tel_chat_simon_c1_1:
    if telefono_minuti_blocco("tel_chat_simon_c1_1", "invia", 1):
        return
    $ msg("sara", "Be honest. Can you see a difference?")
    return

label chat_simon_c1_entrata:
    label tel_chat_simon_c1_entrata_1:
    if telefono_minuti_blocco("tel_chat_simon_c1_entrata_1", "ricevi", 1):
        return
    $ msg("simon", "Good session the other day. You're coming on.")
    label tel_chat_simon_c1_entrata_2:
    if telefono_minuti_blocco("tel_chat_simon_c1_entrata_2", "invia", 1):
        return
    $ msg("sara", "Be honest. Can you see a difference?")
    return

label chat_simon_c1_1:
    label tel_chat_simon_c1_1_1:
    if telefono_minuti_blocco("tel_chat_simon_c1_1_1", "ricevi", 1):
        return
    $ msg("simon", "In your lifts? Sure. Every week.")
    label tel_chat_simon_c1_1_2:
    if telefono_minuti_blocco("tel_chat_simon_c1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's not what I asked.»":
            label tel_chat_simon_c1_1_3:
            if telefono_minuti_blocco("tel_chat_simon_c1_1_3", "invia", 1):
                return
            $ msg("sara", "That's not what I asked.")
            $ caldo()
            label tel_chat_simon_c1_1_4:
            if telefono_minuti_blocco("tel_chat_simon_c1_1_4", "ricevi", 1):
                return
            $ msg("simon", "I know. I'm getting there. I'm a slow warm-up.")
        "«In me.»":
            label tel_chat_simon_c1_1_5:
            if telefono_minuti_blocco("tel_chat_simon_c1_1_5", "invia", 1):
                return
            $ msg("sara", "In me.")
            label tel_chat_simon_c1_1_6:
            if telefono_minuti_blocco("tel_chat_simon_c1_1_6", "ricevi", 1):
                return
            $ msg("simon", "Yeah. I can see a difference.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_c1_2:
    label tel_chat_simon_c1_2_1:
    if telefono_minuti_blocco("tel_chat_simon_c1_2_1", "ricevi", 1):
        return
    $ msg("simon", "I've got a rule. I don't comment on how people look. It's a good rule.")
    label tel_chat_simon_c1_2_2:
    if telefono_minuti_blocco("tel_chat_simon_c1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Then don't comment. Just tell me what you noticed.»":
            label tel_chat_simon_c1_2_3:
            if telefono_minuti_blocco("tel_chat_simon_c1_2_3", "invia", 1):
                return
            $ msg("sara", "Then don't comment. Just tell me what you noticed.")
            $ caldo()
            label tel_chat_simon_c1_2_4:
            if telefono_minuti_blocco("tel_chat_simon_c1_2_4", "ricevi", 1):
                return
            $ msg("simon", "You don't cross your arms any more. You walk in like you've paid for the place. I lose count when you do the cables.")
        "«Keep your rule. I like it.»":
            label tel_chat_simon_c1_2_5:
            if telefono_minuti_blocco("tel_chat_simon_c1_2_5", "invia", 1):
                return
            $ msg("sara", "Keep your rule. I like it.")
            label tel_chat_simon_c1_2_6:
            if telefono_minuti_blocco("tel_chat_simon_c1_2_6", "ricevi", 1):
                return
            $ msg("simon", "Thanks. It's costing me a fortune.")
        "«Break it. Once.»":
            label tel_chat_simon_c1_2_7:
            if telefono_minuti_blocco("tel_chat_simon_c1_2_7", "invia", 1):
                return
            $ msg("sara", "Break it. Once.")
            label tel_chat_simon_c1_2_8:
            if telefono_minuti_blocco("tel_chat_simon_c1_2_8", "ricevi", 1):
                return
            $ msg("simon", "You're the only person I've ever had to look away from. There. Broken.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_c1_3:
    label tel_chat_simon_c1_3_1:
    if telefono_minuti_blocco("tel_chat_simon_c1_3_1", "ricevi", 1):
        return
    $ msg("simon", "Too much?")
    label tel_chat_simon_c1_3_2:
    if telefono_minuti_blocco("tel_chat_simon_c1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«No. I've read it three times.»":
            label tel_chat_simon_c1_3_3:
            if telefono_minuti_blocco("tel_chat_simon_c1_3_3", "invia", 1):
                return
            $ msg("sara", "No. I've read it three times.")
            label tel_chat_simon_c1_3_4:
            if telefono_minuti_blocco("tel_chat_simon_c1_3_4", "ricevi", 1):
                return
            $ msg("simon", "I've wanted to delete it three times. So we're even.")
        "«A bit. Let's go back to elbows.»":
            label tel_chat_simon_c1_3_5:
            if telefono_minuti_blocco("tel_chat_simon_c1_3_5", "invia", 1):
                return
            $ msg("sara", "A bit. Let's go back to elbows.")
            $ frena()
            label tel_chat_simon_c1_3_6:
            if telefono_minuti_blocco("tel_chat_simon_c1_3_6", "ricevi", 1):
                return
            $ msg("simon", "Elbows it is. Goodnight, Novelist.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: allenarsi da soli

label chat_simon_c2:
    label tel_chat_simon_c2_1:
    if telefono_minuti_blocco("tel_chat_simon_c2_1", "invia", 1):
        return
    $ msg("sara", "What's the gym like after closing?")
    return

label chat_simon_c2_entrata:
    label tel_chat_simon_c2_entrata_1:
    if telefono_minuti_blocco("tel_chat_simon_c2_entrata_1", "ricevi", 1):
        return
    $ msg("simon", "Locking up. Last one out again.")
    label tel_chat_simon_c2_entrata_2:
    if telefono_minuti_blocco("tel_chat_simon_c2_entrata_2", "invia", 1):
        return
    $ msg("sara", "What's it like after closing?")
    return

label chat_simon_c2_1:
    label tel_chat_simon_c2_1_1:
    if telefono_minuti_blocco("tel_chat_simon_c2_1_1", "ricevi", 1):
        return
    $ msg("simon", "Quiet. You can hear the fridge. I put my own music on.")
    label tel_chat_simon_c2_1_2:
    if telefono_minuti_blocco("tel_chat_simon_c2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What music?»":
            label tel_chat_simon_c2_1_3:
            if telefono_minuti_blocco("tel_chat_simon_c2_1_3", "invia", 1):
                return
            $ msg("sara", "What music?")
            $ caldo()
            label tel_chat_simon_c2_1_4:
            if telefono_minuti_blocco("tel_chat_simon_c2_1_4", "ricevi", 1):
                return
            $ msg("simon", "You'll laugh. Old soul. Slow stuff. Terrible for cardio.")
        "«I'd like that.»":
            label tel_chat_simon_c2_1_5:
            if telefono_minuti_blocco("tel_chat_simon_c2_1_5", "invia", 1):
                return
            $ msg("sara", "I'd like that.")
            label tel_chat_simon_c2_1_6:
            if telefono_minuti_blocco("tel_chat_simon_c2_1_6", "ricevi", 1):
                return
            $ msg("simon", "Yeah. You would. Nobody to say sorry to.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_c2_2:
    label tel_chat_simon_c2_2_1:
    if telefono_minuti_blocco("tel_chat_simon_c2_2_1", "ricevi", 1):
        return
    $ msg("simon", "I've got a key. I could leave the side lights on one night. Just to train.")
    label tel_chat_simon_c2_2_2:
    if telefono_minuti_blocco("tel_chat_simon_c2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Just to train.»":
            label tel_chat_simon_c2_2_3:
            if telefono_minuti_blocco("tel_chat_simon_c2_2_3", "invia", 1):
                return
            $ msg("sara", "Just to train.")
            $ caldo()
            label tel_chat_simon_c2_2_4:
            if telefono_minuti_blocco("tel_chat_simon_c2_2_4", "ricevi", 1):
                return
            $ msg("simon", "I'd bring a clipboard. I'd hold it in front of me the whole time.")
        "«And what would we do?»":
            label tel_chat_simon_c2_2_5:
            if telefono_minuti_blocco("tel_chat_simon_c2_2_5", "invia", 1):
                return
            $ msg("sara", "And what would we do?")
            label tel_chat_simon_c2_2_6:
            if telefono_minuti_blocco("tel_chat_simon_c2_2_6", "ricevi", 1):
                return
            $ msg("simon", "Stretch first. I'm very strict about stretching. It takes as long as it takes.")
        "«I don't think that's a good idea, Simon.»":
            label tel_chat_simon_c2_2_7:
            if telefono_minuti_blocco("tel_chat_simon_c2_2_7", "invia", 1):
                return
            $ msg("sara", "I don't think that's a good idea, Simon.")
            $ frena()
            label tel_chat_simon_c2_2_8:
            if telefono_minuti_blocco("tel_chat_simon_c2_2_8", "ricevi", 1):
                return
            $ msg("simon", "You're right. Forget I said it. See you Monday, lights on.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_c2_3:
    label tel_chat_simon_c2_3_1:
    if telefono_minuti_blocco("tel_chat_simon_c2_3_1", "ricevi", 1):
        return
    $ msg("simon", "I'm not going to push. I spot. That's different.")
    label tel_chat_simon_c2_3_2:
    if telefono_minuti_blocco("tel_chat_simon_c2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What's the difference?»":
            label tel_chat_simon_c2_3_3:
            if telefono_minuti_blocco("tel_chat_simon_c2_3_3", "invia", 1):
                return
            $ msg("sara", "What's the difference?")
            label tel_chat_simon_c2_3_4:
            if telefono_minuti_blocco("tel_chat_simon_c2_3_4", "ricevi", 1):
                return
            $ msg("simon", "You do the lifting. I'm just close enough if you want me.")
        "«I know. That's why I asked.»":
            label tel_chat_simon_c2_3_5:
            if telefono_minuti_blocco("tel_chat_simon_c2_3_5", "invia", 1):
                return
            $ msg("sara", "I know. That's why I asked.")
            label tel_chat_simon_c2_3_6:
            if telefono_minuti_blocco("tel_chat_simon_c2_3_6", "ricevi", 1):
                return
            $ msg("simon", "Then it's whenever you say. I'll be the one pretending to mop.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: fuori dalla palestra

label chat_simon_c3:
    label tel_chat_simon_c3_1:
    if telefono_minuti_blocco("tel_chat_simon_c3_1", "invia", 1):
        return
    $ msg("sara", "I've never seen you in a shirt with buttons.")
    return

label chat_simon_c3_1:
    label tel_chat_simon_c3_1_1:
    if telefono_minuti_blocco("tel_chat_simon_c3_1_1", "ricevi", 1):
        return
    $ msg("simon", "I own two. One's for funerals.")
    label tel_chat_simon_c3_1_2:
    if telefono_minuti_blocco("tel_chat_simon_c3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And the other one?»":
            label tel_chat_simon_c3_1_3:
            if telefono_minuti_blocco("tel_chat_simon_c3_1_3", "invia", 1):
                return
            $ msg("sara", "And the other one?")
            $ caldo()
            label tel_chat_simon_c3_1_4:
            if telefono_minuti_blocco("tel_chat_simon_c3_1_4", "ricevi", 1):
                return
            $ msg("simon", "Never found the occasion. It's blue. I'm told it works.")
        "«I'd pay to see that.»":
            label tel_chat_simon_c3_1_5:
            if telefono_minuti_blocco("tel_chat_simon_c3_1_5", "invia", 1):
                return
            $ msg("sara", "I'd pay to see that.")
            label tel_chat_simon_c3_1_6:
            if telefono_minuti_blocco("tel_chat_simon_c3_1_6", "ricevi", 1):
                return
            $ msg("simon", "Careful. I'm cheap.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_c3_2:
    label tel_chat_simon_c3_2_1:
    if telefono_minuti_blocco("tel_chat_simon_c3_2_1", "ricevi", 1):
        return
    $ msg("simon", "There's a place by the canal. Does one thing. Burgers. You sit on the wall.")
    label tel_chat_simon_c3_2_2:
    if telefono_minuti_blocco("tel_chat_simon_c3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Sounds like cheating, for a trainer.»":
            label tel_chat_simon_c3_2_3:
            if telefono_minuti_blocco("tel_chat_simon_c3_2_3", "invia", 1):
                return
            $ msg("sara", "Sounds like cheating, for a trainer.")
            label tel_chat_simon_c3_2_4:
            if telefono_minuti_blocco("tel_chat_simon_c3_2_4", "ricevi", 1):
                return
            $ msg("simon", "It's on the programme. «Week nine: burger, wall, conversation.»")
        "«And who would I be there with? My trainer?»":
            label tel_chat_simon_c3_2_5:
            if telefono_minuti_blocco("tel_chat_simon_c3_2_5", "invia", 1):
                return
            $ msg("sara", "And who would I be there with? My trainer?")
            $ caldo()
            label tel_chat_simon_c3_2_6:
            if telefono_minuti_blocco("tel_chat_simon_c3_2_6", "ricevi", 1):
                return
            $ msg("simon", "No. He's got Thursdays off.")
        "«I couldn't, Simon.»":
            label tel_chat_simon_c3_2_7:
            if telefono_minuti_blocco("tel_chat_simon_c3_2_7", "invia", 1):
                return
            $ msg("sara", "I couldn't, Simon.")
            $ frena()
            label tel_chat_simon_c3_2_8:
            if telefono_minuti_blocco("tel_chat_simon_c3_2_8", "ricevi", 1):
                return
            $ msg("simon", "I know. I just wanted you to know about the wall.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_c3_3:
    label tel_chat_simon_c3_3_1:
    if telefono_minuti_blocco("tel_chat_simon_c3_3_1", "ricevi", 1):
        return
    $ msg("simon", "I'd walk you home the long way. You'd tell me what the woman does in the room.")
    label tel_chat_simon_c3_3_2:
    if telefono_minuti_blocco("tel_chat_simon_c3_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And you'd listen?»":
            label tel_chat_simon_c3_3_3:
            if telefono_minuti_blocco("tel_chat_simon_c3_3_3", "invia", 1):
                return
            $ msg("sara", "And you'd listen?")
            label tel_chat_simon_c3_3_4:
            if telefono_minuti_blocco("tel_chat_simon_c3_3_4", "ricevi", 1):
                return
            $ msg("simon", "I'm better at it than people think. It's all reps.")
        "«You'd have to keep your hands in your pockets.»":
            label tel_chat_simon_c3_3_5:
            if telefono_minuti_blocco("tel_chat_simon_c3_3_5", "invia", 1):
                return
            $ msg("sara", "You'd have to keep your hands in your pockets.")
            label tel_chat_simon_c3_3_6:
            if telefono_minuti_blocco("tel_chat_simon_c3_3_6", "ricevi", 1):
                return
            $ msg("simon", "I'd sew them shut. For about a street and a half.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c3_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_c3_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: attrazione reciproca

label chat_simon_d1:
    label tel_chat_simon_d1_1:
    if telefono_minuti_blocco("tel_chat_simon_d1_1", "invia", 1):
        return
    $ msg("sara", "I can feel it in muscles I didn't know I had.")
    return

label chat_simon_d1_1:
    label tel_chat_simon_d1_1_1:
    if telefono_minuti_blocco("tel_chat_simon_d1_1_1", "ricevi", 1):
        return
    $ msg("simon", "Ha. That's a trainer's dream, that sentence.")
    label tel_chat_simon_d1_1_2:
    if telefono_minuti_blocco("tel_chat_simon_d1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I wasn't talking about the workout.»":
            label tel_chat_simon_d1_1_3:
            if telefono_minuti_blocco("tel_chat_simon_d1_1_3", "invia", 1):
                return
            $ msg("sara", "I wasn't talking about the workout.")
            $ caldo()
            label tel_chat_simon_d1_1_4:
            if telefono_minuti_blocco("tel_chat_simon_d1_1_4", "ricevi", 1):
                return
            $ msg("simon", "No. Me neither.")
        "«Is it normal to ache like this?»":
            label tel_chat_simon_d1_1_5:
            if telefono_minuti_blocco("tel_chat_simon_d1_1_5", "invia", 1):
                return
            $ msg("sara", "Is it normal to ache like this?")
            label tel_chat_simon_d1_1_6:
            if telefono_minuti_blocco("tel_chat_simon_d1_1_6", "ricevi", 1):
                return
            $ msg("simon", "Delayed onset. It peaks the second night. I'm told it helps to talk.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_d1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_d1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_d1_2:
    label tel_chat_simon_d1_2_1:
    if telefono_minuti_blocco("tel_chat_simon_d1_2_1", "ricevi", 1):
        return
    $ msg("simon", "I'm not good at this in writing. I usually just show people.")
    label tel_chat_simon_d1_2_2:
    if telefono_minuti_blocco("tel_chat_simon_d1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Then tell me how you'd start.»":
            label tel_chat_simon_d1_2_3:
            if telefono_minuti_blocco("tel_chat_simon_d1_2_3", "invia", 1):
                return
            $ msg("sara", "Then tell me how you'd start.")
            $ caldo()
            label tel_chat_simon_d1_2_4:
            if telefono_minuti_blocco("tel_chat_simon_d1_2_4", "ricevi", 1):
                return
            $ msg("simon", "With your shoulders. Both. I'd wait for them to come down.")
        "«Tell me what you thought about on the bus.»":
            label tel_chat_simon_d1_2_5:
            if telefono_minuti_blocco("tel_chat_simon_d1_2_5", "invia", 1):
                return
            $ msg("sara", "Tell me what you thought about on the bus.")
            label tel_chat_simon_d1_2_6:
            if telefono_minuti_blocco("tel_chat_simon_d1_2_6", "ricevi", 1):
                return
            $ msg("simon", "Which bus? There've been a lot of buses.")
        "«Slowly. Half the weight, twice the time.»":
            label tel_chat_simon_d1_2_7:
            if telefono_minuti_blocco("tel_chat_simon_d1_2_7", "invia", 1):
                return
            $ msg("sara", "Slowly. Half the weight, twice the time.")
            label tel_chat_simon_d1_2_8:
            if telefono_minuti_blocco("tel_chat_simon_d1_2_8", "ricevi", 1):
                return
            $ msg("simon", "You remembered that. Okay. Breathe out first. All the way.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_d1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_d1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_d1_3:
    label tel_chat_simon_d1_3_1:
    if telefono_minuti_blocco("tel_chat_simon_d1_3_1", "ricevi", 1):
        return
    $ msg("simon", "Still there?")
    label tel_chat_simon_d1_3_2:
    if telefono_minuti_blocco("tel_chat_simon_d1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Barely.»":
            label tel_chat_simon_d1_3_3:
            if telefono_minuti_blocco("tel_chat_simon_d1_3_3", "invia", 1):
                return
            $ msg("sara", "Barely.")
            label tel_chat_simon_d1_3_4:
            if telefono_minuti_blocco("tel_chat_simon_d1_3_4", "ricevi", 1):
                return
            $ msg("simon", "Good. Don't rush the way back.")
        "«I lost count.»":
            label tel_chat_simon_d1_3_5:
            if telefono_minuti_blocco("tel_chat_simon_d1_3_5", "invia", 1):
                return
            $ msg("sara", "I lost count.")
            label tel_chat_simon_d1_3_6:
            if telefono_minuti_blocco("tel_chat_simon_d1_3_6", "ricevi", 1):
                return
            $ msg("simon", "So did I. Around seven. I always do, with you.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_d1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_d1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: fantasie

label chat_simon_d2:
    label tel_chat_simon_d2_1:
    if telefono_minuti_blocco("tel_chat_simon_d2_1", "invia", 1):
        return
    $ msg("sara", "Tell me one you've never told anyone.")
    return

label chat_simon_d2_1:
    label tel_chat_simon_d2_1_1:
    if telefono_minuti_blocco("tel_chat_simon_d2_1_1", "ricevi", 1):
        return
    $ msg("simon", "You'll think it's tame.")
    label tel_chat_simon_d2_1_2:
    if telefono_minuti_blocco("tel_chat_simon_d2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Try me.»":
            label tel_chat_simon_d2_1_3:
            if telefono_minuti_blocco("tel_chat_simon_d2_1_3", "invia", 1):
                return
            $ msg("sara", "Try me.")
            $ caldo()
            label tel_chat_simon_d2_1_4:
            if telefono_minuti_blocco("tel_chat_simon_d2_1_4", "ricevi", 1):
                return
            $ msg("simon", "After closing. Side lights. You in the mirror and you don't look away from yourself once.")
        "«I like tame.»":
            label tel_chat_simon_d2_1_5:
            if telefono_minuti_blocco("tel_chat_simon_d2_1_5", "invia", 1):
                return
            $ msg("sara", "I like tame.")
            label tel_chat_simon_d2_1_6:
            if telefono_minuti_blocco("tel_chat_simon_d2_1_6", "ricevi", 1):
                return
            $ msg("simon", "Good. It's got a lot of mirror in it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_d2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_d2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_d2_2:
    label tel_chat_simon_d2_2_1:
    if telefono_minuti_blocco("tel_chat_simon_d2_2_1", "ricevi", 1):
        return
    $ msg("simon", "Your go.")
    label tel_chat_simon_d2_2_2:
    if telefono_minuti_blocco("tel_chat_simon_d2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Same room. Somebody might come back for their keys.»":
            label tel_chat_simon_d2_2_3:
            if telefono_minuti_blocco("tel_chat_simon_d2_2_3", "invia", 1):
                return
            $ msg("sara", "Same room. Somebody might come back for their keys.")
            $ caldo()
            label tel_chat_simon_d2_2_4:
            if telefono_minuti_blocco("tel_chat_simon_d2_2_4", "ricevi", 1):
                return
            $ msg("simon", "...Okay. That isn't tame.")
        "«Same room. You never put the clipboard down.»":
            label tel_chat_simon_d2_2_5:
            if telefono_minuti_blocco("tel_chat_simon_d2_2_5", "invia", 1):
                return
            $ msg("sara", "Same room. You never put the clipboard down.")
            label tel_chat_simon_d2_2_6:
            if telefono_minuti_blocco("tel_chat_simon_d2_2_6", "ricevi", 1):
                return
            $ msg("simon", "I'd hold it with my teeth if I had to.")
        "«I'm watching you lift, and I'm allowed to stare.»":
            label tel_chat_simon_d2_2_7:
            if telefono_minuti_blocco("tel_chat_simon_d2_2_7", "invia", 1):
                return
            $ msg("sara", "I'm watching you lift, and I'm allowed to stare.")
            label tel_chat_simon_d2_2_8:
            if telefono_minuti_blocco("tel_chat_simon_d2_2_8", "ricevi", 1):
                return
            $ msg("simon", "You've always been allowed. I'd go for one more rep than I can do.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_d2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_d2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_d2_3:
    label tel_chat_simon_d2_3_1:
    if telefono_minuti_blocco("tel_chat_simon_d2_3_1", "ricevi", 1):
        return
    $ msg("simon", "I'm smiling at a wall. Somebody's just asked me if I'm all right.")
    label tel_chat_simon_d2_3_2:
    if telefono_minuti_blocco("tel_chat_simon_d2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What did you say?»":
            label tel_chat_simon_d2_3_3:
            if telefono_minuti_blocco("tel_chat_simon_d2_3_3", "invia", 1):
                return
            $ msg("sara", "What did you say?")
            label tel_chat_simon_d2_3_4:
            if telefono_minuti_blocco("tel_chat_simon_d2_3_4", "ricevi", 1):
                return
            $ msg("simon", "Delayed onset.")
        "«Put the phone down, then. Come and do it properly.»":
            label tel_chat_simon_d2_3_5:
            if telefono_minuti_blocco("tel_chat_simon_d2_3_5", "invia", 1):
                return
            $ msg("sara", "Put the phone down, then. Come and do it properly.")
            label tel_chat_simon_d2_3_6:
            if telefono_minuti_blocco("tel_chat_simon_d2_3_6", "ricevi", 1):
                return
            $ msg("simon", "Give me twenty minutes. And warm up first. I mean it ;)")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_d2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_d2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return
