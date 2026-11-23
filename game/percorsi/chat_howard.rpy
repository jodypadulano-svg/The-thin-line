## =============================================================================
## HOWARD — discorsi al telefono: introduzione, A (conoscenti), B (confidenza)
## =============================================================================
## Tono (Q&A 18/11/2026): il disagio si vede SEMPRE dal modo di scrivere
## (troppi messaggi, troppo presto, sa cose che non dovrebbe sapere, battute fuori
## luogo). In circa una chat su tre (intro, A5, A8, B3, B4) un breve retroscena
## testuale dal suo lato. Sara non nota niente: per lei è un vicino solo e gentile.

init python:
    discorso("howard_intro", "howard", ESTRANEI)
    discorso("howard_a1", "howard", CONOSCENTI)
    discorso("howard_a2", "howard", CONOSCENTI)
    discorso("howard_a3", "howard", CONOSCENTI, orario=(17 * 60, 20 * 60 + 30))
    discorso("howard_a4", "howard", CONOSCENTI)
    discorso("howard_a5", "howard", CONOSCENTI)
    discorso("howard_a6", "howard", CONOSCENTI, se="giorno >= 17 and fatto('ep2_pacco_joanie_da_howard')")
    discorso("howard_a7", "howard", CONOSCENTI)
    discorso("howard_a8", "howard", CONOSCENTI)
    discorso("howard_b1", "howard", CONFIDENZA)
    discorso("howard_b2", "howard", CONFIDENZA)
    discorso("howard_b3", "howard", CONFIDENZA, orario=(22 * 60, 2 * 60))
    discorso("howard_b4", "howard", CONFIDENZA)
    discorso("howard_b5", "howard", CONFIDENZA, se="giorno >= 17 and fatto('ep2_corriere_atteso_turno_sara') == giorno")

## Retroscena breve alla fine di una chat (la chat si chiude prima).
label howard_retroscena_chat(testo_rs, testo_diario):
    hide screen telefono_chat
    call inizio_retroscena
    rs "[testo_rs]"
    $ retroscena("howard", testo_diario)
    call fine_retroscena
    return


## --- Introduzione: grazie per le chiavi --------------------------------------

label chat_howard_intro:
    label tel_chat_howard_intro_1:
    if telefono_minuti_blocco("tel_chat_howard_intro_1", "invia", 1):
        return
    $ msg("sara", "Hi Howard, it's Sara. Thank you again for finding my keys. You saved my life.")
    return

label chat_howard_intro_1:
    label tel_chat_howard_intro_1_1:
    if telefono_minuti_blocco("tel_chat_howard_intro_1_1", "ricevi", 4):
        return
    $ msg("howard", "Sara!")
    $ msg("howard", "Oh you don't have to thank me. I was so happy to find them.")
    $ msg("howard", "Under the stairs, can you believe it. Right under our feet all that time.")
    $ msg("howard", "I'm glad you have my number now. For anything. Anything at all. I'm always home.")
    label tel_chat_howard_intro_1_2:
    if telefono_minuti_blocco("tel_chat_howard_intro_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's very kind of you.»":
            label tel_chat_howard_intro_1_3:
            if telefono_minuti_blocco("tel_chat_howard_intro_1_3", "invia", 1):
                return
            $ msg("sara", "That's very kind of you.")
            label tel_chat_howard_intro_1_4:
            if telefono_minuti_blocco("tel_chat_howard_intro_1_4", "ricevi", 1):
                return
            $ msg("howard", "It's nothing. It's what neighbours are for.")
        "«You're a lifesaver, really.»":
            label tel_chat_howard_intro_1_5:
            if telefono_minuti_blocco("tel_chat_howard_intro_1_5", "invia", 1):
                return
            $ msg("sara", "You're a lifesaver, really.")
            $ caldo()
            label tel_chat_howard_intro_1_6:
            if telefono_minuti_blocco("tel_chat_howard_intro_1_6", "ricevi", 2):
                return
            $ msg("howard", "A lifesaver. Nobody ever called me that.")
            $ msg("howard", "I'm going to remember that.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_intro_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_intro_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_intro_2:
    label tel_chat_howard_intro_2_1:
    if telefono_minuti_blocco("tel_chat_howard_intro_2_1", "ricevi", 1):
        return
    $ msg("howard", "Did [nome_compagno] get home all right the other night? I heard your door very late.")
    sp "He heard our door?"
    label tel_chat_howard_intro_2_2:
    if telefono_minuti_blocco("tel_chat_howard_intro_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Yes, a long shift. Sorry about the noise.»":
            label tel_chat_howard_intro_2_3:
            if telefono_minuti_blocco("tel_chat_howard_intro_2_3", "invia", 1):
                return
            $ msg("sara", "Yes, a long shift. Sorry about the noise.")
            label tel_chat_howard_intro_2_4:
            if telefono_minuti_blocco("tel_chat_howard_intro_2_4", "ricevi", 1):
                return
            $ msg("howard", "No noise at all! I just sleep very light. Goodnight Sara.")
        "«You hear everything through those walls, huh :)»":
            label tel_chat_howard_intro_2_5:
            if telefono_minuti_blocco("tel_chat_howard_intro_2_5", "invia", 1):
                return
            $ msg("sara", "You hear everything through those walls, huh :)")
            $ caldo()
            label tel_chat_howard_intro_2_6:
            if telefono_minuti_blocco("tel_chat_howard_intro_2_6", "ricevi", 2):
                return
            $ msg("howard", "Oh no no. Only the door. Only sometimes.")
            $ msg("howard", "Goodnight Sara.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_intro_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_intro_2_2"
            $ telefono_minuti_chiudi = True
            return
    call howard_retroscena_chat("Howard puts the phone down and opens the drawer by the door. Next to his own keys, a new one, still shiny. The copy works perfectly.", "After the chat Howard checked the copy of Sara's key. It works.")
    return


## --- A1: la vita condominiale ------------------------------------------------

label chat_howard_a1:
    label tel_chat_howard_a1_1:
    if telefono_minuti_blocco("tel_chat_howard_a1_1", "invia", 1):
        return
    $ msg("sara", "Howard, do you know who's dragging furniture upstairs at midnight?")
    return

label chat_howard_a1_1:
    label tel_chat_howard_a1_1_1:
    if telefono_minuti_blocco("tel_chat_howard_a1_1_1", "ricevi", 3):
        return
    $ msg("howard", "The Kowalskis. Third floor. They rearrange the living room every Tuesday.")
    $ msg("howard", "And the boy on the fourth floor plays drums on Sundays from 4 to 6.")
    $ msg("howard", "And Mrs. Dean takes the bins out at 6:10 every morning. Like a clock.")
    sp "He knows everyone's schedule. That's... very thorough."
    label tel_chat_howard_a1_1_2:
    if telefono_minuti_blocco("tel_chat_howard_a1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«You know everything about this building.»":
            label tel_chat_howard_a1_1_3:
            if telefono_minuti_blocco("tel_chat_howard_a1_1_3", "invia", 1):
                return
            $ msg("sara", "You know everything about this building.")
            $ caldo()
            label tel_chat_howard_a1_1_4:
            if telefono_minuti_blocco("tel_chat_howard_a1_1_4", "ricevi", 1):
                return
            $ msg("howard", "I've been here a long time. You notice things.")
        "«Thanks. I'll survive until Wednesday then.»":
            label tel_chat_howard_a1_1_5:
            if telefono_minuti_blocco("tel_chat_howard_a1_1_5", "invia", 1):
                return
            $ msg("sara", "Thanks. I'll survive until Wednesday then.")
            label tel_chat_howard_a1_1_6:
            if telefono_minuti_blocco("tel_chat_howard_a1_1_6", "ricevi", 1):
                return
            $ msg("howard", "Ha! Yes. Wednesday is quiet.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_a1_2:
    label tel_chat_howard_a1_2_1:
    if telefono_minuti_blocco("tel_chat_howard_a1_2_1", "ricevi", 1):
        return
    $ msg("howard", "You leave at 8:20, right? The Kowalskis' cat sits on the landing at that time. Watch your step.")
    sp "8:20. Exactly 8:20."
    label tel_chat_howard_a1_2_2:
    if telefono_minuti_blocco("tel_chat_howard_a1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«How do you know when I leave?»":
            label tel_chat_howard_a1_2_3:
            if telefono_minuti_blocco("tel_chat_howard_a1_2_3", "invia", 1):
                return
            $ msg("sara", "How do you know when I leave?")
            label tel_chat_howard_a1_2_4:
            if telefono_minuti_blocco("tel_chat_howard_a1_2_4", "ricevi", 2):
                return
            $ msg("howard", "Oh, I hear your heels on the stairs. Every morning. Very regular.")
            $ msg("howard", "It's a nice sound. It means the day is starting.")
        "«Thanks for the warning :)»":
            label tel_chat_howard_a1_2_5:
            if telefono_minuti_blocco("tel_chat_howard_a1_2_5", "invia", 1):
                return
            $ msg("sara", "Thanks for the warning :)")
            $ caldo()
            label tel_chat_howard_a1_2_6:
            if telefono_minuti_blocco("tel_chat_howard_a1_2_6", "ricevi", 1):
                return
            $ msg("howard", "Anytime. I'll keep an eye out.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A2: problemi domestici --------------------------------------------------

label chat_howard_a2:
    label tel_chat_howard_a2_1:
    if telefono_minuti_blocco("tel_chat_howard_a2_1", "invia", 1):
        return
    $ msg("sara", "Random question: do you know a good plumber? The kitchen tap is dripping all night.")
    return

label chat_howard_a2_1:
    label tel_chat_howard_a2_1_1:
    if telefono_minuti_blocco("tel_chat_howard_a2_1_1", "ricevi", 3):
        return
    $ msg("howard", "A plumber? No no no. Don't waste money.")
    $ msg("howard", "It's the washer. Ten minutes. I can fix it.")
    $ msg("howard", "I have all the tools. I could come tomorrow afternoon.")
    label tel_chat_howard_a2_1_2:
    if telefono_minuti_blocco("tel_chat_howard_a2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Are you sure? I don't want to bother you.»":
            label tel_chat_howard_a2_1_3:
            if telefono_minuti_blocco("tel_chat_howard_a2_1_3", "invia", 1):
                return
            $ msg("sara", "Are you sure? I don't want to bother you.")
            label tel_chat_howard_a2_1_4:
            if telefono_minuti_blocco("tel_chat_howard_a2_1_4", "ricevi", 1):
                return
            $ msg("howard", "Bother! You could never bother me.")
        "«That would be amazing, thank you.»":
            label tel_chat_howard_a2_1_5:
            if telefono_minuti_blocco("tel_chat_howard_a2_1_5", "invia", 1):
                return
            $ msg("sara", "That would be amazing, thank you.")
            $ caldo()
            label tel_chat_howard_a2_1_6:
            if telefono_minuti_blocco("tel_chat_howard_a2_1_6", "ricevi", 1):
                return
            $ msg("howard", "Wonderful. It will be a pleasure.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_a2_2:
    label tel_chat_howard_a2_2_1:
    if telefono_minuti_blocco("tel_chat_howard_a2_2_1", "ricevi", 2):
        return
    $ msg("howard", "What time is [nome_compagno] at work tomorrow? So I know when to come.")
    $ msg("howard", "I mean, so I don't disturb you both. Two people at home and a man under the sink, it's crowded.")
    sp "That's thoughtful of him. I think."
    label tel_chat_howard_a2_2_2:
    if telefono_minuti_blocco("tel_chat_howard_a2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«He's out until seven. Come at four?»":
            label tel_chat_howard_a2_2_3:
            if telefono_minuti_blocco("tel_chat_howard_a2_2_3", "invia", 1):
                return
            $ msg("sara", "He's out until seven. Come at four?")
            label tel_chat_howard_a2_2_4:
            if telefono_minuti_blocco("tel_chat_howard_a2_2_4", "ricevi", 1):
                return
            $ msg("howard", "Four. Perfect. I'll be there at four.")
            $ segna("howard_rubinetto")
        "«Come when we're both home, it's fine.»":
            label tel_chat_howard_a2_2_5:
            if telefono_minuti_blocco("tel_chat_howard_a2_2_5", "invia", 1):
                return
            $ msg("sara", "Come when we're both home, it's fine.")
            label tel_chat_howard_a2_2_6:
            if telefono_minuti_blocco("tel_chat_howard_a2_2_6", "ricevi", 1):
                return
            $ msg("howard", "Oh. Of course. Of course. Saturday then.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A3: cucina casalinga ----------------------------------------------------

label chat_howard_a3:
    label tel_chat_howard_a3_1:
    if telefono_minuti_blocco("tel_chat_howard_a3_1", "invia", 1):
        return
    $ msg("sara", "Howard, the whole stairwell smells amazing. Is that you?")
    return

label chat_howard_a3_entrata:
    label tel_chat_howard_a3_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_a3_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "I made too much lasagna. I always make too much. Old habit.")
    label tel_chat_howard_a3_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_a3_entrata_2", "invia", 1):
        return
    $ msg("sara", "So that's what smells so good in the stairwell!")
    return

label chat_howard_a3_1:
    label tel_chat_howard_a3_1_1:
    if telefono_minuti_blocco("tel_chat_howard_a3_1_1", "ricevi", 2):
        return
    $ msg("howard", "Lasagna. My mother's recipe. It takes four hours.")
    $ msg("howard", "But I always make it for six people and there's only me.")
    label tel_chat_howard_a3_1_2:
    if telefono_minuti_blocco("tel_chat_howard_a3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Four hours! You're patient.»":
            label tel_chat_howard_a3_1_3:
            if telefono_minuti_blocco("tel_chat_howard_a3_1_3", "invia", 1):
                return
            $ msg("sara", "Four hours! You're patient.")
            label tel_chat_howard_a3_1_4:
            if telefono_minuti_blocco("tel_chat_howard_a3_1_4", "ricevi", 1):
                return
            $ msg("howard", "I have time. That's the one thing I have.")
        "«Your mother would be proud.»":
            label tel_chat_howard_a3_1_5:
            if telefono_minuti_blocco("tel_chat_howard_a3_1_5", "invia", 1):
                return
            $ msg("sara", "Your mother would be proud.")
            $ caldo()
            label tel_chat_howard_a3_1_6:
            if telefono_minuti_blocco("tel_chat_howard_a3_1_6", "ricevi", 2):
                return
            $ msg("howard", "She would. She always said I'd make some woman very happy.")
            $ msg("howard", "She was wrong about that.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_a3_2:
    label tel_chat_howard_a3_2_1:
    if telefono_minuti_blocco("tel_chat_howard_a3_2_1", "ricevi", 1):
        return
    $ msg("howard", "Can I bring you a plate? For you and [nome_compagno]. Mostly for you. You're too thin.")
    sp "Too thin. Nobody has ever told me that."
    label tel_chat_howard_a3_2_2:
    if telefono_minuti_blocco("tel_chat_howard_a3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Yes please, that's so sweet.»":
            label tel_chat_howard_a3_2_3:
            if telefono_minuti_blocco("tel_chat_howard_a3_2_3", "invia", 1):
                return
            $ msg("sara", "Yes please, that's so sweet.")
            $ caldo()
            label tel_chat_howard_a3_2_4:
            if telefono_minuti_blocco("tel_chat_howard_a3_2_4", "ricevi", 1):
                return
            $ msg("howard", "I'll leave it at your door in ten minutes. Still warm.")
            $ segna("howard_lasagna")
        "«Thank you, but we already ate.»":
            label tel_chat_howard_a3_2_5:
            if telefono_minuti_blocco("tel_chat_howard_a3_2_5", "invia", 1):
                return
            $ msg("sara", "Thank you, but we already ate.")
            label tel_chat_howard_a3_2_6:
            if telefono_minuti_blocco("tel_chat_howard_a3_2_6", "ricevi", 1):
                return
            $ msg("howard", "Tomorrow then. Lasagna is better the day after.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a3_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A4: film in televisione -------------------------------------------------

label chat_howard_a4:
    label tel_chat_howard_a4_1:
    if telefono_minuti_blocco("tel_chat_howard_a4_1", "invia", 1):
        return
    $ msg("sara", "Do you know any good old films? I want something that isn't a superhero.")
    return

label chat_howard_a4_1:
    label tel_chat_howard_a4_1_1:
    if telefono_minuti_blocco("tel_chat_howard_a4_1_1", "ricevi", 3):
        return
    $ msg("howard", "Oh! Yes. Yes. Old films are my passion.")
    $ msg("howard", "«Last Train Home». Black and white. A woman, married, meets a man at a train station.")
    $ msg("howard", "Nothing happens and everything happens. You'll cry.")
    label tel_chat_howard_a4_1_2:
    if telefono_minuti_blocco("tel_chat_howard_a4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«A married woman and a stranger? Sounds dangerous.»":
            label tel_chat_howard_a4_1_3:
            if telefono_minuti_blocco("tel_chat_howard_a4_1_3", "invia", 1):
                return
            $ msg("sara", "A married woman and a stranger? Sounds dangerous.")
            $ caldo()
            label tel_chat_howard_a4_1_4:
            if telefono_minuti_blocco("tel_chat_howard_a4_1_4", "ricevi", 1):
                return
            $ msg("howard", "The most beautiful things are a little dangerous.")
        "«I'll try it this weekend.»":
            label tel_chat_howard_a4_1_5:
            if telefono_minuti_blocco("tel_chat_howard_a4_1_5", "invia", 1):
                return
            $ msg("sara", "I'll try it this weekend.")
            label tel_chat_howard_a4_1_6:
            if telefono_minuti_blocco("tel_chat_howard_a4_1_6", "ricevi", 1):
                return
            $ msg("howard", "Tell me what you think. I want to know everything you think.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_a4_2:
    label tel_chat_howard_a4_2_1:
    if telefono_minuti_blocco("tel_chat_howard_a4_2_1", "ricevi", 2):
        return
    $ msg("howard", "Sometimes I can hear the music from your films through the wall.")
    $ msg("howard", "The walls are thin. I don't mind. I like hearing you two laugh.")
    sp "I didn't think the TV was that loud."
    label tel_chat_howard_a4_2_2:
    if telefono_minuti_blocco("tel_chat_howard_a4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Sorry! I'll turn it down.»":
            label tel_chat_howard_a4_2_3:
            if telefono_minuti_blocco("tel_chat_howard_a4_2_3", "invia", 1):
                return
            $ msg("sara", "Sorry! I'll turn it down.")
            label tel_chat_howard_a4_2_4:
            if telefono_minuti_blocco("tel_chat_howard_a4_2_4", "ricevi", 1):
                return
            $ msg("howard", "No! Don't. Please. It keeps me company.")
        "«You should come watch one with us sometime.»":
            label tel_chat_howard_a4_2_5:
            if telefono_minuti_blocco("tel_chat_howard_a4_2_5", "invia", 1):
                return
            $ msg("sara", "You should come watch one with us sometime.")
            $ caldo()
            label tel_chat_howard_a4_2_6:
            if telefono_minuti_blocco("tel_chat_howard_a4_2_6", "ricevi", 2):
                return
            $ msg("howard", "Really? You'd let me?")
            $ msg("howard", "I'll bring snacks. Anything you want.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a4_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A5: animali domestici (retroscena) --------------------------------------

label chat_howard_a5:
    label tel_chat_howard_a5_1:
    if telefono_minuti_blocco("tel_chat_howard_a5_1", "invia", 1):
        return
    $ msg("sara", "Howard, was there a cat in your flat once? I keep finding grey hairs on the landing.")
    return

label chat_howard_a5_1:
    label tel_chat_howard_a5_1_1:
    if telefono_minuti_blocco("tel_chat_howard_a5_1_1", "ricevi", 2):
        return
    $ msg("howard", "Duchess. Grey Persian. She died two years ago.")
    $ msg("howard", "Fourteen years together. Longer than any of my relationships. Ha.")
    label tel_chat_howard_a5_1_2:
    if telefono_minuti_blocco("tel_chat_howard_a5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm so sorry.»":
            label tel_chat_howard_a5_1_3:
            if telefono_minuti_blocco("tel_chat_howard_a5_1_3", "invia", 1):
                return
            $ msg("sara", "I'm so sorry.")
            $ caldo()
            label tel_chat_howard_a5_1_4:
            if telefono_minuti_blocco("tel_chat_howard_a5_1_4", "ricevi", 1):
                return
            $ msg("howard", "Thank you. You're the first person who said that.")
        "«Fourteen years is a good long life.»":
            label tel_chat_howard_a5_1_5:
            if telefono_minuti_blocco("tel_chat_howard_a5_1_5", "invia", 1):
                return
            $ msg("sara", "Fourteen years is a good long life.")
            label tel_chat_howard_a5_1_6:
            if telefono_minuti_blocco("tel_chat_howard_a5_1_6", "ricevi", 1):
                return
            $ msg("howard", "It is. She was spoiled. She slept on my pillow.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_a5_2:
    label tel_chat_howard_a5_2_1:
    if telefono_minuti_blocco("tel_chat_howard_a5_2_1", "ricevi", 3):
        return
    $ msg("howard", "You remind me of her a little.")
    $ msg("howard", "Elegant. A bit shy. She only came to me when she wanted something.")
    $ msg("howard", "But when she came, she stayed.")
    sp "That's... a strange compliment. He means it kindly."
    label tel_chat_howard_a5_2_2:
    if telefono_minuti_blocco("tel_chat_howard_a5_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'll take that as a compliment :)»":
            label tel_chat_howard_a5_2_3:
            if telefono_minuti_blocco("tel_chat_howard_a5_2_3", "invia", 1):
                return
            $ msg("sara", "I'll take that as a compliment :)")
            label tel_chat_howard_a5_2_4:
            if telefono_minuti_blocco("tel_chat_howard_a5_2_4", "ricevi", 1):
                return
            $ msg("howard", "It is. The biggest one I have.")
        "«Maybe you should get another cat.»":
            label tel_chat_howard_a5_2_5:
            if telefono_minuti_blocco("tel_chat_howard_a5_2_5", "invia", 1):
                return
            $ msg("sara", "Maybe you should get another cat.")
            label tel_chat_howard_a5_2_6:
            if telefono_minuti_blocco("tel_chat_howard_a5_2_6", "ricevi", 1):
                return
            $ msg("howard", "Maybe. Or maybe I just need better company.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a5_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a5_2_2"
            $ telefono_minuti_chiudi = True
            return
    call howard_retroscena_chat("In Howard's living room, on the armrest next to him, folded with care, there is a piece of lace that does not belong to him. He strokes it while he types.", "Howard keeps Sara's stolen underwear close while he writes to her.")
    return


## --- A6: piccoli favori ------------------------------------------------------

label chat_howard_a6:
    label tel_chat_howard_a6_1:
    if telefono_minuti_blocco("tel_chat_howard_a6_1", "invia", 1):
        return
    $ msg("sara", "Howard, did a courier leave a parcel with you? The tracking says «delivered to neighbour».")
    return

label chat_howard_a6_entrata:
    label tel_chat_howard_a6_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_a6_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "Sara, the courier left a parcel for you. I have it safe. Very safe.")
    label tel_chat_howard_a6_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_a6_entrata_2", "invia", 1):
        return
    $ msg("sara", "Oh thank you! I was looking for it.")
    return

label chat_howard_a6_1:
    label tel_chat_howard_a6_1_1:
    if telefono_minuti_blocco("tel_chat_howard_a6_1_1", "ricevi", 2):
        return
    $ msg("howard", "Yes! It's here. I put it on the kitchen table so nobody steps on it.")
    $ msg("howard", "It's light. Soft. Clothes?")
    sp "Did he shake it?"
    label tel_chat_howard_a6_1_2:
    if telefono_minuti_blocco("tel_chat_howard_a6_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Just a top. Nothing exciting.»":
            label tel_chat_howard_a6_1_3:
            if telefono_minuti_blocco("tel_chat_howard_a6_1_3", "invia", 1):
                return
            $ msg("sara", "Just a top. Nothing exciting.")
            label tel_chat_howard_a6_1_4:
            if telefono_minuti_blocco("tel_chat_howard_a6_1_4", "ricevi", 1):
                return
            $ msg("howard", "I'm sure it will look lovely on you.")
        "«Curious, aren't you? :)»":
            label tel_chat_howard_a6_1_5:
            if telefono_minuti_blocco("tel_chat_howard_a6_1_5", "invia", 1):
                return
            $ msg("sara", "Curious, aren't you? :)")
            $ caldo()
            label tel_chat_howard_a6_1_6:
            if telefono_minuti_blocco("tel_chat_howard_a6_1_6", "ricevi", 1):
                return
            $ msg("howard", "Guilty. I don't get many parcels. I live through other people's.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a6_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a6_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_a6_2:
    label tel_chat_howard_a6_2_1:
    if telefono_minuti_blocco("tel_chat_howard_a6_2_1", "ricevi", 1):
        return
    $ msg("howard", "Come get it whenever. I'll make tea. I have the good biscuits.")
    label tel_chat_howard_a6_2_2:
    if telefono_minuti_blocco("tel_chat_howard_a6_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'll come after work. Five minutes.»":
            label tel_chat_howard_a6_2_3:
            if telefono_minuti_blocco("tel_chat_howard_a6_2_3", "invia", 1):
                return
            $ msg("sara", "I'll come after work. Five minutes.")
            $ caldo()
            label tel_chat_howard_a6_2_4:
            if telefono_minuti_blocco("tel_chat_howard_a6_2_4", "ricevi", 1):
                return
            $ msg("howard", "Five minutes. Wonderful. The kettle will be ready.")
            $ segna("howard_pacco_tea")
        "«Could you leave it at my door? I'm in a rush.»":
            label tel_chat_howard_a6_2_5:
            if telefono_minuti_blocco("tel_chat_howard_a6_2_5", "invia", 1):
                return
            $ msg("sara", "Could you leave it at my door? I'm in a rush.")
            label tel_chat_howard_a6_2_6:
            if telefono_minuti_blocco("tel_chat_howard_a6_2_6", "ricevi", 1):
                return
            $ msg("howard", "Of course. Of course. At your door.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a6_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a6_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A7: abitudini quotidiane ------------------------------------------------

label chat_howard_a7:
    label tel_chat_howard_a7_1:
    if telefono_minuti_blocco("tel_chat_howard_a7_1", "invia", 1):
        return
    $ msg("sara", "How do you fill your days, Howard? I never asked.")
    return

label chat_howard_a7_1:
    label tel_chat_howard_a7_1_1:
    if telefono_minuti_blocco("tel_chat_howard_a7_1_1", "ricevi", 3):
        return
    $ msg("howard", "Oh, a very boring routine. You'll laugh.")
    $ msg("howard", "Up at 6. Coffee. Radio. Crossword. Walk to the market.")
    $ msg("howard", "At 7:40 the pipes start singing, that means you're in the shower and the building is awake.")
    sp "He knows when I shower?"
    label tel_chat_howard_a7_1_2:
    if telefono_minuti_blocco("tel_chat_howard_a7_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«The pipes? Really?»":
            label tel_chat_howard_a7_1_3:
            if telefono_minuti_blocco("tel_chat_howard_a7_1_3", "invia", 1):
                return
            $ msg("sara", "The pipes? Really?")
            label tel_chat_howard_a7_1_4:
            if telefono_minuti_blocco("tel_chat_howard_a7_1_4", "ricevi", 2):
                return
            $ msg("howard", "Old building. Everything echoes. I'm used to all your noises.")
            $ msg("howard", "All the building's noises, I mean.")
        "«Sounds peaceful, actually.»":
            label tel_chat_howard_a7_1_5:
            if telefono_minuti_blocco("tel_chat_howard_a7_1_5", "invia", 1):
                return
            $ msg("sara", "Sounds peaceful, actually.")
            $ caldo()
            label tel_chat_howard_a7_1_6:
            if telefono_minuti_blocco("tel_chat_howard_a7_1_6", "ricevi", 1):
                return
            $ msg("howard", "Peaceful. Yes. Quiet. Too quiet, sometimes.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a7_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a7_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_a7_2:
    label tel_chat_howard_a7_2_1:
    if telefono_minuti_blocco("tel_chat_howard_a7_2_1", "ricevi", 2):
        return
    $ msg("howard", "In the evening I cook, I watch a film, I wait for the day to end.")
    $ msg("howard", "The best part of the day is when I see you on the stairs. Honestly.")
    label tel_chat_howard_a7_2_2:
    if telefono_minuti_blocco("tel_chat_howard_a7_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That's sweet. And a bit sad.»":
            label tel_chat_howard_a7_2_3:
            if telefono_minuti_blocco("tel_chat_howard_a7_2_3", "invia", 1):
                return
            $ msg("sara", "That's sweet. And a bit sad.")
            $ caldo()
            label tel_chat_howard_a7_2_4:
            if telefono_minuti_blocco("tel_chat_howard_a7_2_4", "ricevi", 1):
                return
            $ msg("howard", "A bit sad. Yes. You see me. Not many people do.")
        "«You should join a club or something.»":
            label tel_chat_howard_a7_2_5:
            if telefono_minuti_blocco("tel_chat_howard_a7_2_5", "invia", 1):
                return
            $ msg("sara", "You should join a club or something.")
            label tel_chat_howard_a7_2_6:
            if telefono_minuti_blocco("tel_chat_howard_a7_2_6", "ricevi", 1):
                return
            $ msg("howard", "Maybe. Clubs are full of strangers. You're not a stranger.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a7_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a7_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- A8: la solitudine del weekend (retroscena) ------------------------------

label chat_howard_a8:
    label tel_chat_howard_a8_1:
    if telefono_minuti_blocco("tel_chat_howard_a8_1", "invia", 1):
        return
    $ msg("sara", "Busy weekend, Howard?")
    return

label chat_howard_a8_entrata:
    label tel_chat_howard_a8_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_a8_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "Are you two home this weekend? Just asking. No reason.")
    label tel_chat_howard_a8_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_a8_entrata_2", "invia", 1):
        return
    $ msg("sara", "Probably. Why?")
    return

label chat_howard_a8_1:
    label tel_chat_howard_a8_1_1:
    if telefono_minuti_blocco("tel_chat_howard_a8_1_1", "ricevi", 2):
        return
    $ msg("howard", "Me? Oh, the usual. Nobody calls on Saturdays.")
    $ msg("howard", "Sunday is the worst. The whole building goes out and I stay. Like a guard.")
    label tel_chat_howard_a8_1_2:
    if telefono_minuti_blocco("tel_chat_howard_a8_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That sounds lonely.»":
            label tel_chat_howard_a8_1_3:
            if telefono_minuti_blocco("tel_chat_howard_a8_1_3", "invia", 1):
                return
            $ msg("sara", "That sounds lonely.")
            label tel_chat_howard_a8_1_4:
            if telefono_minuti_blocco("tel_chat_howard_a8_1_4", "ricevi", 1):
                return
            $ msg("howard", "It is. But I'm used to it.")
        "«Come over for coffee on Sunday.»":
            label tel_chat_howard_a8_1_5:
            if telefono_minuti_blocco("tel_chat_howard_a8_1_5", "invia", 1):
                return
            $ msg("sara", "Come over for coffee on Sunday.")
            $ caldo()
            label tel_chat_howard_a8_1_6:
            if telefono_minuti_blocco("tel_chat_howard_a8_1_6", "ricevi", 2):
                return
            $ msg("howard", "Really? Really really?")
            $ msg("howard", "What time? I'll be there. I'll bring the biscuits. The good ones.")
            $ segna("howard_caffe_domenica")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a8_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a8_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_a8_2:
    label tel_chat_howard_a8_2_1:
    if telefono_minuti_blocco("tel_chat_howard_a8_2_1", "ricevi", 1):
        return
    $ msg("howard", "You're the kindest person in this building, Sara. Maybe in this city.")
    sp "Poor Howard. He has nobody."
    label tel_chat_howard_a8_2_2:
    if telefono_minuti_blocco("tel_chat_howard_a8_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Don't exaggerate :)»":
            label tel_chat_howard_a8_2_3:
            if telefono_minuti_blocco("tel_chat_howard_a8_2_3", "invia", 1):
                return
            $ msg("sara", "Don't exaggerate :)")
            label tel_chat_howard_a8_2_4:
            if telefono_minuti_blocco("tel_chat_howard_a8_2_4", "ricevi", 1):
                return
            $ msg("howard", "I never exaggerate about you.")
        "«You deserve a bit of company.»":
            label tel_chat_howard_a8_2_5:
            if telefono_minuti_blocco("tel_chat_howard_a8_2_5", "invia", 1):
                return
            $ msg("sara", "You deserve a bit of company.")
            $ caldo()
            label tel_chat_howard_a8_2_6:
            if telefono_minuti_blocco("tel_chat_howard_a8_2_6", "ricevi", 1):
                return
            $ msg("howard", "I'm starting to believe it.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a8_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_a8_2_2"
            $ telefono_minuti_chiudi = True
            return
    call howard_retroscena_chat("On the kitchen calendar Howard circles Sunday in red. He writes «S.» inside the circle, then a second time, more slowly.", "Howard marks every possible meeting with Sara on his calendar.")
    return


## --- B1: il desiderio di una famiglia ----------------------------------------

label chat_howard_b1:
    label tel_chat_howard_b1_1:
    if telefono_minuti_blocco("tel_chat_howard_b1_1", "invia", 1):
        return
    $ msg("sara", "Howard, can I ask you something personal? Did you ever want children?")
    return

label chat_howard_b1_entrata:
    label tel_chat_howard_b1_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_b1_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "I saw a family on the bus today. Mum, dad, two little ones. I stared like a fool.")
    label tel_chat_howard_b1_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_b1_entrata_2", "invia", 1):
        return
    $ msg("sara", "Did you ever want one? A family?")
    return

label chat_howard_b1_1:
    label tel_chat_howard_b1_1_1:
    if telefono_minuti_blocco("tel_chat_howard_b1_1_1", "ricevi", 3):
        return
    $ msg("howard", "More than anything.")
    $ msg("howard", "A wife who waits for me. Someone to cook for. Someone who needs me.")
    $ msg("howard", "It never happened. Women never saw me. I was always the friend, the neighbour.")
    label tel_chat_howard_b1_1_2:
    if telefono_minuti_blocco("tel_chat_howard_b1_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It's not too late, Howard.»":
            label tel_chat_howard_b1_1_3:
            if telefono_minuti_blocco("tel_chat_howard_b1_1_3", "invia", 1):
                return
            $ msg("sara", "It's not too late, Howard.")
            $ caldo()
            label tel_chat_howard_b1_1_4:
            if telefono_minuti_blocco("tel_chat_howard_b1_1_4", "ricevi", 1):
                return
            $ msg("howard", "You really think so?")
        "«I'm sorry. That must hurt.»":
            label tel_chat_howard_b1_1_5:
            if telefono_minuti_blocco("tel_chat_howard_b1_1_5", "invia", 1):
                return
            $ msg("sara", "I'm sorry. That must hurt.")
            label tel_chat_howard_b1_1_6:
            if telefono_minuti_blocco("tel_chat_howard_b1_1_6", "ricevi", 1):
                return
            $ msg("howard", "Every day. But talking to you helps.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b1_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b1_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_b1_2:
    label tel_chat_howard_b1_2_1:
    if telefono_minuti_blocco("tel_chat_howard_b1_2_1", "ricevi", 2):
        return
    $ msg("howard", "You and [nome_compagno] will have beautiful children.")
    $ msg("howard", "He's a lucky man. I hope he knows it. I hope he never leaves you alone too much.")
    sp "Why does that sound like a warning?"
    label tel_chat_howard_b1_2_2:
    if telefono_minuti_blocco("tel_chat_howard_b1_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«He knows. Don't worry.»":
            label tel_chat_howard_b1_2_3:
            if telefono_minuti_blocco("tel_chat_howard_b1_2_3", "invia", 1):
                return
            $ msg("sara", "He knows. Don't worry.")
            $ interest("josh", 1)
            label tel_chat_howard_b1_2_4:
            if telefono_minuti_blocco("tel_chat_howard_b1_2_4", "ricevi", 1):
                return
            $ msg("howard", "Good. Good.")
        "«He works a lot, lately.»":
            label tel_chat_howard_b1_2_5:
            if telefono_minuti_blocco("tel_chat_howard_b1_2_5", "invia", 1):
                return
            $ msg("sara", "He works a lot, lately.")
            label tel_chat_howard_b1_2_6:
            if telefono_minuti_blocco("tel_chat_howard_b1_2_6", "ricevi", 2):
                return
            $ msg("howard", "I know. I hear him leave early and come back late.")
            $ msg("howard", "If you ever feel alone in there, I'm here. Just a wall away.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b1_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b1_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B2: le occasioni perdute ------------------------------------------------

label chat_howard_b2:
    label tel_chat_howard_b2_1:
    if telefono_minuti_blocco("tel_chat_howard_b2_1", "invia", 1):
        return
    $ msg("sara", "Was there ever someone special, Howard?")
    return

label chat_howard_b2_1:
    label tel_chat_howard_b2_1_1:
    if telefono_minuti_blocco("tel_chat_howard_b2_1_1", "ricevi", 3):
        return
    $ msg("howard", "Once. Margaret. Thirty years ago. She worked at the post office.")
    $ msg("howard", "I bought stamps every day for a year. I had three thousand stamps.")
    $ msg("howard", "I never asked her out. She married a mechanic.")
    label tel_chat_howard_b2_1_2:
    if telefono_minuti_blocco("tel_chat_howard_b2_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Three thousand stamps! Howard!»":
            label tel_chat_howard_b2_1_3:
            if telefono_minuti_blocco("tel_chat_howard_b2_1_3", "invia", 1):
                return
            $ msg("sara", "Three thousand stamps! Howard!")
            $ caldo()
            label tel_chat_howard_b2_1_4:
            if telefono_minuti_blocco("tel_chat_howard_b2_1_4", "ricevi", 1):
                return
            $ msg("howard", "I still have them. I can't throw them away.")
        "«Why didn't you ask?»":
            label tel_chat_howard_b2_1_5:
            if telefono_minuti_blocco("tel_chat_howard_b2_1_5", "invia", 1):
                return
            $ msg("sara", "Why didn't you ask?")
            label tel_chat_howard_b2_1_6:
            if telefono_minuti_blocco("tel_chat_howard_b2_1_6", "ricevi", 1):
                return
            $ msg("howard", "Because I knew the answer. I always know the answer.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b2_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b2_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_b2_2:
    label tel_chat_howard_b2_2_1:
    if telefono_minuti_blocco("tel_chat_howard_b2_2_1", "ricevi", 2):
        return
    $ msg("howard", "I promised myself: next time I won't wait. I'll do something.")
    $ msg("howard", "Even if it's small. Even if nobody notices.")
    sp "I hope he finds someone. He really deserves it."
    label tel_chat_howard_b2_2_2:
    if telefono_minuti_blocco("tel_chat_howard_b2_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Good. Don't wait anymore.»":
            label tel_chat_howard_b2_2_3:
            if telefono_minuti_blocco("tel_chat_howard_b2_2_3", "invia", 1):
                return
            $ msg("sara", "Good. Don't wait anymore.")
            $ caldo()
            label tel_chat_howard_b2_2_4:
            if telefono_minuti_blocco("tel_chat_howard_b2_2_4", "ricevi", 1):
                return
            $ msg("howard", "I won't. Thank you, Sara. You give me courage.")
        "«Small things count.»":
            label tel_chat_howard_b2_2_5:
            if telefono_minuti_blocco("tel_chat_howard_b2_2_5", "invia", 1):
                return
            $ msg("sara", "Small things count.")
            label tel_chat_howard_b2_2_6:
            if telefono_minuti_blocco("tel_chat_howard_b2_2_6", "ricevi", 1):
                return
            $ msg("howard", "They do. They count a lot.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b2_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b2_2_2"
            $ telefono_minuti_chiudi = True
            return
    return


## --- B3: la paura di invecchiare solo (retroscena) ---------------------------

label chat_howard_b3:
    label tel_chat_howard_b3_1:
    if telefono_minuti_blocco("tel_chat_howard_b3_1", "invia", 1):
        return
    $ msg("sara", "You were very quiet on the stairs today. Are you ok?")
    return

label chat_howard_b3_entrata:
    label tel_chat_howard_b3_entrata_1:
    if telefono_minuti_blocco("tel_chat_howard_b3_entrata_1", "ricevi", 1):
        return
    $ msg("howard", "Sorry to write so late. I can't sleep.")
    label tel_chat_howard_b3_entrata_2:
    if telefono_minuti_blocco("tel_chat_howard_b3_entrata_2", "invia", 1):
        return
    $ msg("sara", "It's ok. What's wrong?")
    return

label chat_howard_b3_1:
    label tel_chat_howard_b3_1_1:
    if telefono_minuti_blocco("tel_chat_howard_b3_1_1", "ricevi", 3):
        return
    $ msg("howard", "I went to the doctor. Nothing serious. Blood pressure.")
    $ msg("howard", "But in the waiting room they asked «who should we call in case of emergency».")
    $ msg("howard", "And I had nobody to write. Nobody, Sara.")
    label tel_chat_howard_b3_1_2:
    if telefono_minuti_blocco("tel_chat_howard_b3_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«Write my name.»":
            label tel_chat_howard_b3_1_3:
            if telefono_minuti_blocco("tel_chat_howard_b3_1_3", "invia", 1):
                return
            $ msg("sara", "Write my name.")
            $ caldo()
            label tel_chat_howard_b3_1_4:
            if telefono_minuti_blocco("tel_chat_howard_b3_1_4", "ricevi", 2):
                return
            $ msg("howard", "...")
            $ msg("howard", "Do you mean it?")
            label tel_chat_howard_b3_1_5:
            if telefono_minuti_blocco("tel_chat_howard_b3_1_5", "invia", 1):
                return
            $ msg("sara", "Of course. We're neighbours.")
            $ segna("howard_contatto_emergenza")
        "«Oh Howard. I'm so sorry.»":
            label tel_chat_howard_b3_1_6:
            if telefono_minuti_blocco("tel_chat_howard_b3_1_6", "invia", 1):
                return
            $ msg("sara", "Oh Howard. I'm so sorry.")
            label tel_chat_howard_b3_1_7:
            if telefono_minuti_blocco("tel_chat_howard_b3_1_7", "ricevi", 1):
                return
            $ msg("howard", "Don't be. It's my life. I chose it. Or it chose me.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b3_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b3_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_b3_2:
    label tel_chat_howard_b3_2_1:
    if telefono_minuti_blocco("tel_chat_howard_b3_2_1", "ricevi", 2):
        return
    $ msg("howard", "I'm afraid of dying in this flat and nobody noticing for weeks.")
    $ msg("howard", "Sorry. Sorry. I'm crying like an idiot. Forget it.")
    sp "He's crying. Alone, next door."
    label tel_chat_howard_b3_2_2:
    if telefono_minuti_blocco("tel_chat_howard_b3_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I would notice. I promise.»":
            label tel_chat_howard_b3_2_3:
            if telefono_minuti_blocco("tel_chat_howard_b3_2_3", "invia", 1):
                return
            $ msg("sara", "I would notice. I promise.")
            $ caldo()
            label tel_chat_howard_b3_2_4:
            if telefono_minuti_blocco("tel_chat_howard_b3_2_4", "ricevi", 1):
                return
            $ msg("howard", "Thank you. Goodnight, Sara. You're an angel.")
        "«Try to sleep. We'll talk tomorrow.»":
            label tel_chat_howard_b3_2_5:
            if telefono_minuti_blocco("tel_chat_howard_b3_2_5", "invia", 1):
                return
            $ msg("sara", "Try to sleep. We'll talk tomorrow.")
            label tel_chat_howard_b3_2_6:
            if telefono_minuti_blocco("tel_chat_howard_b3_2_6", "ricevi", 1):
                return
            $ msg("howard", "Tomorrow. Yes. Goodnight.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b3_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b3_2_2"
            $ telefono_minuti_chiudi = True
            return
    call howard_retroscena_chat("Howard's eyes are perfectly dry. He reads her last message twice, smiles, and switches off the lamp. «An angel.»", "Howard's tears in the chat were fake: he was smiling.")
    return


## --- B4: sentirsi finalmente ascoltato (retroscena) --------------------------

label chat_howard_b4:
    label tel_chat_howard_b4_1:
    if telefono_minuti_blocco("tel_chat_howard_b4_1", "invia", 1):
        return
    $ msg("sara", "How are you today, Howard? Better?")
    return

label chat_howard_b4_1:
    label tel_chat_howard_b4_1_1:
    if telefono_minuti_blocco("tel_chat_howard_b4_1_1", "ricevi", 3):
        return
    $ msg("howard", "Better. Because you asked.")
    $ msg("howard", "Do you know you're the only person who asks me how I am?")
    $ msg("howard", "Forty years in this city and you're the only one.")
    label tel_chat_howard_b4_1_2:
    if telefono_minuti_blocco("tel_chat_howard_b4_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«That can't be true.»":
            label tel_chat_howard_b4_1_3:
            if telefono_minuti_blocco("tel_chat_howard_b4_1_3", "invia", 1):
                return
            $ msg("sara", "That can't be true.")
            label tel_chat_howard_b4_1_4:
            if telefono_minuti_blocco("tel_chat_howard_b4_1_4", "ricevi", 1):
                return
            $ msg("howard", "It is. I counted.")
        "«Then I'll keep asking.»":
            label tel_chat_howard_b4_1_5:
            if telefono_minuti_blocco("tel_chat_howard_b4_1_5", "invia", 1):
                return
            $ msg("sara", "Then I'll keep asking.")
            $ caldo()
            label tel_chat_howard_b4_1_6:
            if telefono_minuti_blocco("tel_chat_howard_b4_1_6", "ricevi", 1):
                return
            $ msg("howard", "Every day?")
            label tel_chat_howard_b4_1_7:
            if telefono_minuti_blocco("tel_chat_howard_b4_1_7", "invia", 1):
                return
            $ msg("sara", "Every day you want.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b4_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b4_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_b4_2:
    label tel_chat_howard_b4_2_1:
    if telefono_minuti_blocco("tel_chat_howard_b4_2_1", "ricevi", 2):
        return
    $ msg("howard", "I read our messages again sometimes. When the evening is long.")
    $ msg("howard", "Is that strange? Tell me if it's strange.")
    sp "It is a little strange. But he's lonely."
    label tel_chat_howard_b4_2_2:
    if telefono_minuti_blocco("tel_chat_howard_b4_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«It's not strange. It's sweet.»":
            label tel_chat_howard_b4_2_3:
            if telefono_minuti_blocco("tel_chat_howard_b4_2_3", "invia", 1):
                return
            $ msg("sara", "It's not strange. It's sweet.")
            $ caldo()
            label tel_chat_howard_b4_2_4:
            if telefono_minuti_blocco("tel_chat_howard_b4_2_4", "ricevi", 1):
                return
            $ msg("howard", "Sweet. I'll remember that word too.")
        "«A little strange :) But ok.»":
            label tel_chat_howard_b4_2_5:
            if telefono_minuti_blocco("tel_chat_howard_b4_2_5", "invia", 1):
                return
            $ msg("sara", "A little strange :) But ok.")
            label tel_chat_howard_b4_2_6:
            if telefono_minuti_blocco("tel_chat_howard_b4_2_6", "ricevi", 1):
                return
            $ msg("howard", "Ha. I'll try to be less strange. For you.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b4_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b4_2_2"
            $ telefono_minuti_chiudi = True
            return
    call howard_retroscena_chat("On Howard's computer a folder called «S» grows every night: every message, every photo she has ever posted, sorted by date.", "Howard archives everything Sara writes and posts, in a folder called «S».")
    return


## --- B5: Sara come presenza rassicurante -------------------------------------

label chat_howard_b5:
    label tel_chat_howard_b5_1:
    if telefono_minuti_blocco("tel_chat_howard_b5_1", "invia", 1):
        return
    $ msg("sara", "I'm working late tonight. Could you tell me if the courier comes? Sorry to ask.")
    return

label chat_howard_b5_1:
    label tel_chat_howard_b5_1_1:
    if telefono_minuti_blocco("tel_chat_howard_b5_1_1", "ricevi", 2):
        return
    $ msg("howard", "Of course! I'll stand by the door. Don't worry about anything.")
    $ msg("howard", "It's nice to be useful to someone. To you.")
    label tel_chat_howard_b5_1_2:
    if telefono_minuti_blocco("tel_chat_howard_b5_1_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«What would I do without you?»":
            label tel_chat_howard_b5_1_3:
            if telefono_minuti_blocco("tel_chat_howard_b5_1_3", "invia", 1):
                return
            $ msg("sara", "What would I do without you?")
            $ caldo()
            label tel_chat_howard_b5_1_4:
            if telefono_minuti_blocco("tel_chat_howard_b5_1_4", "ricevi", 1):
                return
            $ msg("howard", "You'd manage. But I'm glad you don't have to.")
        "«Thank you, Howard.»":
            label tel_chat_howard_b5_1_5:
            if telefono_minuti_blocco("tel_chat_howard_b5_1_5", "invia", 1):
                return
            $ msg("sara", "Thank you, Howard.")
            label tel_chat_howard_b5_1_6:
            if telefono_minuti_blocco("tel_chat_howard_b5_1_6", "ricevi", 1):
                return
            $ msg("howard", "Always.")
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b5_1_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b5_1_2"
            $ telefono_minuti_chiudi = True
            return
    return

label chat_howard_b5_2:
    label tel_chat_howard_b5_2_1:
    if telefono_minuti_blocco("tel_chat_howard_b5_2_1", "ricevi", 2):
        return
    $ msg("howard", "Can I tell you something? When I know you're home, I sleep better.")
    $ msg("howard", "It's like having a light on in the corridor.")
    sp "Like a light in the corridor. He needs someone so badly."
    label tel_chat_howard_b5_2_2:
    if telefono_minuti_blocco("tel_chat_howard_b5_2_2", "scelta"):
        return
    menu (screen="scelta_telefono"):
        "«I'm glad I help. Really.»":
            label tel_chat_howard_b5_2_3:
            if telefono_minuti_blocco("tel_chat_howard_b5_2_3", "invia", 1):
                return
            $ msg("sara", "I'm glad I help. Really.")
            $ caldo()
            label tel_chat_howard_b5_2_4:
            if telefono_minuti_blocco("tel_chat_howard_b5_2_4", "ricevi", 1):
                return
            $ msg("howard", "You help more than you know.")
            $ segna("howard_luce_corridoio")
        "«You should meet more people, Howard. Not just me.»":
            label tel_chat_howard_b5_2_5:
            if telefono_minuti_blocco("tel_chat_howard_b5_2_5", "invia", 1):
                return
            $ msg("sara", "You should meet more people, Howard. Not just me.")
            label tel_chat_howard_b5_2_6:
            if telefono_minuti_blocco("tel_chat_howard_b5_2_6", "ricevi", 2):
                return
            $ msg("howard", "...")
            $ msg("howard", "You're right. Of course. Goodnight.")
            sp "Did I hurt him?"
        "Back to messages." if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b5_2_2"
            return
        "[telefono_minuti_uscita]" if telefono_minuti_attivo():
            $ telefono_minuti_riprese[chat_aperta] = "tel_chat_howard_b5_2_2"
            $ telefono_minuti_chiudi = True
            return
    return
