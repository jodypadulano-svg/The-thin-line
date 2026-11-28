## Jacob · incontri numerati, indipendenti dalla data (Jody, 26-27/11/2026).
## Ogni incontro è una label a sé: il giorno che lo ospita la chiama e basta.
## Effetti generali della serata (Corruption, segreto, rientro tardivo) li dà il giorno, non questo file.
## Se in futuro succede qualcosa di importante, si aggiungono qui brevi righe condizionali,
## senza riscrivere la scena (regola della modularità).

default jacob_incontri = 0

init python:
    def cg_ricordo(descrizione, immagine=None):
        """CG di un ricordo, mostrata in seppia. L'immagine si genera a colori:
        il viraggio lo fa il gioco. Se manca, segnaposto con la didascalia."""
        if immagine and renpy.loadable(immagine):
            renpy.show("cg_corrente", what=Transform(immagine, fit="cover",
                xysize=(config.screen_width, config.screen_height), matrixcolor=SepiaMatrix()))
            renpy.with_statement(dissolve)
        else:
            renpy.show_screen("segnaposto_cg", descrizione="Sepia memory: " + descrizione)


## --- Incontro #1 · «One drink» -----------------------------------------------------------
## Jacob prova a farle rivivere solo le cose belle; nella testa di Sara passano anche i litigi.
## Unica scelta: rivalutarlo (Jacob +2) o no (la serata finisce presto, nessun romanticismo).
## Se lo rivaluta le scappa «Lighthouse»: smitizzare (Jacob +1) o infastidirsi (Confidence +1).
## Restituisce True se la serata è arrivata in fondo: allora il giorno può offrire «One more…»
## e poi chiama jacob_incontro_1_saluto. Con False la serata si è già chiusa sulla porta.

label jacob_incontro_1:
    $ jacob_incontri = max(jacob_incontri, 1)
    $ segna("jacob_incontro_1")
    $ vai("strada", "Outside The Lantern — 8:05 p.m.")
    $ ambiente(None)
    $ musica("jacob_ricordi")
    $ cg("The Lantern's shutters down with a small CLOSED WEDNESDAYS card (not readable); Jacob leaning beside the door with his hands in his jacket pockets, Sara arriving under the street light", "images/cg/ep2/jacob1_01_arrivo.webp")
    n "Same bar, he said. The shutters are down. There's a card in the window, and Jacob is leaning beside it as if he'd put it there himself."
    s "It's closed."
    jacob "Wednesdays. I know. Mine isn't."
    s "Yours is closed too, I'd bet."
    jacob "For everyone else."
    n "He walks her two streets towards the station. He keeps half a step behind, the way he used to on crowded pavements. There's nobody on this one."
    $ via_cg()

    $ vai("strip_club", "Jacob's place — 8:20 p.m.")
    $ ambiente("locale_chiuso")
    $ cg("Jacob's empty club after hours: chairs upside down on the tables, the stage dark, only the bar and an old jukebox lit; Jacob behind the bar setting down two glasses, Sara on a stool", "images/cg/ep2/jacob1_02_bancone.webp")
    n "The chairs are upside down on the tables. The stage is dark. Only the bar is lit, and a jukebox in the corner that looks older than both of them put together."
    jacob "One drink."
    n "He pours it, and holds up a finger. One."
    s "You're really counting."
    jacob "I said I would. I keep the promises that don't cost me anything."
    $ via_cg()

    $ cg("Close shot of Jacob across the bar, forearms on the counter, smiling as he starts a story", "images/cg/ep2/jacob1_03_racconta.webp")
    jacob "Do you remember the car? The red one. On the coast road."
    s "The one that died."
    jacob "The one that died beautifully. Right in front of the sea. You said it had chosen the spot."
    $ via_cg()
    $ cg_ricordo("Jacob and Sara, younger, sitting on the bonnet of a broken-down red car by the sea, both laughing in light rain, her hair damp", "images/cg/ep2/jacob1_r1_auto.webp")
    n "Rain. The bonnet still warm. They waited three hours for the tow truck and she laughed for most of them."
    $ via_cg()
    $ cg_ricordo("A small kitchen at night: Sara, younger, standing with her arms crossed, Jacob's phone face down on the table between them", "images/cg/ep2/jacob1_r2_telefono.webp")
    n "The same month. A phone face down on a kitchen table. She'd asked who it was, and he'd said nobody, and turned it over."
    $ via_cg()

    $ cg("Jacob at the jukebox feeding it a coin, his back half-turned, Sara watching from the bar stool", "images/cg/ep2/jacob1_04_jukebox.webp")
    $ suono("jukebox")
    n "He goes to the jukebox. He doesn't need to look at the list."
    jacob "Festival. The second year. You danced on my shoes because the field was mud."
    s "I danced on your shoes because you said I couldn't dance."
    jacob "You couldn't. You could stand on shoes very well."
    $ via_cg()
    $ cg_ricordo("At a muddy summer festival at dusk, Sara, younger, dancing standing on Jacob's boots, his hands on her elbows, both laughing", "images/cg/ep2/jacob1_r3_festival.webp")
    n "Mud to the ankles. Someone's lights strung through a tree. She'd felt very tall."
    $ via_cg()
    $ cg_ricordo("Night, a doorway: Sara, younger, leaving with a holdall over her shoulder, not looking back; Jacob's hand on the door frame", "images/cg/ep2/jacob1_r4_porta.webp")
    n "And the night with the holdall. She'd packed it in eleven minutes. She'd timed it, afterwards, to have something to hold on to."
    $ via_cg()

    $ cg("Sara on the bar stool holding her glass with both hands, looking at Jacob across the bar; the jukebox glow behind her", "images/cg/ep2/jacob1_05_sara.webp")
    jacob "We were good, Sara. Most of the time we were good."
    sp "He's telling it with the bad bits cut out. Like a trailer."
    sp "...Some of the good bits were real, though."
    menu:
        sp "What do I do with the good bits?"
        "Let herself remember them.":
            $ segna("jacob_1_rivalutato")
            $ interest("ex", 2, "Sara let the good memories back in.")
            call jacob_incontro_1_rivalutato
            return True
        "Keep the whole picture.":
            $ segna("jacob_1_quadro_intero")
            s "You've cut the trailer very well. I saw the film."
            jacob "That's what memories are for. The edit."
            s "Mine don't edit. That's sort of the problem."
            n "He laughs, not at all offended, and puts the bottle back on the shelf. One was one."
            $ via_cg()
            $ cg("Jacob holding the door of his closed club open for Sara, the street light outside, the bar lights going off behind him", "images/cg/ep2/jacob1_08_uscita.webp")
            $ suono("serranda")
            jacob "Same time next week? I'll bring better stories."
            s "Bring true ones."
            $ via_cg()
            return False

label jacob_incontro_1_rivalutato:
    s "The car. You fixed the wiper with my hair tie."
    jacob "It worked until the motorway."
    s "It worked until the first bend."
    n "It goes on like that. A story each. Hers are funnier. He tells her so, and he's right, and she stops keeping score of who's telling the better version."
    $ via_cg()
    $ cg("Sara laughing on the bar stool, head tipped back, Jacob grinning across the counter; the single glass nearly empty", "images/cg/ep2/jacob1_06_risata.webp")
    s "You haven't changed at all, Lighthouse."
    $ via_cg()
    $ cg("Close-up: Sara with a hand half-raised to her mouth, cheeks going red, the word still in the air", "images/cg/ep2/jacob1_07_silenzio.webp")
    n "The jukebox chooses that moment to finish its song."
    n "Lighthouse. Because he was the tallest thing in any room, and she always found her way back to him. She hasn't said it in four years. She hasn't thought it in three."
    pause 1.0
    $ via_cg()
    $ cg("Reverse angle on Jacob: a slow, satisfied smile, one finger lifted as if marking a point on a scoreboard", "images/cg/ep2/jacob1_09_punto.webp")
    jacob "Forty minutes."
    s "What?"
    jacob "Four years, and it took you forty minutes."
    menu:
        sp "He's going to be unbearable."
        "Give him the point, and laugh it off.":
            $ interest("ex", 1, "Sara laughed off the old nickname.")
            s "Fine. One point to you. Don't let it go to your head, there's already a lot of room up there."
            jacob "That's why they called me Lighthouse."
            s "Nobody called you Lighthouse. I called you Lighthouse."
            jacob "I know."
        "Don't. Don't make it a thing.":
            $ confidence(1, "Sara didn't let Jacob turn a slip into a win.")
            s "Don't. It's a word. I've had a glass of wine."
            jacob "One glass."
            s "And it was a word."
            n "He lifts both hands. The finger goes down. Point withdrawn, his face says, though not very far."
    $ via_cg()
    return

## Chiusura della serata dopo il rientro facoltativo «One more…» (la chiama il giorno).
label jacob_incontro_1_saluto:
    $ cg("Jacob holding the door of his closed club open for Sara, the street light outside, the bar lights going off behind him", "images/cg/ep2/jacob1_08_uscita.webp")
    $ suono("serranda")
    jacob "Same time next week?"
    s "Count to one first."
    $ via_cg()
    return
