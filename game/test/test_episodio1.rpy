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
            ## Come il giocatore: le frasi bloccate (A3) non si possono scegliere.
            opzioni = [v for v in opzioni if not getattr(v, "kwargs", None) or requisiti_ok(v.kwargs)]
            ## I segreti dei dev non si trovano per caso.
            opzioni = [v for v in opzioni if not (getattr(v, "kwargs", None) or {}).get("segreto")]
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
        click "Magnus"
        click "Barbara"
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

testsuite foto_scelte:
    enabled False
    testcase bloccata:
        $ store.menu = renpy.display_menu
        run Jump("simon_s5_allenamento")
        advance until screen "choice" timeout 30.0
        pause 0.5
        screenshot "scelta_bloccata.png"
        click "«Certo.»"
        pause 0.2
        screenshot "notifica.png"

testsuite foto_cg:
    enabled False
    testcase armadio:
        $ store.menu = renpy.display_menu
        run Jump("ep1_d1_mattina")
        advance repeat 2
        pause 1.0
        screenshot "cg_armadio.png"


## La scelta segreta del giorno 2 (Sara fuma): clic sull'area invisibile
## della sigaretta, poi «sì». Lancia con:  ... test segreto
testsuite segreto:
    testcase rifiuta:
        description "Clic sulla sigaretta nascosta, rifiuta: tutto come prima."
        run Jump("ep1_d2_terrazzino")
        advance until screen "choice" timeout 30.0
        click pos (200, 950)
        advance until screen "choice" timeout 30.0
        click "Pull your hand back."
        advance until screen "choice" timeout 30.0
        assert eval not fatto("sara_fuma") and sara_corruption < 100

    testcase sara_fuma:
        description "Clic sulla sigaretta nascosta, accetta: sara_fuma attiva e Corruption a 100."
        run Jump("ep1_d2_terrazzino")
        advance until screen "choice" timeout 30.0
        click pos (200, 950)
        advance until screen "choice" timeout 30.0
        click "Put it to your lips."
        advance until eval fatto("sara_fuma") and sara_corruption == 100 and len(segreti_trovati) == 1 timeout 30.0


## Verifica a vista dello zoom: ... test foto_zoom --enable-all --overwrite-screenshots
label test_zoom_sguardo:
    $ cg("prova", "images/cg/ep1/d3_08_sguardo_daniel.webp")
    "uno"
    $ zoom_cg("prova", "images/cg/ep1/d3_08_sguardo_daniel.webp", (965, 280, 560, 315))
    "due"
    return

testsuite foto_zoom:
    enabled False
    testcase velocita:
        run Jump("test_zoom_sguardo")
        pause 3.0
        click
        pause 0.8
        screenshot "zoom_inizio.png"
        pause 2.0
        screenshot "zoom_meta.png"
        pause 3.0
        screenshot "zoom_fine.png"

testsuite foto_ui:
    enabled False
    testcase ui:
        run Jump("ep1_d3_cena")
        pause 2.0
        screenshot "ui_testo.png"
        run ShowMenu("preferences")
        pause 1.5
        screenshot "ui_opzioni.png"
        run ShowMenu("diario")
        pause 1.5
        screenshot "ui_diario.png"

testsuite foto_testo:
    enabled False
    testcase nome:
        run Jump("ep1_d1_mattina")
        pause 2.0
        click
        pause 0.5
        click
        pause 0.5
        click
        pause 0.5
        screenshot "ui_nome.png"
