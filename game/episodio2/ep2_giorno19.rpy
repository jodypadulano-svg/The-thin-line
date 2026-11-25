## Giorno 19 · venerdì (docs/narrative/giorno19-scheda-2026-11-24.md).
## Redazione (Jessica, Roberta), eventuale convocazione di Barbara, Samantha,
## sera da Joanie e incontro con Jacob a The Lantern.

## La fantasia di Joanie, ascoltata senza giudicare: in alcune scelte future Sara
## può fare la bad girl solo per far felice l'amica (Jody, 24/11).
default sara_bad_girl = False

label ep2_d19:
    call nuovo_giorno(19, "Same Bar, Friday")
    $ fascia_corrente = FASCE.index("lavoro")
    call ep2_d19_jessica
    call ep2_d19_roberta
    call barbara_convocazione
    $ fascia_corrente = FASCE.index("sera")
    if fatto("ep2_d14_shopping_samantha"):
        call ep2_d19_shopping
    else:
        call ep2_d19_caffe
    call ep2_d19_joanie
    call ep2_d19_lantern
    $ fascia_corrente = FASCE.index("notte")
    call ep2_d19_notte
    $ musica(None)
    $ luogo_corrente = ""
    scene bg nero with fade
    return


## --- Mattina: il libro di Jessica ------------------------------------------------------------
## Non è Anna Karenina: quello, con i margini pieni fino alla fine, è del giorno 10.

label ep2_d19_jessica:
    $ vai("redazione", "The newsroom — Friday, 9:20 a.m.")
    $ musica("redazione")
    $ cg("Jessica beside Sara's desk, holding a worn paperback against her chest with both hands", "images/cg/ep2/d19_01_jessica_libro.webp")
    n "Jessica is holding a thick old book against her chest with both hands, like something she's been told to hand in."
    je "This one fell behind the drawer. When I did the box. I only found it yesterday."
    n "{i}Middlemarch{/i}. The spine has been taped twice."
    s "You said we'd do this one next. After Karenina."
    je "I did, didn't I? Well. You do it. You can tell me who's right."
    $ via_cg()
    $ cg("Close-up of the open novel: the margins crowded with pencil, then the pages go clean", "images/cg/ep2/d19_02_appunti.webp")
    n "The margins are full of pencil. Tiny, quick, arguing with everybody. A little after the middle the notes stop. The last one has a date beside it. Three months ago. Jessica's second week here."
    n "After that the pages are clean, all the way to the end."
    menu:
        sp "I shouldn't read over her shoulder. Even this one."
        "Read the last note.":
            $ segna("ep2_d19_appunto_jessica")
            $ confidence(1, "Sara read what Jessica used to think.")
            $ nota_sara("capa", "The notes in Jessica's book stop in her second week here, halfway down a page.")
            n "{i}She keeps waiting for someone to tell her what she wants.{/i}"
            sp "That's a good note. That's a really good note, Jess."
            je "What does it say? I can't read my own writing any more."
            s "It says you were paying attention."
            n "Jessica laughs and tucks her hair behind her ear. She doesn't ask to see it."
        "Give it back.":
            $ segna("ep2_d19_libro_restituito")
            s "Keep it, Jess. You'll want to finish it."
            n "Jessica opens it where the notes stop and reads half a line. Her lips move. She frowns, the way she used to frown at people who were wrong."
            je "...She should have just asked him."
            s "That's what I said. You told me I'd missed the point."
            n "For a moment Jessica looks as if she's about to tell her again. Then someone laughs across the room, and she closes the book."
            je "Okay. I'll keep it. For a bit."
    $ via_cg()
    return


## --- Mattina: il ciondolo di Roberta e il terrazzino -----------------------------------------
## Nel ciondolo c'è una foto di Barbara: non si vede mai. Il modo di fumare è il segno
## della cerchia (17/11): nessuno lo commenta.

label ep2_d19_roberta:
    $ vai("redazione", "The newsroom kitchen — 10:40 a.m.")
    $ cg("Roberta by the kitchen window, side-on, a small gold heart open in her palm, the photo out of sight", "images/cg/ep2/d19_03_ciondolo.webp")
    n "Roberta is by the window with her back to the door. Her little gold heart is open in her palm. Sara didn't know it opened."
    n "It shuts with a click."
    ro "Sara! You're early. You're never in before quarter to. Sit, sit. I'll do yours the way you like."
    menu:
        sp "I didn't know it opened."
        "«Who's in there?»":
            $ segna("ep2_d19_chiesto_ciondolo")
            $ interest("capa", 1, "Sara asked Roberta about her locket.")
            s "Who's in there?"
            ro "Somebody who's good to me."
            n "She says it to the kettle, very softly, and her ears go pink."
            s "Lucky you."
            ro "Yes. That's what I always think. Lucky me."
        "Don't ask.":
            $ segna("ep2_d19_ciondolo_taciuto")
            $ nota_sara("capa", "Roberta was very lonely before the newspaper. «Until somebody opens the door.»")
            n "Sara gets two cups down and talks about the biscuits. Roberta watches her for a moment."
            ro "You didn't ask."
            s "It looked private."
            ro "It is. Thank you. People usually do."
            n "She puts in the sugar Sara likes without being told."
            ro "Before here I used to eat lunch in my car. Every day. I had a radio. I knew the names of all the presenters and I thought that was knowing people."
            s "That sounds lonely."
            ro "I didn't know it was. That's the funny thing. You don't, until somebody opens the door."
    $ via_cg()
    $ vai("redazione", "The back terrace — 10:50 a.m.")
    $ cg("Jessica and Roberta side by side at the terrace railing, smoking in exactly the same pose, Sara beside them", "images/cg/ep2/d19_04_terrazzino.webp")
    n "On the little terrace Jessica and Roberta lean on the rail with the traffic below them. They lift their cigarettes at almost the same time. They breathe out slowly, at almost the same time."
    if fatto("sara_fuma"):
        n "Jessica holds out the packet without looking. Sara takes one. Nobody remarks on it any more."
    else:
        n "Sara stands upwind with her coffee and lets them talk."
    if sara_stagista:
        ro "You'll love Fridays, now. She's always a little softer on Fridays."
        sp "Now?"
    $ via_cg()
    return


## --- Pomeriggio: Samantha, shopping (se accettato il 14) o caffè -----------------------------
## Il suo segreto con Magnus non si rivela: solo un'esitazione sul nome.

label ep2_d19_samantha_josh:
    if fatto("ep2_d15_litigio_josh"):
        samantha "You're quiet today. Is it my son?"
        s "We had a fight. It's mostly over."
        samantha "Mostly is the long part. Wait, and then don't wait too long."
    return

label ep2_d19_shopping:
    $ vai("negozio", "The boutique — 5:15 p.m.")
    $ musica("casa")
    $ cg("Samantha in the boutique's velvet armchair, coat still on, a cup in her hand, perfectly at home", "images/cg/ep2/d19_05_boutique.webp")
    n "It's the same boutique. The same cream curtain. Samantha sits in the velvet armchair with her coat still on and a cup of something nobody else has been offered."
    samantha "You see? Twenty minutes, and not one person has asked if I need help."
    s "Do you ever buy anything?"
    samantha "Every few years. They keep hoping."
    $ via_cg()
    $ cg("Sara at the gilded mirror in a midnight-blue dress, Samantha behind her, their faces close and alike", "images/cg/ep2/d19_06_specchio.webp")
    n "Samantha does up the last hook and looks at them both in the mirror, over Sara's shoulder."
    n "The same eyes. The same wave in the hair. For a second Sara has the odd feeling of looking at a photograph that hasn't been taken yet."
    n "«Your daughter has your smile,» says the girl with the pins."
    samantha "She's not mine. I'd have kept her better stocked in dresses."
    call ep2_d19_samantha_josh
    samantha "What's it for, the dress?"
    s "I'm meeting a publisher tomorrow. He's reading my first fifty pages. Magnus Larssen."
    n "Samantha's hand stops on the fabric. It's only a moment. Then she smooths the seam, as if that had been what she was doing."
    samantha "Then not that one. Too much zip."
    n "She crosses to the rail and comes back with something plain and grey-green that Sara wouldn't have looked at twice."
    samantha "Wear something you can forget you're wearing. He'll be listening."
    sp "How does she know he's a listener? Publishers, probably. They'd have to be."
    menu:
        sp "For tomorrow."
        "The one Samantha chose.":
            $ segna("ep2_d19_abito_samantha")
            $ interest("editore", 1, "Sara will wear the dress Samantha chose.")
            $ confidence(1, "Sara will wear the dress Samantha chose.")
            $ via_cg()
            $ cg("Sara at the mirror in the plain grey-green dress, looking as if she had come to say something", "images/cg/ep2/d19_07_abito_verde.webp")
            n "In the mirror there's nothing to fix. No strap, no hem. Just Sara, looking as if she'd come to say something."
            samantha "There you are."
        "The one I'd have picked.":
            $ segna("ep2_d19_abito_suo")
            $ confidence(2, "Sara chose her own dress for the publisher.")
            s "I think I'm going to wear the blue. It's the one I'd have picked on my own."
            samantha "Good. Then he'll be meeting you."
            n "She means it. She also takes one last look at the grey-green before she hangs it up again."
    $ via_cg()
    return

label ep2_d19_caffe:
    $ vai("strada", "The café opposite the newsroom — 5:15 p.m.")
    $ musica("casa")
    $ cg("Samantha at a small café table opposite the newsroom, scarf half tied, two cups in front of her, waving Sara over", "images/cg/ep2/d19_08_caffe.webp")
    n "«I did say coffee,» says a voice behind her, and it's Samantha, with her scarf half tied and two hours to kill."
    s "You did. I'm sorry about the shopping."
    samantha "Don't be. I shop like other people go to church."
    call ep2_d19_samantha_josh
    s "I've got a big day tomorrow. A publisher's read my pages. Magnus Larssen."
    n "Samantha's spoon goes round once more than it needs to."
    samantha "Then don't dress up for him. Wear something you can forget you're wearing. He'll be listening."
    menu:
        sp "She sounds very sure."
        "«How do you know he listens?»":
            $ segna("ep2_d19_chiesto_magnus")
            $ nota_sara("editore", "Samantha is sure Magnus listens. She didn't really say why.")
            s "How do you know he listens?"
            samantha "Oh. The good ones always do. The others just wait for you to breathe."
            n "She smiles at the window, not at Sara."
        "Thank her and let it go.":
            s "That's good advice."
            samantha "I've got a drawerful. I never took any of it."
    $ via_cg()
    return


## --- Sera: da Joanie -------------------------------------------------------------------------
## Joanie non mente mai: sceglie che cosa illuminare. Il ricordo con Jacob riguarda
## una Sara fra i 19 e i 23 anni (Sara ha 27 anni).

label ep2_d19_joanie:
    $ vai("casa_joanie", "Joanie's flat — 8:15 p.m.")
    $ musica("casa")
    $ cg("Joanie on her sofa with her legs tucked under her, two wine glasses, dresses thrown over the back; Sara arriving in her coat", "images/cg/ep2/d19_09_joanie.webp")
    n "At home [nome_compagno] has a cardboard shield drying on the kitchen table, for Sunday. He barely looked up when she said she was going to Joanie's."
    ch "Wine, or the other wine?"
    n "Sara takes the glass. The last time she was close to Joanie there was a mirror between them. She hasn't said anything about Wednesday. She doesn't know how to start."
    if fatto("ep2_d15_litigio_josh"):
        s "He read my book, Jo. He just sat down and read it. And then he asked me why she was engaged."
        ch "He {i}asked{/i} you?"
        s "As if I owed him an answer. We had a proper fight. I sent him to bed."
        ch "Good."
    else:
        s "It's nothing, really. He read a bit of the book. While I was out. It was open."
        ch "It was open."
        s "He was tired. He'd had a long week."
        ch "You've just given me three reasons and I didn't ask for one. Say it again without them."
        s "...He read my book without asking."
        ch "There she is."

    ## Prima mossa: Josh più grande.
    ch "You know why he didn't ask? Because he already knew he wouldn't like the answer."
    s "That's not fair."
    ch "It's not. He's a sweetheart. He's a sweetheart who went through your pockets."

    ## Seconda mossa: il nome lo fa Sara.
    $ via_cg()
    $ cg("Joanie turning the stem of her wine glass, pretending not to care; Sara turning towards her", "images/cg/ep2/d19_10_il_nome.webp")
    n "Joanie turns the stem of her glass."
    ch "You know who never once looked in your notebook?"
    ch "...Forget it. I didn't say anything."
    s "Who?"
    ch "No, no. Drink."
    s "...Jacob."
    ch "You said it. Not me."
    n "It's strange to hear it in her own voice. She hasn't said it in this room in years."

    ## Terza mossa: solo dettagli.
    $ via_cg()
    $ cg("Sara telling a story with flushed cheeks, laughing; Joanie listening with her chin on her knee", "images/cg/ep2/d19_11_racconto.webp")
    ch "What was the thing with the car? When you were, what, twenty? You came back sunburnt on one side."
    s "He drove us to the coast and we got lost. Seven hours. For a two-hour drive."
    ch "And you were furious."
    s "I was... no. I was on the bonnet of the car eating cherries. He'd bought a whole crate off a man at the roundabout."
    ch "What did you have on?"
    s "Why does that matter? His shirt. My feet on the windscreen."
    ch "I can see it. Where was he?"
    s "Looking at me. He had the map upside down and he was just looking at me."
    n "Every question Joanie asks is a small one. Every answer comes back warmer than the one before."

    ## Quarta mossa: disinnescare il tradimento.
    s "He cheated on me, Jo. For ages. I used to lie there listening for his phone."
    ch "He did. He was twenty-six and an idiot."
    ch "I'm not saying he was good {i}for{/i} you. I'm saying you were loud, Sara. You'd come into a room and I'd know before I saw you. I miss loud."
    n "Sara opens her mouth to say something sensible. What's in there is the taste of cherries."

    menu:
        sp "I know how it ended. I do know."
        "Let yourself be carried off.":
            $ segna("ep2_d19_ricordo")
            $ interest("ex", 1, "Sara let herself remember Jacob.")
            $ corruption(1, "Sara let herself be carried off by the memory.")
            n "She lets her head fall back on the sofa and closes her eyes. The bonnet's warm. The shirt's too big. Somebody's laughing, and it's her."
            s "I was loud, wasn't I?"
            ch "You were deafening."
        "«You're leaving out how it ended.»":
            $ confidence(1, "Sara reminded Joanie how it ended.")
            s "You're leaving out how it ended."
            n "Joanie laughs, a real one, and lifts both hands."
            ch "Guilty. I always skip the last chapter."
            n "She's right, Sara thinks, and she's said so. But the cherries don't go anywhere."

    $ via_cg()
    $ cg("Joanie holding both of Sara's hands, serious, very close", "images/cg/ep2/d19_12_le_mani.webp")
    n "Joanie puts her glass on the floor and takes both of Sara's hands."
    ch "Can I be your friend for a minute? Not the funny one. Let me tell you what I see. You just listen."
    menu:
        sp "She means it. I think she means it."
        "Let Joanie guide you.":
            if fatto("ep2_d19_ricordo"):
                call ep2_d19_ripeti
                if valore_interest("amica") > 8:
                    call ep2_d19_confidenza
            else:
                $ segna("ep2_d19_guida")
                $ interest("amica", 1, "Sara listened to Joanie.")
                s "Go on, then. One minute."
                ch "You've stopped asking for things. You used to want so much it was exhausting. I just want you to want something again. Anything. I don't care what."
                s "...That's actually a nice thing to say."
                ch "I know. I'm horrified."
        "Keep your own head.":
            $ segna("ep2_d19_razionale")
            $ confidence(1, "Sara kept her own head.")
            s "I love you. And I've been listening to you since I was nineteen, and I know what it sounds like when you're driving."
            n "Joanie's eyebrows go up. Then she kisses Sara on the forehead, hard, with a noise."
            ch "Fine. You drive."
    call ep2_d19_messaggio
    return


## --- Il dialogo a ripetizione: box con una sola scelta ---------------------------------------

label ep2_d19_ripeti:
    $ segna("ep2_d19_ripetizione")
    $ musica("notte")
    $ via_cg()
    $ cg("Close-up of Sara's and Joanie's faces in the light of a single lamp, almost touching", "images/cg/ep2/d19_13_ripeti.webp")
    ch "I'm going to say something, and if it's true, you say it back. That's all. If it isn't true, don't."
    s "This is silly."
    ch "Extremely. Ready?"
    menu:
        ch "[nome_compagno] read my book without asking."
        "«[nome_compagno] read my book without asking.»":
            s "[nome_compagno] read my book without asking."
    n "Easy. It's only what happened."
    menu:
        ch "Jacob never needed to ask."
        "«Jacob never needed to ask.»":
            s "Jacob never needed to ask."
    n "She laughs saying it. Joanie doesn't laugh. She waits."
    menu:
        ch "I was loud with him."
        "«I was loud with him.»":
            s "I was loud with him."
    n "This one comes out quieter than the others."
    menu:
        ch "I miss being loud."
        "«I miss being loud.»":
            s "I miss being loud."
    n "Her eyes have started to sting, and she has no idea why. Joanie's thumbs move over her knuckles. Slowly. Like winding something."
    ch "You're doing so well."
    $ via_cg()
    $ cg("Sara in extreme close-up, eyes shining, a smile escaping her", "images/cg/ep2/d19_14_occhi.webp")
    menu:
        ch "Nobody's made me feel like that since."
        "«Nobody's made me feel like that since.»":
            s "Nobody's made me feel like that since."
    sp "That isn't... [nome_compagno] makes me feel..."
    sp "No. Not {i}that{/i}."
    menu:
        ch "I still want him."
        "«I still want him.»":
            s "I still want him."
    n "It's out. She hears it sitting there in the room, in her own voice, perfectly clear. And something she's been holding up with both arms for four years simply comes down."
    n "She laughs. She's crying, and she's laughing, and she covers her face with her hands."
    s "Oh God. Jo."
    ch "I know."
    s "Sometimes I touch myself thinking about him."
    n "Silence. She looks through her fingers."
    s "Not often. Sometimes. When [nome_compagno]'s asleep. And then I lie there and I feel so... {i}awake{/i}."
    n "Joanie's smile arrives slowly, and it's enormous."
    ch "Told you."
    $ interest("amica", 3, "Sara let Joanie guide her.")
    $ interest("ex", 2, "Sara said it out loud.")
    $ corruption(2, "Sara repeated everything Joanie said.")

    $ musica("casa")
    $ via_cg()
    $ cg("Sara and Joanie collapsed against each other on the sofa, howling with laughter", "images/cg/ep2/d19_15_complici.webp")
    n "What comes after isn't shame. Sara waits for it and it doesn't come. She feels light. She feels about a stone lighter."
    ch "So. Tell me everything. I've waited four years for this conversation."
    s "He was just so... {i}there{/i}. He'd come through a door and the door looked smaller."
    ch "Go on."
    s "He could pick me up with one arm. He did it once in a supermarket. With the basket in the other hand."
    ch "And in bed?"
    s "Jo!"
    ch "You've come this far."
    n "Sara pulls a cushion onto her lap and says it into the top of it."
    s "With [nome_compagno] it's sweet. It's really sweet, and I love him. With Jacob I used to forget what day it was."
    ch "Better?"
    s "So much better. It's not even the same sport. And there was a lot more of him. Everywhere."
    n "They look at each other. Then they're both gone, howling, Joanie sliding off the sofa with her wine held up out of harm's way."
    return


## --- La confidenza di Joanie (solo dopo la ripetizione, Interest Joanie > 8) -----------------
## Confessa soltanto la fantasia: l'attrazione per Sara e la «casa delle bambole»
## restano segrete fino alla tappa 5 (Jody, 24/11).

label ep2_d19_confidenza:
    $ via_cg()
    $ cg("Joanie sitting on the carpet with her knees together, unsure of herself for the first time", "images/cg/ep2/d19_16_joanie_incerta.webp")
    n "When it passes, Joanie stays where she is, on the floor, with her back against the sofa. She isn't laughing any more. She's picking at the hem of her sock."
    ch "Can I tell you one? A real one."
    s "Of course."
    ch "No, wait. It's strange. It's really strange, Sara. It's about you, sort of. And if I say it and you look at me differently, I don't know what I'd do."
    ch "So you can say no. Honestly. If you're not ready, I'd rather keep you than tell you."
    menu:
        sp "She's never been afraid of anything. She's afraid of this."
        "«Some things are better left unsaid.»":
            $ segna("ep2_d19_non_detto")
            s "I don't want to lose you. Some things are better left unsaid. Aren't they?"
            n "Joanie breathes out. She looks relieved, and only a little bit sad."
            ch "Yeah. I think so too. Keep me, then."
            s "Always."
        "«Whatever it is, I won't judge you.»" (acceleratore=True):
            $ sara_bad_girl = True
            $ segna("ep2_d19_fantasia_joanie")
            $ interest("amica", 3, "Sara listened without judging.")
            $ corruption(1, "Sara listened to Joanie's fantasy.")
            s "Whatever it is, I won't judge you. I just told you the worst thing I've got."
            n "Joanie opens her mouth, and shuts it. Her chin goes. Joanie, who has never been shy in her life, can't look at her."
            ch "I think about you. In bed. With somebody else."
            ch "Not with me. I'm just there. I'm watching. And you're with some man who isn't [nome_compagno], and you're so happy, and you look at me, and you're not sorry at all."
            ch "It's the thing. You know. The thing I think about. It's been the thing for years."
            $ via_cg()
            $ cg("Joanie in tears, half laughing, hiding her face in her sleeve", "images/cg/ep2/d19_17_joanie_piange.webp")
            n "She's crying properly now, and half laughing, wiping her face with her sleeve."
            ch "Say something. Please. Say I'm disgusting."
            n "Sara gets down off the sofa, onto the carpet, and puts both arms round her."
            $ via_cg()
            $ cg("Sara and Joanie holding each other on the carpet in the lamplight", "images/cg/ep2/d19_18_abbraccio.webp")
            s "Thank you for telling me."
            ch "...What?"
            s "Thank you. You carried that round on your own all this time, you idiot. You could have told me."
            n "Joanie makes a sound into her shoulder that isn't a word. They stay there until the wine's warm."
            sp "I ought to be shocked. I keep looking for it. All I can think is that she's never trusted anyone this much."
            sp "And that she said I looked happy."
            n "They have been friends for years. They have never been friends like this."
            $ nota_sara("amica", "Joanie's secret: she fantasises about me with another man. She thought I'd hate her for it.")
            call ep2_d19_mercoledi
            call ep2_d19_regola
    return

label ep2_d19_mercoledi:
    n "They're still on the carpet. Sara has her cheek on Joanie's hair, and Wednesday is right there on the tip of her tongue."
    menu:
        sp "The mirror. I could tell her. Or I could let her have tonight."
        "«I saw you with Simon.»":
            $ segna("ep2_d19_sa_di_simon")
            $ nota_sara("amica", "Joanie cheats on Mark. She says it makes her kinder to him. I couldn't find the hole in it.")
            s "Can I give you one back? So we're even."
            s "I saw you. On Wednesday. You and Simon."
            n "Joanie lifts her head. She wipes under one eye with a knuckle. She doesn't blush. If anything she seems to settle, the way she does when a conversation gets to the part she's good at."
            ch "How much of it?"
            if fatto("ep2_d17_ha_guardato_joanie_simon"):
                s "...I stayed. For a bit."
                ch "Good for you."
            else:
                s "Enough."
                ch "You could have said hello."
            $ via_cg()
            $ cg("Joanie, calm, holding Sara's hand and explaining, the tears still on her face", "images/cg/ep2/d19_19_ragioni.webp")
            s "Jo. What about Mark?"
            ch "I love Mark. That's the first thing, and it's not the excuse, it's just true. I'd walk into the sea for him."
            ch "But I tried being the girl who only wants one person. Two years. I was so good. And I got mean, Sara. I picked at him. The way he chews. I hated him for things he hadn't done, because I was so busy not doing mine."
            ch "Then one day I stopped fighting it. And I came home and I wanted to cook for him. I wanted to hear about his boring day. He said, what's got into you, you're lovely lately."
            s "Lovely because you'd..."
            ch "Lovely because I was whole. Nobody took anything from him. He got more of me, not less."
            s "He doesn't know, though."
            ch "No. And I carry that so he doesn't have to. If he ever asks me, straight out, I'll tell him. He's never asked. I don't think he wants to."
            n "Sara looks for the hole in it. There must be one. Joanie's holding her hand and telling her the truth, and it sounds so much kinder than everything she's always believed."
            sp "He got more of me, not less."
            ch "You're the only person I've ever said that to."
        "Let her have tonight.":
            n "Not now. Not on top of this. She kisses Joanie's hair instead, and lets Wednesday go back where it was."
            sp "Another day. It's hers to tell, anyway."
    return


## --- Retroscena: il messaggio a Jacob (I9) ---------------------------------------------------

label ep2_d19_messaggio:
    $ via_cg()
    call inizio_retroscena
    $ cg("Joanie's hand on her phone, a message ready to send; behind her, light under the bathroom door", "images/cg/ep2/d19_20_messaggio.webp")
    rs "Sara is in the bathroom, fixing her eyes. Water running."
    if fatto("ep2_d19_ripetizione"):
        rs "Joanie types. «She's smiling. Give it an hour. Make her laugh.»"
    else:
        rs "Joanie types. «She's on her guard. Give it an hour. Make her laugh.»"
    if sara_bad_girl:
        rs "Her thumb waits over the button. Her eyes are still wet. Then she presses it."
    rs "The answer comes before the tap has stopped. «On my way.»"
    $ retroscena("amica", "Joanie arranged the meeting at The Lantern. She told Jacob to make Sara laugh.")
    $ retroscena("ex", "Joanie told him where Sara would be, and to make her laugh.")
    $ via_cg()
    call fine_retroscena
    $ cg("Joanie on her sofa with her legs tucked under her, two wine glasses, dresses thrown over the back; Sara arriving in her coat", "images/cg/ep2/d19_09_joanie.webp")
    ch "Coat! We're going out."
    s "Out where?"
    ch "The Lantern. Same as always. One drink."
    $ via_cg()
    return


## --- The Lantern -----------------------------------------------------------------------------

label ep2_d19_lantern:
    $ vai("locale", "The Lantern — 10:20 p.m.")
    $ ambiente("locale")
    $ musica("locale")
    $ cg("Sara and Joanie at the end of the bar at The Lantern, under the last lamp, the crowd behind them", "images/cg/ep2/d19_21_bancone.webp")
    n "The Lantern on a Friday is the Lantern on a Saturday with its tie off. They find the end of the bar, under the last lamp, where it's nearly possible to hear."
    if fatto("ep2_d18_pranzo_daniel"):
        s "I didn't tell you about yesterday. I had lunch with Daniel."
        ch "Daniel {i}Daniel{/i}?"
        s "We talked about the book. He's... he's not what I thought."
        ch "What did you think?"
        s "That he was an arrogant—"
        n "She starts again. There's a better place to start."
        if fatto("ep2_d18_ballo"):
            s "He asked me to dance, Jo. In the middle of lunch. And I—"
        else:
            s "So the bill comes, and he looks at me, and he—"
        n "She never gets to the verb."
    else:
        ch "That barman's new. Look at his arms. Don't look at his—"
        n "Joanie stops, with her eyes on something over Sara's shoulder, and takes a long, slow sip of her drink."

    $ via_cg()
    $ cg("A broad man with a shaved head steps up to the bar beside Sara, face still in shadow, a heavy ring on his hand; Sara turning", "images/cg/ep2/d19_22_jacob_arriva.webp")
    jacob "You still hold a glass with both hands."
    n "She knows before she turns. Her shoulders know."
    $ via_cg()
    $ cg("Jacob in close-up: shaved head, goatee without a moustache, amused, looking down at Sara", "images/cg/ep2/d19_23_jacob.webp")
    n "Four years. He's broader. His head's shaved now, and the beard's down to a bit of chin. He's wearing the same ring. He's looking at her as if she were the punchline of a very good joke somebody had finally remembered."
    s "...Jacob."
    jacob "Sara."
    ch "Well! What are the {i}odds{/i}."
    $ incontra("ex")
    $ tappa("ex", 1)
    $ segna("jacob_tornato")
    $ nota_sara("ex", "Jacob, after four years. Out of nowhere, at The Lantern.")
    call ep2_d19_saluto
    if sara_bad_girl:
        call ep2_d19_occhiolini
        return
    jacob "Let me get you one. For old times' sake. Or for new ones, I'm not fussy."
    call ep2_d19_drink
    call ep2_d19_parlano
    call ep2_d19_numero
    ch "So."
    s "Don't."
    ch "I didn't say anything."
    s "You're {i}humming{/i}."
    $ ambiente(None)
    return

label ep2_d19_saluto:
    if sara_bad_girl:
        call ep2_d19_ammicca("bancone")
        n "Over his shoulder, very slowly, Joanie winks."
    menu:
        sp "Four years. Say something."
        "Stay cold.":
            $ segna("ep2_d19_jacob_fredda")
            s "Hello, Jacob. It's been a while."
            jacob "Four years. You've been counting too, or is it just me?"
            s "It's just you."
            n "He takes it well. He takes it exactly as if he'd been handed something."
        "Laugh at an old memory.":
            $ segna("ep2_d19_jacob_risata")
            $ interest("ex", 3, "Jacob made her laugh.")
            $ corruption(1, "Sara laughed at an old memory with Jacob.")
            jacob "Eleven coffees."
            n "And that's it. She's gone. One small café, one waiter, her terrible holiday Spanish, and a tray that kept on coming."
            s "I asked for {i}one{/i}. With milk!"
            jacob "You drank four. So he wouldn't be offended."
            n "She's laughing with her whole face. She can hear it over the music. Loud."
            sp "Oh. There it is."
        "(The wink.)" if sara_bad_girl:
            $ segna("ep2_d19_bad_girl_usata")
            $ d19_segue(1)
            $ via_cg()
            $ cg("Sara's hand flat on Jacob's chest, her eyes past his shoulder on Joanie, whose glass has stopped halfway to her mouth", "images/cg/ep2/d19_24_bad_girl.webp")
            n "She puts her hand flat on the front of his shirt, as if to check he's real."
            s "You got bigger. I didn't think there was room."
            n "She says it to him. She isn't looking at him. Along the bar Joanie's glass has stopped halfway to her mouth."
            n "Sara holds her eyes, and smiles, and leaves her hand where it is one second longer."
            sp "This one's for you, Jo."
            n "Jacob, who thinks it's for him, looks delighted."
            jacob "Four years, and that's the first thing you say to me?"
            s "Was it a bad thing?"
            jacob "It was a very good thing."
    $ via_cg()
    return

## Il mestiere di Jacob: lo strip club si scopre in chat o alla fine della serata.
label ep2_d19_mestiere:
    s "So what do you do now?"
    jacob "I run a place. Near the station."
    s "What sort of place?"
    jacob "The sort where nobody minds if I take Friday off."
    return

label ep2_d19_drink:
    menu:
        sp "One drink is just one drink."
        "«No, thanks.»":
            s "I've got one. Thanks."
            jacob "You have. Both hands."
            ch "So what do you do with yourself these days, Jacob?"
            jacob "I run a place. Near the station."
            ch "What sort of place?"
            jacob "The sort where nobody minds if I take Friday off."
        "«All right. One.»":
            $ segna("ep2_d19_jacob_drink")
            $ interest("ex", 1, "Sara let Jacob buy her a drink.")
            $ corruption(1, "Sara let Jacob buy her a drink.")
            s "All right. One."
            n "He doesn't ask what she drinks. He orders it. It's right."
            call ep2_d19_mestiere
    return

## --- Jacob: il tradimento, Josh, un ballo (Jody, 25/11) --------------------------------------
## Solo nella sera normale. Jacob non chiede mai scusa davvero (Q&A 18/11). Il ballo
## c'è soltanto se Sara ha riso al ricordo.

label ep2_d19_parlano:
    $ via_cg()
    $ cg("Sara and Jacob face to face at the bar, her chin up, his smile gone careful", "images/cg/ep2/d19_22b_tradimento.webp")
    n "He's easy to talk to. He always was. That's the trouble with him: you could be furious and not notice you were leaning in."
    menu:
        sp "Nobody's said it yet. Somebody ought to."
        "«You cheated on me.»":
            $ segna("ep2_d19_detto_tradimento")
            $ confidence(1, "Sara said it to his face.")
            s "You cheated on me."
            n "She says it at an ordinary volume, in an ordinary voice. Beside her, Joanie's straw stops making a noise."
            jacob "I did."
            s "For a long time."
            jacob "For a long time. I was never any good at one, Sara. I told myself I was. I told you."
            n "She waits for the next part. The sorry. It doesn't come, and she sees that it isn't going to, and that he isn't hiding it. There just isn't one in there."
            jacob "You're the only one who ever walked out. Did you know that? The others waited to be told."
            s "Good for me."
            jacob "Yeah. I thought so too. After about a year."
            sp "I've wanted to say that for four years. I thought it would feel bigger. It feels like putting down a bag."
        "Let it lie.":
            n "It's four years old. It would sit there on the bar between them like somebody's wet umbrella. She has a sip of her drink instead."

    jacob "So who's at home?"
    $ via_cg()
    $ cg("Close-up of Sara at the bar, about to answer, her glass halfway to her lips", "images/cg/ep2/d19_22c_esita.webp")
    menu:
        sp "He asked it nicely. Almost nicely."
        "Answer straight away.":
            $ segna("ep2_d19_difende_josh")
            $ interest("josh", 1, "Sara didn't have to think about it.")
            s "[nome_compagno]. He's painting a shield on my kitchen table, for a thing on Sunday, and he'll have fallen asleep on it by now, and he'll have left me the good half of whatever he cooked."
            n "It all comes out in one breath. She hears how fond it sounds. So does Jacob."
            jacob "He sounds all right."
            s "He's better than all right."
            jacob "Then he's a lucky man."
        "Think about it a second too long.":
            $ segna("ep2_d19_esita_josh")
            n "It ought to be the easiest question in the world. She opens her mouth, and there's a gap. It's tiny. You could hardly get a fingernail into it."
            s "...[nome_compagno]. He's lovely. He's really lovely."
            n "Jacob doesn't say anything. He nods, slowly, like a man who's been handed change and has counted it."
            sp "Why did I say it twice?"

    if fatto("ep2_d19_jacob_risata"):
        n "The DJ puts on something old and slow, for the couples. Jacob puts his glass down."
        jacob "One. I won't even talk."
        menu:
            sp "It's only a song."
            "One song.":
                $ segna("ep2_d19_ballo_jacob")
                $ interest("ex", 1, "Sara danced one song with Jacob.")
                $ corruption(1, "Sara danced with Jacob, and her body remembered.")
                $ via_cg()
                $ cg("Sara and Jacob dancing slowly among other couples, a correct distance between them, her eyes wide over his shoulder", "images/cg/ep2/d19_22d_ballo.webp")
                n "He's as good as his word. One hand at her waist, up where a hand should be. The other holding hers as if it were on loan. There's room for a hymn book between them."
                n "He doesn't talk. She's grateful, for about eight bars."
                n "Then they turn, and her weight goes onto her left foot before his shoulder moves. She didn't decide that. She hasn't danced with him in four years and her feet know where he's going."
                sp "My head left him. I was there. I carried the boxes."
                sp "Nobody told the rest of me."
                n "The song ends. He lets go first."
                jacob "Thank you."
            "Not tonight.":
                s "Not tonight."
                jacob "Fair enough. It's a terrible song."
    $ via_cg()
    return

label ep2_d19_numero:
    $ via_cg()
    $ cg("Jacob's hand leaving his unlocked phone on the bar in front of Sara, his face turned to the bottles", "images/cg/ep2/d19_25_telefono.webp")
    n "Before the bell for last orders he puts his phone on the bar in front of her, unlocked, and looks away at the bottles. He doesn't ask. He never did."
    menu:
        sp "He isn't even looking."
        "Give him the number.":
            $ segna("ep2_d19_numero_dato")
            $ interest("ex", 2, "Sara gave Jacob her number.")
            $ da_numero("ex")
            n "Her thumbs know where to go. She doesn't put a surname."
        "Push the phone back.":
            $ segna("ep2_d19_numero_negato")
            s "Not tonight, Jacob."
            jacob "Fair enough."
            $ via_cg()
            call inizio_retroscena
            rs "Later, on the pavement, his phone lights up. Joanie. A number, and nothing else."
            $ retroscena("ex", "Joanie gave him Sara's number.")
            call fine_retroscena
    $ via_cg()
    return


## --- Notte -----------------------------------------------------------------------------------

label ep2_d19_notte:
    $ vai("casa", "Home — 12:50 a.m.")
    $ musica("notte")
    $ cg("Josh asleep on the sofa with a cardboard shield on his chest; Sara in the doorway with her shoes in her hand", "images/cg/ep2/d19_26_josh_dorme.webp")
    n "[nome_compagno] has fallen asleep on the sofa with the shield on his chest. It says something in an alphabet he made up himself."
    n "She takes the paintbrush out of his hand, and puts a blanket over him, and the shield somewhere safe."
    sp "I do love you. I do."
    sp "I'll tell him about Jacob. There's nothing to tell."
    if fatto("ep2_d19_jacob_risata"):
        n "In the bathroom she thinks of eleven coffees, and has to put her hand over her mouth."
    elif fatto("ep2_d19_jacob_drink"):
        n "She wonders how he knew what she drinks. Then she remembers."
    if fatto("ep2_d19_ripetizione"):
        n "In bed she lies on her back with the window open. Wide awake."
    $ via_cg()
    return
