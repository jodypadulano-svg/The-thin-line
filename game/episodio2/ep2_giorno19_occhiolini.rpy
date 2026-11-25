## Giorno 19 · la serata degli occhiolini e il finale forzato «The Wink»
## (docs/narrative/giorno19-occhiolini-2026-11-24.md). Solo con sara_bad_girl.
##
## Joanie fa l'occhiolino (il segnale è sempre lo stesso) e Sara sceglie se
## seguirlo. Saltare non costa mai nulla: Joanie non si offende MAI. Dopo due
## salti di fila smette. Con due seguiti al bancone, due in pista e due al
## divanetto si apre la porta: da lì si esce dalla storia e si va al finale.
## Nessun occhiolino lascia tracce nelle immagini seguenti.

default d19_occhiolini = []     # i numeri seguiti
default d19_salti = 0           # salti di fila
default d19_salti_totali = 0    # per far ruotare le battute del salto

## Finali forzati già visti, in tutte le partite.
default persistent.finali_visti = []

init python:
    ## momento -> occhiolini che gli appartengono
    D19_MOMENTI = {"bancone": (1, 2, 3, 4, 5), "pista": (6, 7, 8), "divanetto": (9, 10, 11)}

    D19_JOANIE = {
        "bancone": ("Joanie at the bar, past a man's broad shoulder: one slow, delighted wink", "images/cg/ep2/d19_j1_occhiolino_bancone.webp"),
        "pista": ("Joanie leaning on a pillar at the edge of the dance floor, winking in the pink light", "images/cg/ep2/d19_j2_occhiolino_pista.webp"),
        "divanetto": ("Joanie across the booth's little table in the candlelight, chin on her fists, winking", "images/cg/ep2/d19_j3_occhiolino_divano.webp"),
    }

    D19_SALTI = [
        "Not this one. Joanie lifts her glass a quarter of an inch, as if to say: {i}quite right{/i}.",
        "Sara shakes her head, just barely. Joanie blows her a kiss.",
        "Sara pulls a face. Joanie nearly spits out her drink, laughing. That's that.",
        "She lets it go by. Nothing happens. Nothing at all. Joanie's still looking at her as though she'd hung the moon.",
    ]

    def d19_seguiti(momento):
        return [o for o in store.d19_occhiolini if o in D19_MOMENTI[momento]]

    def d19_segue(numero):
        """Sara segue un occhiolino. Gli effetti contano una volta per momento."""
        store.d19_salti = 0
        for momento, numeri in D19_MOMENTI.items():
            if numero in numeri and not d19_seguiti(momento):
                interest("amica", 2, "Sara did it for Joanie.")
                interest("ex", 1, "Jacob thinks it was for him.")
                corruption(1, "Sara followed Joanie's wink.")
        if numero not in store.d19_occhiolini:
            store.d19_occhiolini.append(numero)

    def d19_ancora():
        return store.d19_salti < 2

    def d19_porta_aperta():
        return d19_ancora() and all(len(d19_seguiti(m)) >= 2 for m in D19_MOMENTI)

    def finale_visto(nome):
        if nome not in persistent.finali_visti:
            persistent.finali_visti = persistent.finali_visti + [nome]


## --- Da Joanie: la regola --------------------------------------------------------------------

label ep2_d19_regola:
    s "So how would I know? Tonight, say. If you were... enjoying it."
    ch "Oh, you'd know."
    $ via_cg()
    $ cg("Joanie on the carpet, mascara halfway down her cheeks, giving Sara one slow, enormous wink", "images/cg/ep2/d19_19b_prima_volta_occhiolino.webp")
    n "And Joanie, with her mascara halfway down her face, gives her one slow, enormous wink."
    s "{i}That's{/i} it? That's the big signal?"
    ch "That's it. One wink. It means I'm looking, and I like it."
    s "And if I don't want to?"
    ch "Then you don't. I'll never be cross. Not once, not ever. I'd rather have you than any of it."
    s "And if I do?"
    ch "Then you don't have to think about anything. I'm doing the wanting."
    sp "She's doing the wanting. I'd only have to... Oh. That's a nice feeling."
    ch "I should warn you. I'm going to be so greedy."
    return


## --- Motore ----------------------------------------------------------------------------------

label ep2_d19_ammicca(momento):
    $ via_cg()
    $ cg(*D19_JOANIE[momento])
    return

label ep2_d19_salta:
    $ d19_salti += 1
    $ via_cg()
    $ cg("Joanie raising her glass with a warm, easy, loving smile", "images/cg/ep2/d19_j4_salta.webp")
    n "[D19_SALTI[d19_salti_totali]]"
    $ d19_salti_totali = (d19_salti_totali + 1) % len(D19_SALTI)
    if d19_salti >= 2:
        n "After that there aren't any more. Joanie just leans on her shoulder and talks about her boiler, perfectly happy."
    $ via_cg()
    return

## Dopo il saluto con Jacob (il primo occhiolino è in ep2_d19_saluto).
label ep2_d19_occhiolini:
    call ep2_d19_occhi_bancone
    if d19_ancora():
        call ep2_d19_occhi_pista
    if d19_ancora():
        call ep2_d19_occhi_divanetto
    call ep2_d19_numero
    if d19_porta_aperta():
        call ep2_d19_porta
    else:
        $ cg("Sara and Joanie head for The Lantern exit arm in arm", "images/cg/ep2/d19_sara_joanie_uscita_lantern.png")
        n "Last orders. Joanie yawns like a cat and hooks her arm through Sara's."
        ch "Right. Bed. Mine, I mean."
        s "You're {i}humming{/i}."
    $ ambiente(None)
    return


## --- 1 · Il bancone --------------------------------------------------------------------------

label ep2_d19_occhi_bancone:
    $ cg("Jacob offers to get Sara a drink at The Lantern", "images/cg/ep2/d19_jacob_offre_da_bere.png")
    jacob "Let me get you one. For old times' sake. Or for new ones, I'm not fussy."
    call ep2_d19_ammicca("bancone")
    n "Over his shoulder, Joanie winks."
    menu:
        sp "He's got a glass of whisky in his hand."
        "(The wink.)":
            $ d19_segue(2)
            $ segna("ep2_d19_bicchiere")
            $ via_cg()
            $ cg("Sara drinking from Jacob's whisky glass, her eyes over the rim on Joanie", "images/cg/ep2/d19_w02_bicchiere.webp")
            s "No need."
            n "She lifts the glass out of his hand. She turns it, a quarter, a half, until the print of his mouth is in front of hers, and drinks from there. It's whisky. She hates whisky. She looks at Joanie over the rim and swallows."
            jacob "That was mine."
            s "I know whose it was."
            n "Across the bar Joanie puts her own drink down, very carefully, as if it had become heavy."
            call ep2_d19_mestiere
        "Not this one.":
            call ep2_d19_salta
            $ cg("Jacob offers to get Sara a drink at The Lantern", "images/cg/ep2/d19_jacob_offre_da_bere.png")
            call ep2_d19_drink

    if d19_ancora():
        call ep2_d19_ammicca("bancone")
        n "There's a drop of whisky on his lower lip. He hasn't noticed. Joanie has. She winks."
        menu:
            sp "Just there. On his lip."
            "(The wink.)":
                $ d19_segue(3)
                $ via_cg()
                $ cg("Sara wiping a drop of whisky from Jacob's lower lip with her thumb, her eyes already on Joanie", "images/cg/ep2/d19_w03_pollice.webp")
                s "Hold still."
                n "She takes it off with her thumb, slowly, corner to corner. Then she puts the thumb in her own mouth."
                n "She does that part for Joanie."
                jacob "...Was that whisky?"
                s "Mostly."
                sp "Where did that come from? ...From her. It came from her. It's all hers. I'm only saying it."
            "Not this one.":
                call ep2_d19_salta

    if d19_ancora():
        call ep2_d19_ammicca("bancone")
        n "Joanie winks, and cups a hand behind her ear. {i}I can't hear.{/i} Which is the point."
        menu:
            sp "She can't hear a word from there."
            "(The wink.)":
                $ d19_segue(4)
                $ via_cg()
                $ cg("Sara on tiptoe whispering into Jacob's ear, his face changing; Joanie leaning in and hearing nothing", "images/cg/ep2/d19_w04_orecchio.webp")
                n "Sara goes up on her toes, puts one hand on his shoulder, and says it into his ear. All of it. The supermarket. The car. The window that wouldn't shut. She takes her time. She uses the right words."
                n "She can feel him stop breathing about halfway through."
                jacob "...You remember the {i}window{/i}."
                s "I remember everything. I've got a very good memory. I'm a journalist."
                n "Joanie mouths it at her, scarlet, desperate. {i}What did you SAY?{/i}"
                n "Sara shrugs, and smiles, and doesn't tell her. She isn't ever going to tell her. Joanie looks as if she might faint from happiness."
            "Not this one.":
                call ep2_d19_salta

    if d19_ancora():
        call ep2_d19_ammicca("bancone")
        n "He's fishing the cherry out of the bottom of somebody's cocktail, by the stalk, the way he always did. Joanie winks so hard she nearly falls off the stool."
        menu:
            sp "A cherry. Of course it's a cherry."
            "(The wink.)":
                $ d19_segue(5)
                $ via_cg()
                $ cg("Sara taking a cocktail cherry from Jacob's fingers with her mouth, her eyes on Joanie", "images/cg/ep2/d19_w05_ciliegia.webp")
                n "Sara leans in and takes it. With her mouth. She keeps her eyes on Joanie the whole way there and the whole way back, and the stalk stays in his fingers."
                s "I've missed those."
                jacob "You had a whole crate once."
                s "I know. I was telling somebody about it only tonight."
            "Not this one.":
                call ep2_d19_salta
    $ via_cg()
    return


## --- 2 · La pista ----------------------------------------------------------------------------

label ep2_d19_occhi_pista:
    $ cg("Jacob invites Sara onto the dance floor at The Lantern", "images/cg/ep2/d19_jacob_invito_pista.png")
    jacob "You used to dance."
    s "I used to do a lot of things."
    n "The floor at The Lantern is the size of a living room, and it's full. Joanie finds a pillar with a view."
    call ep2_d19_ammicca("pista")
    n "Pink light. Joanie's eye closes, and opens."
    menu:
        sp "Nobody's looking. Except her."
        "(The wink.)":
            $ d19_segue(6)
            $ via_cg()
            $ cg("Sara dancing with her back against Jacob's chest, her eyes on Joanie at the edge of the floor", "images/cg/ep2/d19_w06_di_schiena.webp")
            n "She turns round in his arms and puts her back against his chest. Like this she can't see him at all. She can feel exactly how big he is, and where, and the only person she can see is Joanie."
            n "She dances a whole song looking at her best friend."
            sp "He thinks I can't face him. Poor man. He's got no idea who I'm dancing with."
        "Not this one.":
            call ep2_d19_salta

    if d19_ancora():
        call ep2_d19_ammicca("pista")
        n "Another song. Another wink, quicker than the last."
        menu:
            sp "She's getting impatient."
            "(The wink.)":
                $ d19_segue(7)
                $ via_cg()
                $ cg("Sara dancing with her hair across her face, undoing one more button, a line of black lace, her eyes on Joanie", "images/cg/ep2/d19_w07_capelli.webp")
                n "She shakes her hair right out, into her eyes, into his collar. Then her hand finds the next button of the silk and it gives, easy as anything, and there's a line of black lace in the pink light."
                n "She doesn't look down to check. Joanie's face tells her how much. When the song ends she does it up again, one-handed, still looking."
                jacob "It's warm in here, isn't it."
                s "It's about to be."
            "Not this one.":
                call ep2_d19_salta

    if d19_ancora():
        call ep2_d19_ammicca("pista")
        n "Joanie has stopped pretending to look anywhere else. She winks."
        menu:
            sp "I know what she wants to see."
            "(The wink.)":
                $ d19_segue(8)
                $ via_cg()
                $ cg("Close-up of Sara's hands over Jacob's, placing them on her hips, her head back on his shoulder", "images/cg/ep2/d19_w08_mani.webp")
                n "His hands have been very polite. They've been hovering an inch from her waist for two songs, like a man carrying a cake."
                n "She takes one, and then the other, and puts them where she wants them. On the hips. Lower. {i}There{/i}. She presses them down and leaves hers on top."
                s "You can stop being a gentleman. Somebody's bored."
                jacob "Who's bored?"
                s "Nobody. Not any more."
            "Not this one.":
                call ep2_d19_salta
    $ via_cg()
    return


## --- 3 · Il divanetto ------------------------------------------------------------------------

label ep2_d19_occhi_divanetto:
    $ cg("Joanie takes a seat at the booth while Sara and Jacob stand beside it", "images/cg/ep2/d19_divanetto_arrivo.png")
    n "There's a booth behind the plants that nobody ever finds. Joanie finds it. She slides in on one side with all the coats. There's one seat on the other."
    call ep2_d19_ammicca("divanetto")
    n "Joanie, all innocence, spreads out the coats a little further. And winks."
    menu:
        sp "One seat. Two of us."
        "(The wink.)":
            $ d19_segue(9)
            $ via_cg()
            $ cg("Sara sitting on Jacob's knee in the leather booth, chatting to Joanie as if nothing were happening", "images/cg/ep2/d19_w09_in_braccio.webp")
            s "Well, there's nowhere else."
            n "She sits down on his knee as if it were a chair, crosses her ankles, and picks up the conversation exactly where they'd left it. Something about Joanie's landlord. His arm comes round her waist to stop her sliding off. She hadn't been sliding."
            ch "So anyway. The boiler."
            s "The boiler, yes. Go on."
            n "Neither of them could tell you, afterwards, a single thing about the boiler."
        "Not this one.":
            call ep2_d19_salta

    if d19_ancora():
        call ep2_d19_ammicca("divanetto")
        n "Joanie looks at Sara's feet. Then at Jacob's hands. Then she winks."
        menu:
            sp "They really are killing me, as it happens."
            "(The wink.)":
                $ d19_segue(10)
                $ via_cg()
                $ cg("Sara's foot in Jacob's lap as he undoes the thin strap of her sandal; Joanie watching", "images/cg/ep2/d19_w10_scarpa.webp")
                s "These are killing me."
                n "She swings round against the arm of the booth and puts her foot in his lap. He looks at it. Then he bends that great shaved head and undoes the little strap, with two fingers, as carefully as if it were wired to something."
                n "He doesn't let go of her ankle afterwards. His thumb is on the bone. Joanie's watching the thumb."
                jacob "Better?"
                s "Ask me again in a minute."
                n "He does the strap back up himself. It takes him twice as long."
            "Not this one.":
                call ep2_d19_salta

    if d19_ancora():
        call ep2_d19_ammicca("divanetto")
        n "Jacob goes to the bar. The moment his back's turned, Joanie leans across the candle and winks. Then, for good measure, she does it with the other eye."
        s "That's two."
        ch "I'm {i}starving{/i}."
        menu:
            sp "He'll be a couple of minutes at least."
            "(The wink.)":
                $ d19_segue(11)
                $ via_cg()
                $ cg("Sara, scarlet with laughter, stuffing a black lace bra into Joanie's handbag; Joanie with both hands over her mouth", "images/cg/ep2/d19_w11_reggiseno.webp")
                n "It's a trick she learned in a gym changing room and has never once used for evil. Hook, strap, elbow, the other elbow. She draws the whole thing out of her sleeve like a conjuror with the flags of all nations, black lace and all, and stuffs it into Joanie's handbag."
                n "Joanie has both hands over her mouth. She's making a noise like a kettle."
                ch "Sara. Collins."
                s "Look after it. It was expensive."
                n "They're still crying with laughter when he comes back with the drinks."
                jacob "What did I miss?"
                s "Nothing."
                n "And then silk is only silk, and he sits down, and looks, and doesn't say anything at all for quite a long time."
            "Not this one.":
                call ep2_d19_salta
    $ via_cg()
    return


## --- La porta (ambra: finale forzato) ---------------------------------------------------------
## Nessun effetto e nessuna flag da qui in poi: così «Go back to the choice» riporta
## alla porta con tutto com'era.

label ep2_d19_porta:
    $ vai("locale", "The Lantern — closing time")
    $ ambiente("locale")
    $ musica("locale")
    $ cg("Joanie holding the door of The Lantern open with her back, the street lights behind her, looking at Sara", "images/cg/ep2/d19_porta.webp")
    n "Closing time. Coats. The cold comes in every time the door opens. Joanie's holding it with her back, and the street's behind her, and the lights."
    $ via_cg()
    $ cg("Close-up of Joanie in the doorway, not smiling, breath held, eyes shining", "images/cg/ep2/d19_porta_primo_piano.webp")
    n "She isn't smiling now. She looks at Sara as if she were about to open the best present of her life, and couldn't bear to tear the paper."
    n "She winks."
    sp "I know what that one is."
    sp "I could go home. She'd hug me, and we'd get a taxi, and she'd never say a word about it."
    sp "I don't have to decide. That's the thing. I don't have to decide anything. I only have to do what she wants, and I'd get everything."
    menu:
        sp "One wink."
        "(The wink.) Go with him." (acceleratore="finale"):
            call ep2_d19_finale
            jump ep2_d19_porta
        "Not this one. Home.":
            $ segna("ep2_d19_porta_chiusa")
            $ via_cg()
            $ cg("Joanie raising her glass with a warm, easy, loving smile", "images/cg/ep2/d19_j4_salta.webp")
            n "Joanie breathes out. And there it is, the smile, the real one, all the way up."
            ch "Come on, then. I'll get us a taxi. God, what a {i}night{/i}."
            n "Jacob watches them go from the kerb with his hands in his pockets, like a man who's been told the film's finished and can't see why."
            $ via_cg()
            $ cg("Joanie rests her head on Sara's shoulder in the taxi home", "images/cg/ep2/d19_taxi_verso_casa.png")
            n "In the taxi she puts her head on Sara's shoulder."
            ch "Thank you. That was already too much. That was Christmas."
    return


## --- Dopo la porta: saltare accorcia soltanto la scena ----------------------------------------

label ep2_d19_finale:
    $ via_cg()
    $ cg("Sara pulling Jacob down by his lapels and kissing him by the door; Joanie with a hand on her heart", "images/cg/ep2/d19_w12_bacio.webp")
    n "She takes hold of his lapels, both of them, and pulls. He comes down a long way."
    n "It's four years old, that kiss. It goes off like something left in a cellar."
    $ via_cg()
    $ cg("The second kiss in close-up: Sara's eyes open, shining, on Joanie past Jacob's cheek", "images/cg/ep2/d19_w12b_occhi_aperti.webp")
    n "And when he'd have stopped she does it again, slower, and this time she keeps her eyes open, and gives it to Joanie over his cheek."
    $ via_cg()
    $ cg("The same kiss, deeper: Sara's eyes, heavy-lidded now, still on Joanie", "images/cg/ep2/d19_w12d_bacio_vicino.webp")
    n "All of it. Joanie's hand is flat on her own heart."
    jacob "My place is by the station. It'll be shut by now."
    s "What sort of place?"
    jacob "Come and see."

    $ ambiente(None)
    $ vai("strada", "A taxi — 2:10 a.m.")
    $ musica("notte")
    $ cg("Joanie checks her lipstick while Sara and Jacob sit in the back of the taxi", "images/cg/ep2/d19_taxi_verso_locale_jacob.png")
    n "Joanie takes the front seat before anyone can be polite about it. She pulls the sun visor down and fixes her lipstick in the mirror for the entire journey. Her lipstick's perfect."
    menu:
        n "In the little square of glass, an eye closes, and opens."
        "(The wink.)":
            $ cg("In the mirror, Joanie's eyes; in the back seat Sara's legs across Jacob's lap, his mouth at her neck", "images/cg/ep2/d19_w13_specchietto.webp")
            n "Sara puts her legs across his lap. His mouth finds the place under her jaw, and she lets her head go back on the seat until she's upside down to the street lights, and the only thing the right way up is a pair of eyes in a little square of glass."
            sp "I'm so happy. Is it allowed? I'm so happy."
        "Not this one.":
            n "Sara shakes her head and takes his hand instead. In the mirror, Joanie blows her a kiss."

    $ via_cg()
    $ vai("strip_club", "Jacob's place — 2:30 a.m.")
    $ cg("The empty strip club after closing: Sara leaning over the cracked, glowing jukebox, Jacob beside her, Joanie already in an armchair", "images/cg/ep2/d19_w14_jukebox.webp")
    n "A stage the size of a table. A pole. Forty chairs with their legs in the air."
    s "...You own a {i}strip club{/i}."
    jacob "Don't make that face."
    s "I'm not making a face. Jo, am I making a face?"
    ch "You're making {i}several{/i}."
    n "And in the corner, cracked and glowing, is the jukebox. {i}Their{/i} jukebox. From the place with the sticky floor, where he asked her name."
    s "You kept it."
    jacob "Only plays one song."
    menu:
        n "Joanie winks."
        "(The wink.)":
            n "She knows which button. She presses it without looking."
        "Not this one.":
            n "Sara only lays her palm on the glass. It's warm. Jacob reaches past her and presses the button himself."

    n "Joanie has already chosen the best armchair and taken her shoes off. She pats the one beside her. Jacob sits down like a man in church."
    menu:
        n "Then she turns her head to the stage, and winks."
        "(The wink.)":
            $ via_cg()
            $ cg("Sara barefoot on the small round stage, turning round the brass pole, laughing; Jacob and Joanie in the armchairs", "images/cg/ep2/d19_w15_palco.webp")
            n "It's only a step up. The boards are cold under her feet, and there's a light, and behind the light there are two people who'd like to look at her."
            n "All her life she's crossed her arms. All her life she's carried books."
            n "She puts her hand on the brass, and leans out, and lets go of the ground."
            sp "Let them look."
            menu:
                n "Joanie winks again. She's got her knees up under her chin."
                "(The wink.)":
                    $ via_cg()
                    $ cg("Sara seen from behind on the stage, dropping the burgundy blouse at arm's length, looking back over her shoulder, laughing", "images/cg/ep2/d19_w16_vestiti.webp")
                    n "The silk goes first. It takes for ever. Half of it's the buttons and half of it's that she can't stop laughing."
                    n "With her back to them she holds it out at arm's length, and looks over her shoulder, and opens her fingers."
                    ch "I'm not looking. I'm not looking. I'm looking."
                    jacob "Sara."
                    s "Shh. It's not for you."
                    n "It's the first time she's said it out loud. He looks at her. He looks, slowly, at the armchair next to his. And Jacob, who isn't stupid, starts to grin."
                    jacob "How long's {i}that{/i} been going on?"
                    s "Since about nine o'clock."
                "Not this one.":
                    n "Sara shakes her head, out of breath, and takes a bow instead. Joanie applauds until her hands hurt."
        "Not this one.":
            n "Sara looks at the stage, and laughs, and shakes her head. She goes and sits on the arm of Joanie's chair until the song's finished."

    $ via_cg()
    $ vai("strip_club", "Upstairs")
    $ cg("Sara gestures towards the armchair as Joanie pauses in the doorway", "images/cg/ep2/d19_stanza_piano_di_sopra.png")
    n "There's a staircase behind the bar. There's a room at the top of it, and a bed, and one big chair in the corner."
    n "Joanie stops at the door. It's the only time all night she's looked unsure."
    ch "I can go. If you'd rather. I can honestly just go."
    s "Sit down, Jo."
    n "Joanie sits down."
    $ via_cg()
    $ cg("Close-up of Sara winking over Jacob's shoulder", "images/cg/ep2/d19_w17_occhiolino_sara.webp")
    n "And this time it's Sara who winks."
    $ via_cg()
    ## La scena del letto: game/nsfw/d19_the_wink.rpy (la W17 la chiude).
    call scena_nsfw("d19_the_wink")
    $ via_cg()

    ## La mattina.
    $ vai("strip_club", "Upstairs — Saturday, 8:40 a.m.")
    $ cg("Morning: Sara in a man's huge black T-shirt on the edge of the bed, a phone in her hand; Joanie asleep in the armchair under a leather jacket", "images/cg/ep2/d19_f1_mattina.webp")
    n "The station wakes them. Joanie's asleep in the chair under the leather jacket, with her mouth open and one bare foot out."
    n "Sara's phone has been buzzing on the floor for a while. Fourteen. {i}Are you at Joanie's?{/i} {i}Are you ok?{/i} {i}I made the pancakes. Call me when you see this x{/i}"
    n "She reads them all. She reads the last one twice."
    sp "I'll call him. I'll tell him all of it. He deserves somebody who makes a noise about pancakes."
    n "She waits to be sorry. She's sorry for him, a lot, in a clear place, like being sorry about the weather. She isn't sorry."
    n "She turns the phone face down on the sheet."

    ## Mesi dopo.
    $ via_cg()
    $ musica("chiusura_ep1")
    $ vai("strip_club", "Some months later")
    $ cg("The club open and full, warm gold light: Sara in a red dress at the end of the bar, radiant, Jacob behind it, a stranger talking to her", "images/cg/ep2/d19_f2_mesi_dopo.webp")
    n "It turns out the club needed somebody who could write. The sign outside, the little programme, the stories about the girls. People come for those now. There's a shelf by the jukebox with her book on it."
    n "[nome_compagno] lives near his mother. He's seeing someone from the conventions. He sends Sara reviews he thinks will make her laugh, and they do."
    n "She has a man who's hers on most nights, and a best friend who's hers on all of them. If you asked her who decides, she'd have to think."
    s "I don't decide anything any more. It's the freest I've ever been."
    n "There's a stranger talking to her, at the end of the bar. He's got nice hands. He's asking what she does."
    $ via_cg()
    $ cg("Across the crowded room, Joanie in a velvet armchair raises her glass and gives one slow wink", "images/cg/ep2/d19_f3_ultimo_occhiolino.webp")
    n "Across the room, in the best armchair, somebody raises a glass."
    n "And winks."
    $ via_cg()
    $ musica(None)
    $ luogo_corrente = ""
    scene bg nero with fade
    $ finale_visto("The Wink")
    n "{size=+20}ENDING — THE WINK{/size}"
    menu:
        n "This was a forced ending. The main story is still where you left it."
        "Go back to the choice.":
            return
        "Main menu.":
            $ renpy.full_restart()
    return
