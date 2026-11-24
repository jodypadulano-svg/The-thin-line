## Test del giorno 18: pranzo con Daniel (professionale, privato al primo ballo,
## ballo ripetuto) o assente, mezz'ora con Barbara, step della scala di Howard.

label test_giorno18:
    call ep2_d18
    $ segna("test_giorno18_finito")
    pause
    return

testsuite giorno18:
    testcase bivi:
        parameter ramo = ["professionale", "privato_primo", "privato_ripetuto", "senza_pranzo", "ragazzina_premio"]
        $ debug_azzera_stato()
        $ _d18_scelte = {
            "professionale": ["My usual work clothes.", "Laugh.", "«Of course.»", "Go in.", "Another cup."],
            "privato_primo": ["Joanie's black top, under the blazer.", "«Go on, then. What else did he do?»", "Take his hand.", "Skip the scene.", "«I'm sorry, I can't tonight.»", "Go in.", "Laugh and give it back."],
            "privato_ripetuto": ["My usual work clothes.", "Laugh.", "Take his hand.", "Watch the scene.", "«Come on. Don't say that.»", "«Of course.»", "Go in.", "Let him guide the spoon."],
            "ragazzina_premio": ["Joanie's black top, under the blazer.", "Laugh.", "Give him exactly what he wants.", "«Of course.»", "Go in.", "Another cup."],
            "senza_pranzo": ["«Of course.»", "«Not tonight, Howard.»"],
            }[ramo]
        $ _test_menu_giorno15(_d18_scelte)
        $ segna("ep2_d18_pranzo_daniel_confermato", ramo != "senza_pranzo")
        $ segna("ep2_d17_top_ricevuto", ramo in ("privato_primo", "ragazzina_premio"))
        $ segna("ep1_d13_videoclip", ramo == "privato_ripetuto")
        $ segna("ep1_d13_cerniera", ramo == "privato_ripetuto")
        $ segna("ep1_d13_pranzo_no", ramo == "privato_ripetuto")
        $ sara_corruption = 30 if ramo == "privato_primo" else 10
        $ howard_visite = {"professionale": 1, "privato_primo": 2, "privato_ripetuto": 3, "senza_pranzo": 1, "ragazzina_premio": 1}[ramo]
        ## Sara «ragazzina» solo con Interest Daniel ≥ 12 all'arrivo.
        $ interest("daniel", 12 if ramo in ("privato_ripetuto", "ragazzina_premio") else 0)
        $ _d18_corr = sara_corruption
        $ _d18_conf = sara_confidence
        $ _d18_daniel = valore_interest("daniel")
        $ _d18_capa = valore_interest("capa")
        $ _d18_howard = valore_interest("howard")
        $ segna("test_giorno18_finito", False)
        run Jump("test_giorno18")
        advance until eval fatto("test_giorno18_finito") timeout 120.0
        assert eval not _d18_scelte
        assert eval fatto("ep2_d18_pranzo_daniel") == (ramo != "senza_pranzo")
        assert eval fatto("ep2_d18_privato") == (ramo in ("privato_primo", "privato_ripetuto"))
        assert eval fatto("ep2_d18_ragazzina") == (ramo in ("privato_ripetuto", "ragazzina_premio"))
        assert eval fatto("ep2_d18_sfotto_josh") == (ramo == "ragazzina_premio")
        assert eval fatto("ep2_d18_ballo_ripetuto") == (ramo == "privato_ripetuto")
        assert eval fatto("ep2_d18_angolo_bocca") == (ramo == "privato_ripetuto")
        assert eval fatto("ep2_d18_bacio_orecchio") == (ramo == "privato_primo")
        assert eval fatto("ep2_d18_josh_avvisato") == (ramo == "privato_ripetuto")
        assert eval sara_corruption == _d18_corr + {"professionale": 0, "privato_primo": 6, "privato_ripetuto": 3, "senza_pranzo": 0, "ragazzina_premio": 4}[ramo]
        assert eval sara_confidence == _d18_conf + (1 if ramo == "privato_primo" else 0)
        assert eval valore_interest("daniel") == _d18_daniel + {"professionale": 1, "privato_primo": 5, "privato_ripetuto": 4, "senza_pranzo": 0, "ragazzina_premio": 4}[ramo]
        assert eval valore_interest("capa") == _d18_capa + (0 if ramo == "privato_primo" else 1)
        assert eval ha_numero("capa") == (ramo != "privato_primo")
        assert eval valore_interest("howard") == _d18_howard + {"professionale": 4, "privato_primo": 2, "privato_ripetuto": 4, "senza_pranzo": 0, "ragazzina_premio": 4}[ramo]
        assert eval howard_visite == {"professionale": 2, "privato_primo": 3, "privato_ripetuto": 4, "senza_pranzo": 1, "ragazzina_premio": 2}[ramo]
