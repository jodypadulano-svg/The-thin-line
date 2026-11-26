## Test del giorno 22: abiti, lettera (accettata o rifiutata), Dawn al fiume, Josh umiliato, notte.
## Niente convocazione (sara_stagista False). La faccenda di Howard c'è solo nel ramo «howard» (Interest 60).
## Il telefono della notte si chiude da solo (telefono_pilota): nessun clic, nessun mouse.

label test_giorno22:
    call ep2_d22
    $ segna("test_giorno22_finito")
    jump test_giorno22_fermo

label test_giorno22_fermo:
    pause
    jump test_giorno22_fermo

init python:
    def _d22_pilota():
        return ("chiudi", None)

    _D22_SOLITO, _D22_SCOLLATURA = "Dress as usual tomorrow.", "A little more neckline tomorrow."
    _D22_ACCETTA, _D22_RIFIUTA = "«I'll look into it.»", "«I don't think I'm the right person.»"
    _D22_NADIA, _D22_FATTI = "Ask about Nadia.", "Stick to the facts."
    _D22_CONSOLA, _D22_IRRITA = "Comfort him.", "Get annoyed at how weak he is."
    D22_SCELTE = {
        "empatica": [_D22_SCOLLATURA, _D22_ACCETTA, _D22_NADIA, _D22_CONSOLA],
        "fatti":    [_D22_SOLITO, _D22_ACCETTA, _D22_FATTI, _D22_IRRITA],
        "rifiuto":  [_D22_SOLITO, _D22_RIFIUTA, _D22_CONSOLA],
        ## Interest Howard sopra 50: al rientro c'è la faccenda (nessun menu, nessun punteggio).
        "howard":   [_D22_SOLITO, _D22_RIFIUTA, _D22_CONSOLA],
    }
    ## Josh, Barbara, Daniel, Corruption, Confidence, Suspicion.
    D22_ATTESI = {
        "empatica": (3, 1, 0, 1, 0, 0),
        "fatti":    (-3, 0, 1, 1, 0, 0),
        "rifiuto":  (3, 0, 0, 0, 0, 0),
        "howard":   (3, 0, 0, 0, 0, 0),
    }

    def _d22_stato():
        return (valore_interest("josh"), valore_interest("capa"), valore_interest("daniel"),
                store.sara_corruption, store.sara_confidence, store.josh_suspicion)

testsuite giorno22:
    testcase bivi:
        parameter ramo = ["empatica", "fatti", "rifiuto", "howard"]
        $ debug_azzera_stato()
        $ _d22_scelte = list(D22_SCELTE[ramo])
        $ _test_menu_giorno15(_d22_scelte)
        $ telefono_pilota = _d22_pilota
        $ giorno_entrata = 22
        $ interest_josh = 50
        $ sara_corruption = 20
        $ josh_suspicion = 5
        $ segna("ep2_d21_detto_josh", ramo == "empatica")
        $ segna("ep2_d21_taciuto_josh", ramo == "fatti")
        $ segna("ep2_d21_risposto_jacob", ramo == "fatti")
        $ segna("ep2_d21_joanie_parla_josh", ramo == "empatica")
        $ segna("ep2_d21_colpa_si", ramo == "fatti")
        $ segna("ep2_d18_sfotto_josh", ramo == "rifiuto")
        $ percorso("howard").interest = 60 if ramo == "howard" else 0
        $ _d22_prima = _d22_stato()
        $ segna("test_giorno22_finito", False)
        run Jump("test_giorno22")
        advance until eval fatto("test_giorno22_finito") timeout 120.0
        $ telefono_pilota = None
        assert eval not _d22_scelte
        assert eval not in_retroscena
        $ _d22_dopo = _d22_stato()
        $ print("GIORNO22", ramo, [b - a for a, b in zip(_d22_prima, _d22_dopo)])
        assert eval tuple(b - a for a, b in zip(_d22_prima, _d22_dopo)) == D22_ATTESI[ramo]
        assert eval giorno == 22 and fatto("ep2_d22_josh_dnd")
        assert eval bool(fatto("ep2_d22_inchiesta_accettata")) == (ramo in ("empatica", "fatti"))
        assert eval bool(fatto("ep2_d22_inchiesta_rifiutata")) == (ramo in ("rifiuto", "howard"))
        assert eval bool(fatto("ep2_d22_targa")) == (ramo in ("empatica", "fatti"))
        assert eval bool(fatto("ep2_d22_dawn_fiducia")) == (ramo == "empatica")
        assert eval bool(fatto("ep2_d22_dawn_fatti")) == (ramo == "fatti")
        assert eval bool(fatto("ep2_d22_scollatura_domani")) == (ramo == "empatica")
        assert eval not barbara_missioni_completate
        assert eval (howard_ultima_faccenda_giorno == 22) == (ramo == "howard")
        assert eval not discorsi_fatti and not giorno_tipo
