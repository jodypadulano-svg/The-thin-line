## =============================================================================
## DARIUS (chiave "amico") — discorsi al telefono: introduzione, A, B
## =============================================================================
## Tono (Q&A 18/11/2026): COMPLETAMENTE LEALE A JOSH fino a C. In A e B è l'amico
## di sempre: battute, «lol», ricordi delle superiori con Josh. La svolta arriva
## come una sorpresa da C in poi. Percorso opt-in: senza le risposte calde di Sara
## le sue chat restano fra amici.

init python:
    discorso("amico_intro", "amico", ESTRANEI)
    discorso("amico_a1", "amico", CONOSCENTI)
    discorso("amico_a2", "amico", CONOSCENTI)
    discorso("amico_a3", "amico", CONOSCENTI)
    discorso("amico_a4", "amico", CONOSCENTI)
    discorso("amico_a5", "amico", CONOSCENTI)
    discorso("amico_a6", "amico", CONOSCENTI)
    discorso("amico_a7", "amico", CONOSCENTI)
    discorso("amico_a8", "amico", CONOSCENTI)
    discorso("amico_b1", "amico", CONFIDENZA)
    discorso("amico_b2", "amico", CONFIDENZA)
    discorso("amico_b3", "amico", CONFIDENZA)
    discorso("amico_b4", "amico", CONFIDENZA)
    discorso("amico_b5", "amico", CONFIDENZA)


## --- Introduzione: un messaggio amichevole su Josh ---------------------------

label chat_amico_intro:
    $ msg("sara", "Hey Darius, it's Sara. [nome_compagno]'s birthday is next month. Help me plan something?")
    return

label chat_amico_intro_entrata:
    $ msg("amico", "Sara! Secret mission. [nome_compagno]'s birthday. You in?")
    $ msg("sara", "Of course I'm in!")
    return

label chat_amico_intro_1:
    $ msg("amico", "Yes!! Finally someone organised. Last year I forgot and he still brings it up lol")
    $ msg("amico", "Ideas: surprise party, or the cabin trip he's been talking about since high school")
    menu (screen="scelta_telefono"):
        "«The cabin. He'd love that.»":
            $ msg("sara", "The cabin. He'd love that.")
            $ interest("josh", 1)
            $ msg("amico", "Cabin it is. I'll handle the boys, you handle him")
        "«A party. With everyone.»":
            $ msg("sara", "A party. With everyone.")
            $ caldo()
            $ msg("amico", "Party! I'll bring the embarrassing photos. All of them")
    $ segna("darius_compleanno_josh")
    return

label chat_amico_intro_2:
    $ msg("amico", "He's lucky to have you, you know. Always says so")
    $ msg("amico", "Ok, top secret from now on. Delete this chat lol")
    return


## --- A1: amici comuni --------------------------------------------------------

label chat_amico_a1:
    $ msg("sara", "Who's the guy [nome_compagno] keeps calling «Big Phil»?")
    return

label chat_amico_a1_1:
    $ msg("amico", "Lol. Phil. He's 1 metre 60. Hence Big Phil")
    $ msg("amico", "High school. The three of us were inseparable. Phil, me and your man")
    menu (screen="scelta_telefono"):
        "«I need to meet this legend.»":
            $ msg("sara", "I need to meet this legend.")
            $ caldo()
            $ msg("amico", "You will. He does magic tricks. Badly. Prepare yourself")
        "«[nome_compagno] never told me about him.»":
            $ msg("sara", "[nome_compagno] never told me about him.")
            $ msg("amico", "Probably because of the prom story. Ask him about the prom. Watch his face")
    return

label chat_amico_a1_2:
    $ msg("amico", "We should all get together. Like a proper reunion. You'd fit right in")
    return


## --- A2: ricordi delle superiori ---------------------------------------------

label chat_amico_a2:
    $ msg("sara", "Ok, I asked [nome_compagno] about the prom. He turned red and left the room. Tell me.")
    return

label chat_amico_a2_1:
    $ msg("amico", "LOL. He did the same face?? Classic")
    $ msg("amico", "Ok. He rented a white suit. Spilled a whole cherry punch on it in the first ten minutes")
    $ msg("amico", "He spent the night telling everyone it was «a design»")
    menu (screen="scelta_telefono"):
        "«Oh no. Poor thing :)»":
            $ msg("sara", "Oh no. Poor thing :)")
            $ interest("josh", 1)
            $ msg("amico", "Poor thing danced all night anyway. That's your man")
        "«I'm going to tease him forever.»":
            $ msg("sara", "I'm going to tease him forever.")
            $ caldo()
            $ msg("amico", "Please do. I've been doing it alone for fifteen years")
    return

label chat_amico_a2_2:
    $ msg("amico", "He was the nicest guy in school. Still is. Don't tell him I said that")
    return


## --- A3: musica --------------------------------------------------------------

label chat_amico_a3:
    $ msg("sara", "What was that band you and [nome_compagno] had in high school? He refuses to tell me.")
    return

label chat_amico_a3_1:
    $ msg("amico", "Oh no. He told you about the band??")
    $ msg("amico", "We were called «The Lost Socks». I was on drums. He sang. Terribly")
    menu (screen="scelta_telefono"):
        "«The Lost Socks! I'm dying.»":
            $ msg("sara", "The Lost Socks! I'm dying.")
            $ caldo()
            $ msg("amico", "We had ONE fan. His mum")
        "«He sings in the shower. Still terribly.»":
            $ msg("sara", "He sings in the shower. Still terribly.")
            $ interest("josh", 1)
            $ msg("amico", "Some things never change lol")
    return

label chat_amico_a3_2:
    $ msg("amico", "I might still have a recording. Price: one homemade dinner")
    menu (screen="scelta_telefono"):
        "«Deal. Come on Saturday.»":
            $ msg("sara", "Deal. Come on Saturday.")
            $ caldo()
            $ msg("amico", "I'll bring the tape. And wine")
            $ segna("darius_cena_sabato")
        "«I'll make [nome_compagno] cook. Deal.»":
            $ msg("sara", "I'll make [nome_compagno] cook. Deal.")
            $ msg("amico", "Then I'm bringing antacids too lol")
    return


## --- A4: serate in compagnia -------------------------------------------------

label chat_amico_a4:
    $ msg("sara", "Thanks for last night. [nome_compagno] was so happy. He laughed more than he has in weeks.")
    return

label chat_amico_a4_1:
    $ msg("amico", "Anytime! He needs to get out more. Work is eating him alive")
    $ msg("amico", "His boss sounds like a nightmare honestly")
    menu (screen="scelta_telefono"):
        "«He is. Daniel is awful to him.»":
            $ msg("sara", "He is. Daniel is awful to him.")
            $ interest("josh", 1)
            $ msg("amico", "I'd love five minutes alone with that guy. Just to talk. Mostly")
        "«He'll be fine. He's strong.»":
            $ msg("sara", "He'll be fine. He's strong.")
            $ msg("amico", "He is. Stronger than he looks. Always was")
    return

label chat_amico_a4_2:
    $ msg("amico", "Let's do it more often. The three of us. Board games, pizza, bad movies")
    menu (screen="scelta_telefono"):
        "«Every Friday?»":
            $ msg("sara", "Every Friday?")
            $ caldo()
            $ msg("amico", "Every Friday. It's a tradition now. No backing out")
        "«When we can.»":
            $ msg("sara", "When we can.")
            $ msg("amico", "Deal")
    return


## --- A5: Josh da ragazzo -----------------------------------------------------

label chat_amico_a5:
    $ msg("sara", "What was [nome_compagno] like at sixteen?")
    return

label chat_amico_a5_1:
    $ msg("amico", "Skinny. Glasses. Always reading comics. Too polite to tell a girl he liked her")
    $ msg("amico", "Once he waited outside a girl's house for an hour with flowers and then went home. Didn't knock")
    menu (screen="scelta_telefono"):
        "«That's so sweet.»":
            $ msg("sara", "That's so sweet.")
            $ interest("josh", 1)
            $ msg("amico", "That's him. All heart, zero courage lol")
        "«He waited and didn't knock? Why?»":
            $ msg("sara", "He waited and didn't knock? Why?")
            $ caldo()
            $ msg("amico", "Said he «didn't want to bother her». I knocked for him next time")
            sp "Darius knocked for him."
    return

label chat_amico_a5_2:
    $ msg("amico", "With you he finally found the courage. You changed him. For the better")
    return


## --- A6: videogiochi ---------------------------------------------------------

label chat_amico_a6:
    $ msg("sara", "Why did [nome_compagno] stay up until 3 playing with you? He was a zombie at breakfast.")
    return

label chat_amico_a6_1:
    $ msg("amico", "Guilty lol. Online tournament. We came second!")
    $ msg("amico", "Ok, eleventh. But it FELT like second")
    menu (screen="scelta_telefono"):
        "«Next time send him to bed at midnight.»":
            $ msg("sara", "Next time send him to bed at midnight.")
            $ interest("josh", 1)
            $ msg("amico", "Yes ma'am. I'll set an alarm")
        "«Teach me. I want to beat you both.»":
            $ msg("sara", "Teach me. I want to beat you both.")
            $ caldo()
            $ msg("amico", "Oh it's ON. Saturday. Bring snacks and your worst attitude")
    return

label chat_amico_a6_2:
    $ msg("amico", "He talks about you between rounds, you know. Embarrassing. Very sweet")
    return


## --- A7: programmi del weekend -----------------------------------------------

label chat_amico_a7:
    $ msg("sara", "Any plans this weekend?")
    return

label chat_amico_a7_1:
    $ msg("amico", "Football Saturday. Sunday: fixing my bike, which I've been saying for six months")
    $ msg("amico", "You two? Still the sofa marathon?")
    menu (screen="scelta_telefono"):
        "«Sofa marathon. Season four.»":
            $ msg("sara", "Sofa marathon. Season four.")
            $ msg("amico", "Respect. No spoilers")
        "«We need new plans. Ideas?»":
            $ msg("sara", "We need new plans. Ideas?")
            $ caldo()
            $ msg("amico", "Lake trail on Sunday. I'll bring the frisbee. [nome_compagno] can't catch, it's hilarious")
    return

label chat_amico_a7_2:
    $ msg("amico", "Seriously, call me whenever you two are bored. I'm always free. Sadly lol")
    return


## --- A8: abitudini quotidiane ------------------------------------------------

label chat_amico_a8:
    $ msg("sara", "Random question. Are you a morning person?")
    return

label chat_amico_a8_1:
    $ msg("amico", "Gym at 6. Shower. Coffee. Work. I'm annoyingly organised")
    $ msg("amico", "Unlike someone we both know who hits snooze five times")
    menu (screen="scelta_telefono"):
        "«Six times. I counted.»":
            $ msg("sara", "Six times. I counted.")
            $ caldo()
            $ msg("amico", "SIX. I'm telling him you snitched")
        "«He's not a morning person. It's cute.»":
            $ msg("sara", "He's not a morning person. It's cute.")
            $ interest("josh", 1)
            $ msg("amico", "Cute is one word for it lol")
    return

label chat_amico_a8_2:
    $ msg("amico", "You're a morning person, right? You look like one. Up at dawn, tea, notebook")
    sp "Exactly that. How does he know?"
    return


## --- B1: il rapporto con Josh ------------------------------------------------

label chat_amico_b1:
    $ msg("sara", "Can I ask you something serious? Is [nome_compagno] ok? He seems down lately.")
    return

label chat_amico_b1_entrata:
    $ msg("amico", "Hey. Is [nome_compagno] ok? He was quiet at football")
    $ msg("sara", "I was going to ask you the same thing.")
    return

label chat_amico_b1_1:
    $ msg("amico", "It's work. That Daniel guy is getting into his head")
    $ msg("amico", "He doesn't say it, but I know him. Fifteen years. He's my brother")
    menu (screen="scelta_telefono"):
        "«What can I do?»":
            $ msg("sara", "What can I do?")
            $ interest("josh", 1)
            $ msg("amico", "Just be there. He'd walk through fire for you. He needs to know you're behind him")
        "«I don't know how to help him.»":
            $ msg("sara", "I don't know how to help him.")
            $ caldo()
            $ msg("amico", "We'll figure it out. Together. That's what we do")
    return

label chat_amico_b1_2:
    $ msg("amico", "I'll take him out Thursday. Beers, darts, no talking about work")
    $ msg("amico", "Whatever he needs. Always")
    return


## --- B2: i lati meno conosciuti di Darius ------------------------------------

label chat_amico_b2:
    $ msg("sara", "You always look after everyone. Who looks after you?")
    return

label chat_amico_b2_1:
    $ msg("amico", "...Wow. Nobody's asked me that in a while")
    $ msg("amico", "I'm fine. I like being the one who fixes things. Keeps my head busy")
    menu (screen="scelta_telefono"):
        "«You're allowed to need people too.»":
            $ msg("sara", "You're allowed to need people too.")
            $ caldo()
            $ msg("amico", "Look at you, giving advice. [nome_compagno] said you were wise. He was right")
        "«Well, you have us.»":
            $ msg("sara", "Well, you have us.")
            $ msg("amico", "I know. Best thing I've got")
    return

label chat_amico_b2_2:
    $ msg("amico", "Truth? My dad left when I was ten. I promised myself I'd never leave anyone. Never")
    sp "I never knew that."
    $ segna("darius_padre")
    return


## --- B3: le qualità che Sara apprezza negli uomini ---------------------------

label chat_amico_b3:
    $ msg("sara", "How did the date go? [nome_compagno] said you had a date!")
    return

label chat_amico_b3_1:
    $ msg("amico", "Lol. Disaster. She talked about her ex for two hours")
    $ msg("amico", "Help me out. What do women actually want? Be honest")
    menu (screen="scelta_telefono"):
        "«Someone kind. Who listens.»":
            $ msg("sara", "Someone kind. Who listens.")
            $ msg("amico", "Kind and listens. So, [nome_compagno]. Got it lol")
        "«Someone who makes them feel safe. And a bit dangerous.»" (confidence=25):
            $ msg("sara", "Someone who makes them feel safe. And a bit dangerous.")
            $ caldo()
            $ msg("amico", "Safe AND dangerous. That's a hard combo. Writing it down")
    return

label chat_amico_b3_2:
    $ msg("amico", "Thanks Sara. Seriously. If I find someone half as good as you, I'll be happy")
    $ msg("amico", "[nome_compagno] won the lottery, I keep telling him")
    return


## --- B4: come cambia un'amicizia ---------------------------------------------

label chat_amico_b4:
    $ msg("sara", "Do you miss how things were before I came along? You and [nome_compagno], every day.")
    return

label chat_amico_b4_1:
    $ msg("amico", "Honestly? A little. But not in a bad way")
    $ msg("amico", "He grew up. You're good for him. And I got a friend out of it too")
    menu (screen="scelta_telefono"):
        "«I'm glad you see me as a friend.»":
            $ msg("sara", "I'm glad you see me as a friend.")
            $ caldo()
            $ msg("amico", "Course I do. You're family now. Both of you")
        "«I never want to come between you two.»":
            $ msg("sara", "I never want to come between you two.")
            $ interest("josh", 1)
            $ msg("amico", "You never could. Nobody could")
    return

label chat_amico_b4_2:
    $ msg("amico", "Friendships change. The good ones get bigger, not smaller. That's ours")
    return


## --- B5: sentirsi a proprio agio insieme -------------------------------------

label chat_amico_b5:
    $ msg("sara", "It's funny. I can talk to you about anything. Even more than with some of my friends.")
    return

label chat_amico_b5_1:
    $ msg("amico", "Same here. You're easy to talk to. No pretending")
    $ msg("amico", "[nome_compagno] and you are the only people I don't have to perform for")
    menu (screen="scelta_telefono"):
        "«That means a lot.»":
            $ msg("sara", "That means a lot.")
            $ caldo()
            $ msg("amico", "It's true. Don't make it weird lol")
        "«We're lucky to have you.»":
            $ msg("sara", "We're lucky to have you.")
            $ interest("josh", 1)
            $ msg("amico", "Other way round. Always")
    return

label chat_amico_b5_2:
    $ msg("amico", "Goodnight Sara. Tell your man I said hi. And that he still owes me twenty bucks")
    return
