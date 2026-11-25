## GENERATO da tools/telefono/componi.py: si modifica tools/telefono/daniel.txt.

init python:
    discorso("daniel_t1", "daniel", CONOSCENTI, argomento="Magnus's card", se="fatto('ep1_d13_biglietto')")
    discorso("daniel_t2", "daniel", CONOSCENTI, argomento="That dinner", se="fatto('ep1_d3_risposta_daniel')")
    discorso("daniel_t3", "daniel", CONOSCENTI, argomento="Keeping it about the novel", se="fatto('ep2_d18_professionale')")
    discorso("daniel_t4", "daniel", CONOSCENTI, argomento="The dance", se="fatto('ep2_d18_ballo')")
    discorso("daniel_t5", "daniel", CONOSCENTI, argomento="What I said for you", se="fatto('ep2_d18_sfotto_josh')")
    discorso("daniel_c1", "daniel", COMPLICI, flirt=True)
    discorso("daniel_c2", "daniel", COMPLICI, flirt=True)
    discorso("daniel_d1", "daniel", INTIMI, flirt=True)
    discorso("daniel_d2", "daniel", INTIMI, flirt=True)


## --- Magnus's card

label chat_daniel_t1:
    label tel_chat_daniel_t1_1:
    if telefono_minuti_blocco("tel_chat_daniel_t1_1", "invia", 1):
        return
    $ msg("sara", "You left me alone with Magnus the other night. On purpose?")
    return

label chat_daniel_t1_entrata:
    label tel_chat_daniel_t1_entrata_1:
    if telefono_minuti_blocco("tel_chat_daniel_t1_entrata_1", "ricevi", 1):
        return
    $ msg("daniel", "Have you forgiven me for leaving you with Magnus?")
    label tel_chat_daniel_t1_entrata_2:
    if telefono_minuti_blocco("tel_chat_daniel_t1_entrata_2", "invia", 1):
        return
    $ msg("sara", "That depends. Was it on purpose?")
    return

label chat_daniel_t1_1:
    label tel_chat_daniel_t1_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_t1_1_1", "ricevi", 2):
        return
    $ msg("daniel", "I don't do anything else.")
    $ msg("daniel", "He doesn't read people I'm standing next to.")
    label tel_chat_daniel_t1_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_t1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«So you were being considerate.»":
            label tel_chat_daniel_t1_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_t1_1_3", "invia", 1):
                return
            $ msg("sara", "So you were being considerate.")
            $ caldo()
            label tel_chat_daniel_t1_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_t1_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Don't spread it about.")
        "«I was terrified.»":
            label tel_chat_daniel_t1_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_t1_1_5", "invia", 1):
                return
            $ msg("sara", "I was terrified.")
            label tel_chat_daniel_t1_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_t1_1_6", "ricevi", 1):
                return
            $ msg("daniel", "It didn't show. That's the same as not being.")
        "«What did you tell him about me?»":
            label tel_chat_daniel_t1_1_7:
            if telefono_minuti_blocco("tel_chat_daniel_t1_1_7", "invia", 1):
                return
            $ msg("sara", "What did you tell him about me?")
            label tel_chat_daniel_t1_1_8:
            if telefono_minuti_blocco("tel_chat_daniel_t1_1_8", "ricevi", 1):
                return
            $ msg("daniel", "That you'd be worth the trouble, and that you'd argue.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_t1_2:
    label tel_chat_daniel_t1_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_t1_2_1", "ricevi", 1):
        return
    $ msg("daniel", "What did he write on the card?")
    label tel_chat_daniel_t1_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_t1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "««Fifty pages. No more, no less.»»":
            label tel_chat_daniel_t1_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_t1_2_3", "invia", 1):
                return
            $ msg("sara", "«Fifty pages. No more, no less.»")
            label tel_chat_daniel_t1_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_t1_2_4", "ricevi", 1):
                return
            $ msg("daniel", "He wrote me «Come when you've something to say.» I was twenty-six. It took me a year.")
        "«That's between him and me.»":
            label tel_chat_daniel_t1_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_t1_2_5", "invia", 1):
                return
            $ msg("sara", "That's between him and me.")
            $ caldo()
            label tel_chat_daniel_t1_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_t1_2_6", "ricevi", 1):
                return
            $ msg("daniel", "Good. Keep him that way. He's no use to people who share him.")
        "«Wouldn't you like to know.»":
            label tel_chat_daniel_t1_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_t1_2_7", "invia", 1):
                return
            $ msg("sara", "Wouldn't you like to know.")
            label tel_chat_daniel_t1_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_t1_2_8", "ricevi", 1):
                return
            $ msg("daniel", "Yes. That's why I asked.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_t1_3:
    label tel_chat_daniel_t1_3_1:
    if telefono_minuti_blocco("tel_chat_daniel_t1_3_1", "ricevi", 1):
        return
    $ msg("daniel", "One piece of advice. Don't thank him.")
    label tel_chat_daniel_t1_3_2:
    if telefono_minuti_blocco("tel_chat_daniel_t1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm not good at that.»":
            label tel_chat_daniel_t1_3_3:
            if telefono_minuti_blocco("tel_chat_daniel_t1_3_3", "invia", 1):
                return
            $ msg("sara", "I'm not good at that.")
            label tel_chat_daniel_t1_3_4:
            if telefono_minuti_blocco("tel_chat_daniel_t1_3_4", "ricevi", 1):
                return
            $ msg("daniel", "You thank doors, Sara. Practise on me.")
        "«Then I won't thank you either.»":
            label tel_chat_daniel_t1_3_5:
            if telefono_minuti_blocco("tel_chat_daniel_t1_3_5", "invia", 1):
                return
            $ msg("sara", "Then I won't thank you either.")
            label tel_chat_daniel_t1_3_6:
            if telefono_minuti_blocco("tel_chat_daniel_t1_3_6", "ricevi", 1):
                return
            $ msg("daniel", "There. You've got it.")
        "«I like thanking people.»":
            label tel_chat_daniel_t1_3_7:
            if telefono_minuti_blocco("tel_chat_daniel_t1_3_7", "invia", 1):
                return
            $ msg("sara", "I like thanking people.")
            label tel_chat_daniel_t1_3_8:
            if telefono_minuti_blocco("tel_chat_daniel_t1_3_8", "ricevi", 1):
                return
            $ msg("daniel", "I know. It's how they know where you keep your purse.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- That dinner

label chat_daniel_t2:
    label tel_chat_daniel_t2_1:
    if telefono_minuti_blocco("tel_chat_daniel_t2_1", "invia", 1):
        return
    $ msg("sara", "I still can't believe I answered you back in front of your whole table.")
    return

label chat_daniel_t2_1:
    label tel_chat_daniel_t2_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_t2_1_1", "ricevi", 2):
        return
    $ msg("daniel", "Respect. «Something they don't teach in every job.»")
    $ msg("daniel", "I've had it quoted at me twice since.")
    label tel_chat_daniel_t2_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_t2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I hope it stung.»":
            label tel_chat_daniel_t2_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_t2_1_3", "invia", 1):
                return
            $ msg("sara", "I hope it stung.")
            $ caldo()
            label tel_chat_daniel_t2_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_t2_1_4", "ricevi", 1):
                return
            $ msg("daniel", "It did. Do it again some time.")
        "«You laughed.»":
            label tel_chat_daniel_t2_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_t2_1_5", "invia", 1):
                return
            $ msg("sara", "You laughed.")
            label tel_chat_daniel_t2_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_t2_1_6", "ricevi", 1):
                return
            $ msg("daniel", "I was delighted. Nobody's thrown anything at me in years.")
        "«You'd deserved it.»":
            label tel_chat_daniel_t2_1_7:
            if telefono_minuti_blocco("tel_chat_daniel_t2_1_7", "invia", 1):
                return
            $ msg("sara", "You'd deserved it.")
            label tel_chat_daniel_t2_1_8:
            if telefono_minuti_blocco("tel_chat_daniel_t2_1_8", "ricevi", 1):
                return
            $ msg("daniel", "Entirely. That isn't why I liked it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_t2_2:
    label tel_chat_daniel_t2_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_t2_2_1", "ricevi", 1):
        return
    $ msg("daniel", "You were defending him. It was rather magnificent.")
    label tel_chat_daniel_t2_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_t2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«He doesn't need defending.»":
            label tel_chat_daniel_t2_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_t2_2_3", "invia", 1):
                return
            $ msg("sara", "He doesn't need defending.")
            label tel_chat_daniel_t2_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_t2_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Everyone at that table thought otherwise. Including him.")
        "«Somebody had to.»":
            label tel_chat_daniel_t2_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_t2_2_5", "invia", 1):
                return
            $ msg("sara", "Somebody had to.")
            $ caldo()
            label tel_chat_daniel_t2_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_t2_2_6", "ricevi", 1):
                return
            $ msg("daniel", "Yes. I wondered how long he'd wait. He was still waiting when I left.")
            sp "I was waiting too. With my fork in my hand."
        "«I'd do it again.»":
            label tel_chat_daniel_t2_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_t2_2_7", "invia", 1):
                return
            $ msg("sara", "I'd do it again.")
            $ frena()
            label tel_chat_daniel_t2_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_t2_2_8", "ricevi", 1):
                return
            $ msg("daniel", "I know. Goodnight, Sara.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_t2_3:
    label tel_chat_daniel_t2_3_1:
    if telefono_minuti_blocco("tel_chat_daniel_t2_3_1", "ricevi", 1):
        return
    $ msg("daniel", "Tell me one thing. Were you angry with me, or with him?")
    label tel_chat_daniel_t2_3_2:
    if telefono_minuti_blocco("tel_chat_daniel_t2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«With you.»":
            label tel_chat_daniel_t2_3_3:
            if telefono_minuti_blocco("tel_chat_daniel_t2_3_3", "invia", 1):
                return
            $ msg("sara", "With you.")
            label tel_chat_daniel_t2_3_4:
            if telefono_minuti_blocco("tel_chat_daniel_t2_3_4", "ricevi", 1):
                return
            $ msg("daniel", "Mostly, I think.")
        "«Both.»":
            label tel_chat_daniel_t2_3_5:
            if telefono_minuti_blocco("tel_chat_daniel_t2_3_5", "invia", 1):
                return
            $ msg("sara", "Both.")
            label tel_chat_daniel_t2_3_6:
            if telefono_minuti_blocco("tel_chat_daniel_t2_3_6", "ricevi", 1):
                return
            $ msg("daniel", "That's the honest answer. Nobody ever gives me that one before coffee.")
        "«That's a horrible question.»":
            label tel_chat_daniel_t2_3_7:
            if telefono_minuti_blocco("tel_chat_daniel_t2_3_7", "invia", 1):
                return
            $ msg("sara", "That's a horrible question.")
            label tel_chat_daniel_t2_3_8:
            if telefono_minuti_blocco("tel_chat_daniel_t2_3_8", "ricevi", 1):
                return
            $ msg("daniel", "They're the only ones worth the stamp.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Keeping it about the novel

label chat_daniel_t3:
    label tel_chat_daniel_t3_1:
    if telefono_minuti_blocco("tel_chat_daniel_t3_1", "invia", 1):
        return
    $ msg("sara", "Thank you for lunch. It was nice to talk about the book.")
    return

label chat_daniel_t3_entrata:
    label tel_chat_daniel_t3_entrata_1:
    if telefono_minuti_blocco("tel_chat_daniel_t3_entrata_1", "ricevi", 1):
        return
    $ msg("daniel", "The fish sends its regards.")
    label tel_chat_daniel_t3_entrata_2:
    if telefono_minuti_blocco("tel_chat_daniel_t3_entrata_2", "invia", 1):
        return
    $ msg("sara", "Thank it from me. It was nice to talk about the book.")
    return

label chat_daniel_t3_1:
    label tel_chat_daniel_t3_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_t3_1_1", "ricevi", 1):
        return
    $ msg("daniel", "You thanked me again.")
    label tel_chat_daniel_t3_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_t3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm thanking the fish.»":
            label tel_chat_daniel_t3_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_t3_1_3", "invia", 1):
                return
            $ msg("sara", "I'm thanking the fish.")
            label tel_chat_daniel_t3_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_t3_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Then I'll pass it on.")
        "«You behaved very well.»":
            label tel_chat_daniel_t3_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_t3_1_5", "invia", 1):
                return
            $ msg("sara", "You behaved very well.")
            $ caldo()
            label tel_chat_daniel_t3_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_t3_1_6", "ricevi", 1):
                return
            $ msg("daniel", "I did, didn't I? It was exhausting.")
        "«Force of habit.»":
            label tel_chat_daniel_t3_1_7:
            if telefono_minuti_blocco("tel_chat_daniel_t3_1_7", "invia", 1):
                return
            $ msg("sara", "Force of habit.")
            label tel_chat_daniel_t3_1_8:
            if telefono_minuti_blocco("tel_chat_daniel_t3_1_8", "ricevi", 1):
                return
            $ msg("daniel", "We'll find you a better one.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_t3_2:
    label tel_chat_daniel_t3_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_t3_2_1", "ricevi", 2):
        return
    $ msg("daniel", "You talk faster when it's the book. You use your hands.")
    $ msg("daniel", "I kept moving your glass. You didn't notice.")
    label tel_chat_daniel_t3_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_t3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I noticed.»":
            label tel_chat_daniel_t3_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_t3_2_3", "invia", 1):
                return
            $ msg("sara", "I noticed.")
            $ caldo()
            label tel_chat_daniel_t3_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_t3_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Ah.")
        "«I get carried away.»":
            label tel_chat_daniel_t3_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_t3_2_5", "invia", 1):
                return
            $ msg("sara", "I get carried away.")
            label tel_chat_daniel_t3_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_t3_2_6", "ricevi", 1):
                return
            $ msg("daniel", "Nobody's ever been carried anywhere by staying put.")
        "«I nearly knocked it over, didn't I?»":
            label tel_chat_daniel_t3_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_t3_2_7", "invia", 1):
                return
            $ msg("sara", "I nearly knocked it over, didn't I?")
            label tel_chat_daniel_t3_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_t3_2_8", "ricevi", 1):
                return
            $ msg("daniel", "Three times. I was enjoying the suspense.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_t3_3:
    label tel_chat_daniel_t3_3_1:
    if telefono_minuti_blocco("tel_chat_daniel_t3_3_1", "ricevi", 1):
        return
    $ msg("daniel", "You set the rules at that table. I kept to them.")
    label tel_chat_daniel_t3_3_2:
    if telefono_minuti_blocco("tel_chat_daniel_t3_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'd like it to stay that way.»":
            label tel_chat_daniel_t3_3_3:
            if telefono_minuti_blocco("tel_chat_daniel_t3_3_3", "invia", 1):
                return
            $ msg("sara", "I'd like it to stay that way.")
            label tel_chat_daniel_t3_3_4:
            if telefono_minuti_blocco("tel_chat_daniel_t3_3_4", "ricevi", 1):
                return
            $ msg("daniel", "Then it will. You can have that for as long as you want it.")
        "«For now.»":
            label tel_chat_daniel_t3_3_5:
            if telefono_minuti_blocco("tel_chat_daniel_t3_3_5", "invia", 1):
                return
            $ msg("sara", "For now.")
            label tel_chat_daniel_t3_3_6:
            if telefono_minuti_blocco("tel_chat_daniel_t3_3_6", "ricevi", 1):
                return
            $ msg("daniel", "Two very small words. I'll have them framed.")
        "«I'm not sure you did keep to them.»":
            label tel_chat_daniel_t3_3_7:
            if telefono_minuti_blocco("tel_chat_daniel_t3_3_7", "invia", 1):
                return
            $ msg("sara", "I'm not sure you did keep to them.")
            label tel_chat_daniel_t3_3_8:
            if telefono_minuti_blocco("tel_chat_daniel_t3_3_8", "ricevi", 1):
                return
            $ msg("daniel", "I kept my hands to them. The rest of me I can't answer for.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t3_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t3_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The dance

label chat_daniel_t4:
    label tel_chat_daniel_t4_1:
    if telefono_minuti_blocco("tel_chat_daniel_t4_1", "invia", 1):
        return
    $ msg("sara", "You stopped before the song did.")
    return

label chat_daniel_t4_entrata:
    label tel_chat_daniel_t4_entrata_1:
    if telefono_minuti_blocco("tel_chat_daniel_t4_entrata_1", "ricevi", 1):
        return
    $ msg("daniel", "I've had a tune in my head all evening.")
    label tel_chat_daniel_t4_entrata_2:
    if telefono_minuti_blocco("tel_chat_daniel_t4_entrata_2", "invia", 1):
        return
    $ msg("sara", "You stopped before it did.")
    return

label chat_daniel_t4_1:
    label tel_chat_daniel_t4_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_t4_1_1", "ricevi", 1):
        return
    $ msg("daniel", "You noticed.")
    label tel_chat_daniel_t4_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_t4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Anyone would have.»":
            label tel_chat_daniel_t4_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_t4_1_3", "invia", 1):
                return
            $ msg("sara", "Anyone would have.")
            $ caldo()
            label tel_chat_daniel_t4_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_t4_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Anyone would have been relieved. You looked robbed.")
        "«I was going to stop anyway.»":
            label tel_chat_daniel_t4_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_t4_1_5", "invia", 1):
                return
            $ msg("sara", "I was going to stop anyway.")
            label tel_chat_daniel_t4_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_t4_1_6", "ricevi", 1):
                return
            $ msg("daniel", "Of course. You were building up to it.")
        "«Was it on purpose?»":
            label tel_chat_daniel_t4_1_7:
            if telefono_minuti_blocco("tel_chat_daniel_t4_1_7", "invia", 1):
                return
            $ msg("sara", "Was it on purpose?")
            label tel_chat_daniel_t4_1_8:
            if telefono_minuti_blocco("tel_chat_daniel_t4_1_8", "ricevi", 1):
                return
            $ msg("daniel", "Sara. Everything.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_t4_2:
    label tel_chat_daniel_t4_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_t4_2_1", "ricevi", 1):
        return
    $ msg("daniel", "What were you looking at, all that time? You were facing the window.")
    label tel_chat_daniel_t4_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_t4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«The fig tree.»":
            label tel_chat_daniel_t4_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_t4_2_3", "invia", 1):
                return
            $ msg("sara", "The fig tree.")
            label tel_chat_daniel_t4_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_t4_2_4", "ricevi", 1):
                return
            $ msg("daniel", "And what did it tell you?")
        "«You. In the glass.»":
            label tel_chat_daniel_t4_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_t4_2_5", "invia", 1):
                return
            $ msg("sara", "You. In the glass.")
            $ caldo()
            label tel_chat_daniel_t4_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_t4_2_6", "ricevi", 1):
                return
            $ msg("daniel", "I know. I was looking back.")
            sp "I saw him looking back."
        "«Nothing. My eyes were shut.»":
            label tel_chat_daniel_t4_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_t4_2_7", "invia", 1):
                return
            $ msg("sara", "Nothing. My eyes were shut.")
            label tel_chat_daniel_t4_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_t4_2_8", "ricevi", 1):
                return
            $ msg("daniel", "Not for the last verse.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_t4_3:
    label tel_chat_daniel_t4_3_1:
    if telefono_minuti_blocco("tel_chat_daniel_t4_3_1", "ricevi", 1):
        return
    $ msg("daniel", "I haven't played it since. It's got you in it now.")
    label tel_chat_daniel_t4_3_2:
    if telefono_minuti_blocco("tel_chat_daniel_t4_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You say that to everyone.»":
            label tel_chat_daniel_t4_3_3:
            if telefono_minuti_blocco("tel_chat_daniel_t4_3_3", "invia", 1):
                return
            $ msg("sara", "You say that to everyone.")
            label tel_chat_daniel_t4_3_4:
            if telefono_minuti_blocco("tel_chat_daniel_t4_3_4", "ricevi", 1):
                return
            $ msg("daniel", "I say a good many things to everyone. Not that.")
        "«What happens in the last minute? Of the song?»":
            label tel_chat_daniel_t4_3_5:
            if telefono_minuti_blocco("tel_chat_daniel_t4_3_5", "invia", 1):
                return
            $ msg("sara", "What happens in the last minute? Of the song?")
            label tel_chat_daniel_t4_3_6:
            if telefono_minuti_blocco("tel_chat_daniel_t4_3_6", "ricevi", 1):
                return
            $ msg("daniel", "You'll have to come back for it.")
        "«We shouldn't do that again, Daniel.»":
            label tel_chat_daniel_t4_3_7:
            if telefono_minuti_blocco("tel_chat_daniel_t4_3_7", "invia", 1):
                return
            $ msg("sara", "We shouldn't do that again, Daniel.")
            $ frena()
            label tel_chat_daniel_t4_3_8:
            if telefono_minuti_blocco("tel_chat_daniel_t4_3_8", "ricevi", 1):
                return
            $ msg("daniel", "«Shouldn't.» I heard you. Goodnight.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t4_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t4_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- What I said for you

label chat_daniel_t5:
    label tel_chat_daniel_t5_1:
    if telefono_minuti_blocco("tel_chat_daniel_t5_1", "invia", 1):
        return
    $ msg("sara", "I'm not proud of what I said about [nome_compagno]. At lunch.")
    return

label chat_daniel_t5_entrata:
    label tel_chat_daniel_t5_entrata_1:
    if telefono_minuti_blocco("tel_chat_daniel_t5_entrata_1", "ricevi", 1):
        return
    $ msg("daniel", "I keep hearing your voice. One line of it.")
    label tel_chat_daniel_t5_entrata_2:
    if telefono_minuti_blocco("tel_chat_daniel_t5_entrata_2", "invia", 1):
        return
    $ msg("sara", "I'm not proud of that line.")
    return

label chat_daniel_t5_1:
    label tel_chat_daniel_t5_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_t5_1_1", "ricevi", 1):
        return
    $ msg("daniel", "No? You were smiling when you said it.")
    label tel_chat_daniel_t5_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_t5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's what I'm not proud of.»":
            label tel_chat_daniel_t5_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_t5_1_3", "invia", 1):
                return
            $ msg("sara", "That's what I'm not proud of.")
            label tel_chat_daniel_t5_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_t5_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Then we agree on the facts.")
        "«You made me say it twice.»":
            label tel_chat_daniel_t5_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_t5_1_5", "invia", 1):
                return
            $ msg("sara", "You made me say it twice.")
            $ caldo()
            label tel_chat_daniel_t5_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_t5_1_6", "ricevi", 1):
                return
            $ msg("daniel", "I asked you twice. You're the one with the voice.")
        "«It was cruel.»":
            label tel_chat_daniel_t5_1_7:
            if telefono_minuti_blocco("tel_chat_daniel_t5_1_7", "invia", 1):
                return
            $ msg("sara", "It was cruel.")
            label tel_chat_daniel_t5_1_8:
            if telefono_minuti_blocco("tel_chat_daniel_t5_1_8", "ricevi", 1):
                return
            $ msg("daniel", "It was accurate. Cruel would have been saying it to him.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_t5_2:
    label tel_chat_daniel_t5_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_t5_2_1", "ricevi", 1):
        return
    $ msg("daniel", "Shall I tell you what I heard? Not the joke. Under it.")
    label tel_chat_daniel_t5_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_t5_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Go on.»":
            label tel_chat_daniel_t5_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_t5_2_3", "invia", 1):
                return
            $ msg("sara", "Go on.")
            label tel_chat_daniel_t5_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_t5_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Somebody who's been carrying a tray for years and has just been told she can put it down.")
        "«No. I don't want it explained.»":
            label tel_chat_daniel_t5_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_t5_2_5", "invia", 1):
                return
            $ msg("sara", "No. I don't want it explained.")
            $ frena()
            label tel_chat_daniel_t5_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_t5_2_6", "ricevi", 1):
                return
            $ msg("daniel", "Wise. It never sounds as good the second time.")
        "«I heard it too.»":
            label tel_chat_daniel_t5_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_t5_2_7", "invia", 1):
                return
            $ msg("sara", "I heard it too.")
            $ caldo()
            label tel_chat_daniel_t5_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_t5_2_8", "ricevi", 1):
                return
            $ msg("daniel", "Yes. It's a nice sound, isn't it? Glass.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t5_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t5_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_t5_3:
    label tel_chat_daniel_t5_3_1:
    if telefono_minuti_blocco("tel_chat_daniel_t5_3_1", "ricevi", 1):
        return
    $ msg("daniel", "You needn't do it again. I only wanted to know that you could.")
    label tel_chat_daniel_t5_3_2:
    if telefono_minuti_blocco("tel_chat_daniel_t5_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And now you know.»":
            label tel_chat_daniel_t5_3_3:
            if telefono_minuti_blocco("tel_chat_daniel_t5_3_3", "invia", 1):
                return
            $ msg("sara", "And now you know.")
            label tel_chat_daniel_t5_3_4:
            if telefono_minuti_blocco("tel_chat_daniel_t5_3_4", "ricevi", 1):
                return
            $ msg("daniel", "Now we both do. That's rather the point.")
        "«He's a good man, Daniel.»":
            label tel_chat_daniel_t5_3_5:
            if telefono_minuti_blocco("tel_chat_daniel_t5_3_5", "invia", 1):
                return
            $ msg("sara", "He's a good man, Daniel.")
            label tel_chat_daniel_t5_3_6:
            if telefono_minuti_blocco("tel_chat_daniel_t5_3_6", "ricevi", 1):
                return
            $ msg("daniel", "The best. I'd trust him with anything. I frequently do.")
            sp "He didn't even have to finish the sentence."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t5_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_t5_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: il piacere delle sfide

label chat_daniel_c1:
    label tel_chat_daniel_c1_1:
    if telefono_minuti_blocco("tel_chat_daniel_c1_1", "invia", 1):
        return
    $ msg("sara", "What do you do when somebody doesn't do what you want?")
    return

label chat_daniel_c1_entrata:
    label tel_chat_daniel_c1_entrata_1:
    if telefono_minuti_blocco("tel_chat_daniel_c1_entrata_1", "ricevi", 1):
        return
    $ msg("daniel", "You've been ignoring me beautifully.")
    label tel_chat_daniel_c1_entrata_2:
    if telefono_minuti_blocco("tel_chat_daniel_c1_entrata_2", "invia", 1):
        return
    $ msg("sara", "What do you do when somebody doesn't do what you want?")
    return

label chat_daniel_c1_1:
    label tel_chat_daniel_c1_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_c1_1_1", "ricevi", 1):
        return
    $ msg("daniel", "It's so rare. I generally send flowers.")
    label tel_chat_daniel_c1_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_c1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And if she sends them back?»":
            label tel_chat_daniel_c1_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_c1_1_3", "invia", 1):
                return
            $ msg("sara", "And if she sends them back?")
            $ caldo()
            label tel_chat_daniel_c1_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_c1_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Then I keep the vase.")
        "«Does anyone?»":
            label tel_chat_daniel_c1_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_c1_1_5", "invia", 1):
                return
            $ msg("sara", "Does anyone?")
            label tel_chat_daniel_c1_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_c1_1_6", "ricevi", 1):
                return
            $ msg("daniel", "You. Twice a week, on average. It's done wonders for me.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_c1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_c1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_c1_2:
    label tel_chat_daniel_c1_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_c1_2_1", "ricevi", 1):
        return
    $ msg("daniel", "Let's play something. I say a thing you won't dare do tomorrow. You tell me why.")
    label tel_chat_daniel_c1_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_c1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Go on. I'm not scared of you.»":
            label tel_chat_daniel_c1_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_c1_2_3", "invia", 1):
                return
            $ msg("sara", "Go on. I'm not scared of you.")
            $ caldo()
            label tel_chat_daniel_c1_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_c1_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Wear something under your office clothes that nobody will ever know about but the two of us.")
            sp "Nobody would know. He'd know."
        "«And if I do dare?»":
            label tel_chat_daniel_c1_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_c1_2_5", "invia", 1):
                return
            $ msg("sara", "And if I do dare?")
            label tel_chat_daniel_c1_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_c1_2_6", "ricevi", 1):
                return
            $ msg("daniel", "Then I'll have lost. I'm told it's good for the character.")
        "«I don't play games with you.»":
            label tel_chat_daniel_c1_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_c1_2_7", "invia", 1):
                return
            $ msg("sara", "I don't play games with you.")
            $ frena()
            label tel_chat_daniel_c1_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_c1_2_8", "ricevi", 1):
                return
            $ msg("daniel", "You've been playing for weeks. You're ahead. Goodnight.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_c1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_c1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_c1_3:
    label tel_chat_daniel_c1_3_1:
    if telefono_minuti_blocco("tel_chat_daniel_c1_3_1", "ricevi", 1):
        return
    $ msg("daniel", "You've gone quiet. I'll take that as thinking.")
    label tel_chat_daniel_c1_3_2:
    if telefono_minuti_blocco("tel_chat_daniel_c1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I was choosing a colour.»":
            label tel_chat_daniel_c1_3_3:
            if telefono_minuti_blocco("tel_chat_daniel_c1_3_3", "invia", 1):
                return
            $ msg("sara", "I was choosing a colour.")
            label tel_chat_daniel_c1_3_4:
            if telefono_minuti_blocco("tel_chat_daniel_c1_3_4", "ricevi", 1):
                return
            $ msg("daniel", "Don't tell me. I'd rather guess, across a room, and be right.")
        "«You won't win, you know.»":
            label tel_chat_daniel_c1_3_5:
            if telefono_minuti_blocco("tel_chat_daniel_c1_3_5", "invia", 1):
                return
            $ msg("sara", "You won't win, you know.")
            label tel_chat_daniel_c1_3_6:
            if telefono_minuti_blocco("tel_chat_daniel_c1_3_6", "ricevi", 1):
                return
            $ msg("daniel", "I never mind how it ends. I like watching you decide.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_c1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_c1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: un invito riservato

label chat_daniel_c2:
    label tel_chat_daniel_c2_1:
    if telefono_minuti_blocco("tel_chat_daniel_c2_1", "invia", 1):
        return
    $ msg("sara", "You said there was a place you'd never taken anyone.")
    return

label chat_daniel_c2_entrata:
    label tel_chat_daniel_c2_entrata_1:
    if telefono_minuti_blocco("tel_chat_daniel_c2_entrata_1", "ricevi", 1):
        return
    $ msg("daniel", "I've been thinking of going away for a day or two.")
    label tel_chat_daniel_c2_entrata_2:
    if telefono_minuti_blocco("tel_chat_daniel_c2_entrata_2", "invia", 1):
        return
    $ msg("sara", "To the place you've never taken anyone?")
    return

label chat_daniel_c2_1:
    label tel_chat_daniel_c2_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_c2_1_1", "ricevi", 1):
        return
    $ msg("daniel", "There's a house on the coast. No signal. Very bad paintings.")
    label tel_chat_daniel_c2_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_c2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Why no one?»":
            label tel_chat_daniel_c2_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_c2_1_3", "invia", 1):
                return
            $ msg("sara", "Why no one?")
            $ caldo()
            label tel_chat_daniel_c2_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_c2_1_4", "ricevi", 1):
                return
            $ msg("daniel", "People talk. The sea doesn't need the help.")
        "«I don't believe you.»":
            label tel_chat_daniel_c2_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_c2_1_5", "invia", 1):
                return
            $ msg("sara", "I don't believe you.")
            label tel_chat_daniel_c2_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_c2_1_6", "ricevi", 1):
                return
            $ msg("daniel", "Good. I'd be disappointed if you did.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_c2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_c2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_c2_2:
    label tel_chat_daniel_c2_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_c2_2_1", "ricevi", 1):
        return
    $ msg("daniel", "I'm not inviting you. I'm describing it.")
    label tel_chat_daniel_c2_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_c2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Describe the bedroom, then.»":
            label tel_chat_daniel_c2_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_c2_2_3", "invia", 1):
                return
            $ msg("sara", "Describe the bedroom, then.")
            $ caldo()
            label tel_chat_daniel_c2_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_c2_2_4", "ricevi", 1):
                return
            $ msg("daniel", "White. One window. The light gets in before anyone's decent.")
        "«Describe the kitchen.»":
            label tel_chat_daniel_c2_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_c2_2_5", "invia", 1):
                return
            $ msg("sara", "Describe the kitchen.")
            label tel_chat_daniel_c2_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_c2_2_6", "ricevi", 1):
                return
            $ msg("daniel", "You'd sit on the table. I'd cook. You'd pretend to help.")
        "«You're inviting me.»":
            label tel_chat_daniel_c2_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_c2_2_7", "invia", 1):
                return
            $ msg("sara", "You're inviting me.")
            label tel_chat_daniel_c2_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_c2_2_8", "ricevi", 1):
                return
            $ msg("daniel", "I'm describing it very slowly.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_c2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_c2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_c2_3:
    label tel_chat_daniel_c2_3_1:
    if telefono_minuti_blocco("tel_chat_daniel_c2_3_1", "ricevi", 1):
        return
    $ msg("daniel", "What would you tell him?")
    label tel_chat_daniel_c2_3_2:
    if telefono_minuti_blocco("tel_chat_daniel_c2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm not going, so I don't need to tell him anything.»":
            label tel_chat_daniel_c2_3_3:
            if telefono_minuti_blocco("tel_chat_daniel_c2_3_3", "invia", 1):
                return
            $ msg("sara", "I'm not going, so I don't need to tell him anything.")
            label tel_chat_daniel_c2_3_4:
            if telefono_minuti_blocco("tel_chat_daniel_c2_3_4", "ricevi", 1):
                return
            $ msg("daniel", "Then it costs nothing to think about it. Think about it.")
        "«That I was writing.»":
            label tel_chat_daniel_c2_3_5:
            if telefono_minuti_blocco("tel_chat_daniel_c2_3_5", "invia", 1):
                return
            $ msg("sara", "That I was writing.")
            label tel_chat_daniel_c2_3_6:
            if telefono_minuti_blocco("tel_chat_daniel_c2_3_6", "ricevi", 1):
                return
            $ msg("daniel", "You would be. Afterwards. I'd find you a desk.")
        "«Stop there, Daniel.»":
            label tel_chat_daniel_c2_3_7:
            if telefono_minuti_blocco("tel_chat_daniel_c2_3_7", "invia", 1):
                return
            $ msg("sara", "Stop there, Daniel.")
            $ frena()
            label tel_chat_daniel_c2_3_8:
            if telefono_minuti_blocco("tel_chat_daniel_c2_3_8", "ricevi", 1):
                return
            $ msg("daniel", "I've stopped. The house isn't going anywhere.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_c2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_c2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: confessare l'attrazione

label chat_daniel_d1:
    label tel_chat_daniel_d1_1:
    if telefono_minuti_blocco("tel_chat_daniel_d1_1", "invia", 1):
        return
    $ msg("sara", "I can't concentrate on anything.")
    return

label chat_daniel_d1_1:
    label tel_chat_daniel_d1_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_d1_1_1", "ricevi", 1):
        return
    $ msg("daniel", "I know. I've read the same contract four times.")
    label tel_chat_daniel_d1_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_d1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You?»":
            label tel_chat_daniel_d1_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_d1_1_3", "invia", 1):
                return
            $ msg("sara", "You?")
            $ caldo()
            label tel_chat_daniel_d1_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_d1_1_4", "ricevi", 1):
                return
            $ msg("daniel", "I signed it in the end. I may have sold something.")
        "«Good. I'd hate it to be only me.»":
            label tel_chat_daniel_d1_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_d1_1_5", "invia", 1):
                return
            $ msg("sara", "Good. I'd hate it to be only me.")
            label tel_chat_daniel_d1_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_d1_1_6", "ricevi", 1):
                return
            $ msg("daniel", "It isn't. Don't tell the office.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_d1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_d1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_d1_2:
    label tel_chat_daniel_d1_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_d1_2_1", "ricevi", 1):
        return
    $ msg("daniel", "Where are you?")
    label tel_chat_daniel_d1_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_d1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«In bed. He's working late. You should know.»":
            label tel_chat_daniel_d1_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_d1_2_3", "invia", 1):
                return
            $ msg("sara", "In bed. He's working late. You should know.")
            $ caldo()
            label tel_chat_daniel_d1_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_d1_2_4", "ricevi", 1):
                return
            $ msg("daniel", "I do. I gave him the file.")
            sp "He gave him the file."
        "«At my desk. With the door shut.»":
            label tel_chat_daniel_d1_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_d1_2_5", "invia", 1):
                return
            $ msg("sara", "At my desk. With the door shut.")
            label tel_chat_daniel_d1_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_d1_2_6", "ricevi", 1):
                return
            $ msg("daniel", "Lock it.")
        "«Somewhere I can't talk.»":
            label tel_chat_daniel_d1_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_d1_2_7", "invia", 1):
                return
            $ msg("sara", "Somewhere I can't talk.")
            label tel_chat_daniel_d1_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_d1_2_8", "ricevi", 1):
                return
            $ msg("daniel", "Then don't. Read. Put your free hand where I'd put mine.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_d1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_d1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_d1_3:
    label tel_chat_daniel_d1_3_1:
    if telefono_minuti_blocco("tel_chat_daniel_d1_3_1", "ricevi", 1):
        return
    $ msg("daniel", "Don't say sorry. Whatever you were about to type.")
    label tel_chat_daniel_d1_3_2:
    if telefono_minuti_blocco("tel_chat_daniel_d1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I wasn't going to.»":
            label tel_chat_daniel_d1_3_3:
            if telefono_minuti_blocco("tel_chat_daniel_d1_3_3", "invia", 1):
                return
            $ msg("sara", "I wasn't going to.")
            label tel_chat_daniel_d1_3_4:
            if telefono_minuti_blocco("tel_chat_daniel_d1_3_4", "ricevi", 1):
                return
            $ msg("daniel", "No. I believe you weren't. I've waited a long time for that.")
        "«Say something nice.»":
            label tel_chat_daniel_d1_3_5:
            if telefono_minuti_blocco("tel_chat_daniel_d1_3_5", "invia", 1):
                return
            $ msg("sara", "Say something nice.")
            label tel_chat_daniel_d1_3_6:
            if telefono_minuti_blocco("tel_chat_daniel_d1_3_6", "ricevi", 2):
                return
            $ msg("daniel", "You've stopped asking permission. There isn't anything nicer.")
            $ msg("daniel", "Goodnight, Sara.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_d1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_d1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: i limiti di una relazione segreta

label chat_daniel_d2:
    label tel_chat_daniel_d2_1:
    if telefono_minuti_blocco("tel_chat_daniel_d2_1", "invia", 1):
        return
    $ msg("sara", "What are the rules?")
    return

label chat_daniel_d2_1:
    label tel_chat_daniel_d2_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_d2_1_1", "ricevi", 1):
        return
    $ msg("daniel", "There's one. You can stop it with a word, any time, and I'll open the door for you.")
    label tel_chat_daniel_d2_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_d2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And yours?»":
            label tel_chat_daniel_d2_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_d2_1_3", "invia", 1):
                return
            $ msg("sara", "And yours?")
            $ caldo()
            label tel_chat_daniel_d2_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_d2_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Mine are for me. You needn't keep them.")
        "«What's the word?»":
            label tel_chat_daniel_d2_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_d2_1_5", "invia", 1):
                return
            $ msg("sara", "What's the word?")
            label tel_chat_daniel_d2_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_d2_1_6", "ricevi", 1):
                return
            $ msg("daniel", "«Enough.» It's a good word. I've hardly ever heard you use it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_d2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_d2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_d2_2:
    label tel_chat_daniel_d2_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_d2_2_1", "ricevi", 1):
        return
    $ msg("daniel", "Now you. What won't you do?")
    label tel_chat_daniel_d2_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_d2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Lie to his face.»":
            label tel_chat_daniel_d2_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_d2_2_3", "invia", 1):
                return
            $ msg("sara", "Lie to his face.")
            label tel_chat_daniel_d2_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_d2_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Then we'll never make you. There are plenty of rooms he isn't in.")
        "«I don't know yet. Ask me one thing at a time.»":
            label tel_chat_daniel_d2_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_d2_2_5", "invia", 1):
                return
            $ msg("sara", "I don't know yet. Ask me one thing at a time.")
            $ caldo()
            label tel_chat_daniel_d2_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_d2_2_6", "ricevi", 1):
                return
            $ msg("daniel", "One thing, then. Tomorrow. In the lift. You don't touch me and I don't touch you, and we see who looks away.")
        "«Less than I thought.»":
            label tel_chat_daniel_d2_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_d2_2_7", "invia", 1):
                return
            $ msg("sara", "Less than I thought.")
            label tel_chat_daniel_d2_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_d2_2_8", "ricevi", 1):
                return
            $ msg("daniel", "That's the most dangerous thing you've ever written to me. I've read it twice.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_d2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_d2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_d2_3:
    label tel_chat_daniel_d2_3_1:
    if telefono_minuti_blocco("tel_chat_daniel_d2_3_1", "ricevi", 1):
        return
    $ msg("daniel", "Are you smiling?")
    label tel_chat_daniel_d2_3_2:
    if telefono_minuti_blocco("tel_chat_daniel_d2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Yes.»":
            label tel_chat_daniel_d2_3_3:
            if telefono_minuti_blocco("tel_chat_daniel_d2_3_3", "invia", 1):
                return
            $ msg("sara", "Yes.")
            label tel_chat_daniel_d2_3_4:
            if telefono_minuti_blocco("tel_chat_daniel_d2_3_4", "ricevi", 1):
                return
            $ msg("daniel", "So am I. I'm in a meeting. They think I like the figures.")
        "«Come and see.»":
            label tel_chat_daniel_d2_3_5:
            if telefono_minuti_blocco("tel_chat_daniel_d2_3_5", "invia", 1):
                return
            $ msg("sara", "Come and see.")
            label tel_chat_daniel_d2_3_6:
            if telefono_minuti_blocco("tel_chat_daniel_d2_3_6", "ricevi", 1):
                return
            $ msg("daniel", "Friday. Bring nothing you'd mind losing.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_d2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_d2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return
