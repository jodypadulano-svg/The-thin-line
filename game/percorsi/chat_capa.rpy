## =============================================================================
## BARBARA (chiave "capa") — discorsi al telefono: introduzione, A, B
## =============================================================================
## Tono (Q&A 18/11/2026): teatrale, autoritaria, invadente, «darling», punti
## esclamativi; commenta l'aspetto di Sara (leitmotiv della scollatura: condotta
## inappropriata, parte del personaggio). Risponde solo in orario di lavoro.
## Piccoli ordini personali, AL MASSIMO 3 fra A e B (A3, A4, B3): obbedire ->
## Barbara +1 e flag per la scena del giorno dopo; ironizzare -> niente;
## rifiutare -> Confidence +1 (lei sembra accettare ma ci riprova).
## Non nomina MAI il modo di fumare. Percorso lento: il vero inizio è nel mese 2.

init python:
    discorso("capa_intro", "capa", ESTRANEI, se="fatto('ep2_pezzo_extra_inviato_barbara')")
    discorso("capa_a1", "capa", CONOSCENTI, se="fatto('ep2_scadenza_redazione_venerdi')", argomento="Friday's deadline")
    discorso("capa_a2", "capa", ESTRANEI)
    discorso("capa_a3", "capa", CONOSCENTI, se="fatto('ep2_riunione_sponsor_vigilia') == giorno", argomento="The sponsor meeting", scade="aperta_da >= 1")
    discorso("capa_a4", "capa", CONOSCENTI, se="fatto('ep2_sessione_foto_riprogrammata')", argomento="The photo session")
    discorso("capa_a5", "capa", CONOSCENTI)
    discorso("capa_a6", "capa", CONOSCENTI)
    discorso("capa_a7", "capa", CONOSCENTI)
    discorso("capa_a8", "capa", CONOSCENTI)
    discorso("capa_b1", "capa", CONFIDENZA)
    discorso("capa_b2", "capa", CONFIDENZA)
    discorso("capa_b3", "capa", CONFIDENZA, se="fatto('ep2_intervista_consigliere_vigilia') == giorno", argomento="The councillor interview", scade="aperta_da >= 1")
    discorso("capa_b4", "capa", CONFIDENZA)
    discorso("capa_b5", "capa", CONFIDENZA)


## --- Introduzione: una richiesta professionale dopo il lavoro ----------------

label chat_capa_intro:
    label tel_chat_capa_intro_1:
    if telefono_minuti_blocco("tel_chat_capa_intro_1", "invia", 1):
        return
    $ msg("sara", "Barbara, it's Sara. The extra piece is finished. I sent it to your inbox.")
    return

label chat_capa_intro_1:
    label tel_chat_capa_intro_1_1:
    if telefono_minuti_blocco("tel_chat_capa_intro_1_1", "ricevi", 2):
        return
    $ msg("capa", "I know, darling. I read it in the lift.")
    $ msg("capa", "Paragraph four is limp. LIMP. Fix it tonight and send it back by eight tomorrow.")
    sp "Tonight. Of course tonight."
    label tel_chat_capa_intro_1_2:
    if telefono_minuti_blocco("tel_chat_capa_intro_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Of course. I'll fix it.»":
            label tel_chat_capa_intro_1_3:
            if telefono_minuti_blocco("tel_chat_capa_intro_1_3", "invia", 1):
                return
            $ msg("sara", "Of course. I'll fix it.")
            label tel_chat_capa_intro_1_4:
            if telefono_minuti_blocco("tel_chat_capa_intro_1_4", "ricevi", 1):
                return
            $ msg("capa", "Good girl.")
        "«Can it wait until tomorrow morning?»":
            label tel_chat_capa_intro_1_5:
            if telefono_minuti_blocco("tel_chat_capa_intro_1_5", "invia", 1):
                return
            $ msg("sara", "Can it wait until tomorrow morning?")
            $ confidence(1)
            label tel_chat_capa_intro_1_6:
            if telefono_minuti_blocco("tel_chat_capa_intro_1_6", "ricevi", 1):
                return
            $ msg("capa", "Hm. Tomorrow at nine, on my desk. Not nine-oh-one.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_intro_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_intro_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_intro_2:
    label tel_chat_capa_intro_2_1:
    if telefono_minuti_blocco("tel_chat_capa_intro_2_1", "ricevi", 2):
        return
    $ msg("capa", "The rest is good. Better than good. Don't let it go to your head.")
    $ msg("capa", "And Sara. That blue blouse you wore. Finally something with a neckline. Keep going in that direction.")
    sp "She noticed my blouse. Of course she did."
    label tel_chat_capa_intro_2_2:
    if telefono_minuti_blocco("tel_chat_capa_intro_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Thank you... I think.»":
            label tel_chat_capa_intro_2_3:
            if telefono_minuti_blocco("tel_chat_capa_intro_2_3", "invia", 1):
                return
            $ msg("sara", "Thank you... I think.")
            label tel_chat_capa_intro_2_4:
            if telefono_minuti_blocco("tel_chat_capa_intro_2_4", "ricevi", 1):
                return
            $ msg("capa", "It was a compliment, darling. I don't give many.")
        "«I'll dress as I like, but thanks.»":
            label tel_chat_capa_intro_2_5:
            if telefono_minuti_blocco("tel_chat_capa_intro_2_5", "invia", 1):
                return
            $ msg("sara", "I'll dress as I like, but thanks.")
            $ confidence(1)
            label tel_chat_capa_intro_2_6:
            if telefono_minuti_blocco("tel_chat_capa_intro_2_6", "ricevi", 1):
                return
            $ msg("capa", "Of course you will. For now.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_intro_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_intro_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A1: scadenze in redazione -----------------------------------------------

label chat_capa_a1:
    label tel_chat_capa_a1_1:
    if telefono_minuti_blocco("tel_chat_capa_a1_1", "invia", 1):
        return
    $ msg("sara", "Barbara, quick question about Friday's deadline. Is it Friday morning or Friday night?")
    return

label chat_capa_a1_1:
    label tel_chat_capa_a1_1_1:
    if telefono_minuti_blocco("tel_chat_capa_a1_1_1", "ricevi", 2):
        return
    $ msg("capa", "Friday morning. Friday night is for people with no ambition.")
    $ msg("capa", "Are you going to be late?")
    label tel_chat_capa_a1_1_2:
    if telefono_minuti_blocco("tel_chat_capa_a1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«No. It'll be there.»":
            label tel_chat_capa_a1_1_3:
            if telefono_minuti_blocco("tel_chat_capa_a1_1_3", "invia", 1):
                return
            $ msg("sara", "No. It'll be there.")
            $ caldo()
            label tel_chat_capa_a1_1_4:
            if telefono_minuti_blocco("tel_chat_capa_a1_1_4", "ricevi", 1):
                return
            $ msg("capa", "That's what I like to hear. Short. Certain.")
        "«I might need a few more hours.»":
            label tel_chat_capa_a1_1_5:
            if telefono_minuti_blocco("tel_chat_capa_a1_1_5", "invia", 1):
                return
            $ msg("sara", "I might need a few more hours.")
            label tel_chat_capa_a1_1_6:
            if telefono_minuti_blocco("tel_chat_capa_a1_1_6", "ricevi", 1):
                return
            $ msg("capa", "You have until ten. Not because you asked. Because I'm generous today.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_a1_2:
    label tel_chat_capa_a1_2_1:
    if telefono_minuti_blocco("tel_chat_capa_a1_2_1", "ricevi", 1):
        return
    $ msg("capa", "Jessica used to be late every week. Now she's early every week. People change when they want to please me.")
    sp "Jessica did change. A lot."
    label tel_chat_capa_a1_2_2:
    if telefono_minuti_blocco("tel_chat_capa_a1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm not late. I'm thorough.»":
            label tel_chat_capa_a1_2_3:
            if telefono_minuti_blocco("tel_chat_capa_a1_2_3", "invia", 1):
                return
            $ msg("sara", "I'm not late. I'm thorough.")
            $ confidence(1)
            label tel_chat_capa_a1_2_4:
            if telefono_minuti_blocco("tel_chat_capa_a1_2_4", "ricevi", 1):
                return
            $ msg("capa", "Thorough. Cute word. Be thorough by Friday morning.")
        "«I'll do my best.»":
            label tel_chat_capa_a1_2_5:
            if telefono_minuti_blocco("tel_chat_capa_a1_2_5", "invia", 1):
                return
            $ msg("sara", "I'll do my best.")
            label tel_chat_capa_a1_2_6:
            if telefono_minuti_blocco("tel_chat_capa_a1_2_6", "ricevi", 1):
                return
            $ msg("capa", "Your best is the minimum, darling.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A2: il giornalismo ------------------------------------------------------

label chat_capa_a2:
    label tel_chat_capa_a2_1:
    if telefono_minuti_blocco("tel_chat_capa_a2_1", "invia", 1):
        return
    $ msg("sara", "Can I ask you something? Why did you buy a newspaper? Everyone says print is dying.")
    return

label chat_capa_a2_1:
    label tel_chat_capa_a2_1_1:
    if telefono_minuti_blocco("tel_chat_capa_a2_1_1", "ricevi", 2):
        return
    $ msg("capa", "Everyone says. Everyone is boring.")
    $ msg("capa", "A newspaper is a stage, darling. Whoever owns the stage decides who gets the light.")
    label tel_chat_capa_a2_1_2:
    if telefono_minuti_blocco("tel_chat_capa_a2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«And who gets the light?»":
            label tel_chat_capa_a2_1_3:
            if telefono_minuti_blocco("tel_chat_capa_a2_1_3", "invia", 1):
                return
            $ msg("sara", "And who gets the light?")
            $ caldo()
            label tel_chat_capa_a2_1_4:
            if telefono_minuti_blocco("tel_chat_capa_a2_1_4", "ricevi", 1):
                return
            $ msg("capa", "Whoever deserves it. And whoever I decide deserves it. Not always the same thing.")
        "«I thought it was about the news.»":
            label tel_chat_capa_a2_1_5:
            if telefono_minuti_blocco("tel_chat_capa_a2_1_5", "invia", 1):
                return
            $ msg("sara", "I thought it was about the news.")
            label tel_chat_capa_a2_1_6:
            if telefono_minuti_blocco("tel_chat_capa_a2_1_6", "ricevi", 1):
                return
            $ msg("capa", "Oh, sweet thing. Nothing is ever about the news.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_a2_2:
    label tel_chat_capa_a2_2_1:
    if telefono_minuti_blocco("tel_chat_capa_a2_2_1", "ricevi", 1):
        return
    $ msg("capa", "You could have the light one day. If you stop hiding behind other people's stories.")
    sp "Is she encouraging me? Barbara?"
    label tel_chat_capa_a2_2_2:
    if telefono_minuti_blocco("tel_chat_capa_a2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'd like that.»":
            label tel_chat_capa_a2_2_3:
            if telefono_minuti_blocco("tel_chat_capa_a2_2_3", "invia", 1):
                return
            $ msg("sara", "I'd like that.")
            $ caldo()
            label tel_chat_capa_a2_2_4:
            if telefono_minuti_blocco("tel_chat_capa_a2_2_4", "ricevi", 1):
                return
            $ msg("capa", "I know you would. I can always tell what my girls want.")
        "«I'm happy where I am.»":
            label tel_chat_capa_a2_2_5:
            if telefono_minuti_blocco("tel_chat_capa_a2_2_5", "invia", 1):
                return
            $ msg("sara", "I'm happy where I am.")
            label tel_chat_capa_a2_2_6:
            if telefono_minuti_blocco("tel_chat_capa_a2_2_6", "ricevi", 1):
                return
            $ msg("capa", "Nobody is happy where they are. They're just scared to move.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A3: moda e stile (ordine 1: la camicetta verde) -------------------------

label chat_capa_a3:
    label tel_chat_capa_a3_1:
    if telefono_minuti_blocco("tel_chat_capa_a3_1", "invia", 1):
        return
    $ msg("sara", "Barbara, the dress code for Thursday's meeting with the sponsors. Formal?")
    return

label chat_capa_a3_1:
    label tel_chat_capa_a3_1_1:
    if telefono_minuti_blocco("tel_chat_capa_a3_1_1", "ricevi", 2):
        return
    $ msg("capa", "Formal is for funerals. Elegant. Memorable.")
    $ msg("capa", "Tomorrow, wear the green blouse. The one with the low neckline. Not the grey thing you hide in.")
    sp "How does she even know what's in my wardrobe?"
    label tel_chat_capa_a3_1_2:
    if telefono_minuti_blocco("tel_chat_capa_a3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Ok. The green one.»":
            label tel_chat_capa_a3_1_3:
            if telefono_minuti_blocco("tel_chat_capa_a3_1_3", "invia", 1):
                return
            $ msg("sara", "Ok. The green one.")
            $ interest("capa", 1)
            $ segna("barbara_ordine_camicetta")
            label tel_chat_capa_a3_1_4:
            if telefono_minuti_blocco("tel_chat_capa_a3_1_4", "ricevi", 1):
                return
            $ msg("capa", "Good girl. You'll thank me.")
        "«Yes, ma'am. Shall I salute too? :)»":
            label tel_chat_capa_a3_1_5:
            if telefono_minuti_blocco("tel_chat_capa_a3_1_5", "invia", 1):
                return
            $ msg("sara", "Yes, ma'am. Shall I salute too? :)")
            label tel_chat_capa_a3_1_6:
            if telefono_minuti_blocco("tel_chat_capa_a3_1_6", "ricevi", 1):
                return
            $ msg("capa", "Ha! Cheeky. Wear the blouse and salute, then.")
        "«I'll choose my clothes myself, Barbara.»":
            label tel_chat_capa_a3_1_7:
            if telefono_minuti_blocco("tel_chat_capa_a3_1_7", "invia", 1):
                return
            $ msg("sara", "I'll choose my clothes myself, Barbara.")
            $ confidence(1)
            label tel_chat_capa_a3_1_8:
            if telefono_minuti_blocco("tel_chat_capa_a3_1_8", "ricevi", 2):
                return
            $ msg("capa", "Of course, darling. Of course.")
            $ msg("capa", "We'll talk about it again.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_a3_2:
    label tel_chat_capa_a3_2_1:
    if telefono_minuti_blocco("tel_chat_capa_a3_2_1", "ricevi", 1):
        return
    $ msg("capa", "Style is not what you wear. It's how much you let people look.")
    return


## --- A4: trucco e immagine (ordine 2: il rossetto) ---------------------------

label chat_capa_a4:
    label tel_chat_capa_a4_1:
    if telefono_minuti_blocco("tel_chat_capa_a4_1", "invia", 1):
        return
    $ msg("sara", "Roberta says you had a word with the photographer about my picture for the byline?")
    return

label chat_capa_a4_1:
    label tel_chat_capa_a4_1_1:
    if telefono_minuti_blocco("tel_chat_capa_a4_1_1", "ricevi", 2):
        return
    $ msg("capa", "I did. You looked like a nun on holiday.")
    $ msg("capa", "We're reshooting Monday. Darker lipstick. Burgundy. You have the lips for it, you just don't use them.")
    label tel_chat_capa_a4_1_2:
    if telefono_minuti_blocco("tel_chat_capa_a4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Burgundy. Ok, I'll get one.»":
            label tel_chat_capa_a4_1_3:
            if telefono_minuti_blocco("tel_chat_capa_a4_1_3", "invia", 1):
                return
            $ msg("sara", "Burgundy. Ok, I'll get one.")
            $ interest("capa", 1)
            $ segna("barbara_ordine_rossetto")
            label tel_chat_capa_a4_1_4:
            if telefono_minuti_blocco("tel_chat_capa_a4_1_4", "ricevi", 1):
                return
            $ msg("capa", "I'll have one sent to your desk. Mine. I know the exact shade.")
        "«A nun on holiday? Thanks a lot :)»":
            label tel_chat_capa_a4_1_5:
            if telefono_minuti_blocco("tel_chat_capa_a4_1_5", "invia", 1):
                return
            $ msg("sara", "A nun on holiday? Thanks a lot :)")
            label tel_chat_capa_a4_1_6:
            if telefono_minuti_blocco("tel_chat_capa_a4_1_6", "ricevi", 1):
                return
            $ msg("capa", "A pretty nun. But still a nun.")
        "«I'd rather keep my usual look.»":
            label tel_chat_capa_a4_1_7:
            if telefono_minuti_blocco("tel_chat_capa_a4_1_7", "invia", 1):
                return
            $ msg("sara", "I'd rather keep my usual look.")
            $ confidence(1)
            label tel_chat_capa_a4_1_8:
            if telefono_minuti_blocco("tel_chat_capa_a4_1_8", "ricevi", 1):
                return
            $ msg("capa", "Your usual look is invisible, darling. But fine. For now.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_a4_2:
    label tel_chat_capa_a4_2_1:
    if telefono_minuti_blocco("tel_chat_capa_a4_2_1", "ricevi", 1):
        return
    $ msg("capa", "All my girls wear a little more colour after a few months. Haven't you noticed?")
    sp "Jessica. Roberta. All of them, now that she says it."
    return


## --- A5: le colleghe ---------------------------------------------------------

label chat_capa_a5:
    label tel_chat_capa_a5_1:
    if telefono_minuti_blocco("tel_chat_capa_a5_1", "invia", 1):
        return
    $ msg("sara", "Is Jessica ok? She seemed... different, this week. Very calm.")
    return

label chat_capa_a5_1:
    label tel_chat_capa_a5_1_1:
    if telefono_minuti_blocco("tel_chat_capa_a5_1_1", "ricevi", 2):
        return
    $ msg("capa", "Jessica is perfect. She finally found her place.")
    $ msg("capa", "When she started she was a mess. Anxious, sloppy. Now look at her. Serene.")
    sp "Serene. That's one word for it."
    label tel_chat_capa_a5_1_2:
    if telefono_minuti_blocco("tel_chat_capa_a5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What happened to her?»":
            label tel_chat_capa_a5_1_3:
            if telefono_minuti_blocco("tel_chat_capa_a5_1_3", "invia", 1):
                return
            $ msg("sara", "What happened to her?")
            label tel_chat_capa_a5_1_4:
            if telefono_minuti_blocco("tel_chat_capa_a5_1_4", "ricevi", 1):
                return
            $ msg("capa", "She listened to me, darling. That's all. It's very simple, listening.")
            $ segna("barbara_jessica_accenno")
        "«She does seem happier.»":
            label tel_chat_capa_a5_1_5:
            if telefono_minuti_blocco("tel_chat_capa_a5_1_5", "invia", 1):
                return
            $ msg("sara", "She does seem happier.")
            $ caldo()
            label tel_chat_capa_a5_1_6:
            if telefono_minuti_blocco("tel_chat_capa_a5_1_6", "ricevi", 1):
                return
            $ msg("capa", "They all are. Eventually.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_a5_2:
    label tel_chat_capa_a5_2_1:
    if telefono_minuti_blocco("tel_chat_capa_a5_2_1", "ricevi", 2):
        return
    $ msg("capa", "Roberta was the same. Now she'd do anything for this paper. For me.")
    $ msg("capa", "You'll see. You're at the beginning.")
    return


## --- A6: eventi mondani ------------------------------------------------------

label chat_capa_a6:
    label tel_chat_capa_a6_1:
    if telefono_minuti_blocco("tel_chat_capa_a6_1", "invia", 1):
        return
    $ msg("sara", "I saw your photo in the society pages. The gala. You looked amazing.")
    return

label chat_capa_a6_1:
    label tel_chat_capa_a6_1_1:
    if telefono_minuti_blocco("tel_chat_capa_a6_1_1", "ricevi", 2):
        return
    $ msg("capa", "Of course I did, darling. Leopard and champagne. A classic.")
    $ msg("capa", "Those galas are where the real work happens. Contracts, favours, secrets.")
    label tel_chat_capa_a6_1_2:
    if telefono_minuti_blocco("tel_chat_capa_a6_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It sounds exhausting.»":
            label tel_chat_capa_a6_1_3:
            if telefono_minuti_blocco("tel_chat_capa_a6_1_3", "invia", 1):
                return
            $ msg("sara", "It sounds exhausting.")
            label tel_chat_capa_a6_1_4:
            if telefono_minuti_blocco("tel_chat_capa_a6_1_4", "ricevi", 1):
                return
            $ msg("capa", "Exhausting for the boring. For me it's oxygen.")
        "«I've never been to anything like that.»":
            label tel_chat_capa_a6_1_5:
            if telefono_minuti_blocco("tel_chat_capa_a6_1_5", "invia", 1):
                return
            $ msg("sara", "I've never been to anything like that.")
            $ caldo()
            label tel_chat_capa_a6_1_6:
            if telefono_minuti_blocco("tel_chat_capa_a6_1_6", "ricevi", 1):
                return
            $ msg("capa", "Then one day I'll take you. As my guest. In something red.")
            $ segna("barbara_gala_invito")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a6_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a6_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_a6_2:
    label tel_chat_capa_a6_2_1:
    if telefono_minuti_blocco("tel_chat_capa_a6_2_1", "ricevi", 1):
        return
    $ msg("capa", "I always bring one of my girls. Last time it was Jessica. She didn't leave my side all night.")
    sp "Why does she say «my girls» like that?"
    return


## --- A7: il carattere delle donne --------------------------------------------

label chat_capa_a7:
    label tel_chat_capa_a7_1:
    if telefono_minuti_blocco("tel_chat_capa_a7_1", "invia", 1):
        return
    $ msg("sara", "Why only women in the newsroom? Did you plan it?")
    return

label chat_capa_a7_1:
    label tel_chat_capa_a7_1_1:
    if telefono_minuti_blocco("tel_chat_capa_a7_1_1", "ricevi", 2):
        return
    $ msg("capa", "Women work harder, complain less and lie better. All excellent qualities in a journalist.")
    $ msg("capa", "Men were a distraction. For them, mostly.")
    label tel_chat_capa_a7_1_2:
    if telefono_minuti_blocco("tel_chat_capa_a7_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's a bit unfair to men.»":
            label tel_chat_capa_a7_1_3:
            if telefono_minuti_blocco("tel_chat_capa_a7_1_3", "invia", 1):
                return
            $ msg("sara", "That's a bit unfair to men.")
            label tel_chat_capa_a7_1_4:
            if telefono_minuti_blocco("tel_chat_capa_a7_1_4", "ricevi", 1):
                return
            $ msg("capa", "Life is unfair to men all the time, darling. They just never notice.")
        "«Lie better? Really?»":
            label tel_chat_capa_a7_1_5:
            if telefono_minuti_blocco("tel_chat_capa_a7_1_5", "invia", 1):
                return
            $ msg("sara", "Lie better? Really?")
            $ caldo()
            label tel_chat_capa_a7_1_6:
            if telefono_minuti_blocco("tel_chat_capa_a7_1_6", "ricevi", 1):
                return
            $ msg("capa", "Oh yes. Ask any woman who's been married.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a7_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a7_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_a7_2:
    label tel_chat_capa_a7_2_1:
    if telefono_minuti_blocco("tel_chat_capa_a7_2_1", "ricevi", 1):
        return
    $ msg("capa", "Women understand women. We know what we need before we say it. Men need a manual.")
    sp "She's not entirely wrong."
    return


## --- A8: l'ambizione professionale -------------------------------------------

label chat_capa_a8:
    label tel_chat_capa_a8_1:
    if telefono_minuti_blocco("tel_chat_capa_a8_1", "invia", 1):
        return
    $ msg("sara", "Barbara, do you think I could have my own column one day?")
    return

label chat_capa_a8_1:
    label tel_chat_capa_a8_1_1:
    if telefono_minuti_blocco("tel_chat_capa_a8_1_1", "ricevi", 2):
        return
    $ msg("capa", "Bold. I like it.")
    $ msg("capa", "Yes. One day. When you stop writing as if you were apologising for taking up space.")
    label tel_chat_capa_a8_1_2:
    if telefono_minuti_blocco("tel_chat_capa_a8_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«How do I stop?»":
            label tel_chat_capa_a8_1_3:
            if telefono_minuti_blocco("tel_chat_capa_a8_1_3", "invia", 1):
                return
            $ msg("sara", "How do I stop?")
            $ caldo()
            label tel_chat_capa_a8_1_4:
            if telefono_minuti_blocco("tel_chat_capa_a8_1_4", "ricevi", 1):
                return
            $ msg("capa", "You let someone teach you. Someone who knows what you could be.")
        "«I'll work on it.»":
            label tel_chat_capa_a8_1_5:
            if telefono_minuti_blocco("tel_chat_capa_a8_1_5", "invia", 1):
                return
            $ msg("sara", "I'll work on it.")
            label tel_chat_capa_a8_1_6:
            if telefono_minuti_blocco("tel_chat_capa_a8_1_6", "ricevi", 1):
                return
            $ msg("capa", "Work on it with me. Alone you'll take ten years.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a8_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_a8_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_a8_2:
    label tel_chat_capa_a8_2_1:
    if telefono_minuti_blocco("tel_chat_capa_a8_2_1", "ricevi", 1):
        return
    $ msg("capa", "Ambition is very attractive on a woman, Sara. Remember that.")
    return


## --- B1: il suo divorzio -----------------------------------------------------

label chat_capa_b1:
    label tel_chat_capa_b1_1:
    if telefono_minuti_blocco("tel_chat_capa_b1_1", "invia", 1):
        return
    $ msg("sara", "Can I ask you something personal? Were you ever married?")
    return

label chat_capa_b1_1:
    label tel_chat_capa_b1_1_1:
    if telefono_minuti_blocco("tel_chat_capa_b1_1_1", "ricevi", 2):
        return
    $ msg("capa", "Once. Eleven years. He was handsome, charming and absolutely useless.")
    $ msg("capa", "He promised me everything and gave me a cheap affair with his secretary. A cliché, darling. He couldn't even betray me with style.")
    label tel_chat_capa_b1_1_2:
    if telefono_minuti_blocco("tel_chat_capa_b1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm sorry, Barbara.»":
            label tel_chat_capa_b1_1_3:
            if telefono_minuti_blocco("tel_chat_capa_b1_1_3", "invia", 1):
                return
            $ msg("sara", "I'm sorry, Barbara.")
            $ caldo()
            label tel_chat_capa_b1_1_4:
            if telefono_minuti_blocco("tel_chat_capa_b1_1_4", "ricevi", 1):
                return
            $ msg("capa", "Don't be. It was the best thing that ever happened to me.")
        "«That must have been terrible.»":
            label tel_chat_capa_b1_1_5:
            if telefono_minuti_blocco("tel_chat_capa_b1_1_5", "invia", 1):
                return
            $ msg("sara", "That must have been terrible.")
            label tel_chat_capa_b1_1_6:
            if telefono_minuti_blocco("tel_chat_capa_b1_1_6", "ricevi", 1):
                return
            $ msg("capa", "For six months. Then it was liberating.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_b1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_b1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_b1_2:
    label tel_chat_capa_b1_2_1:
    if telefono_minuti_blocco("tel_chat_capa_b1_2_1", "ricevi", 1):
        return
    $ msg("capa", "Since then I keep only people around me who adore me. Life is too short for anything less.")
    sp "Who adore her. Not who love her. Adore."
    return


## --- B2: le donne indipendenti -----------------------------------------------

label chat_capa_b2:
    label tel_chat_capa_b2_1:
    if telefono_minuti_blocco("tel_chat_capa_b2_1", "invia", 1):
        return
    $ msg("sara", "Do you ever get lonely? You seem so... complete. On your own.")
    return

label chat_capa_b2_1:
    label tel_chat_capa_b2_1_1:
    if telefono_minuti_blocco("tel_chat_capa_b2_1_1", "ricevi", 2):
        return
    $ msg("capa", "Lonely? Darling, I'm never alone. I'm independent. There's a difference.")
    $ msg("capa", "An independent woman chooses her company. She doesn't wait for it.")
    label tel_chat_capa_b2_1_2:
    if telefono_minuti_blocco("tel_chat_capa_b2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I wish I were more like that.»":
            label tel_chat_capa_b2_1_3:
            if telefono_minuti_blocco("tel_chat_capa_b2_1_3", "invia", 1):
                return
            $ msg("sara", "I wish I were more like that.")
            $ caldo()
            label tel_chat_capa_b2_1_4:
            if telefono_minuti_blocco("tel_chat_capa_b2_1_4", "ricevi", 1):
                return
            $ msg("capa", "You could be. You just need the right example.")
        "«I like waiting for [nome_compagno] at home, though.»":
            label tel_chat_capa_b2_1_5:
            if telefono_minuti_blocco("tel_chat_capa_b2_1_5", "invia", 1):
                return
            $ msg("sara", "I like waiting for [nome_compagno] at home, though.")
            $ interest("josh", 1)
            label tel_chat_capa_b2_1_6:
            if telefono_minuti_blocco("tel_chat_capa_b2_1_6", "ricevi", 1):
                return
            $ msg("capa", "Of course you do. How sweet. How very... domestic.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_b2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_b2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_b2_2:
    label tel_chat_capa_b2_2_1:
    if telefono_minuti_blocco("tel_chat_capa_b2_2_1", "ricevi", 1):
        return
    $ msg("capa", "Women spend their lives waiting for men to decide things. I decided to stop. The view is much better from here.")
    return


## --- B3: come valorizzare la propria immagine (ordine 3: la scollatura) ------

label chat_capa_b3:
    label tel_chat_capa_b3_1:
    if telefono_minuti_blocco("tel_chat_capa_b3_1", "invia", 1):
        return
    $ msg("sara", "What should I wear for the councillor interview?")
    return

label chat_capa_b3_entrata:
    label tel_chat_capa_b3_entrata_1:
    if telefono_minuti_blocco("tel_chat_capa_b3_entrata_1", "ricevi", 1):
        return
    $ msg("capa", "Sara. Tomorrow is the interview with the councillor. I want you to make an impression.")
    label tel_chat_capa_b3_entrata_2:
    if telefono_minuti_blocco("tel_chat_capa_b3_entrata_2", "invia", 1):
        return
    $ msg("sara", "What do you suggest?")
    return

label chat_capa_b3_1:
    label tel_chat_capa_b3_1_1:
    if telefono_minuti_blocco("tel_chat_capa_b3_1_1", "ricevi", 2):
        return
    $ msg("capa", "A woman who is seen is a woman who is listened to.")
    $ msg("capa", "Tomorrow: the black dress. Low neckline. No cardigan. I want to see you, not your shyness.")
    sp "No cardigan. She always says that."
    label tel_chat_capa_b3_1_2:
    if telefono_minuti_blocco("tel_chat_capa_b3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Ok. The black dress.»":
            label tel_chat_capa_b3_1_3:
            if telefono_minuti_blocco("tel_chat_capa_b3_1_3", "invia", 1):
                return
            $ msg("sara", "Ok. The black dress.")
            $ interest("capa", 1)
            $ segna("barbara_ordine_scollatura")
            label tel_chat_capa_b3_1_4:
            if telefono_minuti_blocco("tel_chat_capa_b3_1_4", "ricevi", 1):
                return
            $ msg("capa", "Good girl. I'll be waiting at the door to check.")
        "«And if I get cold? :)»":
            label tel_chat_capa_b3_1_5:
            if telefono_minuti_blocco("tel_chat_capa_b3_1_5", "invia", 1):
                return
            $ msg("sara", "And if I get cold? :)")
            label tel_chat_capa_b3_1_6:
            if telefono_minuti_blocco("tel_chat_capa_b3_1_6", "ricevi", 1):
                return
            $ msg("capa", "Then you'll shiver elegantly.")
        "«I'll wear what I'm comfortable in.»":
            label tel_chat_capa_b3_1_7:
            if telefono_minuti_blocco("tel_chat_capa_b3_1_7", "invia", 1):
                return
            $ msg("sara", "I'll wear what I'm comfortable in.")
            $ confidence(1)
            label tel_chat_capa_b3_1_8:
            if telefono_minuti_blocco("tel_chat_capa_b3_1_8", "ricevi", 2):
                return
            $ msg("capa", "Comfortable. Yes. Comfortable is lovely.")
            $ msg("capa", "Think about it overnight anyway.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_b3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_b3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_b3_2:
    label tel_chat_capa_b3_2_1:
    if telefono_minuti_blocco("tel_chat_capa_b3_2_1", "ricevi", 1):
        return
    $ msg("capa", "Your body is an asset, darling. You've been hiding it like a debt.")
    return


## --- B4: la fiducia fra donne ------------------------------------------------

label chat_capa_b4:
    label tel_chat_capa_b4_1:
    if telefono_minuti_blocco("tel_chat_capa_b4_1", "invia", 1):
        return
    $ msg("sara", "Can I trust you with something? It's about work. And not.")
    return

label chat_capa_b4_1:
    label tel_chat_capa_b4_1_1:
    if telefono_minuti_blocco("tel_chat_capa_b4_1_1", "ricevi", 2):
        return
    $ msg("capa", "Of course you can. Everything stays between us. Between us women.")
    $ msg("capa", "Tell me.")
    label tel_chat_capa_b4_1_2:
    if telefono_minuti_blocco("tel_chat_capa_b4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Sometimes I feel invisible. At work, at home.»":
            label tel_chat_capa_b4_1_3:
            if telefono_minuti_blocco("tel_chat_capa_b4_1_3", "invia", 1):
                return
            $ msg("sara", "Sometimes I feel invisible. At work, at home.")
            $ caldo()
            label tel_chat_capa_b4_1_4:
            if telefono_minuti_blocco("tel_chat_capa_b4_1_4", "ricevi", 1):
                return
            $ msg("capa", "Not to me. I see you, Sara. I've seen you from the first day.")
            $ segna("barbara_confidenza_invisibile")
        "«Never mind. It's silly.»":
            label tel_chat_capa_b4_1_5:
            if telefono_minuti_blocco("tel_chat_capa_b4_1_5", "invia", 1):
                return
            $ msg("sara", "Never mind. It's silly.")
            label tel_chat_capa_b4_1_6:
            if telefono_minuti_blocco("tel_chat_capa_b4_1_6", "ricevi", 1):
                return
            $ msg("capa", "Nothing you say is silly to me, darling. Whenever you're ready.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_b4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_b4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_b4_2:
    label tel_chat_capa_b4_2_1:
    if telefono_minuti_blocco("tel_chat_capa_b4_2_1", "ricevi", 1):
        return
    $ msg("capa", "Men listen to answer. Women listen to understand. And I listen to keep.")
    sp "To keep? Keep what?"
    return


## --- B5: cosa pensa davvero di Sara ------------------------------------------

label chat_capa_b5:
    label tel_chat_capa_b5_1:
    if telefono_minuti_blocco("tel_chat_capa_b5_1", "invia", 1):
        return
    $ msg("sara", "Barbara, honestly. What do you think of me? Not as a journalist.")
    return

label chat_capa_b5_1:
    label tel_chat_capa_b5_1_1:
    if telefono_minuti_blocco("tel_chat_capa_b5_1_1", "ricevi", 2):
        return
    $ msg("capa", "Honestly? I think you're a beautiful woman who was taught to say sorry for it.")
    $ msg("capa", "I think you're wasted. On that desk, on that grey wardrobe. Maybe on other things.")
    sp "On other things. She means [nome_compagno]."
    label tel_chat_capa_b5_1_2:
    if telefono_minuti_blocco("tel_chat_capa_b5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm not wasted. I'm happy.»":
            label tel_chat_capa_b5_1_3:
            if telefono_minuti_blocco("tel_chat_capa_b5_1_3", "invia", 1):
                return
            $ msg("sara", "I'm not wasted. I'm happy.")
            $ interest("josh", 1)
            label tel_chat_capa_b5_1_4:
            if telefono_minuti_blocco("tel_chat_capa_b5_1_4", "ricevi", 1):
                return
            $ msg("capa", "Of course you are, darling. Of course.")
        "«...Maybe you're right.»":
            label tel_chat_capa_b5_1_5:
            if telefono_minuti_blocco("tel_chat_capa_b5_1_5", "invia", 1):
                return
            $ msg("sara", "...Maybe you're right.")
            $ caldo()
            label tel_chat_capa_b5_1_6:
            if telefono_minuti_blocco("tel_chat_capa_b5_1_6", "ricevi", 1):
                return
            $ msg("capa", "I'm always right about my girls.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_b5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_capa_b5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_capa_b5_2:
    label tel_chat_capa_b5_2_1:
    if telefono_minuti_blocco("tel_chat_capa_b5_2_1", "ricevi", 1):
        return
    $ msg("capa", "Stay close to me, Sara. I can make you into something extraordinary. If you let me.")
    sp "If I let her. What does that even mean?"
    return
