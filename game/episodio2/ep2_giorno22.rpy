## Giorno 22 · lunedì (docs/narrative/giorni22-24-pianificazione-2026-11-26.md, «Lunedì 22»).
## Redazione: Barbara commenta come è vestita Sara (scelta per domani) e le propone la lettera
## anonima sulla morte di Nadia Reyes. Se Sara accetta, in pausa pranzo incontra Dawn al fiume:
## primo indizio, la targa a metà. Una estrazione di convocazione. Dopo il lavoro, eventuale
## faccenda da Howard. Sera: Josh umiliato da Daniel (spostato dal 24): il motivo per cui
## mercoledì andrà a giocare da Mark.
## Decisioni di Jody del 26/11: registro, «Giorno 22».

## Dawn non è un percorso (regole di lavoro, punto 6): personaggio funzionale dell'inchiesta.
## «Dawn» è il nome che dà a Sara; il resto si conquista con la fiducia, più avanti.
define dawn = Character("Dawn", color="#a3b8d9")

label ep2_d22:
    call nuovo_giorno(22, "Four Lines")
    $ fascia_corrente = FASCE.index("lavoro")
    call ep2_d22_abiti
    call ep2_d22_lettera
    call barbara_convocazione
    if fatto("ep2_d22_inchiesta_accettata"):
        $ fascia_corrente = FASCE.index("pranzo")
        call ep2_d22_dawn
    $ fascia_corrente = FASCE.index("sera")
    call howard_faccende_dopo_lavoro(True, True, False)
    call ep2_d22_josh
    $ fascia_corrente = FASCE.index("notte")
    call ep2_d22_notte
    $ musica(None)
    $ luogo_corrente = ""
    scene bg nero with fade
    return


## --- Mattina: Barbara commenta come è vestita Sara (mese-1, «22 Lun · Lavoro») ---------------
## Il giorno dopo: come sempre → nessun effetto · una scollatura in più → Barbara +1, Corr +1.

label ep2_d22_abiti:
    $ vai("redazione", "The newsroom — Monday, 9:05 a.m.")
    $ musica("redazione")
    $ ambiente("redazione")
    $ cg("Barbara stopping beside Sara's desk with a coffee, looking her up and down over her glasses; Sara in a buttoned cardigan", "images/cg/ep2/d22_a1_barbara_scrivania.webp")
    n "Barbara stops at her desk on the way to the meeting, the way she stops at the window to look at the weather."
    ba "Cardigan. Buttoned. On a Monday."
    s "It's cold in here."
    ba "It's cold everywhere, Sara. That's what other people are for."
    n "She looks for another second, over her glasses. Not at the cardigan. At what Sara has decided to hide under it."
    ba "You dress like someone who's apologising for arriving. One day you'll stop. I'd like to be here for it."
    menu:
        sp "She says it as if it were already true. As if I'd agreed."
        "Dress as usual tomorrow.":
            $ segna("ep2_d22_abito_solito")
            sp "I'll dress like myself. It's the only person I know how to dress."
        "A little more neckline tomorrow.":
            $ segna("ep2_d22_scollatura_domani")
            $ interest("capa", 1, "Sara took Barbara at her word.")
            $ corruption(1, "Sara decided what she'll show tomorrow.")
            sp "Tomorrow. One button. Just to see who notices first."
            n "She catches herself already choosing the blouse. The white one. The one that's never been quite right with a cardigan."
    $ via_cg()
    return


## --- Lavoro: la lettera anonima (inchiesta-giorno22, 25-26/11) -------------------------------
## Barbara propone, non impone. Accettare → flag ep2_d22_inchiesta_accettata (si apre il filone).
## Rifiutare → flag ep2_d22_inchiesta_rifiutata: nessun incontro, nessuna penalità.
## La mittente è Dawn, ma la redazione non lo sa. Sul retro: luogo e ora (Jody, 26/11).

label ep2_d22_lettera:
    $ vai("redazione", "Barbara's office — 10:30 a.m.")
    $ musica("barbara")
    $ cg("Barbara at her desk sliding a handwritten letter across to Sara; the envelope beside it, torn along the top", "images/cg/ep2/d22_a2_lettera.webp")
    n "Barbara doesn't sit behind the desk. She sits on the corner of it, and puts a letter down in front of Sara with two fingers, the way you'd put down a card you aren't sure you want to play."
    ba "It came on Saturday. No stamp. Somebody pushed it through the door by hand."
    n "Blue biro, pressed so hard it's come through the paper. Capital letters, as if the writer didn't trust her own handwriting."
    n "{i}HER NAME WAS NADIA REYES. THE PAPERS GAVE HER FOUR LINES AND NO NAME. THE POLICE CLOSED IT IN A WEEK.{/i}"
    n "{i}SHE WAS FRIGHTENED FOR TWO WEEKS BEFORE. SHE WOULDN'T SAY OF WHAT. SHE WAS NEVER FRIGHTENED OF ANYTHING.{/i}"
    n "{i}NOBODY WILL ASK BECAUSE OF WHAT SHE DID FOR A LIVING. I'M ASKING.{/i}"
    ba "We ran it. Page nineteen, under the weather. «Woman, 26, found dead.» Four lines. Whoever wrote this can count."
    s "Why are you showing me?"
    ba "Because I can't send anyone with a byline. Their faces are on the website. Anyone who wanted to know who was asking would know by lunch."
    ba "You, nobody's looked at yet. Not properly. That's not an insult. In this job, for a little while, it's the most useful thing you've got."
    ba "Find out if there's anything in it. If there isn't, we've lost a morning. If there is..."
    n "She doesn't finish. She takes her glasses off and looks at Sara without them, which she almost never does."
    ba "I'm not giving you this, Sara. I'm offering it. You can say no and go back to the horoscopes, and I'll think exactly the same of you on Tuesday."
    menu:
        sp "Four lines. Somebody was frightened for two weeks, and the paper gave her four lines."
        "«I'll look into it.»":
            $ segna("ep2_d22_inchiesta_accettata")
            $ via_cg()
            $ cg("Close on the back of the letter in Sara's hands: a short line of capitals at the bottom, a time and a place", "images/cg/ep2/d22_a3_retro.webp")
            s "I'll look into it."
            ba "Good. Quietly. You report to me, and only to me."
            n "Sara turns the letter over to give it back. On the back, small, at the very bottom, as if added after the envelope was already sealed and then opened again:"
            n "{i}IF YOU BELIEVE ME. MONDAY, ONE O'CLOCK. THE RIVER, THIRD BENCH PAST THE BOATHOUSE. COME ALONE. NO CAMERA.{/i}"
            s "Barbara. It's today."
            ba "Then you'd better eat a big breakfast tomorrow. You won't have lunch today."
            sp "She saw it. She saw it on Saturday, and she waited for me to turn it over."
        "«I don't think I'm the right person.»":
            $ segna("ep2_d22_inchiesta_rifiutata")
            s "I don't think I'm the right person. I write about the bakery competition, Barbara."
            ba "You write about it very well. That's half of why I asked."
            n "She takes the letter back without any fuss, folds it along its old fold and puts it in the top drawer, on its own."
            ba "It'll be here. Letters like that don't go off."
            sp "Four lines. I'll stop thinking about it by lunch."
            n "She doesn't, quite."
    $ via_cg()
    return


## --- Pausa pranzo: Dawn al fiume (decisioni del 26/11) ---------------------------------------
## Solo con l'inchiesta accettata. Dawn ha paura di fare la fine di Nadia: da qui tutta la
## prudenza. Primo indizio in entrambi i rami: mezza targa su uno scontrino (ep2_d22_targa).
## Empatico → ep2_d22_dawn_fiducia (racconta di più su Nadia) · Fatti → ep2_d22_dawn_fatti.
## Nessun effetto sulle statistiche (nessuno approvato). Non anticipare la soluzione.

label ep2_d22_dawn:
    $ vai("fiume", "The river path — 12:55 p.m.")
    $ ambiente(None)
    $ musica("stranezza")
    $ cg("The river path at midday, a row of benches past an old boathouse; Sara alone on the third bench with her coat buttoned, looking around", "images/cg/ep2/d22_b1_panchina.webp")
    n "Third bench past the boathouse. There's a man feeding ducks out of a bread bag and a jogger who goes past twice. Sara sits with her hands in her pockets and feels watched by both of them."
    n "One o'clock. Five past. Ten past."
    sp "She isn't coming. Or she came, and looked at me, and decided."
    $ via_cg()
    $ cg("A woman in a hooded rain jacket and sunglasses sitting down at the far end of the bench, not looking at Sara, a paper cup in her hands", "images/cg/ep2/d22_b2_dawn_arriva.webp")
    n "At a quarter past, a woman in a hooded rain jacket sits down at the other end of the bench, as far away as the bench allows. She doesn't look at Sara. She looks at the water."
    dawn "Don't turn round. You came out of the side door at twenty to one and you bought a sandwich you haven't eaten."
    s "...You followed me?"
    dawn "I watched the door for an hour. I watched who came out after you. Nobody did. So I'm sitting down."
    s "I'm Sara. I'm from the paper."
    dawn "I know where you're from. Call me Dawn. Don't write it down."
    n "Up close she's younger than her voice. Her nails are short and very neatly painted, a pale shell pink, and she keeps rubbing one with her thumb as if to make sure it's still there."
    s "Why all this? The bench, the hour, the door?"
    dawn "Because Nadia was careful too. Not like this. Not enough."
    dawn "She was frightened for two weeks and she laughed about it. And then she was in four lines on page nineteen."
    dawn "I'm not going to be four lines. So I watch doors."
    menu:
        sp "She's holding that cup so hard it's bending. She came anyway."
        "Ask about Nadia.":
            $ segna("ep2_d22_dawn_fiducia")
            $ via_cg()
            $ cg("Dawn turned a little towards Sara now, sunglasses pushed up, showing her own pink nails while she talks; Sara listening with her sandwich forgotten in her lap", "images/cg/ep2/d22_b3_nadia.webp")
            s "Tell me about her. Not the night. Her."
            n "Dawn looks at her for the first time. Properly. It lasts long enough that Sara thinks she's got it wrong."
            dawn "She did these. My nails. She did everybody's. She had a little case with forty colours and she'd do them on the stairs, in the car, anywhere."
            dawn "She was going to have a place. A beauty place, with her name over the door. She had the name picked. She'd show you on her phone how the sign would look."
            dawn "Every month she sent money home, to her little sister. Like rent. The sister thinks she worked in a hotel."
            s "Does she know? The sister?"
            dawn "She knows Nadia's dead. She doesn't know anything else, and I'm not the one who's going to tell her."
            n "She pushes the sunglasses back down. The pink nail goes round and round under her thumb."
            dawn "She laughed with her whole face. You'd have liked her. Everybody did. That's what nobody wrote."
            sp "Twenty-six. A case with forty colours. A sign she'd already designed."
        "Stick to the facts.":
            $ segna("ep2_d22_dawn_fatti")
            $ via_cg()
            $ cg("Dawn still facing the water, talking low and fast; Sara with a small notebook on her knee, pen still", "images/cg/ep2/d22_b3_fatti.webp")
            s "What do you know that the police don't?"
            dawn "Nothing. Everything. Depends what they wanted to know."
            dawn "Two weeks before, she came back from a night and she wouldn't talk. Nadia always talked. She said she'd seen something she shouldn't have. Then she laughed and said forget it, it's nothing, I'm being stupid."
            s "Seen what?"
            dawn "She didn't tell me. I think she was keeping me out of it. I think she thought that was being kind."
            n "Sara writes {i}two weeks{/i} and {i}saw something{/i}, and Dawn watches the pen as if it might go off."
            dawn "Put the pen away. Please."
            n "She puts the pen away."
    $ via_cg()
    $ cg("Close on Dawn's hand passing a creased supermarket receipt to Sara under the bench seat; half a car number plate written on the back in biro", "images/cg/ep2/d22_b4_scontrino.webp")
    dawn "The last night I saw her, a car picked her up at the corner. Dark. Big. Not one of ours, I know all of ours."
    dawn "She got in like it was normal. I didn't like it. I wrote down what I could before it turned."
    n "A supermarket receipt, folded small enough to hide in a palm. On the back, in biro, half a number plate. The rest is a smudge where the car went round the corner."
    $ segna("ep2_d22_targa")
    s "Did you give this to the police?"
    dawn "No."
    n "Just no. Not because she didn't think of it."
    if fatto("ep2_d22_dawn_fiducia"):
        dawn "If you find anything. Anything. Leave a letter for me where you found mine. In the paper's door, on a Saturday. Write «for the third bench»."
        s "And if I don't find anything?"
        dawn "Then you'll still have asked. That's one more than anyone else."
    else:
        dawn "Don't look for me. If I want to find you, I know the side door."
    $ via_cg()
    $ cg("The bench empty except for Sara, the paper cup left beside her, Dawn's hood far away down the river path between the trees", "images/cg/ep2/d22_b5_sola.webp")
    n "She gets up without saying goodbye and walks away the opposite way from the paper. She doesn't look back once. Sara is sure that's on purpose too."
    n "The cup is still on the bench. Sara drops it in the bin on the way back, and only on the stairs realises she's checked twice who's behind her."
    sp "Half a number plate. A case with forty colours. That's all I've got."
    sp "It's more than four lines."
    $ via_cg()
    return


## --- Sera: Josh torna umiliato da Daniel (spostato dal 24 al 22, Jody 25/11) ----------------
## Josh ha mandato la scheda del personaggio di D&D al posto del report: Daniel la legge alla
## riunione, «com'è andata coi draghi», tutto l'ufficio ride, Josh non risponde (F2). Alla fine
## la battuta su Sara, con un complimento vero per lei (D2). In entrambi i rami Sara capisce
## che Daniel lo fa per conquistare lei, e le fa effetto (Jody, 26/11).
## ★ Consolarlo (Josh 30) → Josh +3 · Irritarsi → Josh -3, Daniel +1, Corr +1.
## Da qui Josh accetta il D&D del mercoledì da Mark (flag ep2_d22_josh_dnd).

label ep2_d22_josh:
    $ vai("casa", "Home — 7:40 p.m.")
    $ ambiente(None)
    $ musica("casa")
    $ cg("Josh sitting on the edge of the sofa still in his work coat, bag at his feet, staring at the dark TV; Sara in the kitchen doorway", "images/cg/ep2/d22_c1_josh_divano.webp")
    n "He doesn't call out when he comes in. That's the first thing. [nome_compagno] always calls out, even when he knows she's in, as if the flat might have forgotten him."
    n "He's on the edge of the sofa with his coat on and his bag between his feet, looking at the television, which is off."
    s "Hey. You're home."
    c "Yeah."
    if fatto("ep2_d21_taciuto_josh") and fatto("ep2_d21_risposto_jacob"):
        sp "Last night he lifted his head off my shoulder and didn't put it back. Is this that? Did he see?"
    elif fatto("ep2_d22_inchiesta_accettata"):
        sp "I've been carrying a dead girl's name around all afternoon. I'd forgotten anybody else could have a bad day."
    $ via_cg()
    $ cg("Sara sitting beside Josh, his coat half off, him telling the story to his own hands", "images/cg/ep2/d22_c2_racconto.webp")
    n "It takes her ten minutes to get the coat off him and the story out of him, and it comes out in the wrong order, the way bad things do."
    c "The quarterly. I did it last night, after the convention. And I'd been doing Mark's thing as well, the character for Wednesday, he's starting a campaign. Same folder."
    c "I attached the wrong one. I sent Daniel a dwarf."
    s "...You sent him a dwarf."
    c "Brother Hollin Ashbeard. Cleric, level three. Two pages. With the backstory."
    n "He nearly laughs. It doesn't make it all the way out."
    c "He didn't say anything about it in the email. He waited for the Monday meeting. Twenty people. He had it printed."
    c "He read it out. All of it. He did a voice. He asked me «how was the dragon thing at the weekend, Josh» and everybody laughed, and then he read out my, my vow of the forge..."
    sp "And you sat there. I know you did. You laughed with them so it would look like a joke you were in on."
    c "I laughed. What was I supposed to do? It's Daniel."
    $ via_cg()
    $ cg("Josh with his face in his hands, Sara's hand on his back, looking past him at nothing, thoughtful", "images/cg/ep2/d22_c3_complimento.webp")
    c "And at the end, when everyone was getting up. He gave me the sheet back. In front of all of them."
    c "He said: «Barnett. I've met your Sara. The most beautiful woman in this city, and the brightest, I'd put money on it. She deserves a man who can tell a quarterly report from a dwarf.»"
    n "He says it in Daniel's voice without meaning to. It's a good imitation. That's the worst part."
    c "And they laughed at that too. And I said «yes, she does». I actually said it. «Yes, she does.»"
    n "Sara doesn't say anything for a moment, because the first thing she feels isn't for [nome_compagno]."
    sp "The most beautiful woman in this city. He said it to twenty people so that it would come home tonight in Josh's mouth."
    sp "It wasn't about the report. It was a letter. To me."
    if fatto("ep2_d18_sfotto_josh"):
        sp "And I laughed with him, on Thursday, about Josh. He remembers. That's why he's sure it'll work."
    elif fatto("ep2_d21_colpa_si"):
        sp "I told Joanie it makes me feel guilty. It does. It doesn't make it stop."
    n "She knows exactly what he's doing. Knowing doesn't make it stop either. There's a warmth under her ribs she didn't ask for, and it stays."
    menu:
        sp "[nome_compagno]'s shaking a little. He's waiting to hear what I think of him."
        "Comfort him." (josh=30):
            $ segna("ep2_d22_consola_josh")
            $ interest("josh", 3, "Sara stayed on his side.")
            $ via_cg()
            $ cg("Sara holding Josh's head against her shoulder on the sofa, his arms round her waist, the character sheet crumpled on the floor", "images/cg/ep2/d22_c4_consola.webp")
            s "Come here."
            n "She pulls his head down onto her shoulder, coat and all, and he lets her."
            s "He did it because he can. Because it's Monday, and you were there. It isn't about you."
            n "It isn't. It's about her. She doesn't say that part."
            c "I said «yes, she does»."
            s "Well. I do. Deserve a man who sends his boss a dwarf by accident. It's the most you thing that's ever happened."
            n "That gets the laugh out, finally. Wet, and too loud, into her collar."
            if fatto("ep2_d21_detto_josh"):
                c "You told me about Jacob. Yesterday. You didn't have to. I keep thinking about that today. That you tell me things."
                sp "I tell you things."
        "Get annoyed at how weak he is.":
            $ segna("ep2_d22_irritata_josh")
            $ interest("josh", -3, "Sara couldn't hide it: he just took it.")
            $ interest("daniel", 1, "Daniel said it in front of everyone, and she heard it.")
            $ corruption(1, "Sara was angry with Josh, not with Daniel.")
            $ via_cg()
            $ cg("Sara standing up from the sofa with her arms folded, looking down at Josh, who looks up at her, stricken", "images/cg/ep2/d22_c4_irritata.webp")
            s "You said «yes, she does»."
            c "What should I have said?"
            s "Anything. Nothing. You could have not laughed, [nome_compagno]. Just once. You could have looked at him."
            c "It's Daniel. You don't know what he's like."
            n "She does, though. A little. She knows exactly what he's like at a table, ordering for two without the menu."
            s "I know you let him."
            n "He looks at her as if she'd done it too. Maybe she has, a bit. She goes into the kitchen to have something to do with her hands."
            sp "I'm angry with the wrong man. I know I am. I'm still angry."
    $ via_cg()
    $ cg("Late, Josh at the kitchen table typing a message on his phone, a calmer face; the dwarf's character sheet smoothed out beside his plate", "images/cg/ep2/d22_c5_mark.webp")
    $ segna("ep2_d22_josh_dnd")
    n "Later, at the table, he smooths the character sheet out with the side of his hand until the creases are almost gone."
    c "Mark's asked me every week since September. Wednesdays, at his. I always said no, because of you. Because of us."
    c "I'm going to say yes. I want one night a week where I'm good at something and nobody does a voice."
    if fatto("ep2_d22_consola_josh"):
        s "Go. Be a dwarf. I'll miss you a reasonable amount."
    else:
        s "Go, then."
        n "It comes out shorter than she meant. He hears it, and types the message anyway."
    sp "Wednesday. Half past seven to half past eleven. A whole evening that nobody's going to ask about."
    $ via_cg()
    return


## --- Notte: il telefono ------------------------------------------------------------------------
## Sessione libera breve. Con ep2_d21_joanie_parla_josh Sara rimanda Joanie: non stasera.

label ep2_d22_notte:
    $ vai("casa", "Home — Monday night")
    $ musica("notte")
    $ cg("The bedroom in lamplight, Josh asleep on his side; Sara sitting up against the headboard with her phone, the letter's words still in her head", "images/cg/ep2/d22_d1_letto.webp")
    n "[nome_compagno] falls asleep like someone who's been carrying furniture all day: all at once, still holding the edge of the duvet."
    if fatto("ep2_d21_joanie_parla_josh"):
        n "Joanie's name lights up. {i}so. when do I get him on his own. this week?{/i}"
        sp "Not this week, Jo. Not after today. Today somebody else already had him on his own."
    if fatto("ep2_d22_targa"):
        sp "Half a number plate in biro, in the zip pocket of my bag. I moved it twice before dinner. As if somebody might look."
    elif fatto("ep2_d22_inchiesta_rifiutata"):
        sp "Nadia Reyes. Twenty-six. In a drawer, on her own."
    call telefono_minuti_sessione(22 * 60 + 30, 23 * 60, "Go to bed")
    sp "The most beautiful woman in this city."
    n "She switches off the lamp before she can decide whether she's smiling."
    $ via_cg()
    return
