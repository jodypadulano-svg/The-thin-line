## La chat aperta deve mostrare l'ultimo messaggio anche quando la storia è lunga
## (Jody 27/11: il messaggio di Joanie a Jacob del 21 non si vedeva con una chat già piena).

label test_chat_scorrimento:
    $ chat_aperta = "ex"
    show screen telefono_chat("ex")
    pause 0.2
    $ msg("sara", "do you still dance like that or was it a one off", premia_avvio=False)
    $ segna("test_chat_scorrimento_finito")
    pause

testsuite chat_scorrimento:
    testcase chat_lunga:
        parameter quanti = [5, 29, 30, 45]
        $ debug_azzera_stato()
        $ da_numero("ex")
        $ chat_log["ex"] = [("ex" if i % 2 else "sara", "message number %d, a line of ordinary length" % i, None, 600 + i, 19) for i in range(quanti)]
        $ segna("test_chat_scorrimento_finito", False)
        run Jump("test_chat_scorrimento")
        advance until eval fatto("test_chat_scorrimento_finito") timeout 20.0
        pause 0.5
        $ print("SCORRIMENTO", quanti, tel_scorrimento.value, tel_scorrimento.range)
        assert eval fatto("test_chat_scorrimento_finito")
        assert eval tel_scorrimento.range == 0 or tel_scorrimento.value >= tel_scorrimento.range - 1
