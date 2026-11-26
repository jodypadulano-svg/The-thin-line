## Giorno 21 · domenica (docs/narrative/giorni19-22-pianificazione-2026-11-24.md, «Domenica 21»).
## Josh è alla convention tutto il giorno. Mattina: Darius passa per Josh (solo amicizia).
## Pomeriggio: Joanie in salotto (Jacob, Daniel se c'è stato il pranzo del 18, Magnus) e
## il messaggio a Jacob scritto da Joanie col telefono di Sara. Sera: Josh torna, dirgli o
## tacergli di Jacob; Jacob scrive (o risponde). Nessuna visita di Daniel.
## Decisioni di Jody del 26/11: registro, «Giorno 21».

default d21_testo_jacob = ""

label ep2_d21:
    call nuovo_giorno(21, "Lowercase")
    $ fascia_corrente = FASCE.index("mattina")
    call ep2_d21_mattina
    call ep2_d21_darius
    $ fascia_corrente = FASCE.index("pranzo")
    call ep2_d21_joanie
    $ fascia_corrente = FASCE.index("sera")
    call ep2_d21_josh
    call ep2_d21_jacob
    $ fascia_corrente = FASCE.index("notte")
    call ep2_d21_notte
    $ musica(None)
    $ luogo_corrente = ""
    scene bg nero with fade
    return


## --- Mattina: la casa vuota ------------------------------------------------------------------

label ep2_d21_mattina:
    $ vai("casa", "Home — Sunday, 9:10 a.m.")
    $ musica("casa")
    $ cg("The kitchen table in morning light: a note in Josh's handwriting propped against the sugar bowl, a single croissant crumb, Sara's coffee", "images/cg/ep2/d21_a1_biglietto.webp")
    n "[nome_compagno] left at six, with the shield under his arm and his good trousers on. She heard the door. She pretended not to, so that he could feel he'd been quiet."
    n "On the table, against the sugar bowl: {i}Judging from 10. Back for dinner. Don't let the flat get lonely. x{/i}"
    n "He'd asked her to come. Twice, and once more on the stairs last night. She'd said no, nicely. A whole day of other people's dragons."
    if fatto("ep2_d20_serata_romantica"):
        sp "He was still smiling when the alarm went. I could hear it in the dark."
    else:
        sp "A whole Sunday. Nobody needs me for anything."
    $ via_cg()
    return


## --- Mattina: Darius passa per Josh (solo amicizia, Jody 26/11) ------------------------------
## Non è un appuntamento cercato da Sara. Nessuna seduzione, nessun opt-in del percorso:
## una scelta neutra sul tono. Darius non tradisce la confidenza di Josh del 16 (I18).

label ep2_d21_darius:
    $ vai("casa", "Home — 10:30 a.m.")
    $ suono("citofono")
    $ cg("Darius at the open front door with a paper bag of croissants, realising, one hand on the back of his neck", "images/cg/ep2/d21_a2_darius_porta.webp")
    n "The intercom goes the way only Darius makes it go: two short, one long, as if it were a password."
    n "He's on the landing with a paper bag going transparent at the corners."
    dr "Morning. I brought the good ones. Is he up?"
    s "He's been up since five, Darius. He's at the convention."
    n "She watches it arrive. It takes a second."
    dr "The convention. It's today. He told me about it eleven times. He made me look at the shield."
    dr "I'm an idiot. Right. I'll leave these with you and go and be an idiot somewhere else."
    if fatto("ep2_d16_minuto_darius"):
        n "He holds out the bag. Over the top of it he says, as if it were the same sentence:"
        dr "Did the minute get her anywhere? The woman at the door."
    menu:
        sp "It's Darius. He's been coming up those stairs since the day we moved in, with the other end of the sofa."
        "Make him a coffee and talk about the book.":
            $ segna("ep2_d21_darius_caffe")
            $ interest("amico", 1, "Sara kept him for a coffee.")
            $ via_cg()
            $ cg("Sara and Darius at the kitchen table with coffee and croissants, Sara talking with her hands, Darius listening, amused", "images/cg/ep2/d21_a3_darius_cucina.webp")
            s "Come in. You can't eat six croissants on the stairs."
            dr "I could. I've done it."
            n "She tells him about the house with the narrow stairs, and the chair by the window, and the man who wouldn't say whether it was good."
            if fatto("ep2_d20_magnus_ascolta"):
                s "He said I'd written forty-nine pages about a window. And one about a hand on the latch."
            else:
                s "He said a third of it's me apologising. He counted."
            dr "That sounds like a yes from somebody who doesn't do yeses."
            s "That's what Joanie said. With more screaming."
            n "He gets crumbs on the table and sweeps them into his palm without being asked, the way he did on moving day, when there was nothing in the flat but boxes and the three of them."
            dr "He's proud of you, you know. Josh. He won't say it right, but he is."
            s "I know. He wrote topics on his hand."
            dr "He did that before his driving test."
        "Send him on to the convention.":
            $ via_cg()
            $ cg("Darius halfway down the stairs, turning to wave with a croissant in his mouth; Sara laughing in the doorway", "images/cg/ep2/d21_a3_darius_scale.webp")
            s "Go and find him. He'll want someone to show the shield to who isn't a dragon."
            dr "You're right. He'd never forgive me. I'd never forgive me."
            n "He takes one croissant for the road and leaves her the bag. Halfway down he turns and waves with it in his mouth."
            if fatto("ep2_d16_minuto_darius"):
                s "Almost a whole page, Darius!"
                n "He gives her a thumbs up without turning round."
    n "When he's gone, the flat is quiet in a different way. It's still warm where he stood."
    $ via_cg()
    return


## --- Pomeriggio: Joanie in salotto -----------------------------------------------------------
## Tre argomenti, tre scelte (Jody 26/11): Jacob, Daniel solo col pranzo del 18, Magnus senza
## scelta. Joanie fa il tifo per Jacob e trova interessante anche Daniel, ricco e potente.
## Poi la svolta: Joanie scrive a Jacob dal telefono di Sara. Joanie non svela nulla di sé:
## l'attrazione per Sara e la «casa delle bambole» restano alla tappa 5.

label ep2_d21_joanie:
    $ vai("casa", "Home — 3 p.m.")
    $ musica("casa")
    $ cg("Joanie on the doorstep in sunglasses with a box of pastries and a bottle of wine, Sara in socks letting her in", "images/cg/ep2/d21_b1_joanie_arriva.webp")
    ch "He's out all day, isn't he. I can smell it. The flat smells of nobody's dragons."
    s "It's three in the afternoon, Jo."
    ch "Which is why it's only one bottle."
    n "She kicks her shoes off in the hall the way she always has, as if it were her flat too, and gets on the sofa feet first."
    $ via_cg()
    $ cg("Sara and Joanie on the sofa, legs tucked under them, pastries between them; Joanie holding up a long supermarket receipt with a list written on the back", "images/cg/ep2/d21_b2_divano.webp")
    n "Out of her bag comes a supermarket receipt. On the back, in eyeliner, there's a list."
    ch "I've done an agenda. Like your boyfriend's hand."
    s "How do you know about his hand?"
    ch "You sent me a photo at eleven last night and said «I love him» and then «don't answer this»."
    $ interest("amica", 1, "Sara let Joanie in for the afternoon.")

    ## 1. Jacob
    if fatto("ep2_d20_da_joanie"):
        ch "Item one. Coffee man. Part two. Yesterday we only got as far as the hands."
    else:
        ch "Item one. Coffee man. You've been very quiet about coffee man, which is how I know."
    ch "Has he written?"
    s "No. Why would he?"
    ch "Because he looked at you on Friday like a man reading his own handwriting."
    if fatto("ep2_d19_ballo_jacob"):
        n "Joanie doesn't mention the dance. She doesn't have to. It's sitting on the sofa with them, with its shoes off."
    menu:
        sp "She's leaning in. She's already decided what I'm going to say."
        "«He was... good. Seeing him.»":
            $ segna("ep2_d21_jacob_aperta")
            $ interest("ex", 1, "Sara talked about Jacob, and liked it.")
            $ corruption(1, "Sara said it out loud: it was good to see him.")
            $ via_cg()
            $ cg("Sara hugging a cushion and talking, half laughing at herself; Joanie with her chin on her fists, rapt", "images/cg/ep2/d21_b3_jacob_racconta.webp")
            s "He was good. Seeing him. I don't know what I expected. Somebody smaller."
            ch "Nobody's ever expected Jacob to be smaller."
            if fatto("ep2_d19_detto_tradimento"):
                s "I told him he cheated on me. To his face. And he just... said yes. Like it was the weather."
                ch "And?"
                s "And it was quite nice, being the one who said it."
            else:
                s "He remembered what I drink. Four years, and he ordered it before I'd sat down."
            n "Joanie hugs her knees. She looks like somebody being told the end of a film she's already seen and loved."
            ch "I knew it. I {i}knew{/i} it. You've gone pink."
        "«It was a drink, Jo. That's all.»":
            $ segna("ep2_d21_jacob_chiusa")
            $ confidence(1, "Sara kept Jacob to herself.")
            s "It was a drink, Jo. That's all. He's still very tall. The end."
            ch "«The end.» You've never said «the end» about anything in your life. You re-read endings."
            n "Sara takes a pastry so that her mouth's busy. Joanie watches her eat it as if it were evidence."

    ## 2. Daniel, solo se il pranzo del 18 c'è stato
    if fatto("ep2_d18_pranzo_daniel"):
        ch "Item two. Friday. You were in the middle of Daniel and then a giant walked in. Finish."
        n "So Sara finishes. The restaurant, the way he ordered for both of them without looking at the menu, the editor he knows by his first name."
        ch "Rich. Powerful. Knows everyone. Looks at you like you're the only thing in the room that's worth what it costs."
        ch "I'm only saying. If I were a girl with a book to sell."
        menu:
            sp "She's half joking. She's the half that isn't."
            "«All right. He's a bit much. I liked it.»":
                $ segna("ep2_d21_daniel_ammesso")
                $ interest("daniel", 1, "Sara admitted she liked how much he was.")
                $ corruption(1, "Sara admitted it, to Joanie and to herself.")
                $ via_cg()
                $ cg("Joanie fanning herself theatrically with the receipt, Sara with her face in a cushion, laughing", "images/cg/ep2/d21_b4_daniel.webp")
                s "All right. He's a bit much. I liked it. There, I said it, it's out, I can't put it back."
                ch "You don't have to put it back. Leave it out. Let it breathe."
                n "Joanie fans herself with the receipt. Item two smudges."
                ch "I'm still team giant. But I'm open to a merger."
            "«It was lunch. He talked about books.»":
                s "It was lunch, Jo. He talked about books. He's my boyfriend's boss."
                ch "Mm. And Henry the Eighth was a man who liked weddings."
        call ep2_d21_colpa
    elif fatto("ep2_d18_pranzo_annullato"):
        n "Item two on the receipt has been crossed out. Sara never told her about the lunch she cancelled. Joanie's crossed it out anyway, as if she'd smelt it."

    ## 3. Magnus, una battuta e nessuna scelta
    if fatto("ep2_d20_da_joanie"):
        ch "Item three, Magnus, done yesterday, I'm still shaking. Has he rung?"
    else:
        ch "Item three. The publisher. Your text said «HE DIDN'T SAY YES» in capitals, which I've decided is the most promising thing anyone's ever said."
        ch "Has he rung?"
    s "Not yet. He said he'd let me know."
    ch "Men who say they'll let you know are either very rude or very sure. He's seventy-one. He's sure."
    $ via_cg()
    call ep2_d21_messaggio
    $ via_cg()
    return


## --- Daniel che sfotte Josh: la confessione e l'offerta di Joanie (Jody 26/11) ----------------
## Solo col pranzo del 18; segue la scelta su Daniel. Con ep2_d18_sfotto_josh Sara confessa di
## averlo sfottuto anche lei per eccitare Daniel; altrimenti che le fa effetto quando lo fa lui.
## «Not much.» → nessun effetto · «Yes. And I feel guilty...» → Daniel +1, Corr +1, poi l'offerta.
## Lasciar parlare Joanie con Josh (acceleratore) → Joanie +2, Corr +1, flag ep2_d21_joanie_parla_josh:
## apre il ramo possibile di Josh complice (registro, 26/11). Non lasciarla → Conf +1.
## Joanie non svela nulla di sé (attrazione per Sara e «casa delle bambole» restano alla tappa 5).

label ep2_d21_colpa:
    n "Joanie's waiting. She can always tell when there's a bit Sara has left out."
    if fatto("ep2_d18_sfotto_josh"):
        s "There's something else. At lunch, he was making fun of [nome_compagno]. The photocopier, all that."
        s "And I joined in. On purpose. Because I could see what it did to him. To Daniel."
        n "She says it to the pastry box. Joanie puts her coffee down very slowly, as if it might go off."
        ch "You teased your boyfriend. To turn his boss on."
        s "When you say it like that."
        ch "I'm saying it exactly like that. Did you like it?"
    else:
        s "There's something else. At lunch, he made fun of [nome_compagno]. Not nastily. Lightly. Like a man flicking a crumb off his sleeve."
        s "And it did something to me. Watching him do it. I didn't join in. I just... felt it."
        ch "Felt what, exactly?"
        s "Jo."
        ch "Did you like it?"
    menu:
        sp "She isn't laughing. That's how I know she really wants the answer."
        "«Not much.»":
            $ segna("ep2_d21_colpa_poco")
            s "Not much. It was a strange moment, that's all. It's gone."
            ch "Okay. Strange moments are allowed. Next item."
        "«Yes. And I feel guilty about him.»":
            $ segna("ep2_d21_colpa_si")
            $ interest("daniel", 1, "Sara admitted what Daniel's game did to her.")
            $ corruption(1, "Sara admitted she liked it.")
            s "Yes. I liked it. And I feel horrible about him. He wrote topics on his hand for me, Jo."
            $ via_cg()
            $ cg("Joanie holding both of Sara's hands across the pastry box, suddenly serious, Sara biting her lip", "images/cg/ep2/d21_b4b_offerta.webp")
            n "Joanie takes both her hands across the pastry box. It's the voice she uses about three times a year."
            ch "Listen to me. If you give me the chance, I'll take every bit of that guilt away."
            ch "But you'd have to let me talk to [nome_compagno]. On my own. And you'd have to trust me."
            s "Talk to him about what?"
            ch "About him. Not about you. I promise you that."
            if sara_bad_girl:
                n "She doesn't wink. For once she doesn't. That's what makes Sara's stomach turn over."
            menu:
                sp "Joanie and [nome_compagno]. On their own. I don't know what she'd say. I don't know what he'd say back."
                "Let Joanie talk to him." (acceleratore=True):
                    $ segna("ep2_d21_joanie_parla_josh")
                    $ interest("amica", 2, "Sara trusted her with Josh.")
                    $ corruption(1, "Sara let Joanie talk to Josh.")
                    s "...Okay. Talk to him. But Jo. Be kind."
                    ch "I'm always kind. I'm just kind in unexpected directions."
                    n "She squeezes Sara's hands once, hard, and lets go, and is herself again, reaching for an almond croissant as if nothing has been decided."
                    sp "Something's been decided."
                "«No, Jo. Not him.»":
                    $ segna("ep2_d21_joanie_fermata")
                    $ confidence(1, "Sara kept Josh out of it.")
                    s "No, Jo. Not him. Whatever this is, it's mine to deal with."
                    ch "Fair. The offer doesn't expire. Like a really good coupon."
                    n "That's the rule. If Sara doesn't want to, Joanie doesn't mind. She means it. She also, Sara notices, doesn't say she'll forget it."
    return


## --- La svolta: il messaggio a Jacob (Jody 26/11) --------------------------------------------
## Joanie prende il telefono e scrive a Jacob in minuscolo, «così sa che sei tu».
## Inviarlo → Jacob +1, Corr +1, e la sera Jacob risponde. Cancellarlo → nessun effetto,
## e la sera Jacob scrive per primo come previsto.

label ep2_d21_messaggio:
    $ cg("Joanie holding Sara's phone high out of reach, typing with her thumb; Sara sprawled across her, reaching for it and laughing", "images/cg/ep2/d21_b5_telefono.webp")
    n "Sara's phone is on the cushion between them. Joanie picks it up as if it were hers."
    ch "Item four. Not on the list. You're not going to write to him. So I am."
    s "Jo. Joanie. Give it back."
    if not ha_numero("ex"):
        n "Sara didn't give him her number. She hasn't got his. Joanie types it in from memory, without looking."
        s "Why have you got his number?"
        ch "I've got everybody's number. It's a public service."
        $ da_numero("ex")
    n "She holds it up out of reach and types with one thumb, and reads it out in a deep voice, like a newsreader."
    if fatto("ep2_d19_ballo_jacob"):
        $ d21_testo_jacob = "do you still dance like that or was it a one off"
    else:
        $ d21_testo_jacob = "sunday. bored. your fault"
    ch "«[d21_testo_jacob]». Lowercase. He'll know it's you."
    s "I don't write in lowercase!"
    ch "He does. That's the point. It's flirting. It's like wearing his jacket."
    if sara_bad_girl:
        n "She stops with her thumb over the arrow, looks at Sara over the top of the phone, and closes one eye. Slowly."
    else:
        n "She stops with her thumb over the arrow and looks at Sara over the top of the phone. She isn't joking any more. She's waiting."
    menu:
        sp "I could take it off her. She'd let me. That's the worst part: she'd let me."
        "Let her send it.":
            $ segna("ep2_d21_messaggio_inviato")
            $ interest("ex", 1, "Sara let the message go.")
            $ corruption(1, "Sara let Joanie press send, and didn't stop her.")
            $ chat_aperta = "ex"
            show screen telefono_chat("ex")
            $ msg("sara", d21_testo_jacob, premia_avvio=False)
            hide screen telefono_chat
            $ chat_aperta = None
            $ via_cg()
            $ cg("The phone face-up on the coffee table between two pastries, both women staring at it, Joanie's hand over her mouth", "images/cg/ep2/d21_b6_inviato.webp")
            n "Sara doesn't take it off her. She doesn't say «don't». She watches Joanie's thumb come down as if it were happening to somebody in a book."
            n "{i}Delivered.{/i} They both stare at it. It doesn't turn into {i}Read{/i}."
            ch "He'll see it tonight. Men like that don't look at their phones in daylight."
            sp "My heart's going. Over lowercase."
        "Take the phone back and delete it.":
            $ segna("ep2_d21_messaggio_cancellato")
            $ via_cg()
            $ cg("Sara holding her phone against her chest, triumphant and a bit breathless; Joanie pouting at the ceiling", "images/cg/ep2/d21_b6_cancellato.webp")
            n "Sara climbs over her, gets a knee in the pastries, and takes it. She deletes it one letter at a time, so that Joanie can watch."
            ch "Coward."
            s "Friend."
            ch "Same thing, on a Sunday."
            n "Joanie lies back with her feet in Sara's lap and doesn't seem cross at all. That's the rule. If Sara doesn't want to, Joanie doesn't mind. It's never been any other way."
    return


## --- Sera: Josh torna. Dirgli o tacergli di Jacob (Jody 24/11 e 26/11) ----------------------
## Dirlo → Josh +1, Conf +1, flag ep2_d21_detto_josh. Tacere → Corr +1, flag ep2_d21_taciuto_josh.
## Josh ha confidato la sua ansia su Jacob a Darius il 16 (I18): si irrigidisce, poi ringrazia.

label ep2_d21_josh:
    $ vai("casa", "Home — 8:20 p.m.")
    $ musica("casa")
    $ cg("Josh in the doorway, exhausted and glowing, the cardboard shield under one arm and a paper rosette pinned crookedly to his chest", "images/cg/ep2/d21_c1_josh_torna.webp")
    n "He comes in backwards, because of the shield, and turns round with a paper rosette pinned to his chest. It says {i}JUDGE{/i}."
    c "Nobody cried. Well. One man cried, but it was a good cry. I gave his gryphon a commendation."
    s "You gave out commendations?"
    c "I made them up on the spot. I'm very powerful on a Sunday."
    if fatto("ep2_d21_darius_caffe"):
        c "Darius turned up at the hall at twelve with half a croissant. He said you'd fed him."
        s "He came for you. He forgot."
        c "He always forgets. He always comes anyway."
    else:
        c "Darius turned up at the hall at twelve with half a croissant. He looked at every single shield. He even did the voices."
    $ via_cg()
    $ cg("Sara and Josh on the sofa with noodles out of cartons, his feet on the coffee table, her legs over his", "images/cg/ep2/d21_c2_divano.webp")
    n "They eat noodles out of the cartons with their legs on top of each other. He tells her about the gryphon. She can feel the day going out of him, like heat out of a stone."
    sp "Friday. The Lantern. I said I'd tell him, and there's nothing to tell."
    sp "There's nothing to tell. That's why it ought to be easy."
    menu:
        sp "He's happy. He's got sauce on his rosette."
        "Tell him about Jacob.":
            $ segna("ep2_d21_detto_josh")
            $ interest("josh", 1, "Sara told him herself.")
            $ confidence(1, "Sara said it before it could become a secret.")
            $ via_cg()
            $ cg("Josh gone very still with his chopsticks in mid-air; Sara's hand resting on his knee", "images/cg/ep2/d21_c3_detto.webp")
            s "On Friday, at The Lantern. With Joanie. Jacob was there. Jacob Trevor."
            n "He doesn't move. The noodles stay in the air on the end of the chopsticks. For a second he isn't in the room at all; he's somewhere she can't see."
            c "Jacob. Right."
            c "Was it... How was that?"
            if fatto("ep2_d19_difende_josh"):
                s "He asked who was at home. I said you. Before he'd finished asking."
                n "Something in his shoulders comes down an inch."
            else:
                s "Strange. Short. He's still enormous."
            c "Thanks for telling me. You didn't have to."
            s "I did, though."
            n "He puts the noodles down and kisses her on the temple, quite hard, as if he were putting a stamp on something."
        "Keep it to herself.":
            $ segna("ep2_d21_taciuto_josh")
            $ corruption(1, "Sara kept Friday to herself.")
            n "She opens her mouth, and he says «and then the gryphon man hugged me», and the moment goes past like a stop she meant to get off at."
            sp "Tomorrow. Or not. It doesn't matter. Nothing happened."
            n "She notices she's said «nothing happened» twice now, to nobody."
    $ via_cg()
    return


## --- Sera: Jacob scrive (mese-1, «21 Dom · Sera») --------------------------------------------
## ★ Rispondere? Sì → Jacob +2, Susp +2 · Ignorarlo → nessun effetto.
## Se Sara ha taciuto a Josh e risponde, in più Susp +1 (Jody 26/11).
## Se il messaggio del pomeriggio è partito, Jacob risponde a quello; altrimenti scrive per primo.

label ep2_d21_jacob:
    $ vai("casa", "Home — 10:40 p.m.")
    $ musica("notte")
    $ suono("telefono_vibra")
    $ cg("The phone lit up on the sofa cushion between Sara and Josh, who is half asleep against her, the TV on low", "images/cg/ep2/d21_c4_telefono.webp")
    n "The phone goes on the cushion between them. [nome_compagno] has his head on her shoulder and the remote on his chest, and the film's watching itself."
    if not ha_numero("ex"):
        $ da_numero("ex")
    $ chat_aperta = "ex"
    show screen telefono_chat("ex")
    if fatto("ep2_d21_messaggio_inviato"):
        $ msg("ex", "only for special occasions")
        $ msg("ex", "and tell joanie lowercase doesn't suit her")
        hide screen telefono_chat
        $ chat_aperta = None
        sp "He knew. Of course he knew. He knew it was her and he answered me anyway."
    else:
        if fatto("ep2_d19_numero_dato"):
            $ msg("ex", "you didn't put a surname")
            $ msg("ex", "i'd have known anyway")
        else:
            $ msg("ex", "it's jacob. a little bird gave me this")
            $ msg("ex", "don't be cross with the bird")
        if fatto("ep2_d19_jacob_risata"):
            $ msg("ex", "you laughed on friday. i'd forgotten what that sounded like")
        else:
            $ msg("ex", "it was good to see you sara. that's all. that's the message")
        hide screen telefono_chat
        $ chat_aperta = None
        sp "Ten forty on a Sunday. He always did write at night."
    menu:
        sp "[nome_compagno]'s breathing slow against my shoulder. He isn't quite asleep."
        "Answer him.":
            $ segna("ep2_d21_risposto_jacob")
            $ interest("ex", 2, "Sara answered him.")
            $ suspicion(2)
            $ via_cg()
            $ cg("Sara typing with the screen tilted away, Josh's eyes open now, looking at the light on her face", "images/cg/ep2/d21_c5_risponde.webp")
            $ chat_aperta = "ex"
            show screen telefono_chat("ex")
            if fatto("ep2_d21_messaggio_inviato"):
                $ msg("sara", "It WAS a one off. I'll tell her.", premia_avvio=False)
                $ msg("ex", "capitals. there she is")
            else:
                $ msg("sara", "It was nice to see you too.", premia_avvio=False)
                $ msg("ex", "«too». i'll take it")
            hide screen telefono_chat
            $ chat_aperta = None
            n "She types it with the screen tipped away from him. It's only manners. It's only four words."
            c "...Who's that?"
            if fatto("ep2_d21_detto_josh"):
                s "Joanie. Being Joanie."
                n "He nods into her shoulder. The lie's so small it hardly needs saying, and she says it anyway, and hears it."
            else:
                $ suspicion(1)
                s "Joanie. Being Joanie."
                n "He doesn't ask anything else. He just lifts his head off her shoulder, and doesn't put it back."
            call ep2_d21_jacob_invito
        "Turn the phone over.":
            $ segna("ep2_d21_ignorato_jacob")
            n "She turns the phone face down on the cushion. The light goes out through the fabric, like a held breath."
            n "[nome_compagno] makes a small sound and settles further into her. He didn't see a thing. There wasn't a thing."
    $ via_cg()
    return


## --- Sera: Jacob la invita per mercoledì (giorni 22-24 e mercoledì di Josh, Jody 26/11) ------
## Solo se Sara gli ha risposto. Nessun punteggio: contano le scelte della serata del 24.
## Sì → flag ep2_d21_jacob_mercoledi (l'appuntamento del 24 è con lui) · No → ep2_d21_jacob_rifiutato.

label ep2_d21_jacob_invito:
    $ suono("telefono_vibra")
    $ via_cg()
    $ cg("Sara on the sofa looking down at her lit phone, Josh half asleep against her shoulder, the TV on low", "images/cg/ep2/d21_c6_invito.webp")
    $ chat_aperta = "ex"
    show screen telefono_chat("ex")
    $ msg("ex", "wednesday. one drink. same bar.")
    hide screen telefono_chat
    $ chat_aperta = None
    sp "Wednesday. [nome_compagno]'s dragons. He doesn't even know, and he picked the one night."
    menu:
        sp "One drink. He always said one drink."
        "Say yes.":
            $ segna("ep2_d21_jacob_mercoledi")
            $ chat_aperta = "ex"
            show screen telefono_chat("ex")
            $ msg("sara", "One drink.", premia_avvio=False)
            $ msg("ex", "one. i'll count")
            hide screen telefono_chat
            $ chat_aperta = None
            n "She puts the phone face down on her knee. Her heart is going as if she'd run up the stairs."
        "Not this week.":
            $ segna("ep2_d21_jacob_rifiutato")
            $ chat_aperta = "ex"
            show screen telefono_chat("ex")
            $ msg("sara", "Not this week.", premia_avvio=False)
            $ msg("ex", "this week. noted")
            hide screen telefono_chat
            $ chat_aperta = None
            n "He's read it before she's even put the phone down. «This week.» As if there were others."
    return

## --- Notte: la chat (mese-1) e il telefono ---------------------------------------------------
## Lasciarla → nessun effetto · Cancellarla → Corr +1, Susp -1.

label ep2_d21_notte:
    $ vai("casa", "Home — Sunday night")
    $ cg("Sara sitting on the edge of the bath in Josh's T-shirt, the phone in both hands, Jacob's chat open", "images/cg/ep2/d21_d1_bagno.webp")
    n "[nome_compagno] goes to bed with the rosette still on. She says she'll be one minute, and sits on the edge of the bath with the door locked, which she never does."
    n "Jacob's name sits at the top of the list, above [nome_compagno]'s, above Joanie's."
    menu:
        sp "If he picked it up. If he just picked it up to check the time."
        "Leave the chat where it is.":
            $ segna("ep2_d21_chat_tenuta")
            n "She leaves it. There's nothing in it. Deleting it would mean there was something in it."
        "Delete the chat.":
            $ segna("ep2_d21_chat_cancellata")
            $ corruption(1, "Sara deleted the chat: something worth hiding.")
            $ suspicion(-1)
            $ chat_log["ex"] = []
            n "She deletes it. It asks her if she's sure. She is, which is the part she'll think about later."
            n "The number stays. She doesn't delete the number."
    $ via_cg()
    $ cg("The bedroom in the dark, Josh asleep with the paper rosette on his chest, Sara at the window with her phone", "images/cg/ep2/d21_d2_finestra.webp")
    call telefono_minuti_sessione(23 * 60, 23 * 60 + 30, "Go to bed")
    if fatto("ep2_d21_detto_josh"):
        sp "I told him. I told him, and he kissed me. That's what's meant to happen."
    else:
        sp "Nothing happened. I'll stop saying it soon."
    n "She takes the rosette off his chest so it won't crease, and puts it on the bedside table, where he'll see it first thing."
    $ via_cg()
    return
