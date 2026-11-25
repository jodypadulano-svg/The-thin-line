## Test del giorno 19: redazione, missione 2 di Barbara, Samantha, Joanie
## (ripetizione, confidenza, Simon), Jacob a The Lantern.

label test_giorno19:
    call ep2_d19
    $ segna("test_giorno19_finito")
    pause
    return

init python:
    ## I sei box a ripetizione, sempre con una sola scelta.
    D19_BOX = ["«[nome_compagno] read my book without asking.»", "«Jacob never needed to ask.»",
               "«I was loud with him.»", "«I miss being loud.»",
               "«Nobody's made me feel like that since.»", "«I still want him.»"]

    ## Fino alla regola di Joanie, per i rami della serata degli occhiolini.
    D19_INIZIO_BAD = ["Give it back.", "Don't ask.", "The one Samantha chose.",
                      "Let yourself be carried off.", "Let Joanie guide you."] + D19_BOX + ["«Whatever it is, I won't judge you.»", "Let her have tonight."]

    ## Prima parte (redazione), Barbara e Samantha a parte.
    D19_SCELTE = {
        ## Razionale e fredda, caffè con Samantha, nessun numero a Jacob.
        "razionale": ["Give it back.", "Don't ask.", "Thank her and let it go.",
                      "«You're leaving out how it ended.»", "Keep your own head.",
                      "Stay cold.", "«No, thanks.»", "«You cheated on me.»", "Answer straight away.", "Push the phone back."],
        ## Guida senza il ricordo: niente ripetizione.
        "guida": ["Read the last note.", "«Who's in there?»", "«How do you know he listens?»",
                  "«You're leaving out how it ended.»", "Let Joanie guide you.",
                  "Laugh at an old memory.", "«No, thanks.»", "Let it lie.", "Think about it a second too long.", "Not tonight.", "Push the phone back."],
        ## Ricordo ma poi razionale.
        "ricordo_razionale": ["Give it back.", "Don't ask.", "The one I'd have picked.",
                              "Let yourself be carried off.", "Keep your own head.",
                              "Laugh at an old memory.", "«All right. One.»", "Let it lie.", "Think about it a second too long.", "One song.", "Give him the number."],
        ## Ripetizione con Joanie a 5: 5 + 3 = 8, non basta per la confidenza.
        "ripeti_soglia": ["Give it back.", "Don't ask.", "The one Samantha chose.",
                          "Let yourself be carried off.", "Let Joanie guide you."] + D19_BOX +
                         ["Laugh at an old memory.", "«All right. One.»", "Let it lie.", "Think about it a second too long.", "One song.", "Give him the number."],
        ## Ripetizione con Joanie a 6: 9, confidenza non ascoltata.
        "non_detto": ["Give it back.", "Don't ask.", "The one Samantha chose.",
                      "Let yourself be carried off.", "Let Joanie guide you."] + D19_BOX +
                     ["«Some things are better left unsaid.»",
                      "Stay cold.", "«All right. One.»", "«You cheated on me.»", "Answer straight away.", "Give him the number."],
        ## Tutto: confessione, Simon, bad girl al Lantern.
        "bad_girl": ["Read the last note.", "«Who's in there?»", "The one Samantha chose.",
                     "Let yourself be carried off.", "Let Joanie guide you."] + D19_BOX +
                    ["«Whatever it is, I won't judge you.»", "«I saw you with Simon.»",
                     "(The wink.)", "Not this one.", "«All right. One.»", "Not this one.", "Give him the number."],
        ## Confessione, ma tace su Simon e ride con Jacob.
        "tace_simon": ["Give it back.", "Don't ask.", "The one Samantha chose.",
                       "Let yourself be carried off.", "Let Joanie guide you."] + D19_BOX +
                      ["«Whatever it is, I won't judge you.»", "Let her have tonight.",
                       "Laugh at an old memory.", "Not this one.", "«All right. One.»", "Not this one.", "Give him the number."],
        ## Tutti gli occhiolini, il finale forzato, poi di nuovo alla porta e a casa.
        "finale": D19_INIZIO_BAD + ["(The wink.)"] * 11 + ["Give him the number.", "(The wink.) Go with him."] +
                  ["(The wink.)"] * 4 + ["Go back to the choice.", "Not this one. Home."],
        ## Finale saltando tutto quello che si può dopo la porta.
        "finale_salti": D19_INIZIO_BAD + ["(The wink.)"] * 11 + ["Push the phone back.", "(The wink.) Go with him."] +
                  ["Not this one."] * 3 + ["Go back to the choice.", "Not this one. Home."],
        ## Due per momento, con salti isolati: la porta si apre lo stesso.
        "porta_minima": D19_INIZIO_BAD + ["Stay cold.", "(The wink.)", "Not this one.", "(The wink.)", "Not this one.",
                  "(The wink.)", "Not this one.", "(The wink.)", "Not this one.", "(The wink.)", "(The wink.)",
                  "Give him the number.", "Not this one. Home."],
        ## In pista ne segue uno solo: la porta resta chiusa.
        "porta_chiusa": D19_INIZIO_BAD + ["(The wink.)"] * 5 + ["Not this one.", "(The wink.)", "Not this one."] +
                  ["(The wink.)"] * 3 + ["Give him the number."],
        ## Due salti di fila in pista: Joanie smette.
        "due_salti": D19_INIZIO_BAD + ["(The wink.)"] * 5 + ["Not this one.", "Not this one.", "Give him the number."],
        ## Barbara: missione 2 fatta e missione 2 rifiutata.
        "barbara_si": ["Give it back.", "Don't ask.", "Go and stand behind her.", "Thank her and let it go.",
                       "«You're leaving out how it ended.»", "Keep your own head.",
                       "Stay cold.", "«No, thanks.»", "«You cheated on me.»", "Answer straight away.", "Push the phone back."],
        "barbara_no": ["Give it back.", "Don't ask.", "«I'd rather not, today.»", "Thank her and let it go.",
                       "«You're leaving out how it ended.»", "Keep your own head.",
                       "Stay cold.", "«No, thanks.»", "«You cheated on me.»", "Answer straight away.", "Push the phone back."],
        ## Stagista ma sotto soglia: nessuna convocazione neanche al 100%.
        "barbara_soglia": ["Give it back.", "Don't ask.", "Thank her and let it go.",
                           "«You're leaving out how it ended.»", "Keep your own head.",
                           "Stay cold.", "«No, thanks.»", "«You cheated on me.»", "Answer straight away.", "Push the phone back."],
    }

    ## Effetti attesi: Jacob, Corruption, Confidence, Joanie, Magnus, Barbara.
    D19_ATTESI = {
        "razionale":         (0, 0, 3, 0, 0, 0),
        "guida":             (3, 1, 2, 1, 0, 1),
        "ricordo_razionale": (8, 4, 3, 0, 0, 0),
        "ripeti_soglia":     (10, 6, 1, 3, 1, 0),
        "non_detto":         (6, 4, 2, 3, 1, 0),
        "bad_girl":          (7, 6, 2, 8, 1, 1),
        "finale":            (8, 7, 1, 12, 1, 0),
        "finale_salti":      (6, 7, 1, 12, 1, 0),
        "porta_minima":      (8, 7, 1, 12, 1, 0),
        "porta_chiusa":      (8, 7, 1, 12, 1, 0),
        "due_salti":         (6, 5, 1, 8, 1, 0),
        "tace_simon":        (9, 6, 1, 6, 1, 0),
        "barbara_si":        (0, 0, 3, 0, 0, 0),
        "barbara_no":        (0, 0, 3, 0, 0, 0),
        "barbara_soglia":    (0, 0, 3, 0, 0, 0),
    }

testsuite giorno19:
    testcase bivi:
        parameter ramo = ["razionale", "guida", "ricordo_razionale", "ripeti_soglia", "non_detto", "bad_girl", "tace_simon", "finale", "finale_salti", "porta_minima", "porta_chiusa", "due_salti", "barbara_si", "barbara_no", "barbara_soglia"]
        $ debug_azzera_stato()
        $ _d19_scelte = list(D19_SCELTE[ramo])
        $ _test_menu_giorno15(_d19_scelte)
        $ _d19_caffe = ramo in ("razionale", "guida", "barbara_si", "barbara_no", "barbara_soglia")
        $ segna("ep2_d14_shopping_samantha", not _d19_caffe)
        $ segna("ep2_d15_litigio_josh", ramo in ("guida", "bad_girl"))
        $ segna("ep2_d18_pranzo_daniel", ramo in ("bad_girl", "ripeti_soglia"))
        $ segna("ep2_d18_ballo", ramo == "bad_girl")
        $ segna("ep2_d17_ha_guardato_joanie_simon", ramo == "bad_girl")
        $ segna("sara_fuma", ramo == "guida")
        $ sara_stagista = ramo.startswith("barbara")
        $ BARBARA_CONVOCAZIONI["probabilita"] = 1.0
        $ interest("capa", 19 if ramo == "barbara_soglia" else 20)
        $ sara_corruption = 10
        $ interest("amica", 5 if ramo == "ripeti_soglia" else 6)
        $ _d19_prima = (valore_interest("ex"), sara_corruption, sara_confidence, valore_interest("amica"), valore_interest("editore"), valore_interest("capa"))
        ## I finali visti sono del giocatore: il test li rimette com'erano.
        $ _d19_finali = list(persistent.finali_visti)
        $ persistent.finali_visti = []
        $ segna("test_giorno19_finito", False)
        run Jump("test_giorno19")
        advance until screen "telefono" timeout 120.0
        click "Go to bed"
        advance until eval fatto("test_giorno19_finito") timeout 120.0
        $ BARBARA_CONVOCAZIONI["probabilita"] = 0.20
        assert eval not _d19_scelte
        assert eval not in_retroscena
        $ _d19_dopo = (valore_interest("ex"), sara_corruption, sara_confidence, valore_interest("amica"), valore_interest("editore"), valore_interest("capa"))
        $ print("GIORNO19", ramo, [b - a for a, b in zip(_d19_prima, _d19_dopo)])
        assert eval tuple(b - a for a, b in zip(_d19_prima, _d19_dopo)) == D19_ATTESI[ramo]
        assert eval fatto("jacob_tornato") and percorso("ex").incontrato
        assert eval sara_bad_girl == (ramo in ("bad_girl", "tace_simon", "finale", "finale_salti", "porta_minima", "porta_chiusa", "due_salti"))
        assert eval fatto("ep2_d19_sa_di_simon") == (ramo == "bad_girl")
        assert eval ha_numero("ex") == (ramo in ("ricordo_razionale", "ripeti_soglia", "non_detto", "bad_girl", "tace_simon", "finale", "porta_minima", "porta_chiusa", "due_salti"))
        ## La porta: due seguiti per momento, mai dopo due salti di fila.
        assert eval fatto("ep2_d19_porta_chiusa") == (ramo in ("finale", "finale_salti", "porta_minima"))
        assert eval ramo not in ("finale", "finale_salti") or "The Wink" in persistent.finali_visti
        assert eval ramo != "porta_chiusa" or len(d19_seguiti("pista")) == 1
        assert eval ramo not in ("bad_girl", "tace_simon", "due_salti") or d19_salti == 2
        assert eval barbara_missioni_completate == ([2] if ramo == "barbara_si" else [])
        assert eval ramo != "barbara_no" or barbara_missioni_disponibili() == [2]
        assert eval ramo != "barbara_si" or barbara_missioni_disponibili() == []
        ## Nessuna scena nel fine settimana, nessun secondo sorteggio nello stesso giorno.
        assert eval barbara_sorteggia() is None
        $ persistent.finali_visti = _d19_finali
