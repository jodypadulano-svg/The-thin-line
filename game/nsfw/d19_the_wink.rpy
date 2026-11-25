## La scena del letto di «The Wink» (giorno 19, finale forzato).
## STRUTTURA SOBRIA: sei momenti, ognuno con la sua CG (il 4 ne ha due). I punti segnati con
## «TESTO DI JODY» si riempiono a mano; il resto regge anche così.
## Attenzione: tools/nsfw/genera_scena.py sovrascrive questo file.
## Regole: tutto chiesto e consensuale, Sara sorride o ride, Joanie resta in
## poltrona, vestita, senza toccarli; Josh non viene nominato.

label nsfw_d19_the_wink:
    ## 1 · Il sì
    $ via_cg()
    $ cg("Sara and Jacob standing face to face by the bed in the lamplight, foreheads close, his hands waiting", "images/cg/ep2/d19_n01_il_si.webp")
    jacob "You're sure?"
    s "I've been sure since the cherry."
    n "He laughs, and it's the laugh she remembers, the low one, the one that starts before he's decided to."

    ## 2 · Ritrovarsi
    $ via_cg()
    $ cg("Sara and Jacob finding each other again on the edge of the bed, laughing into a kiss", "images/cg/ep2/d19_n02_ritrovarsi.webp")
    n "Four years. They bump noses. He remembers the ticklish place and goes straight to it, the swine, and she shrieks, and from the armchair comes a small strangled noise of joy."
    sp "Oh. Hello. I know you."
    ## TESTO DI JODY

    ## 3 · Il primo occhiolino
    $ via_cg()
    $ cg("From the bed: Joanie in the green armchair, knees under her chin, winking in the lamplight", "images/cg/ep2/d19_n03_joanie_poltrona.webp")
    n "Sara turns her head on the pillow. Joanie has her knees under her chin and both hands over her mouth. Over the top of her fingers, one eye closes."
    s "Slower, she says."
    jacob "She didn't say anything."
    s "You're not the one she's talking to."
    ## TESTO DI JODY

    ## 4 · Sara conduce
    $ via_cg()
    $ cg("Sara above Jacob, hair falling forward, laughing, looking over her shoulder towards the armchair", "images/cg/ep2/d19_n04_sara_conduce.webp")
    n "The next one hasn't finished closing before she's rolled him onto his back. He goes over like a wardrobe, amazed. Nobody does that to him."
    jacob "What was that one?"
    s "That one was mine."
    $ via_cg()
    $ cg("Sara above Jacob, eyes closed, lost in it", "images/cg/ep2/d19_n04b_insieme.webp")
    ## TESTO DI JODY

    ## 5 · Gli occhi di Joanie (sotto resta la N04b; la N05 arriva subito dopo il culmine)
    n "And when it comes she shuts her eyes, once, and then opens them again on purpose. She finds Joanie's, across the room, and holds on to them, and she's loud. God, she's loud. Somewhere under the floor the jukebox seems to ring with it."
    ## TESTO DI JODY
    $ via_cg()
    $ cg("Sara on the pillow in Jacob's arms, flushed and smiling, her eyes on the armchair", "images/cg/ep2/d19_n05_gli_occhi.webp")
    n "Joanie's crying. Joanie's laughing. Joanie mouths it, so there's no mistake. {i}Told you.{/i}"

    ## 6 · Dopo
    $ via_cg()
    $ cg("Seen from behind the armchair: Joanie's dark head; beyond, Sara and Jacob under the sheet, Sara smiling towards the chair", "images/cg/ep2/d19_w17_letto.webp")
    n "After a while Sara puts her hand out, over the edge of the bed, into the dark. She doesn't look where. Another hand comes down off the armrest and takes it."
    ch "Was it..."
    s "It was. Go to sleep, Jo."
    n "Nobody lets go."
    return
