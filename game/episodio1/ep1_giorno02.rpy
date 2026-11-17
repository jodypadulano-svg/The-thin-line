## =============================================================================
## EPISODE 1 — DAY 2 (Tuesday)
## =============================================================================
## Calendar: docs/mese-1.md, day 2. Simon scenes 1-2 (docs/personaggi/simon.md),
## Joanie as a catalyst (decisioni: «Joanie — profilo psicologico»).
## Draft for Jody's review. Game text in English (A11); comments in Italian.
## Le CG indicate (images/cg/ep1/d2_*.webp) non esistono ancora: finché mancano
## compare la didascalia [CG].

label ep1_d2:
    call nuovo_giorno(2, "Tuesday")
    call ep1_d2_redazione
    call ep1_d2_palestra
    call ep1_d2_sera
    return


## --- Lavoro: una giornata normale ---------------------------------------------

label ep1_d2_redazione:
    $ vai("redazione", "The newsroom — 12:30 p.m.")
    $ cg("Sara at her desk, stretching, a half-written review of a bakery on the screen", "images/cg/ep1/d2_01_scrivania.webp")

    n "A quiet morning. No doors banging, no one shouting her name across the room."
    n "Barbara's glass office stays closed. Somebody says she's out with the advertisers."
    sp "The bakery review is done. Four hundred words about croissants. Pulitzer, here I come."

    n "At half past twelve the newsroom starts to empty out for lunch."

    menu:
        sp "Lunch break."
        "Eat with the girls from the office.":
            $ cg("Lunch table in the break corner: Jessica chatting, Roberta listening and watching Sara", "images/cg/ep1/d2_02_pranzo_colleghe.webp")
            n "Jessica talks for forty minutes about a new lip gloss. Roberta listens to everything and says almost nothing."
            n "Every time Sara looks up, Roberta is already looking at her."
            sp "Nice. Normal. Completely normal."
        "Eat alone at her desk and write a page of the novel.":
            $ confidence(1, "Sara steals an hour for her novel.")
            $ cg("Sara alone at her desk with a sandwich, typing on a notebook, absorbed", "images/cg/ep1/d2_03_pranzo_scrive.webp")
            n "A sandwich, a notebook, and the empty newsroom all to herself."
            n "Chapter three doesn't move. But she writes a little scene for chapter five, and it's good. She knows it's good."
            sp "One page a day. That's how books get written, right?"
        "Send sweet messages to [nome_compagno].":
            $ interest("josh", 1, "A few sweet words in the middle of the day.")
            $ cg("Sara smiling at her phone, chin in her hand", "images/cg/ep1/d2_04_messaggi_josh.webp")
            n "{i}Thinking about you. And about the risotto. Mostly about you.{/i}"
            n "The answer comes in less than a minute: a heart, a bowl of rice, and «Good luck at the gym tonight, champion»."
            sp "Champion. He has no idea what's waiting for me."

    $ vai("redazione", "The newsroom — 5:00 p.m.")
    n "At five o'clock sharp, her phone buzzes. Joanie."
    n "{i}Downstairs. Don't make me come up there.{/i}"
    return


## --- Sera: la palestra (Simon 1 e 2) --------------------------------------------

label ep1_d2_palestra:
    $ vai("palestra", "The gym — 6:00 p.m.")
    $ cg("Women's locker room: Joanie holds up a tight sports top; Sara clutches her baggy t-shirt", "images/cg/ep1/d2_05_spogliatoio.webp")

    n "The locker room smells like deodorant and somebody else's ambition."
    n "Sara pulls a baggy old t-shirt out of her bag. Joanie looks at it the way people look at a car accident."
    ch "No. Absolutely not. What is that?"
    s "It's a t-shirt. People wear them to the gym. I checked."
    ch "It's a tent, Sara. You could go camping in it."
    n "Joanie digs in her own bag and pulls out a sports top. Small. Black. Very small."
    ch "Here. I brought you a spare. Trust me."
    ch "You've been hiding under clothes like that since college. Nobody here is going to bite you."

    menu:
        sp "That thing is basically a bra with ambitions."
        "Keep the baggy t-shirt.":
            s "I'll keep my tent, thank you. First day. Baby steps."
            ch "Fine. Baby steps. But it's coming with us next time."
            n "Joanie puts the top back in her bag. She doesn't seem disappointed. She seems patient."
        "Try on Joanie's top.":
            $ confidence(1, "Sara dares a little.")
            $ corruption(1, "Sara likes being looked at a little.")
            $ segna("ep1_top_joanie")
            $ cg("Sara in front of the locker room mirror in the tight black top, surprised by herself", "images/cg/ep1/d2_06_top_specchio.webp")
            n "Sara turns to the mirror. For a second she doesn't recognize the woman looking back."
            sp "Oh. Oh, wow. That's... a lot of me."
            ch "That's {i}exactly{/i} enough of you. See? You look amazing."
            sp "[nome_compagno] has never seen me like this. Nobody has."

    $ vai("palestra", "The gym — 6:15 p.m.")
    $ cg("Sara at the edge of the weight room, lost; Joanie beside her, completely at home", "images/cg/ep1/d2_07_ingresso.webp")
    ch "Breathe. Nobody bites."
    s "Joanie, everyone here is... sculpted."
    ch "And soon you will be too. More or less."

    n "Joanie elbows her and nods towards the trainers' desk."
    ch "And that is Simon. The reason I never skip a session."
    $ cg("Simon explaining an exercise to a client: not very tall, broad shoulders, dark hair, easy smile", "images/cg/ep1/d2_08_simon.webp")
    $ incontra("simon")
    sp "He's not very tall. But those arms..."
    sp "He's definitely more muscular than [nome_compagno]. Not that it matters."

    $ cg("Joanie leaning towards Sara with a sly grin", "images/cg/ep1/d2_09_joanie_ammicca.webp")
    menu:
        ch "So? Tell me he's not hot."
        "«Okay, he's a good-looking guy.»":
            $ nota_sara("simon", "A good-looking guy. She admits it without a problem.")
            s "Okay, fine. He's a good-looking guy."
            ch "See? I knew you still had eyes. Having a boyfriend doesn't make you blind."
        "«I'm here to work out, not to look.»":
            $ nota_sara("simon", "Good-looking, but she's not interested. Or so she says.")
            s "I'm here to work out, Joanie. Not to look."
            ch "Sure. And I come here for the treadmill."
            sp "I'm not saying he isn't. It's just none of my business."

    n "As if he'd heard his name, Simon looks up from the desk. He sees Joanie, waves, and then his eyes stop on Sara."
    if fatto("ep1_top_joanie"):
        n "Just for a moment. A professional, polite moment. But Sara feels it all the same, all over the very small black top."
    else:
        n "Just for a moment. A polite nod for the new girl in the big t-shirt."
    $ cg("Simon at the desk raising a hand in greeting, looking straight at Sara", "images/cg/ep1/d2_10_simon_saluta.webp")

    menu:
        sp "He's saying hello. To me."
        "Smile back at him.":
            $ interest("simon", 1, "Sara smiles back at him.")
            n "Sara smiles. Simon smiles back: a quick, open smile, like it costs him nothing."
            ch "Ooh. Look at you."
            s "It's called being polite, Joanie."
        "Give him a quick nod.":
            n "Sara gives him a small nod and looks away, suddenly very interested in her shoelaces."
            ch "Wow. Ice queen."

    $ tappa("simon", 1)

    ## Simon 2 — Joanie chiede a Simon di correggerle lo squat.
    $ vai("palestra", "The gym — 6:45 p.m.")
    $ cg("Sara red-faced and out of breath on a mat; Joanie fresh and smiling", "images/cg/ep1/d2_11_fiatone.webp")
    n "Half an hour later Sara can barely breathe. Joanie, on the other hand, has a plan."
    ch "Simon? Sorry... could you check my squat? I think I'm doing something wrong with my back."
    si "Sure. Show me."
    $ cg("Simon behind Joanie: one hand on her hip, the other between her shoulder blades, correcting her posture", "images/cg/ep1/d2_12_squat_joanie.webp")
    si "Chest up. Weight on your heels... like that. Good."
    ch "Like this? Are you sure?"
    n "Joanie laughs a little too much. Leans back a little too much."
    sp "Joanie has a boyfriend. Mark. Sweet, patient Mark. Three years together."
    sp "He's being professional, you can tell. But she..."

    menu:
        sp "Where does a correction end and a flirt begin?"
        "Look away: it's none of her business.":
            n "Sara turns towards the window and counts the cars in the parking lot."
            sp "That's Joanie's business. Not mine."
        "Keep watching.":
            $ corruption(1, "Sara asks herself a new question.")
            $ segna("ep1_guarda_joanie")
            $ cg("Close-up of Sara on the mat, watching, lips parted, cheeks flushed from the workout", "images/cg/ep1/d2_13_sara_guarda.webp")
            sp "One hand on her hip. One on her back. Is that how it's done?"
            sp "And what if it were my back?"

    $ cg("Simon turns to Sara and Joanie with a friendly smile, towel over his shoulder", "images/cg/ep1/d2_14_simon_sorride.webp")
    si "Great job, both of you. And you're new, right? Sara?"
    s "Sara. Yes. New and dying."
    si "If you need a hand with anything, just ask. That's what I'm here for."
    s "Thanks. For now I'm just trying to survive."
    si "Surviving is step one. Everything else comes later."
    $ nota_sara("simon", "He was kind with Joanie, and he didn't take advantage.")

    $ cg("Joanie, out of Simon's earshot, whispering to Sara with a satisfied smile", "images/cg/ep1/d2_15_joanie_sussurra.webp")
    ch "He remembered your name. After one hello. Just saying."
    s "He's a trainer, Joanie. Remembering names is his job."
    ch "Mm-hm."
    return


## --- Sera: a casa, l'invito alla cena aziendale ---------------------------------

label ep1_d2_sera:
    $ vai("casa", "Home — evening")
    $ cg("Sara collapsed on the sofa, gym bag on the floor; Josh laughing and handing her an ice pack", "images/cg/ep1/d2_16_divano_dolori.webp")
    c "So? Did you survive the gym?"
    s "I found muscles I didn't know I had. All of them hurt. Even the ones in my ears."
    c "I'm proud of you. Seriously."
    n "He sits on the arm of the sofa. He's smiling, but he keeps turning his phone over in his hands."
    $ cg("Josh sitting on the arm of the sofa, nervous, turning his phone in his hands", "images/cg/ep1/d2_17_josh_invito.webp")
    c "I've got news that will make you forget the pain. Tomorrow night there's the company dinner. And this year partners are invited too."
    s "So I'm finally meeting the famous boss?"
    c "Daniel. He's... a type. Difficult. But he's the one who matters. If I make a good impression, it's important for me."
    sp "I've never heard him talk about work with that face."

    menu:
        sp "A company dinner. With Daniel."
        "Be excited for him.":
            $ interest("josh", 1, "Sara is on his side.")
            s "Then we'll make a great impression. Both of us. I'll be the most charming partner in the room."
            c "You always are."
            n "He kisses her forehead and finally puts the phone down."
        "Say she's a bit worried about Daniel.":
            $ segna("ep1_preoccupata_daniel")
            s "Babe... every time you talk about him you look like you're going to the dentist."
            c "He's not that bad. He just likes to... test people."
            s "And what if he tests you in front of everyone?"
            c "Then I'll pass the test. Like always."
            sp "He said it like he was trying to convince himself."

    sp "Tomorrow night. Company dinner. I'll need something to wear."
    sp "And a body that doesn't hurt."
    return
