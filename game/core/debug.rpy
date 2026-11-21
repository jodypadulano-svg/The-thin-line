## =============================================================================
## DEBUG — partire da un giorno qualsiasi (solo per gli sviluppatori)
## =============================================================================
## Dal menu iniziale, solo con config.developer attivo: si sceglie il giorno e
## una configurazione. I giorni precedenti NON si impostano a mano: si giocano
## da soli, saltando i dialoghi, con le scelte della configurazione. Così lo stato
## di partenza è sempre uno che il gioco può davvero produrre, e quando si scrive
## un giorno nuovo (label "ep1_dN") diventa subito raggiungibile.
##
## Ogni configurazione è una lista di inizi di frase delle scelte, in ordine di
## preferenza; se nessuna corrisponde si usa la «riserva» (prima/ultima/alternata).
## Se il testo di una scelta cambia, aggiornare qui (il test debug_salta avvisa).

init python:
    PRESET_DEBUG = {
        "brava": {
            "nome": "Brava ragazza: tutto abbottonato, rifiuta gli inviti",
            "riserva": "prima",
            "scelte": [
                ## Giorno 1
                "Button it all the way up.", "Apologize right away.",
                "Blush and close her blouse", "Decline politely.",
                "Close the laptop and spend the evening with him.",
                "Cook something nice for him.", "Say yes, excited.",
                ## Giorno 2
                "Eat with the girls from the office.", "«No thanks, I don't smoke.»",
                "Look away and think about something else.", "Pull your hand back.",
                "Keep the baggy t-shirt.", "«I'm here to work out, not to look.»",
                "Give him a quick nod.", "Look away: it's none of her business.",
                "Be excited for him.",
                ## Giorno 3
                "Take the piece she's given.", "The navy dress.",
                "Order something else, just for herself.", "Laugh it off",
                "Squeeze [nome_compagno]'s hand under the table.",
                "Smile and go back to the table.", "Smile politely.", "Comfort him",
                ## Giorno 4
                "«You look amazing.»", "«You have nothing to be sorry for.»",
                "«I was harsh in the car. Sorry.»",
                "«Make it the most beautiful spreadsheet ever.»",
                "Decline with a smile.", "One drink is enough.",
                "An evening with [nome_compagno].",
                ## Giorno 5
                "Stop for a minute.", "Ignore him.",
                "A film on the sofa with [nome_compagno].",
                ## Giorno 6
                "Thank him.", "The grey dress.", "Dance with [nome_compagno].",
                ## Giorno 7
                "A walk by the river with [nome_compagno].", "Take the initiative.",
                ## Giorno 8
                "Focus on the piece.", "Go home.",
                ## Giorno 9
                "Something sweet.", "Pretend not to notice.", "Kind words, from her chair.",
                "«I'm sorry, Howard, I really don't have much time.»",
                ## Giorno 10
                "Accept without a word.", "Do it up again", "Let it go.", "Tell him everything about Howard.",
                ## Scelte Corr +1 aggiunte il 21/11 (giorni 5, 7, 9)
                "«There won't be a next time.»", "She asks him who he is.", "Send back an eye-roll.",
                ## Giorno 11
                "Eat with Roberta.", "A handshake.", "«I'll just knock, Howard.", "«Another time, Howard.",
            ],
        },
        "barbara": {
            "nome": "Verso Barbara: aperitivo accettato, guarda le colleghe fumare, vestito audace",
            "riserva": "ultima",
            "scelte": [
                ## Giorno 1
                "Leave one button open.", "A joke:", "«Thanks... I think.»",
                "Accept.", "Write for one more hour", "Order a pizza.",
                "Say yes, with a sigh.",
                ## Giorno 2
                "Eat with the girls from the office.",
                "«No thanks... since when do you smoke, Jess?»",
                "Keep watching them.", "Put it to your lips.",
                "Try on Joanie's top.", "«Okay, he's a good-looking guy.»",
                "Give him a quick nod.", "Keep watching.",
                "Say she's a bit worried about Daniel.",
                ## Giorno 3
                "Propose her own idea.", "The most daring dress she owns.",
                "Order something else, just for herself.",
                "Tell him about it, with passion.", "Change the subject, gracefully.",
                "Smile and go back to the table.", "Answer coldly.",
                "Ask him why he didn't react.",
                ## Giorno 4
                "«You look amazing.»", "«Tell me about your dad, one day.»",
                "«Next time, answer him back.»",
                "«After all, that's how you conquered me.»",
                "Accept the drink.", "Let herself go.", "Write.",
                ## Giorno 5
                "Cut it short: she's late.", "Ignore him.", "Go out with Joanie.",
                ## Giorno 6
                "Thank him.", "The short dress Joanie picked.",
                "Laugh a little too much at Simon's jokes.",
                ## Giorno 7
                "Write.", "She's tired: sleep.",
                ## Giorno 8
                "Chat with Joanie under the desk.", "Go in anyway.", "«Fix the other one too?",
                "«Sure.»", "Save it.", "Don't mention it.",
                ## Giorno 9
                "Let him know she's annoyed.", "Pretend not to notice.", "Hug him.", "Pull away from the hug.",
                "«When it happens, gladly.»",
                ## Giorno 10
                "Accept without a word.", "Leave it open.", "Ask her what happened.", "Play it down.",
                ## Scelte Corr +1 aggiunte il 21/11 (giorni 5, 7, 9)
                "«...He's not ugly.", "She lets him come closer", "Zoom in.",
                ## Giorno 11
                "Eat with Roberta.", "A hug.", "Save it.", "Go in for a coffee.", "Stay for a second coffee.", "Undo a button", "Undo another button.",
            ],
        },
        "daniel": {
            "nome": "Verso Daniel: proposta del cinema, vestito audace, lascia scegliere lui",
            "riserva": "prima",
            "scelte": [
                ## Giorno 1
                "Leave one button open.", "Explain calmly", "Pretend she didn't hear.",
                "Decline politely.", "Write for one more hour", "Order a pizza.",
                "Say yes, with a sigh.",
                ## Giorno 2
                "Eat alone at her desk", "«No thanks, I don't smoke.»",
                "Look away and think about something else.", "Pull your hand back.",
                "Keep the baggy t-shirt.", "«I'm here to work out, not to look.»",
                "Give him a quick nod.", "Look away: it's none of her business.",
                "Be excited for him.",
                ## Giorno 3
                "Propose her own idea.", "The most daring dress she owns.",
                "Let him choose.", "Tell him about it, with passion.",
                "Answer him back.", "Ask her what Daniel is really like.",
                "Smile politely.", "Ask him why he didn't react.",
                ## Giorno 4
                "«I liked you better before.»", "«Tell me about your dad, one day.»",
                "«Next time, answer him back.»",
                "«After all, that's how you conquered me.»",
                "Decline with a smile.", "One drink is enough.", "Write.",
                ## Giorno 5
                "Cut it short: she's late.", "«At least he doesn't forget people.»",
                "Ignore him.", "Go out with Joanie.",
                ## Giorno 6
                "Insist on making him a coffee.", "The short dress Joanie picked.",
                "Stay and talk with Simon.",
                ## Giorno 7
                "Write.", "Take the initiative.",
                ## Giorno 8
                "Focus on the piece.", "Go in anyway.", "«I'll do it myself",
                "«Thanks. I'll ask Joanie.»", "Tell [nome_compagno] about the session",
                ## Giorno 9
                "Something sweet.", "Offer to help him tidy up", "Hug him.", "Keep holding him a little longer.",
                "«Of course, Howard. A coffee now and then.»",
                ## Giorno 10
                "Point out it isn't her job.", "Leave it open.", "Ask her what happened.", "Play it down.",
                ## Scelte Corr +1 aggiunte il 21/11 (giorni 5, 7, 9)
                "«...He's not ugly.", "She asks him who he is.", "Send back an eye-roll.",
                ## Giorno 11
                "Eat alone, and write.", "A hug.", "Save it.", "Go in for a coffee.", "Stay for a second coffee.", "Undo a button", "Undo another button.",
            ],
        },
        "mista": {
            "nome": "Mista: scelte alternate, un po' di tutto",
            "riserva": "alternata",
            "scelte": [],
        },
    }
    ORDINE_PRESET_DEBUG = ["brava", "barbara", "daniel", "mista"]

    ## Stato del salto: None quando non si sta saltando.
    _debug_salto = None
    _foto_debug = {}
    _debug_menu_originale = None
    _debug_skip_unseen = None

    def opzioni_sceglibili(items):
        """Le scelte che il giocatore può davvero cliccare: (testo, valore)."""
        opzioni = []
        for (t, v) in items:
            if v is None:
                continue
            kw = getattr(v, "kwargs", None) or {}
            if rifiuto_howard_bloccato(kw) or (kw and not requisiti_ok(kw)):
                continue
            if kw.get("segreto"):
                continue
            opzioni.append((t, v))
        return opzioni

    def _debug_scegli_con(preset):
        contatore = [0]
        def scegli(items, **kwargs):
            opzioni = opzioni_sceglibili(items)
            contatore[0] += 1
            scelta = None
            for pref in preset["scelte"]:
                for (t, v) in opzioni:
                    if t.startswith(pref):
                        scelta = v
                        break
                if scelta is not None:
                    break
            if scelta is None:
                _debug_salto["senza_preferenza"].append(opzioni[0][0] if opzioni else "?")
                if preset["riserva"] == "prima":
                    scelta = opzioni[0][1]
                elif preset["riserva"] == "ultima":
                    scelta = opzioni[-1][1]
                else:
                    scelta = opzioni[contatore[0] % len(opzioni)][1]
            return getattr(scelta, "value", scelta)
        return scegli

    def giorni_debug():
        """I giorni da cui si può partire: quelli con un label ep1_dN, dal 2 in poi."""
        return [n for n in range(2, 31) if renpy.has_label("ep1_d%d" % n)]

    def debug_azzera_stato():
        """Rimette ogni variabile dichiarata con `default` al valore d'inizio partita
        (il nome del compagno resta). Serve anche ai test, che non ripartono da zero."""
        compagno = store.nome_compagno
        d = renpy.python.store_dicts["store"]
        for s in renpy.ast.default_statements:
            if s.store == "store":
                d[s.varname] = renpy.python.py_eval_bytecode(s.code.bytecode)
        store.nome_compagno = compagno

    def debug_prepara(giorno_arrivo, chiave):
        """Fa giocare da soli i giorni prima di giorno_arrivo con il preset scelto."""
        global _debug_salto, _debug_menu_originale, _debug_skip_unseen
        debug_azzera_stato()
        _debug_salto = {"arrivo": "ep1_d%d" % giorno_arrivo, "preset": chiave,
                        "arrivato": False, "senza_preferenza": []}
        _debug_menu_originale = store.menu
        store.menu = _debug_scegli_con(PRESET_DEBUG[chiave])
        _debug_skip_unseen = _preferences.skip_unseen
        _preferences.skip_unseen = True
        renpy.config.skipping = "fast"

    def _debug_fine_salto():
        global _debug_salto
        store.menu = _debug_menu_originale
        _preferences.skip_unseen = _debug_skip_unseen
        renpy.config.skipping = None
        _debug_salto["arrivato"] = True

    def _debug_traccia(nome, abnormal):
        if _debug_salto and not _debug_salto["arrivato"] and nome == _debug_salto["arrivo"]:
            _debug_fine_salto()
            ## Foto dello stato all'arrivo, per i test (fuori dal rollback).
            _foto_debug.clear()
            _foto_debug.update({"preset": _debug_salto["preset"], "giorno": giorno,
                                "fatti": dict(fatti), "corruption": sara_corruption,
                                "interest": {k: p.interest for k, p in percorsi.items()},
                                "senza_preferenza": list(_debug_salto["senza_preferenza"])})
            mancate = len(_debug_salto["senza_preferenza"])
            renpy.notify("DEBUG: preset «%s»%s" % (_debug_salto["preset"],
                         (", %d scelte senza preferenza" % mancate) if mancate else ""))
    config.label_callbacks.append(_debug_traccia)


## Chiamato dal menu iniziale (script.rpy) solo se config.developer.
label debug_partenza:
    python:
        _scelte_giorno = [("Day %d" % n, n) for n in giorni_debug()]
        _scelte_giorno.append(("Back", None))
        _giorno_debug = renpy.display_menu([("DEBUG: start from which day?", None)] + _scelte_giorno)
    if _giorno_debug is None:
        return
    python:
        _scelte_preset = [(PRESET_DEBUG[k]["nome"], k) for k in ORDINE_PRESET_DEBUG]
        _preset_debug = renpy.display_menu([("DEBUG: which configuration?", None)] + _scelte_preset)
        debug_prepara(_giorno_debug, _preset_debug)
    jump ep1_inizio
