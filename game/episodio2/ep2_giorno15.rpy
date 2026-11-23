label ep2_d15:
    call nuovo_giorno(15, "Fifty Pages")
    $ fascia_corrente = FASCE.index("lavoro")
    call ep2_d15_redazione
    call ep2_d15_palestra
    call ep2_d15_casa
    $ musica(None)
    $ luogo_corrente = ""
    scene bg nero with fade
    return

label ep2_d15_redazione:
    $ vai("redazione", "The newsroom — Monday morning")
    $ musica("redazione")
    $ ambiente("redazione")
    $ cg("Sara and Barbara at the editorial meeting", "images/cg/ep2/d15_01_redazione.webp")
    n "Barbara has spread Friday's paper across the meeting table. The fold runs right through Sara's byline. Sara smooths it flat with the side of her hand."
    ba "Before we move on. Anything we should go back to from Friday?"
    n "Sara has an idea written in the margin of her notebook. She puts her thumb on the first word."
    menu:
        "Keep listening.":
            n "Sara waits for a gap. When Barbara turns the page, she writes a question mark beside the idea. She leaves it there for later."
        "Pitch a follow-up.":
            $ cg("Sara pitches her follow-up to Barbara", "images/cg/ep2/d15_01a_proposta.webp")
            s "I'd like to go back with the paper and let the people I spoke to read it. Then ask them what they think I left out."
            ba "Suppose they tell you they loved it?"
            s "Then I'll ask them separately."
            n "Barbara looks up. Sara had meant it seriously. After a second, Barbara smiles."
            ba "Bring me a paragraph tomorrow."
            n "Sara puts a box around the idea. She can already think of the first person she'd call."
            $ confidence(1, "Sara defended her idea at the editorial meeting.")
    $ ambiente(None)
    $ via_cg()
    return

label ep2_d15_palestra:
    $ fascia_corrente = FASCE.index("sera")
    $ vai("palestra", "The gym — Monday evening")
    $ musica("palestra")
    $ ambiente("palestra")
    $ cg("Joanie saves Sara a mat", "images/cg/ep2/d15_02_tappetini.webp")
    n "Joanie has claimed two mats and is sitting on the corner of Sara's."
    ch "I saved this for you. By sitting on it. People respect that."
    s "People are afraid to ask you to get up."
    ch "Same result."
    $ cg("Simon demonstrates the elbow angle while Sara does a dumbbell press", "images/cg/ep2/d15_03_manubri.webp")
    n "On the last set, Sara brings the dumbbells down too quickly. Simon comes over and crouches beside the bench, where she can see him without lifting her head."
    si "Try taking three counts on the way down. Here. Watch my elbow."
    n "He demonstrates the angle. Sara tries again. By the third count her arms are shaking."
    si "There it is."
    ch "Funny. When I do it wrong, he just shouts ‘elbows’ from across the room."
    menu:
        "Look down, smiling.":
            n "Sara sits up and adjusts the seam of her top where it's pulled across her chest."
            s "I was hoping you hadn't noticed."
            ch "I notice everything. Very little of it goes in the group chat."
        "Play along.":
            $ cg("Simon catches Joanie's towel", "images/cg/ep2/d15_03a_asciugamano.webp")
            s "Have you tried doing it really, spectacularly wrong?"
            si "She has."
            n "Joanie throws her towel at him. He catches it with both hands."
        "Ask for one more rep.":
            $ cg("Joanie spots Sara's final dumbbell repetition", "images/cg/ep2/d15_03b_un_altra.webp")
            s "Can you count the next one? I want to get it right."
            n "Simon counts. On three, Joanie puts a hand under each dumbbell to help Sara rack them."
            ch "I've got them. Let go."
    $ cg("Joanie suggests a chest exercise and Simon waits for Sara's answer", "images/cg/ep2/d15_03c_proposta_cavi.webp")
    n "Joanie rolls a dumbbell back into place with the sole of her shoe."
    ch "You know what Sara never does? Chest. You should show her a couple of exercises."
    n "Simon looks at Sara. Joanie has already turned the bench towards the cable machine."
    si "Do you want me to?"
    menu:
        "I'm done for today.":
            s "Ask me before the last set next time."
            n "Simon nods and reaches for his water. Joanie turns the bench back with her foot."
            ch "For the record, that was my last set."
        "Show me.":
            n "Simon demonstrates a chest press and then a cable fly, slow enough for Sara to follow the movement. He lowers the weight before handing her the grips."
            si "Soft elbows. Want me to guide them once?"
            s "Yes. Just the first one."
            $ cg("Simon guides Sara's elbows as Joanie watches", "images/cg/ep2/d15_03d_cavi.webp")
            n "He puts two fingers under each elbow. As Sara brings the handles together, her top pulls tight across her breasts. In the mirror, she sees Simon's gaze drop from her elbows to her chest. It stays there for the last inch of the rep. By the time he meets her eyes in the glass, she knows he's seen her notice."
            n "Joanie has stopped fiddling with the lid of her bottle. She's watching Sara's chest too. When Sara catches her eye, Joanie smiles."
            si "You've got it."
            n "He takes his hands away. Sara can still feel where his fingers were. She could put the handles back now. Simon would let her."
            $ interest("simon", 2, "Sara asked Simon to show her the cable exercise.")
            $ corruption(1, "Sara enjoyed catching Simon looking.")
            menu:
                "Rack the handles.":
                    n "Sara lets the weights settle and steps away from the machine."
                    s "Okay. I know how to do it now."
                "Let him see one more.":
                    $ cg("Sara chooses another repetition while Simon and Joanie watch", "images/cg/ep2/d15_03e_cavi_extra.webp")
                    n "Sara frees the edge of her neckline where it's caught under her sports-bra strap and draws it lower. The next time she brings the handles together, the neckline dips enough to show much more of her cleavage. She takes all three counts. Simon watches in the mirror, and this time Sara keeps her eyes on him."
                    si "That's the pace."
                    n "Joanie raises the bottle to her mouth without drinking. Sara puts the handles back before either of them says anything else."
                    $ corruption(1, "Sara chose to show Simon more.")
            ch "See? I had a good idea."
            s "You can try it next."
            n "Joanie takes a drink. Sara catches the smile she's trying to hide around the rim."
    $ cg("Joanie creates Gym squad with Sara and Simon", "images/cg/ep2/d15_03f_gym_squad.webp")
    $ da_numero("simon")
    n "Joanie creates a group chat and names it Gym squad."
    ch "proof we all showed up on the same day"
    si "You can put that on my calendar instead of a photograph."
    $ ambiente(None)
    $ via_cg()
    return

label ep2_d15_casa:
    $ fascia_corrente = FASCE.index("notte")
    $ vai("casa", "Home — Late Monday evening")
    $ musica("casa")
    $ cg("Josh interrupts Sara while she is working on the manuscript", "images/cg/ep2/d15_04_manoscritto.webp")
    n "Magnus's card is propped against the lamp. Sara has the first fifty pages open on her laptop and a pencil between her teeth. At the bottom of page forty-nine, she's found a sentence she can cut in half."
    n "[nome_compagno] stops in the doorway. She hears him set a mug down behind her."
    c "Why did you make her engaged?"
    n "Sara takes the pencil out of her mouth."
    s "Who?"
    c "The woman in your book. He takes her out onto a terrace. Gives her his jacket. And she's standing there thinking about how easy it would be to let him kiss her."
    s "You read it?"
    c "It was open yesterday. I sat down and read it."
    $ segna("ep2_d15_josh_letto_di_nascosto")
    s "How much?"
    c "I got to where she goes back inside."
    n "He says it quietly. She knows the line he stopped at. She'd read it out loud three times to get it to sound natural."
    c "I kept thinking about the jacket. At the party, Daniel gave you his jacket."
    s "Yes."
    c "So what am I supposed to think when I find that in there?"
    n "Sara looks at the mug. He's turned the handle towards her, the way he always does. She wants to ask whether he read her notes in the margins, too. She doesn't want to hear the answer."
    menu:
        "Tell him he had no right to read it.":
            $ cg("Sara turns to face Josh and defends her privacy", "images/cg/ep2/d15_04a_confronto.webp")
            s "I wrote her going back to him. To the man she's going to marry. You read that part."
            c "She still wanted the other man."
            s "She did. And I could have written her kissing him. I could have written her going home with him. You still had no right to read it."
            c "Would you have shown me if I'd asked?"
            s "I might have. I'd have liked the chance to decide."
            n "[nome_compagno] reaches for the mug, then leaves it where it is."
            c "I just want to know if I should be worried."
            s "You keep asking me to explain a woman I made up. I'm sitting right here telling you what you did to me."
            n "For a moment she thinks he might sit down. Then he takes his hand off the chair."
            c "I'll leave you to it."
            s "Please do."
            $ interest("josh", -7, "Sara confronted him about reading her draft.")
            $ segna("ep2_d15_litigio_josh")
            call ep2_d15_daniel
        "Let it go.":
            $ interest("josh", -3, "He read Sara’s draft without permission.")
            $ confidence(-10, "Sara let the intrusion pass.")
            n "Sara starts to ask what gave him the right. She sees how tired he looks and lets the first word die in her mouth."
            s "She goes back to her fiancé. That's where I ended it."
            c "I know. I just couldn't stop thinking about how she got there."
            s "It's a draft. I change things all the time."
            n "She makes it easy for him to take that as an answer. He does."
            c "Do you want me to stay up with you?"
            s "Go on to bed. I've got a little more to do."
            $ cg("Josh rests his hand on Sara’s shoulder before leaving", "images/cg/ep2/d15_04b_lascia_correre.webp")
            n "His hand rests briefly on her shoulder before he goes. She almost puts hers over it. After the door closes, she can still feel the weight of it."
    $ cg("Sara selects the ending in her manuscript", "images/cg/ep2/d15_06_revisione.webp")
    n "Sara finds the line she'd read out loud three times."
    $ cg("In the original ending the heroine takes her fiancé’s hand", "images/cg/ep2/d15_06a_romanzo_prima.webp")
    n "{i}She went back inside and took her fiancé's hand. His palm was warm. It was the one thing all evening she hadn't had to think about.{/i}"
    $ cg("Sara returns to the manuscript and deletes the ending", "images/cg/ep2/d15_06_revisione.webp")
    n "The warmth is right. Sara likes that about the line. She selects it anyway, along with the rest of the paragraph. For a second there's nothing below the last line of dialogue."
    $ cg("In the revised ending the heroine kisses the stranger on the terrace", "images/cg/ep2/d15_06b_romanzo_dopo.webp")
    n "{i}Her fiancé was still inside. She could see him through the glass, laughing with his head tipped back. She loved that laugh. She could have crossed the room and put a hand on his back and gone home with him.{/i}"
    n "{i}She turned to the man beside her, took his face in her hands and kissed him. When she pulled back, she told him where to meet her tomorrow. She could already hear herself telling her fiancé she'd be working late. She let the lie settle, then leaned in for another kiss.{/i}"
    $ cg("Sara rereads the new ending at her laptop", "images/cg/ep2/d15_06_revisione.webp")
    n "Sara reads the new ending with her lips barely moving. The woman can see both men from where she's standing. Sara leaves her there, knowing which one she'll go looking for tomorrow."
    n "The last line fits on page fifty. Sara attaches the pages to a message for Magnus, checks the attachment, and hits send."
    $ segna("ep2_d15_manoscritto_rivisto")
    $ segna("ep2_pagine_magnus")
    $ cg("Sara opens the sent copy of the manuscript", "images/cg/ep2/d15_07_invio.webp")
    n "{i}Dear Magnus, here are the first fifty pages, as promised. Thank you for asking to see them. Sara Collins.{/i}"
    $ confidence(2, "Sara sent her manuscript to Magnus.")
    $ interest("editore", 1, "Sara sent Magnus the first fifty pages.")
    n "She opens the sent copy. There it is, under her own name. Someone she hasn't known all her life is going to read past the first page."
    $ via_cg()
    return

label ep2_d15_daniel:
    $ cg("Sara confirms Thursday lunch with Daniel", "images/cg/ep2/d15_05_daniel.webp")
    $ chat_aperta = "daniel"
    show screen telefono_chat("daniel")
    n "The last message on the screen is his. Sara scrolls just far enough to see the reply box. Her hands are still warm from the argument. She types before they cool."
    $ msg("sara", "Thursday. I can do lunch. I\'d like to.", premia_avvio=False)
    $ segna("ep2_d18_pranzo_daniel_confermato")
    n "She sends it. A little later, while she’s reading the same sentence on page forty-nine for the fourth time, the phone lights up."
    $ suono("telefono_vibra")
    $ cg("Sara smiles as she reads Daniel’s reply", "images/cg/ep2/d15_05a_daniel_risposta.webp")
    $ msg("daniel", "Thursday it is. You ought to say what you\'d like more often, Sara. Give people a chance to hear it before you start worrying what they\'ll think.")
    hide screen telefono_chat
    $ chat_aperta = None
    n "Sara reads that second sentence again. Daniel has no idea what happened ten minutes ago. For a moment she wishes he did."
    if fatto("ep1_d13_pranzo_no"):
        sp "I said I’d tell [nome_compagno]. I still will."
    return
