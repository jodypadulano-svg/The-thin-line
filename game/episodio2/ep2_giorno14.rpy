## Giorno 14, domenica. Pranzo delle due famiglie e sblocco del telefono.
## Calendario: docs/mese-1.md. Intrecci approvati: I3, I1, I2, I16, I7.

label ep2_d14:
    call nuovo_giorno(14, "Sunday Lunch")
    $ musica("casa")
    $ vai("casa", "Home — Sunday morning")
    $ cg("Sara in her Sunday dress in the kitchen, phone beside her tea; Josh sets down a second cup", "images/cg/ep2/d14_01_mattina.webp")

    n "In the morning, Daniel's message is still the last thing he sent. Sara taps the thread and waits long enough for the screen to dim."
    if fatto("ep1_d13_cerniera"):
        n "She gathers her hair over one shoulder. In the quiet kitchen she can remember exactly where his mouth touched her ear."
    elif fatto("ep1_d13_pranzo_forse"):
        sp "I could still tell him I've changed my mind. I could tell him that right now."
    else:
        sp "Brave girl. Does he get to decide what counts as brave now?"

    n "[nome_compagno] sets a mug down beside her phone, with the handle turned towards her."
    c "Mum says half past twelve. Dad says twelve. They'll both be annoyed if we get there at quarter past."
    s "Quarter past it is, then."
    n "He smiles a little. Sara takes a sip. It's exactly the way she likes it."
    $ via_cg()

    call ep2_d14_pranzo
    call ep2_d14_cucina
    call ep2_d14_darius
    call ep2_d14_sera

    $ musica(None)
    $ luogo_corrente = ""
    scene bg nero with fade
    return


label ep2_d14_pranzo:
    $ vai("casa", "Sunday lunch — 12:30 p.m.")
    call telefono_fascia("pranzo", con_josh=True)
    $ cg("Wide shot of both families at Sunday lunch: Hugo at the head, Samantha beside him, Sally and Andrew opposite Sara and Josh", "images/cg/ep2/d14_02_tavola.webp")

    n "Hugo takes the carving knife from Samantha just as she makes the first cut. She still has the serving fork in her hand."
    hugo "Leave it. It'll go cold at that rate."
    n "Samantha sets the fork down by his plate."
    samantha "The potatoes are still hot, Sara. Shall I pass them before he takes those too?"
    n "Sara laughs. Andrew reaches for the bowl at the same time she does."
    andrew "Sorry, love. Go on."
    n "[nome_compagno] says the same thing a second later when they both reach for the spoon. Sara looks from one to the other."
    sp "He's sweet the way Dad is. They'd both let the potatoes go cold waiting for me to take the first one."

    hugo "I heard about Harrow. Daniel got them to sign on a Friday night, of all things. The man knows how to close."
    c "It was Thursday. By Friday we'd already—"
    hugo "I'm sure you had all the copies ready for him."
    n "Sally sets her glass down neatly on its coaster. Andrew keeps his eyes on his plate."
    $ via_cg()
    $ cg("Josh at the family table looking down at his plate, holding his fork above an untouched slice; Sara watches from beside him", "images/cg/ep2/d14_03_josh.webp")
    n "[nome_compagno] turns his fork over. At the toast last night, he'd done the same thing with the stem of his glass."
    sp "He's had practice letting a room laugh at him."

    menu:
        "Tell Hugo what [nome_compagno] did on Harrow.":
            $ interest("josh", 3)
            $ confidence(1)
            s "He worked late for six weeks. I should know. I'm the one who kept reheating dinner."
            s "If you want to know how they got it signed, let him finish."
            n "Hugo puts another slice on his own plate. While he's doing it, [nome_compagno] tells them what happened on Thursday. Nobody interrupts this time."
            n "Under the table, his knee touches hers and stays there."
        "Let the remark pass.":
            n "Sara puts a potato on her plate and passes the bowl to Andrew. By the time it reaches Hugo, he's asking for the gravy."
        "Smile at Hugo's joke.":
            $ interest("josh", -2)
            $ via_cg()
            $ cg("Sara at the family table letting out a little laugh, Hugo catching her eye with a small smile, Josh beside her reaching for his water", "images/cg/ep2/d14_03b_sara_hugo.webp")
            n "Sara lets out a little laugh. Hugo catches her eye over his glass, the corner of his mouth lifting just enough for her to see."
            sp "For a second it feels like the two of us heard a different joke from everyone else."
            n "[nome_compagno] sees it. He puts down his fork to reach for water and doesn't pick it back up."

    $ via_cg()
    $ cg("Sara and Sally at the table after the main course; Sally's eyes stop at the neckline of Sara's Sunday dress, Samantha nearby", "images/cg/ep2/d14_04_vestito.webp")
    n "When Sara reaches for Andrew's plate, Sally glances at the neckline of her dress."
    sally "I thought you'd save that one for an evening."

    menu:
        "Lower her eyes and take the plate.":
            n "Sara looks at the gravy gathered along the rim. She lets go of the plate with one hand and smooths the dress at her knee."
        "Tell Sally she likes the dress as it is.":
            $ confidence(1)
            s "I like it in daylight. That's why I wore it today."
            n "Sally folds her napkin once more, though it was folded already."

    samantha "Come shopping with me sometime, Sara. There's a place I can spend an hour in without anyone asking if I'm nearly done."
    n "She tells Sara this as if she's giving her the address of a very good restaurant."

    menu:
        "Take Samantha up on it.":
            $ segna("ep2_d14_shopping_samantha")
            s "I'd like that. Show me where you go."
            samantha "I will. We'll take our time."
        "Thank Samantha and decline.":
            s "Thanks, Samantha. I think I've done enough shopping for a little while."
            samantha "Fair. We'll have coffee some other time."

    n "Sara carries Andrew's plate to the kitchen. Sally gets up to follow with the bread basket."
    $ via_cg()
    call inizio_retroscena
    $ cg("From the empty place at the family table, Sally with the bread basket and Hugo at the far end briefly meet each other's eyes", "images/cg/ep2/d14_05_sguardo.webp")
    rs "At the door, Sally looks back. Hugo is already looking at her. She shifts the bread basket to her other hand and goes through."
    $ via_cg()
    call fine_retroscena
    return


label ep2_d14_cucina:
    $ vai("casa", "The kitchen — after lunch")
    $ cg("Sara and Sally side by side at the kitchen sink after lunch, plates stacked between them, the dining room out of sight", "images/cg/ep2/d14_06_cucina.webp")
    n "Sally puts the basket on the counter. Sara has already run the water."
    sally "Leave the plates in there a minute. You've just sat down for the first time all week, I expect."
    s "I sit down at work."
    sally "With somebody waiting for you to get up again."
    n "She puts the plug in herself. For a minute they listen to the sink filling."
    sally "Go somewhere because you feel like going, Sara. Meet people you wouldn't meet sitting at home."
    s "Should I tell him that, then? I'm going out because my mother told me to get a life?"
    n "Sally laughs once, softly enough that it stays in the kitchen."
    sally "You can tell him where you're going. You can even ask him along. Just make a plan of your own first."
    n "Sara takes her phone out of her pocket and sets it on the dry end of the counter."
    $ sblocca_telefono()
    $ via_cg()
    return


label ep2_d14_darius:
    $ vai("casa", "Home — Sunday afternoon")
    $ cg("Sara at the kitchen sink rinsing an empty milk jug, Josh nearby, afternoon light across the counter", "images/cg/ep2/d14_08a_latte_finito.webp")
    n "There's just enough milk left to turn the bottom of the jug white. Sara puts it back, takes it out again, and rinses it."
    c "I'll get some later."
    s "I'll go. I could do with a walk."
    $ via_cg()

    $ vai("negozio", "The supermarket — Sunday afternoon")
    $ ambiente("supermercato")
    $ cg("Sara with a carton of milk in the supermarket, Darius beside her comparing two packets of biscuits", "images/cg/ep2/d14_08_supermercato.webp")
    n "Darius is standing in the biscuit aisle with a packet in each hand. He puts one back, walks two steps, and goes back for it."
    s "Do you want me to come back when you've made up your mind?"
    dr "I've made up my mind four times."
    s "The ones on the left."
    dr "See, you say that, but you'd steal the ones on the right if I put them out at your place."
    s "Well, now you know what to bring on Tuesday."
    n "He puts both packets in his basket. At the tills, Sara can see the little café across the road. There's a table free by the window."
    s "Have you got time for a coffee?"
    dr "Yeah. I'd like that."
    $ interest("amico", 1, "Sara wanted to keep talking to Darius.")
    $ ambiente(None)
    $ via_cg()

    $ vai("bar_aperitivo", "The café across the road — Sunday afternoon")
    $ cg("Sara and Darius over coffee by a café window, groceries on the floor between their chairs", "images/cg/ep2/d14_09_caffe_darius.webp")
    n "Darius nudges her bag out of the sun with his shoe."
    dr "How's the woman with the door?"
    $ musica("darius_caffe")
    s "You remembered her."
    dr "You never told me what she found on the other side."
    s "A room that feels like hers. The trouble is, somebody else lives in it."
    dr "Does she know them?"
    s "I was going to make her know them. Now I think I'd like her to have a minute on her own in there."
    n "He stirs his coffee. She waits for him to ask her what happens next."
    dr "I'd want a minute too."
    n "Sara looks down at her cup. She's been trying to explain that minute to herself all week."
    s "That's the bit I want to write."
    $ interest("amico", 1, "Darius understood what Sara wanted to write.")
    dr "Well, when you've written it, I'd like to read it. If you feel like showing me."
    n "When they get up, he hands her the milk and offers her one of the packets."
    s "Save them for Tuesday."
    dr "You say that now. I'm putting your name on the good ones."
    n "She walks home smiling. By the time she gets there, she's worked out the first sentence of the room."
    $ segna("phone_d14_darius_room")
    $ via_cg()
    return


label ep2_d14_sera:
    $ musica("casa")
    $ vai("casa", "Home — Sunday evening")
    $ cg("Sara alone in her kitchen at dusk with her phone beside a cup, the warm light from the hall just reaching the table", "images/cg/ep2/d14_07_telefono.webp")
    n "At home, [nome_compagno] goes to take a shower. Sara puts the kettle on and reaches for her phone."
    if fatto("ep1_d13_pranzo_forse") or fatto("ep1_d13_pranzo_no"):
        call ep2_d14_maglione
    $ fascia_corrente = FASCE.index("sera")
    call telefono_nuovo_sessione("Go to bed")
    n "Sara rubs her eyes, puts the phone down and goes to bed."
    $ via_cg()

    $ vai("camera", "The bedroom — Sunday night")
    $ cg("Sara slipping into bed beside Josh as he lifts an arm for her, her phone on the bedside table, quiet bedside light", "images/cg/ep2/d14_10_buonanotte.webp")
    $ fascia_corrente = FASCE.index("notte")
    n "In bed, [nome_compagno] lifts his arm without opening his eyes so Sara can tuck herself under it. She leaves her phone on the nightstand, within reach."
    $ via_cg()
    return


label ep2_d14_maglione:
    $ suono("telefono_vibra")
    $ chat_aperta = "amica"
    show screen telefono_chat("amica")
    $ msg("amica", "sunday check-in. is lunch with daniel still a thing?")
    if fatto("ep1_d13_pranzo_no"):
        $ msg("sara", "I told him [nome_compagno] would know. If I go, I'm telling him first.")
        $ msg("amica", "fair. he asked you to lunch, not to join a secret society")
    else:
        $ msg("sara", "I said maybe. It sounded easier to say on the terrace than it does now.")
        $ msg("amica", "maybe still means maybe. you can think about it")
    $ msg("sara", "If it happens, Thursday's the only lunch break I could stretch. We haven't arranged anything yet.")
    $ msg("amica", "ok. what would you wear?")
    $ msg("sara", "You're going to say something with a low neckline.")
    $ msg("amica", "crew neck actually. hang on, sending you the listing", immagine="images/cg/ep2/d14_maglione_annuncio.webp")
    n "Sara opens the photo. A fitted white crew-neck sweater with HYPNO printed across the front in black. Below the lettering, two black-and-white spirals curl out from where her nipples would be."
    $ msg("sara", "The spirals are a bit much.")
    $ msg("amica", "you opened the photo twice didn't you")
    $ msg("sara", "You'd wear this to talk about a novel?")
    $ msg("amica", "depends on the novel")
    $ msg("amica", "ordered. says it'll get here wednesday")
    $ msg("sara", "There's still a chance I won't go.")
    $ msg("amica", "I bought a sweater, Sara. you can leave it in the box")
    $ segna("ep2_d14_maglione_ordinato")
    hide screen telefono_chat
    $ chat_aperta = None
    return
