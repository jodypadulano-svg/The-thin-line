## =============================================================================
## DANIEL — discorsi al telefono: introduzione, A (conoscenti), B (confidenza)
## =============================================================================
## Tono (Q&A 18/11/2026): sicuro, brillante, messaggi brevi, niente emoticon.
## Piccole frecciate su Josh già da A: difenderlo -> Josh +1; lasciar correre ->
## niente; riderci su -> risposta calda per Daniel e Corruption +1.
## Daniel scrive per primo già dal numero (giorno 13): l'introduzione ha l'entrata.

init python:
    discorso("daniel_intro", "daniel", ESTRANEI, scrive_lui=True)
    discorso("daniel_a1", "daniel", CONOSCENTI)
    discorso("daniel_a2", "daniel", CONOSCENTI)
    discorso("daniel_a3", "daniel", CONOSCENTI)
    discorso("daniel_a4", "daniel", CONOSCENTI)
    discorso("daniel_a5", "daniel", CONOSCENTI)
    discorso("daniel_a6", "daniel", CONOSCENTI)
    discorso("daniel_a7", "daniel", CONOSCENTI)
    discorso("daniel_a8", "daniel", CONOSCENTI)
    discorso("daniel_b1", "daniel", CONFIDENZA)
    discorso("daniel_b2", "daniel", CONFIDENZA)
    discorso("daniel_b3", "daniel", CONFIDENZA)
    discorso("daniel_b4", "daniel", CONFIDENZA)
    discorso("daniel_b5", "daniel", CONFIDENZA)


## --- Introduzione: il romanzo e il primo messaggio ---------------------------

label chat_daniel_intro:
    $ msg("sara", "Good evening. It's Sara. You asked for my number for Magnus... here I am.")
    return

label chat_daniel_intro_entrata:
    $ msg("daniel", "Daniel. I promised Magnus I'd follow up on the novel. So: how many pages do you have?")
    $ msg("sara", "Good evening to you too. About a hundred and twenty.")
    return

label chat_daniel_intro_1:
    $ msg("daniel", "A hundred and twenty pages and you hide them in a drawer. Typical.")
    $ msg("daniel", "Talent always apologises for existing. Mediocrity never does.")
    sp "Is that a compliment? It sounds like a lecture."
    menu (screen="scelta_telefono"):
        "«I'm not hiding them. I'm finishing them.»":
            $ msg("sara", "I'm not hiding them. I'm finishing them.")
            $ caldo()
            $ msg("daniel", "Good answer. Keep that tone with Magnus.")
        "«Thank you for introducing me to him.»":
            $ msg("sara", "Thank you for introducing me to him.")
            $ msg("daniel", "Don't thank me. I don't do favours. I make investments.")
    return

label chat_daniel_intro_2:
    $ msg("daniel", "Did [nome_compagno] read them?")
    menu (screen="scelta_telefono"):
        "«Of course. He loves them.»":
            $ msg("sara", "Of course. He loves them.")
            $ interest("josh", 1)
            $ msg("daniel", "Of course he does. He loves everything you do. That's not a review, that's a reflex.")
        "«Not yet. He's always tired.»":
            $ msg("sara", "Not yet. He's always tired.")
            $ msg("daniel", "Tired. Yes, I've noticed. Goodnight, Sara.")
            sp "Why did I tell him that?"
    return


## --- A1: il libro di Sara ----------------------------------------------------

label chat_daniel_a1:
    $ msg("sara", "You said talent hides. What makes you think I have any? You haven't read a line.")
    return

label chat_daniel_a1_1:
    $ msg("daniel", "I watched you talk about it at dinner. Your voice changed.")
    $ msg("daniel", "People lie about many things. Not about what makes their voice change.")
    menu (screen="scelta_telefono"):
        "«That's a very clever line.»":
            $ msg("sara", "That's a very clever line.")
            $ msg("daniel", "I have many. That one happens to be true.")
        "«What is it about, then? Guess.»" (confidence=25):
            $ msg("sara", "What is it about, then? Guess.")
            $ caldo()
            $ msg("daniel", "A woman who wants more than she's allowed to want.")
            sp "...How?"
    return

label chat_daniel_a1_2:
    $ msg("daniel", "Send me the first page. One page. I'll tell you if it's alive.")
    menu (screen="scelta_telefono"):
        "«Not a chance. Not yet.»":
            $ msg("sara", "Not a chance. Not yet.")
            $ msg("daniel", "Good. Make me wait. It's a sign of quality.")
        "«One page. Be honest.»":
            $ msg("sara", "One page. Be honest.")
            $ caldo()
            $ segna("daniel_prima_pagina")
            $ msg("daniel", "...")
            $ msg("daniel", "Alive. Annoyingly so. Cut the second sentence, it's apologising again.")
    return


## --- A2: l'ambizione professionale (frecciata) -------------------------------

label chat_daniel_a2:
    $ msg("sara", "Can I ask how you got where you are? Everyone at that dinner was terrified of you.")
    return

label chat_daniel_a2_1:
    $ msg("daniel", "I decided at twenty-five that I would never ask permission again.")
    $ msg("daniel", "The rest was just paperwork.")
    menu (screen="scelta_telefono"):
        "«That sounds lonely.»":
            $ msg("sara", "That sounds lonely.")
            $ msg("daniel", "It sounds free. People confuse the two all the time.")
        "«I wish I had that.»":
            $ msg("sara", "I wish I had that.")
            $ caldo()
            $ msg("daniel", "You do. You just keep it on a leash.")
    return

label chat_daniel_a2_2:
    $ msg("daniel", "Some people ask permission their whole life. Some even ask permission to take a day off.")
    $ msg("daniel", "Your [nome_compagno] sent me a three-paragraph email to leave at five on Friday.")
    sp "That's cruel. And it's exactly the kind of thing he'd do."
    menu (screen="scelta_telefono"):
        "«He's polite. That's not a flaw.»":
            $ msg("sara", "He's polite. That's not a flaw.")
            $ interest("josh", 1)
            $ msg("daniel", "Loyal. I like that in you. Less in him.")
        "(Let it slide.)":
            $ msg("sara", "...")
            $ msg("daniel", "Silence. Smart.")
        "«Three paragraphs? Really?»":
            $ msg("sara", "Three paragraphs? Really?")
            $ caldo()
            $ corruption(1)
            $ msg("daniel", "With a bullet list. I'm framing it.")
    return


## --- A3: ristoranti eleganti -------------------------------------------------

label chat_daniel_a3:
    $ msg("sara", "That restaurant on Thursday. Is it always like that, or did you book the whole place to impress?")
    return

label chat_daniel_a3_1:
    $ msg("daniel", "I never need to impress. I just refuse to eat badly.")
    $ msg("daniel", "Did you like it?")
    menu (screen="scelta_telefono"):
        "«The food was perfect. The company was... intense.»":
            $ msg("sara", "The food was perfect. The company was... intense.")
            $ caldo()
            $ msg("daniel", "Intense. I'll take it.")
        "«A bit too formal for me.»":
            $ msg("sara", "A bit too formal for me.")
            $ msg("daniel", "Formal is a costume. You wore it well.")
    return

label chat_daniel_a3_2:
    $ msg("daniel", "There's a place by the harbour. No menu. The chef decides. You'd love it.")
    sp "Is he inviting me? No. He's just... describing."
    menu (screen="scelta_telefono"):
        "«I'll tell [nome_compagno]. Maybe for our anniversary.»":
            $ msg("sara", "I'll tell [nome_compagno]. Maybe for our anniversary.")
            $ msg("daniel", "Do. Tell him to book three months ahead. And to let you order.")
        "«No menu? That sounds like you.»":
            $ msg("sara", "No menu? That sounds like you.")
            $ caldo()
            $ msg("daniel", "Everything good sounds like me.")
    return


## --- A4: automobili (frecciata) ----------------------------------------------

label chat_daniel_a4:
    $ msg("sara", "Was that your car outside the restaurant? The black one that looked like a spaceship?")
    return

label chat_daniel_a4_1:
    $ msg("daniel", "It's not a spaceship. It's a reminder.")
    $ msg("daniel", "Every morning I see it and I remember what I worked for.")
    menu (screen="scelta_telefono"):
        "«Most people use a photo for that.»":
            $ msg("sara", "Most people use a photo for that.")
            $ caldo()
            $ msg("daniel", "Most people don't have anything worth photographing.")
        "«It's very... loud.»":
            $ msg("sara", "It's very... loud.")
            $ msg("daniel", "So am I. We understand each other.")
    return

label chat_daniel_a4_2:
    $ msg("daniel", "What does [nome_compagno] drive? Wait. Let me guess. Something sensible. Grey. Good mileage.")
    menu (screen="scelta_telefono"):
        "«It gets us everywhere. That's what matters.»":
            $ msg("sara", "It gets us everywhere. That's what matters.")
            $ interest("josh", 1)
            $ msg("daniel", "Everywhere he's allowed to go, yes.")
        "(Don't answer.)":
            $ msg("sara", "...")
            $ msg("daniel", "I'll take that as a «grey».")
        "«...It's grey.»":
            $ msg("sara", "...It's grey.")
            $ caldo()
            $ corruption(1)
            $ msg("daniel", "Of course it is.")
            sp "I shouldn't have laughed. I did laugh."
    return


## --- A5: viaggi di lusso -----------------------------------------------------

label chat_daniel_a5:
    $ msg("sara", "[nome_compagno] says you're never in the office on Mondays. Where do you go?")
    return

label chat_daniel_a5_1:
    $ msg("daniel", "Wherever the weekend didn't finish.")
    $ msg("daniel", "Last week, the coast. A hotel where they bring breakfast to the terrace and nobody says a word.")
    menu (screen="scelta_telefono"):
        "«Must be nice.»":
            $ msg("sara", "Must be nice.")
            $ msg("daniel", "It is. That's the point.")
        "«I've never stayed anywhere like that.»":
            $ msg("sara", "I've never stayed anywhere like that.")
            $ caldo()
            $ msg("daniel", "You should. Some women look different with the sea behind them.")
            sp "Some women. Not me. Right?"
    return

label chat_daniel_a5_2:
    $ msg("daniel", "Where would you go? Money is not a question. Answer fast.")
    menu (screen="scelta_telefono"):
        "«Somewhere quiet. With books.»":
            $ msg("sara", "Somewhere quiet. With books.")
            $ msg("daniel", "A writer's answer. Predictable and correct.")
        "«Somewhere nobody knows me.»" (confidence=25):
            $ msg("sara", "Somewhere nobody knows me.")
            $ caldo()
            $ msg("daniel", "Now that's interesting. Who would you be there?")
            $ msg("sara", "I don't know yet.")
    return


## --- A6: gusti musicali ------------------------------------------------------

label chat_daniel_a6:
    $ msg("sara", "What was the music at dinner? Everyone was too scared to ask you.")
    return

label chat_daniel_a6_1:
    $ msg("daniel", "Jazz. Old jazz. Musicians who were drunk, broke and better than anyone alive today.")
    menu (screen="scelta_telefono"):
        "«I don't know anything about jazz.»":
            $ msg("sara", "I don't know anything about jazz.")
            $ msg("daniel", "Nobody does. That's why it works.")
        "«It was beautiful. Send me something.»":
            $ msg("sara", "It was beautiful. Send me something.")
            $ caldo()
            $ msg("daniel", "(A track: a slow saxophone, almost a whisper.)")
            $ msg("daniel", "Listen to it at night. Not in the car.")
            $ segna("daniel_jazz")
    return

label chat_daniel_a6_2:
    $ msg("daniel", "What do you listen to?")
    menu (screen="scelta_telefono"):
        "«Whatever's on the radio, honestly.»":
            $ msg("sara", "Whatever's on the radio, honestly.")
            $ msg("daniel", "Honesty. Rare. Terrible taste, but rare.")
        "«Sad songs. When nobody's around.»":
            $ msg("sara", "Sad songs. When nobody's around.")
            $ caldo()
            $ msg("daniel", "Everyone interesting does.")
    return


## --- A7: il valore del successo (frecciata) ----------------------------------

label chat_daniel_a7:
    $ msg("sara", "Do you ever stop? Working, I mean. [nome_compagno] says you answer emails at three in the morning.")
    return

label chat_daniel_a7_1:
    $ msg("daniel", "Success isn't a job. It's a temperature. You either have it or you're cold.")
    sp "Who talks like that? He does. And it works on people."
    menu (screen="scelta_telefono"):
        "«That's a sad way to live.»":
            $ msg("sara", "That's a sad way to live.")
            $ msg("daniel", "Sad is a word invented by people who settled.")
        "«And what's my temperature?»" (confidence=25):
            $ msg("sara", "And what's my temperature?")
            $ caldo()
            $ msg("daniel", "Rising. You just haven't noticed.")
    return

label chat_daniel_a7_2:
    $ msg("daniel", "Your [nome_compagno] is very good at his job. Very good. Exactly as good as he needs to be, and not one bit more.")
    menu (screen="scelta_telefono"):
        "«He's better than you think.»":
            $ msg("sara", "He's better than you think.")
            $ interest("josh", 1)
            $ msg("daniel", "Then he's hiding it very well. I'll keep looking.")
        "(Let it go.)":
            $ msg("sara", "...")
            $ msg("daniel", "Goodnight.")
        "«That's... horribly accurate.»":
            $ msg("sara", "That's... horribly accurate.")
            $ caldo()
            $ corruption(1)
            $ msg("daniel", "I'm always accurate. Horrible is optional.")
    return


## --- A8: battute sul lavoro (frecciata) --------------------------------------

label chat_daniel_a8:
    $ msg("sara", "Long day at the paper. My editor wants me to rewrite a piece for the third time.")
    return

label chat_daniel_a8_1:
    $ msg("daniel", "Third time. Is it the piece or is it the editor?")
    menu (screen="scelta_telefono"):
        "«The editor. Definitely.»":
            $ msg("sara", "The editor. Definitely.")
            $ caldo()
            $ msg("daniel", "Then rewrite it once more, perfectly, and make her feel stupid.")
        "«Probably me.»":
            $ msg("sara", "Probably me.")
            $ msg("daniel", "Stop that. It's an ugly habit.")
    return

label chat_daniel_a8_2:
    $ msg("daniel", "We had a long day too. [nome_compagno] presented the quarterly report.")
    $ msg("daniel", "He did very well. He only dropped the clicker twice.")
    menu (screen="scelta_telefono"):
        "«Leave him alone, Daniel.»":
            $ msg("sara", "Leave him alone, Daniel.")
            $ interest("josh", 1)
            $ msg("daniel", "I always leave him alone. That's the problem.")
        "(Don't reply.)":
            $ msg("sara", "...")
            $ msg("daniel", "Read. No answer. You're learning.")
        "«Twice?»":
            $ msg("sara", "Twice?")
            $ caldo()
            $ corruption(1)
            $ msg("daniel", "The second time, it slid under the projector. It took two interns to get it out.")
            sp "Poor [nome_compagno]. Why am I smiling?"
    return


## --- B1: cosa rende attraente un uomo ----------------------------------------

label chat_daniel_b1:
    $ msg("sara", "Settle a bet. Joanie says confidence is the most attractive thing in a man. I say kindness.")
    return

label chat_daniel_b1_entrata:
    $ msg("daniel", "A question for a writer. What makes a man attractive? You must have an opinion. You write them.")
    $ msg("sara", "Kindness. Joanie says confidence.")
    return

label chat_daniel_b1_1:
    $ msg("daniel", "Joanie wins. Kindness is what women say. Confidence is what women choose.")
    menu (screen="scelta_telefono"):
        "«That's arrogant.»":
            $ msg("sara", "That's arrogant.")
            $ msg("daniel", "It's statistics. Arrogance is just statistics with good posture.")
        "«Maybe. Sometimes.»":
            $ msg("sara", "Maybe. Sometimes.")
            $ caldo()
            $ msg("daniel", "Sometimes is how it always starts.")
    return

label chat_daniel_b1_2:
    $ msg("daniel", "Think about the men in your stories. Are they kind?")
    sp "...They're not. None of them."
    menu (screen="scelta_telefono"):
        "«Some of them.»":
            $ msg("sara", "Some of them.")
            $ msg("daniel", "The ones nobody remembers.")
        "«...No. They're not.»":
            $ msg("sara", "...No. They're not.")
            $ caldo()
            $ msg("daniel", "I know. I could tell from the first page.")
    return


## --- B2: la sicurezza in sé (frecciata) --------------------------------------

label chat_daniel_b2:
    $ msg("sara", "How do you do it? Walk into a room like you own it?")
    return

label chat_daniel_b2_1:
    $ msg("daniel", "I decide that I do. The room usually agrees.")
    $ msg("daniel", "You could do it too. You just need to stop checking if everyone is ok.")
    menu (screen="scelta_telefono"):
        "«Checking on people is called being nice.»":
            $ msg("sara", "Checking on people is called being nice.")
            $ msg("daniel", "It's called being on duty. You're not a nurse.")
        "«Teach me, then.»" (confidence=30):
            $ msg("sara", "Teach me, then.")
            $ caldo()
            $ msg("daniel", "Lesson one: next time someone talks over you, don't stop talking.")
            $ segna("daniel_lezione")
    return

label chat_daniel_b2_2:
    $ msg("daniel", "Confidence is contagious. So is the opposite. You live with the opposite.")
    menu (screen="scelta_telefono"):
        "«Don't talk about him like that.»":
            $ msg("sara", "Don't talk about him like that.")
            $ interest("josh", 1)
            $ msg("daniel", "Noted. You defend him beautifully. Someone has to.")
        "(Let it slide.)":
            $ msg("sara", "...")
        "«He's... getting better.»":
            $ msg("sara", "He's... getting better.")
            $ caldo()
            $ corruption(1)
            $ msg("daniel", "Getting. Better. Two words nobody wants on their gravestone.")
    return


## --- B3: le insoddisfazioni nascoste (frecciata) -----------------------------

label chat_daniel_b3:
    $ msg("sara", "Can I ask you something? Are you happy? Really?")
    return

label chat_daniel_b3_1:
    $ msg("daniel", "Happy is for people who stopped wanting. I haven't.")
    $ msg("daniel", "And you? Don't give me the dinner answer.")
    menu (screen="scelta_telefono"):
        "«I am happy.»":
            $ msg("sara", "I am happy.")
            $ msg("daniel", "Three words, no punctuation of doubt. Impressive. Almost convincing.")
        "«Mostly. There's... something missing. I don't know what.»":
            $ msg("sara", "Mostly. There's... something missing. I don't know what.")
            $ caldo()
            $ msg("daniel", "You know what. You just don't like the answer.")
    return

label chat_daniel_b3_2:
    $ msg("daniel", "Let me guess. Saturday night. Sofa. He falls asleep at ten. You stay up and write.")
    sp "Exactly that. Every Saturday."
    menu (screen="scelta_telefono"):
        "«He works hard. He's tired.»":
            $ msg("sara", "He works hard. He's tired.")
            $ interest("josh", 1)
            $ msg("daniel", "I make sure of it.")
            sp "What does that mean?"
        "(Don't answer.)":
            $ msg("sara", "...")
            $ msg("daniel", "That's a yes.")
        "«How do you know that?»":
            $ msg("sara", "How do you know that?")
            $ caldo()
            $ corruption(1)
            $ msg("daniel", "Because I've met him. And I've met you.")
    return


## --- B4: le donne che lo hanno colpito ---------------------------------------

label chat_daniel_b4:
    $ msg("sara", "Has any woman ever said no to you?")
    return

label chat_daniel_b4_1:
    $ msg("daniel", "One. At twenty-three. She married a dentist.")
    $ msg("daniel", "I still think about her every time I go to the dentist. Which is why I have perfect teeth.")
    menu (screen="scelta_telefono"):
        "«That's almost sweet.»":
            $ msg("sara", "That's almost sweet.")
            $ caldo()
            $ msg("daniel", "Don't spread it around.")
        "«Only one? I don't believe you.»":
            $ msg("sara", "Only one? I don't believe you.")
            $ msg("daniel", "Only one that mattered.")
    return

label chat_daniel_b4_2:
    $ msg("daniel", "The women who stay with me are the ones who surprise me. It doesn't happen often.")
    sp "Why do I want to ask if I surprised him?"
    menu (screen="scelta_telefono"):
        "«Good luck finding the next one.»":
            $ msg("sara", "Good luck finding the next one.")
            $ msg("daniel", "I don't need luck.")
        "«And what surprises you?»" (confidence=30):
            $ msg("sara", "And what surprises you?")
            $ caldo()
            $ msg("daniel", "A woman who says what she wants. Before I say it for her.")
    return


## --- B5: la differenza tra amore e desiderio ---------------------------------

label chat_daniel_b5:
    $ msg("sara", "Question for a cynic: do you believe in love?")
    return

label chat_daniel_b5_1:
    $ msg("daniel", "I believe in desire. Love is desire that got comfortable and bought a sofa.")
    menu (screen="scelta_telefono"):
        "«That's the saddest thing I've ever read.»":
            $ msg("sara", "That's the saddest thing I've ever read.")
            $ msg("daniel", "And yet you're still reading.")
        "«And what's wrong with a sofa?»":
            $ msg("sara", "And what's wrong with a sofa?")
            $ caldo()
            $ msg("daniel", "Nothing. Until you realise you're the only one still awake on it.")
    return

label chat_daniel_b5_2:
    $ msg("daniel", "You love him. I don't doubt it.")
    $ msg("daniel", "The question is: when was the last time you wanted him?")
    sp "I shouldn't answer that. I'm not going to answer that."
    menu (screen="scelta_telefono"):
        "«That's none of your business. Goodnight.»":
            $ msg("sara", "That's none of your business. Goodnight.")
            $ interest("josh", 1)
            $ msg("daniel", "Goodnight, Sara.")
        "«...Goodnight, Daniel.»":
            $ msg("sara", "...Goodnight, Daniel.")
            $ caldo()
            $ corruption(1)
            $ segna("daniel_domanda_desiderio")
            $ msg("daniel", "That's an answer too.")
    return
