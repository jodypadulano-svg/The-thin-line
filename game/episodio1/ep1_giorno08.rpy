## =============================================================================
## EPISODE 1 — DAY 8 (Monday)
## =============================================================================
## Calendar: docs/mese-1.md, day 8. Work: focus on the piece or chat with Joanie.
## Evening: the gym. Joanie cancels at the last minute (I8: on purpose, revealed
## much later; here nothing shows). Enter alone (Simon 4 and 5, tappa Simon 3) or
## go home. Then home: tell [nome_compagno] about the session with Simon or not.
## Decisions 19-20/11 with Jody:
## - the keys: [nome_compagno] is already home, Sara rings the intercom as she
##   often does when he's in (no keys needed, she still doesn't notice);
## - Simon offers his number («text me»): save it (Simon +1, flag simon_numero,
##   da_numero) or «I'll ask Joanie» (he enters the phone book on day 15, Joanie's
##   «Gym squad» group);
## - if ep1_d7_josh_precoce: [nome_compagno] has cooked her favourite dinner and
##   is a little too attentive; nobody mentions Sunday night. No stats.
## Draft for Jody's review. Game text in English; comments in Italian.
## CG: docs/prompt-immagini/inquadrature-giorno-08.md. Finché mancano,
## compare la didascalia [CG].

label ep1_d8:
    call nuovo_giorno(8, "Monday")
    call ep1_d8_redazione
    call ep1_d8_palestra
    call ep1_d8_casa
    return


## --- Lavoro: il pezzo o Joanie ------------------------------------------------------

label ep1_d8_redazione:
    $ vai("redazione", "The newsroom — 10:40 a.m.")
    $ musica("redazione")
    $ ambiente("redazione")
    $ cg("The newsroom on a grey Monday morning: Sara at her desk with a coffee, the article on screen, her phone face-down beside the keyboard", "images/cg/ep1/d8_01_lunedi.webp")
    n "Monday. The coffee machine has broken down again, and the newsroom smells of burnt toast and other people's weekends."
    n "Sara has a piece due at four: three hundred words on the new cycle lanes. Nobody will read it. She wants it to be good anyway."
    $ suono("telefono_vibra")
    n "Her phone buzzes against the desk. Joanie, of course."
    n "{i}GYM TONIGHT. 6 PM. Simon said no excuses and I quote.{/i}"

    menu:
        sp "Three hundred words on cycle lanes. Or Joanie."
        "Focus on the piece.":
            $ confidence(1, "Sara turns three hundred dull words into something good.")
            n "She turns the phone over and doesn't touch it again until lunch."
            n "By half past twelve the cycle lanes have a beginning, a middle and an end, and one sentence she's genuinely proud of."
            sp "Nobody will read it. But it's good."
        "Chat with Joanie under the desk.":
            $ interest("amica", 1, "An hour of nonsense with Joanie.")
            $ cg("Sara hunched over her phone under the edge of the desk, biting her lip not to laugh, Barbara's office door closed in the background", "images/cg/ep1/d8_02_chat_joanie.webp")
            n "{i}Did you survive Sunday?{/i}"
            n "{i}Darius came round. With croissants.{/i}"
            n "{i}Darius is an angel. Tell him I said so. Actually don't, he'll be unbearable.{/i}"
            n "{i}Also: wear something cute tonight. Not the tent.{/i}"
            sp "I'm a professional journalist. I'm hiding under my desk."
            n "The cycle lanes get finished at five to four, in a hurry. They're fine. Just fine."
    return


## --- Sera: la palestra, Joanie dà buca (I8) ------------------------------------------

label ep1_d8_palestra:
    $ vai("strada", "Outside the gym — 5:55 p.m.")
    $ ambiente(None)
    $ musica(None)
    $ cg("Outside the gym at dusk: Sara with her gym bag on her shoulder, stopped under the neon sign, reading a message on her phone", "images/cg/ep1/d8_03_buca.webp")
    n "Sara is at the gym door, bag on her shoulder, when her phone buzzes."
    n "{i}SORRYSORRYSORRY. Something came up with Mark, I can't make it. Go anyway!!! Simon's expecting you 💪{/i}"
    sp "Alone. The first time I only survived because she was there."
    sp "And 'Simon's expecting you'? Since when does Simon expect anyone?"

    menu:
        sp "In, or home?"
        "Go in anyway.":
            $ segna("ep1_palestra_da_sola")
            $ confidence(3, "Sara walks into the gym on her own.")
            sp "I've paid for the membership. I'm going in."
            call ep1_d8_simon
        "Go home.":
            $ interest("josh", 1, "Sara chose the sofa, and him.")
            sp "Another time. Not tonight."
            n "She walks back to the bus stop with her bag still full of clean clothes, feeling a little guilty and a little relieved."
    return


label ep1_d8_simon:
    ## Simon 4 e 5, tappa Simon 3 (Complicità): si ricorda di lei.
    $ vai("palestra", "The gym — 6:05 p.m.")
    $ musica("palestra")
    $ ambiente("palestra")
    $ suono("armadietto")
    if fatto("ep1_top_joanie"):
        n "In the locker room she pulls out the black top. It never went back to Joanie, somehow. She puts it on before she can change her mind."
    else:
        n "In the locker room she pulls out her old t-shirt, looks at it for a long moment, and puts it on anyway. Baby steps."
    $ cg("The weight room: Simon turning from the trainers' desk with a wide smile as Sara walks in alone, bag in hand", "images/cg/ep1/d8_04_simon_saluta.webp")
    si "Hey! My athlete! All on your own tonight?"
    s "Joanie abandoned me."
    si "Then I'm adopting you for half an hour. If you want."
    if fatto("ep1_d6_parla_simon"):
        si "And it's Monday. I said no excuses, and here you are. I'm impressed."
        si "Still waiting for page fifty-one, by the way."
        sp "He remembers. He actually remembers."
    else:
        sp "He remembers me. He even remembers my name."
    si "Let's build you a proper beginner's plan, so next time you know exactly what to do. With or without Joanie."

    $ cg("Simon showing Sara how to hold a dumbbell, at a professional distance", tuta_d8("05_manubrio"))
    n "He shows her how to hold the dumbbell, standing at a professional distance, explaining each movement like it matters."
    si "Elbow close to your body. No rush. The movement matters more than the weight."
    s "That's what you said last time."
    si "And I'll say it every time until you stop rushing."
    si "Can I? Your shoulder's creeping up. Let me fix it."

    menu:
        "«Sure.»":
            $ interest("simon", 5, "Simon will remember this evening.")
            $ cg("Simon's hand lightly correcting Sara's shoulder as she lifts the dumbbell", tuta_d8("06_spalla"))
            n "His fingers move her shoulder down, barely. A quick, technical touch."
            sp "Joanie's right about one thing: he has sure hands."
            sp "But it's his job. Nothing more."
        "«Fix the other one too?», with a smile." (corruption=15):
            $ interest("simon", 6, "Simon noticed your smile.")
            $ corruption(3, "An innocent game. Almost.")
            $ cg("Simon's hand lightly correcting Sara's shoulder as she lifts the dumbbell", tuta_d8("06_spalla"))
            s "While you're at it... fix the other one too?"
            si "Yes, ma'am."
            n "This time his hands stay a second longer. Neither of them mentions it."
            sp "What am I doing?"
        "«I'll do it myself, thanks. Just tell me how.»":
            $ interest("simon", 3, "Simon respects your space.")
            si "No problem. Drop your shoulder... there. Perfect."
            $ nota_sara("simon", "He understood straight away that she'd rather not be touched.")

    $ vai("palestra", "The gym — 6:50 p.m.")
    $ cg("By the trainers' desk at the end of the session: Simon handing Sara a handwritten training plan, Sara red-faced and out of breath with her water bottle", tuta_d8("07_scheda"))
    n "Forty-five minutes later Sara can't feel her arms, and she's smiling like an idiot."
    si "Well done. Really. Here's your plan."
    n "He hands her a sheet of paper covered in neat handwriting. At the bottom, a phone number."
    si "If you've got questions about the exercises, text me. Anything. Even the stupid ones."
    si "Especially the stupid ones. Those are the ones people get hurt on."

    menu:
        sp "His number."
        "Save it.":
            $ interest("simon", 1, "Sara saved his number.")
            $ segna("simon_numero")
            $ da_numero("simon")
            n "She types it into her phone right there, under «Simon gym», so she doesn't lose the sheet."
            si "Good. Now I know you'll actually read the plan."
        "«Thanks. I'll ask Joanie.»":
            n "She folds the sheet and puts it in her bag."
            s "Thanks. I'll ask Joanie, she knows everything."
            si "Joanie knows a lot. Not everything."
            n "He says it with a grin, and lets it go."

    si "Wednesday? I'll be here. With or without Joanie."
    $ nota_sara("simon", "Funny. Kind. Remembers everything. End of story.")
    $ tappa("simon", 3)
    return


## --- Sera: a casa --------------------------------------------------------------------

label ep1_d8_casa:
    $ vai("casa", "Home — 7:40 p.m.")
    $ ambiente(None)
    $ musica("casa")
    if fatto("ep1_palestra_da_sola"):
        n "She climbs the stairs with legs like jelly and doesn't even look for her keys: the light is on behind the door, [nome_compagno] is home."
    else:
        n "She climbs the stairs without even looking for her keys: the light is on behind the door, [nome_compagno] is home."
    $ suono("citofono")
    n "She rings, two short buzzes, the way she always does when he's in. Faster than digging through the bag."
    c "It's open!"

    if fatto("ep1_d7_josh_precoce"):
        ## Il giorno dopo domenica notte: una traccia, mai detta (decisione 20/11).
        $ cg("The kitchen in the evening: the little table laid with candles and the good plates, Josh at the stove in an apron, turning towards Sara a little too eagerly", "images/cg/ep1/d8_08_cena_josh.webp")
        n "The flat smells of garlic and butter. The little kitchen table is laid properly: the good plates, two candles, the napkins folded into something that's trying to be a swan."
        c "Carbonara. The real one, no cream. Sit down, sit down, you must be starving."
        sp "My favourite. On a Monday."
        n "He pours her wine before she asks. He asks about her day and listens to every word. He laughs at the cycle lanes."
        n "Neither of them says anything about last night. It sits at the table with them anyway, quiet, polite, like a third guest."
        sp "Oh, love. You didn't have to."
        sp "But it's sweet that you did."
    else:
        $ cg("The living room in the evening: Josh on the sofa with his laptop, looking up and smiling as Sara comes in", "images/cg/ep1/d8_09_divano.webp")
        n "[nome_compagno] is on the sofa with his laptop, still half in work clothes, half in Monday."
        c "There she is. How was it?"

    if fatto("ep1_palestra_da_sola"):
        c "So? Did Joanie kill you?"
        s "Joanie didn't come. She bailed. Something with Mark."
        c "And you went in on your own? Look at you."
        menu:
            sp "And Simon spent forty-five minutes fixing my shoulders."
            "Tell [nome_compagno] about the session with Simon.":
                s "The trainer looked after me. Simon, the one from the bar. He made me a whole plan."
                c "The huge guy? That's nice of him."
                if fatto("ep1_d6_ride_simon"):
                    n "He says it lightly. Then he looks at his plate for a second longer than he needs to."
                else:
                    n "He says it lightly, and he means it."
                c "As long as he doesn't break you. I need you in one piece."
            "Don't mention it.":
                $ corruption(1, "Sara keeps a small thing to herself.")
                $ suspicion(1, "Something about the gym doesn't add up.")
                $ segna("ep1_d8_tace_simon")
                s "I did my best. My arms are gone. That's all I know."
                c "Who helped you with the machines?"
                s "Oh, there are people. Trainers. It's fine."
                sp "Why didn't I just say it? There's nothing to say."
                if fatto("ep1_d7_josh_precoce"):
                    sp "He has his silence tonight. And now I have mine."
    else:
        s "Joanie bailed on me, so I bailed on the gym."
        c "Good. The sofa missed you."
        if fatto("ep1_d7_josh_precoce"):
            n "He doesn't ask anything else. He just keeps filling her glass, and watching her like he's checking she's still there."

    n "Next door, Howard's television murmurs through the wall. Sara doesn't notice that she hasn't touched her keys in three days."
    return


init python:
    def tuta_d8(nome):
        """CG della palestra del giorno 8: variante «_top» se Sara ha il top di Joanie."""
        return "images/cg/ep1/d8_%s%s.webp" % (nome, "_top" if fatto("ep1_top_joanie") else "")
