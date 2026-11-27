## Test del giorno 24: pranzo con Darius, pomeriggio (inchiesta o lavoro), serata di Josh, romanzo a casa,
## le sei uscite (Jacob #1, Simon, Daniel al jazz club, Joanie, Darius, Howard) e i rischi del mercoledì.
## I tiri di Howard (50%) e Mark (25%) sono forzati per avere un esito certo.

label test_giorno24:
    call ep2_d24
    $ segna("test_giorno24_finito")
    jump test_giorno24_fermo

label test_giorno24_fermo:
    pause
    jump test_giorno24_fermo

init python:
    def _d24_pilota():
        return ("chiudi", None)

    _D24_TIENI, _D24_DAI = "Keep them for now.", "Give him the fifty pages."
    _D24_RESTA, _D24_TORNA = "«One more…»", "«I should get back.»"
    _D24_SCUSA_J, _D24_SCUSA_P = "«I was at Joanie's.»", "«Just a walk. I couldn't settle.»"
    D24_SCELTE = {
        ## Resta a casa: pista dell'indirizzo, Howard in casa ma Sara va a casa, tiene le pagine.
        "romanzo": [_D24_TIENI, "Go home."],
        ## Jacob, serata piena: pagine a Darius, Joanie la copre, Howard la vede e tace,
        ## Lighthouse smitizzato, «One more…» e scusa di Joanie.
        "jacob_pieno": [_D24_DAI, "Text Joanie: «Cover for me tonight?»", "Let herself remember them.",
                        "Give him the point, and laugh it off.", _D24_RESTA, _D24_SCUSA_J],
        ## Jacob, quadro intero: Howard lo dice a Josh e Mark parla; scusa della passeggiata.
        "jacob_breve": [_D24_TIENI, "Keep the whole picture.", _D24_SCUSA_P],
        ## Jacob rivalutato, Sara s'infastidisce e torna in tempo; Joanie lasciata fuori.
        "jacob_fastidio": [_D24_TIENI, "Leave Joanie out of it.", "Let herself remember them.",
                           "Don't. Don't make it a thing.", _D24_TORNA],
        ## Simon: complimento, impegno in palestra, resta di più.
        "simon": [_D24_TIENI, "«It suits you. Really.»", "«Deal. I'll come more often.»", _D24_RESTA, _D24_SCUSA_J],
        ## Daniel, tutto: top di Joanie, grembo, spalla, sfottò accettato, confessione (Corr 50, Daniel 32).
        "daniel_pieno": [_D24_TIENI, "Joanie's black top again.", "Sit on his knee.", "Rest her head on his shoulder.",
                         "Stay in the spell and play along.", "Admit it.", _D24_RESTA, _D24_SCUSA_J],
        ## Daniel, soglie minime dello sfottò (Corr 40, Daniel 25): Sara difende Josh.
        "daniel_difende": [_D24_TIENI, "The good grey dress.", "«I'll wait for the chair.»",
                           "Rest her head on his shoulder.", "Defend [nome_compagno].", _D24_TORNA],
        ## Joanie: due confidenze, poi «That's everything.» (niente «One more…»).
        "amica": [_D24_TIENI, "Jacob's back.", "Lunch with Darius.", "«That's everything.»"],
        ## Darius: pagine, gli chiede di lui, abbraccio, torna in tempo.
        "amico": [_D24_DAI, "Ask him about himself.", "Hug him goodbye.", _D24_TORNA],
        ## Howard: coperta, braccio, finto sonno; resta di più.
        "howard": [_D24_TIENI, "Share the blanket.", "Let it be.", "Let him sleep.", _D24_RESTA, _D24_SCUSA_J],
    }
    D24_APPUNTAMENTO = {"romanzo": None, "jacob_pieno": "ex", "jacob_breve": "ex", "jacob_fastidio": "ex",
                        "simon": "simon", "daniel_pieno": "daniel", "daniel_difende": "daniel",
                        "amica": "amica", "amico": "amico", "howard": "howard"}
    D24_TIRI = {"jacob_pieno": {"howard": True, "mark": True}, "jacob_breve": {"howard": True, "mark": True}}
    D24_CORRUPTION = {"daniel_pieno": 49, "daniel_difende": 39}
    D24_DANIEL = {"daniel_pieno": 30, "daniel_difende": 24}

    ## Jacob, Darius, Howard, Simon, Daniel, Joanie, Josh, Corruption, Confidence, Suspicion.
    D24_ATTESI = {
        "romanzo":        (0, 1, 0, 0, 0, 0, 0, 0, 1, 0),
        "jacob_pieno":    (4, 3, 0, 0, 0, 0, 0, 1, 0, 2),
        "jacob_breve":    (0, 1, 0, 0, 0, 0, 0, 1, 0, 5),
        "jacob_fastidio": (2, 1, 0, 0, 0, 0, 0, 1, 1, 0),
        "simon":          (0, 1, 0, 4, 0, 0, 0, 1, 0, 2),
        "daniel_pieno":   (0, 1, 0, 0, 17, 0, 0, 3, 0, 2),
        "daniel_difende": (0, 1, 0, 0, 2, 0, 1, 1, 0, 0),
        "amica":          (0, 1, 0, 0, 0, 2, 0, 1, 0, 0),
        "amico":          (0, 5, 0, 0, 0, 0, 0, 1, 0, 0),
        "howard":         (0, 1, 5, 0, 0, 0, 0, 1, 0, 2),
    }

    def _d24_stato():
        return (valore_interest("ex"), valore_interest("amico"), valore_interest("howard"),
                valore_interest("simon"), valore_interest("daniel"), valore_interest("amica"),
                valore_interest("josh"), store.sara_corruption, store.sara_confidence, store.josh_suspicion)

testsuite giorno24:
    testcase bivi:
        parameter ramo = ["romanzo", "jacob_pieno", "jacob_breve", "jacob_fastidio", "simon",
                          "daniel_pieno", "daniel_difende", "amica", "amico", "howard"]
        $ debug_azzera_stato()
        $ _d24_scelte = list(D24_SCELTE[ramo])
        $ _test_menu_giorno15(_d24_scelte)
        $ telefono_pilota = _d24_pilota
        $ giorno_entrata = 24
        $ interest_josh = 50
        $ sara_corruption = D24_CORRUPTION.get(ramo, 20)
        $ josh_suspicion = 5
        $ redazione_prossimo_evento = len(REDAZIONE_EVENTI)
        $ ep2_d24_appuntamento = D24_APPUNTAMENTO[ramo]
        $ ep2_d24_tiri_forzati = dict(D24_TIRI.get(ramo, {"howard": False, "mark": False}))
        $ _accettata = ramo in ("romanzo", "jacob_fastidio")
        $ segna("ep2_d22_inchiesta_accettata", _accettata)
        $ segna("ep2_d22_inchiesta_rifiutata", not _accettata)
        $ segna("ep2_d23_nadia_luogo_ritrovamento", ramo == "romanzo")
        $ segna("ep2_d23_nadia_versione_ufficiale", ramo == "jacob_fastidio")
        $ segna("ep2_d23_magnus_responso")
        $ segna("jacob_tornato")
        $ segna("ep2_d17_top_ricevuto", ramo == "daniel_pieno")
        $ segna("ep2_d22_consola_josh", ramo == "jacob_pieno")
        $ percorso("howard").interest = {"romanzo": 60, "jacob_pieno": 10, "howard": 20}.get(ramo, 0)
        $ percorso("amica").interest = 15 if ramo in ("jacob_pieno", "jacob_fastidio", "amica") else 0
        $ percorso("ex").interest = 10
        $ percorso("amico").interest = 0
        $ percorso("simon").interest = 20
        $ percorso("daniel").interest = D24_DANIEL.get(ramo, 0)
        $ (ramo in ("jacob_pieno", "jacob_fastidio")) and da_numero("amica")
        $ _d24_prima = _d24_stato()
        $ segna("test_giorno24_finito", False)
        run Jump("test_giorno24")
        advance until eval fatto("test_giorno24_finito") timeout 120.0
        $ telefono_pilota = None
        $ ep2_d24_tiri_forzati = {}
        $ print("GIORNO24", ramo, [b - a for a, b in zip(_d24_prima, _d24_stato())])
        assert eval not _d24_scelte
        assert eval tuple(b - a for a, b in zip(_d24_prima, _d24_stato())) == D24_ATTESI[ramo]
        assert eval giorno == 24 and not in_retroscena
        assert eval bool(fatto("ep2_d24_romanzo")) == (ramo == "romanzo")
        assert eval ("ep2_d24_uscita" in segreti) == (ramo != "romanzo")
        assert eval bool(fatto("ep2_d24_darius_pagine")) == (ramo in ("jacob_pieno", "amico"))
        assert eval bool(fatto("jacob_incontro_1")) == ramo.startswith("jacob")
        assert eval bool(fatto("jacob_1_rivalutato")) == (ramo in ("jacob_pieno", "jacob_fastidio"))
        assert eval bool(fatto("ep2_d24_joanie_copre")) == (ramo == "jacob_pieno")
        assert eval bool(fatto("ep2_d24_howard_tace")) == (ramo == "jacob_pieno")
        assert eval bool(fatto("ep2_d24_howard_dice")) == (ramo == "jacob_breve")
        assert eval bool(fatto("ep2_d24_mark_parla")) == (ramo == "jacob_breve")
        assert eval bool(fatto("ep2_d24_tardi")) == (ramo in ("jacob_pieno", "simon", "daniel_pieno", "howard"))
        assert eval bool(fatto("ep2_d24_nadia_fiori")) == (ramo == "romanzo")
        assert eval bool(fatto("ep2_d24_nadia_date")) == (ramo == "jacob_fastidio")
        assert eval bool(fatto("simon_palestra_frequente")) == (ramo == "simon")
        assert eval bool(fatto("ep2_d24_confessa_daniel")) == (ramo == "daniel_pieno")
        assert eval bool(fatto("ep2_d24_difende_josh")) == (ramo == "daniel_difende")
        assert eval bool(fatto("ep2_d24_howard_dorme")) == (ramo == "howard")
        assert eval howard_visite == 0
        assert eval not barbara_missioni_completate
