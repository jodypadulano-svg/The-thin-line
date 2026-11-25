## Test del giorno 20: Magnus, il pomeriggio (palestra, Joanie, scrivere), la cena, la notte.
## Il telefono della notte si chiude da solo (telefono_pilota): nessun clic, nessun mouse.

label test_giorno20:
    call ep2_d20
    $ segna("test_giorno20_finito")
    jump test_giorno20_fermo

label test_giorno20_fermo:
    pause
    jump test_giorno20_fermo

init python:
    def _d20_pilota():
        return ("chiudi", None)

    _D20_LUCK, _D20_TONIGHT = "«Wish me luck.»", "«I'll tell you about it tonight.»"
    D20_SCELTE = {
        "verde_palestra": [_D20_LUCK, "Listen to him.", "Read it to him.", "The gym.", "«I know about you and Joanie.»",
                           "Stay for a stretch.", "Be here, all the way.", "Leave it in the bag."],
        "palestra_zitta": [_D20_TONIGHT, "Listen to him.", "Read it to him.", "The gym.", "Say nothing.",
                           "Shower. Dinner.", "Listen to him, smiling.", "Leave it in the bag."],
        "joanie_parla": [_D20_TONIGHT, "Ask him how to make it better.", "Ask him to read it.", "Joanie's.",
                         "«We're talking about him.»", "Somewhere else.", "Look at it."],
        "joanie_tace": [_D20_LUCK, "Listen to him.", "Ask him to read it.", "Joanie's.",
                        "«We're not talking about him.»", "Be here, all the way.", "Leave it in the bag."],
        "scrive_altro": [_D20_LUCK, "Listen to him.", "Read it to him.", "Home. The book.",
                         "She goes to the one outside.", "Listen to him, smiling.", "Leave it in the bag."],
        "scrive_fidanzato": [_D20_TONIGHT, "Ask him how to make it better.", "Read it to him.", "Home. The book.",
                             "She goes back in to the one who's laughing.", "Be here, all the way.", "Leave it in the bag."],
        "scrive_sola": [_D20_TONIGHT, "Ask him how to make it better.", "Ask him to read it.", "Home. The book.",
                        "She goes home alone, and walks.", "Somewhere else.", "Look at it."],
    }
    ## Josh, Magnus, Simon, Joanie, Jacob, Corruption, Confidence, Suspicion.
    D20_ATTESI = {
        "verde_palestra":   (5, 3, 5, 0, 0, 1, 4, 0),
        "palestra_zitta":   (0, 3, 2, 0, 0, 0, 3, 0),
        "joanie_parla":     (-2, 3, 0, 2, 1, 2, 3, 2),
        "joanie_tace":      (5, 4, 0, 2, 0, 0, 3, 0),
        "scrive_altro":     (1, 3, 0, 0, 0, 1, 5, 0),
        "scrive_fidanzato": (5, 2, 0, 0, 0, 0, 6, 0),
        "scrive_sola":      (-2, 3, 0, 0, 0, 1, 6, 2),
    }

    def _d20_stato():
        return (valore_interest("josh"), valore_interest("editore"), valore_interest("simon"), valore_interest("amica"),
                valore_interest("ex"), store.sara_corruption, store.sara_confidence, store.josh_suspicion)

testsuite giorno20:
    testcase bivi:
        parameter ramo = ["verde_palestra", "palestra_zitta", "joanie_parla", "joanie_tace", "scrive_altro", "scrive_fidanzato", "scrive_sola"]
        $ debug_azzera_stato()
        $ _d20_scelte = list(D20_SCELTE[ramo])
        $ _test_menu_giorno15(_d20_scelte)
        $ telefono_pilota = _d20_pilota
        $ giorno_entrata = 20
        ## Josh sopra 30 (serata romantica) e lontano dal massimo, che nasconderebbe gli aumenti.
        $ interest_josh = 50
        $ sara_corruption = 20
        $ josh_suspicion = 5
        $ segna("ep2_d19_abito_samantha", ramo in ("verde_palestra", "joanie_tace"))
        $ segna("ep2_d19_abito_suo", ramo in ("joanie_parla", "scrive_altro"))
        $ segna("ep2_d15_litigio_josh", ramo in ("joanie_parla", "scrive_sola"))
        $ segna("ep2_d18_pranzo_daniel", ramo in ("joanie_parla", "scrive_altro"))
        $ segna("ep1_d13_magnus_pagine", ramo in ("verde_palestra", "scrive_sola"))
        $ segna("ep1_d7_josh_precoce", ramo == "joanie_tace")
        $ segna("ep2_d19_sa_di_simon", ramo == "verde_palestra")
        $ sara_bad_girl = ramo == "joanie_parla"
        $ interest("daniel", 25 if ramo == "scrive_altro" else 0)
        $ da_numero("daniel")
        $ _d20_prima = _d20_stato()
        $ segna("test_giorno20_finito", False)
        run Jump("test_giorno20")
        advance until eval fatto("test_giorno20_finito") timeout 120.0
        $ telefono_pilota = None
        assert eval not _d20_scelte
        assert eval not in_retroscena
        $ _d20_dopo = _d20_stato()
        $ print("GIORNO20", ramo, [b - a for a, b in zip(_d20_prima, _d20_dopo)])
        assert eval tuple(b - a for a, b in zip(_d20_prima, _d20_dopo)) == D20_ATTESI[ramo]
        assert eval giorno == 20 and percorso("editore").tappa >= 2
        assert eval fatto("ep2_d20_serata_romantica") == ("Be here, all the way." in D20_SCELTE[ramo])
        assert eval sum(bool(fatto("ep2_d20_romanzo_" + x)) for x in ("altro", "fidanzato", "sola")) == ramo.startswith("scrive")
        ## La chat di trama: Daniel dopo il pranzo, altrimenti Joanie; non consuma le chat libere.
        assert eval (chat_log.get("daniel", []) != []) == (ramo in ("joanie_parla", "scrive_altro"))
        assert eval not discorsi_fatti and not giorno_tipo
        ## Samantha non viene mai nominata, il cassetto sì.
        assert eval len([x for x in percorso("editore").sai_tu if "page fifty" in x]) == 1
