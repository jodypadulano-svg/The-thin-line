## =============================================================================
## EPISODE 1 — DAY 3 (Wednesday)
## =============================================================================
## Calendar: docs/mese-1.md, day 3. Daniel 1 (docs/personaggi/daniel.md, B),
## thread I1 (Josh's father, one line in the car).
## Draft for Jody's review. Game text in English (A11); comments in Italian.
## CG: docs/prompt-immagini/inquadrature-giorno-03.md. Finché mancano,
## compare la didascalia [CG].

init python:
    def vestito_d3(nome):
        """CG della cena con Sara in vista, nella variante del vestito scelto:
        «_audace» (rosso), «_nero» (nero), nessun suffisso (blu, sobrio).
        Se la variante non esiste ancora, usa l'immagine col vestito blu."""
        base = "images/cg/ep1/d3_%s.webp" % nome
        if fatto("ep1_d3_audace"):
            suffisso = "_audace"
        elif fatto("ep1_d3_nero"):
            suffisso = "_nero"
        else:
            return base
        variante = "images/cg/ep1/d3_%s%s.webp" % (nome, suffisso)
        return variante if renpy.loadable(variante) else base


label ep1_d3:
    call nuovo_giorno(3, "Wednesday")
    call ep1_d3_riunione
    call ep1_d3_vestito
    call ep1_d3_cena
    call ep1_d3_auto
    return


## --- Lavoro: la riunione di redazione -----------------------------------------

label ep1_d3_riunione:
    $ vai("redazione", "The newsroom — 9:30 a.m.")
    $ musica("redazione")
    $ ambiente("redazione")
    $ cg("The newsroom meeting table: Barbara at the head handing out assignments, the journalists around her; Sara at the far end with a notebook", "images/cg/ep1/d3_01_riunione.webp")

    n "Wednesday morning means the editorial meeting. Twelve chairs around a table built for eight, and Barbara at the head of it, like a queen at a banquet she has paid for."
    n "Every Wednesday the same ritual: Barbara reads the list, says a name, says a story. Nobody argues. Nobody has ever argued."
    sp "The cheese festival is over, at least. What could possibly be worse?"
    $ musica("barbara")
    ba "The new car park on Fourth Street. Somebody, please. Anybody. Sara, darling."

    $ cg("Close-up of Sara at the meeting table, pen frozen over her notebook, a page full of crossed-out ideas", "images/cg/ep1/d3_02_sara_riunione.webp")
    sp "The car park. Eight hundred words on a car park."
    n "Under her pen, on the page of her notebook, there's an idea she's been circling for a week. The old cinema by the river closes at the end of the month."
    n "Sixty years of first dates, first kisses, people who met in the dark and stayed together for a lifetime. Nobody has written a line about it."
    sp "Say it. Just say it. What's the worst that can happen?"
    sp "She laughs at me in front of eleven people. That's the worst that can happen."

    menu:
        sp "The car park, or the cinema?"
        "Take the piece she's given.":
            s "The car park. Sure. I'll take it."
            $ cg("Barbara at the head of the table, already moving on to the next name on her list", "images/cg/ep1/d3_03_barbara_riunione.webp")
            ba "Wonderful. Eight hundred words, and try to make concrete sound sexy."
            n "Barbara is already on the next name. Sara closes her notebook over the cinema."
            sp "Next week. I'll say it next week."
        "Propose her own idea.":
            $ confidence(2, "Sara fights for her own story.")
            $ segna("ep1_d3_proposta_cinema")
            s "Actually... can I propose something else?"
            n "Eleven heads turn. Somebody's coffee cup stops halfway to their mouth."
            $ cg("Barbara at the head of the table, glasses lowered, looking at Sara with sudden interest", "images/cg/ep1/d3_03_barbara_riunione.webp")
            ba "Well, well. The cheese girl has an opinion. Go on, darling. Amaze me."
            s "The Riverside cinema closes at the end of the month. Sixty years. I'd like to talk to the people who met there. Couples. First dates. Not the building. The people."
            n "Silence. Barbara taps her red nail on the table, once, twice."
            ba "Hm. Love stories in the dark. Our readers are old and sentimental. They'll eat it with a spoon."
            ba "Write it. Twelve hundred words. If it's boring, you'll do car parks until Christmas."
            sp "Yes. Yes! She said yes!"
            sp "Don't smile. Don't smile in front of everybody. Too late, I'm smiling."

    $ vai("redazione", "The newsroom — 5:00 p.m.")
    $ musica("redazione")
    n "The afternoon goes by in a blur. At five o'clock sharp Sara is out of the door: tonight there's a company dinner, and she still has no idea what to wear."
    return


## --- Sera: cosa mettere ----------------------------------------------------------

label ep1_d3_vestito:
    $ vai("camera", "Home — 7:00 p.m.")
    $ ambiente(None)
    $ musica("casa")
    $ cg("Sara in front of the open wardrobe in her robe, three dresses laid out on the bed", "images/cg/ep1/d3_04_tre_vestiti.webp")

    n "Three dresses on the bed. Sara in her robe, hair still damp, looking at them as if they were the three doors of a game show."
    sp "The navy one. Safe. Nobody has ever been fired because of a navy dress."
    sp "The black one. [nome_compagno]'s favourite. He always says I look like a film star in it. He's biased, but he's sweet."
    sp "And the red one. The one Joanie made me buy last summer and I've never had the courage to wear."
    c "Babe? We need to leave in twenty minutes! Daniel hates people who are late!"
    sp "Of course he does."

    menu:
        sp "What does the partner of a good employee wear?"
        "The navy dress. Sober and elegant.":
            $ segna("ep1_d3_sobrio")
            $ cg("Sara in front of the mirror in the navy dress, calm and satisfied", "images/cg/ep1/d3_19_vestito_blu.webp")
            n "The navy dress, buttoned up to the collarbone. Sara looks at herself in the mirror and sees a woman nobody will remember. Perfect."
            sp "Tonight it's his night, not mine."
        "The black dress [nome_compagno] likes so much.":
            $ interest("josh", 1, "She wore the dress he loves.")
            $ segna("ep1_d3_nero")
            $ cg("Sara in the black dress at the mirror; Josh stops in the doorway with his tie half-knotted", "images/cg/ep1/d3_20_vestito_nero.webp")
            n "The black dress. Simple, just above the knee. When [nome_compagno] sees her he stops in the doorway with his tie half-knotted."
            c "Oh. That one."
            s "That one. For luck."
            c "Daniel's going to think I'm punching way above my weight."
            s "You are. Now finish that tie."
        "The most daring dress she owns.":
            $ corruption(1, "Sara wants to be seen tonight.")
            $ segna("ep1_d3_audace")
            $ cg("Sara in front of the mirror in a fitted red dress, surprised by her own reflection", "images/cg/ep1/d3_05_vestito_rosso.webp")
            n "The red one. Fitted, the neckline lower than anything she wears at work, the hem well above the knee."
            n "Sara looks at the mirror for a long moment. The woman looking back seems to know something she doesn't."
            sp "It's a company dinner, Sara. Not a red carpet."
            sp "But [nome_compagno] wants to make a good impression. And a good impression starts with his partner, right?"
            c "Babe, are you ready? We need to... oh."
            n "[nome_compagno] stops in the doorway. His mouth opens and stays open."
            c "Wow. Are you... sure? About that one? For a work thing?"
            s "You don't like it?"
            c "I love it. I just... I love it. Let's go before I change my mind."
    return


## --- Sera: la cena aziendale (Daniel 1) ----------------------------------------

label ep1_d3_cena:
    $ vai("ristorante", "The restaurant — 8:15 p.m.")
    $ musica("ristorante")
    $ ambiente("ristorante")
    $ cg("An elegant restaurant, a long table for the company dinner; Josh leads Sara by the hand toward a confident man in a dark suit", vestito_d3("06_arrivo"))

    n "The restaurant is the kind Sara has only seen in magazines: white tablecloths, candles, waiters who move without making a sound."
    n "A long table at the back is already half full. [nome_compagno]'s colleagues, their partners, the polite laughter of people who see each other every day and don't really know each other."
    c "Daniel, this is Sara. Sara, Daniel."

    $ cg("Daniel stands up from the table: dark suit, magazine-cover smile, a handshake one moment too long", "images/cg/ep1/d3_07_daniel_saluta.webp")
    $ incontra("daniel")
    n "He stands up. Mid-thirties, tall, a dark suit that probably costs more than their rent. A smile that knows exactly how good it is."
    da "Sara. Finally. He never talks about you. Now I understand why: he keeps you hidden."
    n "His handshake lasts one moment too long. Warm, dry, sure of itself."
    s "Nice to meet you. [nome_compagno] talks about you all the time."
    da "Does he? Good things, I hope. No, don't answer. I'd rather keep my illusions."
    if fatto("ep1_d3_audace"):
        $ interest("daniel", 1, "Daniel noticed the red dress.")
        da "And that dress, Sara. [nome_compagno], you didn't tell me your partner had such good taste. You certainly didn't learn it from her."
        n "[nome_compagno] laughs. A second too late."
    sp "Okay. Charming. Very charming. A little too aware of it."

    ## Retroscena: lo sguardo di Daniel (scheda B). Il giocatore lo vede, Sara no.
    ## Alterna lo sguardo di Daniel e zoom lenti su Sara ricavati da CG già fatte
    ## (C3 per i fianchi, C7 per la scollatura): niente immagini in più.
    call inizio_retroscena
    $ cg("Behind the scenes: Daniel's gaze lingering on Sara as she sits down, while a colleague talks to him", vestito_d3("08_sguardo_daniel"))
    rs "Sara sits down, smoothing her dress over her hips."
    if fatto("ep1_d3_audace"):
        $ zoom_cg("Daniel's gaze slides down Sara's hips in the red dress", vestito_d3("08_sguardo_daniel"), (992, 200, 560, 315))
    else:
        $ zoom_cg("Daniel's gaze slides down Sara's hips in the navy dress", vestito_d3("08_sguardo_daniel"), (965, 280, 560, 315))
    rs "Daniel's eyes follow the movement all the way down, slowly, as if he had all the time in the world."
    $ cg("Close-up of Daniel leaning back in his chair, wine glass in hand, amused, looking straight at Sara", "images/cg/ep1/d3_11_daniel_brinda.webp")
    rs "The employee at his side is telling him something about quarterly figures. Daniel isn't listening to a single word."
    rs "When Sara leans forward to reach the water..."
    if fatto("ep1_d3_audace"):
        $ zoom_cg("Daniel's gaze on Sara's neckline in the red dress", vestito_d3("12_sara_tavola"), (530, 380, 640, 360))
    elif fatto("ep1_d3_nero"):
        $ zoom_cg("Daniel's gaze on Sara's neckline in the black dress", vestito_d3("12_sara_tavola"), (600, 420, 640, 360))
    else:
        $ zoom_cg("Daniel's gaze on Sara's neckline in the navy dress", vestito_d3("12_sara_tavola"), (470, 420, 640, 360))
    rs "...his gaze slides from her face to her neckline, and stays there."
    $ cg("Close-up of Daniel leaning back in his chair, wine glass in hand, amused, looking straight at Sara", "images/cg/ep1/d3_11_daniel_brinda.webp")
    rs "He smiles to himself. Then he looks at [nome_compagno]. Then back at her."
    $ retroscena("daniel", "At the dinner Daniel noticed Sara, and not as an employee's partner.")
    call fine_retroscena

    ## L'ordinazione: Daniel decide per tutti.
    $ cg("Close-up of Daniel leaning back in his chair, wine glass in hand, amused, looking straight at Sara", "images/cg/ep1/d3_11_daniel_brinda.webp")
    n "Daniel doesn't open the wine list. He hands it back to the waiter without looking at it."
    da "Two bottles of the red I had last time. And the tasting menu for everyone. Trust me, it's the only thing worth eating here."
    n "Nods all around the table. Nobody has opened a menu."
    da "Unless the lady has a preference, of course. Sara?"
    menu:
        sp "Everybody's looking at me."
        "Let him choose.":
            s "Whatever you recommend."
            da "Wise woman. [nome_compagno], she's wiser than you. You always ask for the bread before the food arrives."
            n "Polite laughter. [nome_compagno] laughs too."
        "Order something else, just for herself.":
            $ confidence(1, "Sara doesn't let him decide for her.")
            $ segna("ep1_d3_ordina_da_sola")
            s "Actually, I'd like the risotto. And a glass of white, please."
            n "The waiter looks at Daniel for a fraction of a second, as if asking permission. Then he writes it down."
            da "A woman who knows what she wants. How rare. And how refreshing."
            sp "It's a risotto. Not a declaration of independence."
            sp "So why does it feel like one?"

    ## Daniel scopre il romanzo (prepara la festa: «si è ricordato che scrivo»).
    $ cg("The long table: Daniel at the centre holding court, the colleagues laughing; Josh smiling with effort; Sara beside him", vestito_d3("09_tavolata"))
    da "So, Sara. What do you do, when you're not being hidden by [nome_compagno]?"
    s "I'm a journalist. Culture pages. Restaurants, fairs, the occasional exhibition."
    da "A journalist! Then I'd better be careful what I say tonight."
    $ cg("Close-up of Josh at the table, beaming with pride, gesturing toward Sara", "images/cg/ep1/d3_16_josh_orgoglioso.webp")
    c "And she's writing a novel. A real one. She's going to be famous, I'm telling you."
    n "[nome_compagno] says it with such pride that, for a moment, he looks like himself again."
    s "[nome_compagno]..."
    $ cg("Close-up of Daniel leaning back in his chair, wine glass in hand, amused, looking straight at Sara", "images/cg/ep1/d3_11_daniel_brinda.webp")
    da "A novel. Now that's interesting. What's it about?"
    menu:
        sp "Why does he want to know?"
        "Laugh it off: «It's just a hobby.»":
            s "Oh, it's nothing. A hobby. Three chapters and a lot of coffee."
            da "Three chapters is more than most people ever write. Don't sell yourself short, Sara. Nobody else will do it for you."
            sp "Was that advice, or a dig at [nome_compagno]? With him I can't tell."
        "Tell him about it, with passion.":
            $ confidence(1)
            $ interest("daniel", 1, "Daniel listened to every word.")
            $ segna("ep1_d3_romanzo_daniel")
            s "It's about a woman who finds a door in her apartment. A door that wasn't there before."
            s "And she has to decide whether to open it. Whether the life behind it is better than the one she has."
            n "Daniel has stopped smiling. He's listening, chin on his hand, as if nobody else were at the table."
            da "And does she open it?"
            s "I don't know yet. That's the problem."
            da "Then I'll have to read it when you find out."
    call inizio_retroscena
    rs "Daniel takes a sip of wine. He won't forget the word «novel». He never forgets anything that might be useful."
    $ retroscena("daniel", "Daniel now knows that Sara is writing a novel.")
    call fine_retroscena

    $ cg("The long table: Daniel at the centre holding court, the colleagues laughing; Josh smiling with effort; Sara beside him", vestito_d3("09_tavolata"))
    n "The evening starts well. Daniel is the centre of the table, and he knows how to be: a story about a client abroad, an impression of the CEO that makes everybody laugh."
    $ musica("daniel")
    n "Then, between the starters and the main course, he starts to needle."
    da "Our [nome_compagno] is the most punctual man in the office. Pity he's just as punctual with his problems."
    n "A few laughs around the table. [nome_compagno] smiles, barely."
    da "No, really. Last week he sent me a forty-page report. Forty! I asked him for the numbers, and he gave me a novel."
    s "Maybe he's just thorough."
    da "Thorough. That's a lovely word, Sara. That's exactly what we say about people who will never be promoted."
    n "More laughter. Louder this time."

    $ cg("Close-up of Josh at the table, smiling with effort, his fork motionless, eyes on his plate", "images/cg/ep1/d3_10_josh_umiliato.webp")
    n "[nome_compagno] looks at his plate. He's still smiling, but his fork hasn't moved in a minute."
    sp "Say something. [nome_compagno], say something. Anything."
    $ cg("Close-up of Daniel leaning back in his chair, wine glass in hand, amused, looking straight at Sara", "images/cg/ep1/d3_11_daniel_brinda.webp")
    da "Seriously, Sara. How did he do it? A woman like you, with... a man so careful. He must have conquered you with a spreadsheet."

    $ cg("Close-up of Sara at the table, jaw tight, eyes flashing, between indignation and embarrassment", vestito_d3("12_sara_tavola"))
    menu:
        sp "That's enough. I can't let that one go."
        "Answer him back.":
            $ interest("daniel", 2, "Daniel likes people who stand up to him.")
            $ confidence(1)
            $ segna("ep1_d3_risposta_daniel")
            s "He conquered me by treating me with respect. Which, apparently, isn't something they teach in every job."
            n "For a second the table goes completely silent. Somebody coughs."
            $ cg("Close-up of Daniel leaning back in his chair, wine glass in hand, amused, looking straight at Sara", "images/cg/ep1/d3_11_daniel_brinda.webp")
            n "Then Daniel laughs. Really laughs, delighted, as if she'd given him a present."
            da "Touché! You see? She has character. [nome_compagno], maybe you should borrow a little of hers. For the office."
            sp "He turned it around again. How does he do that?"
            $ retroscena("daniel", "The more Sara stands up to him, the more Daniel enjoys himself.")
        "Squeeze [nome_compagno]'s hand under the table.":
            $ interest("josh", 2, "[nome_compagno] feels your hand.")
            $ segna("ep1_d3_mano_josh")
            n "Sara says nothing. Under the tablecloth she finds [nome_compagno]'s hand and squeezes it, hard."
            n "He squeezes back. A small, grateful pressure."
            $ cg("Close-up of Daniel leaning back in his chair, wine glass in hand, amused, looking straight at Sara", "images/cg/ep1/d3_11_daniel_brinda.webp")
            da "How sweet. You two are holding hands under the table, aren't you? [nome_compagno] needs support, eh?"
            n "[nome_compagno] lets go of her hand. His ears are red."
        "Change the subject, gracefully.":
            s "Can we talk about something else? This wine is wonderful. Who chose it?"
            $ cg("Close-up of Daniel leaning back in his chair, wine glass in hand, amused, looking straight at Sara", "images/cg/ep1/d3_11_daniel_brinda.webp")
            da "I did. Obviously."
            sp "Obviously."
            da "A red, fifteen years old. Patient wine. It waits years in the dark before anyone appreciates it. A bit like some employees."
            n "[nome_compagno] laughs with everyone else. Sara doesn't."

    $ cg("The long table: Daniel at the centre holding court, the colleagues laughing; Josh smiling with effort; Sara beside him", vestito_d3("09_tavolata"))
    n "The rest of the dinner goes on like that. Every one of Daniel's jokes sounds almost reasonable. Every time, [nome_compagno] takes it in silence."
    n "Sara has never seen him like this."
    sp "He's always made me feel protected. Tonight he looks like a schoolboy in the headmaster's office."
    $ nota_sara("daniel", "An arrogant show-off. He humiliated [nome_compagno] all evening.")

    ## Pausa in bagno: Emma, moglie di un collega (personaggio funzionale).
    $ cg("The restaurant's ladies' room: Sara at the mirror catching her breath; an elegant older woman reapplying lipstick beside her", vestito_d3("17_bagno"))
    $ musica(None)
    $ ambiente(None)
    n "Between the main course and dessert Sara escapes to the ladies' room. Two minutes. Two minutes without Daniel's voice."
    n "At the mirror there's a woman she noticed at the table: forties, elegant, the wife of one of [nome_compagno]'s colleagues. She's reapplying her lipstick with the calm of someone who's done this many times."
    $ cg("Close-up of Emma at the mirror, lipstick in hand, a knowing, slightly tired smile", "images/cg/ep1/d3_18_emma.webp")
    $ suono("rossetto")
    em "First company dinner?"
    s "Is it that obvious?"
    em "You still look surprised. Give it a couple of years. I'm Emma, by the way. Paul's wife. Accounts."
    em "Don't take it personally, with Daniel. He does it with every new one. He picks someone and plays with them all evening."
    em "Although..."
    n "She closes her lipstick and looks at Sara in the mirror. Up and down, quickly."
    em "Although I've never seen him in such good form. It must be you, sweetheart."

    menu:
        sp "What does that mean?"
        "Ask her what Daniel is really like.":
            $ segna("ep1_d3_emma_daniel")
            $ interest("daniel", 1, "Sara wants to know more about him.")
            s "What's he really like? Daniel."
            em "Charming. Brilliant. Generous, when he wants something."
            em "My husband adores him and hates him, sometimes in the same sentence."
            em "And he always, always gets what he wants. That's all I know. And it's all anybody here knows."
            sp "That's not reassuring."
        "Smile and go back to the table.":
            s "Well. Let's hope he gets bored soon."
            em "Oh, sweetheart. Men like Daniel don't get bored. They get busy."
            n "She winks at her in the mirror."
    em "Your [nome_compagno] is a sweetheart, by the way. Don't let anybody tell you otherwise."
    n "The door swings shut behind her. Sara stays at the mirror a moment longer and looks at her own reflection."
    sp "It must be you, sweetheart."
    sp "Great. Just great."

    ## Il brindisi: Daniel le parla da vicino.
    $ cg("Daniel standing by Sara's chair with a glass of champagne, leaning down to speak to her alone, while the others toast", vestito_d3("13_brindisi"))
    $ ambiente("ristorante")
    $ musica("daniel")
    $ suono("calici")
    n "At dessert Daniel stands for the toast: to the team, to the quarter, to the people who make it all possible. Applause."
    n "Then, while the others are refilling their glasses, he walks around the table and stops beside Sara's chair."
    da "I hope I wasn't too hard on him. It's a game, you know. [nome_compagno] knows it's a game."
    da "But you... you didn't play along. I like that. Most people here laugh at everything I say."
    n "He's close. Close enough that she can smell his cologne, something expensive and woody."

    menu:
        sp "What does he want from me?"
        "Answer coldly.":
            s "I didn't laugh because it wasn't funny."
            da "Fair enough. I'll try harder next time."
            n "He smiles, unbothered, and goes back to his seat."
            sp "Next time. As if there's going to be a next time."
        "Smile politely.":
            $ interest("daniel", 1, "A smile, even a polite one.")
            n "Sara smiles. It's [nome_compagno]'s boss. A smile costs nothing."
            s "It was a lovely dinner. Thank you for inviting partners."
            da "Thank {i}you{/i} for coming. You've made the evening a lot more interesting."
            n "He raises his glass slightly, just towards her, and goes back to his seat."
            sp "It's just politeness. That's all it is."
    return


## --- In auto: la riga di Josh su suo padre (I1) ---------------------------------

label ep1_d3_auto:
    $ vai("strada", "In the car — night")
    $ ambiente("pioggia_auto")
    $ suono("portiera_auto")
    $ musica("notte")
    $ cg("Night, inside the car: Josh driving in silence, both hands on the wheel, the city lights sliding over his face; Sara looking at him", vestito_d3("14_auto"))

    n "It has started to rain. In the car the silence weighs more than the dinner."
    n "[nome_compagno] drives with both hands on the wheel, the way they teach you at driving school and nobody ever does afterwards. The streetlights slide over his face, one after another."
    sp "Say something. One of us has to say something."

    menu:
        sp "What do I say to him?"
        "Comfort him: «He's the problem, not you.»":
            $ interest("josh", 3, "Sara is on his side.")
            $ segna("ep1_d3_consola")
            s "He's the problem. Not you. He's a pompous, insecure bully in a nice suit."
            $ cg("Close-up of Josh driving at night, eyes on the road, a tired, grateful half-smile", "images/cg/ep1/d3_15_josh_guida.webp")
            n "[nome_compagno] lets out a breath that sounds almost like a laugh."
            c "He's my boss, Sara. I can't afford to answer him back."
            c "And anyway... I'm used to it."
            s "Used to it?"
            c "My father talks like that. He always has. At every dinner, every Christmas. You learn to smile and wait for it to pass."
            n "He says it lightly, as if it were nothing. He doesn't look at her."
            sp "His father. All this time, and he's never told me that."
            s "You don't have to wait for anything to pass with me. You know that, right?"
            c "I know. That's why I love you."
        "Ask him why he didn't react.":
            $ interest("josh", -2, "For the first time, she sees him as weak.")
            $ segna("ep1_d3_rimprovero")
            s "Why didn't you say anything? Not a word, [nome_compagno]. All evening."
            $ cg("Close-up of Josh driving at night, jaw tight, eyes fixed on the road", "images/cg/ep1/d3_15_josh_guida.webp")
            c "And what should I have said? He signs my contract."
            s "Something. Anything. He called you a loser in front of everybody, and you laughed."
            c "My father talks like that. He always has. You learn to laugh along, or it gets worse."
            n "He says it flatly, eyes on the road. It doesn't sound like an excuse. It sounds like a rule he learned a long time ago."
            sp "His father. He's never told me that."
            sp "He's right, Daniel's his boss. And yet..."
            sp "And yet tonight, for the first time, I wanted him to be someone else."

    $ cg("Night, inside the car: Josh driving in silence, both hands on the wheel, the city lights sliding over his face; Sara looking at him", vestito_d3("14_auto"))
    n "They drive the rest of the way without the radio. When they get home [nome_compagno] goes straight to bed. Sara stays in the dark kitchen a little longer, still in her dress."
    sp "A spreadsheet. He said [nome_compagno] conquered me with a spreadsheet."
    sp "What an idiot."
    n "She doesn't know why she's still thinking about it."
    $ tappa("daniel", 1)
    return
