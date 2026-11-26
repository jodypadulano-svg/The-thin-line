## Test del giorno 21: Darius, Joanie (Jacob, Daniel, Magnus, il messaggio), Josh, Jacob, la notte.
## Il telefono della notte si chiude da solo (telefono_pilota): nessun clic, nessun mouse.

label test_giorno21:
    call ep2_d21
    $ segna("test_giorno21_finito")
    jump test_giorno21_fermo

label test_giorno21_fermo:
    pause
    jump test_giorno21_fermo

init python:
    def _d21_pilota():
        return ("chiudi", None)

    _D21_CAFFE, _D21_SCALE = "Make him a coffee and talk about the book.", "Send him on to the convention."
    _D21_APRE, _D21_CHIUDE = "«He was... good. Seeing him.»", "«It was a drink, Jo. That's all.»"
    _D21_INVIA, _D21_CANCELLA = "Let her send it.", "Take the phone back and delete it."
    _D21_DICE, _D21_TACE = "Tell him about Jacob.", "Keep it to herself."
    _D21_RISPONDE, _D21_GIRA = "Answer him.", "Turn the phone over."
    _D21_TIENE, _D21_ELIMINA = "Leave the chat where it is.", "Delete the chat."
    _D21_POCO, _D21_COLPA = "«Not much.»", "«Yes. And I feel guilty about him.»"
    _D21_PARLA, _D21_FERMA = "Let Joanie talk to him.", "«No, Jo. Not him.»"
    D21_SCELTE = {
        ## Pranzo del 18 avvenuto: c'è anche la scelta su Daniel.
        "tutto_aperto": [_D21_CAFFE, _D21_APRE, "«All right. He's a bit much. I liked it.»", _D21_COLPA, _D21_PARLA, _D21_INVIA,
                         _D21_DICE, _D21_RISPONDE, "Say yes.", _D21_TIENE],
        "pranzo_chiuso": [_D21_SCALE, _D21_CHIUDE, "«It was lunch. He talked about books.»", _D21_COLPA, _D21_FERMA, _D21_CANCELLA,
                          _D21_TACE, _D21_RISPONDE, "Not this week.", _D21_ELIMINA],
        ## Pranzo senza sfottò, Sara dice che non le è piaciuto molto.
        "poco": [_D21_SCALE, _D21_APRE, "«It was lunch. He talked about books.»", _D21_POCO, _D21_INVIA,
                 _D21_DICE, _D21_GIRA, _D21_TIENE],
        ## Nessun pranzo e numero negato il 19: Joanie scrive il numero a memoria.
        "senza_numero": [_D21_SCALE, _D21_APRE, _D21_INVIA, _D21_TACE, _D21_GIRA, _D21_TIENE],
        ## Pranzo annullato: niente scelta su Daniel.
        "annullato": [_D21_CAFFE, _D21_CHIUDE, _D21_CANCELLA, _D21_DICE, _D21_GIRA, _D21_ELIMINA],
    }
    ## Josh, Darius, Joanie, Jacob, Daniel, Corruption, Confidence, Suspicion.
    D21_ATTESI = {
        "tutto_aperto":  (1, 1, 3, 4, 2, 5, 1, 2),
        "pranzo_chiuso": (0, 0, 1, 2, 1, 3, 2, 2),
        "poco":          (1, 0, 1, 2, 0, 2, 1, 0),
        "senza_numero":  (0, 0, 1, 2, 0, 3, 0, 0),
        "annullato":     (1, 1, 1, 0, 0, 1, 2, -1),
    }

    def _d21_stato():
        return (valore_interest("josh"), valore_interest("amico"), valore_interest("amica"), valore_interest("ex"),
                valore_interest("daniel"), store.sara_corruption, store.sara_confidence, store.josh_suspicion)

testsuite giorno21:
    testcase bivi:
        parameter ramo = ["tutto_aperto", "pranzo_chiuso", "poco", "senza_numero", "annullato"]
        $ debug_azzera_stato()
        $ _d21_scelte = list(D21_SCELTE[ramo])
        $ _test_menu_giorno15(_d21_scelte)
        $ telefono_pilota = _d21_pilota
        $ giorno_entrata = 21
        $ interest_josh = 50
        $ sara_corruption = 20
        $ josh_suspicion = 5
        $ segna("ep2_d18_pranzo_daniel", ramo in ("tutto_aperto", "pranzo_chiuso", "poco"))
        $ segna("ep2_d18_sfotto_josh", ramo == "tutto_aperto")
        $ segna("ep2_d18_pranzo_annullato", ramo == "annullato")
        $ segna("ep2_d19_numero_dato", ramo != "senza_numero")
        $ segna("ep2_d19_numero_negato", ramo == "senza_numero")
        $ segna("ep2_d19_ballo_jacob", ramo == "tutto_aperto")
        $ segna("ep2_d19_jacob_risata", ramo == "tutto_aperto")
        $ segna("ep2_d19_difende_josh", ramo == "tutto_aperto")
        $ segna("ep2_d19_detto_tradimento", ramo == "senza_numero")
        $ segna("ep2_d16_minuto_darius", ramo in ("tutto_aperto", "senza_numero"))
        $ segna("ep2_d20_da_joanie", ramo == "pranzo_chiuso")
        $ segna("ep2_d20_magnus_ascolta", ramo == "tutto_aperto")
        $ segna("ep2_d20_serata_romantica", ramo == "annullato")
        $ sara_bad_girl = ramo == "senza_numero"
        $ (ramo != "senza_numero") and da_numero("ex")
        $ _d21_prima = _d21_stato()
        $ segna("test_giorno21_finito", False)
        run Jump("test_giorno21")
        advance until eval fatto("test_giorno21_finito") timeout 120.0
        $ telefono_pilota = None
        assert eval not _d21_scelte
        assert eval not in_retroscena
        $ _d21_dopo = _d21_stato()
        $ print("GIORNO21", ramo, [b - a for a, b in zip(_d21_prima, _d21_dopo)])
        assert eval tuple(b - a for a, b in zip(_d21_prima, _d21_dopo)) == D21_ATTESI[ramo]
        assert eval giorno == 21 and ha_numero("ex")
        assert eval fatto("ep2_d21_detto_josh") == (_D21_DICE in D21_SCELTE[ramo])
        assert eval fatto("ep2_d21_messaggio_inviato") == (_D21_INVIA in D21_SCELTE[ramo])
        assert eval bool(fatto("ep2_d21_joanie_parla_josh")) == (ramo == "tutto_aperto")
        assert eval bool(fatto("ep2_d21_joanie_fermata")) == (ramo == "pranzo_chiuso")
        assert eval bool(fatto("ep2_d21_jacob_mercoledi")) == (ramo == "tutto_aperto")
        assert eval bool(fatto("ep2_d21_jacob_rifiutato")) == (ramo == "pranzo_chiuso")
        ## La chat di Jacob resta solo se Sara non la cancella; nessun discorso libero consumato.
        assert eval (chat_log.get("ex", []) != []) == (_D21_TIENE in D21_SCELTE[ramo])
        assert eval not discorsi_fatti and not giorno_tipo
