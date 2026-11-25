## =============================================================================
## DARIUS (chiave "amico") — discorsi al telefono: introduzione, A, B
## =============================================================================
## Tono (Q&A 18/11/2026): COMPLETAMENTE LEALE A JOSH fino a C. In A e B è l'amico
## di sempre: battute, «lol», ricordi delle superiori con Josh. La svolta arriva
## come una sorpresa da C in poi. Percorso opt-in: senza le risposte calde di Sara
## le sue chat restano fra amici.

init python:
    discorso("amico_intro", "amico", ESTRANEI, se="fatto('ep2_preparativi_compleanno_josh')")
    discorso("amico_a1", "amico", ESTRANEI)
    discorso("amico_a2", "amico", CONOSCENTI)
    discorso("amico_a3", "amico", CONOSCENTI)
    discorso("amico_a4", "amico", CONOSCENTI, se="giorno >= 17 and fatto('ep2_serata_amici_giorno') == giorno - 1", argomento="The night out with everyone", scade="aperta_da >= 1")
    discorso("amico_a5", "amico", CONOSCENTI)
    discorso("amico_a6", "amico", CONOSCENTI)
    discorso("amico_a7", "amico", CONOSCENTI)
    discorso("amico_a8", "amico", CONOSCENTI)
    discorso("amico_b1", "amico", CONFIDENZA)
    discorso("amico_b2", "amico", CONFIDENZA)
    discorso("amico_b3", "amico", CONFIDENZA)
    discorso("amico_b4", "amico", CONFIDENZA)
    discorso("amico_b5", "amico", CONFIDENZA)


## --- Introduzione: un messaggio amichevole su Josh ---------------------------

label chat_amico_intro:
    label tel_chat_amico_intro_1:
    if telefono_minuti_blocco("tel_chat_amico_intro_1", "invia", 1):
        return
    $ msg("sara", "Hey Darius, it's Sara. [nome_compagno]'s birthday is next month. Help me plan something?")
    return

label chat_amico_intro_entrata:
    label tel_chat_amico_intro_entrata_1:
    if telefono_minuti_blocco("tel_chat_amico_intro_entrata_1", "ricevi", 1):
        return
    $ msg("amico", "Sara! Secret mission. [nome_compagno]'s birthday. You in?")
    label tel_chat_amico_intro_entrata_2:
    if telefono_minuti_blocco("tel_chat_amico_intro_entrata_2", "invia", 1):
        return
    $ msg("sara", "Of course I'm in!")
    return

label chat_amico_intro_1:
    label tel_chat_amico_intro_1_1:
    if telefono_minuti_blocco("tel_chat_amico_intro_1_1", "ricevi", 2):
        return
    $ msg("amico", "Yes!! Finally someone organised. Last year I forgot and he still brings it up lol")
    $ msg("amico", "Ideas: surprise party, or the cabin trip he's been talking about since high school")
    label tel_chat_amico_intro_1_2:
    if telefono_minuti_blocco("tel_chat_amico_intro_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«The cabin. He'd love that.»":
            label tel_chat_amico_intro_1_3:
            if telefono_minuti_blocco("tel_chat_amico_intro_1_3", "invia", 1):
                return
            $ msg("sara", "The cabin. He'd love that.")
            $ interest("josh", 1)
            label tel_chat_amico_intro_1_4:
            if telefono_minuti_blocco("tel_chat_amico_intro_1_4", "ricevi", 1):
                return
            $ msg("amico", "Cabin it is. I'll handle the boys, you handle him")
        "«A party. With everyone.»":
            label tel_chat_amico_intro_1_5:
            if telefono_minuti_blocco("tel_chat_amico_intro_1_5", "invia", 1):
                return
            $ msg("sara", "A party. With everyone.")
            $ caldo()
            label tel_chat_amico_intro_1_6:
            if telefono_minuti_blocco("tel_chat_amico_intro_1_6", "ricevi", 1):
                return
            $ msg("amico", "Party! I'll bring the embarrassing photos. All of them")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_intro_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_intro_1_2"
            $ telefono_minuti_chiudi = True
            return
    $ segna("darius_compleanno_josh")
    return

label chat_amico_intro_2:
    label tel_chat_amico_intro_2_1:
    if telefono_minuti_blocco("tel_chat_amico_intro_2_1", "ricevi", 2):
        return
    $ msg("amico", "He's lucky to have you, you know. Always says so")
    $ msg("amico", "Ok, top secret from now on. Delete this chat lol")
    return


## --- A1: amici comuni --------------------------------------------------------

label chat_amico_a1:
    label tel_chat_amico_a1_1:
    if telefono_minuti_blocco("tel_chat_amico_a1_1", "invia", 1):
        return
    $ msg("sara", "Who's the guy [nome_compagno] keeps calling «Big Phil»?")
    return

label chat_amico_a1_1:
    label tel_chat_amico_a1_1_1:
    if telefono_minuti_blocco("tel_chat_amico_a1_1_1", "ricevi", 2):
        return
    $ msg("amico", "Lol. Phil. He's 1 metre 60. Hence Big Phil")
    $ msg("amico", "High school. The three of us were inseparable. Phil, me and your man")
    label tel_chat_amico_a1_1_2:
    if telefono_minuti_blocco("tel_chat_amico_a1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I need to meet this legend.»":
            label tel_chat_amico_a1_1_3:
            if telefono_minuti_blocco("tel_chat_amico_a1_1_3", "invia", 1):
                return
            $ msg("sara", "I need to meet this legend.")
            $ caldo()
            label tel_chat_amico_a1_1_4:
            if telefono_minuti_blocco("tel_chat_amico_a1_1_4", "ricevi", 1):
                return
            $ msg("amico", "You will. He does magic tricks. Badly. Prepare yourself")
        "«[nome_compagno] never told me about him.»":
            label tel_chat_amico_a1_1_5:
            if telefono_minuti_blocco("tel_chat_amico_a1_1_5", "invia", 1):
                return
            $ msg("sara", "[nome_compagno] never told me about him.")
            label tel_chat_amico_a1_1_6:
            if telefono_minuti_blocco("tel_chat_amico_a1_1_6", "ricevi", 1):
                return
            $ msg("amico", "Probably because of the prom story. Ask him about the prom. Watch his face")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_a1_2:
    label tel_chat_amico_a1_2_1:
    if telefono_minuti_blocco("tel_chat_amico_a1_2_1", "ricevi", 1):
        return
    $ msg("amico", "We should all get together. Like a proper reunion. You'd fit right in")
    return


## --- A2: ricordi delle superiori ---------------------------------------------

label chat_amico_a2:
    label tel_chat_amico_a2_1:
    if telefono_minuti_blocco("tel_chat_amico_a2_1", "invia", 1):
        return
    $ msg("sara", "Ok, I asked [nome_compagno] about the prom. He turned red and left the room. Tell me.")
    return

label chat_amico_a2_1:
    label tel_chat_amico_a2_1_1:
    if telefono_minuti_blocco("tel_chat_amico_a2_1_1", "ricevi", 3):
        return
    $ msg("amico", "LOL. He did the same face?? Classic")
    $ msg("amico", "Ok. He rented a white suit. Spilled a whole cherry punch on it in the first ten minutes")
    $ msg("amico", "He spent the night telling everyone it was «a design»")
    label tel_chat_amico_a2_1_2:
    if telefono_minuti_blocco("tel_chat_amico_a2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Oh no. Poor thing :)»":
            label tel_chat_amico_a2_1_3:
            if telefono_minuti_blocco("tel_chat_amico_a2_1_3", "invia", 1):
                return
            $ msg("sara", "Oh no. Poor thing :)")
            $ interest("josh", 1)
            label tel_chat_amico_a2_1_4:
            if telefono_minuti_blocco("tel_chat_amico_a2_1_4", "ricevi", 1):
                return
            $ msg("amico", "Poor thing danced all night anyway. That's your man")
        "«I'm going to tease him forever.»":
            label tel_chat_amico_a2_1_5:
            if telefono_minuti_blocco("tel_chat_amico_a2_1_5", "invia", 1):
                return
            $ msg("sara", "I'm going to tease him forever.")
            $ caldo()
            label tel_chat_amico_a2_1_6:
            if telefono_minuti_blocco("tel_chat_amico_a2_1_6", "ricevi", 1):
                return
            $ msg("amico", "Please do. I've been doing it alone for fifteen years")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_a2_2:
    label tel_chat_amico_a2_2_1:
    if telefono_minuti_blocco("tel_chat_amico_a2_2_1", "ricevi", 1):
        return
    $ msg("amico", "He was the nicest guy in school. Still is. Don't tell him I said that")
    return


## --- A3: musica --------------------------------------------------------------

label chat_amico_a3:
    label tel_chat_amico_a3_1:
    if telefono_minuti_blocco("tel_chat_amico_a3_1", "invia", 1):
        return
    $ msg("sara", "What was that band you and [nome_compagno] had in high school? He refuses to tell me.")
    return

label chat_amico_a3_1:
    label tel_chat_amico_a3_1_1:
    if telefono_minuti_blocco("tel_chat_amico_a3_1_1", "ricevi", 2):
        return
    $ msg("amico", "Oh no. He told you about the band??")
    $ msg("amico", "We were called «The Lost Socks». I was on drums. He sang. Terribly")
    label tel_chat_amico_a3_1_2:
    if telefono_minuti_blocco("tel_chat_amico_a3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«The Lost Socks! I'm dying.»":
            label tel_chat_amico_a3_1_3:
            if telefono_minuti_blocco("tel_chat_amico_a3_1_3", "invia", 1):
                return
            $ msg("sara", "The Lost Socks! I'm dying.")
            $ caldo()
            label tel_chat_amico_a3_1_4:
            if telefono_minuti_blocco("tel_chat_amico_a3_1_4", "ricevi", 1):
                return
            $ msg("amico", "We had ONE fan. His mum")
        "«He sings in the shower. Still terribly.»":
            label tel_chat_amico_a3_1_5:
            if telefono_minuti_blocco("tel_chat_amico_a3_1_5", "invia", 1):
                return
            $ msg("sara", "He sings in the shower. Still terribly.")
            $ interest("josh", 1)
            label tel_chat_amico_a3_1_6:
            if telefono_minuti_blocco("tel_chat_amico_a3_1_6", "ricevi", 1):
                return
            $ msg("amico", "Some things never change lol")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_a3_2:
    label tel_chat_amico_a3_2_1:
    if telefono_minuti_blocco("tel_chat_amico_a3_2_1", "ricevi", 1):
        return
    $ msg("amico", "I might still have a recording. Price: one homemade dinner")
    label tel_chat_amico_a3_2_2:
    if telefono_minuti_blocco("tel_chat_amico_a3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Deal. Come on Saturday.»":
            label tel_chat_amico_a3_2_3:
            if telefono_minuti_blocco("tel_chat_amico_a3_2_3", "invia", 1):
                return
            $ msg("sara", "Deal. Come on Saturday.")
            $ caldo()
            label tel_chat_amico_a3_2_4:
            if telefono_minuti_blocco("tel_chat_amico_a3_2_4", "ricevi", 1):
                return
            $ msg("amico", "I'll bring the tape. And wine")
            $ segna("darius_cena_sabato")
        "«I'll make [nome_compagno] cook. Deal.»":
            label tel_chat_amico_a3_2_5:
            if telefono_minuti_blocco("tel_chat_amico_a3_2_5", "invia", 1):
                return
            $ msg("sara", "I'll make [nome_compagno] cook. Deal.")
            label tel_chat_amico_a3_2_6:
            if telefono_minuti_blocco("tel_chat_amico_a3_2_6", "ricevi", 1):
                return
            $ msg("amico", "Then I'm bringing antacids too lol")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A4: serate in compagnia -------------------------------------------------

label chat_amico_a4:
    label tel_chat_amico_a4_1:
    if telefono_minuti_blocco("tel_chat_amico_a4_1", "invia", 1):
        return
    $ msg("sara", "Thanks for last night. [nome_compagno] was so happy. He laughed more than he has in weeks.")
    return

label chat_amico_a4_1:
    label tel_chat_amico_a4_1_1:
    if telefono_minuti_blocco("tel_chat_amico_a4_1_1", "ricevi", 2):
        return
    $ msg("amico", "Anytime! He needs to get out more. Work is eating him alive")
    $ msg("amico", "His boss sounds like a nightmare honestly")
    label tel_chat_amico_a4_1_2:
    if telefono_minuti_blocco("tel_chat_amico_a4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«He is. Daniel is awful to him.»":
            label tel_chat_amico_a4_1_3:
            if telefono_minuti_blocco("tel_chat_amico_a4_1_3", "invia", 1):
                return
            $ msg("sara", "He is. Daniel is awful to him.")
            $ interest("josh", 1)
            label tel_chat_amico_a4_1_4:
            if telefono_minuti_blocco("tel_chat_amico_a4_1_4", "ricevi", 1):
                return
            $ msg("amico", "I'd love five minutes alone with that guy. Just to talk. Mostly")
        "«He'll be fine. He's strong.»":
            label tel_chat_amico_a4_1_5:
            if telefono_minuti_blocco("tel_chat_amico_a4_1_5", "invia", 1):
                return
            $ msg("sara", "He'll be fine. He's strong.")
            label tel_chat_amico_a4_1_6:
            if telefono_minuti_blocco("tel_chat_amico_a4_1_6", "ricevi", 1):
                return
            $ msg("amico", "He is. Stronger than he looks. Always was")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_a4_2:
    label tel_chat_amico_a4_2_1:
    if telefono_minuti_blocco("tel_chat_amico_a4_2_1", "ricevi", 1):
        return
    $ msg("amico", "Let's do it more often. The three of us. Board games, pizza, bad movies")
    label tel_chat_amico_a4_2_2:
    if telefono_minuti_blocco("tel_chat_amico_a4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Every Friday?»":
            label tel_chat_amico_a4_2_3:
            if telefono_minuti_blocco("tel_chat_amico_a4_2_3", "invia", 1):
                return
            $ msg("sara", "Every Friday?")
            $ caldo()
            label tel_chat_amico_a4_2_4:
            if telefono_minuti_blocco("tel_chat_amico_a4_2_4", "ricevi", 1):
                return
            $ msg("amico", "Every Friday. It's a tradition now. No backing out")
        "«When we can.»":
            label tel_chat_amico_a4_2_5:
            if telefono_minuti_blocco("tel_chat_amico_a4_2_5", "invia", 1):
                return
            $ msg("sara", "When we can.")
            label tel_chat_amico_a4_2_6:
            if telefono_minuti_blocco("tel_chat_amico_a4_2_6", "ricevi", 1):
                return
            $ msg("amico", "Deal")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A5: Josh da ragazzo -----------------------------------------------------

label chat_amico_a5:
    label tel_chat_amico_a5_1:
    if telefono_minuti_blocco("tel_chat_amico_a5_1", "invia", 1):
        return
    $ msg("sara", "What was [nome_compagno] like at sixteen?")
    return

label chat_amico_a5_1:
    label tel_chat_amico_a5_1_1:
    if telefono_minuti_blocco("tel_chat_amico_a5_1_1", "ricevi", 2):
        return
    $ msg("amico", "Skinny. Glasses. Always reading comics. Too polite to tell a girl he liked her")
    $ msg("amico", "Once he waited outside a girl's house for an hour with flowers and then went home. Didn't knock")
    label tel_chat_amico_a5_1_2:
    if telefono_minuti_blocco("tel_chat_amico_a5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's so sweet.»":
            label tel_chat_amico_a5_1_3:
            if telefono_minuti_blocco("tel_chat_amico_a5_1_3", "invia", 1):
                return
            $ msg("sara", "That's so sweet.")
            $ interest("josh", 1)
            label tel_chat_amico_a5_1_4:
            if telefono_minuti_blocco("tel_chat_amico_a5_1_4", "ricevi", 1):
                return
            $ msg("amico", "That's him. All heart, zero courage lol")
        "«He waited and didn't knock? Why?»":
            label tel_chat_amico_a5_1_5:
            if telefono_minuti_blocco("tel_chat_amico_a5_1_5", "invia", 1):
                return
            $ msg("sara", "He waited and didn't knock? Why?")
            $ caldo()
            label tel_chat_amico_a5_1_6:
            if telefono_minuti_blocco("tel_chat_amico_a5_1_6", "ricevi", 1):
                return
            $ msg("amico", "Said he «didn't want to bother her». I knocked for him next time")
            sp "Darius knocked for him."
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_a5_2:
    label tel_chat_amico_a5_2_1:
    if telefono_minuti_blocco("tel_chat_amico_a5_2_1", "ricevi", 1):
        return
    $ msg("amico", "With you he finally found the courage. You changed him. For the better")
    return


## --- A6: videogiochi ---------------------------------------------------------

label chat_amico_a6:
    label tel_chat_amico_a6_1:
    if telefono_minuti_blocco("tel_chat_amico_a6_1", "invia", 1):
        return
    $ msg("sara", "Why did [nome_compagno] stay up until 3 playing with you? He was a zombie at breakfast.")
    return

label chat_amico_a6_1:
    label tel_chat_amico_a6_1_1:
    if telefono_minuti_blocco("tel_chat_amico_a6_1_1", "ricevi", 2):
        return
    $ msg("amico", "Guilty lol. Online tournament. We came second!")
    $ msg("amico", "Ok, eleventh. But it FELT like second")
    label tel_chat_amico_a6_1_2:
    if telefono_minuti_blocco("tel_chat_amico_a6_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Next time send him to bed at midnight.»":
            label tel_chat_amico_a6_1_3:
            if telefono_minuti_blocco("tel_chat_amico_a6_1_3", "invia", 1):
                return
            $ msg("sara", "Next time send him to bed at midnight.")
            $ interest("josh", 1)
            label tel_chat_amico_a6_1_4:
            if telefono_minuti_blocco("tel_chat_amico_a6_1_4", "ricevi", 1):
                return
            $ msg("amico", "Yes ma'am. I'll set an alarm")
        "«Teach me. I want to beat you both.»":
            label tel_chat_amico_a6_1_5:
            if telefono_minuti_blocco("tel_chat_amico_a6_1_5", "invia", 1):
                return
            $ msg("sara", "Teach me. I want to beat you both.")
            $ caldo()
            label tel_chat_amico_a6_1_6:
            if telefono_minuti_blocco("tel_chat_amico_a6_1_6", "ricevi", 1):
                return
            $ msg("amico", "Oh it's ON. Saturday. Bring snacks and your worst attitude")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a6_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a6_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_a6_2:
    label tel_chat_amico_a6_2_1:
    if telefono_minuti_blocco("tel_chat_amico_a6_2_1", "ricevi", 1):
        return
    $ msg("amico", "He talks about you between rounds, you know. Embarrassing. Very sweet")
    return


## --- A7: programmi del weekend -----------------------------------------------

label chat_amico_a7:
    label tel_chat_amico_a7_1:
    if telefono_minuti_blocco("tel_chat_amico_a7_1", "invia", 1):
        return
    $ msg("sara", "Any plans this weekend?")
    return

label chat_amico_a7_1:
    label tel_chat_amico_a7_1_1:
    if telefono_minuti_blocco("tel_chat_amico_a7_1_1", "ricevi", 2):
        return
    $ msg("amico", "Football Saturday. Sunday: fixing my bike, which I've been saying for six months")
    $ msg("amico", "You two? Still the sofa marathon?")
    label tel_chat_amico_a7_1_2:
    if telefono_minuti_blocco("tel_chat_amico_a7_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Sofa marathon. Season four.»":
            label tel_chat_amico_a7_1_3:
            if telefono_minuti_blocco("tel_chat_amico_a7_1_3", "invia", 1):
                return
            $ msg("sara", "Sofa marathon. Season four.")
            label tel_chat_amico_a7_1_4:
            if telefono_minuti_blocco("tel_chat_amico_a7_1_4", "ricevi", 1):
                return
            $ msg("amico", "Respect. No spoilers")
        "«We need new plans. Ideas?»":
            label tel_chat_amico_a7_1_5:
            if telefono_minuti_blocco("tel_chat_amico_a7_1_5", "invia", 1):
                return
            $ msg("sara", "We need new plans. Ideas?")
            $ caldo()
            label tel_chat_amico_a7_1_6:
            if telefono_minuti_blocco("tel_chat_amico_a7_1_6", "ricevi", 1):
                return
            $ msg("amico", "Lake trail on Sunday. I'll bring the frisbee. [nome_compagno] can't catch, it's hilarious")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a7_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a7_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_a7_2:
    label tel_chat_amico_a7_2_1:
    if telefono_minuti_blocco("tel_chat_amico_a7_2_1", "ricevi", 1):
        return
    $ msg("amico", "Seriously, call me whenever you two are bored. I'm always free. Sadly lol")
    return


## --- A8: abitudini quotidiane ------------------------------------------------

label chat_amico_a8:
    label tel_chat_amico_a8_1:
    if telefono_minuti_blocco("tel_chat_amico_a8_1", "invia", 1):
        return
    $ msg("sara", "Random question. Are you a morning person?")
    return

label chat_amico_a8_1:
    label tel_chat_amico_a8_1_1:
    if telefono_minuti_blocco("tel_chat_amico_a8_1_1", "ricevi", 2):
        return
    $ msg("amico", "Gym at 6. Shower. Coffee. Work. I'm annoyingly organised")
    $ msg("amico", "Unlike someone we both know who hits snooze five times")
    label tel_chat_amico_a8_1_2:
    if telefono_minuti_blocco("tel_chat_amico_a8_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Six times. I counted.»":
            label tel_chat_amico_a8_1_3:
            if telefono_minuti_blocco("tel_chat_amico_a8_1_3", "invia", 1):
                return
            $ msg("sara", "Six times. I counted.")
            $ caldo()
            label tel_chat_amico_a8_1_4:
            if telefono_minuti_blocco("tel_chat_amico_a8_1_4", "ricevi", 1):
                return
            $ msg("amico", "SIX. I'm telling him you snitched")
        "«He's not a morning person. It's cute.»":
            label tel_chat_amico_a8_1_5:
            if telefono_minuti_blocco("tel_chat_amico_a8_1_5", "invia", 1):
                return
            $ msg("sara", "He's not a morning person. It's cute.")
            $ interest("josh", 1)
            label tel_chat_amico_a8_1_6:
            if telefono_minuti_blocco("tel_chat_amico_a8_1_6", "ricevi", 1):
                return
            $ msg("amico", "Cute is one word for it lol")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a8_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_a8_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_a8_2:
    label tel_chat_amico_a8_2_1:
    if telefono_minuti_blocco("tel_chat_amico_a8_2_1", "ricevi", 1):
        return
    $ msg("amico", "You're a morning person, right? You look like one. Up at dawn, tea, notebook")
    sp "Exactly that. How does he know?"
    return


## --- B1: il rapporto con Josh ------------------------------------------------

label chat_amico_b1:
    label tel_chat_amico_b1_1:
    if telefono_minuti_blocco("tel_chat_amico_b1_1", "invia", 1):
        return
    $ msg("sara", "Can I ask you something serious? Is [nome_compagno] ok? He seems down lately.")
    return

label chat_amico_b1_entrata:
    label tel_chat_amico_b1_entrata_1:
    if telefono_minuti_blocco("tel_chat_amico_b1_entrata_1", "ricevi", 1):
        return
    $ msg("amico", "Hey. Is [nome_compagno] ok? He was quiet at football")
    label tel_chat_amico_b1_entrata_2:
    if telefono_minuti_blocco("tel_chat_amico_b1_entrata_2", "invia", 1):
        return
    $ msg("sara", "I was going to ask you the same thing.")
    return

label chat_amico_b1_1:
    label tel_chat_amico_b1_1_1:
    if telefono_minuti_blocco("tel_chat_amico_b1_1_1", "ricevi", 2):
        return
    $ msg("amico", "It's work. That Daniel guy is getting into his head")
    $ msg("amico", "He doesn't say it, but I know him. Fifteen years. He's my brother")
    label tel_chat_amico_b1_1_2:
    if telefono_minuti_blocco("tel_chat_amico_b1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What can I do?»":
            label tel_chat_amico_b1_1_3:
            if telefono_minuti_blocco("tel_chat_amico_b1_1_3", "invia", 1):
                return
            $ msg("sara", "What can I do?")
            $ interest("josh", 1)
            label tel_chat_amico_b1_1_4:
            if telefono_minuti_blocco("tel_chat_amico_b1_1_4", "ricevi", 1):
                return
            $ msg("amico", "Just be there. He'd walk through fire for you. He needs to know you're behind him")
        "«I don't know how to help him.»":
            label tel_chat_amico_b1_1_5:
            if telefono_minuti_blocco("tel_chat_amico_b1_1_5", "invia", 1):
                return
            $ msg("sara", "I don't know how to help him.")
            $ caldo()
            label tel_chat_amico_b1_1_6:
            if telefono_minuti_blocco("tel_chat_amico_b1_1_6", "ricevi", 1):
                return
            $ msg("amico", "We'll figure it out. Together. That's what we do")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_b1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_b1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_b1_2:
    label tel_chat_amico_b1_2_1:
    if telefono_minuti_blocco("tel_chat_amico_b1_2_1", "ricevi", 2):
        return
    $ msg("amico", "I'll take him out Thursday. Beers, darts, no talking about work")
    $ msg("amico", "Whatever he needs. Always")
    return


## --- B2: i lati meno conosciuti di Darius ------------------------------------

label chat_amico_b2:
    label tel_chat_amico_b2_1:
    if telefono_minuti_blocco("tel_chat_amico_b2_1", "invia", 1):
        return
    $ msg("sara", "You always look after everyone. Who looks after you?")
    return

label chat_amico_b2_1:
    label tel_chat_amico_b2_1_1:
    if telefono_minuti_blocco("tel_chat_amico_b2_1_1", "ricevi", 2):
        return
    $ msg("amico", "...Wow. Nobody's asked me that in a while")
    $ msg("amico", "I'm fine. I like being the one who fixes things. Keeps my head busy")
    label tel_chat_amico_b2_1_2:
    if telefono_minuti_blocco("tel_chat_amico_b2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You're allowed to need people too.»":
            label tel_chat_amico_b2_1_3:
            if telefono_minuti_blocco("tel_chat_amico_b2_1_3", "invia", 1):
                return
            $ msg("sara", "You're allowed to need people too.")
            $ caldo()
            label tel_chat_amico_b2_1_4:
            if telefono_minuti_blocco("tel_chat_amico_b2_1_4", "ricevi", 1):
                return
            $ msg("amico", "Look at you, giving advice. [nome_compagno] said you were wise. He was right")
        "«Well, you have us.»":
            label tel_chat_amico_b2_1_5:
            if telefono_minuti_blocco("tel_chat_amico_b2_1_5", "invia", 1):
                return
            $ msg("sara", "Well, you have us.")
            label tel_chat_amico_b2_1_6:
            if telefono_minuti_blocco("tel_chat_amico_b2_1_6", "ricevi", 1):
                return
            $ msg("amico", "I know. Best thing I've got")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_b2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_b2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_b2_2:
    label tel_chat_amico_b2_2_1:
    if telefono_minuti_blocco("tel_chat_amico_b2_2_1", "ricevi", 1):
        return
    $ msg("amico", "Truth? My dad left when I was ten. I promised myself I'd never leave anyone. Never")
    sp "I never knew that."
    $ segna("darius_padre")
    return


## --- B3: le qualità che Sara apprezza negli uomini ---------------------------

label chat_amico_b3:
    label tel_chat_amico_b3_1:
    if telefono_minuti_blocco("tel_chat_amico_b3_1", "invia", 1):
        return
    $ msg("sara", "How did the date go? [nome_compagno] said you had a date!")
    return

label chat_amico_b3_1:
    label tel_chat_amico_b3_1_1:
    if telefono_minuti_blocco("tel_chat_amico_b3_1_1", "ricevi", 2):
        return
    $ msg("amico", "Lol. Disaster. She talked about her ex for two hours")
    $ msg("amico", "Help me out. What do women actually want? Be honest")
    label tel_chat_amico_b3_1_2:
    if telefono_minuti_blocco("tel_chat_amico_b3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Someone kind. Who listens.»":
            label tel_chat_amico_b3_1_3:
            if telefono_minuti_blocco("tel_chat_amico_b3_1_3", "invia", 1):
                return
            $ msg("sara", "Someone kind. Who listens.")
            label tel_chat_amico_b3_1_4:
            if telefono_minuti_blocco("tel_chat_amico_b3_1_4", "ricevi", 1):
                return
            $ msg("amico", "Kind and listens. So, [nome_compagno]. Got it lol")
        "«Someone who makes them feel safe. And a bit dangerous.»" (confidence=25):
            label tel_chat_amico_b3_1_5:
            if telefono_minuti_blocco("tel_chat_amico_b3_1_5", "invia", 1):
                return
            $ msg("sara", "Someone who makes them feel safe. And a bit dangerous.")
            $ caldo()
            label tel_chat_amico_b3_1_6:
            if telefono_minuti_blocco("tel_chat_amico_b3_1_6", "ricevi", 1):
                return
            $ msg("amico", "Safe AND dangerous. That's a hard combo. Writing it down")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_b3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_b3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_b3_2:
    label tel_chat_amico_b3_2_1:
    if telefono_minuti_blocco("tel_chat_amico_b3_2_1", "ricevi", 2):
        return
    $ msg("amico", "Thanks Sara. Seriously. If I find someone half as good as you, I'll be happy")
    $ msg("amico", "[nome_compagno] won the lottery, I keep telling him")
    return


## --- B4: come cambia un'amicizia ---------------------------------------------

label chat_amico_b4:
    label tel_chat_amico_b4_1:
    if telefono_minuti_blocco("tel_chat_amico_b4_1", "invia", 1):
        return
    $ msg("sara", "Do you miss how things were before I came along? You and [nome_compagno], every day.")
    return

label chat_amico_b4_1:
    label tel_chat_amico_b4_1_1:
    if telefono_minuti_blocco("tel_chat_amico_b4_1_1", "ricevi", 2):
        return
    $ msg("amico", "Honestly? A little. But not in a bad way")
    $ msg("amico", "He grew up. You're good for him. And I got a friend out of it too")
    label tel_chat_amico_b4_1_2:
    if telefono_minuti_blocco("tel_chat_amico_b4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm glad you see me as a friend.»":
            label tel_chat_amico_b4_1_3:
            if telefono_minuti_blocco("tel_chat_amico_b4_1_3", "invia", 1):
                return
            $ msg("sara", "I'm glad you see me as a friend.")
            $ caldo()
            label tel_chat_amico_b4_1_4:
            if telefono_minuti_blocco("tel_chat_amico_b4_1_4", "ricevi", 1):
                return
            $ msg("amico", "Course I do. You're family now. Both of you")
        "«I never want to come between you two.»":
            label tel_chat_amico_b4_1_5:
            if telefono_minuti_blocco("tel_chat_amico_b4_1_5", "invia", 1):
                return
            $ msg("sara", "I never want to come between you two.")
            $ interest("josh", 1)
            label tel_chat_amico_b4_1_6:
            if telefono_minuti_blocco("tel_chat_amico_b4_1_6", "ricevi", 1):
                return
            $ msg("amico", "You never could. Nobody could")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_b4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_b4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_b4_2:
    label tel_chat_amico_b4_2_1:
    if telefono_minuti_blocco("tel_chat_amico_b4_2_1", "ricevi", 1):
        return
    $ msg("amico", "Friendships change. The good ones get bigger, not smaller. That's ours")
    return


## --- B5: sentirsi a proprio agio insieme -------------------------------------

label chat_amico_b5:
    label tel_chat_amico_b5_1:
    if telefono_minuti_blocco("tel_chat_amico_b5_1", "invia", 1):
        return
    $ msg("sara", "It's funny. I can talk to you about anything. Even more than with some of my friends.")
    return

label chat_amico_b5_1:
    label tel_chat_amico_b5_1_1:
    if telefono_minuti_blocco("tel_chat_amico_b5_1_1", "ricevi", 2):
        return
    $ msg("amico", "Same here. You're easy to talk to. No pretending")
    $ msg("amico", "[nome_compagno] and you are the only people I don't have to perform for")
    label tel_chat_amico_b5_1_2:
    if telefono_minuti_blocco("tel_chat_amico_b5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That means a lot.»":
            label tel_chat_amico_b5_1_3:
            if telefono_minuti_blocco("tel_chat_amico_b5_1_3", "invia", 1):
                return
            $ msg("sara", "That means a lot.")
            $ caldo()
            label tel_chat_amico_b5_1_4:
            if telefono_minuti_blocco("tel_chat_amico_b5_1_4", "ricevi", 1):
                return
            $ msg("amico", "It's true. Don't make it weird lol")
        "«We're lucky to have you.»":
            label tel_chat_amico_b5_1_5:
            if telefono_minuti_blocco("tel_chat_amico_b5_1_5", "invia", 1):
                return
            $ msg("sara", "We're lucky to have you.")
            $ interest("josh", 1)
            label tel_chat_amico_b5_1_6:
            if telefono_minuti_blocco("tel_chat_amico_b5_1_6", "ricevi", 1):
                return
            $ msg("amico", "Other way round. Always")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_b5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_amico_b5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_amico_b5_2:
    label tel_chat_amico_b5_2_1:
    if telefono_minuti_blocco("tel_chat_amico_b5_2_1", "ricevi", 1):
        return
    $ msg("amico", "Goodnight Sara. Tell your man I said hi. And that he still owes me twenty bucks")
    return
