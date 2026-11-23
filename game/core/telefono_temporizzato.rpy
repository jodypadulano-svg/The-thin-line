## Sessioni libere con orologio in minuti. Le chat di trama usano msg come prima.
default telefono_minuti_ora = None
default telefono_minuti_fine = None
default telefono_minuti_uscita = "Put the phone down"
default telefono_minuti_chiudi = False
default telefono_minuti_riprese = {}
default telefono_minuti_inbox = {}
default telefono_minuti_risposte_lette = set()

init -4 python:
    ## Minimo e massimo di attesa alla prima fascia utile, in minuti.
    TELEFONO_ATTESE = {
        "amica": (1, 4), "howard": (0, 0), "simon": (3, 20),
        "amico": (1, 8), "ex": (3, 25), "daniel": (5, 900),
        "editore": (1440, 2880), "capa": (720, 1440),
    }

    def telefono_minuti_attivo():
        return store.telefono_minuti_fine is not None

    def telefono_minuti_rimasti():
        return store.telefono_minuti_fine - store.telefono_minuti_ora

    def telefono_orario(minuto):
        ore, minuti = divmod(minuto % 1440, 60)
        return "%02d:%02d" % (ore, minuti)

    def _telefono_orario_adatto(k, minuto):
        giorno, ora = divmod(minuto, 1440)
        if k == "capa":
            return (giorno - 1) % 7 < 5 and 9 * 60 <= ora < 17 * 60
        if k == "simon":
            return 18 * 60 <= ora < 23 * 60
        if k == "ex":
            return ora >= 22 * 60 or ora < 2 * 60
        return True

    def _telefono_arrivo_minuti(k):
        minimo, massimo = TELEFONO_ATTESE[k]
        if k == "daniel" and renpy.random.random() < 0.45:
            massimo = 25
        attesa = renpy.random.randint(minimo, massimo)
        livello = gradino(k)
        if k != "howard" and livello >= INTIMI:
            attesa = min(attesa, 3)
        elif livello >= COMPLICI:
            attesa //= 2
        arrivo = store.telefono_minuti_ora + attesa
        while not _telefono_orario_adatto(k, arrivo):
            arrivo += 1
        return arrivo

    def _telefono_notifica_minuti():
        vibrato = False
        for k in contatti():
            risposta = store.telefono_minuti_inbox.get(k)
            if (risposta and not risposta["notificata"]
                    and risposta["arrivo"] <= store.telefono_minuti_ora
                    and _telefono_minuti_ripresa_disponibile(k)):
                risposta["notificata"] = True
                if not vibrato:
                    suono("telefono_vibra")
                    vibrato = True
                _annuncia_testo("%s replied." % nome_mittente(k))

    def _telefono_prossimo_minuto():
        ora = store.telefono_minuti_ora
        return min([store.telefono_minuti_fine] + [
            v["arrivo"] for k, v in store.telefono_minuti_inbox.items()
            if k in contatti() and v["arrivo"] > ora and _telefono_minuti_ripresa_disponibile(k)
        ])

    def _telefono_minuti_ripresa_disponibile(k):
        aperto = store.discorso_aperto.get(k)
        if not aperto or aperto.get("contesto_verificato"):
            return True
        return discorso_contesto_ok(DISCORSI[aperto["id"]])

    def telefono_minuti_stato(k):
        if not _telefono_minuti_ripresa_disponibile(k):
            return "contesto"
        risposta = store.telefono_minuti_inbox.get(k)
        if risposta:
            if risposta["arrivo"] > store.telefono_minuti_ora:
                return "attesa"
            return "risposta" if risposta["bolle"] <= telefono_minuti_rimasti() else "rinviata"
        return stato_contatto(k)

    def _telefono_importa_coda():
        for k, precedente in list(store.coda_chat.items()):
            if k in store.discorso_aperto and k not in store.telefono_minuti_inbox:
                giorno, fascia = divmod(precedente["arrivo"], len(FASCE))
                store.telefono_minuti_inbox[k] = {
                    "arrivo": giorno * 1440 + ORARI_FASCE_TELEFONO[fascia],
                    "bolle": int(bool(precedente.get("insiste"))),
                    "notificata": precedente.get("rimandata", False),
                    "precedente": precedente,
                }
                del store.coda_chat[k]

    def _telefono_contatto_in_entrata():
        if store.giorno_entrata == store.giorno:
            return None
        candidati = [
            (k, d.id)
            for k in contatti()
            if telefono_minuti_stato(k) == "nuovo"
            and store.giorno - store.ultima_entrata.get(k, -99) >= GIORNI_TRA_ENTRATE
            for d in discorsi_in_entrata(k)
            if renpy.has_label("chat_" + d.id + "_entrata")
        ]
        if candidati and renpy.random.random() < PROBABILITA_ENTRATA:
            return renpy.random.choice(candidati)
        return None

    def telefono_minuti_blocco(punto, tipo, bolle=0):
        """True sospende la label. Una risposta si paga tutta prima della prima bolla."""
        if not telefono_minuti_attivo():
            return False
        k = store.chat_aperta
        if tipo == "ricevi":
            risposta = store.telefono_minuti_inbox.get(k)
            if risposta is None:
                store.telefono_minuti_inbox[k] = {
                    "arrivo": _telefono_arrivo_minuti(k), "bolle": bolle, "notificata": False,
                }
                _telefono_notifica_minuti()
                store.telefono_minuti_riprese[k] = punto
                return True
            if risposta["arrivo"] > store.telefono_minuti_ora or bolle > telefono_minuti_rimasti():
                store.telefono_minuti_riprese[k] = punto
                return True
            del store.telefono_minuti_inbox[k]
            store.telefono_minuti_risposte_lette.add(k)
        else:
            appena_letto = k in store.telefono_minuti_risposte_lette
            store.telefono_minuti_risposte_lette.discard(k)
            if max(bolle, 1) > telefono_minuti_rimasti() or (tipo == "invia" and appena_letto):
                store.telefono_minuti_riprese[k] = punto
                return True
        store.telefono_minuti_ora += bolle
        _telefono_notifica_minuti()
        return False

label telefono_minuti_sessione(inizio, fine, uscita="Put the phone down"):
    $ renpy.stop_skipping()
    $ telefono_minuti_ora = giorno * 1440 + inizio
    $ telefono_minuti_fine = giorno * 1440 + fine
    $ telefono_minuti_uscita = uscita
    $ telefono_minuti_chiudi = False
    $ _telefono_importa_coda()
    $ _telefono_notifica_minuti()
    $ _entrata_minuti = _telefono_contatto_in_entrata()
    if _entrata_minuti:
        call telefono_minuti_conversazione(_entrata_minuti[0], _entrata_minuti[1])
    while telefono_minuti_rimasti() > 0 and not telefono_minuti_chiudi:
        $ _azione_minuti = renpy.call_screen("telefono")
        if _azione_minuti is None or _azione_minuti[0] == "chiudi":
            jump .fine
        if _azione_minuti[0] == "aspetta":
            $ telefono_minuti_ora = _telefono_prossimo_minuto()
            $ _telefono_notifica_minuti()
        else:
            call telefono_minuti_conversazione(_azione_minuti[1])
    label .fine:
    $ telefono_minuti_fine = None
    $ telefono_minuti_ora = None
    return

label telefono_minuti_conversazione(k, entrata=None):
    if not _telefono_minuti_ripresa_disponibile(k):
        return
    if k in discorso_aperto:
        $ discorso_aperto[k]["contesto_verificato"] = True
    $ chat_aperta = k
    show screen telefono_chat(k)
    $ _legacy_minuti = telefono_minuti_inbox.get(k, {}).get("precedente")
    if _legacy_minuti:
        $ telefono_minuti_inbox.pop(k)
        if _legacy_minuti.get("insiste"):
            $ telefono_minuti_ora += 1
            $ _telefono_notifica_minuti()
            $ msg(k, _legacy_minuti["insiste"])
    if k in telefono_minuti_riprese:
        $ _punto_minuti = telefono_minuti_riprese.pop(k)
        call expression _punto_minuti
    elif k not in discorso_aperto:
        $ _discorso_minuti = DISCORSI[entrata] if entrata else renpy.random.choice(discorsi_disponibili(k))
        $ discorso_aperto[k] = {"id": _discorso_minuti.id, "parte": 0, "caldo": False, "frenato": False, "contesto_verificato": True, "premio_avvio": not entrata}
        if entrata:
            $ ultima_entrata[k] = giorno
            $ giorno_entrata = giorno
            call expression "chat_" + entrata + "_entrata"
        else:
            call expression "chat_" + _discorso_minuti.id

    while k not in telefono_minuti_riprese:
        $ _parte_minuti = discorso_aperto[k]["parte"] + 1
        $ _label_minuti = _parte(discorso_aperto[k]["id"], _parte_minuti)
        if discorso_aperto[k]["frenato"] or not _label_minuti:
            $ telefono_minuti_risposte_lette.discard(k)
            call telefono_fine_discorso(k)
            jump .fine
        $ discorso_aperto[k]["parte"] = _parte_minuti
        call expression _label_minuti

    label .fine:
    hide screen telefono_chat
    $ chat_aperta = None
    return
