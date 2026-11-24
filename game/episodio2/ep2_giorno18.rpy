## Giorno 18 · giovedì (docs/mese-1.md, decisioni del 24/11/2026).
## Lavoro, pranzo con Daniel solo se confermato il 15, mezz'ora con Barbara,
## sera da Howard con lo step successivo della scala delle visite.

label ep2_d18:
    call nuovo_giorno(18, "Lunch Hour")
    $ fascia_corrente = FASCE.index("mattina")
    call ep2_d18_mattina
    $ fascia_corrente = FASCE.index("lavoro")
    call ep2_d18_redazione
    $ fascia_corrente = FASCE.index("pranzo")
    if fatto("ep2_d18_pranzo_daniel_confermato"):
        call ep2_d18_pranzo_daniel
    else:
        call ep2_d18_pranzo_scrivania
    $ fascia_corrente = FASCE.index("lavoro")
    call ep2_d18_barbara
    $ fascia_corrente = FASCE.index("sera")
    call ep2_d18_howard
    $ musica(None)
    $ luogo_corrente = ""
    scene bg nero with fade
    return


## --- Mattina: cosa mettere e, se promesso il 13, avvisare Josh ---------------------------

label ep2_d18_mattina:
    $ vai("casa", "Home — Thursday morning")
    $ musica("casa")
    if not fatto("ep2_d18_pranzo_daniel_confermato"):
        $ cg("Sara drinks her coffee standing at the kitchen counter", "images/cg/ep2/d18_01_colazione.webp")
        n "[nome_compagno] has already left. His mug is in the sink, rinsed, upside down. Sara drinks her coffee standing up and takes her coat from the hook."
        $ via_cg()
        return

    $ cg("Sara stands at the open wardrobe on Thursday morning", "images/cg/ep2/d18_01_armadio.webp")
    n "Sara has been standing at the wardrobe long enough for her coffee to go cold on the dresser."
    sp "It's lunch. About the book. People have lunch about books all the time."
    ## Il top nero solo se è arrivato il 17 (decisione 24/11).
    if fatto("ep2_d17_top_ricevuto"):
        n "The black top is still over the back of the chair, where she left it last night."
    menu:
        sp "What do I wear to lunch with Daniel?"
        "Joanie's black top, under the blazer." if fatto("ep2_d17_top_ricevuto"):
            $ segna("ep2_d18_top_nero")
            $ corruption(1, "Sara wore Joanie's black top to lunch with Daniel.")
            $ via_cg()
            $ cg("Sara checks the black mesh top under her blazer in the mirror", "images/cg/ep2/d18_01a_top_nero.webp")
            n "She pulls the mesh over her head and smooths it down. The two dark circles sit exactly where Joanie meant them to. The sleeves turn her arms to shadow."
            n "With the blazer buttoned, it could almost pass for office wear. Almost. She undoes the button and looks again."
            sp "I'll do it up on the bus."
        "The good grey dress.":
            $ segna("ep2_d18_vestito_grigio")
            n "The grey dress is the one she wears when she wants to be taken seriously. It does that. It also does a little more than that, and she knows it."
        "My usual work clothes.":
            n "Trousers, blouse, flat shoes. If anyone asks, it's just a Thursday."
    $ via_cg()

    ## La promessa del giorno 13: «Josh will know» va rispettata prima del pranzo.
    if fatto("ep1_d13_pranzo_no"):
        call ep2_d18_avvisa_josh
    return

label ep2_d18_avvisa_josh:
    $ segna("ep2_d18_josh_avvisato")
    $ chat_aperta = "josh"
    show screen telefono_chat("josh")
    n "On the bus she opens [nome_compagno]'s chat. The last message is from Tuesday, a photo of a sandwich. Nothing since Monday night."
    sp "I said he'd know. So he'll know."
    $ msg("sara", "I'm having lunch with Daniel today. He wants to talk about the book and Magnus. Just so you know.", premia_avvio=False)
    n "The two ticks turn blue almost at once. Then nothing, for a whole stop."
    $ msg("josh", "Daniel? Ok. Sure.")
    $ msg("josh", "That's good, actually. If he's interested, that's a big deal. Don't let me get in the way.")
    $ msg("josh", "He's keeping me late tonight anyway. Back around nine.")
    hide screen telefono_chat
    $ chat_aperta = None
    n "Sara reads «Don't let me get in the way» twice. She doesn't know if it's kindness or if he just can't say no to anything with Daniel's name on it."
    return


## --- Lavoro ------------------------------------------------------------------------

label ep2_d18_redazione:
    $ vai("redazione", "The newsroom — Thursday morning")
    $ musica("redazione")
    $ ambiente("redazione")
    $ cg("Sara at her desk on Thursday morning, Jessica leaning over the partition", "images/cg/ep2/d18_02_redazione.webp")
    n "Jessica leans over the partition with yesterday's proofs in her hand."
    je "They've put the website pictures up on the shared drive. Yours is in the folder already."
    s "Is it awful?"
    je "It's not awful."
    if fatto("ep2_d17_glamour"):
        je "It's not very you either. Or it's very you and nobody knew."
    else:
        je "You look like you're about to ask the photographer a question."
    s "I was."
    if fatto("ep2_d18_pranzo_daniel_confermato"):
        n "Sara checks the time in the corner of the screen. Then again, four minutes later."
        if fatto("ep2_d18_top_nero"):
            n "She keeps her blazer buttoned all morning. Jessica notices, and decides not to say anything. Sara can see her deciding."
    $ ambiente(None)
    $ via_cg()
    return


## --- Pausa pranzo senza Daniel ------------------------------------------------------------

label ep2_d18_pranzo_scrivania:
    $ vai("redazione", "The newsroom — Lunch break")
    $ cg("Sara eats lunch at her desk with her notebook open", "images/cg/ep2/d18_03_pranzo_scrivania.webp")
    n "Sara eats at her desk with her notebook open beside the sandwich. She writes three lines and crosses out two."
    if fatto("ep1_d13_pranzo_forse"):
        sp "«One day.» Daniel never said which day."
        n "Her phone stays dark. She turns it face down anyway."
    $ via_cg()
    return


## --- Pausa pranzo con Daniel --------------------------------------------------------------
## Il privato (24/11): solo se il 13 hanno dondolato sulla terrazza (video C), oppure col
## top nero e Corruption ≥ 20. Altrimenti il pranzo resta su romanzo e Magnus.

label ep2_d18_pranzo_daniel:
    $ segna("ep2_d18_pranzo_daniel")
    $ vai("ristorante", "Ristorante Verde — a private room, 1 p.m.")
    $ musica("ristorante")
    $ cg("A small private dining room: Daniel already seated, standing as Sara comes in", "images/cg/ep2/d18_04_saletta.webp")
    n "The waiter doesn't take her to a table. He takes her down a corridor to a door with no number on it, and opens it for her."
    n "A small room. One table, laid for two. A window onto a courtyard with a fig tree. Daniel is already there, and stands up when she comes in."
    da "Sara. You came."
    s "I said I would."
    da "You did. In writing. I've kept it."
    if fatto("ep2_d18_top_nero"):
        n "He doesn't look at the blazer. He looks at what the blazer doesn't quite close over, and then at her face, without hurrying either."
        da "Joanie's taste or yours?"
        s "How do you know Joanie has taste?"
        da "Because you'd never have bought that for yourself. And you wore it anyway."
    elif fatto("ep2_d18_vestito_grigio"):
        da "Grey. Very serious. You dressed to be listened to."
        s "Is it working?"
        da "I'm listening."
    n "He pulls out her chair. When she sits, his hand rests on the back of it a moment longer than a waiter's would."

    $ via_cg()
    $ cg("Daniel and Sara at the table, a basket of bread between them, Daniel turning his glass", "images/cg/ep2/d18_05_tavolo.webp")
    da "I've ordered for both of us. If you hate it, you can tell me. Nobody ever does."
    s "Maybe I'll be the first."
    da "I hope so."
    da "Magnus has your pages."
    s "Since Monday night."
    da "He hasn't said a word to me about them. Not one. That's how I know he's read them."
    s "Is that good?"
    da "Magnus talks about the books he doesn't care about. The ones he wants, he keeps to himself. Like a man with a good bottle."
    da "What happens to her? Your girl on the terrace."
    sp "He remembers the terrace. Of course he does."
    s "She has a choice to make."
    da "And she makes it?"
    s "On page fifty."
    da "Which way?"
    n "Sara tears a piece of bread in half. She could tell him. She could tell him exactly what the woman on page fifty does, and watch his face while she does it."
    s "You'll have to read it."
    da "Then I'll read it."

    ## Josh: Daniel lo sfotte (24/11). Stasera lo tiene in ufficio lui.
    da "I'll have plenty of time this evening. [nome_compagno] won't. I've given him the Harrow contracts to do again."
    s "Again?"
    da "He photocopied page four upside down. Twice. I've started to think he does it on purpose, so he has something to apologise for."

    if fatto("ep1_d13_videoclip") or (fatto("ep2_d18_top_nero") and sara_corruption >= 20):
        call ep2_d18_privato
    else:
        call ep2_d18_professionale
    $ via_cg()
    return

label ep2_d18_professionale:
    menu:
        sp "He's talking about [nome_compagno]."
        "Laugh.":
            $ interest("daniel", 1, "Sara laughed at his joke about Josh.")
            n "It comes out before she can stop it. A short laugh, into her napkin."
            da "There. You see? You're allowed."
            sp "I shouldn't have laughed. It was funny, though. That's the worst part."
        "«Don't talk about him like that.»":
            $ confidence(1, "Sara stopped Daniel mocking Josh.")
            s "Don't talk about him like that. Not to me."
            da "Fair enough. Not to you."
            n "He says it as if he were writing it down somewhere, to be looked at later."
    $ via_cg()
    $ cg("Daniel signs the bill without looking at it while Sara puts on her coat", "images/cg/ep2/d18_06_conto.webp")
    n "The rest of lunch is about the book. He asks good questions, the kind that make her want to go home and write. At ten to two he signs the bill without looking at it."
    da "Saturday, Magnus will want to see you. Wear something you can think in."
    s "Is that advice?"
    da "That's an order. I'm told you don't take them."
    n "Outside, the air is cold. She realizes she's smiling and stops, and then starts again on the bus."
    return

label ep2_d18_privato:
    $ segna("ep2_d18_privato")
    n "He's watching her when he says it. Not [nome_compagno]'s name. Her."
    da "You don't mind. I can tell. You're trying very hard to mind."
    menu:
        sp "He's waiting to see what I'll do."
        "«Go on, then. What else did he do?»" if sara_corruption > 25:
            ## Non lo confessa: lo fa capire con una battuta (24/11).
            $ segna("ep2_d18_lascia_proseguire")
            $ interest("daniel", 2, "Sara let him go on about Josh.")
            $ corruption(2, "Sara let Daniel go on about Josh, and liked it.")
            s "Go on, then. What else did he do? I've got until two."
            n "Daniel's eyebrows lift, just slightly. It's the first time she has seen him surprised. He hides it quickly, but she saw."
            da "He thanked me. After I told him. He thanked me for the chance to do it again."
            s "He does that."
            da "I know. And you know. And now we both know you like hearing it."
            s "I didn't say that."
            da "You didn't have to. You asked for more."
            sp "I did. I asked for more."
        "Laugh.":
            $ interest("daniel", 1, "Sara laughed at his joke about Josh.")
            n "She laughs into her glass. She doesn't look away while she does it."
            da "That's better."
        "«Don't talk about him like that.»":
            $ confidence(1, "Sara stopped Daniel mocking Josh.")
            s "Don't. Not to me."
            da "As you like."
            n "He doesn't apologise. He just lets the silence sit there until she's the one who wants to fill it."

    $ via_cg()
    $ cg("Daniel stands by a small speaker on the sideboard, phone in hand, looking back at Sara", "images/cg/ep2/d18_07_musica.webp")
    if fatto("ep1_d13_videoclip"):
        ## Il 13 hanno dondolato: Sara sogna di rifarlo e Daniel glielo concede.
        n "There's a small speaker on the sideboard, playing something quiet with strings. Sara has heard a different song in her head since Saturday. In the shower. On the bus. Over the sound of [nome_compagno] asking if she wanted tea."
        sp "The terrace. His hands. The song. I keep going back there."
        n "Daniel gets up, as if she had said it out loud. He picks up his phone and scrolls without hurrying."
        da "You've been humming it. Did you know? Since you sat down."
        s "I haven't."
        da "You have. Under your breath. I'd know that one anywhere. I chose it."
        n "He touches the screen. The first low notes come out of the little speaker, and Sara's whole body remembers before she does."
        da "Come here."
    else:
        n "There's a small speaker on the sideboard, playing something quiet with strings. Daniel gets up, picks up his phone and changes it."
        n "A woman's voice, low and close, over a slow beat. Sara knows it from somewhere. The party. It was playing on the terrace."
        da "I don't dance at parties. Too many people watching."
        da "Here, nobody's watching."
        da "Come here."

    menu:
        sp "He's holding out his hand."
        "Take his hand.":
            pass
        "«Not here.»":
            $ confidence(1, "Sara turned down the dance.")
            s "Not here, Daniel."
            n "He lowers his hand, without hurry. He turns the music down, not off."
            da "Not here. That's not a no. I'll take it."
            n "They finish their coffee. The song plays to the end, quietly, and Sara listens to all of it."
            sp "That's not a no. He's right, and he knows he's right."
            return

    $ segna("ep2_d18_ballo")
    if fatto("ep1_d13_videoclip"):
        $ segna("ep2_d18_ballo_ripetuto")
        $ interest("daniel", 3, "Sara danced with him again.")
        $ corruption(3, "Sara danced with Daniel again.")
    else:
        $ interest("daniel", 3, "Sara danced with him for the first time.")
        $ corruption(2, "Sara danced with Daniel for the first time.")

    ## La sequenza a tempo sulla canzone della terrazza, come il 13 (avviso e salto).
    n "{i}The next scene plays to music and runs on its own, about three minutes.{/i}"
    menu:
        "Watch the scene.":
            call ep2_d18_ballo(True)
        "Skip the scene.":
            call ep2_d18_ballo(False)
    return


## --- Il ballo nella saletta (24/11) --------------------------------------------------------
## Stessa canzone e stessi tempi della terrazza (0:49, 1:18, 2:00, 2:29). Il passo in più:
## se il 13 c'è stato il bacio sull'orecchio (cerniera), oggi collo, mandibola e angolo
## della bocca, poi lui si ferma; altrimenti oggi arriva il bacio sull'orecchio.

init python:
    def d18_sequenza(righe, a_tempo):
        """righe: (secondi, tipo, a, b). Tipi: quadro (file, descrizione), video
        (file, (riserva, descrizione)), riga (chi, testo), pensiero (None, testo)."""
        for t, tipo, a, b in righe:
            if a_tempo:
                vc_a(t)
                if tipo == "quadro":
                    vc_quadro(a, b)
                elif tipo == "video":
                    vc_video(a, b[0], b[1])
                elif tipo == "riga":
                    vc_riga(a, b, VC_DANIEL if a == "Daniel" else VC_SARA)
                else:
                    vc_riga(None, b, pensiero=True)
            else:
                if tipo == "quadro":
                    cg(b, a)
                elif tipo == "video":
                    cg(b[1], b[0])
                elif tipo == "riga":
                    renpy.say(store.da if a == "Daniel" else store.s, b)
                else:
                    renpy.say(store.sp, b)
        if a_tempo:
            vc_via()

define D18_ABBRACCIO = "images/cg/ep2/d18_08_abbraccio.webp"
define D18_PP_DANIEL = "images/cg/ep2/d18_08c_daniel_pp.webp"
define D18_PP_SARA = "images/cg/ep2/d18_08d_sara_pp.webp"

label ep2_d18_ballo(a_tempo):
    $ renpy.block_rollback()
    $ luogo_corrente = ""
    if a_tempo:
        $ vc_inizia()
    else:
        $ musica("daniel_seduzione")
    python:
        righe = [
            (0, "quadro", D18_ABBRACCIO, "Daniel draws Sara in by the waist in the small private room, the fig tree in the window behind them"),
            (3, "riga", "Daniel", "Closer. I won't break."),
            (8, "quadro", D18_PP_SARA, "Close-up of Sara against Daniel's shoulder, eyes half closed"),
            (8, "pensiero", None, "His hand on my back. Exactly where it was."
                if fatto("ep1_d13_videoclip") else "I've never danced with anyone but [nome_compagno]. Not like this."),
            (15, "riga", "Sara", "Someone could come in."),
            (19, "quadro", D18_PP_DANIEL, "Close-up of Daniel, amused, looking down at her"),
            (19, "riga", "Daniel", "Nobody comes in unless I call them."),
            (26, "riga", "Daniel", "He'll be at the photocopier by now. Page four. Right way up, if he's lucky."),
            (33, "quadro", D18_PP_SARA, "Close-up of Sara biting back a smile"),
            (33, "pensiero", None, "I should tell him to stop. I'm smiling."),
            (40, "riga", "Daniel", "You're smiling."),
            (44, "riga", "Sara", "I'm not."),
            ## Ritornello 1: il dondolio.
            (49, "video", "images/video/ep2/d18_va_dondolio.webm", (D18_ABBRACCIO, "Daniel and Sara sway together, her forehead nearly at his collar")),
            (64, "riga", "Daniel", "You've been thinking about this since Saturday." if fatto("ep1_d13_videoclip") else "You've been wanting to do this since the terrace."),
            (70, "riga", "Sara", "You don't know that."),
            (74, "riga", "Daniel", "I know exactly where to put my hands. So do you."),
            ## Strofa 2: lui la gira piano, la tiene più stretta.
            (78, "video", "images/video/ep2/d18_vb_giro.webm", (D18_ABBRACCIO, "Daniel turns Sara slowly in his arms, her back to the window")),
            (93, "quadro", D18_PP_DANIEL, "Close-up of Daniel, his mouth near her hair"),
            (93, "riga", "Daniel", "Does he dance with you?"),
            (98, "quadro", D18_PP_SARA, "Close-up of Sara, eyes closed"),
            (98, "riga", "Sara", "He steps on my feet."),
            (102, "riga", "Daniel", "Of course he does."),
            (106, "pensiero", None, "That was unkind. I said it to make him say that."),
            (112, "riga", "Daniel", "Say something else unkind. I like it on you."),
            ## Ritornello 2: le mani sui fianchi, più vicini.
            (120, "video", "images/video/ep2/d18_vc_fianchi.webm", (D18_ABBRACCIO, "Daniel's hands low on Sara's hips as they sway, her hands flat on his chest")),
            (135, "riga", "Daniel", "Don't move."),
        ]
        if fatto("ep1_d13_cerniera"):
            ## Il passo in più: dall'orecchio alla bocca, senza arrivarci.
            righe += [
                (149, "video", "images/video/ep2/d18_vd_mandibola.webm", ("images/cg/ep2/d18_09_mandibola.webp", "Daniel's lips trace from below Sara's ear down her jaw, stopping at the corner of her mouth; her eyes closed, her face turning toward him")),
                (156, "pensiero", None, "Below my ear. Then lower. Then my jaw."),
                (161, "pensiero", None, "The corner of my mouth. Turn. Just turn your head."),
                (166, "quadro", "images/cg/ep2/d18_09b_si_ferma.webp", "Sara turns her face to meet him; Daniel has already drawn back an inch, smiling"),
                (167, "riga", "Daniel", "Not today."),
            ]
        else:
            righe += [
                (149, "video", "images/video/ep2/d18_vd_orecchio.webm", ("images/cg/ep2/d18_09c_orecchio.webp", "Daniel kisses Sara just below the ear as they sway; she tilts her head, offering her neck")),
                (156, "pensiero", None, "Just below my ear. And I'm tilting my head."),
                (162, "riga", "Daniel", "There you are."),
            ]
        d18_sequenza(righe, a_tempo)

    if fatto("ep1_d13_cerniera"):
        $ segna("ep2_d18_angolo_bocca")
        n "She has turned her face to meet him, and he isn't there. He's an inch away, smiling, as if he'd won something small and was saving the big prize for later."
        s "That's cruel."
        da "That's a promise. There's a difference. You'll learn it."
        sp "I turned my head. I would have let him. I wanted him to."
        sp "And he's the one who stopped."
    else:
        $ segna("ep2_d18_bacio_orecchio")
        n "He kisses her below the ear, lightly, and she tilts her head before she can decide not to. Daniel steps back and straightens her collar for her, the way he'd straighten a frame."
        da "Two o'clock. You'll be late for Barbara."
        sp "My neck. I gave him my neck. And he gave me back my collar."
    $ via_cg()
    $ musica("ristorante")
    $ vai("ristorante", "Ristorante Verde — 1:55 p.m.")
    n "He walks her to the door of the restaurant and doesn't touch her again, not even to say goodbye. That is somehow worse."
    $ nota_sara("daniel", "We danced in a little room with a fig tree in the window. His song. He stopped before I wanted him to.")
    return


## --- Fine giornata: mezz'ora con Barbara ---------------------------------------------------

label ep2_d18_barbara:
    $ vai("redazione", "The newsroom — 5:30 p.m.")
    $ musica("redazione")
    $ cg("Barbara at her office door, holding a folder of prints, calling Sara over", "images/cg/ep2/d18_10_barbara.webp")
    n "Sara has her coat half on when Barbara appears in her office doorway with a folder of prints."
    ba "Sara. Have you got half an hour? I need to pick your portrait for the website, and I'd rather not do it without you."
    if sara_stagista:
        ba "Consider it part of your internship. The ordinary part."
    menu:
        sp "Half an hour more."
        "«Of course.»":
            $ segna("ep2_d18_resta_barbara")
            $ interest("capa", 1, "Sara stayed late to help Barbara.")
            $ via_cg()
            $ vai("redazione", "Barbara's office")
            if fatto("ep2_d17_glamour"):
                $ cg("Barbara spreads Sara's glamour portraits across her desk", "images/cg/ep2/d18_11_ritratti_glamour.webp")
            else:
                $ cg("Barbara spreads Sara's portraits across her desk", "images/cg/ep2/d18_11_ritratti.webp")
            n "Barbara lays six prints out on her desk in two rows. Five of them are the website portrait. Sara can see the sixth is different from across the room. Barbara turns it face down without comment."
            ba "Which one?"
            s "The first. I wasn't posing yet."
            ba "That's the one I'd have chosen. Good. You know your own face."
            n "Barbara writes something on a sticky note and holds it out between two fingers. A phone number."
            ba "For things that can't wait until morning. There won't be many."
            $ da_numero("capa")
            s "Thank you."
            ba "Don't thank me. Use it properly."
        "«I'm sorry, I can't tonight.»":
            $ confidence(1, "Sara politely declined to stay late.")
            s "I'm sorry, Barbara. I can't tonight. Tomorrow morning, first thing?"
            ba "Tomorrow morning, then."
            n "Barbara goes back into her office. She doesn't seem annoyed. She seems to be making a note of it."
    $ via_cg()
    return


## --- Sera: Howard, scala delle visite (21/11) ----------------------------------------------
## Ogni incontro un invito. howard_visite: 1 → step 2 (tazze), 2 → step 3 (lampadina),
## 3 o più → step 4 (ragù). Accettare: Howard +2 (calendario). Il rifiuto è grigio col
## Complesso. Il 18 non si chiama il giro delle faccende: Howard la incontra per l'invito.

label ep2_d18_howard:
    $ vai("pianerottolo", "The landing — Thursday evening")
    $ musica("casa")
    if fatto("ep2_d18_josh_avvisato"):
        n "[nome_compagno] said nine. The flat will be dark for another three hours."
    else:
        $ chat_aperta = "josh"
        show screen telefono_chat("josh")
        $ msg("josh", "Daniel's got me redoing Harrow. Back around nine. Sorry. Eat without me")
        hide screen telefono_chat
        $ chat_aperta = None
    $ cg("Howard on the landing in his cardigan, holding his door open", "images/cg/ep1/d9_04_howard_porta.webp")
    n "Howard's door opens before she has found her keys. He must have heard her on the stairs."
    if howard_visite <= 1:
        ho "Sara. The cups. The new ones. I keep washing them and nobody drinks out of them."
    elif howard_visite == 2:
        ho "Sara. I hate to ask. The bulb in my bathroom. I stood on the edge of the bath and my knees told me not to be stupid."
    else:
        ho "Sara. Do you like ragù? Real ragù. My mother's. I'm the only one alive who knows how to make it, and I can't eat four portions."
    n "He's looking at his slippers. The hopeful face of a dog who already expects to be told no."
    menu:
        sp "Go to Howard's?"
        "Go in.":
            $ interest("howard", 2, "Sara came round on Thursday evening.")
            $ howard_visite += 1
            $ segna("ep2_d18_visita_howard")
            if howard_visite <= 2:
                call ep2_d18_howard_tazze
            elif howard_visite == 3:
                call ep2_d18_howard_lampadina
            else:
                call ep2_d18_howard_ragu
        "«Not tonight, Howard.»" (rifiuto_howard=True):
            $ segna("ep2_d18_rifiuta_howard")
            s "Not tonight, Howard. Another time."
            ho "Another time. Of course. I'm always here."
            n "He closes the door very gently, as if it were her he were trying not to wake."
    $ via_cg()
    if fatto("ep2_d18_ballo"):
        $ vai("casa", "Home — Thursday night")
        n "Later, alone on the sofa with the television off, Sara hears the song again. Not in the room. In her shoulders, where his hands were."
    return

label ep2_d18_howard_tazze:
    $ vai("casa_howard", "Howard's flat — 6:30 p.m.")
    $ ambiente("tv_howard")
    $ cg("Howard pours coffee into two new white cups; Sara on his sofa with her notebook", "images/cg/ep1/d11_08_tazze_nuove.webp")
    n "The flat is a little tidier than she remembers. By accident, he says. The newspapers have found a corner. The two white cups are on the table, side by side."
    ho "Tell me about your book. I've never known anyone who writes a book."
    n "So she does. Not the terrace. The other parts. When he asks to hear a bit, she reads him a paragraph about the heroine's mother, from her phone."
    ho "You make me see her. The mother. I could pick her out on a bus."
    n "He says it shyly, almost apologising. Nobody has said that about her mother-character before. Sara had worried she was the weakest part."
    menu:
        sp "Another coffee?"
        "Another cup.":
            $ interest("howard", 2, "Sara stayed for a second coffee.")
            n "The second coffee lasts an hour. He tells her about the factory canteen, where the cook used to keep a cat in the larder."
        "«I'd better go.»" (rifiuto_howard=True):
            $ interest("howard", 1, "A coffee in the new cups.")
            ho "Of course. You've worked all day."
    $ ambiente(None)
    return

label ep2_d18_howard_lampadina:
    $ vai("casa_howard", "Howard's bathroom — 6:30 p.m.")
    $ cg("Sara standing on Howard's bathtub edge to change a bulb, Howard holding her steady from below and looking up", "images/cg/ep2/d18_12_lampadina.webp")
    n "The bathroom is dark. The new bulb is waiting on the edge of the sink, out of its box already."
    if complesso_crocerossina:
        ho "Shoes off, my dear. The bath is slippery. I'd never forgive myself."
        sp "Shoes off. Again. It's safer. It's nothing."
        n "She's out of them before she has finished the thought."
    n "Sara stands on the edge of the bath. Howard holds her by the hips, very correctly, and looks up."
    ho "You know, from down here... it's a lot better than the ceiling."
    n "She understands exactly what he means. The blouse. The angle. Her face goes hot."
    menu:
        sp "Howard!"
        "Laugh and give it back.":
            $ segna("ep2_d18_battuta_howard")
            $ corruption(1, "Sara laughed at Howard's joke and gave it back.")
            s "Howard, do you always think about things like that?"
            ho "At my age? Only on Thursdays."
            n "She laughs so much she nearly drops the bulb. He holds her a little tighter, for safety."
        "Get down and leave it there.":
            n "She screws the bulb in and climbs down without a word. Howard is suddenly very interested in the light."
            ho "Look at that. Like day. You're a marvel."
    return

label ep2_d18_howard_ragu:
    $ vai("casa_howard", "Howard's kitchen — 6:30 p.m.")
    $ ambiente("tv_howard")
    $ cg("Howard's small kitchen: Sara at the stove with a wooden spoon, Howard behind her, his hands over hers on the spoon", "images/cg/ep2/d18_13_ragu.webp")
    n "Howard's kitchen smells of onions and red wine. A pot the size of a bucket is already ticking on the stove."
    ho "Slowly. Always the same way. You stir it like you're telling it a secret."
    n "He stands behind her and puts his hands over hers on the spoon. He's not tall. His chin is about level with her shoulder, and his eyes are a good deal lower than that."
    ho "My mother had a figure like yours. Well. Not quite like yours. Nobody has a figure quite like yours."
    if complesso_crocerossina:
        sp "I should say something. Move. Why am I still stirring?"
        sp "It's only cooking. It's nothing serious."
    menu:
        sp "His hands are still on hers."
        "Let him guide the spoon.":
            $ segna("ep2_d18_ragu_mani")
            $ interest("howard", 2, "Sara let him guide her hands at the stove.")
            n "She lets him. Round and round, slowly. He tells her the whole story of the recipe, and none of it is about the recipe."
        "Step aside and hand him the spoon.":
            s "Show me. I'll watch."
            ho "Of course. Watching is how I learned."
    n "They eat at his little table. When she leaves, he gives her a jar of sauce wrapped in a tea towel."
    ho "For [nome_compagno]. Tell him the neighbour made it. That's all he needs to know."
    $ nota_sara("howard", "His mother's ragù. A jar for [nome_compagno], wrapped in a tea towel.")
    $ ambiente(None)
    return
