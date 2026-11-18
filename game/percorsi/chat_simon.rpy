## =============================================================================
## SIMON — discorsi al telefono: introduzione, A (conoscenti), B (confidenza)
## =============================================================================
## Tono (Q&A 18/11/2026): cordiale e professionale, con un filo di attenzione.
## In B complimenti SOLO sui progressi: il personale resta fuori, il flirt è da C.
## Modello: docs/argomenti-telefono.md e game/percorsi/leggimi_percorsi.rpy.

init python:
    discorso("simon_intro", "simon", ESTRANEI)
    discorso("simon_a1", "simon", CONOSCENTI)
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
    $ msg("sara", "Hi, it's Sara. From the gym. You said I could text you about the exercises... is that still ok?")
    return

label chat_simon_intro_1:
    $ msg("simon", "Of course! Joanie's friend. The shoulder, right?")
    $ msg("simon", "How's it feeling?")
    menu (screen="scelta_telefono"):
        "«Much better. You fixed it.»":
            $ msg("sara", "Much better. You fixed it.")
            $ caldo()
            $ msg("simon", "You fixed it. I just pointed.")
        "«Still a bit stiff.»":
            $ msg("sara", "Still a bit stiff.")
            $ msg("simon", "Normal. It'll loosen up if you keep moving it.")
    return

label chat_simon_intro_2:
    $ msg("simon", "Next session: ten minutes on the bike to warm up, then back and shoulders. Light.")
    $ msg("simon", "And bring water. Real water, not those neon drinks.")
    sp "Neon drinks. Joanie's bottle is literally blue."
    menu (screen="scelta_telefono"):
        "«Noted.»":
            $ msg("sara", "Noted.")
            $ msg("simon", "See you there.")
        "«Yes, sir :)»":
            $ msg("sara", "Yes, sir :)")
            $ caldo()
            $ msg("simon", "Ha. Simon is fine.")
        "«Do you give homework to all your clients?»" (confidence=25):
            $ msg("sara", "Do you give homework to all your clients?")
            $ caldo()
            $ msg("simon", "Only the ones who actually do it.")
            sp "Is that a compliment or a challenge?"
    return


## --- A1: dolori muscolari (bozza approvata da Jody) --------------------------

label chat_simon_a1:
    $ msg("sara", "Hi Simon, it's Sara. Quick question... is it normal that I can't walk down the stairs today? :)")
    return

label chat_simon_a1_entrata:
    $ msg("simon", "Day after leg day. How are the stairs treating you? ;)")
    $ msg("sara", "Is it normal that I can't walk down them? :)")
    return

label chat_simon_a1_1:
    $ msg("simon", "Haha, totally normal. It's called DOMS.")
    $ msg("simon", "Delayed onset muscle soreness. Basically your legs are filing a complaint.")
    sp "He even makes pain sound fun."
    menu (screen="scelta_telefono"):
        "«So what do I do? Stay on the sofa all day?»":
            $ msg("sara", "So what do I do? Stay on the sofa all day?")
            $ msg("simon", "Nope. The sofa is the enemy.")
        "«Tell my legs it was your idea, not mine.»":
            $ msg("sara", "Tell my legs it was your idea, not mine.")
            $ caldo()
            $ msg("simon", "Already did. They said you're tougher than you look.")
        "«Next time go easier on me, coach.»" (confidence=25):
            $ msg("sara", "Next time go easier on me, coach.")
            $ caldo()
            $ msg("simon", "Easier? You were the one who asked for one more set.")
            $ msg("simon", "Coach. I like that.")
    return

label chat_simon_a1_2:
    $ msg("simon", "Light walk, lots of water, ten minutes of stretching before bed.")
    $ msg("simon", "And a hot shower. Not a cold one, whatever Joanie tells you.")
    sp "How does he know Joanie told me to take a cold shower?"
    menu (screen="scelta_telefono"):
        "«Joanie says a lot of things.»":
            $ msg("sara", "Joanie says a lot of things.")
            $ msg("simon", "She does. Don't listen to half of them.")
        "«Can you send me the stretches?»":
            $ msg("sara", "Can you send me the stretches?")
            $ segna("simon_stretching")
        "«Or I could just skip leg day forever.»":
            $ msg("sara", "Or I could just skip leg day forever.")
            $ msg("simon", "Not on my watch.")
    return

label chat_simon_a1_3:
    if fatto("simon_stretching"):
        $ msg("simon", "1. Quads against the wall, 30 seconds each leg.")
        $ msg("simon", "2. Sit down, legs straight, reach for your toes. Don't bounce.")
        $ msg("simon", "3. Child's pose. Just breathe.")
        $ msg("simon", "Do them tonight. I'll ask you next time.")
    else:
        $ msg("simon", "Do the stretches anyway. I'll ask you next time.")
    menu (screen="scelta_telefono"):
        "«Promise.»":
            $ msg("sara", "Promise.")
            $ msg("simon", "That's the spirit.")
        "«Yes, coach :)»":
            $ msg("sara", "Yes, coach :)")
            $ caldo()
            $ msg("simon", "Good. Now go drink some water.")
        "«We'll see ;)»" (confidence=25):
            $ msg("sara", "We'll see ;)")
            $ caldo()
            $ msg("simon", "I'll know if you didn't. I always know.")
            sp "Does he say that to all his clients?"
    return


## --- A2: alimentazione -------------------------------------------------------

label chat_simon_a2:
    $ msg("sara", "Ok, nutrition question. What am I supposed to eat before training? I always feel dizzy.")
    return

label chat_simon_a2_entrata:
    $ msg("simon", "Random check: what did you eat before yesterday's session? You looked pale.")
    $ msg("sara", "Coffee. And half a cookie. Is that bad?")
    return

label chat_simon_a2_1:
    $ msg("simon", "That's why. You're training on empty.")
    $ msg("simon", "An hour before: a banana, some yogurt, a slice of toast. Nothing heavy.")
    menu (screen="scelta_telefono"):
        "«Does chocolate count as fuel?»":
            $ msg("sara", "Does chocolate count as fuel?")
            $ caldo()
            $ msg("simon", "Dark chocolate, two squares. After. As a reward.")
        "«A banana I can do.»":
            $ msg("sara", "A banana I can do.")
            $ msg("simon", "Good. Small changes, big difference.")
    return

label chat_simon_a2_2:
    $ msg("simon", "And breakfast. Real breakfast. Oats, eggs, fruit.")
    $ msg("simon", "I'll send you what I eat. Copy it for a week and tell me how you feel.")
    $ segna("simon_colazione")
    sp "His breakfast has more protein than my entire week."
    menu (screen="scelta_telefono"):
        "«Deal. One week.»":
            $ msg("sara", "Deal. One week.")
            $ msg("simon", "I'll hold you to it.")
        "«Do you ever eat pizza? Be honest.»":
            $ msg("sara", "Do you ever eat pizza? Be honest.")
            $ caldo()
            $ msg("simon", "Every Saturday. Don't tell my clients.")
            $ msg("sara", "Your secret is safe.")
    return


## --- A3: musica in palestra --------------------------------------------------

label chat_simon_a3:
    $ msg("sara", "Can I file a complaint about the gym music? Same five songs every day.")
    return

label chat_simon_a3_1:
    $ msg("simon", "Haha. That's the owner's playlist. I've been fighting it for two years.")
    $ msg("simon", "What do you listen to when you train?")
    menu (screen="scelta_telefono"):
        "«Old pop. Don't judge me.»":
            $ msg("sara", "Old pop. Don't judge me.")
            $ msg("simon", "No judging. Whatever makes you move.")
        "«Nothing. I'm too busy trying not to die.»":
            $ msg("sara", "Nothing. I'm too busy trying not to die.")
            $ caldo()
            $ msg("simon", "Ha! That's a playlist too.")
    return

label chat_simon_a3_2:
    $ msg("simon", "Try this. Fast enough for cardio, not so loud it kills you.")
    $ msg("simon", "(A link to a playlist: «Simon — Leg Day»)")
    $ segna("simon_playlist")
    sp "A playlist called Leg Day. Of course."
    menu (screen="scelta_telefono"):
        "«I'll try it tomorrow.»":
            $ msg("sara", "I'll try it tomorrow.")
            $ msg("simon", "Tell me if it works.")
        "«If I survive leg day, it's thanks to this.»":
            $ msg("sara", "If I survive leg day, it's thanks to this.")
            $ caldo()
            $ msg("simon", "You'll survive. You always do.")
    return


## --- A4: esercizi preferiti --------------------------------------------------

label chat_simon_a4:
    $ msg("sara", "Honest question: is there anyone in the world who actually likes burpees?")
    return

label chat_simon_a4_1:
    $ msg("simon", "Me.")
    $ msg("simon", "But I also like deadlifts, so I'm not a reliable witness.")
    menu (screen="scelta_telefono"):
        "«What's your favourite one?»":
            $ msg("sara", "What's your favourite one?")
            $ msg("simon", "Deadlift. Pick something heavy off the floor. Simple. Honest.")
        "«You're a monster.»":
            $ msg("sara", "You're a monster.")
            $ caldo()
            $ msg("simon", "A friendly monster.")
    return

label chat_simon_a4_2:
    $ msg("simon", "What's yours? And «none» is not an answer.")
    menu (screen="scelta_telefono"):
        "«The bike. Because I can sit.»":
            $ msg("sara", "The bike. Because I can sit.")
            $ msg("simon", "Fair. We'll work on that.")
        "«Squats. They're starting to feel good.»":
            $ msg("sara", "Squats. They're starting to feel good.")
            $ caldo()
            $ msg("simon", "Squats are the queen of exercises. Good taste.")
            $ segna("simon_squat")
    return


## --- A5: il weekend ----------------------------------------------------------

label chat_simon_a5:
    $ msg("sara", "Do personal trainers rest on weekends or do you live at the gym?")
    return

label chat_simon_a5_1:
    $ msg("simon", "Saturday mornings I hike with some friends. Saturday nights, out.")
    $ msg("simon", "Sunday I do absolutely nothing. It's sacred.")
    $ msg("simon", "You?")
    menu (screen="scelta_telefono"):
        "«[nome_compagno] and I usually stay in. Movies, takeaway.»":
            $ msg("sara", "[nome_compagno] and I usually stay in. Movies, takeaway.")
            $ msg("simon", "Sounds nice. Calm.")
        "«Nothing exciting. Laundry, mostly.»":
            $ msg("sara", "Nothing exciting. Laundry, mostly.")
            $ msg("simon", "Laundry. Wild.")
    return

label chat_simon_a5_2:
    $ msg("simon", "If you ever want to try a hike, the trail by the lake is easy. Great view.")
    sp "He didn't say «with me». He just said «try a hike»."
    menu (screen="scelta_telefono"):
        "«Maybe with Joanie, one day.»":
            $ msg("sara", "Maybe with Joanie, one day.")
            $ msg("simon", "Good idea.")
        "«Send me the name of the trail.»":
            $ msg("sara", "Send me the name of the trail.")
            $ caldo()
            $ msg("simon", "Pine Ridge. Start early, it gets crowded.")
    return


## --- A6: locali notturni -----------------------------------------------------

label chat_simon_a6:
    $ msg("sara", "Joanie wants to go out Saturday and says you know every bar in town. Is that true?")
    return

label chat_simon_a6_1:
    $ msg("simon", "Every bar is an exaggeration. Most of them.")
    $ msg("simon", "What kind of night? Dancing, drinks, or talking without shouting?")
    menu (screen="scelta_telefono"):
        "«Talking without shouting. I'm old.»":
            $ msg("sara", "Talking without shouting. I'm old.")
            $ msg("simon", "You're not old. Try The Lantern, on the river. Quiet, good cocktails.")
        "«Joanie will say dancing. She always does.»":
            $ msg("sara", "Joanie will say dancing. She always does.")
            $ caldo()
            $ msg("simon", "Then Velvet. But wear comfortable shoes, the floor is murder.")
    return

label chat_simon_a6_2:
    $ msg("simon", "If you go, say hi. I'm usually around with my friends.")
    sp "He'd be there. Of course he would."
    menu (screen="scelta_telefono"):
        "«We'll see what Joanie decides.»":
            $ msg("sara", "We'll see what Joanie decides.")
            $ msg("simon", "She always decides.")
        "«Then I'll know at least one face.»":
            $ msg("sara", "Then I'll know at least one face.")
            $ caldo()
            $ msg("simon", "A friendly one :)")
    return


## --- A7: abbigliamento sportivo ----------------------------------------------

label chat_simon_a7:
    $ msg("sara", "My running shoes are older than my relationship. Should I buy new ones?")
    return

label chat_simon_a7_1:
    $ msg("simon", "If they're older than your relationship, yes. Definitely.")
    $ msg("simon", "Go to a proper shop. Ask them to look at how you walk.")
    menu (screen="scelta_telefono"):
        "«And clothes? I train in an old T-shirt.»":
            $ msg("sara", "And clothes? I train in an old T-shirt.")
            $ msg("simon", "Whatever you're comfortable in. Comfortable means you move better.")
        "«Do you get a commission from the shoe shop?»":
            $ msg("sara", "Do you get a commission from the shoe shop?")
            $ caldo()
            $ msg("simon", "I wish. I'd be rich. Everyone has bad shoes.")
    return

label chat_simon_a7_2:
    $ msg("simon", "Honestly, the shoes matter. The rest is up to you.")
    $ msg("simon", "Some people train better when they feel good in what they wear. That's all.")
    sp "Joanie would say that's a hint about the tight top. Simon probably just means... shoes."
    menu (screen="scelta_telefono"):
        "«Shoes first. Then we'll see.»":
            $ msg("sara", "Shoes first. Then we'll see.")
            $ msg("simon", "Good plan.")
        "«Joanie wants me to buy matching sets. Like hers.»":
            $ msg("sara", "Joanie wants me to buy matching sets. Like hers.")
            $ caldo()
            $ msg("simon", "Joanie's sets are a whole event. You don't need an event. You need to train.")
    return


## --- A8: obiettivi fisici ----------------------------------------------------

label chat_simon_a8:
    $ msg("sara", "Can I ask you something? What should my goal be? I don't even know why I'm training.")
    return

label chat_simon_a8_1:
    $ msg("simon", "Good question. Most people never ask it.")
    $ msg("simon", "What do you want to feel? Not look. Feel.")
    menu (screen="scelta_telefono"):
        "«Stronger. I want to carry the shopping without dying.»":
            $ msg("sara", "Stronger. I want to carry the shopping without dying.")
            $ msg("simon", "That's a real goal. I like real goals.")
        "«More sure of myself.»":
            $ msg("sara", "More sure of myself.")
            $ caldo()
            $ msg("simon", "That's the best one. And training is a good way to get there.")
    return

label chat_simon_a8_2:
    $ msg("simon", "So here's yours: ten proper push-ups by the end of the month.")
    $ msg("simon", "Not on your knees. Proper ones.")
    $ segna("simon_obiettivo_pushup")
    sp "Ten. I can barely do two."
    menu (screen="scelta_telefono"):
        "«Ten? Are you serious?»":
            $ msg("sara", "Ten? Are you serious?")
            $ msg("simon", "Completely. You'll get there.")
        "«Deal. And if I make it?»" (confidence=25):
            $ msg("sara", "Deal. And if I make it?")
            $ caldo()
            $ msg("simon", "Then you set the next goal. Not me.")
            sp "I like that more than I should."
    return


## --- B1: insicurezze sul corpo -----------------------------------------------

label chat_simon_b1:
    $ msg("sara", "Can I tell you something stupid? I hate the mirrors at the gym.")
    return

label chat_simon_b1_entrata:
    $ msg("simon", "You always train facing away from the mirror. I noticed. Everything ok?")
    $ msg("sara", "I hate the mirrors. That's all.")
    return

label chat_simon_b1_1:
    $ msg("simon", "Not stupid. Almost everyone does, at the beginning.")
    $ msg("simon", "What do you see in there?")
    menu (screen="scelta_telefono"):
        "«Someone who doesn't belong in a gym.»":
            $ msg("sara", "Someone who doesn't belong in a gym.")
            $ msg("simon", "Wrong. You show up every week. That's the only thing that makes someone belong.")
        "«Everything I'd like to change.»":
            $ msg("sara", "Everything I'd like to change.")
            $ msg("simon", "Then look at what's already changed. Your posture. Your squat. You stand differently.")
            $ caldo()
    $ segna("simon_insicurezza")
    return

label chat_simon_b1_2:
    $ msg("simon", "Next time, one set facing the mirror. Just one. Watch your form, not the rest.")
    sp "Watch your form, not the rest. He makes it sound so easy."
    menu (screen="scelta_telefono"):
        "«One set. I'll try.»":
            $ msg("sara", "One set. I'll try.")
            $ msg("simon", "That's all I'm asking.")
        "«Only if you don't laugh.»":
            $ msg("sara", "Only if you don't laugh.")
            $ caldo()
            $ msg("simon", "I never laugh at people who work hard. Only at people who skip leg day.")
    return


## --- B2: la vita da single ---------------------------------------------------

label chat_simon_b2:
    $ msg("sara", "Joanie asked me to ask you something. Are you seeing anyone? Her words, not mine.")
    return

label chat_simon_b2_1:
    $ msg("simon", "Haha. Tell Joanie: no. Single.")
    $ msg("simon", "Between the gym, clients and the weekend, there's not much room left.")
    menu (screen="scelta_telefono"):
        "«Sounds lonely.»":
            $ msg("sara", "Sounds lonely.")
            $ msg("simon", "Sometimes. Mostly it's just free.")
        "«The gym is your relationship.»":
            $ msg("sara", "The gym is your relationship.")
            $ caldo()
            $ msg("simon", "The gym and I are very happy together. It never asks where I've been.")
    return

label chat_simon_b2_2:
    $ msg("simon", "And you? How long with [nome_compagno]?")
    sp "He remembers his name."
    menu (screen="scelta_telefono"):
        "«A few years. He's a good man.»":
            $ msg("sara", "A few years. He's a good man.")
            $ msg("simon", "Good. That's rare.")
            $ interest("josh", 1)
        "«A few years. It's... comfortable.»":
            $ msg("sara", "A few years. It's... comfortable.")
            $ msg("simon", "Comfortable is good. Comfortable is also a word people use for sofas.")
            sp "Why did I write «comfortable»?"
    return


## --- B3: come lui vede Sara (solo progressi) ---------------------------------

label chat_simon_b3:
    $ msg("sara", "Be honest with me. Am I hopeless? As a client, I mean.")
    return

label chat_simon_b3_1:
    $ msg("simon", "Honest? You're one of the most improved people I train.")
    $ msg("simon", "Four weeks ago you couldn't hold a plank for twenty seconds. Now it's a minute.")
    menu (screen="scelta_telefono"):
        "«You're just being nice.»":
            $ msg("sara", "You're just being nice.")
            $ msg("simon", "I'm never nice about planks. Ask anyone.")
        "«Really? A minute?»":
            $ msg("sara", "Really? A minute?")
            $ caldo()
            $ msg("simon", "I count. It's my job.")
    return

label chat_simon_b3_2:
    $ msg("simon", "You listen, you don't complain much, and you come back. That's 90% of it.")
    sp "I complain a lot. Just not to him."
    menu (screen="scelta_telefono"):
        "«Thank you. I needed that.»":
            $ msg("sara", "Thank you. I needed that.")
            $ caldo()
            $ msg("simon", "Anytime. Now go stretch.")
        "«I'll tell Joanie I'm your best client.»":
            $ msg("sara", "I'll tell Joanie I'm your best client.")
            $ msg("simon", "Don't. She'll want a rematch.")
    return


## --- B4: le sue precedenti relazioni -----------------------------------------

label chat_simon_b4:
    $ msg("sara", "Can I ask why you're single? You seem like a catch. Joanie's words again.")
    return

label chat_simon_b4_1:
    $ msg("simon", "Joanie should open a dating agency.")
    $ msg("simon", "I was with someone for three years. She said I loved the gym more than her.")
    menu (screen="scelta_telefono"):
        "«Was she right?»":
            $ msg("sara", "Was she right?")
            $ msg("simon", "...Partly. I was 22 and stupid. I'd do it differently now.")
        "«That must have hurt.»":
            $ msg("sara", "That must have hurt.")
            $ caldo()
            $ msg("simon", "It did. For a while. Then I trained more. Very healthy, I know.")
    return

label chat_simon_b4_2:
    $ msg("simon", "What about you? Ever been dumped for a hobby?")
    menu (screen="scelta_telefono"):
        "«No. I was the one who left, last time.»":
            $ msg("sara", "No. I was the one who left, last time.")
            $ msg("simon", "Good for you. Leaving takes guts.")
            sp "I don't want to talk about Jacob. Not with him."
        "«Only for my writing. [nome_compagno] says I live in my laptop.»":
            $ msg("sara", "Only for my writing. [nome_compagno] says I live in my laptop.")
            $ caldo()
            $ msg("simon", "Writing? You never told me. What do you write?")
            $ msg("sara", "Stories. A novel, maybe. One day.")
            $ msg("simon", "Cool. Train the body, train the head.")
    return


## --- B5: il piacere di sentirsi notati (dai progressi) -----------------------

label chat_simon_b5:
    $ msg("sara", "Weird thing today. A colleague asked if I'd done something different. «You walk differently.»")
    return

label chat_simon_b5_1:
    $ msg("simon", "Ha! Told you. Posture changes first. People notice before you do.")
    $ msg("simon", "How did it feel?")
    menu (screen="scelta_telefono"):
        "«Strange. I'm not used to being noticed.»":
            $ msg("sara", "Strange. I'm not used to being noticed.")
            $ msg("simon", "Get used to it. It's only going to happen more.")
        "«Good. Really good, actually.»":
            $ msg("sara", "Good. Really good, actually.")
            $ caldo()
            $ msg("simon", "That's the feeling. Remember it on the days you don't want to come.")
            $ segna("simon_notata")
    return

label chat_simon_b5_2:
    $ msg("simon", "You did the work. Not me. Enjoy it.")
    sp "Enjoy it. When was the last time someone told me to enjoy something about myself?"
    menu (screen="scelta_telefono"):
        "«I will. Thanks, Simon.»":
            $ msg("sara", "I will. Thanks, Simon.")
            $ msg("simon", ":)")
        "«You did some of the work. The shouting part.»":
            $ msg("sara", "You did some of the work. The shouting part.")
            $ caldo()
            $ msg("simon", "I never shout. I motivate loudly.")
    return
