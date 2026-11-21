## =============================================================================
## EPISODE 1 — DAY 1 (Monday)
## =============================================================================
## Calendar: docs/mese-1.md, day 1. Threads: I21, I22.
## Draft for Jody's review. Game text in English (A11); comments in Italian.
## Immagini: campo e controcampo secondo docs/prompt-immagini/inquadrature-giorno-01.md
## (A1-G2, 28 CG in images/cg/ep1/d1_*.webp).

label ep1_d1:
    call nuovo_giorno(1, "Monday")
    call ep1_d1_mattina
    call ep1_d1_redazione
    call ep1_d1_sera
    return


## --- Prima del lavoro --------------------------------------------------------

label ep1_d1_mattina:
    $ vai("camera", "Home — 7:40 a.m.")
    $ ambiente(None)
    $ musica("casa")
    $ suono("sveglia")
    ## A1
    $ cg("Sara in front of the open wardrobe, hair still damp, holding two blouses", "images/cg/ep1/d1_01_armadio.webp")

    n "The alarm went off twenty minutes ago. Sara has spent fifteen of them staring at the same two blouses."
    sp "The white one or the white one. Wow, Sara. Living on the edge."

    $ suono("rasoio")
    n "From the bathroom comes the sound of an electric razor, then a voice slightly muffled by foam."
    c "Babe, have you seen my blue tie?"
    s "Second drawer. Under the grey one you never wear."
    c "You're a genius."
    s "I'm a woman who folds laundry. It's not the same thing."

    ## A2
    $ cg("Sara in the mirror, fingers stopped on the top button of her blouse", "images/cg/ep1/d1_01b_specchio.webp")
    n "She picks the plain white blouse and buttons it in front of the mirror."
    n "Her fingers stop at the last button, the one at the collar."

    menu:
        sp "All the way up, like every Monday?"
        "Button it all the way up.":
            sp "All the way up. Nobody reads the culture page for the journalist's collarbones."
        "Leave one button open. She feels pretty today.":
            ## A3
            $ cg("Sara smiles shyly at her reflection, top button open", "images/cg/ep1/d1_01c_un_bottone.webp")
            $ confidence(1, "Sara likes what she sees in the mirror.")
            sp "One button. That's all. Today I feel... nice."
            sp "Is that allowed on a Monday?"

    ## A4
    $ cg("Josh in the doorway kisses Sara on the temple while she buttons her blouse", "images/cg/ep1/d1_02_bacio_tempia.webp")
    n "[nome_compagno] appears in the doorway, tie finally knotted, and kisses her on the temple."
    c "You look great. Go and conquer the world."
    s "The world. Or at least page twenty-six."
    c "Page twenty-six is lucky to have you."
    ## A5
    $ cg("Josh halfway down the stairs shouts up; Sara laughs at the door", "images/cg/ep1/d1_02b_love_you_scale.webp")
    n "He's already halfway down the stairs when he shouts back:"
    c "Love you!"
    s "Love you more!"
    sp "Every single morning. He never forgets."
    return


## --- In redazione (I21, I22) ----------------------------------------------------

label ep1_d1_redazione:
    $ vai("redazione", "The newsroom — 9:05 a.m.")
    $ musica("redazione")
    $ ambiente("redazione")
    ## B1
    $ cg("An open-plan newsroom: Sara at a small desk near the window", "images/cg/ep1/d1_03_scrivania.webp")

    n "The newsroom smells like coffee and printer toner. Sara has worked here for eight months, and she still hasn't written a single article she'd show to her mother."
    sp "Restaurant reviews. Local fairs. «Ten ways to enjoy the autumn.»"
    sp "One day I'll write something real. One day."

    $ suono("porta_sbattuta")
    n "She has barely turned on her computer when a door bangs open at the end of the room."
    n "Every head in the newsroom drops a little lower over its keyboard."

    ## B2
    $ cg("Barbara bursts out of her glass office pointing at Sara; the colleagues duck over their keyboards", "images/cg/ep1/d1_04_barbara_entra.webp")
    $ incontra("capa")
    $ musica("barbara")
    ba "SARA!"
    n "Barbara. The owner of the newspaper. She doesn't walk through the newsroom: she sails through it, like a ship that never learned to brake."
    ba "Darling. The piece on the cheese festival."
    ## B4
    $ cg("Sara looks up from her desk, embarrassed", "images/cg/ep1/d1_03b_sara_imbarazzo.webp")
    s "Yes?"
    ## B3
    $ cg("Barbara at Sara's desk waving a printed page, glasses on the tip of her nose", "images/cg/ep1/d1_04d_barbara_foglio.webp")
    ba "«Grated with love.» You wrote «grated with love» in the subtitle."
    ba "We are a newspaper, sweetheart. Not a greeting card."

    ## B4
    $ cg("Sara looks up from her desk, embarrassed", "images/cg/ep1/d1_03b_sara_imbarazzo.webp")
    menu:
        sp "Here we go."
        "Apologize right away.":
            s "I'm sorry. I'll change it right now."
            $ cg("Barbara at Sara's desk waving a printed page", "images/cg/ep1/d1_04d_barbara_foglio.webp")
            ba "Of course you will."
        "Explain calmly: it was the editor's suggestion.":
            $ confidence(1)
            s "It was the copy desk's line, actually. I wanted «Aged to perfection», but they said it sounded like a wine ad."
            $ cg("Barbara at Sara's desk waving a printed page", "images/cg/ep1/d1_04d_barbara_foglio.webp")
            ba "The copy desk has the poetic sensibility of a parking meter. Next time, trust yourself."
            $ cg("Sara looks up from her desk, embarrassed", "images/cg/ep1/d1_03b_sara_imbarazzo.webp")
            sp "Was that... a compliment?"
        "A joke: «At least nobody will forget it.»":
            $ confidence(1)
            $ interest("capa", 1, "Barbara likes a girl with a tongue.")
            s "Well, at least nobody's going to forget it."
            n "For a moment the whole newsroom holds its breath."
            ## B5
            $ cg("Barbara throws her head back laughing; the colleagues peek in disbelief", "images/cg/ep1/d1_04c_barbara_ride.webp")
            n "Then Barbara laughs: a big, theatrical laugh that makes the glass walls tremble."
            ba "Cheeky! I like it. Change it anyway."

    n "Barbara is already turning away. Then she stops, and looks at Sara again. Slowly. From top to bottom."
    ## B6
    $ cg("Barbara leans on Sara's desk and looks her over; Sara blushes, a colleague giggles", "images/cg/ep1/d1_04b_barbara_scollatura.webp")
    ba "And darling... one more thing."
    ba "With what you've been given, you could stop dressing like a nun at a funeral."
    ba "A little neckline never hurt anyone's career. Trust me."
    n "Somewhere behind a monitor, someone giggles."

    menu:
        sp "Did she really just say that? In front of everyone?"
        "Blush and close her blouse with one hand.":
            ## B7
            $ cg("Sara blushes, clutching the collar of her blouse; a colleague giggles", "images/cg/ep1/d1_04e_sara_arrossisce.webp")
            n "Sara's hand goes to her collar on its own. Her cheeks are burning."
            sp "Great. Now everyone's looking."
        "Pretend she didn't hear.":
            $ cg("Sara at her desk staring at the monitor", "images/cg/ep1/d1_03_scrivania.webp")
            n "Sara stares at her screen as if the cheese festival were the most fascinating thing in the world."
        "«Thanks... I think.»":
            $ interest("capa", 1)
            $ cg("Sara looks up from her desk, embarrassed", "images/cg/ep1/d1_03b_sara_imbarazzo.webp")
            s "Thanks... I think?"
            $ cg("Barbara looks Sara over", "images/cg/ep1/d1_04b_barbara_scollatura.webp")
            ba "You're welcome, darling. I always think."

    $ vai("redazione", "The newsroom — 10:30 a.m.")
    $ musica("redazione")
    $ suono("tazza")
    ## C1
    $ cg("Roberta brings Sara a cappuccino with cinnamon, smiling a little too wide", "images/cg/ep1/d1_05_roberta_cappuccino.webp")
    n "Half an hour later a cup of coffee appears next to her keyboard. Cappuccino, no sugar, a little cinnamon on top."
    n "Exactly how she likes it. She has never told anyone how she likes it."
    ro "For you. Don't let Barbara scare you, she's a sweetheart, really. She just... notices people."
    s "Thank you, Roberta. How did you know about the cinnamon?"
    ## C2
    $ cg("Close-up of Roberta, sweet smile a little too wide, staring", "images/cg/ep1/d1_05b_roberta_sguardo.webp")
    $ musica("stranezza")
    ro "Oh, I notice people too."
    ## C3
    $ cg("Roberta back at her desk outside Barbara's office, looking back over her shoulder", "images/cg/ep1/d1_05c_roberta_al_suo_posto.webp")
    n "Roberta keeps smiling at her for a second too long. Then she goes back to her desk, right outside Barbara's glass office."
    sp "Okay. That was sweet. And a little weird."

    $ vai("redazione", "The newsroom — 1:00 p.m.")
    $ suono("macchinetta_caffe")
    ## D1
    $ cg("Jessica at the coffee machine taps Sara's nose; an old novel sticks out of her pink bag", "images/cg/ep1/d1_06_jessica_naso.webp")
    je "Saaaara! You look so cute today!"
    ## D2
    $ cg("Flashback: the shy, bookish Jessica of three months ago talking with Sara over a novel", "images/cg/ep1/d1_06b_jessica_ricordo.webp")
    n "Jessica. Sara remembers Jessica's first week here, three months ago: a quiet girl with thick glasses and a battered copy of a Russian novel always in her bag."
    n "They had spent a whole lunch break arguing about whether Anna Karenina was a victim or a heroine. Jessica had won."
    ## D4
    $ cg("Sara holding her paper cup, puzzled", "images/cg/ep1/d1_06d_sara_perplessa.webp")
    sp "Now she talks like that. Dresses like that. And she hasn't opened a book since... since when?"
    s "Thanks, Jess. You look... different. Again."
    ## D3
    $ cg("Close-up of Jessica, glossy lips, dreamy vacant smile", "images/cg/ep1/d1_06c_jessica_sognante.webp")
    je "I know, right? I feel amazing. Something happened to me, Sara. Something really, really good."
    $ cg("Sara holding her paper cup, puzzled", "images/cg/ep1/d1_06d_sara_perplessa.webp")
    s "Something like what?"
    $ cg("Close-up of Jessica, dreamy vacant smile", "images/cg/ep1/d1_06c_jessica_sognante.webp")
    je "Mmh... I can't tell you. Not yet."
    ## D1
    $ cg("Jessica taps Sara's nose", "images/cg/ep1/d1_06_jessica_naso.webp")
    n "She giggles and taps the tip of Sara's nose with a long pink nail."
    je "But you should try it too. You'd be so much happier. Everyone would be so happy for you."
    $ cg("Sara holding her paper cup, puzzled", "images/cg/ep1/d1_06d_sara_perplessa.webp")
    sp "Try {i}what{/i}?"

    $ cg("Close-up of Jessica, dreamy vacant smile", "images/cg/ep1/d1_06c_jessica_sognante.webp")
    je "Oh! Thursday after work we're having drinks, just us girls. You have to come. Pleeease?"

    $ cg("Sara holding her paper cup, puzzled", "images/cg/ep1/d1_06d_sara_perplessa.webp")
    menu:
        sp "Drinks with the girls from the office."
        "Accept.":
            $ segna("ep1_aperitivo_accettato")
            s "Sure. Why not?"
            $ cg("Close-up of Jessica, dreamy vacant smile", "images/cg/ep1/d1_06c_jessica_sognante.webp")
            je "Yay! Roberta's going to be so happy. Everyone's going to be so happy!"
            $ cg("Sara holding her paper cup, puzzled", "images/cg/ep1/d1_06d_sara_perplessa.webp")
            sp "Why would everyone be so happy?"
        "Decline politely.":
            s "I'm not sure I can make it on Thursday, Jess. Maybe next time."
            $ cg("Close-up of Jessica, dreamy vacant smile", "images/cg/ep1/d1_06c_jessica_sognante.webp")
            je "Oh. Okay! Next time, then. There's always a next time."
            n "She says it like a promise."

    $ vai("redazione", "The newsroom — 4:55 p.m.")
    $ musica("redazione")
    ## E1
    $ cg("Golden late-afternoon light: Sara leaves her desk at five o'clock sharp", "images/cg/ep1/d1_07_le_17.webp")
    n "The afternoon passes between a review of a new bakery and three different versions of a headline about the cheese festival."
    n "At five o'clock sharp, Sara grabs her bag and doesn't look back."
    return


## --- La sera: il prologo --------------------------------------------------------

label ep1_d1_sera:
    $ vai("casa", "Home — evening")
    $ ambiente(None)
    $ musica("casa")
    ## F1
    $ cg("Sara at the table by the window, laptop open, a cup of tea going cold beside her", "images/cg/ep1/d1_08_capitolo_tre.webp")

    sp "Chapter three. Still chapter three."
    sp "My heroine has to open that door, and I still don't know what's on the other side."
    n "Sara deletes the last sentence. Then types it again, word for word."

    $ suono("chiave_serratura")
    n "A key turns in the lock."
    ## F2
    $ cg("Josh comes home and kisses the top of Sara's head; she laughs", "images/cg/ep1/d1_09_josh_rientra.webp")
    c "I'm home! Please tell me there's something left to eat, I'm starving."
    s "There's leftover pasta. And a writer in crisis, if you're interested."
    c "I'm always interested in the writer."
    n "He kisses the top of her head and leans over to read the screen."
    ## F3
    $ cg("Josh reads over Sara's shoulder; she covers the screen, pretending to be offended", "images/cg/ep1/d1_09b_josh_legge.webp")
    c "Chapter three?"
    s "Don't say it in that tone."
    c "What tone? I'll read it when it's finished. First signed copy, remember?"
    ## F2
    $ cg("Josh kisses the top of Sara's head; she laughs", "images/cg/ep1/d1_09_josh_rientra.webp")
    sp "He believes in me more than I do. He always has."

    menu:
        sp "And tonight..."
        "Close the laptop and spend the evening with him." (josh=30):
            ## F4
            $ cg("Sara and Josh on the sofa under the throw, bowls of pasta, laughing", "images/cg/ep1/d1_10_divano_pasta.webp")
            $ interest("josh", 3, "Sara chooses him tonight.")
            s "Enough chapter three. Couch and pasta?"
            c "I'd marry you just for that sentence."
            s "You'd marry me for leftover pasta?"
            c "I'd marry you for leftover anything."
        "Write for one more hour: inspiration just arrived.":
            ## F5
            $ cg("Sara types, inspired; Josh quietly brings her a cup of tea", "images/cg/ep1/d1_10b_scrive_te.webp")
            $ confidence(2, "Sara believes a little more in her novel.")
            $ segna("ep1_prologo_scrive")
            s "Give me an hour. I think I know what's behind the door."
            c "Go. I'll heat up the pasta and bring you a hot tea."
            n "When he comes back with the tea, she doesn't even notice. She's typing fast, for the first time in weeks."

    menu:
        sp "Dinner."
        "Cook something nice for him.":
            ## F6
            $ cg("Sara stirs a risotto; Josh hugs her from behind", "images/cg/ep1/d1_10c_risotto.webp")
            $ interest("josh", 1)
            $ suono("sobbollire")
            n "Sara puts the pasta back in the fridge and makes the risotto he likes, the one that takes forty minutes of stirring."
            c "What did I do to deserve this?"
            s "You came home."
        "Order a pizza.":
            ## F4
            $ cg("Sara and Josh on the sofa under the throw, laughing", "images/cg/ep1/d1_10_divano_pasta.webp")
            n "Pizza on the couch, a bad movie, his feet on the coffee table. A perfect Monday."

    $ vai("camera", "Home — night")
    $ musica("notte")
    ## G1
    $ cg("Night, bedside lamp: Sara on the bed on the phone, laughing; Josh asleep", "images/cg/ep1/d1_11_telefonata_joanie.webp")
    $ suono("telefono_vibra")
    n "It's almost eleven when Sara's phone lights up. Joanie."
    ch "Tomorrow. Gym. No excuses."
    s "Joanie, it's eleven o'clock at night."
    ch "Exactly. The perfect time for life-changing decisions. I already signed you up, by the way. First session's free."
    ## G2
    $ cg("Close-up of Sara on the phone, rolling her eyes and laughing", "images/cg/ep1/d1_11b_telefonata_primo_piano.webp")
    s "You signed me up without asking?"
    ## G1
    $ cg("Sara on the bed on the phone; Josh asleep", "images/cg/ep1/d1_11_telefonata_joanie.webp")
    ch "I signed you up {i}for{/i} you. That's different. Six o'clock. I'll pick you up."

    ## G2
    $ cg("Close-up of Sara on the phone, rolling her eyes and laughing", "images/cg/ep1/d1_11b_telefonata_primo_piano.webp")
    menu:
        sp "I've never set foot in a gym in my life."
        "Say yes, excited.":
            $ interest("amica", 1)
            s "Okay. Okay! Let's do it. New Sara starts tomorrow."
            ch "THAT's my girl."
        "Say yes, with a sigh.":
            s "Fine. But if I die on a treadmill, I'm haunting you."
            ch "Deal. Wear something cute."

    sp "Something cute. For the gym."
    sp "With Joanie, saying no has never really been an option."
    return
