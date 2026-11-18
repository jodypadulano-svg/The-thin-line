## =============================================================================
## JOANIE (chiave "amica") — discorsi al telefono: introduzione, A, B
## =============================================================================
## Tono (Q&A 18/11/2026): la tifosa. Chiede di Simon, Daniel, poi Jacob a seconda
## di come vanno quei percorsi (le chat cambiano con la partita). Da B rari indizi
## ambigui che coglie solo il giocatore; Sara non li nota. Nessun indizio esplicito.
## Mark è il suo fidanzato. B4 solo dopo il ritorno di Jacob (flag jacob_tornato).

init python:
    discorso("amica_intro", "amica", ESTRANEI)
    discorso("amica_a1", "amica", CONOSCENTI)
    discorso("amica_a2", "amica", CONOSCENTI)
    discorso("amica_a3", "amica", CONOSCENTI)
    discorso("amica_a4", "amica", CONOSCENTI)
    discorso("amica_a5", "amica", CONOSCENTI)
    discorso("amica_a6", "amica", CONOSCENTI)
    discorso("amica_a7", "amica", CONOSCENTI)
    discorso("amica_a8", "amica", CONOSCENTI)
    discorso("amica_b1", "amica", CONFIDENZA)
    discorso("amica_b2", "amica", CONFIDENZA)
    discorso("amica_b3", "amica", CONFIDENZA)
    discorso("amica_b4", "amica", CONFIDENZA, se="fatto('jacob_tornato')")
    discorso("amica_b5", "amica", CONFIDENZA)


## --- Introduzione: la solita chiacchierata fra amiche ------------------------

label chat_amica_intro:
    $ msg("sara", "Are you awake? I'm bored.")
    return

label chat_amica_intro_entrata:
    $ msg("amica", "BORED. ENTERTAIN ME.")
    $ msg("sara", "Ha. Same here.")
    return

label chat_amica_intro_1:
    $ msg("amica", "omg yes. Mark is watching football and I'm dying")
    $ msg("amica", "tell me something. anything. gossip, drama, a crime")
    menu (screen="scelta_telefono"):
        "«Nothing happens in my life, you know that.»":
            $ msg("sara", "Nothing happens in my life, you know that.")
            $ msg("amica", "LIES. something always happens. you just don't tell me")
        "«My boss told me to wear a lower neckline.»":
            $ msg("sara", "My boss told me to wear a lower neckline.")
            $ caldo()
            $ msg("amica", "BARBARA?? I love her. and she's right, sorry")
    return

label chat_amica_intro_2:
    $ msg("amica", "ok I have to go, Mark scored. I mean his team. whatever")
    $ msg("amica", "love you babe. sleep well")
    menu (screen="scelta_telefono"):
        "«Love you too.»":
            $ msg("sara", "Love you too.")
            $ caldo()
        "«Night!»":
            $ msg("sara", "Night!")
    return


## --- A1: la palestra (tifosa di Simon) ---------------------------------------

label chat_amica_a1:
    $ msg("sara", "My legs are dead. Why did I let you sign me up for the gym?")
    return

label chat_amica_a1_1:
    $ msg("amica", "because you love me. and because of the view ;)")
    if percorso("simon").interest >= 5:
        $ msg("amica", "also. Simon. talks about you. like, a lot")
        $ msg("amica", "«Sara's squat is getting really good». HIS WORDS")
        sp "He talks about my squat with Joanie?"
    else:
        $ msg("amica", "Simon asked where you were last time. just saying")
    menu (screen="scelta_telefono"):
        "«He's my trainer, Joanie. Stop.»":
            $ msg("sara", "He's my trainer, Joanie. Stop.")
            $ msg("amica", "a trainer with ARMS. I'm just pointing out facts")
        "«...He did?»":
            $ msg("sara", "...He did?")
            $ caldo()
            $ interest("simon", 1)
            $ msg("amica", "HE DID. ok I'm screaming")
    return

label chat_amica_a1_2:
    $ msg("amica", "Thursday. you and me. no excuses. wear the black leggings")
    return


## --- A2: shopping ------------------------------------------------------------

label chat_amica_a2:
    $ msg("sara", "I need a dress for Saturday and everything I own is beige.")
    return

label chat_amica_a2_1:
    $ msg("amica", "FINALLY. I've been waiting years for this message")
    $ msg("amica", "tomorrow after work. the mall. I'm choosing. you're not allowed to say «too short»")
    menu (screen="scelta_telefono"):
        "«Within reason.»":
            $ msg("sara", "Within reason.")
            $ msg("amica", "reason is beige. no reason")
        "«Fine. You choose.»":
            $ msg("sara", "Fine. You choose.")
            $ caldo()
            $ corruption(1)
            $ msg("amica", "best. day. ever")
            $ segna("joanie_sceglie_vestito")
    return

label chat_amica_a2_2:
    $ msg("amica", "you have the body of a goddess and you dress like a librarian. it's a crime")
    sp "A goddess. Joanie always exaggerates."
    return


## --- A3: il fidanzato di Joanie ----------------------------------------------

label chat_amica_a3:
    $ msg("sara", "How are things with Mark?")
    return

label chat_amica_a3_1:
    $ msg("amica", "good! he's so sweet. he made me breakfast today. heart-shaped pancakes")
    $ msg("amica", "they looked like kidneys but the thought counts")
    menu (screen="scelta_telefono"):
        "«He's a keeper.»":
            $ msg("sara", "He's a keeper.")
            $ caldo()
            $ msg("amica", "he is. he really is")
        "«[nome_compagno] has never made me pancakes.»":
            $ msg("sara", "[nome_compagno] has never made me pancakes.")
            $ msg("amica", "then [nome_compagno] has work to do")
    return

label chat_amica_a3_2:
    $ msg("amica", "Mark's the best thing that happened to me. well. second best")
    $ msg("sara", "What's the first?")
    $ msg("amica", "you, duh. best friend since forever")
    return


## --- A4: gossip (tifosa di Daniel) -------------------------------------------

label chat_amica_a4:
    $ msg("sara", "Ok, gossip. Roberta at work dyed her hair the same red as our boss.")
    return

label chat_amica_a4_1:
    $ msg("amica", "STOP. that's creepy. is it a cult? it sounds like a cult")
    sp "She's joking. Isn't she?"
    if ha_numero("daniel"):
        $ msg("amica", "also wait. I have better gossip. is Daniel texting you??")
        menu (screen="scelta_telefono"):
            "«Only about the novel.»":
                $ msg("sara", "Only about the novel.")
                $ msg("amica", "«the novel». sure. the hot rich boss is very interested in literature")
            "«Maybe. A little.»":
                $ msg("sara", "Maybe. A little.")
                $ caldo()
                $ interest("daniel", 1)
                $ msg("amica", "SARA. I need screenshots. all of them")
    else:
        menu (screen="scelta_telefono"):
            "«It's just a coincidence.»":
                $ msg("sara", "It's just a coincidence.")
                $ msg("amica", "nothing is a coincidence. trust me")
            "«Maybe it IS a cult.»":
                $ msg("sara", "Maybe it IS a cult.")
                $ caldo()
                $ msg("amica", "if they offer you a red hair dye, RUN")
    return

label chat_amica_a4_2:
    $ msg("amica", "I live for your office drama. it's better than TV")
    return


## --- A5: serie televisive ----------------------------------------------------

label chat_amica_a5:
    $ msg("sara", "What are you watching? I need a new series.")
    return

label chat_amica_a5_1:
    $ msg("amica", "the one with the married woman and the gardener. you'll LOVE it")
    $ msg("amica", "she's so bored and then... well. watch it")
    menu (screen="scelta_telefono"):
        "«Sounds a bit predictable.»":
            $ msg("sara", "Sounds a bit predictable.")
            $ msg("amica", "predictable and HOT. the best combination")
        "«I'll start it tonight.»":
            $ msg("sara", "I'll start it tonight.")
            $ caldo()
            $ msg("amica", "episode 3. trust me. watch it alone")
            $ segna("joanie_serie_giardiniere")
    return

label chat_amica_a5_2:
    $ msg("amica", "Mark falls asleep in the first five minutes of anything. I watch everything alone. it's tragic")
    return


## --- A6: abbigliamento -------------------------------------------------------

label chat_amica_a6:
    $ msg("sara", "Honest opinion. The red top or the white one for tomorrow?")
    return

label chat_amica_a6_1:
    $ msg("amica", "red. always red. why is this even a question")
    $ msg("amica", "the white one makes you look like you're going to confession")
    menu (screen="scelta_telefono"):
        "«The red one is a bit much for the office.»":
            $ msg("sara", "The red one is a bit much for the office.")
            $ msg("amica", "a bit much is the right amount")
        "«Red it is.»":
            $ msg("sara", "Red it is.")
            $ caldo()
            $ msg("amica", "YES. send a photo tomorrow")
    return

label chat_amica_a6_2:
    $ msg("amica", "seriously babe. you should dress for yourself. not for being invisible")
    return


## --- A7: programmi del weekend -----------------------------------------------

label chat_amica_a7:
    $ msg("sara", "Plans for the weekend?")
    return

label chat_amica_a7_1:
    $ msg("amica", "Saturday dinner with Mark's parents. pray for me")
    $ msg("amica", "Sunday free. brunch? you, me, mimosas")
    menu (screen="scelta_telefono"):
        "«Can't, Sunday is lunch with my parents.»":
            $ msg("sara", "Can't, Sunday is lunch with my parents.")
            $ msg("amica", "noooo. next week then. I'm writing it in blood")
        "«Brunch. Yes. Please.»":
            $ msg("sara", "Brunch. Yes. Please.")
            $ caldo()
            $ msg("amica", "bottomless mimosas. I'm booking")
    return

label chat_amica_a7_2:
    $ msg("amica", "and bring gossip. I want everything")
    return


## --- A8: piccoli problemi quotidiani -----------------------------------------

label chat_amica_a8:
    $ msg("sara", "The washing machine flooded the bathroom. I want to cry.")
    return

label chat_amica_a8_1:
    $ msg("amica", "noooo. is [nome_compagno] home?")
    menu (screen="scelta_telefono"):
        "«He's on his way. He'll fix it.»":
            $ msg("sara", "He's on his way. He'll fix it.")
            $ interest("josh", 1)
            $ msg("amica", "good. towels, babe. all the towels")
        "«Working late. As always.»":
            $ msg("sara", "Working late. As always.")
            $ caldo()
            $ msg("amica", "ugh. as always. ok I'm calling you, stay on the phone with me while you mop")
    return

label chat_amica_a8_2:
    $ msg("amica", "you know you can always call me. any hour. right?")
    $ msg("sara", "I know.")
    return


## --- B1: confidenze sulla coppia ---------------------------------------------

label chat_amica_b1:
    $ msg("sara", "Can I ask you something embarrassing?")
    return

label chat_amica_b1_entrata:
    $ msg("amica", "ok I need to know something. how are things with [nome_compagno]. REALLY")
    $ msg("sara", "Fine. Good. Why?")
    return

label chat_amica_b1_1:
    $ msg("amica", "is it still exciting? like, after all these years?")
    sp "I don't know how to answer that."
    menu (screen="scelta_telefono"):
        "«It's comfortable. Safe. I like safe.»":
            $ msg("sara", "It's comfortable. Safe. I like safe.")
            $ msg("amica", "safe is good. safe is... safe")
        "«Not like it used to be.»":
            $ msg("sara", "Not like it used to be.")
            $ caldo()
            $ corruption(1)
            $ msg("amica", "I KNEW IT. ok. we need to talk. seriously")
            $ segna("joanie_sa_della_noia")
    return

label chat_amica_b1_2:
    $ msg("amica", "listen. you deserve to feel wanted. like, really wanted. by someone who looks at you like you're on fire")
    $ msg("amica", "[nome_compagno] is lucky. someone is, anyway")
    sp "What does she mean, «someone is»?"
    return


## --- B2: le insicurezze di Sara ----------------------------------------------

label chat_amica_b2:
    $ msg("sara", "Do you think I'm boring? Be honest.")
    return

label chat_amica_b2_1:
    $ msg("amica", "WHAT. no. who told you that. I'll kill them")
    $ msg("amica", "you're the least boring person I know. you just hide it under seven layers of «sorry»")
    menu (screen="scelta_telefono"):
        "«I feel boring.»":
            $ msg("sara", "I feel boring.")
            $ msg("amica", "feelings lie. I don't")
        "«You always make me feel better.»":
            $ msg("sara", "You always make me feel better.")
            $ caldo()
            $ msg("amica", "that's my job. my favourite job")
    return

label chat_amica_b2_2:
    if percorso("simon").interest >= 10 or percorso("daniel").interest >= 7:
        $ msg("amica", "and from what I see, some people don't find you boring AT ALL")
        $ msg("sara", "Joanie...")
        $ msg("amica", "just saying ;)")
    else:
        $ msg("amica", "you just need someone to remind you who you are. luckily you have me")
    return


## --- B3: il desiderio di sentirsi belle (indizio) ----------------------------

label chat_amica_b3:
    $ msg("sara", "Do you ever look in the mirror and not recognise yourself?")
    return

label chat_amica_b3_1:
    $ msg("amica", "every morning before coffee lol")
    $ msg("amica", "why? what did you see?")
    menu (screen="scelta_telefono"):
        "«Someone tired.»":
            $ msg("sara", "Someone tired.")
            $ msg("amica", "then sleep more and let me do your makeup on saturday")
        "«Someone who wants to feel beautiful again.»":
            $ msg("sara", "Someone who wants to feel beautiful again.")
            $ caldo()
            $ msg("amica", "babe. you ARE. you're the most beautiful woman I know. objectively. I've checked")
    return

label chat_amica_b3_2:
    $ msg("amica", "sometimes I look at you and think, how does she not know")
    sp "Know what? That I'm pretty? Joanie is sweet."
    return


## --- B4: consigli su Jacob (dopo il suo ritorno) -----------------------------

label chat_amica_b4:
    $ msg("sara", "I can't stop thinking about seeing Jacob again. Is that bad?")
    return

label chat_amica_b4_entrata:
    $ msg("amica", "so. JACOB. we need to talk about JACOB")
    $ msg("sara", "There's nothing to talk about.")
    return

label chat_amica_b4_1:
    $ msg("amica", "girl. he looked at you like you were dessert")
    $ msg("amica", "and you looked at him like you hadn't eaten in four years")
    menu (screen="scelta_telefono"):
        "«He cheated on me, Joanie. Remember?»":
            $ msg("sara", "He cheated on me, Joanie. Remember?")
            $ confidence(1)
            $ msg("amica", "I know, I know. people change though. maybe")
        "«...Was it that obvious?»":
            $ msg("sara", "...Was it that obvious?")
            $ caldo()
            $ interest("ex", 1)
            $ msg("amica", "the whole bar noticed. it was HOT")
    return

label chat_amica_b4_2:
    $ msg("amica", "I'm not saying do anything. I'm saying it's ok to feel things. you're allowed")
    $ msg("amica", "and if you want to talk about it, I'm here. always. I'll never judge you")
    sp "Why is she so happy he's back?"
    return


## --- B5: la paura di cambiare vita (indizio) ---------------------------------

label chat_amica_b5:
    $ msg("sara", "Sometimes I think my life is already decided. Job, [nome_compagno], house. Forever.")
    return

label chat_amica_b5_1:
    $ msg("amica", "is that bad? or good?")
    menu (screen="scelta_telefono"):
        "«Good. It's what I wanted.»":
            $ msg("sara", "Good. It's what I wanted.")
            $ interest("josh", 1)
            $ msg("amica", "then I'm happy for you. really")
        "«I don't know anymore.»":
            $ msg("sara", "I don't know anymore.")
            $ caldo()
            $ msg("amica", "then it's not decided. nothing is decided until you say so")
    return

label chat_amica_b5_2:
    $ msg("amica", "whatever you decide. whatever happens. I'm there. always. even if it's crazy")
    $ msg("amica", "especially if it's crazy")
    sp "I don't know what I'd do without her."
    return
