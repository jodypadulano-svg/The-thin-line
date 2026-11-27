## L'effetto delle scelte ambra entra ed esce senza errori e lascia lo stato pulito.

label test_effetti_ambra:
    scene bg casa
    $ musica("casa")
    menu:
        "A normal choice.":
            pass
        "An amber choice." (acceleratore=True):
            pass
    $ segna("test_ambra_finito")
    pause

testsuite effetti_ambra:
    testcase entra_esce:
        $ segna("test_ambra_finito", False)
        run Jump("test_effetti_ambra")
        pause 1.0
        assert eval _ambra_attiva
        click "An amber choice."
        advance until eval fatto("test_ambra_finito") timeout 10.0
        assert eval not _ambra_attiva and not _ambra_scelta
        assert eval not renpy.music.is_playing(channel="battito")
