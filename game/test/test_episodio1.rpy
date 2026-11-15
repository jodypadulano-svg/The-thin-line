## =============================================================================
## TEST AUTOMATICI — Episodio 1
## =============================================================================
## Gioca l'episodio dall'inizio alla fine con tre strategie di scelta
## (sempre la prima opzione, sempre l'ultima, alternate) e apre il Diario.
## Da riga di comando, nella cartella dell'SDK:
##   lib\py3-windows-x86_64\python.exe renpy.py <cartella del gioco> test episodio1

init python:
    def _test_scelte(strategia):
        """Sostituisce il menu con uno che sceglie da solo."""
        contatore = [0]
        def scegli(items, **kwargs):
            opzioni = [v for (t, v) in items if v is not None]
            contatore[0] += 1
            if strategia == "prima":
                i = 0
            elif strategia == "ultima":
                i = len(opzioni) - 1
            else:
                i = contatore[0] % len(opzioni)
            scelta = opzioni[i]
            return getattr(scelta, "value", scelta)
        store.menu = scegli

    _test_esito = {"fine": False, "label": []}

    def _test_traccia(nome, abnormal):
        if renpy.is_in_test():
            _test_esito["label"].append(nome)
            if nome == "ep1_fine":
                _test_esito["fine"] = True
    config.label_callbacks.append(_test_traccia)

testsuite episodio1:
    testcase gioca_tutto:
        description "Gioca tutto l'episodio con tre strategie di scelta e apre il Diario."
        parameter strategia = ["prima", "ultima", "alternata"]
        $ _test_scelte(strategia)
        $ _test_esito["fine"] = False
        run Jump("ep1_inizio")
        advance until eval _test_esito["fine"] timeout 300.0
        run ShowMenu("diario")
        click "Simon"
        click "Daniel"
        click "Howard"
        click "L'editore"
        click "Sara"

## Foto del Diario per controllo a vista (non parte con la suite globale).
## Lancia con:  ... test foto --enable-all --overwrite-screenshots
testsuite foto:
    enabled False
    testcase diario:
        $ _test_scelte("alternata")
        $ _test_esito["fine"] = False
        run Jump("ep1_inizio")
        advance until eval _test_esito["fine"] timeout 300.0
        run ShowMenu("diario")
        pause 0.5
        screenshot "diario_sara.png"
        click "Howard"
        pause 0.5
        screenshot "diario_howard.png"
