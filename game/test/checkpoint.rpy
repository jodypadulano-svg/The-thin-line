## Stati di inizio giornata per i test mirati. Il JSON viene generato solo
## dalla suite checkpoint_ep1, in un passaggio con la strategia «prima».

init python:
    import json
    from pathlib import Path

    _checkpoint_raccolta = None

    def _checkpoint_file():
        return Path(config.gamedir) / "test" / "checkpoint_ep1.json"

    def _checkpoint_stato():
        stato = {
            s.varname: getattr(store, s.varname)
            for s in renpy.ast.default_statements
            if s.store == "store"
        }
        stato["abiti_visti"] = sorted(stato["abiti_visti"])
        stato["percorsi"] = {
            chiave: dict(vars(p), interest=p.interest, tappa=p.tappa,
                        chiuso=p.chiuso, incontrato=p.incontrato)
            for chiave, p in store.percorsi.items()
        }
        return stato

    def _checkpoint_registra(nome, abnormal):
        if _checkpoint_raccolta is None or not renpy.is_in_test():
            return
        giorno_arrivo = store.giorno + 1
        if 2 <= giorno_arrivo <= 13 and nome == "ep1_d%d" % giorno_arrivo:
            # Serializzare subito evita di conservare liste e dizionari che
            # le giornate successive potrebbero ancora modificare.
            _checkpoint_raccolta[str(giorno_arrivo)] = json.loads(json.dumps(_checkpoint_stato()))

    config.label_callbacks.append(_checkpoint_registra)

    def carica_checkpoint_ep1(giorno_arrivo):
        """Carica lo stato prima della giornata e restituisce la label da chiamare."""
        dati = json.loads(_checkpoint_file().read_text(encoding="utf-8"))
        if dati["versione"] != 1:
            raise ValueError("Versione del checkpoint non supportata")
        stato = dati["giorni"][str(giorno_arrivo)]
        if stato["giorno"] != giorno_arrivo - 1:
            raise ValueError("Il checkpoint non corrisponde al giorno richiesto")
        debug_azzera_stato()
        for chiave, valori in stato.pop("percorsi").items():
            vars(store.percorsi[chiave]).update(valori)
        stato["abiti_visti"] = set(stato["abiti_visti"])
        for nome, valore in stato.items():
            setattr(store, nome, valore)
        return "ep1_d%d" % giorno_arrivo

testsuite checkpoint_ep1:
    enabled False
    testcase genera:
        description "Registra i giorni 2–13 in un passaggio, senza proseguire oltre l'apertura del giorno 13."
        $ _checkpoint_raccolta = {}
        $ _test_scelte("prima")
        run Jump("ep1_inizio")
        advance until eval "13" in _checkpoint_raccolta timeout 300.0
        assert eval set(_checkpoint_raccolta) == set(str(giorno) for giorno in range(2, 14))
        python:
            destinazione = _checkpoint_file()
            temporaneo = destinazione.with_suffix(".tmp")
            dati = {"versione": 1, "strategia": "prima", "giorni": _checkpoint_raccolta}
            temporaneo.write_text(json.dumps(dati, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            temporaneo.replace(destinazione)
            _checkpoint_raccolta = None
        assert eval carica_checkpoint_ep1(13) == "ep1_d13" and giorno == 12
