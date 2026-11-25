## =============================================================================
## EPISODE 1 — DAY 13 (Saturday) — last day of the episode
## =============================================================================
## Calendar: docs/mese-1.md, day 13. Morning: shopping with Joanie for the party
## (dress: simple —, elegant Conf +1, daring chosen by Joanie Corr +2, Conf +1,
## Joanie +1). Afternoon: open gym, optional (Simon +2). Evening: Daniel's autumn
## party (Q&A 19/11, points 5-6): Daniel introduces Magnus (thank him Daniel +2,
## stay cool —); ★ with Magnus (enthusiasm +4, shyness +2, Conf 25 «pages
## tomorrow» +5 Conf +2); ★ at home, Magnus's card (tell Josh, Josh 30, Josh +2 ·
## keep it secret, Corr +2, Susp +3).
## Decisions with Jody (21/11):
## - A lot of tension and chemistry between Sara and Daniel; clues that she is
##   vulnerable to him, that he humiliates Josh and she can't, or doesn't want to,
##   defend him. No kiss (the first kiss is much later).
## - New choice at the toast: defend Josh / say nothing / smile at the joke.
## - The terrace: two doors. The zip (Daniel closes it slowly, whispering; close-up
##   of Sara, very aroused; a kiss on the ear; she tilts her neck) and the secret
##   (a lunch «one day», without telling Josh).
## - Simon: with Corruption 15 at the open gym, «Show me. Hands on.»
## - Joanie is shameless (her fantasies about Sara and other men; her feelings for
##   Sara are NOT hinted at in Episode 1).
## - Ending: the night's retroscena, then Daniel's message at 1:12, «typing...».
## Draft by Claude, 21/11/2026: to review with Jody.
## Game text in English; comments in Italian.
## CG: docs/prompt-immagini/inquadrature-giorno-13.md. Finché mancano,
## compare la didascalia [CG].

## Il vestito della festa cambia le immagini in cui si vede (come al giorno 3):
## base = il nero semplice; varianti _elegante e _audace.
init python:
    def cg13(descrizione, nome, varianti=("elegante", "audace")):
        ## varianti: i vestiti che hanno un'immagine propria; gli altri usano la base.
        if fatto("ep1_d13_vestito_audace") and "audace" in varianti:
            v = "_audace"
        elif fatto("ep1_d13_vestito_elegante") and "elegante" in varianti:
            v = "_elegante"
        else:
            v = ""
        cg(descrizione, "images/cg/ep1/%s%s.webp" % (nome, v))

label ep1_d13:
    call nuovo_giorno(13, "Saturday")
    call ep1_d13_shopping
    call ep1_d13_palestra
    call ep1_d13_invito
    call ep1_d13_festa
    call ep1_d13_terrazza
    call ep1_d13_ritorno
    call ep1_d13_notte
    return


## --- Mattina: shopping con Joanie ----------------------------------------------------------

label ep1_d13_shopping:
    $ vai("negozio", "A boutique in the centre — 10:40 a.m.")
    $ musica("aperitivo")
    $ cg("A small, elegant boutique: Joanie holding three dresses up against Sara at once, grinning; Sara laughing, half-protesting, in front of a tall mirror", "images/cg/ep1/d13_01_boutique.webp")
    n "Joanie picks her up at ten on the dot, honks twice, and doesn't let her finish her coffee."
    ch "Villa of the year. Bosses, clients, money. You are not going in that navy thing from the company dinner."
    s "What's wrong with the navy thing?"
    ch "Nothing. That's what's wrong with it."
    n "The boutique is the kind of place Sara walks past and never walks into. Joanie walks into it as if she owned the lease."
    n "Ten minutes later Sara is in the changing room with six dresses, and Joanie is on the other side of the curtain, narrating."
    if fatto("ep1_d12_consiglio_joanie"):
        ch "Last night you said maybe. I heard it. I have witnesses. Me."

    menu:
        sp "Which one?"
        "Keep it simple: the little black one.":
            $ segna("ep1_d13_vestito_sobrio")
            $ cg("The changing-room mirror: Sara in a simple, knee-length black dress, sleeves to the elbow, looking at herself with a small, sensible smile", "images/cg/ep1/d13_02a_sobrio.webp")
            s "This one. It's pretty. It's... me."
            ch "It's you at your aunt's funeral, babe."
            s "Jo."
            ch "Fine. Fine! It's lovely. You'll be the most elegant widow at the party."
            sp "It's a good dress. It's a safe dress. Nobody will look twice."
            sp "...Which is the point. Isn't it?"
        "Something elegant.":
            $ confidence(1, "Sara chooses a dress that makes her feel like a grown-up.")
            $ segna("ep1_d13_vestito_elegante")
            $ cg("The changing-room mirror: Sara in an elegant deep-green satin dress to the knee, thin straps, a zip at the back, turning to see herself, surprised and pleased", "images/cg/ep1/d13_02b_elegante.webp")
            s "This one."
            n "Deep green satin, thin straps, down to the knee. It shows a little. Just enough. It moves when she breathes."
            ch "Oh. Oh, okay. Okay, that's a grown woman. Who's that grown woman?"
            sp "That's me. I look like someone who gets invited to villas."
        "Let Joanie choose.":
            $ corruption(2, "Sara lets Joanie dress her for the party.")
            $ confidence(1, "Sara wears something she'd never have chosen.")
            $ interest("amica", 1, "Sara lets Joanie choose.")
            $ segna("ep1_d13_vestito_audace")
            s "...You choose."
            ch "Say that again. Slowly. I want to frame it."
            n "The curtain flies open before Sara can cover herself. Joanie doesn't knock. Joanie has never knocked in her life."
            n "She hangs one dress on the hook and takes all the others away."
            $ cg("The changing room: Joanie, half inside the curtain, holding up a black velvet corset dress with a sweetheart neckline, visible gold boning, a tiny keyhole with a gold ring between the cups and sheer black sleeves, a wicked grin; Sara in her slip, arms crossed over her chest, laughing and scandalised", "images/cg/ep1/d13_02c_audace.webp")
            ch "This. Black velvet, a corset, sheer sleeves, short. And a zip all the way down the back."
            ch "Look at the cups. Look how they're cut. This dress has one job, babe, and it isn't keeping you warm."
            n "Between the cups, right at the centre of the neckline, a tiny oval opening, closed by a thin gold ring. Like a full stop. Like a wink."
            ch "And no bra. Don't look at me like that. The corset does everything. A bra under this is a crime against fashion."
            s "Joanie! It's a work party! [nome_compagno]'s boss will be there!"
            ch "Exactly. Let him see what [nome_compagno] goes home to."
            ch "And if he looks... babe, let him look. Looking is free."
            ch "Personally? A man like that? I'd have him in the cloakroom between the starters and the speeches."
            s "You are a terrible person."
            ch "I'm a {i}wonderful{/i} person with a {i}terrible{/i} imagination. Put it on."
            $ cg("The changing-room mirror: Sara in the black velvet corset dress, sweetheart neckline lifting and framing her bust, the tiny gold ring between the cups, sheer black sleeves, looking at her reflection with wide eyes and parted lips, one hand at her throat; Joanie behind her, delighted", "images/cg/ep1/d13_02d_audace_specchio.webp")
            n "Sara puts it on. Joanie laces nothing, adjusts nothing: the corset knows exactly what to do. It lifts. It holds. It offers."
            n "Then Sara looks in the mirror, and for a long moment she doesn't say anything at all."
            sp "It's like a frame. And I'm the picture. And everybody is going to look at... the picture."
            sp "That isn't me."
            sp "...Is it?"
            ch "{i}There{/i} she is."

    n "At the till, Joanie takes a photo of her with the bag and sends it to herself. «For the archive.»"
    ch "Tonight I want messages. Live. Every hour. If Daniel speaks to you, I want the verbs."
    sp "With Joanie, saying no has never really been an option."
    return


## --- Pomeriggio: palestra libera (facoltativa) -------------------------------------------

label ep1_d13_palestra:
    $ vai("casa", "Home — 2:30 p.m.")
    $ musica("casa")
    $ cg("Josh carefully irons his white shirt for Daniel's party", "images/cg/ep1/d13_josh_stira_camicia.webp")
    n "Back home, [nome_compagno] is ironing his shirt for tonight for the third time, and practising his handshake on the coat rack."
    if fatto("ep1_palestra_da_sola"):
        sp "«Saturday morning? Open gym. No Joanie required.» He said morning. Joanie ate the morning."
        sp "But it's open all day."
    else:
        sp "The gym has an open day on Saturdays. Joanie says Simon is always there."
    sp "An hour of sweating instead of an hour of [nome_compagno] practising handshakes."

    menu:
        sp "The open gym?"
        "Go to the open gym.":
            call ep1_d13_simon
        "Skip it: she needs a nap before tonight.":
            $ segna("ep1_d13_niente_palestra")
            show expression Transform("images/cg/ep1/d13_josh_stira_camicia.webp", crop=(25, 440, 1280, 720), xysize=(config.screen_width, config.screen_height)) as cg_corrente
            with dissolve
            n "She lies down for twenty minutes and spends all twenty of them thinking about the dress in its bag."
    return

label ep1_d13_simon:
    $ segna("ep1_d13_palestra")
    $ vai("palestra", "The gym — 3:10 p.m.")
    $ musica("palestra")
    $ ambiente("palestra")
    $ cg("The almost empty gym on a Saturday afternoon: Simon by the squat rack, arms crossed, smiling as Sara walks in with her gym bag", "images/cg/ep1/d13_03_simon_open_gym.webp")
    n "Saturday afternoon, the gym is almost empty. Two old men on the bikes, the radio too loud, and Simon by the squat rack, as if he'd been waiting there."
    if fatto("ep1_palestra_da_sola"):
        si "Morning, I said. It's three."
        s "Joanie kidnapped me. Shopping."
    else:
        si "Look who's here. And no Joanie?"
        s "No Joanie. She took me shopping and then abandoned me."
    si "Joanie on a Saturday. Where's she now, then?"
    n "He says it lightly. Very lightly. He's looking at the barbell while he says it."
    s "Home, I think. Why?"
    si "No reason. Squats. Come on."
    n "Twenty minutes later her thighs are burning and Simon is watching her from the side with his arms crossed."
    si "Your hips. You're sitting back too late. Again."

    menu:
        sp "Again. She can't feel it."
        "«Show me. Hands on.»" (corruption=15):
            $ interest("simon", 3, "Sara asks Simon to correct her, hands on.")
            $ corruption(1, "Sara likes his hands on her hips.")
            $ segna("ep1_d13_mani_simon")
            $ cg("The gym: Sara at the bottom of a squat with an empty bar, Simon standing close behind her, his hands on her hips guiding her down; Sara's eyes half closed, a flush on her cheeks", "images/cg/ep1/d13_04_mani_simon.webp")
            s "Show me. Hands on. I can't feel it otherwise."
            n "For a second he doesn't move. Then he steps in behind her and puts his hands on her hips. Big hands. Warm through the leggings."
            si "Down. Slow. Back, not forward. Like you're sitting on something that isn't there."
            n "She goes down. His hands go with her, steady, sure. Then up."
            sp "Oh. Oh, I can feel it now."
            sp "I can feel a lot of things now."
            n "At the top of the third rep, his hands stay on her hips one second longer than the exercise needs. She doesn't step away. She lets the second pass."
            si "...Good. That's it. That's the one."
            n "His voice is a little lower than usual. He steps back and starts loading plates he doesn't need."
            sp "One second. It was one second."
            sp "Why didn't I move?"
        "«Just tell me. I'll get it.»":
            $ interest("simon", 2, "An hour of squats with Simon.")
            n "He tells her. Twice more. On the fourth try she gets it, and he whistles."
            si "There. That's a real squat. Six weeks ago you couldn't find this building."
            n "She laughs. He's proud of her, she can tell. Like a teacher. Like something more than a teacher, maybe. She doesn't look too closely."
    $ ambiente(None)
    $ nota_sara("simon", "Open gym on Saturday. Simon asked about Joanie a bit too casually.")
    return


## --- Retroscena: l'invito non è un caso (scheda di Daniel, D) ----------------------------

label ep1_d13_invito:
    $ luogo_corrente = ""
    scene bg nero with fade
    call inizio_retroscena
    $ cg("Retroscena: Daniel in a dark study at night, feet on the desk, typing on his phone with a small, satisfied smile; a glass of whisky beside him", "images/cg/ep1/d13_05_daniel_messaggio.webp")
    rs "Two days earlier, late on Thursday night, Daniel sends a message to an old friend."
    rs "{i}«Come on Saturday. There's someone you need to meet. An aspiring writer. Do me a favour: make her feel special.»{/i}"
    rs "The answer arrives a minute later: {i}«Since when do you do favours?»{/i}"
    rs "Daniel doesn't reply. He smiles at the screen, and turns off the light."
    $ retroscena("daniel", "Meeting the publisher at the party wasn't luck: Daniel arranged it.")
    call fine_retroscena
    return


## --- Sera: la festa d'autunno nella villa di Daniel (Q&A 19/11) --------------------------

label ep1_d13_festa:
    $ vai("villa_daniel", "Daniel's villa — 8:15 p.m.")
    $ musica("daniel_villa")    ## musica sexy della festa (Jody, 21/11)
    $ ambiente("bar")
    $ cg("The hilltop villa glowing above the drive and the parked cars", "images/cg/ep1/d13_villa_esterno.webp")
    n "The villa is up in the hills, all glass and stone and warm light, with cars parked along the drive that cost more than Sara's flat."
    n "[nome_compagno] holds her hand in the car park, too tight."
    c "Best people in the company. Clients. Investors. Two years ago I wasn't even on the list."
    c "Just... smile. Be you. And if Daniel says something, laugh. Please."
    $ cg13("The entrance of a hillside villa at night, lanterns and autumn leaves, elegant guests; Sara on Josh's arm, Josh visibly nervous; Daniel coming down the steps towards them, glass in hand, his eyes on Sara", "d13_06_arrivo")
    n "Daniel comes down the steps to meet them himself. Not a waiter. Him."
    da "[nome_compagno]. Good, you found it. And Sara."
    n "He looks at her. He takes his time about it. From her shoes up, slowly, as if he were reading a contract he intends to sign."
    if fatto("ep1_d13_vestito_audace"):
        da "Well. Somebody finally dressed you properly."
        da "I'd say it was your idea. But we both know you needed permission."
        sp "How does he... Don't blush. Do not blush."
        n "His eyes stop where the dress wants them to stop. On the little gold ring. And they stay there, unhurried, as if he had every right."
        n "She blushes. The corset holds her up and out, like something on display, and she feels his look like a hand. And he knows it. She can tell he knows it."
    elif fatto("ep1_d13_vestito_elegante"):
        da "Emerald. Careful, Sara. People will think you belong here."
        s "And do I?"
        da "That's what we'll find out tonight."
    else:
        da "Black. Discreet. Safe."
        da "You'll grow out of it."
    c "Isn't she beautiful?"
    da "She is. You're a lucky man, [nome_compagno]. Remember that. Luck runs out."
    n "He says it with a smile. [nome_compagno] laughs, a beat late."
    $ suono("calici")
    n "Then Daniel turns to a passing waiter without looking at him."
    da "Two. Now."
    n "And Sara, without meaning to, straightens her back. As if he had been speaking to her."
    sp "What was that? Why did I do that?"

    $ suono("telefono_vibra")
    n "Her phone, in her bag. Joanie, obviously."
    ch "{i}Is he looking? Of course he's looking. Describe the hands. ALL the details.{/i}"
    sp "The hands."
    n "She looks. She can't help it, now that Joanie's said it. Long fingers around the glass. A heavy watch. A hand that has never asked anybody for anything."
    sp "He's arrogant. Full stop."

    ## Il brindisi (Q&A 19/11): il contratto, «il team», niente Josh.
    $ vai("villa_daniel", "Daniel's villa — the great room, 9:30 p.m.")
    $ cg("The great room of the villa: Daniel on the stairs raising a glass to the crowd of guests; Josh in the crowd looking up hopefully; Sara beside him, and Daniel's eyes on her, not on the room", "images/cg/ep1/d13_07_brindisi.webp")
    n "At half past nine someone taps a glass. Daniel is on the third step of the staircase, so he can see everyone and everyone can see him."
    da "I'll be quick, because the wine is better than I am."
    da "Yesterday at eight p.m. we closed the Harrow contract. The biggest in this company's history."
    n "Applause. [nome_compagno] squeezes her hand so hard it hurts. Six weeks. Every evening. Friday until eight."
    da "I want to thank the team. You know who you are. Every one of you."
    da "To the team."
    n "Glasses rise. [nome_compagno]'s rises a second later than the others. His name doesn't come. It isn't going to."
    n "And all the time Daniel was talking, he wasn't looking at the team. He was looking at Sara."
    n "She is furious. She can feel it in her face. And she doesn't look away. Neither does he."
    sp "You did that on purpose. You did that in front of me on purpose."
    sp "...And you want me to know it."

    $ vai("villa_daniel", "Daniel's villa — 9:50 p.m.")
    $ musica("daniel")
    $ cg("Daniel puts a nervous Josh on the spot in front of his clients", "images/cg/ep1/d13_daniel_josh_clienti.webp")
    n "Later, Daniel crosses the room with three men in expensive suits and stops right next to them."
    da "Gentlemen, [nome_compagno]. [nome_compagno] was on Harrow too. Weren't you, [nome_compagno]?"
    c "Yes. I... yes, the whole time."
    da "The whole time. Photocopies, mostly. Somebody has to love paper. Every team needs one."
    n "The clients laugh. Somebody's wife laughs. [nome_compagno] laughs too, because he promised he would, and that's the worst part."
    $ cg("Sara weighs whether to answer Daniel in front of the clients", "images/cg/ep1/d13_sara_pensa_rispondere.webp")
    sp "Say something. Say something, Sara."

    menu:
        sp "Daniel is waiting. They're all waiting."
        "Defend [nome_compagno].":
            $ interest("josh", 2, "Sara stands up for [nome_compagno] in front of his boss.")
            $ interest("daniel", 1, "Daniel enjoys it when she bites.")
            $ segna("ep1_d13_difende_josh")
            s "He was there every night until eight. I know, because I ate dinner alone. Every night."
            n "It comes out smaller than she wanted. Her voice shakes on «alone»."
            $ cg("Daniel smiles after Sara defends Josh; the clients listen", "images/cg/ep1/d13_daniel_josh_clienti.webp")
            n "A silence. Then Daniel smiles at her, slow and pleased, the way you smile at a puppy that has growled."
            da "Loyal. Charming."
            da "Hold on to her, [nome_compagno]. She's the only one here who'd fight for you."
            $ cg("Sara absorbs Daniel's reply in silence", "images/cg/ep1/d13_sara_pensa_rispondere.webp")
            sp "He turned it round. I defended him and he turned it round, and now it's even worse."
        "Say nothing.":
            $ segna("ep1_d13_tace")
            n "Sara opens her mouth. And nothing comes out."
            n "She holds her glass. She looks at the floor. She waits for it to be over."
            sp "Why didn't I say anything?"
            sp "Because I couldn't think of what to say. Because they're clients. Because it would have made it worse."
            sp "...Because I didn't want to."
            n "The thought arrives and she pushes it away at once, the way you snatch your hand back from a hot pan."
        "Smile at the joke.":
            $ interest("josh", -2, "Sara smiles at a joke about [nome_compagno].")
            $ interest("daniel", 2, "Sara smiled at his joke.")
            $ corruption(1, "Sara smiles while Daniel humiliates [nome_compagno].")
            $ segna("ep1_d13_sorride")
            $ cg("Sara's involuntary half-smile at Daniel's joke", "images/cg/ep1/d13_sara_sorriso_trattenuto.webp")
            n "It's only a small smile. The corner of her mouth. It escapes her before she can stop it."
            n "Daniel sees it. Of course he sees it. His eyes glitter for a second, like a man who has just been dealt the card he wanted."
            n "[nome_compagno] sees it too. He looks at her, and then at his shoes."
            sp "It was funny. It was a little bit funny. That's all."
            sp "No. That isn't all, and I know it isn't."

    ## Magnus (Q&A 19/11, punto 6): solo l'editore. Daniel lo presenta.
    $ vai("villa_daniel", "Daniel's villa — the library, 10:15 p.m.")
    $ musica("ristorante")
    $ cg("Daniel finds Sara by the bookshelves before introducing her to Magnus", "images/cg/ep1/d13_daniel_scaffali.webp")
    n "Half an hour later, Daniel finds her by the bookshelves, where she has gone to stop thinking."
    da "There you are. Come. There's someone you should meet. [nome_compagno] tells me you write."
    s "[nome_compagno] tells you...?"
    da "He talks about you all the time. It's the only interesting thing he talks about. And I read your piece on Friday. «Not bad», I told him."
    if fatto("ep1_d3_proposta_cinema"):
        da "It was better than «not bad». Ada and Walter. Row F. I'm not going to tell him that."
    else:
        da "You made a car park sad. That's harder than it sounds. I'm not going to tell him that."
    $ cg13("A warm wood-panelled library in the villa: an elegant man in his early seventies with silver hair and thin glasses, a tumbler of whisky in his hand; beside him a poised woman in her forties with a silver bob and a dark dress, smiling at Sara as if she knew her; Daniel making the introduction", "d13_08_magnus")
    n "By the fire, a man in his early seventies, silver-haired, thin glasses, a suit so well cut it looks like it grew on him. Beside him, a woman of about forty with a silver bob and a dark dress, who isn't introduced."
    da "Magnus. An old friend. He publishes novels, when he has nothing better to do."
    $ incontra("editore")
    ed "Daniel exaggerates. I publish novels even when I have something better to do. It's a vice."
    ed "You write, he tells me. What do you write?"
    n "The woman with the silver bob says nothing. She smiles at Sara, warmly, as if they had met before. As if she already knew how this conversation will end."
    n "For a moment, Magnus looks at Sara's face a little longer than he needs to. As if she reminded him of someone."

    menu:
        sp "A publisher. A real one."
        "Tell him about the novel, with all her heart.":
            $ interest("editore", 4, "Magnus saw your passion.")
            $ segna("ep1_d13_magnus_entusiasmo")
            s "A novel about a woman who finds a door in her flat. A door that wasn't there before."
            ed "And what's behind it?"
            s "That's what I'm trying to find out. For three chapters now."
            ed "Then here's my second question. Does she close it again, after?"
            s "...I don't know yet."
            ed "Good. That's the most honest answer I've heard from a writer in years. Most of them know too much."
        "Downplay it, shyly.":
            $ interest("editore", 2, "Magnus noticed the novel she hid.")
            $ segna("ep1_d13_magnus_timida")
            s "Oh, nothing serious. I try, in my spare time."
            ed "All serious novels begin as nothing serious."
            ed "What's the first sentence? You know it by heart. Everyone does."
            s "«The door was there on Tuesday.»"
            ed "Hm. Not bad. Not bad at all."
        "«I'll send you the first fifty pages tomorrow.»" (confidence=25):
            $ interest("editore", 5, "Magnus likes people who believe in themselves.")
            $ confidence(2, "Sara asks for what she wants.")
            $ segna("ep1_d13_magnus_pagine")
            s "I'll send you the first fifty pages tomorrow. You won't regret it."
            ed "I hope not. I like people who don't apologise for their talent."
            ed "Two questions, then, so I know what I'm reading. Who's telling it? And does she want to be found?"
            s "She is. And... no. Not yet."
            ed "Good answers."

    n "Daniel has already drifted away towards the bar, towards [nome_compagno] and the clients. He doesn't look back. He leaves them alone without a second thought, as if Magnus couldn't possibly matter."
    $ retroscena("editore", "Daniel left them alone without thinking: he doesn't see his friend as a rival.")
    $ cg13("Close-up of Magnus's hand giving Sara a thick cream business card, a line written by hand across it in ink", "d13_09_biglietto", ("audace",))
    ed "Send them to me. This is my card."
    n "Thick cream card, raised letters. And across the back, handwritten, in ink: {i}Fifty pages. No more, no less.{/i}"
    $ da_numero("editore")
    $ segna("ep1_d13_biglietto")
    ed "No more because I'm old. No less because you're not allowed to hide."
    n "The woman with the silver bob touches Magnus's arm, and they move away. At the door she turns, and smiles at Sara once more."
    if fatto("ep1_d7_scena_audace"):
        sp "Where does page fifty end? Before she lets him come closer, or after?"
        sp "If it's in there... do I leave it in?"

    ## Daniel torna: la scelta del calendario.
    n "Ten minutes later Daniel is back at her side, a fresh glass in his hand for her. He doesn't ask if she wants it."
    da "Well?"
    s "He wants fifty pages."
    da "Of course he does. I told him you were worth reading."

    menu:
        sp "Daniel did this. For me."
        "Thank Daniel, sincerely.":
            $ interest("daniel", 2, "Sara thanked him sincerely.")
            $ segna("ep1_d13_ringrazia_daniel")
            s "Daniel. Thank you. Really. I don't... nobody's ever done something like that for me."
            da "Nobody's ever been worth it, then."
            n "He holds her eyes for a long second. She is the one who looks away first."
            sp "Oh. I didn't expect that. He remembered I write. He actually listened."
        "Stay cool with him.":
            $ segna("ep1_d13_fredda_daniel")
            s "That was kind. Thank you."
            n "Two sentences. Polite and cold, like a receipt."
            da "Cold. Good. You're angry about the toast."
            da "Stay angry, Sara. It suits you. It's the most alive you've looked all night."
            sp "I hate that he's right."

    ## Il numero (telefono, 18/11): se lo fa dare «per il romanzo».
    $ musica("daniel_villa")
    da "Give me your phone."
    s "Excuse me?"
    da "Magnus will tell me what he thinks of your pages before he tells you. You'll want to know. Phone."
    n "And her hand gives him the phone. Just like that. As if it belonged to someone else."
    n "He types, quick and sure. His phone buzzes once in his jacket. He hands hers back."
    da "There. Now we can reach each other. For the novel."
    $ da_numero("daniel")
    n "Under «Daniel», on her screen, a missed call to a number she now has. And he has hers."
    $ nota_sara("daniel", "He introduced me to a real publisher. He remembered I write. And he humiliated [nome_compagno] in front of everyone.")
    $ nota_sara("editore", "Magnus, a real publisher, wants my first fifty pages. «No more, no less.»")
    $ tappa("daniel", 2)
    $ tappa("editore", 1)
    return


## --- La terrazza: la cerniera e il segreto (Jody, 21/11) ----------------------------------

label ep1_d13_terrazza:
    $ vai("villa_daniel", "Daniel's villa — the terrace, 11:20 p.m.")
    $ musica("daniel_seduzione")    ## la terrazza e la cerniera (Jody, 21/11)
    $ ambiente(None)
    show expression Transform("images/cg/ep1/d13_salone_base.webp", crop=(720, 25, 864, 486), xysize=(config.screen_width, config.screen_height)) as cg_corrente
    with dissolve
    $ suono("telefono_vibra")
    n "Another message from Joanie."
    ch "{i}Bathroom. Lipstick. Then walk past him slowly. SLOWLY. Not to do anything. Just to see his face.{/i}"
    sp "Absolutely not."
    $ cg13("The villa's stone terrace at night, the lights of the town far below: Daniel leaning on the railing, turning his head as Sara steps out of the French windows, the party glowing behind her", "d13_10_terrazza")
    n "She goes out on the terrace instead, to breathe. The valley is black, with the lights of the town far below like spilled sugar."
    n "There's someone at the railing already. Alone, without a glass, his jacket open."
    ## Il videoclip a tempo di musica (Jody, 22/11): solo col corsetto, si può saltare.
    if fatto("ep1_d13_vestito_audace"):
        n "{i}The next scene plays to music and runs on its own, about three minutes.{/i}"
        menu:
            "Watch the scene.":
                call ep1_d13_videoclip
                jump ep1_d13_terrazza_pranzo
            "Skip the scene.":
                $ musica(None, dissolvenza=0)
    da "Escaping?"
    s "Breathing. It's allowed, I think. Even in your house."
    da "In my house almost everything is allowed. That's why people come."
    n "She should go back in. She stays. She stands at the railing, a metre away from him. Then less."
    s "You humiliated him. Tonight. Twice. In front of me."
    da "I told the truth in a nice suit. He didn't answer. You noticed that too."
    if fatto("ep1_d13_difende_josh"):
        da "You answered for him. Very sweet. Your voice shook."
    elif fatto("ep1_d13_sorride"):
        da "And you smiled. Don't worry. I won't tell anyone. Least of all him."
    else:
        da "And you said nothing. I watched you say nothing. It was the most honest thing anyone said all night."
    sp "He's arrogant. Full stop."
    sp "...Full stop."
    n "The wind comes up the hill, cold and sudden. Sara shivers."
    ## La giacca (Jody, 22/11): da dietro, si vedono solo spalle e capelli: vale per tutti i vestiti.
    $ cg("The terrace at night seen from behind Sara, at shoulder height: Daniel, in his white shirt, settling his dark suit jacket on her shoulders, his hands lingering; Sara's face in profile, turned slightly towards him, the valley lights below", "images/cg/ep1/d13_10b_giacca_spalle.webp")
    n "Without a word, Daniel takes off his jacket and puts it on her shoulders. It's warm. It smells of him: wood, smoke, something expensive."
    da "Last line of your piece. I've been thinking about it all week."
    if fatto("ep1_d3_proposta_cinema"):
        da "«The Riverside closes on the thirtieth. The people it made will stay open.»"
        da "Who made you, Sara? And who's keeping you closed?"
    else:
        da "«Concrete doesn't care. But it waits.»"
        da "You've been waiting a long time too. I can tell. I'm good at waiting myself. Not as good as you."
    sp "He learned it by heart. My last line. He learned it by heart."

    ## Porta 3: la cerniera (Jody, 21/11). Lui la chiude piano, parlandole all'orecchio.
    n "When she turns to go back in, the jacket slides a little off one shoulder. And she feels it: cool air, low on her back."
    sp "The zip. It's slipped. How long has it been open?"
    n "Daniel has already noticed. Of course he has. He's standing right behind her."
    da "Don't move."
    da "Allow me."

    menu:
        sp "His voice is right behind her ear."
        "Let him do it.":
            $ corruption(2, "Sara lets Daniel close her zip.")
            $ interest("daniel", 2, "Sara let him close her zip.")
            $ segna("ep1_d13_cerniera")
            call ep1_d13_cerniera
        "«I can do it myself.»":
            $ segna("ep1_d13_cerniera_da_sola")
            s "I can do it myself."
            n "She reaches behind her back. Her fingers can't find the tab. She tries again. It goes up, crooked, in little jerks."
            n "Daniel watches her do it, without helping, without moving. Smiling, as if he were watching a clock that he knows will strike."
            da "Of course you can."
            da "Next time, then."
            sp "There won't be a next time."
            sp "...He didn't even argue. Why didn't he argue?"

    ## Porta 1: il segreto (Jody, 21/11).
label ep1_d13_terrazza_pranzo:
    da "Lunch. One day. Just the two of us, to talk about your novel. About what Magnus says, and what he doesn't."
    da "[nome_compagno] doesn't need to know. He'd only feel small. He feels small so easily."
    n "It isn't a question. He's already looking at the party behind her, as if the answer were a formality."

    menu:
        sp "A lunch. A secret one."
        "«Maybe.»":
            $ interest("daniel", 3, "Sara said maybe.")
            $ corruption(1, "Sara keeps a door open for Daniel.")
            $ segna("ep1_d13_pranzo_forse")
            $ segreto("ep1_pranzo_daniel", "Daniel invited her to lunch, «one day». She said maybe, and didn't tell [nome_compagno].", 2)
            s "...Maybe."
            n "Just one word. She hears it leave her mouth, and she can't call it back."
            da "Maybe is a yes that's ashamed of itself. I'll take it."
            n "He leaves her there, with his jacket on her shoulders, and goes back inside without looking round."
            sp "Maybe. I said maybe. To Daniel."
            sp "It's only lunch. One day. Maybe never."
        "«[nome_compagno] will know.»":
            $ segna("ep1_d13_pranzo_no")
            s "If there's a lunch, [nome_compagno] will know about it."
            da "Of course. Of course he will."
            n "He smiles. He isn't disappointed in the slightest. He looks like a man who has heard «no» before, and knows how long it lasts."
            n "He goes back inside without looking round. His jacket is still on her shoulders."

    $ vai("villa_daniel", "Daniel's villa — 11:45 p.m.")
    $ musica("daniel_villa")
    $ cg("The villa's French windows: Josh, a little drunk and dishevelled, finding Sara as she comes in from the terrace wrapped in a man's dark jacket that is much too big for her; his smile fading", "images/cg/ep1/d13_12_giacca.webp")
    n "[nome_compagno] finds her a minute later, by the French windows. His tie is crooked; the clients have been buying."
    c "There you are! I was looking for... whose jacket is that?"
    s "Daniel's. It was cold outside."
    c "Oh. That's... that's nice of him."
    n "He says it slowly, as if he were checking each word for a hidden step."
    n "At the front door, when they leave, she gives the jacket back. Daniel takes it without looking at [nome_compagno] at all."
    da "Goodnight, Sara."
    da "Goodnight, [nome_compagno]. Drive carefully. You've got something valuable in that car."
    return


## --- La cerniera: il primo piano di Sara (Jody, 21/11) -----------------------------------

label ep1_d13_cerniera:
    ## Regia (Jody): lui chiude la cerniera piano e le parla all'orecchio; noi vediamo
    ## il primo piano di Sara, eccitatissima. In cima, un bacio leggero sull'orecchio
    ## e lei inclina il collo. Video se c'è, altrimenti la CG.
    $ cg("Close-up of Sara on the night terrace, Daniel just behind her, out of focus, his mouth at her ear: her eyes half closed, cheeks flushed, biting her lower lip, a breath escaping her", "images/cg/ep1/d13_11_cerniera.webp")
    n "His fingers find the tab at the small of her back. Cool metal, warm fingers. He doesn't hurry. He doesn't hurry at all."
    n "One tooth. Then another."
    da "Your dress has been trying to escape from you all evening. I've been watching it try."
    n "One more. His knuckles brush her skin, all the way up her spine, one vertebra at a time."
    da "You know what I noticed tonight?"
    da "You didn't look away. Not once. Not even when you hated me."
    sp "Step away. Say something. Laugh. Step away."
    n "She doesn't step away. Her eyes close on their own. She bites her lip, hard, and it still isn't enough."
    da "He doesn't see you, Sara. He's never really seen you."
    da "I do. Every centimetre I'm closing."
    n "A breath escapes her. Not a word. A sigh, small and shameless, that she will hear again tonight, in the dark."
    sp "Oh God. Oh God, I want..."
    n "The zip reaches the top. His fingers rest there, at the nape of her neck, for a moment that lasts much longer than a moment."
    ## Il video (Jody, 22/11): il momento della cerniera fino al collo inclinato. Senza audio,
    ## così continua la canzone. Se il file manca, si va avanti con le CG.
    $ filmato("images/video/ep1/d13_11_cerniera.webm")
    n "Then he bends his head, and kisses her. Only her ear. A light, dry, almost polite kiss, just below the lobe."
label ep1_d13_cerniera_collo:
    $ cg("Close-up of Sara at the moment of the kiss on the ear: her head tilting to the side, offering her neck, eyes closed, lips parted, a helpless, blissful expression", "images/cg/ep1/d13_11b_collo.webp")
    n "And Sara tilts her head."
    n "Just a little. To the side. Away from the kiss, towards it. Offering him her neck."
    n "Neither of them says anything. There's nothing to say. They both know what it means."
    n "Daniel steps back. Calm. Collected. As if he'd fixed a picture hanging crooked on a wall."
    sp "What did I just do?"
    sp "I tilted my head. I gave him my neck. In his house. With [nome_compagno] in the next room."
    sp "And if he hadn't stepped back... I wouldn't have."
    $ nota_sara("daniel", "On the terrace he closed my zip. Slowly. He kissed my ear. And I... I tilted my head.")
    return


## --- Ritorno: l'auto e il biglietto di Magnus --------------------------------------------

label ep1_d13_ritorno:
    $ vai("strada", "The car — 12:20 a.m.")
    $ ambiente("pioggia_auto")
    $ musica(None)
    $ cg("Inside the car at night, rain on the windscreen: Josh driving in silence, jaw tight, the dashboard lights on his glasses; Sara in the passenger seat, looking out of the window, her coat pulled tight", "images/cg/ep1/d13_13_auto.webp")
    n "It starts to rain on the way down the hill. [nome_compagno] drives in silence for ten minutes. Then:"
    c "He didn't say my name."
    c "Six weeks. Every night until eight. And he didn't say my name."
    if fatto("ep1_d13_difende_josh"):
        c "You stood up for me, though. In front of the Harrow people."
        c "...He made it sound like you had to. Like I needed my girlfriend to—"
        n "He stops. He doesn't finish."
    elif fatto("ep1_d13_sorride"):
        c "And you smiled."
        s "I didn't..."
        c "You smiled, Sara. I saw you."
        n "Then he doesn't say anything else, all the way home. The windscreen wipers say it for him."
    else:
        c "And you didn't say anything. Neither did I. So."
        n "«So.» He leaves it there, in the car, between them."
    sp "He's hurt. He's hurt and I'm..."
    if fatto("ep1_d13_cerniera"):
        sp "I'm thinking about a zip. God help me, I'm thinking about a zip."
    else:
        sp "I'm thinking about the terrace. About his jacket. About his voice."
    $ ambiente(None)

    $ vai("camera", "The bedroom — 12:55 a.m.")
    $ musica("notte")
    $ cg13("The bedroom at night by the bedside lamp: Sara sitting on the edge of the bed in her party dress, turning a cream business card over in her fingers; Josh behind her, already under the covers, facing the wall", "d13_14_biglietto_letto")
    n "At home [nome_compagno] undresses without turning on the light. Sara sits on the edge of the bed with Magnus's card in her hand."
    n "{i}Fifty pages. No more, no less.{/i}"
    c "You still up?"

    menu:
        sp "I should tell him."
        "Tell [nome_compagno] about Magnus." (josh=30):
            $ interest("josh", 2, "Sara shares her dream with [nome_compagno].")
            $ segna("ep1_d13_detto_josh")
            s "At the party I met a publisher. A real one. He wants to read my novel. Fifty pages."
            n "[nome_compagno] turns over. In the dark she can't see his face, but she hears it change."
            c "What? Sara, that's... that's amazing. I told you. Didn't I tell you?"
            c "...Daniel introduced you?"
            s "Yes. I know. I didn't expect it either."
            n "He's quiet for a moment too long. Then he finds her hand under the covers and squeezes it."
            c "Then I owe him one. Great. Just great."
        "Keep the card to herself, for now.":
            $ corruption(2, "Sara keeps a gift from Daniel's world to herself.")
            $ segreto("ep1_editore", "Magnus's card, and Daniel's help.")
            $ segna("ep1_d13_biglietto_segreto")
            s "Yes. Just thinking about the party. Go to sleep."
            n "She puts the card in the zip pocket of her bag, the one where she keeps her passport."
            sp "I'll tell him. When there's something real to tell."
            sp "It isn't a secret. It's just... not yet."
    if fatto("ep1_d13_pranzo_forse"):
        sp "And the lunch. «Maybe.» That one isn't «not yet». That one is just a secret."
    if fatto("ep1_d8_tace_simon") or fatto("ep1_d13_mani_simon"):
        sp "And Simon's hands, this afternoon. That's nothing. That's the gym."
    return


## --- La notte: i retroscena e il messaggio di Daniel (chiusura dell'Episodio 1) -----------

label ep1_d13_notte:
    ## I retroscena della notte sono passati nel montaggio finale (Jody, 21/11).

    $ vai("camera", "The bedroom — 1:12 a.m.")
    $ musica("notte")
    $ cg("Sara lies awake with her phone in hand, Josh asleep beside her with his back turned", "images/cg/ep1/d13_18_messaggio_daniel.webp")
    n "Sara can't sleep. [nome_compagno] is breathing slowly beside her, turned towards the wall."
    $ suono("telefono_vibra")
    n "The phone vibrates in her hand. Joanie."
    $ chat_aperta = "amica"
    show screen telefono_chat("amica")
    $ msg("amica", "REPORT. NOW.")
    if fatto("ep1_d13_cerniera"):
        $ msg("sara", "I ran into Daniel on the terrace. My zip had slipped. I let him do it up and he kissed my ear.")
        $ msg("amica", "Your EAR. Okay, but how did it feel?")
        menu (screen="scelta_telefono"):
            "Admit she wanted him to do it again.":
                $ msg("sara", "I went all warm. I tilted my head without thinking. I think I wanted him to do it again.")
                $ msg("amica", "Oh, Sara. Is that the first time you've said that to yourself, too?")
            "Tell her how much it caught her off guard.":
                $ msg("sara", "I tilted my head before I'd even thought about it. That was the part that threw me. I keep thinking about it.")
                $ msg("amica", "I get it. You can sit with that for a bit. You don't have to figure it out tonight.")
            "Keep how she felt to herself.":
                $ msg("sara", "I don't know how to talk about that yet. Can I just tell you what happened next?")
                $ msg("amica", "Of course. I'm here.")
    else:
        $ msg("sara", "I ran into Daniel on the terrace. He offered to do up my zip. I told him I could do it myself.")
        $ msg("amica", "You and your extremely capable hands. Go on.")
    if fatto("ep1_d13_pranzo_forse"):
        $ msg("sara", "He asked me to lunch to talk about the novel. He said [nome_compagno] didn't need to know. I said maybe.")
        $ msg("amica", "Maybe. Okay. Are you still saying maybe now that you're home?")
    else:
        $ msg("sara", "Then he asked me to lunch. He wanted it to be our secret. I told him [nome_compagno] would know.")
        $ msg("amica", "You said that to his face? Oh, I wish I'd seen it.")
    hide screen telefono_chat
    $ chat_aperta = None
    $ suono("telefono_vibra")
    $ musica("daniel_notte")    ## il messaggio dell'1:12 (Jody, 21/11)
    n "Then a new message appears. A number saved four hours ago."
    if fatto("ep1_d13_cerniera") and fatto("ep1_d13_pranzo_forse"):
        n "{i}Daniel: «You tilted your head. And you said maybe. Both of those were yes, Sara.»{/i}"
    elif fatto("ep1_d13_cerniera"):
        n "{i}Daniel: «I can still feel the zip under my fingers. Can you?»{/i}"
    elif fatto("ep1_d13_pranzo_forse"):
        n "{i}Daniel: «Fifty pages for him. One lunch for me. That's a fair price, isn't it?»{/i}"
    else:
        n "{i}Daniel: «You closed it yourself. Brave girl. Goodnight, Sara.»{/i}"
    sp "Daniel."
    sp "It's one in the morning. [nome_compagno] is right here."
    n "Her thumb hangs over the screen. She doesn't write anything. She doesn't put the phone down either."
    n "And under his message, three little dots appear."
    n "{i}Daniel is typing...{/i}"
    $ via_cg()
    $ luogo_corrente = ""
    scene bg nero with fade
    pause 1.5
    return


## --- Nella prossima puntata (piano di pubblicazione, sezione 2) ---------------------------
## Bozzetti del prossimo episodio: parte comune e una o due anteprime personalizzate.

label ep1_teaser:
    $ luogo_corrente = ""
    scene bg nero with fade
    n "{size=+12}Next time, on The Thin Line...{/size}"
    $ cg("Episode 2 preview: a sketch of two families at a long Sunday lunch table, Hugo at its head, a hand beside an empty plate in the foreground", "images/cg/ep2/teaser_pranzo_famiglie.webp")
    n "Sunday lunch. Two families at one table. And a man at its head who has never once said a kind word to his son."
    python:
        _anteprime = []
        if valore_interest("simon") >= max(valore_interest("daniel"), valore_interest("howard"), valore_interest("capa")) and fatto("ep1_palestra_da_sola"):
            _anteprime.append((
                "Episode 2 preview: a sketch of the empty gym after hours, warm light spilling through an open door",
                "The gym, after closing time. Sara arrives early. Too early.",
                "images/cg/ep2/teaser_simon.webp",
            ))
        if fatto("ep1_howard_caffe") in ("si", "forse") or howard_visite >= 2:
            _anteprime.append((
                "Episode 2 preview: a sketch of the green door ajar on the landing, two cups on a tray",
                "Josh works late again. And next door, the coffee is already on.",
                "images/cg/ep2/teaser_howard.webp",
            ))
        if fatto("ep1_d10_bottone_aperto") or fatto("ep1_aperitivo_accettato"):
            _anteprime.append((
                "Episode 2 preview: a sketch of Barbara's office, her red nails resting beside a folder on the desk",
                "«Stay half an hour, darling. Just half an hour.»",
                "images/cg/ep2/teaser_barbara.webp",
            ))
        if not _anteprime:
            _anteprime.append((
                "Episode 2 preview: a sketch of a candlelit table for two, a hand near a small box in a jacket pocket",
                "Josh has booked a table. He's been planning something.",
                "images/cg/ep2/teaser_josh.webp",
            ))
        if fatto("ep1_d13_biglietto"):
            _anteprime.insert(0, (
                "Episode 2 preview: a sketch of a thick envelope held up to a wooden door with a brass plaque",
                "The fifty pages. And the door of a publishing house that doesn't open for just anyone.",
                "images/cg/ep2/teaser_editore.webp",
            ))
        _anteprime = _anteprime[:2]
    $ cg(_anteprime[0][0], _anteprime[0][2] if len(_anteprime[0]) > 2 else None)
    $ renpy.say(n, _anteprime[0][1])
    if len(_anteprime) > 1:
        $ cg(_anteprime[1][0], _anteprime[1][2] if len(_anteprime[1]) > 2 else None)
        $ renpy.say(n, _anteprime[1][1])
    $ cg("Episode 2 preview: a sketch of a man in shadow at a bar, his ring catching the light on the counter", "images/cg/ep2/teaser_jacob.webp")
    n "And on a Friday night, in a bar across town, a man Sara left four years ago. And has never quite forgotten."
    n "{i}«Some doors you close. Some doors you only think you closed.»{/i}"
    $ via_cg()
    $ luogo_corrente = ""
    scene bg nero with fade
    return


## --- Montaggio prima del teaser: un ritratto per ogni strada (Jody, 22/11) ----------------
## Dieci immagini scorrono con una panoramica laterale, mentre passa una canzone malinconica e sexy
## cantata da una voce femminile (`chiusura_ep1`, docs/prompt-audio.md). Il giocatore
## vede quello che Sara non sa. Jacob e Darius non si nominano: si capisce più avanti.

transform panoramica_destra(durata=7.0):
    zoom 1.18 xalign 0.0 yalign 0.5
    linear durata xalign 1.0

transform panoramica_sinistra(durata=7.0):
    zoom 1.18 xalign 1.0 yalign 0.5
    linear durata xalign 0.0

init python:
    def quadro(descrizione, immagine, verso="destra", durata=7.0):
        """Un'inquadratura del montaggio: panoramica laterale lenta, poi pausa."""
        renpy.hide_screen("segnaposto_cg")
        if renpy.loadable(immagine):
            t = panoramica_destra(durata) if verso == "destra" else panoramica_sinistra(durata)
            renpy.show("cg_corrente", what=At(immagine, t))
            renpy.with_statement(dissolve)
        else:
            renpy.hide("cg_corrente")
            renpy.show_screen("segnaposto_cg", descrizione=descrizione)

    def battuta_montaggio(testo, durata, chi=None, colore="#ffffff"):
        """Mostra la battuta per il tempo di lettura previsto, senza clic."""
        renpy.show_screen("battuta_tempo", chi=chi, testo=testo, colore=colore, pensiero=False)
        renpy.pause(durata, hard=True)
        renpy.hide_screen("battuta_tempo")

## L'epilogo si può saltare (Jody, 25/11): un pulsante discreto, sempre visibile.
## Va mostrato dopo inizio_retroscena e tolto prima di fine_retroscena, perché il
## salto dentro quelle chiamate lascerebbe il ritorno nel punto sbagliato.
screen salta_epilogo():
    zorder 70
    textbutton "Skip epilogue":
        xalign 0.98 ypos 30
        padding (24, 12)
        background Solid("#00000080")
        hover_background Solid("#000000d0")
        text_size 26
        text_color "#d9c8d0"
        text_hover_color "#ffffff"
        action Jump("ep1_d13_montaggio_fine")

label ep1_d13_montaggio:
    $ luogo_corrente = ""
    scene bg nero with fade
    $ musica("chiusura_ep1")
    call inizio_retroscena
    show screen salta_epilogo
    $ quadro("Sara in bed in the dark, her phone on her chest, smiling to herself, Josh asleep beside her", "images/cg/ep1/d13_m01_sara.webp", "destra")
    $ renpy.pause(8.0, hard=True)
    $ quadro("Howard's hand in the yellow lamplight, holding a pair of pale pink lace panties, the drawer open, the brass key beside it", "images/cg/ep1/d13_m02_howard.webp", "sinistra")
    $ renpy.pause(8.0, hard=True)
    $ quadro("Simon alone in the empty gym at night, training hard under a single light, sweat on his back", "images/cg/ep1/d13_m03_simon.webp", "destra")
    $ renpy.pause(8.0, hard=True)
    $ quadro("Joanie curled on her sofa at night, typing on her phone with a wicked little smile, her boyfriend asleep behind her", "images/cg/ep1/d13_m04_joanie.webp", "sinistra")
    $ renpy.pause(7.0, hard=True)
    $ quadro("A man's hand only, strong, a heavy ring, holding a phone with a new message on the screen; a dim bar behind", "images/cg/ep1/d13_m05_jacob.webp", "destra")
    $ battuta_montaggio("{i}Joanie: «Same bar. Friday. I'll bring her.»{/i}", 7.0)
    $ quadro("Darius alone at a kitchen table at night, looking at a photograph we cannot see, a beer going warm beside him", "images/cg/ep1/d13_m06_darius.webp", "sinistra")
    $ renpy.pause(8.0, hard=True)
    $ quadro("Low close-up at the foot of a bed in shadow, too close to see who is in it: on the floor a leopard-print blouse and skirt tangled with a fitted red dress, red heels, a gold heart pendant", "images/cg/ep1/d13_m07_barbara.webp", "destra")
    $ renpy.pause(8.0, hard=True)
    $ quadro("The back seat of a dark car at night, city lights sliding past: Magnus looking out of the window, the woman with the silver bob beside him, her hand on his arm", "images/cg/ep1/d13_m08_magnus_auto.webp", "sinistra")
    $ battuta_montaggio("In the back of a black car going down the hill, the woman with the silver bob rests her hand on Magnus's arm.", 7.0)
    $ battuta_montaggio("{i}«Is it her?»{/i}", 3.0)
    $ battuta_montaggio("Magnus doesn't answer. He looks at the lights of the town, and smiles very slightly.", 5.5)
    $ quadro("Magnus's hand holding an old, faded photograph of a young woman with wavy hair, laughing; a leather album under a green lamp", "images/cg/ep1/d13_m09_foto.webp", "destra")
    $ battuta_montaggio("Later, in his study, he opens an old album, and stops at a photograph from a long time ago.", 6.0)
    $ battuta_montaggio("A young woman, laughing at whoever held the camera. Wavy hair. That same way of laughing with her whole face.", 6.5)
    $ retroscena("editore", "Magnus keeps an old photo of a young woman who looks a lot like Sara.")
    $ retroscena("editore", "The woman with the silver bob asked him: «Is it her?»")
    $ quadro("The villa's great room after the party, candles burning low: Daniel and Magnus alone by the dying fire, two glasses of whisky", "images/cg/ep1/d13_m10_daniel_magnus.webp", "sinistra", 10.0)
    $ battuta_montaggio("Interesting, your friend.", 3.5, "Magnus", "#d4b483")
    $ battuta_montaggio("Isn't she.", 2.5, "Daniel", VC_DANIEL)
    $ battuta_montaggio("Very.", 3.0, "Magnus", "#d4b483")
    $ battuta_montaggio("Daniel smiles, pleased with himself. He thinks it's a compliment to his taste.", 5.0)
    $ battuta_montaggio("It doesn't occur to him, not even for a second, that it might not be about him at all.", 6.5)

label ep1_d13_montaggio_fine:
    hide screen salta_epilogo
    hide screen battuta_tempo
    ## Le note del Diario valgono anche per chi salta (chi ha visto tutto non le ripete).
    $ retroscena("editore", "Magnus keeps an old photo of a young woman who looks a lot like Sara.")
    $ retroscena("editore", "The woman with the silver bob asked him: «Is it her?»")
    $ retroscena("daniel", "He thinks Magnus was complimenting him. He doesn't see his old friend as a rival.")
    call fine_retroscena
    $ via_cg()
    $ luogo_corrente = ""
    scene bg nero with fade
    ## La canzone continua quando entra il teaser.
    return


## --- Il videoclip della terrazza (Jody, 22/11) ---------------------------------------------
## Solo col corsetto, se il giocatore sceglie di guardarlo. Tutto a tempo sulla canzone
## `daniel_seduzione` (tempi in docs/prompt-audio.md): le battute compaiono da sole fra un
## video e l'altro (campo e controcampo), i video A, B e C cadono sui ritornelli e sulla
## seconda strofa, la cerniera sul ponte. Il giocatore non clicca, tranne nelle scelte.
## Se un video o un'immagine mancano, si vede l'immagine di riserva o la didascalia [CG].

screen battuta_tempo(chi, testo, colore, pensiero):
    zorder 60
    frame:
        xalign 0.5
        yalign 0.95
        xminimum 900
        xmaximum 1600
        padding (40, 22)
        background Solid("#000000b0")
        vbox:
            spacing 6
            if chi:
                text chi size 32 bold True color colore
            if pensiero:
                text "(" + testo + ")" size 34 italic True color "#d9c8d0"
            else:
                text testo size 34 color "#ffffff"

init python:
    import time as _tempo_vc
    _vc = {"inizio": 0.0, "pausa": None}

    def vc_inizia():
        """Fa ripartire la canzone dall'inizio e azzera l'orologio della scena."""
        f = _file_audio("musica", "daniel_seduzione")
        if f:
            renpy.music.play(f, channel="music", loop=False, fadein=0.5)
        _vc["inizio"] = _tempo_vc.time()
        _vc["pausa"] = None

    def vc_ora():
        if _vc["pausa"] is not None:
            return _vc["pausa"] - _vc["inizio"]
        p = renpy.music.get_pos("music")
        if p is not None:
            return p
        return _tempo_vc.time() - _vc["inizio"]

    def vc_a(secondi):
        """Aspetta (senza che il clic possa saltare) che la canzone arrivi a quel punto."""
        if renpy.is_in_test():
            return
        while vc_ora() < secondi:
            renpy.pause(0.05, hard=True)

    def vc_pausa(pausa):
        """Ferma o riprende la canzone (durante le scelte)."""
        try:
            renpy.music.set_pause(pausa, channel="music")
        except Exception:
            pass
        if pausa:
            _vc["pausa"] = _tempo_vc.time()
        elif _vc["pausa"] is not None:
            _vc["inizio"] += _tempo_vc.time() - _vc["pausa"]
            _vc["pausa"] = None

    def vc_quadro(immagine, descrizione=""):
        renpy.hide_screen("segnaposto_cg")
        if renpy.loadable(immagine):
            renpy.show("cg_corrente", what=Transform(immagine, fit="cover", xysize=(config.screen_width, config.screen_height)))
            renpy.with_statement(dissolve)
        else:
            renpy.hide("cg_corrente")
            renpy.show_screen("segnaposto_cg", descrizione=descrizione or immagine)

    def vc_video(video, riserva, descrizione=""):
        renpy.hide_screen("battuta_tempo")
        if renpy.loadable(video):
            renpy.hide_screen("segnaposto_cg")
            renpy.show("cg_corrente", what=Movie(play=video, loop=False, size=(config.screen_width, config.screen_height)))
            renpy.with_statement(dissolve)
        else:
            vc_quadro(riserva, descrizione)

    def vc_riga(chi, testo, colore="#ffffff", pensiero=False):
        renpy.show_screen("battuta_tempo", chi=chi, testo=testo, colore=colore, pensiero=pensiero)
        renpy.restart_interaction()

    def vc_via():
        renpy.hide_screen("battuta_tempo")

define VC_DANIEL = "#c9a0ff"
define VC_SARA = "#e8a3b8"
define VC_PP_DANIEL = "images/cg/ep1/d13_10c_daniel_pp.webp"
define VC_PP_SARA = "images/cg/ep1/d13_10d_sara_pp.webp"
define VC_PP_SARA_SENZA_GIACCA = "images/cg/ep1/d13_10d_sara_pp_senza_giacca.webp"

label ep1_d13_videoclip:
    $ segna("ep1_d13_videoclip")
    $ renpy.block_rollback()
    $ luogo_corrente = ""
    $ vc_inizia()
    ## Strofa 1 (0:00-0:49): campo e controcampo.
    $ vc_a(0); vc_quadro("images/cg/ep1/d13_10_terrazza_audace.webp")
    $ vc_a(2); vc_riga("Daniel", "Escaping?", VC_DANIEL)
    $ vc_a(6); vc_quadro(VC_PP_SARA_SENZA_GIACCA, "Close-up of Sara on the terrace in the corset dress, listening, tempted"); vc_riga("Sara", "Breathing. It's allowed, I think.", VC_SARA)
    $ vc_a(10); vc_quadro(VC_PP_DANIEL, "Close-up of Daniel on the terrace, white shirt, a half smile"); vc_riga("Daniel", "In my house almost everything is allowed.", VC_DANIEL)
    $ vc_a(15); vc_quadro(VC_PP_SARA_SENZA_GIACCA); vc_riga("Sara", "You humiliated him. Twice.", VC_SARA)
    $ vc_a(20); vc_quadro(VC_PP_DANIEL); vc_riga("Daniel", "I told the truth in a nice suit.", VC_DANIEL)
    if fatto("ep1_d13_difende_josh"):
        $ vc_a(25); vc_riga("Daniel", "You answered for him. Your voice shook.", VC_DANIEL)
    elif fatto("ep1_d13_sorride"):
        $ vc_a(25); vc_riga("Daniel", "And you smiled. I won't tell him.", VC_DANIEL)
    else:
        $ vc_a(25); vc_riga("Daniel", "And you said nothing. The most honest thing anyone said all night.", VC_DANIEL)
    $ vc_a(31); vc_riga("Daniel", "And you wore {i}that{/i}. For whom, Sara?", VC_DANIEL)
    $ vc_a(37); vc_quadro(VC_PP_SARA_SENZA_GIACCA); vc_riga("Sara", "For myself.", VC_SARA)
    $ vc_a(41); vc_quadro(VC_PP_DANIEL); vc_riga("Daniel", "Liar.", VC_DANIEL)
    $ vc_a(45); vc_quadro(VC_PP_SARA_SENZA_GIACCA); vc_riga(None, "He's arrogant. Full stop.", pensiero=True)
    ## Ritornello 1 (0:49): video A, la giacca e l'anellino.
    $ vc_a(49); vc_video("images/video/ep1/d13_va_giacca.webm", "images/cg/ep1/d13_10b_giacca_spalle.webp")
    $ vc_a(64); vc_quadro(VC_PP_DANIEL); vc_riga("Daniel", "Cold?", VC_DANIEL)
    $ vc_a(68); vc_quadro(VC_PP_SARA); vc_riga("Sara", "Not any more.", VC_SARA)
    $ vc_a(72); vc_riga(None, "He's looking. Right there. And I'm letting him.", pensiero=True)
    ## Strofa 2 (1:18): video B, lui le gira intorno; Josh ride dietro il vetro.
    $ vc_a(78); vc_video("images/video/ep1/d13_vb_vetro.webm", "images/cg/ep1/d13_10_terrazza_audace.webp")
    $ vc_a(93); vc_quadro(VC_PP_DANIEL); vc_riga("Daniel", "He's laughing in there. Hear him?", VC_DANIEL)
    $ vc_a(98); vc_quadro(VC_PP_SARA); vc_riga("Sara", "Don't.", VC_SARA)
    $ vc_a(101); vc_quadro(VC_PP_DANIEL); vc_riga("Daniel", "Don't what?", VC_DANIEL)
    $ vc_a(104); vc_quadro(VC_PP_SARA); vc_riga(None, "Don't stop.", pensiero=True)
    $ vc_a(108); vc_quadro(VC_PP_DANIEL); vc_riga("Daniel", "The last line of your piece. I've been thinking about it all week.", VC_DANIEL)
    if fatto("ep1_d3_proposta_cinema"):
        $ vc_a(113); vc_riga("Daniel", "«The people it made will stay open.» Who's keeping you closed, Sara?", VC_DANIEL)
    else:
        $ vc_a(113); vc_riga("Daniel", "«Concrete doesn't care. But it waits.» You've been waiting a long time too.", VC_DANIEL)
    ## Ritornello 2 (2:00): video C, le mani sui fianchi.
    $ vc_a(120); vc_video("images/video/ep1/d13_vc_fianchi.webm", "images/cg/ep1/d13_11_cerniera.webp")
    $ vc_a(135); vc_quadro("images/cg/ep1/d13_11_cerniera.webp"); vc_riga("Daniel", "Your zip.", VC_DANIEL)
    $ vc_a(140); vc_riga("Daniel", "Don't move.", VC_DANIEL)
    $ vc_a(144); vc_riga("Daniel", "Allow me.", VC_DANIEL)
    $ vc_a(149); vc_via(); vc_pausa(True)

    ## La scelta (la canzone si ferma e riparte dopo).
    menu:
        sp "His voice is right behind her ear."
        "Let him do it.":
            $ corruption(2, "Sara lets Daniel close her zip.")
            $ interest("daniel", 2, "Sara let him close her zip.")
            $ segna("ep1_d13_cerniera")
            $ vc_pausa(False)
            ## Il ponte (2:29): il video della cerniera, 14 secondi.
            $ vc_video("images/video/ep1/d13_11_cerniera.webm", "images/cg/ep1/d13_11_cerniera.webp")
            $ vc_a(163)
            call ep1_d13_cerniera_collo
        "«I can do it myself.»":
            $ segna("ep1_d13_cerniera_da_sola")
            $ vc_pausa(False)
            s "I can do it myself."
            n "She reaches behind her back. Her fingers can't find the tab. She tries again. It goes up, crooked, in little jerks."
            n "Daniel watches her do it, without helping, without moving. Smiling, as if he were watching a clock that he knows will strike."
            da "Of course you can."
            da "Next time, then."
            sp "There won't be a next time."
            sp "...He didn't even argue. Why didn't he argue?"
    return
