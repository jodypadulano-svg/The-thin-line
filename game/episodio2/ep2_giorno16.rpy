default interest_hugo = 0

define mark = Character("Mark", color="#a9b9dd")

label ep2_d16:
    call nuovo_giorno(16, "Tuesday Dinner")
    $ fascia_corrente = FASCE.index("lavoro")
    call ep2_d16_redazione
    $ fascia_corrente = FASCE.index("sera")
    call ep2_d16_hugo
    call ep2_d16_cena
    $ fascia_corrente = FASCE.index("notte")
    call ep2_d16_retroscena
    call ep2_d16_telefono
    $ musica(None)
    $ luogo_corrente = ""
    scene bg nero with fade
    return

label ep2_d16_redazione:
    $ vai("redazione", "The newsroom — Tuesday morning")
    $ musica("redazione")
    $ cg("Jessica brings Sara a sugar packet", "images/cg/ep2/d16_01_jessica_caffe.webp")
    je "Have you got a minute?"
    s "Depends. Are you about to ask me to do the horoscopes again?"
    je "No. I was thinking about what I told you that day. About the really good thing that happened to me."
    n "Sara remembers the book Jessica used to carry in her bag. Once she'd saved Sara a seat at lunch just to finish their argument about Anna Karenina."
    s "I remember."
    je "I keep nearly bringing it up, and then there's always somebody here."
    menu:
        "Ask what happened to her.":
            s "Jess, what actually happened to you?"
            $ cg("Jessica looks down at the sugar packet", "images/cg/ep2/d16_01a_jessica_domanda.webp")
            je "Remember when you asked if I wanted to go for a drink after work, and I said I had to get home?"
            s "Which time?"
            je "Exactly. Half the time I went home and wished I'd come with you."
            s "You could've said yes."
            je "I know. It sounds easy when you say it."
            s "And now?"
            je "Now I can say yes while I still want to."
            s "What changed?"
            je "I can tell you how it feels. I'm still working out how to tell you what happened."
            s "All right. When you've worked it out, I'd like to hear it."
            je "Okay. I'd like that."
        "Let it go.":
            s "I'm glad you're happy, Jess."
            je "You always look a little worried when you say that."
            n "Sara blows on her coffee. Jessica watches her for another second, then smiles."
            je "Sorry. You've got a deadline, haven't you?"
            s "Eleven thirty. And I still need a headline."
            je "Read it to me when you've got one. You always know when it's wrong if you say it out loud."
    n "On her way back to her desk, Sara tries the headline under her breath. At the third word she stops. That's the one she'll cut."
    $ via_cg()
    return

label ep2_d16_hugo:
    $ vai("casa", "Home — Tuesday afternoon")
    $ musica("casa")
    $ cg("Hugo stops by for Sunday's roasting dish", "images/cg/ep2/d16_02_hugo_teglia.webp")
    hugo "I came for the roasting dish. How's [nome_compagno]?"
    menu:
        "Answer and say goodbye.":
            s "He's still at work. I'll tell him you stopped by."
            hugo "Thanks, Sara."
        "Stay and talk a minute.":
            if fatto("ep2_d15_litigio_josh"):
                s "He seemed all right this morning. Better than he was after we fought, anyway."
                hugo "What did you fight about?"
                s "He sat down and read my draft without asking. I told him he had no right."
                $ cg("Hugo takes Sara's side", "images/cg/ep2/d16_02a_hugo_difende_sara.webp")
                hugo "He didn't. If he wanted to read it, he should have asked you."
                n "Sara had been waiting for him to make an excuse for his son. She looks up at Hugo. She likes how sure he sounds."
                $ interest_hugo += 1
                n "Hugo sets the dish down and pulls out the chair beside her."
                hugo "Put your bag down. Sit here."
                menu:
                    "Put the bag down and sit.":
                        $ cg("Sara sits exactly where Hugo indicated", "images/cg/ep2/d16_02b_sara_obbedisce.webp")
                        n "Sara slips the bag off her shoulder at once. She sets it beside her feet, sits exactly where Hugo indicated and places both hands in her lap."
                        s "Yes, Hugo."
                        $ interest_hugo += 2
                        n "She looks up and waits for him to speak. She hadn't expected to like the feeling of doing exactly as he asked."
                        hugo "You told him straight. Good."
                        n "Sara stays seated until Hugo picks up the dish to leave."
                    "Stay on your feet.":
                        s "I'd better get started on dinner. We've got people coming."
                        hugo "All right. Have a good evening."
            else:
                s "He's at work. We're having friends over later."
                hugo "Then I'd better get this out of your way. Have a good evening."
    n "Hugo takes the dish with him when he leaves."
    $ via_cg()
    return

label ep2_d16_cena:
    $ vai("casa", "Home — Tuesday evening")
    $ cg("Joanie introduces Mark at the door", "images/cg/ep2/d16_03_arrivo_mark.webp")
    n "The bell catches [nome_compagno] looking for the trivet. Sara lifts the dish to show him it's already underneath."
    c "I've been looking for that for five minutes."
    s "I know. I wanted to see where you'd look next."
    if fatto("ep2_d15_litigio_josh"):
        c "Are we all right to do this tonight?"
        s "I'd like to see them. We can talk about yesterday another time."
        c "All right."
    else:
        c "I left the end of the table clear. In case you want to write after they go."
        s "I sent the pages last night."
        c "Oh. You did it, then."
        s "Yeah. I did."
    ch "Mark, this is Sara. Sara, this is Mark. I've been telling each of you about the other one for years, so please agree with everything I've said."
    mark "I only remember the nice parts."
    s "How much did she have to leave out?"
    mark "She told me you once left a birthday party to take a spider outside."
    s "It was in my glass."
    ch "She took the glass with her. We had to explain it to the bar."
    n "Mark laughs and shakes [nome_compagno]'s hand. Then something hisses in the oven."
    c "Could you open that window?"
    n "Mark opens it and passes him the oven gloves. A moment later they're both bent over the dish."
    mark "Which bits are we calling crispy?"
    c "Everything on your half."
    mark "Good. I like crispy."
    $ cg("Mark asks Sara about her novel", "images/cg/ep2/d16_04_tavolata.webp")
    n "After dinner, Mark and [nome_compagno] discover they've both lost an entire Saturday to the same model of bookcase."
    mark "Did you put the back on before you noticed?"
    c "I'd put the books in."
    n "Mark puts his glass down to laugh. By the time he recovers, [nome_compagno] can't finish the sentence either."
    n "Darius puts the two biscuit packets he brought on the table. One has Sara's name in black marker."
    dr "There. Evidence."
    s "You actually did it."
    dr "I did. I also checked the name was still on there after I'd eaten one."
    mark "Joanie says you're writing a book. How's it going?"
    s "I sent the first fifty pages to an editor last night."
    mark "Fifty? That's a lot of pages to let out of the house."
    s "It felt like it when I pressed send."
    mark "How'd you know they were ready?"
    n "Sara thinks of the last line. Of the woman who'll have to find a reason to go out again."
    menu:
        "Stay close to [nome_compagno].":
            $ cg("Sara puts a hand on Josh's sleeve", "images/cg/ep2/d16_04a_vicina_josh.webp")
            s "I read the last page out loud. I could hear where I wanted it to stop."
            n "Sara moves a little closer and rests her hand on his sleeve."
            if fatto("ep2_d15_litigio_josh"):
                c "I wanted to ask you how it went."
                s "You can ask."
                c "How did it feel?"
                s "Good. I opened the sent copy just to see my name on it."
                c "I'd have done that twice."
            else:
                c "Did you change much last night?"
                s "Enough that I was glad I stayed up."
                c "I'm glad you sent it."
                n "He covers her hand with his. The relief arrives before Sara has decided what to do with it."
            $ interest("josh", 1)
        "Laugh with Darius.":
            $ cg("Darius slides Sara a napkin while she laughs", "images/cg/ep2/d16_04b_risata_darius.webp")
            n "Sara takes a biscuit from the blue packet. Darius catches her before she can take a bite."
            dr "I want everyone to know I was right about this on Sunday."
            s "I'm checking you bought the right ones."
            dr "You picked those up without even looking."
            n "Sara laughs so suddenly she has to put the biscuit down. Darius pushes a napkin toward her."
            s "I knew I was ready when I had something I actually wanted somebody to read."
            mark "And now you have to wait for him to read it."
            s "That's the part I hadn't thought through."
            n "Later, as they pass plates toward the sink, Darius leans close enough to be heard over the others."
            dr "Did she get her minute?"
            n "Sara remembers the room beyond the door."
            s "She did. It ended up being almost a whole page."
            dr "Good. I liked hearing you talk about that bit."
            $ segna("phone_d16_darius_page")
            $ interest("amico", 1)
        "Confide in Joanie in the kitchen.":
            s "I knew I could keep changing it until Thursday and I'd still find something to change on Thursday."
            n "Sara picks up the empty jug and touches Joanie's elbow on the way past."
            $ cg("Joanie listens while filling the jug", "images/cg/ep2/d16_05_confidenza_joanie.webp")
            ch "What happened?"
            s "[nome_compagno] read the draft last night. It was open on my laptop. He sat down and read it."
            $ segna("phone_d16_joanie_draft")
            ch "Did he tell you?"
            s "He asked me about a scene. Took me a second to work out how he knew it."
            if fatto("ep2_d15_litigio_josh"):
                ch "What did you say?"
                s "I told him he had no right to read it."
                if fatto("ep2_d18_pranzo_daniel_confermato"):
                    s "Then, after he left the room, I told Daniel I'd have lunch with him on Thursday."
                    ch "You said yes?"
                    s "I said I'd like to. I nearly took that bit out before I sent it."
                    ch "And now that it's Tuesday?"
                    s "I still want to go. I wish I knew what I was going to say when I got there."
                    if fatto("ep1_d13_pranzo_no"):
                        s "I still have to tell [nome_compagno]. I said I would."
                        ch "Do you want to do it tonight?"
                        s "I'll talk to him before Thursday. I want to do it when we're on our own."
            else:
                ch "Did you tell him it bothered you?"
                s "I told him it was a draft. He went to bed thinking we'd finished talking about it."
                ch "Had you?"
                s "I thought I had. Then Mark asked about the book, and for a second I was waiting for [nome_compagno] to answer."
                ch "I heard you answer."
            mark "I can hear running water. Are you two washing up without me?"
            ch "We're talking about you, darling."
            mark "Oh, carry on, then."
            $ interest("amica", 1)
    $ cg("Mark hands Josh back his phone", "images/cg/ep2/d16_06_mark_josh_saluti.webp")
    mark "Did you ever get the doors straight?"
    c "On the bookcase? No. If you catch it looking good, move your head a little to the left."
    mark "Send me a photo. I've got a spare hinge. Actually, give me your phone."
    n "Mark rings his own number and hands the phone back when he hears his pocket buzz."
    mark "There. Now you have to send me a photo. I want to see how bad it is."
    ch "He's going to come round here with a screwdriver next Tuesday. You've only yourselves to blame."
    c "He can come round with a screwdriver any Tuesday he likes."
    n "Sara takes her keys and walks them to the front door. Darius stays to help with the last of the glasses."
    $ via_cg()
    return

label ep2_d16_retroscena:
    call inizio_retroscena
    $ cg("Josh asks Darius about Jacob", "images/cg/ep2/d16_07_josh_darius_confidenza.webp")
    dr "You want me to go after this?"
    c "You can stay a minute."
    rs "[nome_compagno] puts the leftovers in the fridge, closes it and keeps his hand on the handle."
    c "Do you remember Jacob Trevor?"
    dr "Sara's ex?"
    c "Yeah."
    dr "Why?"
    c "I thought I'd forgotten something she said about him. Turns out I can remember exactly how she said it."
    $ cg("Sara holds Josh's hand in his memory", "images/cg/ep2/d16_08_ricordo_josh_sara.webp")
    rs "In his memory, they're sitting on the edge of the bed. One of Sara's shoes is still on. He's just asked what she missed about Jacob after four years together."
    s "For a while? The sex."
    rs "He nods. Sara gives a small, embarrassed laugh."
    s "You did ask."
    c "I know. Was it really that good?"
    s "Yeah. He was good in bed. For a long time, any time we were getting on, that was what we were doing."
    rs "He looks down at the shoe on the floor. Sara puts her hand on his."
    s "I wanted him to be faithful. I spent so long hoping he would be. By the end I was tired of listening for his phone."
    c "Do you ever miss being with him?"
    s "Sometimes I remember the good bits. I still know why I left. And I love you, [nome_compagno]. Today I bought two peaches and spent the whole walk home trying to remember if you even liked peaches. I wanted to bring you something you liked."
    c "I like peaches."
    s "I know. You ate both of them."
    rs "He smiles. Sara rests her head on his shoulder. He strokes her thumb, hoping he'll stop hearing the way she said yeah."
    $ cg("Josh looks down at his hands as Darius listens", "images/cg/ep2/d16_07a_josh_darius_segreto.webp")
    dr "Did you ever tell her it got to you?"
    c "She was trying so hard to make me feel loved. I thought it'd pass."
    dr "And did it?"
    c "Most days I don't think about him at all."
    rs "He hears the front door and lowers his voice."
    c "Tonight I wanted to tell somebody who wouldn't ask her about it."
    dr "All right. It stays here."
    call fine_retroscena
    n "Sara comes back in and puts down her keys. [nome_compagno] hands her the packet with her name on it."
    c "Better put these away before he comes back for them."
    dr "I can still hear you."
    n "Sara takes a biscuit and holds out the packet to Darius. [nome_compagno] waits for her to pass him the last one."
    $ via_cg()
    return

label ep2_d16_telefono:
    $ vai("casa", "Home — Late Tuesday evening")
    $ cg("Sara checks her phone at the writing table", "images/cg/ep2/d15_05_daniel.webp")
    n "Once Darius has gone, Sara changes out of her work clothes and takes her phone to the writing table."
    call telefono_nuovo_sessione("Go to bed")
    $ via_cg()
    return
