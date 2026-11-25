## =============================================================================
## SIMON — discorsi al telefono: introduzione, A (conoscenti), B (confidenza)
## =============================================================================
## Tono (Q&A 18/11/2026): cordiale e professionale, con un filo di attenzione.
## In B complimenti SOLO sui progressi: il personale resta fuori, il flirt è da C.
## Modello: docs/argomenti-telefono.md e game/percorsi/leggimi_percorsi.rpy.

init python:
    discorso("simon_intro", "simon", ESTRANEI)
    discorso("simon_a1", "simon", CONOSCENTI, se="(giorno == 14 and fatto('ep1_d13_palestra')) or (giorno >= 16 and fatto('ep2_ultimo_allenamento_simon') == giorno - 1)", argomento="The last workout", scade="aperta_da >= 1")
    discorso("simon_a2", "simon", CONOSCENTI)
    discorso("simon_a3", "simon", CONOSCENTI)
    discorso("simon_a4", "simon", CONOSCENTI)
    discorso("simon_a5", "simon", CONOSCENTI)
    discorso("simon_a6", "simon", CONOSCENTI)
    discorso("simon_a7", "simon", CONOSCENTI)
    discorso("simon_a8", "simon", CONOSCENTI)
    discorso("simon_b1", "simon", CONFIDENZA)
    discorso("simon_b2", "simon", CONFIDENZA)
    discorso("simon_b3", "simon", CONFIDENZA)
    discorso("simon_b4", "simon", CONFIDENZA)
    discorso("simon_b5", "simon", CONFIDENZA)


## --- Introduzione: consigli per il prossimo allenamento ----------------------

label chat_simon_intro:
    label tel_chat_simon_intro_1:
    if telefono_minuti_blocco("tel_chat_simon_intro_1", "invia", 1):
        return
    $ msg("sara", "Hi, it's Sara. From the gym. You said I could text you about the exercises... is that still ok?")
    return

label chat_simon_intro_1:
    label tel_chat_simon_intro_1_1:
    if telefono_minuti_blocco("tel_chat_simon_intro_1_1", "ricevi", 2):
        return
    $ msg("simon", "Of course! Joanie's friend. The shoulder, right?")
    $ msg("simon", "How's it feeling?")
    label tel_chat_simon_intro_1_2:
    if telefono_minuti_blocco("tel_chat_simon_intro_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Much better. You fixed it.»":
            label tel_chat_simon_intro_1_3:
            if telefono_minuti_blocco("tel_chat_simon_intro_1_3", "invia", 1):
                return
            $ msg("sara", "Much better. You fixed it.")
            $ caldo()
            label tel_chat_simon_intro_1_4:
            if telefono_minuti_blocco("tel_chat_simon_intro_1_4", "ricevi", 1):
                return
            $ msg("simon", "You fixed it. I just pointed.")
        "«Still a bit stiff.»":
            label tel_chat_simon_intro_1_5:
            if telefono_minuti_blocco("tel_chat_simon_intro_1_5", "invia", 1):
                return
            $ msg("sara", "Still a bit stiff.")
            label tel_chat_simon_intro_1_6:
            if telefono_minuti_blocco("tel_chat_simon_intro_1_6", "ricevi", 1):
                return
            $ msg("simon", "Normal. It'll loosen up if you keep moving it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_intro_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_intro_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_intro_2:
    label tel_chat_simon_intro_2_1:
    if telefono_minuti_blocco("tel_chat_simon_intro_2_1", "ricevi", 2):
        return
    $ msg("simon", "Next session: ten minutes on the bike to warm up, then back and shoulders. Light.")
    $ msg("simon", "And bring water. Real water, not those neon drinks.")
    sp "Neon drinks. Joanie's bottle is literally blue."
    label tel_chat_simon_intro_2_2:
    if telefono_minuti_blocco("tel_chat_simon_intro_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Noted.»":
            label tel_chat_simon_intro_2_3:
            if telefono_minuti_blocco("tel_chat_simon_intro_2_3", "invia", 1):
                return
            $ msg("sara", "Noted.")
            label tel_chat_simon_intro_2_4:
            if telefono_minuti_blocco("tel_chat_simon_intro_2_4", "ricevi", 1):
                return
            $ msg("simon", "See you there.")
        "«Yes, sir :)»":
            label tel_chat_simon_intro_2_5:
            if telefono_minuti_blocco("tel_chat_simon_intro_2_5", "invia", 1):
                return
            $ msg("sara", "Yes, sir :)")
            $ caldo()
            label tel_chat_simon_intro_2_6:
            if telefono_minuti_blocco("tel_chat_simon_intro_2_6", "ricevi", 1):
                return
            $ msg("simon", "Ha. Simon is fine.")
        "«Do you give homework to all your clients?»" (confidence=25):
            label tel_chat_simon_intro_2_7:
            if telefono_minuti_blocco("tel_chat_simon_intro_2_7", "invia", 1):
                return
            $ msg("sara", "Do you give homework to all your clients?")
            $ caldo()
            label tel_chat_simon_intro_2_8:
            if telefono_minuti_blocco("tel_chat_simon_intro_2_8", "ricevi", 1):
                return
            $ msg("simon", "Only the ones who actually do it.")
            sp "Is that a compliment or a challenge?"
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_intro_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_intro_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A1: dolori muscolari (bozza approvata da Jody) --------------------------

label chat_simon_a1:
    label tel_chat_simon_a1_1:
    if telefono_minuti_blocco("tel_chat_simon_a1_1", "invia", 1):
        return
    $ msg("sara", "Hi Simon, it's Sara. Quick question... is it normal that I can't walk down the stairs today? :)")
    return

label chat_simon_a1_entrata:
    label tel_chat_simon_a1_entrata_1:
    if telefono_minuti_blocco("tel_chat_simon_a1_entrata_1", "ricevi", 1):
        return
    $ msg("simon", "Day after leg day. How are the stairs treating you? ;)")
    label tel_chat_simon_a1_entrata_2:
    if telefono_minuti_blocco("tel_chat_simon_a1_entrata_2", "invia", 1):
        return
    $ msg("sara", "Is it normal that I can't walk down them? :)")
    return

label chat_simon_a1_1:
    label tel_chat_simon_a1_1_1:
    if telefono_minuti_blocco("tel_chat_simon_a1_1_1", "ricevi", 2):
        return
    $ msg("simon", "Haha, totally normal. It's called DOMS.")
    $ msg("simon", "Delayed onset muscle soreness. Basically your legs are filing a complaint.")
    sp "He even makes pain sound fun."
    label tel_chat_simon_a1_1_2:
    if telefono_minuti_blocco("tel_chat_simon_a1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«So what do I do? Stay on the sofa all day?»":
            label tel_chat_simon_a1_1_3:
            if telefono_minuti_blocco("tel_chat_simon_a1_1_3", "invia", 1):
                return
            $ msg("sara", "So what do I do? Stay on the sofa all day?")
            label tel_chat_simon_a1_1_4:
            if telefono_minuti_blocco("tel_chat_simon_a1_1_4", "ricevi", 1):
                return
            $ msg("simon", "Nope. The sofa is the enemy.")
        "«Tell my legs it was your idea, not mine.»":
            label tel_chat_simon_a1_1_5:
            if telefono_minuti_blocco("tel_chat_simon_a1_1_5", "invia", 1):
                return
            $ msg("sara", "Tell my legs it was your idea, not mine.")
            $ caldo()
            label tel_chat_simon_a1_1_6:
            if telefono_minuti_blocco("tel_chat_simon_a1_1_6", "ricevi", 1):
                return
            $ msg("simon", "Already did. They said you're tougher than you look.")
        "«Next time go easier on me, coach.»" (confidence=25):
            label tel_chat_simon_a1_1_7:
            if telefono_minuti_blocco("tel_chat_simon_a1_1_7", "invia", 1):
                return
            $ msg("sara", "Next time go easier on me, coach.")
            $ caldo()
            label tel_chat_simon_a1_1_8:
            if telefono_minuti_blocco("tel_chat_simon_a1_1_8", "ricevi", 2):
                return
            $ msg("simon", "Easier? You were the one who asked for one more set.")
            $ msg("simon", "Coach. I like that.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_a1_2:
    label tel_chat_simon_a1_2_1:
    if telefono_minuti_blocco("tel_chat_simon_a1_2_1", "ricevi", 2):
        return
    $ msg("simon", "Light walk, lots of water, ten minutes of stretching before bed.")
    $ msg("simon", "And a hot shower. Not a cold one, whatever Joanie tells you.")
    sp "How does he know Joanie told me to take a cold shower?"
    label tel_chat_simon_a1_2_2:
    if telefono_minuti_blocco("tel_chat_simon_a1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Joanie says a lot of things.»":
            label tel_chat_simon_a1_2_3:
            if telefono_minuti_blocco("tel_chat_simon_a1_2_3", "invia", 1):
                return
            $ msg("sara", "Joanie says a lot of things.")
            label tel_chat_simon_a1_2_4:
            if telefono_minuti_blocco("tel_chat_simon_a1_2_4", "ricevi", 1):
                return
            $ msg("simon", "She does. Don't listen to half of them.")
        "«Can you send me the stretches?»":
            label tel_chat_simon_a1_2_5:
            if telefono_minuti_blocco("tel_chat_simon_a1_2_5", "invia", 1):
                return
            $ msg("sara", "Can you send me the stretches?")
            $ segna("simon_stretching")
        "«Or I could just skip leg day forever.»":
            label tel_chat_simon_a1_2_6:
            if telefono_minuti_blocco("tel_chat_simon_a1_2_6", "invia", 1):
                return
            $ msg("sara", "Or I could just skip leg day forever.")
            label tel_chat_simon_a1_2_7:
            if telefono_minuti_blocco("tel_chat_simon_a1_2_7", "ricevi", 1):
                return
            $ msg("simon", "Not on my watch.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_a1_3:
    if fatto("simon_stretching"):
        label tel_chat_simon_a1_3_1:
        if telefono_minuti_blocco("tel_chat_simon_a1_3_1", "ricevi", 4):
            return
        $ msg("simon", "1. Quads against the wall, 30 seconds each leg.")
        $ msg("simon", "2. Sit down, legs straight, reach for your toes. Don't bounce.")
        $ msg("simon", "3. Child's pose. Just breathe.")
        $ msg("simon", "Do them tonight. I'll ask you next time.")
    else:
        label tel_chat_simon_a1_3_2:
        if telefono_minuti_blocco("tel_chat_simon_a1_3_2", "ricevi", 1):
            return
        $ msg("simon", "Do the stretches anyway. I'll ask you next time.")
    label tel_chat_simon_a1_3_3:
    if telefono_minuti_blocco("tel_chat_simon_a1_3_3", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Promise.»":
            label tel_chat_simon_a1_3_4:
            if telefono_minuti_blocco("tel_chat_simon_a1_3_4", "invia", 1):
                return
            $ msg("sara", "Promise.")
            label tel_chat_simon_a1_3_5:
            if telefono_minuti_blocco("tel_chat_simon_a1_3_5", "ricevi", 1):
                return
            $ msg("simon", "That's the spirit.")
        "«Yes, coach :)»":
            label tel_chat_simon_a1_3_6:
            if telefono_minuti_blocco("tel_chat_simon_a1_3_6", "invia", 1):
                return
            $ msg("sara", "Yes, coach :)")
            $ caldo()
            label tel_chat_simon_a1_3_7:
            if telefono_minuti_blocco("tel_chat_simon_a1_3_7", "ricevi", 1):
                return
            $ msg("simon", "Good. Now go drink some water.")
        "«We'll see ;)»" (confidence=25):
            label tel_chat_simon_a1_3_8:
            if telefono_minuti_blocco("tel_chat_simon_a1_3_8", "invia", 1):
                return
            $ msg("sara", "We'll see ;)")
            $ caldo()
            label tel_chat_simon_a1_3_9:
            if telefono_minuti_blocco("tel_chat_simon_a1_3_9", "ricevi", 1):
                return
            $ msg("simon", "I'll know if you didn't. I always know.")
            sp "Does he say that to all his clients?"
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a1_3_3"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a1_3_3"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A2: alimentazione -------------------------------------------------------

label chat_simon_a2:
    label tel_chat_simon_a2_1:
    if telefono_minuti_blocco("tel_chat_simon_a2_1", "invia", 1):
        return
    $ msg("sara", "Ok, nutrition question. What am I supposed to eat before training? I always feel dizzy.")
    return

label chat_simon_a2_entrata:
    label tel_chat_simon_a2_entrata_1:
    if telefono_minuti_blocco("tel_chat_simon_a2_entrata_1", "ricevi", 1):
        return
    $ msg("simon", "Random check: what do you normally eat before a session? It makes a difference.")
    label tel_chat_simon_a2_entrata_2:
    if telefono_minuti_blocco("tel_chat_simon_a2_entrata_2", "invia", 1):
        return
    $ msg("sara", "Coffee. And half a cookie. Is that bad?")
    return

label chat_simon_a2_1:
    label tel_chat_simon_a2_1_1:
    if telefono_minuti_blocco("tel_chat_simon_a2_1_1", "ricevi", 2):
        return
    $ msg("simon", "That's why. You're training on empty.")
    $ msg("simon", "An hour before: a banana, some yogurt, a slice of toast. Nothing heavy.")
    label tel_chat_simon_a2_1_2:
    if telefono_minuti_blocco("tel_chat_simon_a2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Does chocolate count as fuel?»":
            label tel_chat_simon_a2_1_3:
            if telefono_minuti_blocco("tel_chat_simon_a2_1_3", "invia", 1):
                return
            $ msg("sara", "Does chocolate count as fuel?")
            $ caldo()
            label tel_chat_simon_a2_1_4:
            if telefono_minuti_blocco("tel_chat_simon_a2_1_4", "ricevi", 1):
                return
            $ msg("simon", "Dark chocolate, two squares. After. As a reward.")
        "«A banana I can do.»":
            label tel_chat_simon_a2_1_5:
            if telefono_minuti_blocco("tel_chat_simon_a2_1_5", "invia", 1):
                return
            $ msg("sara", "A banana I can do.")
            label tel_chat_simon_a2_1_6:
            if telefono_minuti_blocco("tel_chat_simon_a2_1_6", "ricevi", 1):
                return
            $ msg("simon", "Good. Small changes, big difference.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_a2_2:
    label tel_chat_simon_a2_2_1:
    if telefono_minuti_blocco("tel_chat_simon_a2_2_1", "ricevi", 2):
        return
    $ msg("simon", "And breakfast. Real breakfast. Oats, eggs, fruit.")
    $ msg("simon", "I'll send you what I eat. Copy it for a week and tell me how you feel.")
    $ segna("simon_colazione")
    sp "His breakfast has more protein than my entire week."
    label tel_chat_simon_a2_2_2:
    if telefono_minuti_blocco("tel_chat_simon_a2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Deal. One week.»":
            label tel_chat_simon_a2_2_3:
            if telefono_minuti_blocco("tel_chat_simon_a2_2_3", "invia", 1):
                return
            $ msg("sara", "Deal. One week.")
            label tel_chat_simon_a2_2_4:
            if telefono_minuti_blocco("tel_chat_simon_a2_2_4", "ricevi", 1):
                return
            $ msg("simon", "I'll hold you to it.")
        "«Do you ever eat pizza? Be honest.»":
            label tel_chat_simon_a2_2_5:
            if telefono_minuti_blocco("tel_chat_simon_a2_2_5", "invia", 1):
                return
            $ msg("sara", "Do you ever eat pizza? Be honest.")
            $ caldo()
            label tel_chat_simon_a2_2_6:
            if telefono_minuti_blocco("tel_chat_simon_a2_2_6", "ricevi", 1):
                return
            $ msg("simon", "Every Saturday. Don't tell my clients.")
            label tel_chat_simon_a2_2_7:
            if telefono_minuti_blocco("tel_chat_simon_a2_2_7", "invia", 1):
                return
            $ msg("sara", "Your secret is safe.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A3: musica in palestra --------------------------------------------------

label chat_simon_a3:
    label tel_chat_simon_a3_1:
    if telefono_minuti_blocco("tel_chat_simon_a3_1", "invia", 1):
        return
    $ msg("sara", "Can I file a complaint about the gym music? Same five songs every day.")
    return

label chat_simon_a3_1:
    label tel_chat_simon_a3_1_1:
    if telefono_minuti_blocco("tel_chat_simon_a3_1_1", "ricevi", 2):
        return
    $ msg("simon", "Haha. That's the owner's playlist. I've been fighting it for two years.")
    $ msg("simon", "What do you listen to when you train?")
    label tel_chat_simon_a3_1_2:
    if telefono_minuti_blocco("tel_chat_simon_a3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Old pop. Don't judge me.»":
            label tel_chat_simon_a3_1_3:
            if telefono_minuti_blocco("tel_chat_simon_a3_1_3", "invia", 1):
                return
            $ msg("sara", "Old pop. Don't judge me.")
            label tel_chat_simon_a3_1_4:
            if telefono_minuti_blocco("tel_chat_simon_a3_1_4", "ricevi", 1):
                return
            $ msg("simon", "No judging. Whatever makes you move.")
        "«Nothing. I'm too busy trying not to die.»":
            label tel_chat_simon_a3_1_5:
            if telefono_minuti_blocco("tel_chat_simon_a3_1_5", "invia", 1):
                return
            $ msg("sara", "Nothing. I'm too busy trying not to die.")
            $ caldo()
            label tel_chat_simon_a3_1_6:
            if telefono_minuti_blocco("tel_chat_simon_a3_1_6", "ricevi", 1):
                return
            $ msg("simon", "Ha! That's a playlist too.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_a3_2:
    label tel_chat_simon_a3_2_1:
    if telefono_minuti_blocco("tel_chat_simon_a3_2_1", "ricevi", 2):
        return
    $ msg("simon", "Try this. Fast enough for cardio, not so loud it kills you.")
    $ msg("simon", "(A link to a playlist: «Simon — Leg Day»)")
    $ segna("simon_playlist")
    sp "A playlist called Leg Day. Of course."
    label tel_chat_simon_a3_2_2:
    if telefono_minuti_blocco("tel_chat_simon_a3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'll try it tomorrow.»":
            label tel_chat_simon_a3_2_3:
            if telefono_minuti_blocco("tel_chat_simon_a3_2_3", "invia", 1):
                return
            $ msg("sara", "I'll try it tomorrow.")
            label tel_chat_simon_a3_2_4:
            if telefono_minuti_blocco("tel_chat_simon_a3_2_4", "ricevi", 1):
                return
            $ msg("simon", "Tell me if it works.")
        "«If I survive leg day, it's thanks to this.»":
            label tel_chat_simon_a3_2_5:
            if telefono_minuti_blocco("tel_chat_simon_a3_2_5", "invia", 1):
                return
            $ msg("sara", "If I survive leg day, it's thanks to this.")
            $ caldo()
            label tel_chat_simon_a3_2_6:
            if telefono_minuti_blocco("tel_chat_simon_a3_2_6", "ricevi", 1):
                return
            $ msg("simon", "You'll survive. You always do.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A4: esercizi preferiti --------------------------------------------------

label chat_simon_a4:
    label tel_chat_simon_a4_1:
    if telefono_minuti_blocco("tel_chat_simon_a4_1", "invia", 1):
        return
    $ msg("sara", "Honest question: is there anyone in the world who actually likes burpees?")
    return

label chat_simon_a4_1:
    label tel_chat_simon_a4_1_1:
    if telefono_minuti_blocco("tel_chat_simon_a4_1_1", "ricevi", 2):
        return
    $ msg("simon", "Me.")
    $ msg("simon", "But I also like deadlifts, so I'm not a reliable witness.")
    label tel_chat_simon_a4_1_2:
    if telefono_minuti_blocco("tel_chat_simon_a4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What's your favourite one?»":
            label tel_chat_simon_a4_1_3:
            if telefono_minuti_blocco("tel_chat_simon_a4_1_3", "invia", 1):
                return
            $ msg("sara", "What's your favourite one?")
            label tel_chat_simon_a4_1_4:
            if telefono_minuti_blocco("tel_chat_simon_a4_1_4", "ricevi", 1):
                return
            $ msg("simon", "Deadlift. Pick something heavy off the floor. Simple. Honest.")
        "«You're a monster.»":
            label tel_chat_simon_a4_1_5:
            if telefono_minuti_blocco("tel_chat_simon_a4_1_5", "invia", 1):
                return
            $ msg("sara", "You're a monster.")
            $ caldo()
            label tel_chat_simon_a4_1_6:
            if telefono_minuti_blocco("tel_chat_simon_a4_1_6", "ricevi", 1):
                return
            $ msg("simon", "A friendly monster.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_a4_2:
    label tel_chat_simon_a4_2_1:
    if telefono_minuti_blocco("tel_chat_simon_a4_2_1", "ricevi", 1):
        return
    $ msg("simon", "What's yours? And «none» is not an answer.")
    label tel_chat_simon_a4_2_2:
    if telefono_minuti_blocco("tel_chat_simon_a4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«The bike. Because I can sit.»":
            label tel_chat_simon_a4_2_3:
            if telefono_minuti_blocco("tel_chat_simon_a4_2_3", "invia", 1):
                return
            $ msg("sara", "The bike. Because I can sit.")
            label tel_chat_simon_a4_2_4:
            if telefono_minuti_blocco("tel_chat_simon_a4_2_4", "ricevi", 1):
                return
            $ msg("simon", "Fair. We'll work on that.")
        "«Squats. They're starting to feel good.»":
            label tel_chat_simon_a4_2_5:
            if telefono_minuti_blocco("tel_chat_simon_a4_2_5", "invia", 1):
                return
            $ msg("sara", "Squats. They're starting to feel good.")
            $ caldo()
            label tel_chat_simon_a4_2_6:
            if telefono_minuti_blocco("tel_chat_simon_a4_2_6", "ricevi", 1):
                return
            $ msg("simon", "Squats are the queen of exercises. Good taste.")
            $ segna("simon_squat")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A5: il weekend ----------------------------------------------------------

label chat_simon_a5:
    label tel_chat_simon_a5_1:
    if telefono_minuti_blocco("tel_chat_simon_a5_1", "invia", 1):
        return
    $ msg("sara", "Do personal trainers rest on weekends or do you live at the gym?")
    return

label chat_simon_a5_1:
    label tel_chat_simon_a5_1_1:
    if telefono_minuti_blocco("tel_chat_simon_a5_1_1", "ricevi", 3):
        return
    $ msg("simon", "Saturday mornings I hike with some friends. Saturday nights, out.")
    $ msg("simon", "Sunday I do absolutely nothing. It's sacred.")
    $ msg("simon", "You?")
    label tel_chat_simon_a5_1_2:
    if telefono_minuti_blocco("tel_chat_simon_a5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«[nome_compagno] and I usually stay in. Movies, takeaway.»":
            label tel_chat_simon_a5_1_3:
            if telefono_minuti_blocco("tel_chat_simon_a5_1_3", "invia", 1):
                return
            $ msg("sara", "[nome_compagno] and I usually stay in. Movies, takeaway.")
            label tel_chat_simon_a5_1_4:
            if telefono_minuti_blocco("tel_chat_simon_a5_1_4", "ricevi", 1):
                return
            $ msg("simon", "Sounds nice. Calm.")
        "«Nothing exciting. Laundry, mostly.»":
            label tel_chat_simon_a5_1_5:
            if telefono_minuti_blocco("tel_chat_simon_a5_1_5", "invia", 1):
                return
            $ msg("sara", "Nothing exciting. Laundry, mostly.")
            label tel_chat_simon_a5_1_6:
            if telefono_minuti_blocco("tel_chat_simon_a5_1_6", "ricevi", 1):
                return
            $ msg("simon", "Laundry. Wild.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_a5_2:
    label tel_chat_simon_a5_2_1:
    if telefono_minuti_blocco("tel_chat_simon_a5_2_1", "ricevi", 1):
        return
    $ msg("simon", "If you ever want to try a hike, the trail by the lake is easy. Great view.")
    sp "He didn't say «with me». He just said «try a hike»."
    label tel_chat_simon_a5_2_2:
    if telefono_minuti_blocco("tel_chat_simon_a5_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Maybe with Joanie, one day.»":
            label tel_chat_simon_a5_2_3:
            if telefono_minuti_blocco("tel_chat_simon_a5_2_3", "invia", 1):
                return
            $ msg("sara", "Maybe with Joanie, one day.")
            label tel_chat_simon_a5_2_4:
            if telefono_minuti_blocco("tel_chat_simon_a5_2_4", "ricevi", 1):
                return
            $ msg("simon", "Good idea.")
        "«Send me the name of the trail.»":
            label tel_chat_simon_a5_2_5:
            if telefono_minuti_blocco("tel_chat_simon_a5_2_5", "invia", 1):
                return
            $ msg("sara", "Send me the name of the trail.")
            $ caldo()
            label tel_chat_simon_a5_2_6:
            if telefono_minuti_blocco("tel_chat_simon_a5_2_6", "ricevi", 1):
                return
            $ msg("simon", "Pine Ridge. Start early, it gets crowded.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a5_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a5_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A6: locali notturni -----------------------------------------------------

label chat_simon_a6:
    label tel_chat_simon_a6_1:
    if telefono_minuti_blocco("tel_chat_simon_a6_1", "invia", 1):
        return
    $ msg("sara", "Joanie says you know every bar in town. If we go out one weekend, where should we start?")
    return

label chat_simon_a6_1:
    label tel_chat_simon_a6_1_1:
    if telefono_minuti_blocco("tel_chat_simon_a6_1_1", "ricevi", 2):
        return
    $ msg("simon", "Every bar is an exaggeration. Most of them.")
    $ msg("simon", "What kind of night? Dancing, drinks, or talking without shouting?")
    label tel_chat_simon_a6_1_2:
    if telefono_minuti_blocco("tel_chat_simon_a6_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Talking without shouting. I'm old.»":
            label tel_chat_simon_a6_1_3:
            if telefono_minuti_blocco("tel_chat_simon_a6_1_3", "invia", 1):
                return
            $ msg("sara", "Talking without shouting. I'm old.")
            label tel_chat_simon_a6_1_4:
            if telefono_minuti_blocco("tel_chat_simon_a6_1_4", "ricevi", 1):
                return
            $ msg("simon", "You're not old. Try The Lantern, on the river. Quiet, good cocktails.")
        "«Joanie will say dancing. She always does.»":
            label tel_chat_simon_a6_1_5:
            if telefono_minuti_blocco("tel_chat_simon_a6_1_5", "invia", 1):
                return
            $ msg("sara", "Joanie will say dancing. She always does.")
            $ caldo()
            label tel_chat_simon_a6_1_6:
            if telefono_minuti_blocco("tel_chat_simon_a6_1_6", "ricevi", 1):
                return
            $ msg("simon", "Then Velvet. But wear comfortable shoes, the floor is murder.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a6_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a6_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_a6_2:
    label tel_chat_simon_a6_2_1:
    if telefono_minuti_blocco("tel_chat_simon_a6_2_1", "ricevi", 1):
        return
    $ msg("simon", "If you go, say hi. I'm usually around with my friends.")
    sp "He'd be there. Of course he would."
    label tel_chat_simon_a6_2_2:
    if telefono_minuti_blocco("tel_chat_simon_a6_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«We'll see what Joanie decides.»":
            label tel_chat_simon_a6_2_3:
            if telefono_minuti_blocco("tel_chat_simon_a6_2_3", "invia", 1):
                return
            $ msg("sara", "We'll see what Joanie decides.")
            label tel_chat_simon_a6_2_4:
            if telefono_minuti_blocco("tel_chat_simon_a6_2_4", "ricevi", 1):
                return
            $ msg("simon", "She always decides.")
        "«Then I'll know at least one face.»":
            label tel_chat_simon_a6_2_5:
            if telefono_minuti_blocco("tel_chat_simon_a6_2_5", "invia", 1):
                return
            $ msg("sara", "Then I'll know at least one face.")
            $ caldo()
            label tel_chat_simon_a6_2_6:
            if telefono_minuti_blocco("tel_chat_simon_a6_2_6", "ricevi", 1):
                return
            $ msg("simon", "A friendly one :)")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a6_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a6_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A7: abbigliamento sportivo ----------------------------------------------

label chat_simon_a7:
    label tel_chat_simon_a7_1:
    if telefono_minuti_blocco("tel_chat_simon_a7_1", "invia", 1):
        return
    $ msg("sara", "My running shoes are older than my relationship. Should I buy new ones?")
    return

label chat_simon_a7_1:
    label tel_chat_simon_a7_1_1:
    if telefono_minuti_blocco("tel_chat_simon_a7_1_1", "ricevi", 2):
        return
    $ msg("simon", "If they're older than your relationship, yes. Definitely.")
    $ msg("simon", "Go to a proper shop. Ask them to look at how you walk.")
    label tel_chat_simon_a7_1_2:
    if telefono_minuti_blocco("tel_chat_simon_a7_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And clothes? I train in an old T-shirt.»":
            label tel_chat_simon_a7_1_3:
            if telefono_minuti_blocco("tel_chat_simon_a7_1_3", "invia", 1):
                return
            $ msg("sara", "And clothes? I train in an old T-shirt.")
            label tel_chat_simon_a7_1_4:
            if telefono_minuti_blocco("tel_chat_simon_a7_1_4", "ricevi", 1):
                return
            $ msg("simon", "Whatever you're comfortable in. Comfortable means you move better.")
        "«Do you get a commission from the shoe shop?»":
            label tel_chat_simon_a7_1_5:
            if telefono_minuti_blocco("tel_chat_simon_a7_1_5", "invia", 1):
                return
            $ msg("sara", "Do you get a commission from the shoe shop?")
            $ caldo()
            label tel_chat_simon_a7_1_6:
            if telefono_minuti_blocco("tel_chat_simon_a7_1_6", "ricevi", 1):
                return
            $ msg("simon", "I wish. I'd be rich. Everyone has bad shoes.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a7_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a7_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_a7_2:
    label tel_chat_simon_a7_2_1:
    if telefono_minuti_blocco("tel_chat_simon_a7_2_1", "ricevi", 2):
        return
    $ msg("simon", "Honestly, the shoes matter. The rest is up to you.")
    $ msg("simon", "Some people train better when they feel good in what they wear. That's all.")
    sp "Joanie would say that's a hint about the tight top. Simon probably just means... shoes."
    label tel_chat_simon_a7_2_2:
    if telefono_minuti_blocco("tel_chat_simon_a7_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Shoes first. Then we'll see.»":
            label tel_chat_simon_a7_2_3:
            if telefono_minuti_blocco("tel_chat_simon_a7_2_3", "invia", 1):
                return
            $ msg("sara", "Shoes first. Then we'll see.")
            label tel_chat_simon_a7_2_4:
            if telefono_minuti_blocco("tel_chat_simon_a7_2_4", "ricevi", 1):
                return
            $ msg("simon", "Good plan.")
        "«Joanie wants me to buy matching sets. Like hers.»":
            label tel_chat_simon_a7_2_5:
            if telefono_minuti_blocco("tel_chat_simon_a7_2_5", "invia", 1):
                return
            $ msg("sara", "Joanie wants me to buy matching sets. Like hers.")
            $ caldo()
            label tel_chat_simon_a7_2_6:
            if telefono_minuti_blocco("tel_chat_simon_a7_2_6", "ricevi", 1):
                return
            $ msg("simon", "Joanie's sets are a whole event. You don't need an event. You need to train.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a7_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a7_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A8: obiettivi fisici ----------------------------------------------------

label chat_simon_a8:
    label tel_chat_simon_a8_1:
    if telefono_minuti_blocco("tel_chat_simon_a8_1", "invia", 1):
        return
    $ msg("sara", "Can I ask you something? What should my goal be? I don't even know why I'm training.")
    return

label chat_simon_a8_1:
    label tel_chat_simon_a8_1_1:
    if telefono_minuti_blocco("tel_chat_simon_a8_1_1", "ricevi", 2):
        return
    $ msg("simon", "Good question. Most people never ask it.")
    $ msg("simon", "What do you want to feel? Not look. Feel.")
    label tel_chat_simon_a8_1_2:
    if telefono_minuti_blocco("tel_chat_simon_a8_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Stronger. I want to carry the shopping without dying.»":
            label tel_chat_simon_a8_1_3:
            if telefono_minuti_blocco("tel_chat_simon_a8_1_3", "invia", 1):
                return
            $ msg("sara", "Stronger. I want to carry the shopping without dying.")
            label tel_chat_simon_a8_1_4:
            if telefono_minuti_blocco("tel_chat_simon_a8_1_4", "ricevi", 1):
                return
            $ msg("simon", "That's a real goal. I like real goals.")
        "«More sure of myself.»":
            label tel_chat_simon_a8_1_5:
            if telefono_minuti_blocco("tel_chat_simon_a8_1_5", "invia", 1):
                return
            $ msg("sara", "More sure of myself.")
            $ caldo()
            label tel_chat_simon_a8_1_6:
            if telefono_minuti_blocco("tel_chat_simon_a8_1_6", "ricevi", 1):
                return
            $ msg("simon", "That's the best one. And training is a good way to get there.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a8_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a8_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_a8_2:
    label tel_chat_simon_a8_2_1:
    if telefono_minuti_blocco("tel_chat_simon_a8_2_1", "ricevi", 2):
        return
    $ msg("simon", "So here's yours: ten proper push-ups by the end of the month.")
    $ msg("simon", "Not on your knees. Proper ones.")
    $ segna("simon_obiettivo_pushup")
    sp "Ten. I can barely do two."
    label tel_chat_simon_a8_2_2:
    if telefono_minuti_blocco("tel_chat_simon_a8_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Ten? Are you serious?»":
            label tel_chat_simon_a8_2_3:
            if telefono_minuti_blocco("tel_chat_simon_a8_2_3", "invia", 1):
                return
            $ msg("sara", "Ten? Are you serious?")
            label tel_chat_simon_a8_2_4:
            if telefono_minuti_blocco("tel_chat_simon_a8_2_4", "ricevi", 1):
                return
            $ msg("simon", "Completely. You'll get there.")
        "«Deal. And if I make it?»" (confidence=25):
            label tel_chat_simon_a8_2_5:
            if telefono_minuti_blocco("tel_chat_simon_a8_2_5", "invia", 1):
                return
            $ msg("sara", "Deal. And if I make it?")
            $ caldo()
            label tel_chat_simon_a8_2_6:
            if telefono_minuti_blocco("tel_chat_simon_a8_2_6", "ricevi", 1):
                return
            $ msg("simon", "Then you set the next goal. Not me.")
            sp "I like that more than I should."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a8_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_a8_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B1: insicurezze sul corpo -----------------------------------------------

label chat_simon_b1:
    label tel_chat_simon_b1_1:
    if telefono_minuti_blocco("tel_chat_simon_b1_1", "invia", 1):
        return
    $ msg("sara", "Can I tell you something stupid? I hate the mirrors at the gym.")
    return

label chat_simon_b1_entrata:
    label tel_chat_simon_b1_entrata_1:
    if telefono_minuti_blocco("tel_chat_simon_b1_entrata_1", "ricevi", 1):
        return
    $ msg("simon", "You always train facing away from the mirror. I noticed. Everything ok?")
    label tel_chat_simon_b1_entrata_2:
    if telefono_minuti_blocco("tel_chat_simon_b1_entrata_2", "invia", 1):
        return
    $ msg("sara", "I hate the mirrors. That's all.")
    return

label chat_simon_b1_1:
    label tel_chat_simon_b1_1_1:
    if telefono_minuti_blocco("tel_chat_simon_b1_1_1", "ricevi", 2):
        return
    $ msg("simon", "Not stupid. Almost everyone does, at the beginning.")
    $ msg("simon", "What do you see in there?")
    label tel_chat_simon_b1_1_2:
    if telefono_minuti_blocco("tel_chat_simon_b1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Someone who doesn't belong in a gym.»":
            label tel_chat_simon_b1_1_3:
            if telefono_minuti_blocco("tel_chat_simon_b1_1_3", "invia", 1):
                return
            $ msg("sara", "Someone who doesn't belong in a gym.")
            label tel_chat_simon_b1_1_4:
            if telefono_minuti_blocco("tel_chat_simon_b1_1_4", "ricevi", 1):
                return
            $ msg("simon", "Wrong. You show up every week. That's the only thing that makes someone belong.")
        "«Everything I'd like to change.»":
            label tel_chat_simon_b1_1_5:
            if telefono_minuti_blocco("tel_chat_simon_b1_1_5", "invia", 1):
                return
            $ msg("sara", "Everything I'd like to change.")
            label tel_chat_simon_b1_1_6:
            if telefono_minuti_blocco("tel_chat_simon_b1_1_6", "ricevi", 1):
                return
            $ msg("simon", "Then look at what's already changed. Your posture. Your squat. You stand differently.")
            $ caldo()
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b1_1_2"
            $ telefono_minuti_chiudi = True
            return
    $ segna("simon_insicurezza")
    return

label chat_simon_b1_2:
    label tel_chat_simon_b1_2_1:
    if telefono_minuti_blocco("tel_chat_simon_b1_2_1", "ricevi", 1):
        return
    $ msg("simon", "Next time, one set facing the mirror. Just one. Watch your form, not the rest.")
    sp "Watch your form, not the rest. He makes it sound so easy."
    label tel_chat_simon_b1_2_2:
    if telefono_minuti_blocco("tel_chat_simon_b1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«One set. I'll try.»":
            label tel_chat_simon_b1_2_3:
            if telefono_minuti_blocco("tel_chat_simon_b1_2_3", "invia", 1):
                return
            $ msg("sara", "One set. I'll try.")
            label tel_chat_simon_b1_2_4:
            if telefono_minuti_blocco("tel_chat_simon_b1_2_4", "ricevi", 1):
                return
            $ msg("simon", "That's all I'm asking.")
        "«Only if you don't laugh.»":
            label tel_chat_simon_b1_2_5:
            if telefono_minuti_blocco("tel_chat_simon_b1_2_5", "invia", 1):
                return
            $ msg("sara", "Only if you don't laugh.")
            $ caldo()
            label tel_chat_simon_b1_2_6:
            if telefono_minuti_blocco("tel_chat_simon_b1_2_6", "ricevi", 1):
                return
            $ msg("simon", "I never laugh at people who work hard. Only at people who skip leg day.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B2: la vita da single ---------------------------------------------------

label chat_simon_b2:
    label tel_chat_simon_b2_1:
    if telefono_minuti_blocco("tel_chat_simon_b2_1", "invia", 1):
        return
    $ msg("sara", "Joanie asked me to ask you something. Are you seeing anyone? Her words, not mine.")
    return

label chat_simon_b2_1:
    label tel_chat_simon_b2_1_1:
    if telefono_minuti_blocco("tel_chat_simon_b2_1_1", "ricevi", 2):
        return
    $ msg("simon", "Haha. Tell Joanie: no. Single.")
    $ msg("simon", "Between the gym, clients and the weekend, there's not much room left.")
    label tel_chat_simon_b2_1_2:
    if telefono_minuti_blocco("tel_chat_simon_b2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Sounds lonely.»":
            label tel_chat_simon_b2_1_3:
            if telefono_minuti_blocco("tel_chat_simon_b2_1_3", "invia", 1):
                return
            $ msg("sara", "Sounds lonely.")
            label tel_chat_simon_b2_1_4:
            if telefono_minuti_blocco("tel_chat_simon_b2_1_4", "ricevi", 1):
                return
            $ msg("simon", "Sometimes. Mostly it's just free.")
        "«The gym is your relationship.»":
            label tel_chat_simon_b2_1_5:
            if telefono_minuti_blocco("tel_chat_simon_b2_1_5", "invia", 1):
                return
            $ msg("sara", "The gym is your relationship.")
            $ caldo()
            label tel_chat_simon_b2_1_6:
            if telefono_minuti_blocco("tel_chat_simon_b2_1_6", "ricevi", 1):
                return
            $ msg("simon", "The gym and I are very happy together. It never asks where I've been.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_b2_2:
    label tel_chat_simon_b2_2_1:
    if telefono_minuti_blocco("tel_chat_simon_b2_2_1", "ricevi", 1):
        return
    $ msg("simon", "And you? How long with [nome_compagno]?")
    sp "He remembers his name."
    label tel_chat_simon_b2_2_2:
    if telefono_minuti_blocco("tel_chat_simon_b2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«A few years. He's a good man.»":
            label tel_chat_simon_b2_2_3:
            if telefono_minuti_blocco("tel_chat_simon_b2_2_3", "invia", 1):
                return
            $ msg("sara", "A few years. He's a good man.")
            label tel_chat_simon_b2_2_4:
            if telefono_minuti_blocco("tel_chat_simon_b2_2_4", "ricevi", 1):
                return
            $ msg("simon", "Good. That's rare.")
            $ interest("josh", 1)
        "«A few years. It's... comfortable.»":
            label tel_chat_simon_b2_2_5:
            if telefono_minuti_blocco("tel_chat_simon_b2_2_5", "invia", 1):
                return
            $ msg("sara", "A few years. It's... comfortable.")
            label tel_chat_simon_b2_2_6:
            if telefono_minuti_blocco("tel_chat_simon_b2_2_6", "ricevi", 1):
                return
            $ msg("simon", "Comfortable is good. Comfortable is also a word people use for sofas.")
            sp "Why did I write «comfortable»?"
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B3: come lui vede Sara (solo progressi) ---------------------------------

label chat_simon_b3:
    label tel_chat_simon_b3_1:
    if telefono_minuti_blocco("tel_chat_simon_b3_1", "invia", 1):
        return
    $ msg("sara", "Be honest with me. Am I hopeless? As a client, I mean.")
    return

label chat_simon_b3_1:
    label tel_chat_simon_b3_1_1:
    if telefono_minuti_blocco("tel_chat_simon_b3_1_1", "ricevi", 2):
        return
    $ msg("simon", "Honest? You're one of the most improved people I train.")
    $ msg("simon", "Four weeks ago you couldn't hold a plank for twenty seconds. Now it's a minute.")
    label tel_chat_simon_b3_1_2:
    if telefono_minuti_blocco("tel_chat_simon_b3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You're just being nice.»":
            label tel_chat_simon_b3_1_3:
            if telefono_minuti_blocco("tel_chat_simon_b3_1_3", "invia", 1):
                return
            $ msg("sara", "You're just being nice.")
            label tel_chat_simon_b3_1_4:
            if telefono_minuti_blocco("tel_chat_simon_b3_1_4", "ricevi", 1):
                return
            $ msg("simon", "I'm never nice about planks. Ask anyone.")
        "«Really? A minute?»":
            label tel_chat_simon_b3_1_5:
            if telefono_minuti_blocco("tel_chat_simon_b3_1_5", "invia", 1):
                return
            $ msg("sara", "Really? A minute?")
            $ caldo()
            label tel_chat_simon_b3_1_6:
            if telefono_minuti_blocco("tel_chat_simon_b3_1_6", "ricevi", 1):
                return
            $ msg("simon", "I count. It's my job.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_b3_2:
    label tel_chat_simon_b3_2_1:
    if telefono_minuti_blocco("tel_chat_simon_b3_2_1", "ricevi", 1):
        return
    $ msg("simon", "You listen, you don't complain much, and you come back. That's 90% of it.")
    sp "I complain a lot. Just not to him."
    label tel_chat_simon_b3_2_2:
    if telefono_minuti_blocco("tel_chat_simon_b3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Thank you. I needed that.»":
            label tel_chat_simon_b3_2_3:
            if telefono_minuti_blocco("tel_chat_simon_b3_2_3", "invia", 1):
                return
            $ msg("sara", "Thank you. I needed that.")
            $ caldo()
            label tel_chat_simon_b3_2_4:
            if telefono_minuti_blocco("tel_chat_simon_b3_2_4", "ricevi", 1):
                return
            $ msg("simon", "Anytime. Now go stretch.")
        "«I'll tell Joanie I'm your best client.»":
            label tel_chat_simon_b3_2_5:
            if telefono_minuti_blocco("tel_chat_simon_b3_2_5", "invia", 1):
                return
            $ msg("sara", "I'll tell Joanie I'm your best client.")
            label tel_chat_simon_b3_2_6:
            if telefono_minuti_blocco("tel_chat_simon_b3_2_6", "ricevi", 1):
                return
            $ msg("simon", "Don't. She'll want a rematch.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B4: le sue precedenti relazioni -----------------------------------------

label chat_simon_b4:
    label tel_chat_simon_b4_1:
    if telefono_minuti_blocco("tel_chat_simon_b4_1", "invia", 1):
        return
    $ msg("sara", "Can I ask why you're single? You seem like a catch. Joanie's words again.")
    return

label chat_simon_b4_1:
    label tel_chat_simon_b4_1_1:
    if telefono_minuti_blocco("tel_chat_simon_b4_1_1", "ricevi", 2):
        return
    $ msg("simon", "Joanie should open a dating agency.")
    $ msg("simon", "I was with someone for three years. She said I loved the gym more than her.")
    label tel_chat_simon_b4_1_2:
    if telefono_minuti_blocco("tel_chat_simon_b4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Was she right?»":
            label tel_chat_simon_b4_1_3:
            if telefono_minuti_blocco("tel_chat_simon_b4_1_3", "invia", 1):
                return
            $ msg("sara", "Was she right?")
            label tel_chat_simon_b4_1_4:
            if telefono_minuti_blocco("tel_chat_simon_b4_1_4", "ricevi", 1):
                return
            $ msg("simon", "...Partly. I was 22 and stupid. I'd do it differently now.")
        "«That must have hurt.»":
            label tel_chat_simon_b4_1_5:
            if telefono_minuti_blocco("tel_chat_simon_b4_1_5", "invia", 1):
                return
            $ msg("sara", "That must have hurt.")
            $ caldo()
            label tel_chat_simon_b4_1_6:
            if telefono_minuti_blocco("tel_chat_simon_b4_1_6", "ricevi", 1):
                return
            $ msg("simon", "It did. For a while. Then I trained more. Very healthy, I know.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_b4_2:
    label tel_chat_simon_b4_2_1:
    if telefono_minuti_blocco("tel_chat_simon_b4_2_1", "ricevi", 1):
        return
    $ msg("simon", "What about you? Ever been dumped for a hobby?")
    label tel_chat_simon_b4_2_2:
    if telefono_minuti_blocco("tel_chat_simon_b4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«No. I was the one who left, last time.»":
            label tel_chat_simon_b4_2_3:
            if telefono_minuti_blocco("tel_chat_simon_b4_2_3", "invia", 1):
                return
            $ msg("sara", "No. I was the one who left, last time.")
            label tel_chat_simon_b4_2_4:
            if telefono_minuti_blocco("tel_chat_simon_b4_2_4", "ricevi", 1):
                return
            $ msg("simon", "Good for you. Leaving takes guts.")
            sp "I don't want to talk about Jacob. Not with him."
        "«Only for my writing. [nome_compagno] says I live in my laptop.»":
            label tel_chat_simon_b4_2_5:
            if telefono_minuti_blocco("tel_chat_simon_b4_2_5", "invia", 1):
                return
            $ msg("sara", "Only for my writing. [nome_compagno] says I live in my laptop.")
            $ caldo()
            label tel_chat_simon_b4_2_6:
            if telefono_minuti_blocco("tel_chat_simon_b4_2_6", "ricevi", 1):
                return
            $ msg("simon", "Writing? You never told me. What do you write?")
            label tel_chat_simon_b4_2_7:
            if telefono_minuti_blocco("tel_chat_simon_b4_2_7", "invia", 1):
                return
            $ msg("sara", "Stories. A novel, maybe. One day.")
            label tel_chat_simon_b4_2_8:
            if telefono_minuti_blocco("tel_chat_simon_b4_2_8", "ricevi", 1):
                return
            $ msg("simon", "Cool. Train the body, train the head.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B5: il piacere di sentirsi notati (dai progressi) -----------------------

label chat_simon_b5:
    label tel_chat_simon_b5_1:
    if telefono_minuti_blocco("tel_chat_simon_b5_1", "invia", 1):
        return
    $ msg("sara", "Weird thing today. A colleague asked if I'd done something different. «You walk differently.»")
    return

label chat_simon_b5_1:
    label tel_chat_simon_b5_1_1:
    if telefono_minuti_blocco("tel_chat_simon_b5_1_1", "ricevi", 2):
        return
    $ msg("simon", "Ha! Told you. Posture changes first. People notice before you do.")
    $ msg("simon", "How did it feel?")
    label tel_chat_simon_b5_1_2:
    if telefono_minuti_blocco("tel_chat_simon_b5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Strange. I'm not used to being noticed.»":
            label tel_chat_simon_b5_1_3:
            if telefono_minuti_blocco("tel_chat_simon_b5_1_3", "invia", 1):
                return
            $ msg("sara", "Strange. I'm not used to being noticed.")
            label tel_chat_simon_b5_1_4:
            if telefono_minuti_blocco("tel_chat_simon_b5_1_4", "ricevi", 1):
                return
            $ msg("simon", "Get used to it. It's only going to happen more.")
        "«Good. Really good, actually.»":
            label tel_chat_simon_b5_1_5:
            if telefono_minuti_blocco("tel_chat_simon_b5_1_5", "invia", 1):
                return
            $ msg("sara", "Good. Really good, actually.")
            $ caldo()
            label tel_chat_simon_b5_1_6:
            if telefono_minuti_blocco("tel_chat_simon_b5_1_6", "ricevi", 1):
                return
            $ msg("simon", "That's the feeling. Remember it on the days you don't want to come.")
            $ segna("simon_notata")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_simon_b5_2:
    label tel_chat_simon_b5_2_1:
    if telefono_minuti_blocco("tel_chat_simon_b5_2_1", "ricevi", 1):
        return
    $ msg("simon", "You did the work. Not me. Enjoy it.")
    sp "Enjoy it. When was the last time someone told me to enjoy something about myself?"
    label tel_chat_simon_b5_2_2:
    if telefono_minuti_blocco("tel_chat_simon_b5_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I will. Thanks, Simon.»":
            label tel_chat_simon_b5_2_3:
            if telefono_minuti_blocco("tel_chat_simon_b5_2_3", "invia", 1):
                return
            $ msg("sara", "I will. Thanks, Simon.")
            label tel_chat_simon_b5_2_4:
            if telefono_minuti_blocco("tel_chat_simon_b5_2_4", "ricevi", 1):
                return
            $ msg("simon", ":)")
        "«You did some of the work. The shouting part.»":
            label tel_chat_simon_b5_2_5:
            if telefono_minuti_blocco("tel_chat_simon_b5_2_5", "invia", 1):
                return
            $ msg("sara", "You did some of the work. The shouting part.")
            $ caldo()
            label tel_chat_simon_b5_2_6:
            if telefono_minuti_blocco("tel_chat_simon_b5_2_6", "ricevi", 1):
                return
            $ msg("simon", "I never shout. I motivate loudly.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b5_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_simon_b5_2_2"
            $ telefono_minuti_chiudi = True
            return
    return
