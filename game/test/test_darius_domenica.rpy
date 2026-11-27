## Riproduzione (Jody 27/11): da un salvataggio della notte del 19 si passa al 20 e al 21.
## Darius deve suonare al citofono la domenica mattina, prima di Joanie.

label test_darius_domenica:
    call ep2_d20
    call ep2_d21
    $ segna("test_darius_finito")
    jump test_darius_fermo

label test_darius_fermo:
    pause
    jump test_darius_fermo

init python:
    def _darius_pilota():
        return ("chiudi", None)

testsuite darius_domenica:
    testcase dal_19:
        parameter strategia = ["prima", "ultima"]
        $ debug_azzera_stato()
        $ _test_scelte(strategia)
        $ telefono_pilota = _darius_pilota
        $ interest_josh = 50
        $ sara_corruption = 20
        $ da_numero("ex")
        $ segna("ep2_d19_numero_dato")
        $ del _test_esito["label"][:]
        $ segna("test_darius_finito", False)
        run Jump("test_darius_domenica")
        advance until eval fatto("test_darius_finito") timeout 240.0
        $ telefono_pilota = None
        $ _etichette = _test_esito["label"]
        $ print("DARIUS", strategia, [l for l in _etichette if l.startswith("ep2_d21")])
        assert eval "ep2_d21_darius" in _etichette
        assert eval _etichette.index("ep2_d21_darius") < _etichette.index("ep2_d21_joanie")
