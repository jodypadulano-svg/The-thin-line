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
    _test_esito_telefono = {"fine": False}

    def _test_traccia(nome, abnormal):
        if renpy.is_in_test():
            _test_esito["label"].append(nome)
            if nome == "ep1_fine":
                _test_esito["fine"] = True
            if nome == "telefono_prova_fine":
                _test_esito_telefono["fine"] = True
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
        run Jump("ep1_d8_simon")
        advance until screen "choice" timeout 30.0
        pause 0.5
        screenshot "scelta_bloccata.png"
        click "«Sure.»"
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


## Telefono: giorni 14-22 simulati, con tre strategie per lo slot (10.6-10.9).
init python:
    _test_strategia_tel = ["daniel"]

    def _test_contatto():
        """Lo slot nei test: sempre lo stesso contatto, sparpagliato, o mai."""
        s = _test_strategia_tel[0]
        disponibili = contatti_attivi()
        if s == "nessuno" or not disponibili:
            return None
        if s == "sparpagliata":
            k = disponibili[giorno % len(disponibili)]
        else:
            k = s if s in disponibili else disponibili[0]
        return ("sollecita" if in_attesa(k) else "scrivi", k)

testsuite telefono:
    testcase giorni_14_22:
        description "Rubrica, slot, risposte asincrone, solleciti, entrate e serata del 22."
        parameter strategia = ["daniel", "simon", "sparpagliata", "nessuno"]
        parameter scelte = ["prima", "alternata"]
        $ renpy.random.seed(7)
        $ _test_scelte(scelte)
        $ _test_strategia_tel[0] = strategia
        $ _test_esito_telefono["fine"] = False
        run Jump("telefono_prova")
        advance until eval _test_esito_telefono["fine"] timeout 120.0
        ## Il telefono si è acceso e i numeri ci sono.
        assert eval _foto_telefono["libero"] and "daniel" in _foto_telefono["rubrica"] and "amica" in _foto_telefono["rubrica"]
        ## Chi non scrive mai finisce solo i discorsi aperti dagli altri (Daniel e Magnus scrivono per primi).
        assert eval strategia != "nessuno" or set(_foto_telefono["passi"]) <= {"daniel", "editore"}
        assert eval strategia not in ("daniel", "simon") or _foto_telefono["passi"].get(strategia, 0) >= 2
        ## Chi ha finito la chat introduttiva senza frenare è almeno conoscente (A).
        assert eval strategia != "daniel" or _foto_telefono["interest"]["daniel"] >= 3
        ## Nessun discorso si ripete.
        assert eval len(_foto_telefono["fatti"]) == len(set(_foto_telefono["fatti"]))
        $ print("TELEFONO", strategia, scelte, _foto_telefono)


## Partenza di debug: i giorni prima del 4 si giocano da soli col preset, poi
## si verifica lo stato all'arrivo e si gioca il resto dell'episodio.
## Lancia con:  ... test debug_salta
testsuite debug_salta:
    testcase salto:
        description "Salto ai giorni 4, 5 e 6 con ogni preset: stato coerente, poi fino alla fine."
        parameter preset = ["brava", "barbara", "daniel", "mista"]
        parameter arrivo = [4, 5, 6, 7, 8, 9, 10, 11]
        $ _foto_debug.clear()
        $ _test_esito["fine"] = False
        $ debug_prepara(arrivo, preset)
        run Jump("ep1_inizio")
        advance until eval _foto_debug.get("preset") == preset timeout 120.0
        assert eval _foto_debug["giorno"] == arrivo - 1
        ## Ogni scelta dei giorni 1-3 ha trovato la sua preferenza (se no, il testo è cambiato).
        assert eval preset == "mista" or not _foto_debug["senza_preferenza"]
        assert eval preset != "brava" or not (_foto_debug["fatti"].get("ep1_aperitivo_accettato") or _foto_debug["fatti"].get("sara_fuma"))
        assert eval preset != "brava" or _foto_debug["fatti"].get("ep1_d3_sobrio")
        $ print("DEBUG", preset, _foto_debug)
        assert eval preset != "barbara" or (_foto_debug["fatti"].get("ep1_aperitivo_accettato") and _foto_debug["fatti"].get("ep1_guarda_fumo") and _foto_debug["fatti"].get("ep1_d3_audace"))
        assert eval preset != "daniel" or (_foto_debug["fatti"].get("ep1_d3_proposta_cinema") and _foto_debug["fatti"].get("ep1_d3_audace") and not _foto_debug["fatti"].get("ep1_aperitivo_accettato"))
        $ _test_scelte("alternata")
        advance until eval _test_esito["fine"] timeout 300.0


## Verifica a vista dello scorrimento della chat: con tanti messaggi deve
## restare sull'ultimo anche quando ne arrivano altri.
## Lancia con:  ... test foto_chat --enable-all --overwrite-screenshots
label test_chat_lunga:
    python:
        chat_aperta = "simon"
        chat_log["simon"] = []
        for _i in range(12):
            chat_log["simon"].append(("simon", "Message number %d from Simon, long enough to wrap onto two lines." % (_i + 1)))
            chat_log["simon"].append(("sara", "Reply %d." % (_i + 1)))
    show screen telefono_chat("simon")
    "uno"
    $ msg("simon", "LAST MESSAGE: this one must be visible at the bottom.")
    hide screen telefono_chat
    $ chat_aperta = None
    return

testsuite foto_chat:
    enabled False
    testcase scorrimento:
        run Start("test_chat_lunga")
        advance until screen "telefono_chat" timeout 20.0
        pause 1.5
        screenshot "chat_prima.png"
        click
        pause 1.5
        assert eval tel_scorrimento.range > 0 and tel_scorrimento.value == tel_scorrimento.range
        screenshot "chat_scorrimento.png"
