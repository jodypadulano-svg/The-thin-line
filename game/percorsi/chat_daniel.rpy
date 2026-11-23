## =============================================================================
## DANIEL — discorsi al telefono: introduzione, A (conoscenti), B (confidenza)
## =============================================================================
## Tono (Q&A 18/11/2026): sicuro, brillante, messaggi brevi, niente emoticon.
## Piccole frecciate su Josh già da A: difenderlo -> Josh +1; lasciar correre ->
## niente; riderci su -> risposta calda per Daniel e Corruption +1.
## Daniel scrive per primo già dal numero (giorno 13): l'introduzione ha l'entrata.

init python:
    discorso("daniel_intro", "daniel", ESTRANEI, scrive_lui=True)
    discorso("daniel_a1", "daniel", CONOSCENTI, se="fatto('chat_daniel_intro')")
    discorso("daniel_a2", "daniel", CONOSCENTI)
    discorso("daniel_a3", "daniel", CONOSCENTI)
    discorso("daniel_a4", "daniel", CONOSCENTI)
    discorso("daniel_a5", "daniel", CONOSCENTI)
    discorso("daniel_a6", "daniel", CONOSCENTI)
    discorso("daniel_a7", "daniel", CONOSCENTI)
    discorso("daniel_a8", "daniel", CONOSCENTI, se="fatto('ep2_relazione_trimestrale_josh') == giorno")
    discorso("daniel_b1", "daniel", CONFIDENZA)
    discorso("daniel_b2", "daniel", CONFIDENZA)
    discorso("daniel_b3", "daniel", CONFIDENZA)
    discorso("daniel_b4", "daniel", CONFIDENZA)
    discorso("daniel_b5", "daniel", CONFIDENZA)


## --- Introduzione: il romanzo e il primo messaggio ---------------------------

label chat_daniel_intro:
    label tel_chat_daniel_intro_1:
    if telefono_minuti_blocco("tel_chat_daniel_intro_1", "invia", 1):
        return
    $ msg("sara", "I saw your message after the party. Can we talk about the novel?")
    return

label chat_daniel_intro_entrata:
    label tel_chat_daniel_intro_entrata_1:
    if telefono_minuti_blocco("tel_chat_daniel_intro_entrata_1", "ricevi", 1):
        return
    $ msg("daniel", "I promised Magnus I'd follow up on the novel. So: how many pages do you have?")
    label tel_chat_daniel_intro_entrata_2:
    if telefono_minuti_blocco("tel_chat_daniel_intro_entrata_2", "invia", 1):
        return
    $ msg("sara", "Good evening to you too. About a hundred and twenty.")
    return

label chat_daniel_intro_1:
    label tel_chat_daniel_intro_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_intro_1_1", "ricevi", 2):
        return
    $ msg("daniel", "A hundred and twenty pages and you hide them in a drawer. Typical.")
    $ msg("daniel", "Talent always apologises for existing. Mediocrity never does.")
    sp "Is that a compliment? It sounds like a lecture."
    label tel_chat_daniel_intro_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_intro_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm not hiding them. I'm finishing them.»":
            label tel_chat_daniel_intro_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_intro_1_3", "invia", 1):
                return
            $ msg("sara", "I'm not hiding them. I'm finishing them.")
            $ caldo()
            label tel_chat_daniel_intro_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_intro_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Good answer. Keep that tone with Magnus.")
        "«Thank you for introducing me to him.»":
            label tel_chat_daniel_intro_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_intro_1_5", "invia", 1):
                return
            $ msg("sara", "Thank you for introducing me to him.")
            label tel_chat_daniel_intro_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_intro_1_6", "ricevi", 1):
                return
            $ msg("daniel", "Don't thank me. I don't do favours. I make investments.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_intro_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_intro_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_intro_2:
    label tel_chat_daniel_intro_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_intro_2_1", "ricevi", 1):
        return
    $ msg("daniel", "Did [nome_compagno] read them?")
    label tel_chat_daniel_intro_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_intro_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Of course. He loves them.»":
            label tel_chat_daniel_intro_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_intro_2_3", "invia", 1):
                return
            $ msg("sara", "Of course. He loves them.")
            $ interest("josh", 1)
            label tel_chat_daniel_intro_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_intro_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Of course he does. He loves everything you do. That's not a review, that's a reflex.")
        "«Not yet. He's always tired.»":
            label tel_chat_daniel_intro_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_intro_2_5", "invia", 1):
                return
            $ msg("sara", "Not yet. He's always tired.")
            label tel_chat_daniel_intro_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_intro_2_6", "ricevi", 1):
                return
            $ msg("daniel", "Tired. Yes, I've noticed. Goodnight, Sara.")
            sp "Why did I tell him that?"
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_intro_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_intro_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A1: il libro di Sara ----------------------------------------------------

label chat_daniel_a1:
    label tel_chat_daniel_a1_1:
    if telefono_minuti_blocco("tel_chat_daniel_a1_1", "invia", 1):
        return
    $ msg("sara", "You said talent hides. What makes you think I have any? You haven't read a line.")
    return

label chat_daniel_a1_1:
    label tel_chat_daniel_a1_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_a1_1_1", "ricevi", 2):
        return
    $ msg("daniel", "I watched you talk about it at the party. Your voice changed.")
    $ msg("daniel", "People lie about many things. Not about what makes their voice change.")
    label tel_chat_daniel_a1_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_a1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's a very clever line.»":
            label tel_chat_daniel_a1_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_a1_1_3", "invia", 1):
                return
            $ msg("sara", "That's a very clever line.")
            label tel_chat_daniel_a1_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_a1_1_4", "ricevi", 1):
                return
            $ msg("daniel", "I have many. That one happens to be true.")
        "«What is it about, then? Guess.»" (confidence=25):
            label tel_chat_daniel_a1_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_a1_1_5", "invia", 1):
                return
            $ msg("sara", "What is it about, then? Guess.")
            $ caldo()
            label tel_chat_daniel_a1_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_a1_1_6", "ricevi", 1):
                return
            $ msg("daniel", "A woman who wants more than she's allowed to want.")
            sp "...How?"
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_a1_2:
    label tel_chat_daniel_a1_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_a1_2_1", "ricevi", 1):
        return
    $ msg("daniel", "Send me the first page. One page. I'll tell you if it's alive.")
    label tel_chat_daniel_a1_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_a1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Not a chance. Not yet.»":
            label tel_chat_daniel_a1_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_a1_2_3", "invia", 1):
                return
            $ msg("sara", "Not a chance. Not yet.")
            label tel_chat_daniel_a1_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_a1_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Good. Make me wait. It's a sign of quality.")
        "«One page. Be honest.»":
            label tel_chat_daniel_a1_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_a1_2_5", "invia", 1):
                return
            $ msg("sara", "One page. Be honest.")
            $ caldo()
            $ segna("daniel_prima_pagina")
            label tel_chat_daniel_a1_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_a1_2_6", "ricevi", 2):
                return
            $ msg("daniel", "...")
            $ msg("daniel", "Alive. Annoyingly so. Cut the second sentence, it's apologising again.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A2: l'ambizione professionale (frecciata) -------------------------------

label chat_daniel_a2:
    label tel_chat_daniel_a2_1:
    if telefono_minuti_blocco("tel_chat_daniel_a2_1", "invia", 1):
        return
    $ msg("sara", "Can I ask how you got where you are? Everyone at that dinner was terrified of you.")
    return

label chat_daniel_a2_1:
    label tel_chat_daniel_a2_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_a2_1_1", "ricevi", 2):
        return
    $ msg("daniel", "I decided at twenty-five that I would never ask permission again.")
    $ msg("daniel", "The rest was just paperwork.")
    label tel_chat_daniel_a2_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_a2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That sounds lonely.»":
            label tel_chat_daniel_a2_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_a2_1_3", "invia", 1):
                return
            $ msg("sara", "That sounds lonely.")
            label tel_chat_daniel_a2_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_a2_1_4", "ricevi", 1):
                return
            $ msg("daniel", "It sounds free. People confuse the two all the time.")
        "«I wish I had that.»":
            label tel_chat_daniel_a2_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_a2_1_5", "invia", 1):
                return
            $ msg("sara", "I wish I had that.")
            $ caldo()
            label tel_chat_daniel_a2_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_a2_1_6", "ricevi", 1):
                return
            $ msg("daniel", "You do. You just keep it on a leash.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_a2_2:
    label tel_chat_daniel_a2_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_a2_2_1", "ricevi", 2):
        return
    $ msg("daniel", "Some people ask permission their whole life. Some even ask permission to take a day off.")
    $ msg("daniel", "Your [nome_compagno] sent me a three-paragraph email to leave at five on Friday.")
    sp "That's cruel. And it's exactly the kind of thing he'd do."
    label tel_chat_daniel_a2_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_a2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«He's polite. That's not a flaw.»":
            label tel_chat_daniel_a2_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_a2_2_3", "invia", 1):
                return
            $ msg("sara", "He's polite. That's not a flaw.")
            $ interest("josh", 1)
            label tel_chat_daniel_a2_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_a2_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Loyal. I like that in you. Less in him.")
        "(Let it slide.)":
            label tel_chat_daniel_a2_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_a2_2_5", "invia", 1):
                return
            $ msg("sara", "...")
            label tel_chat_daniel_a2_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_a2_2_6", "ricevi", 1):
                return
            $ msg("daniel", "Silence. Smart.")
        "«Three paragraphs? Really?»":
            label tel_chat_daniel_a2_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_a2_2_7", "invia", 1):
                return
            $ msg("sara", "Three paragraphs? Really?")
            $ caldo()
            $ corruption(1)
            label tel_chat_daniel_a2_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_a2_2_8", "ricevi", 1):
                return
            $ msg("daniel", "With a bullet list. I'm framing it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A3: ristoranti eleganti -------------------------------------------------

label chat_daniel_a3:
    label tel_chat_daniel_a3_1:
    if telefono_minuti_blocco("tel_chat_daniel_a3_1", "invia", 1):
        return
    $ msg("sara", "That restaurant from the company dinner. Is it always like that, or did you book the whole place to impress?")
    return

label chat_daniel_a3_1:
    label tel_chat_daniel_a3_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_a3_1_1", "ricevi", 2):
        return
    $ msg("daniel", "I never need to impress. I just refuse to eat badly.")
    $ msg("daniel", "Did you like it?")
    label tel_chat_daniel_a3_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_a3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«The food was perfect. The company was... intense.»":
            label tel_chat_daniel_a3_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_a3_1_3", "invia", 1):
                return
            $ msg("sara", "The food was perfect. The company was... intense.")
            $ caldo()
            label tel_chat_daniel_a3_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_a3_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Intense. I'll take it.")
        "«A bit too formal for me.»":
            label tel_chat_daniel_a3_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_a3_1_5", "invia", 1):
                return
            $ msg("sara", "A bit too formal for me.")
            label tel_chat_daniel_a3_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_a3_1_6", "ricevi", 1):
                return
            $ msg("daniel", "Formal is a costume. You wore it well.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_a3_2:
    label tel_chat_daniel_a3_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_a3_2_1", "ricevi", 1):
        return
    $ msg("daniel", "There's a place by the harbour. No menu. The chef decides. You'd love it.")
    sp "Is he inviting me? No. He's just... describing."
    label tel_chat_daniel_a3_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_a3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'll tell [nome_compagno]. Maybe for our anniversary.»":
            label tel_chat_daniel_a3_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_a3_2_3", "invia", 1):
                return
            $ msg("sara", "I'll tell [nome_compagno]. Maybe for our anniversary.")
            label tel_chat_daniel_a3_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_a3_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Do. Tell him to book three months ahead. And to let you order.")
        "«No menu? That sounds like you.»":
            label tel_chat_daniel_a3_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_a3_2_5", "invia", 1):
                return
            $ msg("sara", "No menu? That sounds like you.")
            $ caldo()
            label tel_chat_daniel_a3_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_a3_2_6", "ricevi", 1):
                return
            $ msg("daniel", "Everything good sounds like me.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A4: automobili (frecciata) ----------------------------------------------

label chat_daniel_a4:
    label tel_chat_daniel_a4_1:
    if telefono_minuti_blocco("tel_chat_daniel_a4_1", "invia", 1):
        return
    $ msg("sara", "Was that your car outside the restaurant? The black one that looked like a spaceship?")
    return

label chat_daniel_a4_1:
    label tel_chat_daniel_a4_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_a4_1_1", "ricevi", 2):
        return
    $ msg("daniel", "It's not a spaceship. It's a reminder.")
    $ msg("daniel", "Every morning I see it and I remember what I worked for.")
    label tel_chat_daniel_a4_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_a4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Most people use a photo for that.»":
            label tel_chat_daniel_a4_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_a4_1_3", "invia", 1):
                return
            $ msg("sara", "Most people use a photo for that.")
            $ caldo()
            label tel_chat_daniel_a4_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_a4_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Most people don't have anything worth photographing.")
        "«It's very... loud.»":
            label tel_chat_daniel_a4_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_a4_1_5", "invia", 1):
                return
            $ msg("sara", "It's very... loud.")
            label tel_chat_daniel_a4_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_a4_1_6", "ricevi", 1):
                return
            $ msg("daniel", "So am I. We understand each other.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_a4_2:
    label tel_chat_daniel_a4_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_a4_2_1", "ricevi", 1):
        return
    $ msg("daniel", "What does [nome_compagno] drive? Wait. Let me guess. Something sensible. Grey. Good mileage.")
    label tel_chat_daniel_a4_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_a4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It gets us everywhere. That's what matters.»":
            label tel_chat_daniel_a4_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_a4_2_3", "invia", 1):
                return
            $ msg("sara", "It gets us everywhere. That's what matters.")
            $ interest("josh", 1)
            label tel_chat_daniel_a4_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_a4_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Everywhere he's allowed to go, yes.")
        "(Don't answer.)":
            label tel_chat_daniel_a4_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_a4_2_5", "invia", 1):
                return
            $ msg("sara", "...")
            label tel_chat_daniel_a4_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_a4_2_6", "ricevi", 1):
                return
            $ msg("daniel", "I'll take that as a «grey».")
        "«...It's grey.»":
            label tel_chat_daniel_a4_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_a4_2_7", "invia", 1):
                return
            $ msg("sara", "...It's grey.")
            $ caldo()
            $ corruption(1)
            label tel_chat_daniel_a4_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_a4_2_8", "ricevi", 1):
                return
            $ msg("daniel", "Of course it is.")
            sp "I shouldn't have laughed. I did laugh."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A5: viaggi di lusso -----------------------------------------------------

label chat_daniel_a5:
    label tel_chat_daniel_a5_1:
    if telefono_minuti_blocco("tel_chat_daniel_a5_1", "invia", 1):
        return
    $ msg("sara", "[nome_compagno] says you're never in the office on Mondays. Where do you go?")
    return

label chat_daniel_a5_1:
    label tel_chat_daniel_a5_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_a5_1_1", "ricevi", 2):
        return
    $ msg("daniel", "Wherever the weekend didn't finish.")
    $ msg("daniel", "Last week, the coast. A hotel where they bring breakfast to the terrace and nobody says a word.")
    label tel_chat_daniel_a5_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_a5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Must be nice.»":
            label tel_chat_daniel_a5_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_a5_1_3", "invia", 1):
                return
            $ msg("sara", "Must be nice.")
            label tel_chat_daniel_a5_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_a5_1_4", "ricevi", 1):
                return
            $ msg("daniel", "It is. That's the point.")
        "«I've never stayed anywhere like that.»":
            label tel_chat_daniel_a5_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_a5_1_5", "invia", 1):
                return
            $ msg("sara", "I've never stayed anywhere like that.")
            $ caldo()
            label tel_chat_daniel_a5_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_a5_1_6", "ricevi", 1):
                return
            $ msg("daniel", "You should. Some women look different with the sea behind them.")
            sp "Some women. Not me. Right?"
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_a5_2:
    label tel_chat_daniel_a5_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_a5_2_1", "ricevi", 1):
        return
    $ msg("daniel", "Where would you go? Money is not a question. Answer fast.")
    label tel_chat_daniel_a5_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_a5_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Somewhere quiet. With books.»":
            label tel_chat_daniel_a5_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_a5_2_3", "invia", 1):
                return
            $ msg("sara", "Somewhere quiet. With books.")
            label tel_chat_daniel_a5_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_a5_2_4", "ricevi", 1):
                return
            $ msg("daniel", "A writer's answer. Predictable and correct.")
        "«Somewhere nobody knows me.»" (confidence=25):
            label tel_chat_daniel_a5_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_a5_2_5", "invia", 1):
                return
            $ msg("sara", "Somewhere nobody knows me.")
            $ caldo()
            label tel_chat_daniel_a5_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_a5_2_6", "ricevi", 1):
                return
            $ msg("daniel", "Now that's interesting. Who would you be there?")
            label tel_chat_daniel_a5_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_a5_2_7", "invia", 1):
                return
            $ msg("sara", "I don't know yet.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a5_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a5_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A6: gusti musicali ------------------------------------------------------

label chat_daniel_a6:
    label tel_chat_daniel_a6_1:
    if telefono_minuti_blocco("tel_chat_daniel_a6_1", "invia", 1):
        return
    $ msg("sara", "What was the music at dinner? Everyone was too scared to ask you.")
    return

label chat_daniel_a6_1:
    label tel_chat_daniel_a6_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_a6_1_1", "ricevi", 1):
        return
    $ msg("daniel", "Jazz. Old jazz. Musicians who were drunk, broke and better than anyone alive today.")
    label tel_chat_daniel_a6_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_a6_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I don't know anything about jazz.»":
            label tel_chat_daniel_a6_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_a6_1_3", "invia", 1):
                return
            $ msg("sara", "I don't know anything about jazz.")
            label tel_chat_daniel_a6_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_a6_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Nobody does. That's why it works.")
        "«It was beautiful. Send me something.»":
            label tel_chat_daniel_a6_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_a6_1_5", "invia", 1):
                return
            $ msg("sara", "It was beautiful. Send me something.")
            $ caldo()
            label tel_chat_daniel_a6_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_a6_1_6", "ricevi", 2):
                return
            $ msg("daniel", "(A track: a slow saxophone, almost a whisper.)")
            $ msg("daniel", "Listen to it at night. Not in the car.")
            $ segna("daniel_jazz")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a6_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a6_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_a6_2:
    label tel_chat_daniel_a6_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_a6_2_1", "ricevi", 1):
        return
    $ msg("daniel", "What do you listen to?")
    label tel_chat_daniel_a6_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_a6_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Whatever's on the radio, honestly.»":
            label tel_chat_daniel_a6_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_a6_2_3", "invia", 1):
                return
            $ msg("sara", "Whatever's on the radio, honestly.")
            label tel_chat_daniel_a6_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_a6_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Honesty. Rare. Terrible taste, but rare.")
        "«Sad songs. When nobody's around.»":
            label tel_chat_daniel_a6_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_a6_2_5", "invia", 1):
                return
            $ msg("sara", "Sad songs. When nobody's around.")
            $ caldo()
            label tel_chat_daniel_a6_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_a6_2_6", "ricevi", 1):
                return
            $ msg("daniel", "Everyone interesting does.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a6_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a6_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A7: il valore del successo (frecciata) ----------------------------------

label chat_daniel_a7:
    label tel_chat_daniel_a7_1:
    if telefono_minuti_blocco("tel_chat_daniel_a7_1", "invia", 1):
        return
    $ msg("sara", "Do you ever stop? Working, I mean. [nome_compagno] says you answer emails at three in the morning.")
    return

label chat_daniel_a7_1:
    label tel_chat_daniel_a7_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_a7_1_1", "ricevi", 1):
        return
    $ msg("daniel", "Success isn't a job. It's a temperature. You either have it or you're cold.")
    sp "Who talks like that? He does. And it works on people."
    label tel_chat_daniel_a7_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_a7_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's a sad way to live.»":
            label tel_chat_daniel_a7_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_a7_1_3", "invia", 1):
                return
            $ msg("sara", "That's a sad way to live.")
            label tel_chat_daniel_a7_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_a7_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Sad is a word invented by people who settled.")
        "«And what's my temperature?»" (confidence=25):
            label tel_chat_daniel_a7_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_a7_1_5", "invia", 1):
                return
            $ msg("sara", "And what's my temperature?")
            $ caldo()
            label tel_chat_daniel_a7_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_a7_1_6", "ricevi", 1):
                return
            $ msg("daniel", "Rising. You just haven't noticed.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a7_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a7_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_a7_2:
    label tel_chat_daniel_a7_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_a7_2_1", "ricevi", 1):
        return
    $ msg("daniel", "Your [nome_compagno] is very good at his job. Very good. Exactly as good as he needs to be, and not one bit more.")
    label tel_chat_daniel_a7_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_a7_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«He's better than you think.»":
            label tel_chat_daniel_a7_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_a7_2_3", "invia", 1):
                return
            $ msg("sara", "He's better than you think.")
            $ interest("josh", 1)
            label tel_chat_daniel_a7_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_a7_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Then he's hiding it very well. I'll keep looking.")
        "(Let it go.)":
            label tel_chat_daniel_a7_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_a7_2_5", "invia", 1):
                return
            $ msg("sara", "...")
            label tel_chat_daniel_a7_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_a7_2_6", "ricevi", 1):
                return
            $ msg("daniel", "Goodnight.")
        "«That's... horribly accurate.»":
            label tel_chat_daniel_a7_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_a7_2_7", "invia", 1):
                return
            $ msg("sara", "That's... horribly accurate.")
            $ caldo()
            $ corruption(1)
            label tel_chat_daniel_a7_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_a7_2_8", "ricevi", 1):
                return
            $ msg("daniel", "I'm always accurate. Horrible is optional.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a7_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a7_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A8: battute sul lavoro (frecciata) --------------------------------------

label chat_daniel_a8:
    label tel_chat_daniel_a8_1:
    if telefono_minuti_blocco("tel_chat_daniel_a8_1", "invia", 1):
        return
    $ msg("sara", "Long day at the paper. My editor wants me to rewrite a piece for the third time.")
    return

label chat_daniel_a8_1:
    label tel_chat_daniel_a8_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_a8_1_1", "ricevi", 1):
        return
    $ msg("daniel", "Third time. Is it the piece or is it the editor?")
    label tel_chat_daniel_a8_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_a8_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«The editor. Definitely.»":
            label tel_chat_daniel_a8_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_a8_1_3", "invia", 1):
                return
            $ msg("sara", "The editor. Definitely.")
            $ caldo()
            label tel_chat_daniel_a8_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_a8_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Then rewrite it once more, perfectly, and make her feel stupid.")
        "«Probably me.»":
            label tel_chat_daniel_a8_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_a8_1_5", "invia", 1):
                return
            $ msg("sara", "Probably me.")
            label tel_chat_daniel_a8_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_a8_1_6", "ricevi", 1):
                return
            $ msg("daniel", "Stop that. It's an ugly habit.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a8_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a8_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_a8_2:
    label tel_chat_daniel_a8_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_a8_2_1", "ricevi", 2):
        return
    $ msg("daniel", "We had a long day too. [nome_compagno] presented the quarterly report.")
    $ msg("daniel", "He did very well. He only dropped the clicker twice.")
    label tel_chat_daniel_a8_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_a8_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Leave him alone, Daniel.»":
            label tel_chat_daniel_a8_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_a8_2_3", "invia", 1):
                return
            $ msg("sara", "Leave him alone, Daniel.")
            $ interest("josh", 1)
            label tel_chat_daniel_a8_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_a8_2_4", "ricevi", 1):
                return
            $ msg("daniel", "I always leave him alone. That's the problem.")
        "(Don't reply.)":
            label tel_chat_daniel_a8_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_a8_2_5", "invia", 1):
                return
            $ msg("sara", "...")
            label tel_chat_daniel_a8_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_a8_2_6", "ricevi", 1):
                return
            $ msg("daniel", "Read. No answer. You're learning.")
        "«Twice?»":
            label tel_chat_daniel_a8_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_a8_2_7", "invia", 1):
                return
            $ msg("sara", "Twice?")
            $ caldo()
            $ corruption(1)
            label tel_chat_daniel_a8_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_a8_2_8", "ricevi", 1):
                return
            $ msg("daniel", "The second time, it slid under the projector. It took two interns to get it out.")
            sp "Poor [nome_compagno]. Why am I smiling?"
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a8_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_a8_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B1: cosa rende attraente un uomo ----------------------------------------

label chat_daniel_b1:
    label tel_chat_daniel_b1_1:
    if telefono_minuti_blocco("tel_chat_daniel_b1_1", "invia", 1):
        return
    $ msg("sara", "Settle a bet. Joanie says confidence is the most attractive thing in a man. I say kindness.")
    return

label chat_daniel_b1_entrata:
    label tel_chat_daniel_b1_entrata_1:
    if telefono_minuti_blocco("tel_chat_daniel_b1_entrata_1", "ricevi", 1):
        return
    $ msg("daniel", "A question for a writer. What makes a man attractive? You must have an opinion. You write them.")
    label tel_chat_daniel_b1_entrata_2:
    if telefono_minuti_blocco("tel_chat_daniel_b1_entrata_2", "invia", 1):
        return
    $ msg("sara", "Kindness. Joanie says confidence.")
    return

label chat_daniel_b1_1:
    label tel_chat_daniel_b1_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_b1_1_1", "ricevi", 1):
        return
    $ msg("daniel", "Joanie wins. Kindness is what women say. Confidence is what women choose.")
    label tel_chat_daniel_b1_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_b1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's arrogant.»":
            label tel_chat_daniel_b1_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_b1_1_3", "invia", 1):
                return
            $ msg("sara", "That's arrogant.")
            label tel_chat_daniel_b1_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_b1_1_4", "ricevi", 1):
                return
            $ msg("daniel", "It's statistics. Arrogance is just statistics with good posture.")
        "«Maybe. Sometimes.»":
            label tel_chat_daniel_b1_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_b1_1_5", "invia", 1):
                return
            $ msg("sara", "Maybe. Sometimes.")
            $ caldo()
            label tel_chat_daniel_b1_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_b1_1_6", "ricevi", 1):
                return
            $ msg("daniel", "Sometimes is how it always starts.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_b1_2:
    label tel_chat_daniel_b1_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_b1_2_1", "ricevi", 1):
        return
    $ msg("daniel", "Think about the men in your stories. Are they kind?")
    sp "...They're not. None of them."
    label tel_chat_daniel_b1_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_b1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Some of them.»":
            label tel_chat_daniel_b1_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_b1_2_3", "invia", 1):
                return
            $ msg("sara", "Some of them.")
            label tel_chat_daniel_b1_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_b1_2_4", "ricevi", 1):
                return
            $ msg("daniel", "The ones nobody remembers.")
        "«...No. They're not.»":
            label tel_chat_daniel_b1_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_b1_2_5", "invia", 1):
                return
            $ msg("sara", "...No. They're not.")
            $ caldo()
            label tel_chat_daniel_b1_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_b1_2_6", "ricevi", 1):
                return
            $ msg("daniel", "I know. I could tell from the first page.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B2: la sicurezza in sé (frecciata) --------------------------------------

label chat_daniel_b2:
    label tel_chat_daniel_b2_1:
    if telefono_minuti_blocco("tel_chat_daniel_b2_1", "invia", 1):
        return
    $ msg("sara", "How do you do it? Walk into a room like you own it?")
    return

label chat_daniel_b2_1:
    label tel_chat_daniel_b2_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_b2_1_1", "ricevi", 2):
        return
    $ msg("daniel", "I decide that I do. The room usually agrees.")
    $ msg("daniel", "You could do it too. You just need to stop checking if everyone is ok.")
    label tel_chat_daniel_b2_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_b2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Checking on people is called being nice.»":
            label tel_chat_daniel_b2_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_b2_1_3", "invia", 1):
                return
            $ msg("sara", "Checking on people is called being nice.")
            label tel_chat_daniel_b2_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_b2_1_4", "ricevi", 1):
                return
            $ msg("daniel", "It's called being on duty. You're not a nurse.")
        "«Teach me, then.»" (confidence=30):
            label tel_chat_daniel_b2_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_b2_1_5", "invia", 1):
                return
            $ msg("sara", "Teach me, then.")
            $ caldo()
            label tel_chat_daniel_b2_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_b2_1_6", "ricevi", 1):
                return
            $ msg("daniel", "Lesson one: next time someone talks over you, don't stop talking.")
            $ segna("daniel_lezione")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_b2_2:
    label tel_chat_daniel_b2_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_b2_2_1", "ricevi", 1):
        return
    $ msg("daniel", "Confidence is contagious. So is the opposite. You live with the opposite.")
    label tel_chat_daniel_b2_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_b2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Don't talk about him like that.»":
            label tel_chat_daniel_b2_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_b2_2_3", "invia", 1):
                return
            $ msg("sara", "Don't talk about him like that.")
            $ interest("josh", 1)
            label tel_chat_daniel_b2_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_b2_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Noted. You defend him beautifully. Someone has to.")
        "(Let it slide.)":
            label tel_chat_daniel_b2_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_b2_2_5", "invia", 1):
                return
            $ msg("sara", "...")
        "«He's... getting better.»":
            label tel_chat_daniel_b2_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_b2_2_6", "invia", 1):
                return
            $ msg("sara", "He's... getting better.")
            $ caldo()
            $ corruption(1)
            label tel_chat_daniel_b2_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_b2_2_7", "ricevi", 1):
                return
            $ msg("daniel", "Getting. Better. Two words nobody wants on their gravestone.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B3: le insoddisfazioni nascoste (frecciata) -----------------------------

label chat_daniel_b3:
    label tel_chat_daniel_b3_1:
    if telefono_minuti_blocco("tel_chat_daniel_b3_1", "invia", 1):
        return
    $ msg("sara", "Can I ask you something? Are you happy? Really?")
    return

label chat_daniel_b3_1:
    label tel_chat_daniel_b3_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_b3_1_1", "ricevi", 2):
        return
    $ msg("daniel", "Happy is for people who stopped wanting. I haven't.")
    $ msg("daniel", "And you? Don't give me the dinner answer.")
    label tel_chat_daniel_b3_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_b3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I am happy.»":
            label tel_chat_daniel_b3_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_b3_1_3", "invia", 1):
                return
            $ msg("sara", "I am happy.")
            label tel_chat_daniel_b3_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_b3_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Three words, no punctuation of doubt. Impressive. Almost convincing.")
        "«Mostly. There's... something missing. I don't know what.»":
            label tel_chat_daniel_b3_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_b3_1_5", "invia", 1):
                return
            $ msg("sara", "Mostly. There's... something missing. I don't know what.")
            $ caldo()
            label tel_chat_daniel_b3_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_b3_1_6", "ricevi", 1):
                return
            $ msg("daniel", "You know what. You just don't like the answer.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_b3_2:
    label tel_chat_daniel_b3_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_b3_2_1", "ricevi", 1):
        return
    $ msg("daniel", "Let me guess. Saturday night. Sofa. He falls asleep at ten. You stay up and write.")
    sp "Exactly that. Every Saturday."
    label tel_chat_daniel_b3_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_b3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«He works hard. He's tired.»":
            label tel_chat_daniel_b3_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_b3_2_3", "invia", 1):
                return
            $ msg("sara", "He works hard. He's tired.")
            $ interest("josh", 1)
            label tel_chat_daniel_b3_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_b3_2_4", "ricevi", 1):
                return
            $ msg("daniel", "I make sure of it.")
            sp "What does that mean?"
        "(Don't answer.)":
            label tel_chat_daniel_b3_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_b3_2_5", "invia", 1):
                return
            $ msg("sara", "...")
            label tel_chat_daniel_b3_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_b3_2_6", "ricevi", 1):
                return
            $ msg("daniel", "That's a yes.")
        "«How do you know that?»":
            label tel_chat_daniel_b3_2_7:
            if telefono_minuti_blocco("tel_chat_daniel_b3_2_7", "invia", 1):
                return
            $ msg("sara", "How do you know that?")
            $ caldo()
            $ corruption(1)
            label tel_chat_daniel_b3_2_8:
            if telefono_minuti_blocco("tel_chat_daniel_b3_2_8", "ricevi", 1):
                return
            $ msg("daniel", "Because I've met him. And I've met you.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B4: le donne che lo hanno colpito ---------------------------------------

label chat_daniel_b4:
    label tel_chat_daniel_b4_1:
    if telefono_minuti_blocco("tel_chat_daniel_b4_1", "invia", 1):
        return
    $ msg("sara", "Has any woman ever said no to you?")
    return

label chat_daniel_b4_1:
    label tel_chat_daniel_b4_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_b4_1_1", "ricevi", 2):
        return
    $ msg("daniel", "One. At twenty-three. She married a dentist.")
    $ msg("daniel", "I still think about her every time I go to the dentist. Which is why I have perfect teeth.")
    label tel_chat_daniel_b4_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_b4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's almost sweet.»":
            label tel_chat_daniel_b4_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_b4_1_3", "invia", 1):
                return
            $ msg("sara", "That's almost sweet.")
            $ caldo()
            label tel_chat_daniel_b4_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_b4_1_4", "ricevi", 1):
                return
            $ msg("daniel", "Don't spread it around.")
        "«Only one? I don't believe you.»":
            label tel_chat_daniel_b4_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_b4_1_5", "invia", 1):
                return
            $ msg("sara", "Only one? I don't believe you.")
            label tel_chat_daniel_b4_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_b4_1_6", "ricevi", 1):
                return
            $ msg("daniel", "Only one that mattered.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_b4_2:
    label tel_chat_daniel_b4_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_b4_2_1", "ricevi", 1):
        return
    $ msg("daniel", "The women who stay with me are the ones who surprise me. It doesn't happen often.")
    sp "Why do I want to ask if I surprised him?"
    label tel_chat_daniel_b4_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_b4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Good luck finding the next one.»":
            label tel_chat_daniel_b4_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_b4_2_3", "invia", 1):
                return
            $ msg("sara", "Good luck finding the next one.")
            label tel_chat_daniel_b4_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_b4_2_4", "ricevi", 1):
                return
            $ msg("daniel", "I don't need luck.")
        "«And what surprises you?»" (confidence=30):
            label tel_chat_daniel_b4_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_b4_2_5", "invia", 1):
                return
            $ msg("sara", "And what surprises you?")
            $ caldo()
            label tel_chat_daniel_b4_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_b4_2_6", "ricevi", 1):
                return
            $ msg("daniel", "A woman who says what she wants. Before I say it for her.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B5: la differenza tra amore e desiderio ---------------------------------

label chat_daniel_b5:
    label tel_chat_daniel_b5_1:
    if telefono_minuti_blocco("tel_chat_daniel_b5_1", "invia", 1):
        return
    $ msg("sara", "Question for a cynic: do you believe in love?")
    return

label chat_daniel_b5_1:
    label tel_chat_daniel_b5_1_1:
    if telefono_minuti_blocco("tel_chat_daniel_b5_1_1", "ricevi", 1):
        return
    $ msg("daniel", "I believe in desire. Love is desire that got comfortable and bought a sofa.")
    label tel_chat_daniel_b5_1_2:
    if telefono_minuti_blocco("tel_chat_daniel_b5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's the saddest thing I've ever read.»":
            label tel_chat_daniel_b5_1_3:
            if telefono_minuti_blocco("tel_chat_daniel_b5_1_3", "invia", 1):
                return
            $ msg("sara", "That's the saddest thing I've ever read.")
            label tel_chat_daniel_b5_1_4:
            if telefono_minuti_blocco("tel_chat_daniel_b5_1_4", "ricevi", 1):
                return
            $ msg("daniel", "And yet you're still reading.")
        "«And what's wrong with a sofa?»":
            label tel_chat_daniel_b5_1_5:
            if telefono_minuti_blocco("tel_chat_daniel_b5_1_5", "invia", 1):
                return
            $ msg("sara", "And what's wrong with a sofa?")
            $ caldo()
            label tel_chat_daniel_b5_1_6:
            if telefono_minuti_blocco("tel_chat_daniel_b5_1_6", "ricevi", 1):
                return
            $ msg("daniel", "Nothing. Until you realise you're the only one still awake on it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_daniel_b5_2:
    label tel_chat_daniel_b5_2_1:
    if telefono_minuti_blocco("tel_chat_daniel_b5_2_1", "ricevi", 2):
        return
    $ msg("daniel", "You love him. I don't doubt it.")
    $ msg("daniel", "The question is: when was the last time you wanted him?")
    sp "I shouldn't answer that. I'm not going to answer that."
    label tel_chat_daniel_b5_2_2:
    if telefono_minuti_blocco("tel_chat_daniel_b5_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's none of your business. Goodnight.»":
            label tel_chat_daniel_b5_2_3:
            if telefono_minuti_blocco("tel_chat_daniel_b5_2_3", "invia", 1):
                return
            $ msg("sara", "That's none of your business. Goodnight.")
            $ interest("josh", 1)
            label tel_chat_daniel_b5_2_4:
            if telefono_minuti_blocco("tel_chat_daniel_b5_2_4", "ricevi", 1):
                return
            $ msg("daniel", "Goodnight, Sara.")
        "«...Goodnight, Daniel.»":
            label tel_chat_daniel_b5_2_5:
            if telefono_minuti_blocco("tel_chat_daniel_b5_2_5", "invia", 1):
                return
            $ msg("sara", "...Goodnight, Daniel.")
            $ caldo()
            $ corruption(1)
            $ segna("daniel_domanda_desiderio")
            label tel_chat_daniel_b5_2_6:
            if telefono_minuti_blocco("tel_chat_daniel_b5_2_6", "ricevi", 1):
                return
            $ msg("daniel", "That's an answer too.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b5_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_daniel_b5_2_2"
            $ telefono_minuti_chiudi = True
            return
    return
