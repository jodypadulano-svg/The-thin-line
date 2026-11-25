## GENERATO da tools/telefono/componi.py: si modifica tools/telefono/amica.txt.

init python:
    discorso("amica_t1", "amica", CONOSCENTI, argomento="Lunch with Daniel", se="giorno < 18 and fatto('ep1_d13_pranzo_forse')")
    discorso("amica_t2", "amica", CONOSCENTI, argomento="My first piece", se="fatto('ep1_d12_prima_joanie')")
    discorso("amica_t3", "amica", CONOSCENTI, argomento="What I told you in the kitchen", se="fatto('ep2_d16_confida_joanie')")
    discorso("amica_t4", "amica", CONOSCENTI, argomento="The black top", se="fatto('ep2_d17_top_ricevuto')")
    discorso("amica_t5", "amica", CONOSCENTI, argomento="After the Lantern", se="fatto('jacob_tornato')")
    discorso("amica_t6", "amica", CONOSCENTI, argomento="Mark and Simon", se="fatto('ep2_d19_sa_di_simon')")
    discorso("amica_t7", "amica", CONFIDENZA, argomento="What you told me on the carpet", se="fatto('ep2_d19_fantasia_joanie')")
    discorso("amica_c1", "amica", COMPLICI, flirt=True)
    discorso("amica_c2", "amica", COMPLICI, flirt=True)
    discorso("amica_c3", "amica", COMPLICI, flirt=True)
    discorso("amica_d1", "amica", INTIMI, flirt=True)
    discorso("amica_d2", "amica", INTIMI, flirt=True)


## --- Lunch with Daniel

label chat_amica_t1:
    label tel_chat_amica_t1_1:
    if telefono_minuti_blocco("tel_chat_amica_t1_1", "invia", 1):
        return
    $ msg("sara", "I keep hearing myself say «maybe» to Daniel.")
    return

label chat_amica_t1_entrata:
    label tel_chat_amica_t1_entrata_1:
    if telefono_minuti_blocco("tel_chat_amica_t1_entrata_1", "ricevi", 2):
        return
    $ msg("amica", "ok so")
    $ msg("amica", "daniel. lunch. SPEAK")
    label tel_chat_amica_t1_entrata_2:
    if telefono_minuti_blocco("tel_chat_amica_t1_entrata_2", "invia", 1):
        return
    $ msg("sara", "I said maybe. I keep hearing myself say it.")
    return

label chat_amica_t1_1:
    label tel_chat_amica_t1_1_1:
    if telefono_minuti_blocco("tel_chat_amica_t1_1_1", "ricevi", 2):
        return
    $ msg("amica", "how did it sound")
    $ msg("amica", "in your head. do the voice")
    label tel_chat_amica_t1_1_2:
    if telefono_minuti_blocco("tel_chat_amica_t1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Like someone else's voice. Lower.»":
            label tel_chat_amica_t1_1_3:
            if telefono_minuti_blocco("tel_chat_amica_t1_1_3", "invia", 1):
                return
            $ msg("sara", "Like someone else's voice. Lower.")
            $ caldo()
            label tel_chat_amica_t1_1_4:
            if telefono_minuti_blocco("tel_chat_amica_t1_1_4", "ricevi", 1):
                return
            $ msg("amica", "ok I need that voice on my answering machine")
        "«Like a mistake.»":
            label tel_chat_amica_t1_1_5:
            if telefono_minuti_blocco("tel_chat_amica_t1_1_5", "invia", 1):
                return
            $ msg("sara", "Like a mistake.")
            label tel_chat_amica_t1_1_6:
            if telefono_minuti_blocco("tel_chat_amica_t1_1_6", "ricevi", 1):
                return
            $ msg("amica", "mistakes are quieter. you've got a whole tone")
        "«Like «maybe». It's a normal word.»":
            label tel_chat_amica_t1_1_7:
            if telefono_minuti_blocco("tel_chat_amica_t1_1_7", "invia", 1):
                return
            $ msg("sara", "Like «maybe». It's a normal word.")
            label tel_chat_amica_t1_1_8:
            if telefono_minuti_blocco("tel_chat_amica_t1_1_8", "ricevi", 1):
                return
            $ msg("amica", "it's the least normal word there is. it's yes in a coat")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t1_2:
    label tel_chat_amica_t1_2_1:
    if telefono_minuti_blocco("tel_chat_amica_t1_2_1", "ricevi", 1):
        return
    $ msg("amica", "so what's the worst that happens. you eat a fish. he looks at you. you come home")
    label tel_chat_amica_t1_2_2:
    if telefono_minuti_blocco("tel_chat_amica_t1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«The looking is the part I can't picture.»":
            label tel_chat_amica_t1_2_3:
            if telefono_minuti_blocco("tel_chat_amica_t1_2_3", "invia", 1):
                return
            $ msg("sara", "The looking is the part I can't picture.")
            $ caldo()
            label tel_chat_amica_t1_2_4:
            if telefono_minuti_blocco("tel_chat_amica_t1_2_4", "ricevi", 1):
                return
            $ msg("amica", "liar. you've pictured the jacket and everything")
            sp "I have pictured the jacket."
        "«The worst is that [nome_compagno] finds out.»":
            label tel_chat_amica_t1_2_5:
            if telefono_minuti_blocco("tel_chat_amica_t1_2_5", "invia", 1):
                return
            $ msg("sara", "The worst is that [nome_compagno] finds out.")
            label tel_chat_amica_t1_2_6:
            if telefono_minuti_blocco("tel_chat_amica_t1_2_6", "ricevi", 1):
                return
            $ msg("amica", "finds out you had LUNCH. with a FORK")
        "«The worst is that I enjoy it.»":
            label tel_chat_amica_t1_2_7:
            if telefono_minuti_blocco("tel_chat_amica_t1_2_7", "invia", 1):
                return
            $ msg("sara", "The worst is that I enjoy it.")
            label tel_chat_amica_t1_2_8:
            if telefono_minuti_blocco("tel_chat_amica_t1_2_8", "ricevi", 1):
                return
            $ msg("amica", "oh no. not that. call someone")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t1_3:
    label tel_chat_amica_t1_3_1:
    if telefono_minuti_blocco("tel_chat_amica_t1_3_1", "ricevi", 1):
        return
    $ msg("amica", "can I say one serious thing and then I'll stop")
    label tel_chat_amica_t1_3_2:
    if telefono_minuti_blocco("tel_chat_amica_t1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Go on.»":
            label tel_chat_amica_t1_3_3:
            if telefono_minuti_blocco("tel_chat_amica_t1_3_3", "invia", 1):
                return
            $ msg("sara", "Go on.")
            label tel_chat_amica_t1_3_4:
            if telefono_minuti_blocco("tel_chat_amica_t1_3_4", "ricevi", 2):
                return
            $ msg("amica", "you never want anything out loud. you want it under a pile of coats")
            $ msg("amica", "I'd just like to see you want something with the lights on. even if it's a fish")
        "«You've never said one serious thing in your life.»":
            label tel_chat_amica_t1_3_5:
            if telefono_minuti_blocco("tel_chat_amica_t1_3_5", "invia", 1):
                return
            $ msg("sara", "You've never said one serious thing in your life.")
            label tel_chat_amica_t1_3_6:
            if telefono_minuti_blocco("tel_chat_amica_t1_3_6", "ricevi", 2):
                return
            $ msg("amica", "true. so imagine how bad it must be")
            $ msg("amica", "go to bed. maybe")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- My first piece

label chat_amica_t2:
    label tel_chat_amica_t2_1:
    if telefono_minuti_blocco("tel_chat_amica_t2_1", "invia", 1):
        return
    $ msg("sara", "Did you really frame my article in the bathroom?")
    return

label chat_amica_t2_1:
    label tel_chat_amica_t2_1_1:
    if telefono_minuti_blocco("tel_chat_amica_t2_1_1", "ricevi", 2):
        return
    $ msg("amica", "opposite the bath. it's the only place I sit still")
    $ msg("amica", "mark asked if he could move it. I asked if he'd like to move out")
    label tel_chat_amica_t2_1_2:
    if telefono_minuti_blocco("tel_chat_amica_t2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What does he do when he's in there?»":
            label tel_chat_amica_t2_1_3:
            if telefono_minuti_blocco("tel_chat_amica_t2_1_3", "invia", 1):
                return
            $ msg("sara", "What does he do when he's in there?")
            $ caldo()
            label tel_chat_amica_t2_1_4:
            if telefono_minuti_blocco("tel_chat_amica_t2_1_4", "ricevi", 1):
                return
            $ msg("amica", "reads it. out loud. he does all the voices")
        "«You're ridiculous.»":
            label tel_chat_amica_t2_1_5:
            if telefono_minuti_blocco("tel_chat_amica_t2_1_5", "invia", 1):
                return
            $ msg("sara", "You're ridiculous.")
            label tel_chat_amica_t2_1_6:
            if telefono_minuti_blocco("tel_chat_amica_t2_1_6", "ricevi", 1):
                return
            $ msg("amica", "I'm an early collector")
        "«The steam will ruin it.»":
            label tel_chat_amica_t2_1_7:
            if telefono_minuti_blocco("tel_chat_amica_t2_1_7", "invia", 1):
                return
            $ msg("sara", "The steam will ruin it.")
            label tel_chat_amica_t2_1_8:
            if telefono_minuti_blocco("tel_chat_amica_t2_1_8", "ricevi", 1):
                return
            $ msg("amica", "I LAMINATED it. who do you think I am")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t2_2:
    label tel_chat_amica_t2_2_1:
    if telefono_minuti_blocco("tel_chat_amica_t2_2_1", "ricevi", 2):
        return
    $ msg("amica", "you sent it to me first. before anyone")
    $ msg("amica", "I haven't mentioned it. I've been incredibly cool about it")
    label tel_chat_amica_t2_2_2:
    if telefono_minuti_blocco("tel_chat_amica_t2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You screamed for a whole minute.»":
            label tel_chat_amica_t2_2_3:
            if telefono_minuti_blocco("tel_chat_amica_t2_2_3", "invia", 1):
                return
            $ msg("sara", "You screamed for a whole minute.")
            $ caldo()
            label tel_chat_amica_t2_2_4:
            if telefono_minuti_blocco("tel_chat_amica_t2_2_4", "ricevi", 1):
                return
            $ msg("amica", "coolly")
        "«You've believed in it the longest.»":
            label tel_chat_amica_t2_2_5:
            if telefono_minuti_blocco("tel_chat_amica_t2_2_5", "invia", 1):
                return
            $ msg("sara", "You've believed in it the longest.")
            label tel_chat_amica_t2_2_6:
            if telefono_minuti_blocco("tel_chat_amica_t2_2_6", "ricevi", 1):
                return
            $ msg("amica", "ok well now I've got something in my eye and I'm at work")
        "«Alphabetical order.»":
            label tel_chat_amica_t2_2_7:
            if telefono_minuti_blocco("tel_chat_amica_t2_2_7", "invia", 1):
                return
            $ msg("sara", "Alphabetical order.")
            label tel_chat_amica_t2_2_8:
            if telefono_minuti_blocco("tel_chat_amica_t2_2_8", "ricevi", 1):
                return
            $ msg("amica", "J comes after everyone I know. nice try")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t2_3:
    label tel_chat_amica_t2_3_1:
    if telefono_minuti_blocco("tel_chat_amica_t2_3_1", "ricevi", 1):
        return
    $ msg("amica", "what did he say when you sent it to him")
    label tel_chat_amica_t2_3_2:
    if telefono_minuti_blocco("tel_chat_amica_t2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«He's printing it for the whole office. He's lovely about it.»":
            label tel_chat_amica_t2_3_3:
            if telefono_minuti_blocco("tel_chat_amica_t2_3_3", "invia", 1):
                return
            $ msg("sara", "He's printing it for the whole office. He's lovely about it.")
            label tel_chat_amica_t2_3_4:
            if telefono_minuti_blocco("tel_chat_amica_t2_3_4", "ricevi", 2):
                return
            $ msg("amica", "he is. he's a puppy with a printer")
            $ msg("amica", "and what do YOU think of it. nobody ever asks the writer")
        "«I think it's good. I think it's actually good.»":
            label tel_chat_amica_t2_3_5:
            if telefono_minuti_blocco("tel_chat_amica_t2_3_5", "invia", 1):
                return
            $ msg("sara", "I think it's good. I think it's actually good.")
            label tel_chat_amica_t2_3_6:
            if telefono_minuti_blocco("tel_chat_amica_t2_3_6", "ricevi", 1):
                return
            $ msg("amica", "say it again and don't look round to check if anybody heard")
            sp "How does she know I looked round?"
        "«There's a comma I'd move.»":
            label tel_chat_amica_t2_3_7:
            if telefono_minuti_blocco("tel_chat_amica_t2_3_7", "invia", 1):
                return
            $ msg("sara", "There's a comma I'd move.")
            label tel_chat_amica_t2_3_8:
            if telefono_minuti_blocco("tel_chat_amica_t2_3_8", "ricevi", 1):
                return
            $ msg("amica", "there's always a comma with you. leave it. let it live")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- What I told you in the kitchen

label chat_amica_t3:
    label tel_chat_amica_t3_1:
    if telefono_minuti_blocco("tel_chat_amica_t3_1", "invia", 1):
        return
    $ msg("sara", "Thank you for Tuesday. For the kitchen.")
    return

label chat_amica_t3_entrata:
    label tel_chat_amica_t3_entrata_1:
    if telefono_minuti_blocco("tel_chat_amica_t3_entrata_1", "ricevi", 1):
        return
    $ msg("amica", "still thinking about you and that jug")
    label tel_chat_amica_t3_entrata_2:
    if telefono_minuti_blocco("tel_chat_amica_t3_entrata_2", "invia", 1):
        return
    $ msg("sara", "Thank you for that. For the kitchen.")
    return

label chat_amica_t3_1:
    label tel_chat_amica_t3_1_1:
    if telefono_minuti_blocco("tel_chat_amica_t3_1_1", "ricevi", 2):
        return
    $ msg("amica", "thank YOU. I was about to dry the same plate for the fifth time")
    $ msg("amica", "have you two talked since. properly")
    label tel_chat_amica_t3_1_2:
    if telefono_minuti_blocco("tel_chat_amica_t3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«A bit. Around the edges.»":
            label tel_chat_amica_t3_1_3:
            if telefono_minuti_blocco("tel_chat_amica_t3_1_3", "invia", 1):
                return
            $ msg("sara", "A bit. Around the edges.")
            label tel_chat_amica_t3_1_4:
            if telefono_minuti_blocco("tel_chat_amica_t3_1_4", "ricevi", 1):
                return
            $ msg("amica", "that's not talking that's hoovering")
        "«Not really.»":
            label tel_chat_amica_t3_1_5:
            if telefono_minuti_blocco("tel_chat_amica_t3_1_5", "invia", 1):
                return
            $ msg("sara", "Not really.")
            $ caldo()
            label tel_chat_amica_t3_1_6:
            if telefono_minuti_blocco("tel_chat_amica_t3_1_6", "ricevi", 1):
                return
            $ msg("amica", "ok. I'm not going to push. I'm going to sit here and push silently")
        "«He said sorry. He meant it.»":
            label tel_chat_amica_t3_1_7:
            if telefono_minuti_blocco("tel_chat_amica_t3_1_7", "invia", 1):
                return
            $ msg("sara", "He said sorry. He meant it.")
            label tel_chat_amica_t3_1_8:
            if telefono_minuti_blocco("tel_chat_amica_t3_1_8", "ricevi", 1):
                return
            $ msg("amica", "I know he did. he'd say sorry to a chair")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t3_2:
    label tel_chat_amica_t3_2_1:
    if telefono_minuti_blocco("tel_chat_amica_t3_2_1", "ricevi", 1):
        return
    $ msg("amica", "can I ask you what bothered you. him reading it. or him reading THAT")
    label tel_chat_amica_t3_2_2:
    if telefono_minuti_blocco("tel_chat_amica_t3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That he didn't ask.»":
            label tel_chat_amica_t3_2_3:
            if telefono_minuti_blocco("tel_chat_amica_t3_2_3", "invia", 1):
                return
            $ msg("sara", "That he didn't ask.")
            label tel_chat_amica_t3_2_4:
            if telefono_minuti_blocco("tel_chat_amica_t3_2_4", "ricevi", 1):
                return
            $ msg("amica", "yeah. it's yours. it's the one thing that was only yours")
        "«That bit. The terrace bit.»":
            label tel_chat_amica_t3_2_5:
            if telefono_minuti_blocco("tel_chat_amica_t3_2_5", "invia", 1):
                return
            $ msg("sara", "That bit. The terrace bit.")
            $ caldo()
            label tel_chat_amica_t3_2_6:
            if telefono_minuti_blocco("tel_chat_amica_t3_2_6", "ricevi", 2):
                return
            $ msg("amica", "thought so")
            $ msg("amica", "was he in it")
            sp "The fiancé laughing behind the glass. Yes. He was in it."
        "«I haven't worked it out yet.»":
            label tel_chat_amica_t3_2_7:
            if telefono_minuti_blocco("tel_chat_amica_t3_2_7", "invia", 1):
                return
            $ msg("sara", "I haven't worked it out yet.")
            label tel_chat_amica_t3_2_8:
            if telefono_minuti_blocco("tel_chat_amica_t3_2_8", "ricevi", 1):
                return
            $ msg("amica", "you will. it'll come out on page ninety in somebody else's mouth")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t3_3:
    label tel_chat_amica_t3_3_1:
    if telefono_minuti_blocco("tel_chat_amica_t3_3_1", "ricevi", 1):
        return
    $ msg("amica", "next time write it at mine. I've got a desk. it's under some things")
    label tel_chat_amica_t3_3_2:
    if telefono_minuti_blocco("tel_chat_amica_t3_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What things?»":
            label tel_chat_amica_t3_3_3:
            if telefono_minuti_blocco("tel_chat_amica_t3_3_3", "invia", 1):
                return
            $ msg("sara", "What things?")
            label tel_chat_amica_t3_3_4:
            if telefono_minuti_blocco("tel_chat_amica_t3_3_4", "ricevi", 1):
                return
            $ msg("amica", "it's mostly things. there's a desk shape")
        "«I might, you know.»":
            label tel_chat_amica_t3_3_5:
            if telefono_minuti_blocco("tel_chat_amica_t3_3_5", "invia", 1):
                return
            $ msg("sara", "I might, you know.")
            label tel_chat_amica_t3_3_6:
            if telefono_minuti_blocco("tel_chat_amica_t3_3_6", "ricevi", 2):
                return
            $ msg("amica", "I'll clear it. I'll make that horrible coffee you like. and I will NOT look over your shoulder")
            $ msg("amica", "I'll look at you from the sofa. you do a thing with your mouth when it's going well")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t3_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t3_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- The black top

label chat_amica_t4:
    label tel_chat_amica_t4_1:
    if telefono_minuti_blocco("tel_chat_amica_t4_1", "invia", 1):
        return
    $ msg("sara", "I'm holding your top up to the light. I can see the whole kitchen through it.")
    return

label chat_amica_t4_entrata:
    label tel_chat_amica_t4_entrata_1:
    if telefono_minuti_blocco("tel_chat_amica_t4_entrata_1", "ricevi", 2):
        return
    $ msg("amica", "have you opened it")
    $ msg("amica", "have you held it up")
    label tel_chat_amica_t4_entrata_2:
    if telefono_minuti_blocco("tel_chat_amica_t4_entrata_2", "invia", 1):
        return
    $ msg("sara", "I can see the whole kitchen through it.")
    return

label chat_amica_t4_1:
    label tel_chat_amica_t4_1_1:
    if telefono_minuti_blocco("tel_chat_amica_t4_1_1", "ricevi", 2):
        return
    $ msg("amica", "that's how you know it's good")
    $ msg("amica", "put it ON")
    label tel_chat_amica_t4_1_2:
    if telefono_minuti_blocco("tel_chat_amica_t4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It's on.»":
            label tel_chat_amica_t4_1_3:
            if telefono_minuti_blocco("tel_chat_amica_t4_1_3", "invia", 1):
                return
            $ msg("sara", "It's on.")
            $ caldo()
            label tel_chat_amica_t4_1_4:
            if telefono_minuti_blocco("tel_chat_amica_t4_1_4", "ricevi", 2):
                return
            $ msg("amica", "......")
            $ msg("amica", "ok and")
        "«It's on the back of a chair.»":
            label tel_chat_amica_t4_1_5:
            if telefono_minuti_blocco("tel_chat_amica_t4_1_5", "invia", 1):
                return
            $ msg("sara", "It's on the back of a chair.")
            label tel_chat_amica_t4_1_6:
            if telefono_minuti_blocco("tel_chat_amica_t4_1_6", "ricevi", 1):
                return
            $ msg("amica", "the chair must be having a great night")
        "«It's back in the box.»":
            label tel_chat_amica_t4_1_7:
            if telefono_minuti_blocco("tel_chat_amica_t4_1_7", "invia", 1):
                return
            $ msg("sara", "It's back in the box.")
            label tel_chat_amica_t4_1_8:
            if telefono_minuti_blocco("tel_chat_amica_t4_1_8", "ricevi", 1):
                return
            $ msg("amica", "that box gets more action than most people")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t4_2:
    label tel_chat_amica_t4_2_1:
    if telefono_minuti_blocco("tel_chat_amica_t4_2_1", "ricevi", 1):
        return
    $ msg("amica", "what exactly are you scared of. list them. I'll tick them off")
    label tel_chat_amica_t4_2_2:
    if telefono_minuti_blocco("tel_chat_amica_t4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That people will look.»":
            label tel_chat_amica_t4_2_3:
            if telefono_minuti_blocco("tel_chat_amica_t4_2_3", "invia", 1):
                return
            $ msg("sara", "That people will look.")
            label tel_chat_amica_t4_2_4:
            if telefono_minuti_blocco("tel_chat_amica_t4_2_4", "ricevi", 1):
                return
            $ msg("amica", "yes that's the feature")
        "«That I'll like it when they do.»":
            label tel_chat_amica_t4_2_5:
            if telefono_minuti_blocco("tel_chat_amica_t4_2_5", "invia", 1):
                return
            $ msg("sara", "That I'll like it when they do.")
            $ caldo()
            label tel_chat_amica_t4_2_6:
            if telefono_minuti_blocco("tel_chat_amica_t4_2_6", "ricevi", 1):
                return
            $ msg("amica", "ah. there she is. hello")
            sp "I typed that. I typed that and sent it."
        "«That I'll look like somebody else.»":
            label tel_chat_amica_t4_2_7:
            if telefono_minuti_blocco("tel_chat_amica_t4_2_7", "invia", 1):
                return
            $ msg("sara", "That I'll look like somebody else.")
            label tel_chat_amica_t4_2_8:
            if telefono_minuti_blocco("tel_chat_amica_t4_2_8", "ricevi", 1):
                return
            $ msg("amica", "you'll look like you without the seven layers of sorry")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t4_3:
    label tel_chat_amica_t4_3_1:
    if telefono_minuti_blocco("tel_chat_amica_t4_3_1", "ricevi", 1):
        return
    $ msg("amica", "you don't have to wear it anywhere. wear it to do the washing up")
    label tel_chat_amica_t4_3_2:
    if telefono_minuti_blocco("tel_chat_amica_t4_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«In that? To do the washing up?»":
            label tel_chat_amica_t4_3_3:
            if telefono_minuti_blocco("tel_chat_amica_t4_3_3", "invia", 1):
                return
            $ msg("sara", "In that? To do the washing up?")
            label tel_chat_amica_t4_3_4:
            if telefono_minuti_blocco("tel_chat_amica_t4_3_4", "ricevi", 1):
                return
            $ msg("amica", "best washed plates in england")
        "«Would you wear it?»":
            label tel_chat_amica_t4_3_5:
            if telefono_minuti_blocco("tel_chat_amica_t4_3_5", "invia", 1):
                return
            $ msg("sara", "Would you wear it?")
            label tel_chat_amica_t4_3_6:
            if telefono_minuti_blocco("tel_chat_amica_t4_3_6", "ricevi", 1):
                return
            $ msg("amica", "I've got one. I bought two. I wasn't going to make you do it on your own")
            sp "She bought two."
            label tel_chat_amica_t4_3_7:
            if telefono_minuti_blocco("tel_chat_amica_t4_3_7", "ricevi", 1):
                return
            $ msg("amica", "go on. night. give the chair my love")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t4_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t4_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- After the Lantern

label chat_amica_t5:
    label tel_chat_amica_t5_1:
    if telefono_minuti_blocco("tel_chat_amica_t5_1", "invia", 1):
        return
    $ msg("sara", "What were the odds, Joanie?")
    return

label chat_amica_t5_entrata:
    label tel_chat_amica_t5_entrata_1:
    if telefono_minuti_blocco("tel_chat_amica_t5_entrata_1", "ricevi", 2):
        return
    $ msg("amica", "soooo")
    $ msg("amica", "fancy that")
    label tel_chat_amica_t5_entrata_2:
    if telefono_minuti_blocco("tel_chat_amica_t5_entrata_2", "invia", 1):
        return
    $ msg("sara", "What were the odds, Joanie?")
    return

label chat_amica_t5_1:
    label tel_chat_amica_t5_1_1:
    if telefono_minuti_blocco("tel_chat_amica_t5_1_1", "ricevi", 2):
        return
    $ msg("amica", "of what")
    $ msg("amica", "of a person being in a bar. on a friday. in a town. pretty good I'd say")
    label tel_chat_amica_t5_1_2:
    if telefono_minuti_blocco("tel_chat_amica_t5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You were humming.»":
            label tel_chat_amica_t5_1_3:
            if telefono_minuti_blocco("tel_chat_amica_t5_1_3", "invia", 1):
                return
            $ msg("sara", "You were humming.")
            $ caldo()
            label tel_chat_amica_t5_1_4:
            if telefono_minuti_blocco("tel_chat_amica_t5_1_4", "ricevi", 1):
                return
            $ msg("amica", "I hum. I'm a hummer. it's a medical thing")
        "«Did you know he'd be there?»":
            label tel_chat_amica_t5_1_5:
            if telefono_minuti_blocco("tel_chat_amica_t5_1_5", "invia", 1):
                return
            $ msg("sara", "Did you know he'd be there?")
            label tel_chat_amica_t5_1_6:
            if telefono_minuti_blocco("tel_chat_amica_t5_1_6", "ricevi", 2):
                return
            $ msg("amica", "define know")
            $ msg("amica", "define there")
        "«I nearly fell off my stool.»":
            label tel_chat_amica_t5_1_7:
            if telefono_minuti_blocco("tel_chat_amica_t5_1_7", "invia", 1):
                return
            $ msg("sara", "I nearly fell off my stool.")
            label tel_chat_amica_t5_1_8:
            if telefono_minuti_blocco("tel_chat_amica_t5_1_8", "ricevi", 1):
                return
            $ msg("amica", "I saw. you went pink from the collar up. it was like a sunrise")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t5_2:
    label tel_chat_amica_t5_2_1:
    if telefono_minuti_blocco("tel_chat_amica_t5_2_1", "ricevi", 1):
        return
    $ msg("amica", "so. four years. how was it")
    label tel_chat_amica_t5_2_2:
    if telefono_minuti_blocco("tel_chat_amica_t5_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It was like putting on an old coat and finding money in it.»":
            label tel_chat_amica_t5_2_3:
            if telefono_minuti_blocco("tel_chat_amica_t5_2_3", "invia", 1):
                return
            $ msg("sara", "It was like putting on an old coat and finding money in it.")
            $ caldo()
            label tel_chat_amica_t5_2_4:
            if telefono_minuti_blocco("tel_chat_amica_t5_2_4", "ricevi", 1):
                return
            $ msg("amica", "SARA. you can't just say things like that and then be a person who writes horoscopes")
        "«It was strange.»":
            label tel_chat_amica_t5_2_5:
            if telefono_minuti_blocco("tel_chat_amica_t5_2_5", "invia", 1):
                return
            $ msg("sara", "It was strange.")
            label tel_chat_amica_t5_2_6:
            if telefono_minuti_blocco("tel_chat_amica_t5_2_6", "ricevi", 1):
                return
            $ msg("amica", "strange good or strange dentist")
        "«He hasn't changed.»":
            label tel_chat_amica_t5_2_7:
            if telefono_minuti_blocco("tel_chat_amica_t5_2_7", "invia", 1):
                return
            $ msg("sara", "He hasn't changed.")
            label tel_chat_amica_t5_2_8:
            if telefono_minuti_blocco("tel_chat_amica_t5_2_8", "ricevi", 1):
                return
            $ msg("amica", "no. you have though. he noticed. I watched him notice")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t5_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t5_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t5_3:
    label tel_chat_amica_t5_3_1:
    if telefono_minuti_blocco("tel_chat_amica_t5_3_1", "ricevi", 1):
        return
    $ msg("amica", "are you telling [nome_compagno]")
    label tel_chat_amica_t5_3_2:
    if telefono_minuti_blocco("tel_chat_amica_t5_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«There's nothing to tell.»":
            label tel_chat_amica_t5_3_3:
            if telefono_minuti_blocco("tel_chat_amica_t5_3_3", "invia", 1):
                return
            $ msg("sara", "There's nothing to tell.")
            label tel_chat_amica_t5_3_4:
            if telefono_minuti_blocco("tel_chat_amica_t5_3_4", "ricevi", 1):
                return
            $ msg("amica", "then it'll be a short conversation")
        "«I will. I just want to have it to myself for a night.»":
            label tel_chat_amica_t5_3_5:
            if telefono_minuti_blocco("tel_chat_amica_t5_3_5", "invia", 1):
                return
            $ msg("sara", "I will. I just want to have it to myself for a night.")
            label tel_chat_amica_t5_3_6:
            if telefono_minuti_blocco("tel_chat_amica_t5_3_6", "ricevi", 1):
                return
            $ msg("amica", "one night. that's fair. I won't even ask you what you do with it")
        "«Should I?»":
            label tel_chat_amica_t5_3_7:
            if telefono_minuti_blocco("tel_chat_amica_t5_3_7", "invia", 1):
                return
            $ msg("sara", "Should I?")
            label tel_chat_amica_t5_3_8:
            if telefono_minuti_blocco("tel_chat_amica_t5_3_8", "ricevi", 2):
                return
            $ msg("amica", "you should do what lets you sleep. I sleep like a baby and look at me")
            $ msg("amica", "you laughed tonight. or you nearly did. either way I was there. night night")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t5_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t5_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Mark and Simon

label chat_amica_t6:
    label tel_chat_amica_t6_1:
    if telefono_minuti_blocco("tel_chat_amica_t6_1", "invia", 1):
        return
    $ msg("sara", "I'm still thinking about what you said. About Mark.")
    return

label chat_amica_t6_1:
    label tel_chat_amica_t6_1_1:
    if telefono_minuti_blocco("tel_chat_amica_t6_1_1", "ricevi", 1):
        return
    $ msg("amica", "good thinking or looking at me differently thinking")
    label tel_chat_amica_t6_1_2:
    if telefono_minuti_blocco("tel_chat_amica_t6_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Neither. Just thinking.»":
            label tel_chat_amica_t6_1_3:
            if telefono_minuti_blocco("tel_chat_amica_t6_1_3", "invia", 1):
                return
            $ msg("sara", "Neither. Just thinking.")
            label tel_chat_amica_t6_1_4:
            if telefono_minuti_blocco("tel_chat_amica_t6_1_4", "ricevi", 1):
                return
            $ msg("amica", "that's the one that scares me")
        "«I couldn't find the hole in it.»":
            label tel_chat_amica_t6_1_5:
            if telefono_minuti_blocco("tel_chat_amica_t6_1_5", "invia", 1):
                return
            $ msg("sara", "I couldn't find the hole in it.")
            $ caldo()
            label tel_chat_amica_t6_1_6:
            if telefono_minuti_blocco("tel_chat_amica_t6_1_6", "ricevi", 1):
                return
            $ msg("amica", "I know. I've looked. I turn it round at night like a jumper")
        "«I felt sorry for Mark.»":
            label tel_chat_amica_t6_1_7:
            if telefono_minuti_blocco("tel_chat_amica_t6_1_7", "invia", 1):
                return
            $ msg("sara", "I felt sorry for Mark.")
            label tel_chat_amica_t6_1_8:
            if telefono_minuti_blocco("tel_chat_amica_t6_1_8", "ricevi", 1):
                return
            $ msg("amica", "yeah. I do too sometimes. then he whistles while he does the bins and I think, would he swap")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t6_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t6_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t6_2:
    label tel_chat_amica_t6_2_1:
    if telefono_minuti_blocco("tel_chat_amica_t6_2_1", "ricevi", 1):
        return
    $ msg("amica", "you can ask me anything. I'd rather you asked")
    label tel_chat_amica_t6_2_2:
    if telefono_minuti_blocco("tel_chat_amica_t6_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Are you ever afraid he'll find out?»":
            label tel_chat_amica_t6_2_3:
            if telefono_minuti_blocco("tel_chat_amica_t6_2_3", "invia", 1):
                return
            $ msg("sara", "Are you ever afraid he'll find out?")
            label tel_chat_amica_t6_2_4:
            if telefono_minuti_blocco("tel_chat_amica_t6_2_4", "ricevi", 1):
                return
            $ msg("amica", "every day for about a minute. usually in the queue at the bank")
        "«Do you love Simon?»":
            label tel_chat_amica_t6_2_5:
            if telefono_minuti_blocco("tel_chat_amica_t6_2_5", "invia", 1):
                return
            $ msg("sara", "Do you love Simon?")
            $ caldo()
            label tel_chat_amica_t6_2_6:
            if telefono_minuti_blocco("tel_chat_amica_t6_2_6", "ricevi", 1):
                return
            $ msg("amica", "no. god no. I like him the way you like swimming")
        "«Does it make you happy?»":
            label tel_chat_amica_t6_2_7:
            if telefono_minuti_blocco("tel_chat_amica_t6_2_7", "invia", 1):
                return
            $ msg("sara", "Does it make you happy?")
            label tel_chat_amica_t6_2_8:
            if telefono_minuti_blocco("tel_chat_amica_t6_2_8", "ricevi", 1):
                return
            $ msg("amica", "it makes me nice. I don't know if that's the same. it might be better")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t6_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t6_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t6_3:
    label tel_chat_amica_t6_3_1:
    if telefono_minuti_blocco("tel_chat_amica_t6_3_1", "ricevi", 1):
        return
    $ msg("amica", "I haven't told anyone but you. ever. I want you to know that")
    label tel_chat_amica_t6_3_2:
    if telefono_minuti_blocco("tel_chat_amica_t6_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I know. I won't say a word.»":
            label tel_chat_amica_t6_3_3:
            if telefono_minuti_blocco("tel_chat_amica_t6_3_3", "invia", 1):
                return
            $ msg("sara", "I know. I won't say a word.")
            label tel_chat_amica_t6_3_4:
            if telefono_minuti_blocco("tel_chat_amica_t6_3_4", "ricevi", 1):
                return
            $ msg("amica", "I know you won't. you've got the face of a safe")
        "«I'm glad you told me. Even if I don't know what to do with it.»":
            label tel_chat_amica_t6_3_5:
            if telefono_minuti_blocco("tel_chat_amica_t6_3_5", "invia", 1):
                return
            $ msg("sara", "I'm glad you told me. Even if I don't know what to do with it.")
            label tel_chat_amica_t6_3_6:
            if telefono_minuti_blocco("tel_chat_amica_t6_3_6", "ricevi", 2):
                return
            $ msg("amica", "you don't do anything with it. you just hold the other end")
            $ msg("amica", "thanks for not going all quiet. night")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t6_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t6_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- What you told me on the carpet

label chat_amica_t7:
    label tel_chat_amica_t7_1:
    if telefono_minuti_blocco("tel_chat_amica_t7_1", "invia", 1):
        return
    $ msg("sara", "I'm not looking at you differently. I thought you might be lying there wondering.")
    return

label chat_amica_t7_entrata:
    label tel_chat_amica_t7_entrata_1:
    if telefono_minuti_blocco("tel_chat_amica_t7_entrata_1", "ricevi", 2):
        return
    $ msg("amica", "are you up")
    $ msg("amica", "you're allowed not to answer")
    label tel_chat_amica_t7_entrata_2:
    if telefono_minuti_blocco("tel_chat_amica_t7_entrata_2", "invia", 1):
        return
    $ msg("sara", "I'm up, and I'm not looking at you differently. Were you lying there wondering?")
    return

label chat_amica_t7_1:
    label tel_chat_amica_t7_1_1:
    if telefono_minuti_blocco("tel_chat_amica_t7_1_1", "ricevi", 2):
        return
    $ msg("amica", "I was")
    $ msg("amica", "I've been looking at the ceiling since you left. there's a stain like a rabbit")
    label tel_chat_amica_t7_1_2:
    if telefono_minuti_blocco("tel_chat_amica_t7_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I know that rabbit. I've lain under that rabbit.»":
            label tel_chat_amica_t7_1_3:
            if telefono_minuti_blocco("tel_chat_amica_t7_1_3", "invia", 1):
                return
            $ msg("sara", "I know that rabbit. I've lain under that rabbit.")
            label tel_chat_amica_t7_1_4:
            if telefono_minuti_blocco("tel_chat_amica_t7_1_4", "ricevi", 1):
                return
            $ msg("amica", "don't. I'll cry again and I've only just got my eyes back")
        "«You could have told me years ago.»":
            label tel_chat_amica_t7_1_5:
            if telefono_minuti_blocco("tel_chat_amica_t7_1_5", "invia", 1):
                return
            $ msg("sara", "You could have told me years ago.")
            $ caldo()
            label tel_chat_amica_t7_1_6:
            if telefono_minuti_blocco("tel_chat_amica_t7_1_6", "ricevi", 1):
                return
            $ msg("amica", "I couldn't. years ago you'd have said sorry. for existing. near me. while I had it")
        "«It was brave, telling me.»":
            label tel_chat_amica_t7_1_7:
            if telefono_minuti_blocco("tel_chat_amica_t7_1_7", "invia", 1):
                return
            $ msg("sara", "It was brave, telling me.")
            label tel_chat_amica_t7_1_8:
            if telefono_minuti_blocco("tel_chat_amica_t7_1_8", "ricevi", 1):
                return
            $ msg("amica", "it was wine and a good rug")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t7_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t7_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t7_2:
    label tel_chat_amica_t7_2_1:
    if telefono_minuti_blocco("tel_chat_amica_t7_2_1", "ricevi", 1):
        return
    $ msg("amica", "can I ask. you don't have to answer. was it horrible to hear")
    label tel_chat_amica_t7_2_2:
    if telefono_minuti_blocco("tel_chat_amica_t7_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«No. It was strange, and then it wasn't.»":
            label tel_chat_amica_t7_2_3:
            if telefono_minuti_blocco("tel_chat_amica_t7_2_3", "invia", 1):
                return
            $ msg("sara", "No. It was strange, and then it wasn't.")
            $ caldo()
            label tel_chat_amica_t7_2_4:
            if telefono_minuti_blocco("tel_chat_amica_t7_2_4", "ricevi", 1):
                return
            $ msg("amica", "how long was the strange bit")
        "«About as long as it took you to stop crying.»":
            label tel_chat_amica_t7_2_5:
            if telefono_minuti_blocco("tel_chat_amica_t7_2_5", "invia", 1):
                return
            $ msg("sara", "About as long as it took you to stop crying.")
            sp "She'd be just there, she said. And I'd look at her, and not be sorry."
        "«A little. Not the way you think.»":
            label tel_chat_amica_t7_2_6:
            if telefono_minuti_blocco("tel_chat_amica_t7_2_6", "invia", 1):
                return
            $ msg("sara", "A little. Not the way you think.")
            label tel_chat_amica_t7_2_7:
            if telefono_minuti_blocco("tel_chat_amica_t7_2_7", "ricevi", 1):
                return
            $ msg("amica", "ok. I can live with a little")
        "«I don't know yet. Ask me on Sunday.»":
            label tel_chat_amica_t7_2_8:
            if telefono_minuti_blocco("tel_chat_amica_t7_2_8", "invia", 1):
                return
            $ msg("sara", "I don't know yet. Ask me on Sunday.")
            label tel_chat_amica_t7_2_9:
            if telefono_minuti_blocco("tel_chat_amica_t7_2_9", "ricevi", 1):
                return
            $ msg("amica", "I'll put it in my diary. «ask sara if horrible»")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t7_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t7_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_t7_3:
    label tel_chat_amica_t7_3_1:
    if telefono_minuti_blocco("tel_chat_amica_t7_3_1", "ricevi", 1):
        return
    $ msg("amica", "it's only a thing in my head. it doesn't need to go anywhere. it's been very happy in there")
    label tel_chat_amica_t7_3_2:
    if telefono_minuti_blocco("tel_chat_amica_t7_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It can stay there. Safe.»":
            label tel_chat_amica_t7_3_3:
            if telefono_minuti_blocco("tel_chat_amica_t7_3_3", "invia", 1):
                return
            $ msg("sara", "It can stay there. Safe.")
            label tel_chat_amica_t7_3_4:
            if telefono_minuti_blocco("tel_chat_amica_t7_3_4", "ricevi", 1):
                return
            $ msg("amica", "safe. good. I'd hate for it to catch cold")
        "«And if one day I felt like teasing you about it?»":
            label tel_chat_amica_t7_3_5:
            if telefono_minuti_blocco("tel_chat_amica_t7_3_5", "invia", 1):
                return
            $ msg("sara", "And if one day I felt like teasing you about it?")
            label tel_chat_amica_t7_3_6:
            if telefono_minuti_blocco("tel_chat_amica_t7_3_6", "ricevi", 2):
                return
            $ msg("amica", "then I'd die. happily. you'd get the flat")
            $ msg("amica", "goodnight best person. one eye open ;)")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t7_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_t7_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: indispensabili

label chat_amica_c1:
    label tel_chat_amica_c1_1:
    if telefono_minuti_blocco("tel_chat_amica_c1_1", "invia", 1):
        return
    $ msg("sara", "I had a bad day and I noticed you were the first person I wanted to tell.")
    return

label chat_amica_c1_1:
    label tel_chat_amica_c1_1_1:
    if telefono_minuti_blocco("tel_chat_amica_c1_1_1", "ricevi", 2):
        return
    $ msg("amica", "before the puppy")
    $ msg("amica", "interesting. go on. I've put my face cream down")
    label tel_chat_amica_c1_1_2:
    if telefono_minuti_blocco("tel_chat_amica_c1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Before anyone.»":
            label tel_chat_amica_c1_1_3:
            if telefono_minuti_blocco("tel_chat_amica_c1_1_3", "invia", 1):
                return
            $ msg("sara", "Before anyone.")
            $ caldo()
            label tel_chat_amica_c1_1_4:
            if telefono_minuti_blocco("tel_chat_amica_c1_1_4", "ricevi", 1):
                return
            $ msg("amica", "you can't say that to a woman with one eyebrow on")
        "«Alphabetical order again.»":
            label tel_chat_amica_c1_1_5:
            if telefono_minuti_blocco("tel_chat_amica_c1_1_5", "invia", 1):
                return
            $ msg("sara", "Alphabetical order again.")
            label tel_chat_amica_c1_1_6:
            if telefono_minuti_blocco("tel_chat_amica_c1_1_6", "ricevi", 1):
                return
            $ msg("amica", "J. sara. we've BEEN through J")
        "«He'd have tried to fix it.»":
            label tel_chat_amica_c1_1_7:
            if telefono_minuti_blocco("tel_chat_amica_c1_1_7", "invia", 1):
                return
            $ msg("sara", "He'd have tried to fix it.")
            label tel_chat_amica_c1_1_8:
            if telefono_minuti_blocco("tel_chat_amica_c1_1_8", "ricevi", 1):
                return
            $ msg("amica", "and me")
            sp "You'd have taken my side before I'd finished."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_c1_2:
    label tel_chat_amica_c1_2_1:
    if telefono_minuti_blocco("tel_chat_amica_c1_2_1", "ricevi", 1):
        return
    $ msg("amica", "what do you need. options. one, I come round. two, I tell you you're gorgeous until you get annoyed")
    label tel_chat_amica_c1_2_2:
    if telefono_minuti_blocco("tel_chat_amica_c1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Two. Until I get annoyed.»":
            label tel_chat_amica_c1_2_3:
            if telefono_minuti_blocco("tel_chat_amica_c1_2_3", "invia", 1):
                return
            $ msg("sara", "Two. Until I get annoyed.")
            $ caldo()
            label tel_chat_amica_c1_2_4:
            if telefono_minuti_blocco("tel_chat_amica_c1_2_4", "ricevi", 2):
                return
            $ msg("amica", "gorgeous. the neck. the hands. that mouth when you're trying not to laugh at somebody's shoes")
            $ msg("amica", "are you annoyed")
        "«Not yet.»":
            label tel_chat_amica_c1_2_5:
            if telefono_minuti_blocco("tel_chat_amica_c1_2_5", "invia", 1):
                return
            $ msg("sara", "Not yet.")
            label tel_chat_amica_c1_2_6:
            if telefono_minuti_blocco("tel_chat_amica_c1_2_6", "ricevi", 1):
                return
            $ msg("amica", "good because I've only done the top half")
        "«One, but it's midnight.»":
            label tel_chat_amica_c1_2_7:
            if telefono_minuti_blocco("tel_chat_amica_c1_2_7", "invia", 1):
                return
            $ msg("sara", "One, but it's midnight.")
            label tel_chat_amica_c1_2_8:
            if telefono_minuti_blocco("tel_chat_amica_c1_2_8", "ricevi", 1):
                return
            $ msg("amica", "I've got a coat and no morals")
        "«Let's leave it there, Jo. You'll make me blush.»":
            label tel_chat_amica_c1_2_9:
            if telefono_minuti_blocco("tel_chat_amica_c1_2_9", "invia", 1):
                return
            $ msg("sara", "Let's leave it there, Jo. You'll make me blush.")
            $ frena()
            label tel_chat_amica_c1_2_10:
            if telefono_minuti_blocco("tel_chat_amica_c1_2_10", "ricevi", 1):
                return
            $ msg("amica", "I have made you blush. I'll stop while I'm winning")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_c1_3:
    label tel_chat_amica_c1_3_1:
    if telefono_minuti_blocco("tel_chat_amica_c1_3_1", "ricevi", 1):
        return
    $ msg("amica", "you know it's the same for me. you're the first one")
    label tel_chat_amica_c1_3_2:
    if telefono_minuti_blocco("tel_chat_amica_c1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Even before Simon?»":
            label tel_chat_amica_c1_3_3:
            if telefono_minuti_blocco("tel_chat_amica_c1_3_3", "invia", 1):
                return
            $ msg("sara", "Even before Simon?")
            label tel_chat_amica_c1_3_4:
            if telefono_minuti_blocco("tel_chat_amica_c1_3_4", "ricevi", 1):
                return
            $ msg("amica", "simon is a hobby. you're the house")
        "«I know.»":
            label tel_chat_amica_c1_3_5:
            if telefono_minuti_blocco("tel_chat_amica_c1_3_5", "invia", 1):
                return
            $ msg("sara", "I know.")
            label tel_chat_amica_c1_3_6:
            if telefono_minuti_blocco("tel_chat_amica_c1_3_6", "ricevi", 2):
                return
            $ msg("amica", "good. I don't say it enough. I say it in shoes and lunches")
            $ msg("amica", "sleep. the neck can have the night off")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: segreti solo per Joanie

label chat_amica_c2:
    label tel_chat_amica_c2_1:
    if telefono_minuti_blocco("tel_chat_amica_c2_1", "invia", 1):
        return
    $ msg("sara", "Tell me something you've never told anybody.")
    return

label chat_amica_c2_entrata:
    label tel_chat_amica_c2_entrata_1:
    if telefono_minuti_blocco("tel_chat_amica_c2_entrata_1", "ricevi", 1):
        return
    $ msg("amica", "can't sleep. entertain me")
    label tel_chat_amica_c2_entrata_2:
    if telefono_minuti_blocco("tel_chat_amica_c2_entrata_2", "invia", 1):
        return
    $ msg("sara", "Tell me something you've never told anybody.")
    return

label chat_amica_c2_1:
    label tel_chat_amica_c2_1_1:
    if telefono_minuti_blocco("tel_chat_amica_c2_1_1", "ricevi", 1):
        return
    $ msg("amica", "in exchange for what")
    label tel_chat_amica_c2_1_2:
    if telefono_minuti_blocco("tel_chat_amica_c2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«One of mine. Same size.»":
            label tel_chat_amica_c2_1_3:
            if telefono_minuti_blocco("tel_chat_amica_c2_1_3", "invia", 1):
                return
            $ msg("sara", "One of mine. Same size.")
            label tel_chat_amica_c2_1_4:
            if telefono_minuti_blocco("tel_chat_amica_c2_1_4", "ricevi", 1):
                return
            $ msg("amica", "oh I like this shop")
        "«Nothing. I'm greedy.»":
            label tel_chat_amica_c2_1_5:
            if telefono_minuti_blocco("tel_chat_amica_c2_1_5", "invia", 1):
                return
            $ msg("sara", "Nothing. I'm greedy.")
            label tel_chat_amica_c2_1_6:
            if telefono_minuti_blocco("tel_chat_amica_c2_1_6", "ricevi", 1):
                return
            $ msg("amica", "you ARE. nobody ever sees it. I do")
        "«A look, next time I see you.»":
            label tel_chat_amica_c2_1_7:
            if telefono_minuti_blocco("tel_chat_amica_c2_1_7", "invia", 1):
                return
            $ msg("sara", "A look, next time I see you.")
            $ caldo()
            label tel_chat_amica_c2_1_8:
            if telefono_minuti_blocco("tel_chat_amica_c2_1_8", "ricevi", 1):
                return
            $ msg("amica", "which look. I know all of them. I've got favourites")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_c2_2:
    label tel_chat_amica_c2_2_1:
    if telefono_minuti_blocco("tel_chat_amica_c2_2_1", "ricevi", 1):
        return
    $ msg("amica", "ok. I kept a photo of you from last summer. in the green dress. it's in my purse behind the library card")
    label tel_chat_amica_c2_2_2:
    if telefono_minuti_blocco("tel_chat_amica_c2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«The one that kept slipping off my shoulder?»":
            label tel_chat_amica_c2_2_3:
            if telefono_minuti_blocco("tel_chat_amica_c2_2_3", "invia", 1):
                return
            $ msg("sara", "The one that kept slipping off my shoulder?")
            $ caldo()
            label tel_chat_amica_c2_2_4:
            if telefono_minuti_blocco("tel_chat_amica_c2_2_4", "ricevi", 1):
                return
            $ msg("amica", "I don't know WHICH shoulder. I haven't STUDIED it")
        "«You don't have a library card.»":
            label tel_chat_amica_c2_2_5:
            if telefono_minuti_blocco("tel_chat_amica_c2_2_5", "invia", 1):
                return
            $ msg("sara", "You don't have a library card.")
            label tel_chat_amica_c2_2_6:
            if telefono_minuti_blocco("tel_chat_amica_c2_2_6", "ricevi", 1):
                return
            $ msg("amica", "I got one so it'd have something to be behind")
        "«Why that one?»":
            label tel_chat_amica_c2_2_7:
            if telefono_minuti_blocco("tel_chat_amica_c2_2_7", "invia", 1):
                return
            $ msg("sara", "Why that one?")
            label tel_chat_amica_c2_2_8:
            if telefono_minuti_blocco("tel_chat_amica_c2_2_8", "ricevi", 1):
                return
            $ msg("amica", "you'd forgotten anybody was there. you should see yourself when you've forgotten")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_c2_3:
    label tel_chat_amica_c2_3_1:
    if telefono_minuti_blocco("tel_chat_amica_c2_3_1", "ricevi", 1):
        return
    $ msg("amica", "now you. same size")
    label tel_chat_amica_c2_3_2:
    if telefono_minuti_blocco("tel_chat_amica_c2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Sometimes I get dressed and think, would Joanie wink?»":
            label tel_chat_amica_c2_3_3:
            if telefono_minuti_blocco("tel_chat_amica_c2_3_3", "invia", 1):
                return
            $ msg("sara", "Sometimes I get dressed and think, would Joanie wink?")
            label tel_chat_amica_c2_3_4:
            if telefono_minuti_blocco("tel_chat_amica_c2_3_4", "ricevi", 2):
                return
            $ msg("amica", ".......")
            $ msg("amica", "and do I")
        "«More often than you'd believe.»":
            label tel_chat_amica_c2_3_5:
            if telefono_minuti_blocco("tel_chat_amica_c2_3_5", "invia", 1):
                return
            $ msg("sara", "More often than you'd believe.")
            label tel_chat_amica_c2_3_6:
            if telefono_minuti_blocco("tel_chat_amica_c2_3_6", "ricevi", 1):
                return
            $ msg("amica", "I'm going to lie down on my own floor for a minute")
        "«I can't think of one that good.»":
            label tel_chat_amica_c2_3_7:
            if telefono_minuti_blocco("tel_chat_amica_c2_3_7", "invia", 1):
                return
            $ msg("sara", "I can't think of one that good.")
            label tel_chat_amica_c2_3_8:
            if telefono_minuti_blocco("tel_chat_amica_c2_3_8", "ricevi", 1):
                return
            $ msg("amica", "you will. in the bath. it's where they all live")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Flirt: la paura di perdersi

label chat_amica_c3:
    label tel_chat_amica_c3_1:
    if telefono_minuti_blocco("tel_chat_amica_c3_1", "invia", 1):
        return
    $ msg("sara", "Would anything I did make you stop liking me?")
    return

label chat_amica_c3_entrata:
    label tel_chat_amica_c3_entrata_1:
    if telefono_minuti_blocco("tel_chat_amica_c3_entrata_1", "ricevi", 1):
        return
    $ msg("amica", "random question. do I ever annoy you")
    label tel_chat_amica_c3_entrata_2:
    if telefono_minuti_blocco("tel_chat_amica_c3_entrata_2", "invia", 1):
        return
    $ msg("sara", "Never. Would anything I did make you stop liking me?")
    return

label chat_amica_c3_1:
    label tel_chat_amica_c3_1_1:
    if telefono_minuti_blocco("tel_chat_amica_c3_1_1", "ricevi", 1):
        return
    $ msg("amica", "if you got a fringe like mine. that's copyright")
    label tel_chat_amica_c3_1_2:
    if telefono_minuti_blocco("tel_chat_amica_c3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Seriously.»":
            label tel_chat_amica_c3_1_3:
            if telefono_minuti_blocco("tel_chat_amica_c3_1_3", "invia", 1):
                return
            $ msg("sara", "Seriously.")
            label tel_chat_amica_c3_1_4:
            if telefono_minuti_blocco("tel_chat_amica_c3_1_4", "ricevi", 1):
                return
            $ msg("amica", "seriously. no. I've looked for the edge of it. there isn't one")
        "«Anything?»":
            label tel_chat_amica_c3_1_5:
            if telefono_minuti_blocco("tel_chat_amica_c3_1_5", "invia", 1):
                return
            $ msg("sara", "Anything?")
            $ caldo()
            label tel_chat_amica_c3_1_6:
            if telefono_minuti_blocco("tel_chat_amica_c3_1_6", "ricevi", 1):
                return
            $ msg("amica", "try me. start small. stolen a pen")
        "«What if I turned into someone else?»":
            label tel_chat_amica_c3_1_7:
            if telefono_minuti_blocco("tel_chat_amica_c3_1_7", "invia", 1):
                return
            $ msg("sara", "What if I turned into someone else?")
            label tel_chat_amica_c3_1_8:
            if telefono_minuti_blocco("tel_chat_amica_c3_1_8", "ricevi", 1):
                return
            $ msg("amica", "then I'd want to meet her. I think I've seen her at parties")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_c3_2:
    label tel_chat_amica_c3_2_1:
    if telefono_minuti_blocco("tel_chat_amica_c3_2_1", "ricevi", 1):
        return
    $ msg("amica", "your turn. what would make you stop liking me")
    label tel_chat_amica_c3_2_2:
    if telefono_minuti_blocco("tel_chat_amica_c3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«If you stopped winking at me.»":
            label tel_chat_amica_c3_2_3:
            if telefono_minuti_blocco("tel_chat_amica_c3_2_3", "invia", 1):
                return
            $ msg("sara", "If you stopped winking at me.")
            $ caldo()
            label tel_chat_amica_c3_2_4:
            if telefono_minuti_blocco("tel_chat_amica_c3_2_4", "ricevi", 1):
                return
            $ msg("amica", "my eye would have to fall out")
        "«Nothing so far, and you've tried.»":
            label tel_chat_amica_c3_2_5:
            if telefono_minuti_blocco("tel_chat_amica_c3_2_5", "invia", 1):
                return
            $ msg("sara", "Nothing so far, and you've tried.")
            label tel_chat_amica_c3_2_6:
            if telefono_minuti_blocco("tel_chat_amica_c3_2_6", "ricevi", 1):
                return
            $ msg("amica", "I HAVE tried. I've been magnificent")
        "«If you lied to me.»":
            label tel_chat_amica_c3_2_7:
            if telefono_minuti_blocco("tel_chat_amica_c3_2_7", "invia", 1):
                return
            $ msg("sara", "If you lied to me.")
            label tel_chat_amica_c3_2_8:
            if telefono_minuti_blocco("tel_chat_amica_c3_2_8", "ricevi", 1):
                return
            $ msg("amica", "I leave things out. it's different. leaving out is manners")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_c3_3:
    label tel_chat_amica_c3_3_1:
    if telefono_minuti_blocco("tel_chat_amica_c3_3_1", "ricevi", 1):
        return
    $ msg("amica", "you go quiet sometimes and I think, that's it, I've gone too far")
    label tel_chat_amica_c3_3_2:
    if telefono_minuti_blocco("tel_chat_amica_c3_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I go quiet when I like something too much.»":
            label tel_chat_amica_c3_3_3:
            if telefono_minuti_blocco("tel_chat_amica_c3_3_3", "invia", 1):
                return
            $ msg("sara", "I go quiet when I like something too much.")
            label tel_chat_amica_c3_3_4:
            if telefono_minuti_blocco("tel_chat_amica_c3_3_4", "ricevi", 2):
                return
            $ msg("amica", "oh")
            $ msg("amica", "OH. ok. noted. in ink")
        "«Let's not poke at it, Jo.»":
            label tel_chat_amica_c3_3_5:
            if telefono_minuti_blocco("tel_chat_amica_c3_3_5", "invia", 1):
                return
            $ msg("sara", "Let's not poke at it, Jo.")
            $ frena()
            label tel_chat_amica_c3_3_6:
            if telefono_minuti_blocco("tel_chat_amica_c3_3_6", "ricevi", 1):
                return
            $ msg("amica", "no poking. I'll put it on the high shelf. night")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c3_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_c3_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: oltre l'amicizia

label chat_amica_d1:
    label tel_chat_amica_d1_1:
    if telefono_minuti_blocco("tel_chat_amica_d1_1", "invia", 1):
        return
    $ msg("sara", "I can still taste your lip balm. Is it the cherry one?")
    return

label chat_amica_d1_1:
    label tel_chat_amica_d1_1_1:
    if telefono_minuti_blocco("tel_chat_amica_d1_1_1", "ricevi", 2):
        return
    $ msg("amica", "it's the cherry one")
    $ msg("amica", "I've put some more on. it seemed only right")
    label tel_chat_amica_d1_1_2:
    if telefono_minuti_blocco("tel_chat_amica_d1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Where are you?»":
            label tel_chat_amica_d1_1_3:
            if telefono_minuti_blocco("tel_chat_amica_d1_1_3", "invia", 1):
                return
            $ msg("sara", "Where are you?")
            $ caldo()
            label tel_chat_amica_d1_1_4:
            if telefono_minuti_blocco("tel_chat_amica_d1_1_4", "ricevi", 1):
                return
            $ msg("amica", "in bed. under the rabbit. thinking about your face")
        "«I keep touching my mouth. Like an idiot.»":
            label tel_chat_amica_d1_1_5:
            if telefono_minuti_blocco("tel_chat_amica_d1_1_5", "invia", 1):
                return
            $ msg("sara", "I keep touching my mouth. Like an idiot.")
            label tel_chat_amica_d1_1_6:
            if telefono_minuti_blocco("tel_chat_amica_d1_1_6", "ricevi", 1):
                return
            $ msg("amica", "don't stop on my account")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_d1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_d1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_d1_2:
    label tel_chat_amica_d1_2_1:
    if telefono_minuti_blocco("tel_chat_amica_d1_2_1", "ricevi", 1):
        return
    $ msg("amica", "I've imagined talking to you like this so many times and now I've got no lines. it's humiliating")
    label tel_chat_amica_d1_2_2:
    if telefono_minuti_blocco("tel_chat_amica_d1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You don't need lines. Just tell me what you're looking at.»":
            label tel_chat_amica_d1_2_3:
            if telefono_minuti_blocco("tel_chat_amica_d1_2_3", "invia", 1):
                return
            $ msg("sara", "You don't need lines. Just tell me what you're looking at.")
            $ caldo()
            label tel_chat_amica_d1_2_4:
            if telefono_minuti_blocco("tel_chat_amica_d1_2_4", "ricevi", 1):
                return
            $ msg("amica", "the photo. the shoulder. I've got it propped on the lamp")
        "«Then let me. You're wearing that grey shirt. One button's wrong.»":
            label tel_chat_amica_d1_2_5:
            if telefono_minuti_blocco("tel_chat_amica_d1_2_5", "invia", 1):
                return
            $ msg("sara", "Then let me. You're wearing that grey shirt. One button's wrong.")
            label tel_chat_amica_d1_2_6:
            if telefono_minuti_blocco("tel_chat_amica_d1_2_6", "ricevi", 1):
                return
            $ msg("amica", "how do you DO that")
        "«Slowly, then. We've got all night.»":
            label tel_chat_amica_d1_2_7:
            if telefono_minuti_blocco("tel_chat_amica_d1_2_7", "invia", 1):
                return
            $ msg("sara", "Slowly, then. We've got all night.")
            label tel_chat_amica_d1_2_8:
            if telefono_minuti_blocco("tel_chat_amica_d1_2_8", "ricevi", 1):
                return
            $ msg("amica", "slowly. yes. ok. I'm going to need both hands for the phone and I resent it")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_d1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_d1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_d1_3:
    label tel_chat_amica_d1_3_1:
    if telefono_minuti_blocco("tel_chat_amica_d1_3_1", "ricevi", 1):
        return
    $ msg("amica", "you're laughing aren't you. I can hear it from here")
    label tel_chat_amica_d1_3_2:
    if telefono_minuti_blocco("tel_chat_amica_d1_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm laughing and I'm on fire. Is that allowed?»":
            label tel_chat_amica_d1_3_3:
            if telefono_minuti_blocco("tel_chat_amica_d1_3_3", "invia", 1):
                return
            $ msg("sara", "I'm laughing and I'm on fire. Is that allowed?")
            label tel_chat_amica_d1_3_4:
            if telefono_minuti_blocco("tel_chat_amica_d1_3_4", "ricevi", 1):
                return
            $ msg("amica", "it's my favourite combination in a person")
        "«Come over tomorrow.»":
            label tel_chat_amica_d1_3_5:
            if telefono_minuti_blocco("tel_chat_amica_d1_3_5", "invia", 1):
                return
            $ msg("sara", "Come over tomorrow.")
            label tel_chat_amica_d1_3_6:
            if telefono_minuti_blocco("tel_chat_amica_d1_3_6", "ricevi", 2):
                return
            $ msg("amica", "I was already putting my shoes on")
            $ msg("amica", "goodnight. I mean it. stop smiling. I'm not stopping either")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_d1_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_d1_3_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- Sexting: una vita insieme

label chat_amica_d2:
    label tel_chat_amica_d2_1:
    if telefono_minuti_blocco("tel_chat_amica_d2_1", "invia", 1):
        return
    $ msg("sara", "If you were here, what would we be doing?")
    return

label chat_amica_d2_1:
    label tel_chat_amica_d2_1_1:
    if telefono_minuti_blocco("tel_chat_amica_d2_1_1", "ricevi", 1):
        return
    $ msg("amica", "honest answer or nice answer")
    label tel_chat_amica_d2_1_2:
    if telefono_minuti_blocco("tel_chat_amica_d2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Honest.»":
            label tel_chat_amica_d2_1_3:
            if telefono_minuti_blocco("tel_chat_amica_d2_1_3", "invia", 1):
                return
            $ msg("sara", "Honest.")
            $ caldo()
            label tel_chat_amica_d2_1_4:
            if telefono_minuti_blocco("tel_chat_amica_d2_1_4", "ricevi", 1):
                return
            $ msg("amica", "first I'd look at you for about an hour. you'd get cross. you'd tell me to hurry up")
        "«Nice, then honest.»":
            label tel_chat_amica_d2_1_5:
            if telefono_minuti_blocco("tel_chat_amica_d2_1_5", "invia", 1):
                return
            $ msg("sara", "Nice, then honest.")
            label tel_chat_amica_d2_1_6:
            if telefono_minuti_blocco("tel_chat_amica_d2_1_6", "ricevi", 1):
                return
            $ msg("amica", "nice: toast. honest: not toast")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_d2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_d2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_d2_2:
    label tel_chat_amica_d2_2_1:
    if telefono_minuti_blocco("tel_chat_amica_d2_2_1", "ricevi", 1):
        return
    $ msg("amica", "would you be shy")
    label tel_chat_amica_d2_2_2:
    if telefono_minuti_blocco("tel_chat_amica_d2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«For a minute. You'd wink and I'd forget to be.»":
            label tel_chat_amica_d2_2_3:
            if telefono_minuti_blocco("tel_chat_amica_d2_2_3", "invia", 1):
                return
            $ msg("sara", "For a minute. You'd wink and I'd forget to be.")
            $ caldo()
            label tel_chat_amica_d2_2_4:
            if telefono_minuti_blocco("tel_chat_amica_d2_2_4", "ricevi", 1):
                return
            $ msg("amica", "I'd do it with my whole face. you'd have no chance")
        "«I think you would.»":
            label tel_chat_amica_d2_2_5:
            if telefono_minuti_blocco("tel_chat_amica_d2_2_5", "invia", 1):
                return
            $ msg("sara", "I think you would.")
            label tel_chat_amica_d2_2_6:
            if telefono_minuti_blocco("tel_chat_amica_d2_2_6", "ricevi", 1):
                return
            $ msg("amica", "me. SHY. ......ok yes. for a minute. don't tell anyone")
        "«You'd find out.»":
            label tel_chat_amica_d2_2_7:
            if telefono_minuti_blocco("tel_chat_amica_d2_2_7", "invia", 1):
                return
            $ msg("sara", "You'd find out.")
            label tel_chat_amica_d2_2_8:
            if telefono_minuti_blocco("tel_chat_amica_d2_2_8", "ricevi", 1):
                return
            $ msg("amica", "that's a terrible thing to say to somebody who has to get up at seven")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_d2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_d2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amica_d2_3:
    label tel_chat_amica_d2_3_1:
    if telefono_minuti_blocco("tel_chat_amica_d2_3_1", "ricevi", 1):
        return
    $ msg("amica", "and after")
    label tel_chat_amica_d2_3_2:
    if telefono_minuti_blocco("tel_chat_amica_d2_3_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«After, you'd steal all the covers.»":
            label tel_chat_amica_d2_3_3:
            if telefono_minuti_blocco("tel_chat_amica_d2_3_3", "invia", 1):
                return
            $ msg("sara", "After, you'd steal all the covers.")
            label tel_chat_amica_d2_3_4:
            if telefono_minuti_blocco("tel_chat_amica_d2_3_4", "ricevi", 1):
                return
            $ msg("amica", "and you'd let me. and we'd eat the toast after all. in bed. crumbs everywhere")
        "«After, I'd want you to stay.»":
            label tel_chat_amica_d2_3_5:
            if telefono_minuti_blocco("tel_chat_amica_d2_3_5", "invia", 1):
                return
            $ msg("sara", "After, I'd want you to stay.")
            label tel_chat_amica_d2_3_6:
            if telefono_minuti_blocco("tel_chat_amica_d2_3_6", "ricevi", 2):
                return
            $ msg("amica", "say that one again tomorrow when it's light. I want to see if it still works")
            $ msg("amica", "goodnight you. one eye open. the other one's dreaming")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_d2_3_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amica_d2_3_2"
            $ telefono_minuti_chiudi = True
            return
    return
