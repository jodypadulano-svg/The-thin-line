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
    ## Variante col top nero sotto il blazer (24/11), altrimenti la camicetta da lavoro.
    if fatto("ep2_d18_top_nero"):
        $ cg("Sara at her desk in her blazer and black top, Jessica leaning over the partition", "images/cg/ep2/d18_02b_redazione_top.webp")
    else:
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
    ## Sara «ragazzina» (24/11): fiducia e intimità, solo con Interest Daniel ≥ 12 all'arrivo.
    $ segna("ep2_d18_ragazzina", valore_interest("daniel") >= 12)
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
    if fatto("ep2_d18_ragazzina"):
        call ep2_d18_ragazzina

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
    if fatto("ep2_d18_ragazzina"):
        call ep2_d18_dopo_conto
    if fatto("ep2_d18_ballo"):
        $ musica("ristorante")
        $ vai("ristorante", "Ristorante Verde — 1:55 p.m.")
        if fatto("ep2_d18_sfotto_josh"):
            n "He walks her to the door of the restaurant with his hand at the small of her back, the whole way, as if the corridor belonged to him. She lets it stay there."
        else:
            n "He walks her to the door of the restaurant and doesn't touch her again, not even to say goodbye. That is somehow worse."
        $ nota_sara("daniel", "We danced in a little room with a fig tree in the window. His song. He stopped before I wanted him to.")
    else:
        $ vai("strada", "Outside the restaurant — 2 p.m.")
        n "Outside, the air is cold. She realizes she's smiling and stops, and then starts again on the bus."
    $ via_cg()
    return


## --- Sara «ragazzina» (24/11) -------------------------------------------------------------
## Solo con Interest Daniel ≥ 12: non sta composta, confessa l'abito, gli ruba il pane.
## Nessun effetto numerico: è il segno della fiducia. Niente teasing in questo momento.

label ep2_d18_ragazzina:
    $ via_cg()
    $ cg("Sara at the table, blushing, confessing something with a hand half over her mouth; Daniel listening, surprised", "images/cg/ep2/d18_05b_confessione.webp")
    n "She means to sit the way she sits at work. Back straight, napkin on her knee. It lasts about four seconds."
    s "Can I tell you something stupid?"
    da "Please."
    if fatto("ep2_d18_top_nero"):
        s "Joanie bought it. The top. As a joke, sort of. But this morning I picked it. For you."
        s "I didn't even think about it. I just knew it was the one I'd wear to see you."
        n "She hears it out loud and her hand flies up to her mouth, too late."
        s "Oh God. Forget I said that."
    elif fatto("ep2_d18_vestito_grigio"):
        s "I changed three times this morning. Three. I ended up in the first one."
        s "I wanted you to think I look like this every Thursday."
        n "She laughs at herself before he can, a hand over her mouth."
    else:
        s "I changed three times this morning. And then I put my work clothes back on, so it wouldn't look like I'd changed three times."
        n "She laughs at herself before he can, a hand over her mouth."
    da "I'm not going to forget a word of it."

    $ via_cg()
    $ cg("Sara with her elbows on the table and her chin in her hands, beaming, leaning toward Daniel as she talks", "images/cg/ep2/d18_05c_raggiante.webp")
    n "Then the words start and she can't stop them. Elbows on the table, chin in her hands. The website photo. The yellow slip under her monitor. Fifty pages sent at midnight, with her own name at the bottom."
    s "And Jess said my portrait looks like I'm about to ask the photographer a question. Which I was. I was going to ask him if I could—sorry. I'm talking too much."
    da "You're not."
    s "I am. I can hear myself."
    da "Then keep going. I want to hear the rest."
    sp "I'm happy. I don't even care if he can see it."

    $ via_cg()
    $ cg("Sara steals a piece of bread from Daniel's plate and bites it, looking straight at him; Daniel laughing openly", "images/cg/ep2/d18_05d_pane.webp")
    n "His bread is on the side of his plate, untouched. Sara reaches across, takes it, and bites into it, looking him straight in the eye."
    s "You weren't eating it."
    n "For a second Daniel just looks at her. Then he laughs. Not the half smile she knows. A real laugh, surprised out of him, his head back."
    da "Nobody has taken food off my plate since I was nine years old."
    s "Then you were overdue."
    da "I've never seen you like this, Sara."
    s "Like what?"
    da "Happy where I can see it. I like it. I like it more than I expected to."
    n "She feels her face go hot. She doesn't look away and she doesn't stop smiling."
    return


## --- Dopo il conto (24/11): il bacio sulla guancia e lo sfottò di Josh ---------------------

label ep2_d18_dopo_conto:
    $ via_cg()
    $ cg("Standing by the door of the private room, Sara rises on her toes to kiss Daniel's cheek; he has just put his wallet away", "images/cg/ep2/d18_06b_bacio_guancia.webp")
    if not fatto("ep2_d18_professionale"):
        n "The bill comes in a leather folder. Daniel signs it without looking."
    n "Sara is on her feet before he is, almost bouncing. At the door she rises on her toes and kisses his cheek, quickly, the way she'd thank a friend who'd given her the best afternoon of her week."
    s "Thank you. Really. This was the nicest lunch I've ever had."
    s "You're the most interesting man I've ever sat across a table from."
    n "Daniel doesn't move. He looks at her the way he looks at a contract, to see exactly how much it's worth."
    da "Interesting. Not like the one at home, then. Doing page four again, right way up, if he's lucky."
    menu:
        sp "He's waiting to hear what I'll say."
        "«Come on. Don't say that.»":
            s "Come on. Don't say that."
            n "She says it lightly, with a little push to his arm. Daniel smiles as if he'd lost nothing at all."
            da "As you like."
        "Give him exactly what he wants.":
            call ep2_d18_premio
    return

label ep2_d18_premio:
    ## Prima volta che Sara partecipa allo sfottò su Josh: non da ragazzina, da donna
    ## seducente. Ha capito che prevalere su Josh è ciò che eccita Daniel, e glielo regala.
    $ segna("ep2_d18_sfotto_josh")
    $ interest("daniel", 3, "Sara joined in, and gave him exactly what he wanted.")
    $ corruption(3, "Sara mocked Josh for Daniel, on purpose.")
    sp "That's what he wants. Not me laughing. Me choosing. Him over [nome_compagno]."
    sp "Just once. I can give him that."
    if renpy.loadable("images/video/ep2/d18_06c_premio.webm"):
        $ filmato("images/video/ep2/d18_06c_premio.webm", stop_music=False)
        $ via_cg()
        $ cg("Daniel holds Sara by the nape of her neck, a breath from her mouth, her eyes in his", "images/cg/ep2/d18_06c_premio.webp")
    else:
        $ via_cg()
        $ cg("Daniel holds Sara by the nape of her neck, a breath from her mouth, her eyes in his", "images/cg/ep2/d18_06c_premio.webp")
        n "The girl who stole his bread is gone. Sara steps close, slowly, and straightens his collar with two fingers. When she speaks, her voice is low and very near his mouth."
        s "He'd have asked me if he could pay. And then said sorry for asking."
        n "Daniel's hand comes up to the back of her neck and holds her there, a breath away."
        da "Say it again."
        s "He'd have said sorry."
    n "Daniel lets her go with the slow smile of a man who has just won, and collected."
    da "Thank you, Sara. That was the best part of lunch."
    n "She smooths her hair. Her hands aren't quite steady, and her smile is enormous."
    sp "I gave it to him. On purpose. And I liked giving it."
    $ nota_sara("daniel", "I said it for him. About [nome_compagno]. He made me say it twice, and I did.")
    return

label ep2_d18_professionale:
    $ segna("ep2_d18_professionale")
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
            if fatto("ep2_d18_top_nero"):
                ## Il blazer resta sulla sedia: nel ballo si vede il top (24/11).
                n "Sara stands and slips off her blazer. She hangs it on the back of her chair, taking her time, and only then gives him her hand."
                n "His palm settles at her waist, on the mesh. She feels the warmth of it through the holes, on her bare skin."
        "«Not here.»":
            $ confidence(1, "Sara turned down the dance.")
            s "Not here, Daniel."
            n "He lowers his hand, without hurry. He turns the music down, not off."
            da "Not here. That's not a no. I'll take it."
            n "They finish their coffee. The song plays to the end, quietly, and Sara listens to all of it."
            sp "That's not a no. He's right, and he knows he's right."
            return

    ## Il dondolio (24/11): lei davanti, lui dietro, come alla cerniera del 13.
    n "Daniel turns her gently by the shoulders until she's facing the window, and steps in close behind her. The fig tree. The courtyard. His chest against her back."
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
    def d18_video(video, riserva, descrizione="", fine=None):
        """Come vc_video del giorno 13, ma a video finito resta un'immagine (fine o la
        riserva) invece dello schermo vuoto: i video possono durare meno della finestra."""
        renpy.hide_screen("battuta_tempo")
        if renpy.loadable(video):
            renpy.hide_screen("segnaposto_cg")
            dopo = fine if fine and renpy.loadable(fine) else riserva
            renpy.show("cg_corrente", what=Movie(play=video, loop=False, size=(config.screen_width, config.screen_height),
                                                 image=Transform(dopo, fit="cover", xysize=(config.screen_width, config.screen_height)) if renpy.loadable(dopo) else None))
            renpy.with_statement(dissolve)
        else:
            vc_quadro(riserva, descrizione)

    def d18_sequenza(righe, a_tempo):
        """righe: (secondi, tipo, a, b). Tipi: quadro (file, descrizione), video
        (file, (riserva, descrizione)), riga (chi, testo), pensiero (None, testo)."""
        for t, tipo, a, b in righe:
            if a_tempo:
                vc_a(t)
                if tipo == "quadro":
                    vc_quadro(a, b)
                elif tipo == "video":
                    d18_video(a, b[0], b[1], b[2] if len(b) > 2 else None)
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
            (0, "quadro", D18_ABBRACCIO, "Daniel stands close behind Sara, his hands on her waist, both facing the fig tree window; the door shut"),
            (3, "riga", "Daniel", "Closer. I won't break."),
            (8, "quadro", D18_PP_SARA, "Close-up of Sara leaning back against Daniel's chest, eyes half closed"),
            (8, "pensiero", None, "His hand on my back. Exactly where it was."
                if fatto("ep1_d13_videoclip") else "I've never danced with anyone but [nome_compagno]. Not like this."),
            (15, "riga", "Sara", "Someone could come in."),
            (19, "quadro", D18_PP_DANIEL, "Close-up of Daniel over Sara's shoulder, amused, looking down at her"),
            (19, "riga", "Daniel", "Nobody comes in unless I call them."),
            (26, "riga", "Daniel", "He'll be at the photocopier by now. Page four. Right way up, if he's lucky."),
            (33, "quadro", D18_PP_SARA, "Close-up of Sara biting back a smile"),
            (33, "pensiero", None, "I should tell him to stop. I'm smiling."),
            (40, "riga", "Daniel", "You're smiling."),
            (44, "riga", "Sara", "I'm not."),
            ## Ritornello 1: il dondolio.
            (49, "video", "images/video/ep2/d18_va_dondolio.webm", (D18_ABBRACCIO, "Daniel and Sara sway together, he behind her, her back against his chest")),
            (64, "riga", "Daniel", "You've been thinking about this since Saturday." if fatto("ep1_d13_videoclip") else "You've been wanting to do this since the terrace."),
            (70, "riga", "Sara", "You don't know that."),
            (74, "riga", "Daniel", "I know exactly where to put my hands. So do you."),
            ## Strofa 2: lui la gira piano, la tiene più stretta.
            (78, "video", "images/video/ep2/d18_vb_giro.webm", (D18_ABBRACCIO, "Daniel's mouth at Sara's hair as they sway, one hand flat on the mesh over her stomach")),
            (93, "quadro", D18_PP_DANIEL, "Close-up of Daniel, his mouth near her hair"),
            (93, "riga", "Daniel", "Does he dance with you?"),
            (98, "quadro", D18_PP_SARA, "Close-up of Sara, eyes closed"),
            (98, "riga", "Sara", "He steps on my feet."),
            (102, "riga", "Daniel", "Of course he does."),
            (106, "pensiero", None, "That was unkind. I said it to make him say that."),
            (112, "riga", "Daniel", "Say something else unkind. I like it on you."),
            ## Ritornello 2: le mani sui fianchi, più vicini.
            (120, "video", "images/video/ep2/d18_vc_fianchi.webm", (D18_ABBRACCIO, "Daniel's hands low on Sara's hips from behind as they sway, her hands resting over his")),
            (135, "riga", "Daniel", "Don't move."),
        ]
        if fatto("ep1_d13_cerniera"):
            ## Il passo in più: dall'orecchio alla bocca, senza arrivarci.
            righe += [
                (149, "video", "images/video/ep2/d18_vd_mandibola.webm", ("images/cg/ep2/d18_09_mandibola.webp", "From behind, Daniel's lips trace from below Sara's ear down her jaw to the corner of her mouth; she turns her face back over her shoulder toward him", "images/cg/ep2/d18_09b_si_ferma.webp")),
                (156, "pensiero", None, "Below my ear. Then lower. Then my jaw."),
                (161, "pensiero", None, "The corner of my mouth. Turn. Just turn your head."),
                (166, "quadro", "images/cg/ep2/d18_09b_si_ferma.webp", "Sara has turned her face over her shoulder to meet him; Daniel has already drawn back an inch, smiling"),
                (167, "riga", "Daniel", "Not today."),
            ]
        else:
            righe += [
                (149, "video", "images/video/ep2/d18_vd_orecchio.webm", ("images/cg/ep2/d18_09c_orecchio.webp", "From behind, Daniel kisses Sara just below the ear as they sway; she tilts her head, offering her neck")),
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
    n "He makes her chop the onion his mother's way. «You don't cut it. You make it cry first.» Sara laughs so hard her eyes water, and he says that proves his point."

    ## Il sugo sulla camicetta (Jody, 24/11): solo con Interest Howard ≥ 15 o col Complesso.
    if valore_interest("howard") >= 15 or complesso_crocerossina:
        call ep2_d18_howard_macchia

    $ via_cg()
    if fatto("ep2_d18_cena_reggiseno"):
        $ cg("Howard's little kitchen table: Sara in her bra, perfectly at ease, laughing at something Howard said over two plates of ragù; her blouse drying on the radiator behind her", "images/cg/ep2/d18_13b_cena_reggiseno.webp")
    else:
        $ cg("Howard's little kitchen table laid with his mother's good tablecloth; Sara and Howard eating ragù and laughing", "images/cg/ep2/d18_13a_cena.webp")
    n "Howard lays the table with a cloth that smells of a drawer. Embroidered cherries in the corners. His mother's, for best."
    ho "Not that one. That one wobbles. Sit there. That's the good chair."
    n "He pulls it out for her. It's the one facing the window, with a cushion on it someone has plumped recently."
    ho "So. Tell me about your day. All of it. I've got nothing on the stove but this."
    n "He listens the way nobody listens. Fork down, eyes on her face, nodding at the right places. He never once looks at a phone. He doesn't seem to own one he cares about."
    if fatto("ep2_d18_pranzo_daniel"):
        ho "You're different tonight. Lit up. Like someone's been telling you you're wonderful."
        s "Somebody bought me lunch, that's all."
        ho "Lucky somebody."
        n "He smiles and asks nothing else. Sara has the odd feeling he didn't need to."
    else:
        ho "Your boss. The one with the hair. Is she being nice to you?"
        s "In her own way."
        ho "That's the only way anyone's ever nice."
    ho "He's always late on Thursdays, isn't he? Your [nome_compagno]."
    s "Is he?"
    ho "Thursdays and most Tuesdays. The walls here are very thin, my dear. You get to know a man's footsteps."
    sp "He knows when [nome_compagno] comes home better than I do."

    menu:
        sp "It's ten to nine."
        "Stay for dessert.":
            $ segna("ep2_d18_dolce_howard")
            $ interest("howard", 1, "Sara stayed for his mother's tiramisù.")
            $ via_cg()
            if fatto("ep2_d18_cena_reggiseno"):
                $ cg("Sara in her bra at Howard's table, licking tiramisù off a spoon and laughing, Howard beaming", "images/cg/ep2/d18_13c_dolce_reggiseno.webp")
            else:
                $ cg("Sara and Howard sharing tiramisù at his little table, both laughing", "images/cg/ep2/d18_13c_dolce.webp")
            n "The tiramisù comes out of the fridge in a glass dish with a chipped corner. His mother's again. He watches her take the first spoonful as if it were an exam."
            s "Howard. This is criminal."
            ho "Thirty years I've waited for someone to say that."
            n "She hears the front door next door while she's scraping the dish. [nome_compagno], home. She stays another five minutes anyway."
        "Get home before [nome_compagno].":
            s "I'd better get back before [nome_compagno] does."
            ho "Of course. He'll be tired. Daniel works him so hard."
    if fatto("ep2_d18_cena_reggiseno"):
        n "Her blouse is still a little damp when she buttons it. There's a faint pink shadow where the sauce was. You'd only see it if you were looking."
    n "At the door he gives her a jar of sauce wrapped in a tea towel."
    ho "For [nome_compagno]. Tell him the neighbour made it. That's all he needs to know."
    if fatto("ep2_d18_cena_reggiseno"):
        call ep2_d18_howard_retroscena
    $ nota_sara("howard", "His mother's ragù, at his little table. A jar for [nome_compagno], wrapped in a tea towel.")
    $ ambiente(None)
    return

label ep2_d18_howard_macchia:
    $ via_cg()
    $ cg("At Howard's stove, a splash of red sauce lands across the front of Sara's cream blouse; Howard holding the ladle, all apology", "images/cg/ep2/d18_13d_macchia.webp")
    n "Howard reaches past her for the ladle. It slips. A fat red splash lands right across the front of her blouse."
    ho "Oh! Oh, clumsy old fool. Look what I've done. Your lovely blouse."
    s "It's fine, Howard, really—"
    ho "Not if it sets, it isn't. Rinse it now, cold water, and hang it on the radiator. It'll be dry by the time we've eaten. Go on. Bathroom's there."
    if complesso_crocerossina:
        sp "Take it off. At Howard's. Why am I already undoing the buttons?"
        sp "It's only a blouse. It's nothing serious."
    else:
        sp "He's right. Tomato never comes out once it's dry."
    $ via_cg()
    $ cg("In Howard's kitchen Sara pulls her stained blouse off over her head, left in her bra; Howard openly staring at her chest, not even pretending", "images/cg/ep2/d18_13f_si_toglie.webp")
    n "Sara doesn't ask any questions. She doesn't even go to the bathroom. She unbuttons the blouse right there by the stove and peels it off."
    n "Howard doesn't look away. He doesn't pretend to. His eyes are on her chest and they stay there, frankly, the way he'd look at a sunset."
    s "Howard!"
    ho "Old eyes, my dear. They go where they like. I gave up arguing with them years ago."
    n "She laughs, because it's Howard. She rinses the blouse in his little sink, wrings it out, and lays it over the radiator by the window, smoothing the sleeves."
    n "Then she sits down at his table in her bra, as if that were the most natural thing in the world. After a minute, it is."
    $ segna("ep2_d18_cena_reggiseno")
    $ corruption(2, "Sara had dinner at Howard's in her bra.")
    $ interest("howard", 2, "Sara stayed for dinner in her bra.")
    return

label ep2_d18_howard_retroscena:
    call inizio_retroscena
    $ cg("Retroscena: Howard alone in his kitchen after Sara has gone, looking at a red splash on the stove top and smiling", "images/cg/ep2/d18_13e_retroscena.webp")
    rs "When the door has closed, Howard wipes the stove. He leaves one small red splash on the enamel, just for a moment, and looks at it."
    rs "Thirty-one years in a factory. His hands have never once dropped anything he didn't mean to drop."
    $ retroscena("howard", "The sauce on Sara's blouse wasn't an accident.")
    call fine_retroscena
    return
