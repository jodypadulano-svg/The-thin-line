label ep2_d17:
    call nuovo_giorno(17, "Picture Day")
    $ fascia_corrente = FASCE.index("lavoro")
    call ep2_d17_redazione
    $ fascia_corrente = FASCE.index("pranzo")
    call ep2_d17_bar
    $ fascia_corrente = FASCE.index("lavoro")
    call ep2_d17_foto
    $ fascia_corrente = FASCE.index("sera")
    call ep2_d17_rientro
    call ep2_d17_palestra
    $ cg("Sara checks her phone outside the gym", "images/cg/ep2/d17_palestra_telefono_libero.png")
    menu:
        "Check the phone.":
            call telefono_nuovo_sessione("Go to bed")
        "Go to bed.":
            pass
    $ via_cg()
    $ musica(None)
    $ luogo_corrente = ""
    scene bg nero with fade
    return

label ep2_d17_redazione:
    $ vai("redazione", "The newsroom — Wednesday morning")
    $ musica("redazione")
    $ cg("Barbara reminds Sara about the website photos", "images/cg/ep2/d17_redazione_01_foto.png")
    n "Sara is reading a headline under her breath when Barbara stops beside her desk."
    ba "You're still in your coat."
    s "I was going to take it off an hour ago."
    ba "And at two?"
    s "At two I'll have taken it off."
    ba "Good. We're having our pictures taken at two."
    n "Sara looks at the yellow slip tucked under her monitor. She wrote WEBSITE PHOTOS on it herself."
    s "I thought that was next Wednesday."
    ba "You can forget them again next Wednesday. Today I need you downstairs after lunch."
    n "Jessica hides a smile behind her coffee."
    s "Have you got a mirror, Jess?"
    je "In my bag. Do you want the little one or the one that tells you everything?"
    ba "Come to my office if you like. I've got a brush and some makeup. We have time before lunch."
    menu:
        "I think I'll keep it simple.":
            s "Thanks, though. Jess, I'll take the little mirror."
            n "Jessica fishes it out of her bag and slides it across the desk."
            je "It's got a crack down the middle. Pick whichever half you like best."
            n "Sara props it against her keyboard. In either half, a coat collar is sticking up around one ear."
            s "That's plenty to be getting on with."
            n "Barbara taps the yellow slip on her way past. Sara moves it to the middle of the screen."
        "All right. What would you do?":
            $ segna("ep2_d17_glamour")
            $ via_cg()
            $ vai("redazione", "Barbara's office")
            $ cg("Barbara pins Sara's hair back beside the window", "images/cg/ep2/d17_redazione_02_capelli.png")
            n "Sara sits beside the window while Barbara pins her hair back. A strand slips loose beside her cheek. Barbara catches it, looks at Sara, and lets it fall again."
            n "Jessica wore her hair that way last week. Sara assumed hers had fallen down on the walk to work."
            n "Barbara sets two lipsticks on the desk. Sara picks up the darker one and turns it over to read the name."
            s "I always put this shade back when I try it in a shop."
            ba "Let's see it on you in daylight."
            n "Barbara finishes the lipstick and dusts a little color over Sara's cheeks."
            n "Sara tilts the mirror toward the window and presses her lips together once."
            ba "Try opening one more button. See how you like it."
            $ via_cg()
            $ cg("Sara checks her glamorous makeup in Barbara's mirror", "images/cg/ep2/d17_redazione_03_specchio.png")
            n "Sara undoes the button herself. She turns sideways, then back."
            s "I'd have done it up again by now if I'd tried this at home."
            ba "You've still got both hands."
            s "I think I'll leave it for lunch."
            n "She hands Barbara the mirror, then asks for it back for one last look."
    $ via_cg()
    return

label ep2_d17_bar:
    $ vai("bar_aperitivo", "The café — Lunch break")
    if fatto("ep2_d17_glamour"):
        $ cg("Jessica steals a chip from Sara's plate", "images/cg/ep2/d17_bar_01_tavolo.png")
    else:
        $ cg("Sara and her colleagues share a table at the café", "images/cg/ep2/d17_bar_01_tavolo_abituale.png")
    n "Jessica has saved Sara a seat with her bag. By the time Sara puts her plate down, someone has already taken one of her chips."
    s "I saw that."
    je "Then you know how long I waited."
    if fatto("ep2_d17_glamour"):
        $ via_cg()
        $ cg("A stranger stops at the table beside Sara", "images/cg/ep2/d17_bar_02_sconosciuto.png")
        n "A man passing their table slows down. He has his coat over one arm and one point of his shirt collar is folded in."
        "Man" "Sorry. I was halfway to the door and thought I'd regret it if I didn't say hello."
        s "Well, hello."
        n "He smiles. Jessica lowers her eyes to her plate. Sara can feel the attention of the whole table on her. To her surprise, she's enjoying it."
        menu:
            "Answer him as yourself.":
                s "I'm Sara. What were you going to say after hello?"
                "Man" "I was hoping you'd give me a minute to work that out."
                s "You can have until my chips get cold."
                n "He laughs. They talk until one of his friends waves him over from the door."
                "Man" "Nice meeting you, Sara."
                s "You too."
                n "Jessica waits until he's out of earshot."
                je "Your chips were cold when he got here."
                s "I know. It was a generous offer."
            "Play along. Do it like Jessica.":
                $ via_cg()
                $ cg("Sara gives the stranger a playful look", "images/cg/ep2/d17_bar_03_recita.png")
                n "Sara catches Jessica's eye and tilts her head the way Jessica does when she's about to ask for something she knows she'll get."
                s "All the way to the door? And you came back just for me?"
                "Man" "I did."
                s "That's sweet. I'd have pretended I'd forgotten my coat."
                if sara_corruption > 25:
                    n "Jessica glances at Sara's plate, then back up at her. One eyebrow goes up."
                    $ via_cg()
                    $ cg("Sara teases the stranger with her hot dog", "images/cg/ep2/d17_bar_03a_hot_dog.png")
                    n "Sara lifts the hot dog to her lips and mimes the gesture, holding his gaze a beat longer than she needs to. She wants Jessica to see that she's taken the dare."
                    n "His cheeks go red. He opens his mouth as if he's about to speak and nothing comes out."
                    n "Sara sets the hot dog back on her plate. Jessica has stopped pretending to eat."
                    $ via_cg()
                    $ cg("Sara gives the stranger a playful look", "images/cg/ep2/d17_bar_03_recita.png")
                n "She reaches up and smooths the folded point of his collar with her thumb."
                n "For half a second her hand stays there. She meant to do the voice and tilt her head. She didn't mean to touch him."
                n "She takes her hand back and feels her face warm."
                s "Sorry. It was tucked in."
                "Man" "Oh. Thanks. I'd have walked around like that all afternoon."
                n "His friend calls from the door. He touches his collar once, smiles at Sara, and goes to join him."
                je "That wasn't in the script."
                s "I know."
                $ via_cg()
                $ cg("Sara laughs with Jessica after the stranger leaves", "images/cg/ep2/d17_bar_06_risata.png")
                n "Sara takes a drink. When she puts the glass down, Jessica is still trying to keep a straight face. Sara laughs first."
    else:
        n "Jessica glances at the butter knife beside Sara's plate."
        je "You've checked your reflection in that twice."
        s "It's the only mirror I've found that makes me look taller."
        n "Jessica turns the knife over. The other side is smeared with butter."
        je "There. Now you can eat."
    $ via_cg()
    return

label ep2_d17_foto:
    $ musica(None, dissolvenza=0)
    $ vai("redazione", "The newsroom — 2 p.m.")
    $ ambiente("redazione")
    if fatto("ep2_d17_glamour"):
        $ cg("The photographer takes Sara's website portrait in her glamour look", "images/cg/ep2/d17_foto_glamour.png")
    else:
        $ cg("The photographer takes Sara's website portrait in her usual look", "images/cg/ep2/d17_foto_abituale.png")
    n "The photographer has pushed a filing cabinet out of the way and taped a mark to the carpet. Sara stands on it while he checks her name."
    "Photographer" "Sara Collins?"
    s "That's me."
    "Photographer" "For the caption, what do you do here?"
    s "I write. You can put that."
    n "He writes it down. She answered before she could think of a smaller way to say it."
    if fatto("ep2_d17_glamour"):
        n "In the reflection of the dark window, the lipstick looks darker than it did in Barbara's office. Sara checks the open button with one finger and leaves it where it is."
    else:
        n "Sara lifts a hand to fix her hair, then lowers it. She's already fixed it three times in the mirror."
    "Photographer" "Turn a little toward the window. That's it."
    $ suono("otturatore")
    n "The shutter clicks while Sara is still waiting for him to tell her to smile."
    n "He shows her two frames on the back of the camera. In the second one she can see herself beginning to pose."
    s "Can we use the first one?"
    "Photographer" "Of course."
    if fatto("ep2_d17_glamour"):
        call ep2_d17_foto_extra
        $ musica(None)
    else:
        n "On her way back upstairs, she catches Barbara coming down."
        ba "Survived it?"
        s "Even got the caption right."
    $ ambiente(None)
    $ via_cg()
    return

label ep2_d17_rientro:
    $ vai("casa", "Home — After work")
    if fatto("ep2_d14_maglione_ordinato"):
        ## Il corriere può lasciare il pacco a Sara o al vicino.
        $ segna("ep2_pacco_joanie_da_howard", renpy.random.choice((False, True)))
        if not fatto("ep2_pacco_joanie_da_howard"):
            $ cg("Sara notices the parcel by her front door", "images/cg/ep2/d17_rientro_pacco.png")
            n "A parcel is waiting by the front door. Sara recognizes the shop name from the link Joanie sent on Sunday."
            $ via_cg()

    if fatto("ep2_d17_glamour"):
        $ cg("Sara removes her makeup and hairpins at the bathroom mirror", "images/cg/ep2/d17_rientro_strucco.png")
        n "Sara washes off the lipstick and makeup, takes out the pins and changes out of her work clothes."
        $ via_cg()

    if fatto("ep2_d14_maglione_ordinato"):
        if fatto("ep2_pacco_joanie_da_howard"):
            call ep2_d17_ritiro_howard
        call ep2_d17_pacco

    ## La finestra si chiude prima di partire per arrivare in anticipo in palestra.
    if howard_puo_fare_faccenda(giorno, FASCE[fascia_corrente], True, True, fatto("ep2_d17_ritiro_howard"), howard_ultima_faccenda_giorno, valore_interest("howard")):
        $ cg("Sara pauses by Howard's closed door with her gym bag at her feet", "images/cg/ep2/d17_pianerottolo_prima_palestra.png")
        n "Sara has already packed her gym bag. She checks the time. There's still an hour before she needs to leave."
        n "On the landing she hears Howard saying goodbye to someone on the phone behind his door. She sets her bag down."
        call howard_faccende_dopo_lavoro(True, True, False)
    return

label ep2_d17_ritiro_howard:
    $ cg("Sara checks the delivery notice and knocks at Howard's door", "images/cg/ep2/d17_ritiro_pacco_porta_howard.png")
    n "The delivery notice says the courier left the parcel with Howard. Sara knocks at his door."
    $ cg("Howard answers Sara's knock", "images/cg/ep1/d9_04_howard_porta.webp")
    ho "Ah. I put it on the table. Hang on."
    n "He comes back holding the parcel flat on both palms."
    ho "It weighed so little I thought they'd given me the envelope by mistake."
    s "I think that might be the idea."
    n "Howard looks down at the parcel again. Sara takes it before she has to think of what to say next."
    s "Thanks for taking it in."
    $ segna("ep2_pacco_joanie_da_howard", False)
    $ segna("ep2_d17_ritiro_howard")
    $ via_cg()
    return

label ep2_d17_pacco:
    $ cg("Sara lifts the black mesh top out of Joanie's parcel", "images/cg/ep2/d17_pacco_top.png")
    n "Sara opens the parcel on the kitchen table, expecting white knit and two ridiculous spirals. The first thing she pulls out is a sheer black sleeve."
    n "She frees the mesh from a rough edge of cardboard and lifts the top by its wavy collar. Two large, opaque black circles are joined by a thin strip of fabric."
    $ segna("ep2_d17_top_ricevuto")
    $ chat_aperta = "amica"
    show screen telefono_chat("amica")
    $ msg("sara", "Joanie. Where are my spirals?", premia_avvio=False)
    $ msg("amica", "YOUR spirals? on sunday they were a bit much")
    $ msg("sara", "I spent three days wondering if I'd have the nerve to wear them.")
    $ msg("amica", "i know. that's why i sent you the listing")
    $ msg("sara", "You ordered this one the whole time?")
    $ msg("amica", "yep. but say the word and i'll get you the spiral one too :D")
    $ msg("sara", "Let me get through one parcel at a time.")
    hide screen telefono_chat
    $ chat_aperta = None
    if fatto("ep2_d18_pranzo_daniel_confermato"):
        n "Sara holds the top against herself and thinks of Daniel waiting while she takes off her coat. She folds it along the crease it made in the parcel. She can decide what to wear in the morning."
    else:
        n "Sara holds the top against herself. Joanie said she could leave it in the box. She lays it over the back of a chair instead."
    $ via_cg()
    return

label ep2_d17_palestra:
    $ vai("casa", "Home — Before the gym")
    menu:
        "Wear the loose T-shirt.":
            $ segna("ep2_d17_top_palestra_aderente", False)
        "Wear the fitted workout top.":
            $ segna("ep2_d17_top_palestra_aderente")
            $ corruption(1, "Sara chose the fitted top for the gym.")
            $ interest("simon", 1, "Sara chose the fitted top for the gym.")

    $ vai("palestra", "The gym — Wednesday evening")
    $ musica("palestra")
    $ ambiente("palestra")
    $ cg("Sara finds Simon's water bottle on the empty reception desk", "images/cg/ep2/d17_palestra_01_reception.png")
    n "The clock above reception is seven minutes fast. Simon told Sara that on Monday. She looks at it anyway."
    n "His water bottle is on the counter. The stool behind it is empty."
    s "Simon?"
    $ via_cg()
    $ cg("Sara pauses by the half-open stretching room door", "images/cg/ep2/d17_palestra_02_porta.png")
    n "She walks past the treadmills toward the stretching room. The door is open a hand's width. She sees Joanie's reflection in the wall mirror first. Then Simon moves, close against her, and Sara understands what she's walked in on."
    n "The night before, she watched Mark and Josh get on as if they'd known each other for years. Now Mark's face comes back to her before she can think what to do."
    menu:
        "Stay for another moment.":
            $ corruption(2, "Sara stayed a moment after discovering Joanie and Simon.")
            $ segna("ep2_d17_ha_guardato_joanie_simon")
            $ filmato("images/video/ep2/d17_palestra_joanie_simon.webm")
            $ via_cg()
            $ cg("Sara's reaction at the stretching-room doorway", "images/cg/ep2/d17_palestra_02a_reazione.png")
            n "Sara keeps her hand on the doorframe. She could step back. She stays long enough to hear Joanie say Simon's name, quietly, almost laughing."
            n "Then Joanie shifts and Sara sees how easily she could turn her head and catch her in the mirror. Sara backs into the corridor and lets her hand fall."
            n "At reception she pulls her water bottle out of her bag. She has to look down to find the cap she's already holding."
        "Walk away quietly.":
            n "Sara steps back before either of them looks up. She walks to reception, sits down, and reties a shoe that's already tied."
            n "She can wait here until he comes out. From where she's sitting, there's no reason she should know he was anywhere other than the staff room."
    $ via_cg()
    if fatto("ep2_d17_top_palestra_aderente"):
        $ cg("Simon finds Sara at reception in her fitted workout top", "images/cg/ep2/d17_palestra_04_simon_top_aderente.png")
    else:
        $ cg("Simon finds Sara at reception in her loose T-shirt", "images/cg/ep2/d17_palestra_03_simon_maglia_larga.png")
    n "Simon comes around the corner with his sleeves pushed up and a red patch high on his neck."
    si "Sorry. How long have you been here?"
    s "A few minutes."
    n "He picks up his bottle from the counter."
    si "You doing the same warm-up as Monday?"
    n "Sara knows what she's supposed to say next. She takes a drink first."
    menu:
        "Train with Simon.":
            $ interest("simon", 3, "Sara trained with Simon on Wednesday.")
            $ via_cg()
            if fatto("ep2_d17_top_palestra_aderente"):
                $ cg("Simon counts Sara's reps by the rack", "images/cg/ep2/d17_palestra_05_simon_top_aderente.png")
            else:
                $ cg("Simon counts Sara's reps by the rack while she wears her loose T-shirt", "images/cg/ep2/d17_palestra_05_simon_maglia_larga.png")
            s "Yes. Can you check the last set with me?"
            si "Sure. Show me the first one and I'll see what we're working with."
            n "He counts her reps from beside the rack. On the sixth he starts to say something, then lets her finish. Sara sets the weight down."
            si "You caught it yourself that time."
            s "I felt my left heel lift."
            si "That's it. Do you want another set?"
            s "In a minute."
            n "She likes how quickly he notices when she gets something right. He did that on Monday too. She takes her minute and asks him to count again."
        "Train on your own.":
            $ confidence(1, "Sara chose to train on her own on Wednesday.")
            $ via_cg()
            $ cg("Sara works through her sets alone", "images/cg/ep2/d17_palestra_06_da_sola.png")
            s "I think I'll do my own sets tonight."
            si "All right. Give me a shout if you need anything."
            n "She starts lighter than she planned. On the second set she moves her left foot half an inch and feels the difference. By the time she puts the weight back, she knows what she wants to try next time."
            n "Simon lifts a hand from across the room. Sara lifts hers in return and goes to get her bag."
    $ via_cg()
    $ ambiente(None)
    $ fascia_corrente = FASCE.index("notte")
    $ vai("strada", "Outside the gym — Wednesday night")
    $ cg("Outside the gym, Sara looks at her chat with Joanie", "images/cg/ep2/d17_palestra_07_uscita.png")
    n "Outside, Sara opens her chat with Joanie."
    if fatto("ep2_d17_top_ricevuto"):
        n "In the afternoon she thought she might send a picture when she tried the top on. Now she wonders what she'd write above it."
    else:
        n "There's a message from earlier in the week she meant to answer. She finds it. For a while she just looks at Joanie's name."
    n "Her screen dims with the message box still empty. She puts her phone in her pocket and starts home."
    $ via_cg()
    return
