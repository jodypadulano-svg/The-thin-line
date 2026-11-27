## Test del giorno 23: redazione, inchiesta (tre piste) o lavoro ordinario, Magnus, palestra con
## l'eventuale invito a Simon, Howard al rientro, cena, telefono per il mercoledì.
## Punteggi approvati da Jody il 27/11; si controllano anche flag e appuntamento del 24.
## L'evento ordinario della redazione (25%) è escluso per avere un esito certo.

label test_giorno23:
    call ep2_d23
    $ segna("test_giorno23_finito")
    jump test_giorno23_fermo

label test_giorno23_fermo:
    pause
    jump test_giorno23_fermo

init python:
    def _d23_pilota():
        return ("chiudi", None)

    _D23_ARCHIVIO = "Trace the newspaper brief in the archive."
    _D23_POLIZIA = "Ask at the police station."
    _D23_SUPERMERCATO = "Try the supermarket on the receipt."
    _D23_SIMON, _D23_NO_SIMON = "Ask Simon if he's free tomorrow.", "Leave it there."
    _D23_HOWARD, _D23_CASA = "Offer to help Howard.", "Go home."
    D23_SCELTE = {
        ## Archivio, invito a Simon in palestra: niente telefono la sera.
        "archivio_simon": [_D23_ARCHIVIO, _D23_SIMON],
        ## Commissariato, Simon lasciato stare, faccenda da Howard, invito a Joanie col telefono.
        "polizia_joanie": [_D23_POLIZIA, _D23_NO_SIMON, _D23_HOWARD, "Text Joanie."],
        ## Supermercato; Jacob ha già invitato Sara il 21: niente Simon e niente telefono.
        "supermercato_jacob": [_D23_SUPERMERCATO],
        ## Inchiesta rifiutata, Howard in casa ma Sara torna a casa, invito a Daniel.
        "rifiuto_daniel": [_D23_CASA, "Text Daniel."],
        ## Inchiesta rifiutata e nessuno da invitare: telefono posato.
        "rifiuto_nessuno": ["Put the phone down."],
    }
    D23_APPUNTAMENTO = {
        "archivio_simon": "simon", "polizia_joanie": "amica", "supermercato_jacob": "ex",
        "rifiuto_daniel": "daniel", "rifiuto_nessuno": None,
    }

    ## Josh, Magnus, Simon, Howard, Joanie, Daniel, Corruption, Confidence, Suspicion.
    D23_ATTESI = {
        "archivio_simon":     (1, 2, 2, 0, 0, 0, 0, 3, 0),
        "polizia_joanie":     (1, 2, 0, 1, 1, 0, 0, 3, 0),
        "supermercato_jacob": (1, 2, 0, 0, 0, 0, 0, 3, 0),
        "rifiuto_daniel":     (1, 2, 0, 0, 0, 1, 0, 2, 0),
        "rifiuto_nessuno":    (1, 2, 0, 0, 0, 0, 0, 2, 0),
    }

    def _d23_stato():
        return (valore_interest("josh"), valore_interest("editore"), valore_interest("simon"), valore_interest("howard"),
                valore_interest("amica"), valore_interest("daniel"),
                store.sara_corruption, store.sara_confidence, store.josh_suspicion)

testsuite giorno23:
    testcase bivi:
        parameter ramo = ["archivio_simon", "polizia_joanie", "supermercato_jacob", "rifiuto_daniel", "rifiuto_nessuno"]
        $ debug_azzera_stato()
        $ _d23_scelte = list(D23_SCELTE[ramo])
        $ _test_menu_giorno15(_d23_scelte)
        $ telefono_pilota = _d23_pilota
        $ giorno_entrata = 23
        $ interest_josh = 50
        $ sara_corruption = 20
        $ josh_suspicion = 5
        $ redazione_prossimo_evento = len(REDAZIONE_EVENTI)
        $ _accettata = ramo in ("archivio_simon", "polizia_joanie", "supermercato_jacob")
        $ segna("ep2_d22_inchiesta_accettata", _accettata)
        $ segna("ep2_d22_inchiesta_rifiutata", not _accettata)
        $ segna("ep2_d22_targa", _accettata)
        $ segna("ep2_d22_dawn_fiducia", ramo == "archivio_simon")
        $ segna("ep2_d22_dawn_fatti", ramo == "polizia_joanie")
        $ segna("ep2_d22_consola_josh", ramo != "rifiuto_nessuno")
        $ segna("ep2_d22_josh_dnd")
        $ segna("ep2_d21_jacob_mercoledi", ramo == "supermercato_jacob")
        $ percorso("simon").interest = 0 if ramo in ("rifiuto_daniel", "rifiuto_nessuno") else 20
        $ percorso("howard").interest = 60 if ramo in ("polizia_joanie", "rifiuto_daniel") else 0
        $ percorso("amica").interest = 15 if ramo == "polizia_joanie" else 0
        $ percorso("amico").interest = 0
        $ percorso("daniel").interest = 30 if ramo == "rifiuto_daniel" else 0
        $ (ramo == "rifiuto_daniel") and da_numero("daniel")
        $ _d23_prima = _d23_stato()
        $ segna("test_giorno23_finito", False)
        run Jump("test_giorno23")
        advance until eval fatto("test_giorno23_finito") timeout 120.0
        $ telefono_pilota = None
        $ print("GIORNO23", ramo, ep2_d24_appuntamento, [b - a for a, b in zip(_d23_prima, _d23_stato())])
        assert eval not _d23_scelte
        assert eval tuple(b - a for a, b in zip(_d23_prima, _d23_stato())) == D23_ATTESI[ramo]
        assert eval not in_retroscena
        assert eval giorno == 23 and fatto("ep2_d23_magnus_responso")
        assert eval ep2_d24_appuntamento == D23_APPUNTAMENTO[ramo]
        assert eval bool(fatto("ep2_d23_nadia_luogo_ritrovamento")) == (ramo == "archivio_simon")
        assert eval bool(fatto("ep2_d23_nadia_versione_ufficiale")) == (ramo == "polizia_joanie")
        assert eval bool(fatto("ep2_d23_nadia_supermercato")) == (ramo == "supermercato_jacob")
        assert eval (howard_ultima_faccenda_giorno == 23) == (ramo == "polizia_joanie")
        assert eval not barbara_missioni_completate
