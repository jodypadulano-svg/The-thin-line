label test_giorno16:
    call ep2_d16
    $ segna("test_giorno16_finito")
    pause
    return

testsuite giorno16:
    testcase bivi:
        parameter ramo = ["obbedisce", "rifiuta", "saluta", "senza_lite"]
        $ _d16_lite = ramo != "senza_lite"
        $ _d16_cena = {"obbedisce": "Confide in Joanie in the kitchen.", "rifiuta": "Laugh with Darius.", "saluta": "Laugh with Darius.", "senza_lite": "Stay close to [nome_compagno]."}[ramo]
        $ _d16_scelte = ["Ask what happened to her." if _d16_lite else "Let it go.", "Answer and say goodbye." if ramo == "saluta" else "Stay and talk a minute."]
        $ _d16_scelte.extend({"obbedisce": ["Put the bag down and sit."], "rifiuta": ["Stay on your feet."]}.get(ramo, []))
        $ _d16_scelte.append(_d16_cena)
        $ _test_menu_giorno15(_d16_scelte)
        $ _d16_hugo = interest_hugo
        $ _d16_josh = valore_interest("josh")
        $ _d16_darius = valore_interest("amico")
        $ _d16_joanie = valore_interest("amica")
        $ segna("ep2_d15_litigio_josh", _d16_lite)
        $ segna("ep2_d18_pranzo_daniel_confermato", _d16_lite)
        $ segna("ep1_d13_pranzo_no", True)
        $ segna("test_giorno16_finito", False)
        run Jump("test_giorno16")
        advance until screen "telefono" timeout 120.0
        assert eval telefono_minuti_ora == 16 * 1440 + 22 * 60 and telefono_minuti_rimasti() == 60
        assert eval not in_retroscena and renpy.showing("cg_corrente")
        click "Go to bed"
        advance until eval fatto("test_giorno16_finito") timeout 120.0
        assert eval not telefono_minuti_attivo()
        assert eval not _d16_scelte
        assert eval interest_hugo == _d16_hugo + {"obbedisce": 3, "rifiuta": 1, "saluta": 0, "senza_lite": 0}[ramo]
        assert eval valore_interest("josh") == _d16_josh + (ramo == "senza_lite")
        assert eval valore_interest("amico") == _d16_darius + (ramo in ("rifiuta", "saluta"))
        assert eval valore_interest("amica") == _d16_joanie + (ramo == "obbedisce")
        assert eval fatto("ep2_d18_pranzo_daniel_confermato") == _d16_lite
        assert eval not in_retroscena
