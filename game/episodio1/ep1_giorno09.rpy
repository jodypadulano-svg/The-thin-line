## =============================================================================
## EPISODE 1 — DAY 9 (Tuesday)
## =============================================================================
## Calendar: docs/mese-1.md, day 9. Work: [nome_compagno]'s message, «Daniel has
## put me on until nine» (I14, announced on day 7). Evening: Sara comes home alone
## and has no keys (stolen by Howard on day 6). Howard takes her in: Howard 3,
## the fake crying (retroscena), «can we see each other more often?». Tappa
## Howard 3.
## Decisions with Jody:
## - 19/11 Q&A: at Howard's Sara feels only tenderness, an almost maternal
##   protectiveness; she has NOT yet understood that he desires her (that comes
##   on day 11). The player, through the retroscena, sees more than she does.
## - 19/11 Q&A: no locksmith. [nome_compagno] says to wait a couple of days,
##   «they always turn up, and a locksmith costs a fortune»; he opens for now.
## - Howard notes 19/11: he plans everything, never threatens, never sabotages
##   [nome_compagno]; the game makes clear to the player that he set this up.
## Draft for Jody's review. Game text in English; comments in Italian.
## CG: docs/prompt-immagini/inquadrature-giorno-09.md. Finché mancano,
## compare la didascalia [CG].

label ep1_d9:
    call nuovo_giorno(9, "Tuesday")
    call ep1_d9_mattina
    call ep1_d9_lavoro
    call ep1_d9_chiusa_fuori
    call ep1_d9_da_howard
    call ep1_d9_sera
    return


## --- Retroscena: Howard dallo spioncino ----------------------------------------------

label ep1_d9_mattina:
    $ luogo_corrente = ""
    scene bg nero with fade
    call inizio_retroscena
    $ cg("Through the fish-eye of a peephole: Sara and Josh going down the stairs together in the morning, Josh locking the door behind them", "images/cg/ep1/d9_01_spioncino.webp")
    rs "Twenty past eight. Sara and [nome_compagno] leave together. He's the one who locks the door. He always is, since Saturday."
    rs "Behind the green door, Howard watches them through the peephole until the street door bangs shut."
    rs "Tuesday. The late shift. He heard it through the bedroom wall on Sunday night, in [nome_compagno]'s tired voice: «Tuesday for sure, maybe more.»"
    rs "In the drawer of his bedside table, next to something pale pink and lacy, there's a ring of keys with a little silver pen."
    rs "He doesn't take it out. He just looks at it, and closes the drawer."
    $ retroscena("howard", "He knows the couple's timetable: he knew Sara would come home alone on Tuesday, with no keys.")
    call fine_retroscena
    return


## --- Lavoro: il messaggio di Josh (I14) -----------------------------------------------

label ep1_d9_lavoro:
    $ vai("redazione", "The newsroom — 3:20 p.m.")
    $ musica("redazione")
    $ ambiente("redazione")
    $ cg("The newsroom in the afternoon: Sara at her desk reading a message on her phone, a little crease between her eyebrows", "images/cg/ep1/d9_02_messaggio_josh.webp")
    $ suono("telefono_vibra")
    n "Mid-afternoon, her phone buzzes. [nome_compagno]."
    n "{i}Bad news. Daniel's put me on until nine. Maybe later. Don't wait up for dinner, I'll grab something. Sorry sorry sorry.{/i}"
    sp "He told me on Sunday. I knew. It still stings a little."
    if fatto("ep1_d5_risposta_daniel"):
        sp "Is this because of me? Because of what I said to Daniel on Friday?"
        sp "No. Don't be ridiculous. It's just work."

    menu:
        sp "How do I answer?"
        "Something sweet.":
            $ interest("josh", 1, "A sweet message in the middle of a long day.")
            n "{i}Poor love. I'll keep the bed warm. Eat something that isn't from a machine.{/i}"
            $ suono("notifica")
            n "The answer is a single heart and a photo of a sad vending-machine sandwich."
            sp "Idiot. My idiot."
        "Let him know she's annoyed.":
            $ interest("josh", -1, "Sara let her irritation show.")
            n "{i}Again? It's the second time this month. Does Daniel know you have a life?{/i}"
            $ suono("notifica")
            n "The answer takes twenty minutes to arrive: {i}I know. I'm sorry. It's not up to me.{/i}"
            sp "I know it isn't. That's what annoys me."
    return


## --- Sera: senza chiavi -----------------------------------------------------------------

label ep1_d9_chiusa_fuori:
    $ vai("pianerottolo", "The landing — 5:45 p.m.")
    $ ambiente(None)
    $ musica(None)
    $ cg("The landing at dusk: Sara crouched on the doormat in front of her door, the contents of her bag spread out around her, searching desperately", "images/cg/ep1/d9_03_senza_chiavi.webp")
    n "Sara climbs the stairs already thinking about the sofa, a hot shower and an evening alone with her novel."
    n "In front of the door, she puts her hand in her bag. Then the other hand. Then she empties the whole bag onto the doormat."
    s "No, no, no... where are they?"
    n "Wallet. Notebook. Three pens, none of them silver. A lip balm. A receipt from the Lantern. No keys."
    sp "When did I last use them? Saturday? Since Saturday [nome_compagno] has always opened the door. Always."
    sp "First the underwear, now the keys. What is wrong with me?"
    $ suono("telefono_vibra")
    n "She calls [nome_compagno]. He answers on the fifth ring, in a whisper, from the middle of a meeting."
    c "I can't leave, love. Daniel's right here. Nine o'clock, I swear, I'll run."
    sp "Nine. It's quarter to six."
    n "She's still sitting on the doormat, gathering her things, when the green door across the landing opens."

    $ cg("Howard in the doorway of his green flat in his old cardigan, looking down at Sara on the doormat with an expression of exaggerated concern", "images/cg/ep1/d9_04_howard_porta.webp")
    ho "Sara? Oh, dear. Oh, dear, dear. Problems?"
    s "I've lost my keys. And [nome_compagno] is stuck at work until nine."
    ho "Lost them? Oh, you poor thing. It happens. It happens to everyone, it does."
    ho "Well, you can't stay out here on the landing for three hours. Come and wait at mine. I'll make you a coffee."
    if fatto("ep1_d6_caffe_howard"):
        ho "You made me one on Saturday. Now it's my turn. Fair's fair."
    sp "Three hours on a doormat. Or Howard."
    sp "Be nice, Sara. He's only being kind."
    return


## --- Da Howard: Howard 3 e il pianto finto ----------------------------------------------

label ep1_d9_da_howard:
    $ vai("casa_howard", "Howard's flat — 6:00 p.m.")
    $ cg("Howard's living room: dark and stuffy, curtains drawn, piles of old newspapers, dirty plates on the table, an armchair moulded by years of the same body, the television murmuring", "images/cg/ep1/d9_05_casa_howard.webp")
    n "The flat is the mirror image of theirs, and the opposite in every other way."
    n "The curtains are drawn. Newspapers are stacked on the chairs, on the floor, on the radiator. There are plates on the table with something dried on them. The air is thick, old, closed."
    sp "Oh God. Don't breathe through your nose, Sara. And smile."
    ho "Sorry about the mess. Nobody ever comes round, you see. You stop noticing."
    n "He clears a chair by moving a pile of newspapers to another pile of newspapers."

    menu:
        sp "The mess."
        "Pretend not to notice.":
            s "Don't worry. Ours is a disaster too."
            n "It isn't, and they both know it. Howard smiles anyway."
        "Offer to help him tidy up, one of these days.":
            $ interest("howard", 2, "Sara offered to help him.")
            $ segna("ep1_d9_aiuto_pulire")
            s "You know what? One of these days I'll come over and help you. Two people, two hours, and it'll look like a new flat."
            ho "You... you'd do that? For me?"
            n "He looks at her as if she'd offered him a kidney."
            ho "Nobody's ever... well. Well. We'll see. We'll see."
            call inizio_retroscena
            rs "Howard turns towards the kitchen to hide his face. He's smiling, and it isn't the awkward smile."
            $ retroscena("howard", "Sara offered to come back to tidy his flat. He'll make sure she remembers.")
            call fine_retroscena

    $ cg("Howard's kitchen table: Howard pouring coffee into two chipped mugs, Sara sitting with her coat still on, politely holding her cup", "images/cg/ep1/d9_06_caffe.webp")
    n "Howard makes coffee in chipped mugs and doesn't ask her anything. He talks."
    n "About the factory where he worked for thirty-one years. About his mother, whom he looked after until the end. About dinners in front of the television."
    ho "At my age you stop hoping, you know. You get up, you eat, you watch the telly, you go to bed. And tomorrow, the same."
    ho "I always thought there'd be someone. A woman. Someone to cook for. Someone to tell about my day."
    ho "Then one day you look up and you're sixty-three, and the someone never came."
    sp "God. Poor man."
    n "Then his voice cracks. He puts his mug down. He covers his face with his hands, and his shoulders begin to shake."

    $ cg("Howard hunched in his armchair with his face in his hands, shoulders shaking; Sara on the edge of her chair leaning towards him, moved", "images/cg/ep1/d9_07_pianto.webp")
    call inizio_retroscena
    rs "Between his fingers, Howard's eyes are dry. He's watching her."
    rs "He's watching how she leans forward. How her face softens. How her hand starts to move towards him and stops."
    $ retroscena("howard", "The crying was fake: he wanted Sara's compassion.")
    call fine_retroscena

    sp "He's really crying. Oh, Howard."
    sp "Nobody should be this alone."

    menu:
        sp "What do I do?"
        "Kind words, from her chair.":
            $ interest("howard", 1, "Sara's kind words.")
            s "Hey. Howard. It's all right. You're not alone. We're right across the landing, [nome_compagno] and me."
            s "You can knock whenever you want. I mean it."
            n "Howard nods behind his hands, slowly. After a while, he wipes his eyes with the back of his wrist, though there's nothing to wipe."
        "Hug him.":
            $ interest("howard", 1, "Sara hugged Howard to comfort him.")
            $ segna("ep1_d9_abbraccio")
            $ howard_abbraccio_prolungamenti = 0
            $ cg("Sara crouches beside Howard's worn armchair and embraces him tenderly; he presses his face into her hair.", "images/cg/ep1/d9_10_abbraccio.webp")
            n "Sara gets up, crouches by the armchair and puts her arms around him, the way she'd hug a child who's fallen off a bike."
            s "Shh. It's all right. It's all right, Howard."
            n "He smells of old wool and instant coffee. He's bigger and softer than she expected, and he's trembling."
            call inizio_retroscena
            rs "Howard closes his eyes, buries his face in her hair, and slowly breathes her in. Sara cannot see him."
            $ retroscena("howard", "Howard lingered in her arms and breathed in her hair without her noticing.")
            call fine_retroscena
            sp "He's shaking. Like a big, frightened child."

            ## Ogni scelta di restare aggiunge un punto a Howard. Dopo la terza,
            ## il tratto Crocerossina è permanente: le proposte di Howard
            ## marcate rifiuto_howard=True non potranno più essere rifiutate.
            while howard_abbraccio_prolungamenti < 3:
                if howard_abbraccio_prolungamenti == 0:
                    n "Howard makes no move to release her. Perhaps she should be the one to end the hug."
                elif howard_abbraccio_prolungamenti == 1:
                    n "It's going on rather long. His hand rests lower on her back than before. She can still pull away."
                else:
                    n "{b}WARNING: This decision will have permanent consequences.{/b}"
                    n "Continuing will activate Sara's Savior Complex toward Howard. From this point on, refusal options when Howard makes a proposal will be greyed out for the rest of the game."
                    n "{b}Continue at your own risk. This lasts for the rest of the playthrough unless you roll back or reload an earlier save.{/b}"

                menu:
                    "Pull away from the hug.":
                        n "Sara gently straightens up. Howard doesn't release her until she moves away."
                        s "There. See? You're not on your own."
                        jump ep1_d9_abbraccio_finito
                    "Keep holding him a little longer.":
                        $ howard_abbraccio_prolungamenti += 1
                        $ interest("howard", 1, "Sara chose to prolong the comforting hug.")
                        if howard_abbraccio_prolungamenti == 1:
                            $ cg("The same hug: Howard's lower hand has slid down to Sara's waist, at the waistband of her skirt", "images/cg/ep1/d9_10b_vita.webp")
                            n "Howard stays very still, as though afraid the moment might end."
                            sp "He must have needed someone to hold him for such a long time."
                        elif howard_abbraccio_prolungamenti == 2:
                            $ cg("The same hug: Howard's hand has slipped further down, onto the side of Sara's hip, the edge of her bottom; Sara still holds him tenderly.", "images/cg/ep1/d9_11_mani.webp")
                            sp "His hand is lower than before."
                            sp "He's just holding on. Like someone who's drowning."
                        else:
                            ## Terza volta (Jody, 20/11): la mano sul sedere, il volto di
                            ## Sara che si rimprovera, il volto soddisfatto di Howard,
                            ## poi l'avviso del tratto.
                            $ cg("The same hug: Howard's hand is now squarely on Sara's bottom; his eyes closed, smiling", "images/cg/ep1/d9_11b_mano.webp")
                            n "And then his hand isn't on her back any more."
                            $ cg("Close-up of Sara's face against Howard's shoulder: her eyes open wide for a moment, a flicker of doubt, then guilt", "images/cg/ep1/d9_11c_sara_volto.webp")
                            sp "Wait. Is that... his hand on my...?"
                            sp "No. What are you even thinking, Sara? He's a heartbroken old man. He doesn't know where his hands are."
                            sp "Shame on you."
                            $ cg("Two panels: Howard's face, eyes closed, a greedy, satisfied smile over Sara's head; his hand spread on her bottom", "images/cg/ep1/d9_12_howard_sorriso.webp")
                            call inizio_retroscena
                            rs "Sara's face is against his shoulder. She cannot see Howard's expression: his eyes are half-closed, and a small, greedy smile curls his lips."
                            rs "He knows exactly where his hand is. And he does not intend to let go first."
                            $ retroscena("howard", "After three choices to continue the hug, his hand reached her bottom. Sara blamed herself for even thinking it. She never saw his smile.")
                            call fine_retroscena
                            $ complesso_crocerossina = True
                            $ segna("ep1_d9_crocerossina_attivata")
                            n "{b}Trait activated: Savior Complex — Howard.{/b}"
                            n "{b}From now on, choices that go against Howard are disabled: they will stay visible, in grey, for the rest of the playthrough.{/b}"
                            sp "Poor Howard. No one should feel so alone."
                            n "Eventually Sara rises, gently disentangling herself. Howard would have stayed like that indefinitely."

label ep1_d9_abbraccio_finito:
    $ nota_sara("howard", "A lonely man. She feels enormously tender towards him.")
    n "The rest of the evening passes slowly, and not unpleasantly. Howard shows her photos of his mother. He makes her a cheese sandwich that she eats out of politeness, and then out of hunger."
    sp "He's sweet, in his way. A little sad. A little strange. But sweet."
    return


## --- Josh torna: «possiamo vederci più spesso?» ----------------------------------------

label ep1_d9_sera:
    $ vai("casa_howard", "Howard's flat — 9:10 p.m.")
    $ suono("chiave_serratura")
    n "At ten past nine, footsteps run up the stairs and a key turns in the lock across the landing. [nome_compagno]."
    $ cg("Howard's doorway: Howard holding the door for Sara as she leaves, looking up at her with hopeful, wet eyes; across the landing Josh's door is open with light pouring out", "images/cg/ep1/d9_08_soglia.webp")
    ho "Sara..."
    ho "It was nice, today. Talking to someone. Really talking."
    ho "Could we... see each other now and then? Just a coffee. A little chat. Nothing more."

    menu:
        sp "What do I tell him?"
        "«Of course, Howard. A coffee now and then.»":
            $ interest("howard", 3, "Howard won't forget this answer.")
            $ segna("ep1_howard_caffe", "si")
            ho "Really? Oh... thank you. Thank you, Sara."
            n "He says her name as if he were putting it somewhere safe."
        "«When it happens, gladly.»":
            $ interest("howard", 2, "A door left ajar.")
            $ segna("ep1_howard_caffe", "forse")
            ho "When it happens. Of course. I'm always here."
        "«I'm sorry, Howard, I really don't have much time.»" (rifiuto_howard=True):
            $ segna("ep1_howard_caffe", "no")
            ho "I understand. I understand perfectly."
            call inizio_retroscena
            rs "When the door closes, Howard stays in the hall, staring at it for a long time."
            rs "Then he goes to the bedside table and opens the drawer again."
            $ retroscena("howard", "The refusal didn't stop him. It only made him more patient.")
            call fine_retroscena

    $ tappa("howard", 3)

    $ vai("casa", "Home — 9:20 p.m.")
    $ musica("casa")
    $ cg("The entrance hall of the flat: Josh still in his work clothes, tie loosened, hugging Sara tight; her bag dropped on the floor", "images/cg/ep1/d9_09_josh_abbraccio.webp")
    c "I'm so sorry. I'm so, so sorry. Three hours at Howard's. Are you alive?"
    s "I'm alive. He was sweet, actually. He's very lonely."
    c "Poor guy. Well, thank God for Howard."
    s "And the keys? Should we call a locksmith? Change the lock?"
    c "A locksmith? Do you know what they charge at night? A fortune."
    c "They'll turn up, love. They always turn up. In a coat pocket, in the gym bag, under the sofa. Give it a couple of days."
    c "Till then I'll open. I'm your doorman. Very cheap, very handsome."
    sp "He's right. They'll turn up."
    sp "Where could they possibly be?"
    n "Across the landing, behind the green door, the light stays on for a long time."
    return
