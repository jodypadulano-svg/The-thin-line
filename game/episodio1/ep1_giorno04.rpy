## =============================================================================
## EPISODE 1 — DAY 4 (Thursday)
## =============================================================================
## Calendar: docs/mese-1.md, day 4. Barbara walks past without looking; Jessica's
## new dress; phone filler with Josh at lunch (decision 17/11); evening drinks
## with the girls if accepted on day 1, otherwise a free evening.
## Seeds for the finales (decisioni.md, «Gli 8 finali»): the gold heart pendant of
## Barbara's circle, the cinnamon cappuccino, the puckered smoking, chapter three
## of the novel, «Love you!» / «Love you more!», the spreadsheet.
## Draft for Jody's review. Game text in English; comments in Italian.
## CG: docs/prompt-immagini/inquadrature-giorno-04.md. Finché mancano,
## compare la didascalia [CG].

label ep1_d4:
    call nuovo_giorno(4, "Thursday")
    call ep1_d4_redazione
    call ep1_d4_pausa_josh
    if fatto("ep1_aperitivo_accettato"):
        call ep1_d4_aperitivo
    else:
        call ep1_d4_serata_libera
    call ep1_d4_notte
    return


## --- Lavoro: Barbara non la guarda, il vestito di Jessica ----------------------

label ep1_d4_redazione:
    $ vai("redazione", "The newsroom — 9:10 a.m.")
    $ musica("redazione")
    $ ambiente("redazione")
    $ cg("The newsroom corridor: Barbara sweeping past Sara's desk without a glance, Sara half-rising from her chair with a printed draft in her hand", "images/cg/ep1/d4_01_barbara_passa.webp")

    if fatto("ep1_d3_proposta_cinema"):
        n "The cinema piece is on Barbara's desk at nine sharp. Twelve hundred words, rewritten until two in the morning."
        n "At ten past nine Barbara walks past Sara's desk. She doesn't stop. She doesn't look. Not even a «darling»."
        sp "She's read it. She hated it. Car parks until Christmas."
    else:
        n "The car park piece is on Barbara's desk at nine sharp. Eight hundred words on concrete, as sexy as concrete can be."
        n "At ten past nine Barbara walks past Sara's desk. She doesn't stop. She doesn't look. Not even a «darling»."
        sp "Did I do something wrong? Yesterday she called me darling in front of everybody."
    sp "Maybe it's nothing. Maybe she's just busy. Maybe I'm going to be fired."

    $ musica("barbara")
    $ suono("tazza")
    $ cg("Roberta leaning over Sara's desk to set down a cappuccino with cinnamon, a thin gold heart pendant swinging at her throat", "images/cg/ep1/d4_02_roberta_cappuccino.webp")
    n "A cup appears next to her keyboard. Cappuccino, no sugar, a little cinnamon on top. Like Monday. Like every day since Monday."
    ro "Don't take it personally. When she doesn't look at you, it means she's thinking about you."
    s "That's... not reassuring, Roberta."
    ro "It should be."
    n "Roberta smiles her wide, patient smile and leans in to straighten Sara's stapler. A thin gold heart swings on a chain at her throat."
    sp "Pretty. I've never noticed it before."

    $ musica("redazione")
    $ cg("Jessica twirling beside Sara's desk in a new fitted red dress, a thin gold heart pendant at her throat, beaming", "images/cg/ep1/d4_03_jessica_vestito.webp")
    n "Half an hour later Jessica stops by. Or rather, she makes an entrance."
    je "Sara. Be honest. Honest honest. What do you think?"
    n "A red dress, fitted, much shorter than anything Jessica wore when Sara met her. Red lipstick. Heels that click on the floor like a metronome."
    n "And at her throat, on a thin chain, a little gold heart. The same as Roberta's."
    $ cg("Close-up of Sara at her desk looking up at Jessica, a polite smile, a flicker of doubt in her eyes", "images/cg/ep1/d4_04_sara_scrivania.webp")
    sp "Two months ago she wore cardigans and argued with me about Anna Karenina for a whole lunch break."
    sp "Now she looks like... like a smaller Barbara."

    menu:
        sp "What do I tell her?"
        "«You look amazing.»":
            s "You look amazing, Jessica. Really."
            $ cg("Jessica twirling beside Sara's desk in a new fitted red dress, a thin gold heart pendant at her throat, beaming", "images/cg/ep1/d4_03_jessica_vestito.webp")
            je "Right? Barbara chose it. She has such an eye. She sees what you could be, you know? Before you see it."
            sp "Barbara chose her dress?"
        "«I liked you better before.»":
            $ confidence(1, "Sara says what she really thinks.")
            $ segna("ep1_d4_jessica_prima")
            s "Honestly? I liked you better before. You looked like... you."
            n "For a second something passes over Jessica's face. Not hurt. Something emptier, like a room where the furniture has been moved."
            $ cg("Jessica twirling beside Sara's desk in a new fitted red dress, a thin gold heart pendant at her throat, beaming", "images/cg/ep1/d4_03_jessica_vestito.webp")
            je "Before? Oh, Sara. Before I was so tired all the time."
            je "This is me. This is the real me. Barbara helped me find her."

    $ zoom_cg("Close-up of the little gold heart pendant at Jessica's throat", "images/cg/ep1/d4_03_jessica_vestito.webp", (943, 113, 400, 225))
    s "That's a pretty necklace. Roberta has the same one."
    je "Oh, this?"
    n "Jessica touches the little heart with two fingers, the way some people touch a cross."
    je "It's a gift. You get one when you... when you belong. You'll see."
    sp "When you belong. To what? The paper?"
    if fatto("ep1_d3_proposta_cinema"):
        je "Oh, and don't worry about Barbara. She read your cinema thing at seven this morning. She told Roberta it was «delicious»."
        je "She'll never tell you. That's how she is. She makes you wait."
        $ confidence(1, "Barbara liked the cinema piece.")
        sp "Delicious. She said delicious."
    $ nota_sara("capa", "Jessica and Roberta wear the same little gold heart. «You get one when you belong.»")
    return


## --- Pausa pranzo: il filler al telefono con Josh (decisione 17/11) ------------

label ep1_d4_pausa_josh:
    $ vai("redazione", "The newsroom — lunch break")
    $ musica("casa")
    $ cg("Sara alone at her desk at lunch, a half-eaten sandwich beside the keyboard, smiling at her phone", "images/cg/ep1/d4_05_pausa_telefono.webp")
    n "At one o'clock the newsroom empties. Sara stays at her desk with a sandwich and her phone."
    $ suono("telefono_vibra")
    n "Before she can unlock it, it buzzes. [nome_compagno]."
    call chat_josh_d4
    $ cg("Sara alone at her desk at lunch, a half-eaten sandwich beside the keyboard, smiling at her phone", "images/cg/ep1/d4_05_pausa_telefono.webp")
    n "She puts the phone face-down next to the sandwich. She's still smiling when Jessica's heels click back into the room."
    return

label chat_josh_d4:
    $ chat_aperta = "josh"
    show screen telefono_chat("josh")
    $ msg("josh", "Survived the morning?")
    $ msg("josh", "I've been thinking about last night. All morning. Sorry about Daniel. And about the car.")
    if fatto("ep1_d3_consola"):
        sp "He's still thinking about it. Of course he is."
        menu (screen="scelta_telefono"):
            "«You have nothing to be sorry for.»":
                $ msg("sara", "You have nothing to be sorry for. He's the idiot.")
                $ interest("josh", 1, "Sara is on his side.")
                $ msg("josh", "Pompous, insecure bully in a nice suit. I wrote it on a post-it. It's in my drawer.")
            "«Tell me about your dad, one day.»":
                $ msg("sara", "One day you'll tell me about your dad. Properly. Ok?")
                $ segna("ep1_d4_chiede_padre")
                $ msg("josh", "One day. Not today. Today I have three reports and a sandwich that tastes like cardboard.")
    else:
        sp "He's apologising. Like always."
        menu (screen="scelta_telefono"):
            "«I was harsh in the car. Sorry.»":
                $ msg("sara", "I was harsh in the car. I'm sorry. I was angry at him, not you.")
                $ interest("josh", 1, "Sara apologises.")
                $ msg("josh", "You were right, though. I should have said something.")
            "«Next time, answer him back.»":
                $ msg("sara", "Next time, answer him back. Please. For me.")
                $ confidence(1)
                $ msg("josh", "I'll try. Promise. Step one: stop laughing at his jokes.")
                sp "Step one. We'll see."

    $ msg("josh", "Speaking of Daniel. Guess who has to redo the quarterly spreadsheet. Third time.")
    sp "The spreadsheet. Of course it's a spreadsheet."
    menu (screen="scelta_telefono"):
        "«Make it the most beautiful spreadsheet ever.»":
            $ msg("sara", "Make it the most beautiful spreadsheet he's ever seen. Colour-coded. With a little heart in cell A1.")
            $ interest("josh", 1)
            $ msg("josh", "A heart in A1. Career suicide. Worth it.")
        "«After all, that's how you conquered me.»":
            $ msg("sara", "After all, that's how you conquered me. With a spreadsheet.")
            $ segna("ep1_d4_battuta_excel")
            $ msg("josh", "...Too soon.")
            $ msg("josh", "Ok, a little funny. Too soon, but funny.")
            sp "Why did I say that? It was Daniel's joke. Not mine."

    $ msg("josh", "Pizza tonight? Or do you have drinks with the girls?")
    if fatto("ep1_aperitivo_accettato"):
        $ msg("sara", "Drinks with the girls. I promised Jessica on Monday.")
        $ msg("josh", "Have fun. Don't let your boss make you drink anything green.")
    else:
        $ msg("sara", "Pizza. Definitely pizza.")
        $ msg("josh", "Best news of the day.")
    $ msg("josh", "Love you!")
    $ msg("sara", "Love you more!")
    hide screen telefono_chat
    $ chat_aperta = None
    return


## --- Sera A: l'aperitivo con le colleghe ----------------------------------------

label ep1_d4_aperitivo:
    $ vai("bar_aperitivo", "The Copper Room — 7:00 p.m.")
    $ musica("aperitivo")
    $ ambiente("bar")
    $ cg("A cosy cocktail bar at golden hour: the girls from the newsroom crowded around a low table full of colourful drinks; Sara among them, laughing a little stiffly", "images/cg/ep1/d4_06_bar_colleghe.webp")
    n "The Copper Room is the kind of bar where the cocktails have names longer than the newspaper's headlines. The girls from the office have taken the corner table, like every Thursday."
    n "Jessica, Roberta, the two girls from layout, the intern from the website. All women. Sara is starting to get used to it."
    je "Sara! You came! I told you she'd come, Roberta."
    ro "You did. You always know."
    sp "It's nice. It's... nice. Why do I feel like I'm being interviewed?"

    $ cg("Barbara making an entrance into the cocktail bar, leopard coat, red lips, every head at the corner table turning toward her", "images/cg/ep1/d4_07_barbara_arriva.webp")
    $ musica("barbara")
    n "At half past seven the door opens and the temperature of the room changes."
    n "Leopard coat. Red lips. Barbara crosses the bar like it belongs to her. Perhaps it does."
    ba "Girls! Don't get up. Well, get up a little. It's polite."
    n "Everyone laughs. Everyone gets up a little."
    sp "Barbara. Here. She didn't look at me all day."

    $ cg("Barbara leaning over Sara at the low table, holding out a pink cocktail in a coupe glass, her red-nailed hand light on Sara's shoulder", "images/cg/ep1/d4_08_barbara_drink.webp")
    ba "And you. The girl with the cinema."
    if not fatto("ep1_d3_proposta_cinema"):
        ba "Or rather the girl with the car park. Very solid. Very... grey."
    n "Barbara holds out a pink cocktail in a wide glass. Her hand rests on Sara's shoulder. It stays there."
    ba "I ordered for you. You look like someone who always orders the same thing. Tonight you don't."

    menu:
        sp "Take the drink?"
        "Accept the drink.":
            $ interest("capa", 1, "Sara lets Barbara choose for her.")
            $ segna("ep1_d4_drink_barbara")
            s "Thank you. What is it?"
            ba "Something you've never tried. That's all you need to know, darling."
            n "It's sweet, then bitter, then sweet again. Sara can't decide if she likes it. She takes a second sip to find out."
        "Decline with a smile.":
            s "That's very kind. Just water for me, if you don't mind."
            n "For a moment Barbara's smile doesn't move at all. Then it widens."
            ba "A woman who knows what she wants. How rare. How annoying."
            n "She hands the pink glass to Jessica without looking. Jessica takes it as if it were a prize."

    ## Col drink rosa se l'ha accettato, con un bicchiere d'acqua se l'ha rifiutato.
    if fatto("ep1_d4_drink_barbara"):
        $ cg("Close-up of Sara at the bar table, the pink cocktail in hand, cheeks a little flushed, caught between laughter and caution", "images/cg/ep1/d4_09_sara_bar.webp")
    else:
        $ cg("Close-up of Sara at the bar table, a glass of water in hand, cheeks a little flushed, caught between laughter and caution", "images/cg/ep1/d4_09_sara_bar_acqua.webp")
    n "The evening goes on. Barbara tells a story about a minister and a hotel bathtub that may or may not be true. The girls laugh at exactly the right moments."
    n "Sara notices that they all look at Barbara before they laugh. Just for a second. As if they were checking."

    menu:
        sp "Another round is coming."
        "One drink is enough.":
            s "Not for me, thanks. Tomorrow's an early start."
            ba "Of course. Early starts. Sensible girl."
            sp "Sensible. Why does it sound like an insult when she says it?"
        "Let herself go.":
            $ corruption(1, "Sara lets herself go a little.")
            $ interest("capa", 1)
            $ segna("ep1_d4_lasciarsi_andare")
            s "Why not. One more."
            $ cg("Close-up of Sara at the bar table, laughing freely with her head tilted back, cheeks flushed, a second glass in hand", "images/cg/ep1/d4_09b_sara_ride.webp")
            n "The second glass goes down easier than the first. At some point Sara realises she's laughing with her head thrown back, loudly, the way she hasn't laughed since university."
            ba "There she is. I knew there was someone in there."
            sp "There she is. Who?"

    ## Jessica e Roberta escono a fumare: lo stesso gesto del terrazzino (giorno 2).
    $ cg("Through the bar window: Jessica and Roberta smoking on the pavement outside, lips puckered tightly, exhaling slow, identical ribbons of smoke", "images/cg/ep1/d4_10_fumo_vetrina.webp")
    $ suono("accendino")
    n "At nine Jessica and Roberta step outside to smoke. Through the window Sara watches them light up."
    n "Lips puckered tight, the same way. Smoke out slow, the same way. Like two dancers who learned the same choreography."
    if fatto("sara_fuma"):
        sp "I know that taste now. I know exactly what they're feeling."
        sp "Why does part of me want to go outside with them?"
    elif fatto("ep1_jessica_fuma_notato") or fatto("ep1_guarda_fumo"):
        sp "Like on the terrace. Exactly like on the terrace. Even the way they hold the cigarette."
    else:
        sp "Funny. They smoke exactly the same way."

    ## Retroscena: lo sguardo di Barbara.
    call inizio_retroscena
    $ cg("Behind the scenes: Barbara alone at the table, chin resting on her hand, watching Sara at the window; outside, Jessica looks back at Barbara and nods", "images/cg/ep1/d4_11_barbara_sguardo.webp")
    rs "While Sara looks at the window, Barbara looks at Sara."
    rs "Outside, Jessica turns her head and meets Barbara's eyes through the glass. A tiny nod. A question."
    rs "Barbara smiles, and shakes her head. Not yet."
    $ retroscena("capa", "At the drinks Barbara and Jessica exchanged a look about Sara: «not yet».")
    call fine_retroscena

    $ cg("A cosy cocktail bar at golden hour: the girls from the newsroom crowded around a low table full of colourful drinks; Sara among them, laughing a little stiffly", "images/cg/ep1/d4_06_bar_colleghe.webp")
    $ musica("aperitivo")
    n "At ten Barbara pays for everyone, kisses the air next to every cheek and disappears into a taxi."
    n "Before she goes, she stops next to Sara. Close. Her perfume is heavy, sweet, expensive."
    ba "Delicious, by the way."
    if fatto("ep1_d3_proposta_cinema"):
        sp "The cinema piece. She means the cinema piece."
        sp "...Doesn't she?"
    else:
        sp "Delicious? The drink? Me?"
    $ tappa("capa", 1)
    return


## --- Sera B: serata libera (aperitivo rifiutato) ---------------------------------

label ep1_d4_serata_libera:
    $ vai("casa", "Home — evening")
    $ ambiente(None)
    $ musica("casa")
    n "No drinks with the girls tonight. Pizza on the way, [nome_compagno] in the shower, two free hours that belong to nobody."
    sp "Two hours. What do I do with two hours?"

    menu:
        sp "The evening is hers."
        "Write.":
            $ confidence(1, "Sara chooses her novel.")
            $ segna("ep1_d4_capitolo_tre")
            $ cg("Night, the kitchen: Sara alone at the table with her laptop, a cold cup of tea, the window dark behind her, typing with total concentration", "images/cg/ep1/d4_12_sara_scrive.webp")
            n "She opens the laptop at the kitchen table. Chapter three. The one she's been avoiding for a month."
            n "A woman alone in a kitchen, at night. Her husband asleep. A door at the end of the corridor that she has never opened."
            sp "What's behind the door? I don't know. I've never known."
            sp "Every time I get to the door, I stop writing."
            n "Tonight she gets to the door again. Her fingers stop on the keyboard."
            n "She doesn't open it. But for the first time, she writes that the handle is warm."
            sp "Warm. Why warm? Who's on the other side?"
        "An evening with [nome_compagno].":
            $ interest("josh", 1, "A quiet evening together.")
            $ segna("ep1_d4_sera_josh")
            $ cg("Night, the living room: Josh asleep against Sara's shoulder on the sofa, an empty pizza box on the table, the TV glow on their faces; Sara awake, gently stroking his hair", "images/cg/ep1/d4_13_divano_josh.webp")
            n "Pizza on the sofa. The fourth episode of the series they're both pretending to follow."
            n "By ten [nome_compagno] is asleep against her shoulder, his mouth a little open, a slice of crust still in his hand."
            sp "He's exhausted. Daniel is eating him alive."
            sp "I could wake him. I could go to bed. I could write."
            n "She stays. She strokes his hair until the episode ends, and then the next one."
            sp "This is nice. This is what nice feels like."
            sp "...Isn't it?"
    return


## --- Notte: il rituale ------------------------------------------------------------

label ep1_d4_notte:
    $ vai("casa", "Home — night")
    $ ambiente(None)
    $ musica("notte")
    if fatto("ep1_aperitivo_accettato"):
        n "When Sara gets home [nome_compagno] is already in bed, the bedside lamp still on, a work report open on his chest."
        if fatto("ep1_d4_lasciarsi_andare"):
            n "She takes her shoes off in the corridor so she won't wake him, and laughs at herself for no reason at all."
        c "Fun?"
        s "Strange. Fun. Strange."
        c "Did your boss make you drink something green?"
        if fatto("ep1_d4_drink_barbara"):
            s "Pink."
            c "Worse."
    n "Before she switches off the light, she touches her own throat. Where Jessica wears the little gold heart."
    sp "When you belong."
    sp "Belong to what?"
    c "Love you."
    s "Love you more."
    return
