## Sessioni libere con orologio in minuti. Le chat di trama usano msg come prima.
default telefono_minuti_ora = None
default telefono_minuti_fine = None
default telefono_minuti_uscita = "Put the phone down"
default telefono_minuti_chiudi = False
default telefono_minuti_riprese = {}
default telefono_minuti_inbox = {}
default telefono_minuti_risposte_lette = set()

init -4 python:
    ## Solo nei test: una funzione che sceglie il contatto al posto della rubrica.
    telefono_pilota = None

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
                _annuncia_testo(("%s wrote to Sara." if risposta.get("entrata") else "%s replied.") % nome_mittente(k))

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

    ## Chi scrive per primo (tabella approvata da Jody, 25/11/2026): probabilità ogni sera,
    ## giorni minimi fra due messaggi, e le sere in cui un fatto la alza.
    ENTRATE = {
        "howard": (0.60, 1, {}),
        "amica": (0.45, 2, {17: 0.80, 19: 0.80}),
        "ex": (0.35, 3, {}),
        "daniel": (0.35, 3, {}),
        "simon": (0.25, 3, {15: 0.50, 17: 0.50}),
        "amico": (0.20, 4, {14: 0.40, 16: 0.40}),
        "editore": (0.10, 7, {}),
        "capa": (0.20, 4, {}),
    }
    ENTRATE_PER_SERA = 2
    DANIEL_ROMANZO = ("daniel_intro", "daniel_t1", "daniel_t3")

    ## Se Sara lascia il messaggio senza risposta, il giorno dopo (gli altri non insistono).
    SILENZIO = {
        "howard": "Sara? Did I say something wrong?",
        "amica": "?? ok fine. I'll be here. being fascinating. on my own",
        "amico": "Lol, busy. Got it",
    }

    def _entrate_possibili(k):
        """Le chat che k può aprire stasera; se ce n'è, vengono prima i fatti vissuti insieme."""
        ora = store.telefono_minuti_ora % 1440
        if k in store.discorso_aperto or k in store.coda_chat or k in store.telefono_minuti_inbox:
            return []
        if store.giorno - store.ultima_entrata.get(k, -99) < ENTRATE[k][1]:
            return []
        if k == "ex" and not (ora >= 22 * 60 or ora < 2 * 60):
            return []
        if k == "simon" and not 18 * 60 <= ora < 23 * 60:
            return []
        if k == "capa" and (store.giorno - 1) % 7 >= 5:
            return []
        if k == "daniel" and store.daniel_tace:
            return []
        tutte = [d for d in discorsi_in_entrata(k) if renpy.has_label("chat_" + d.id + "_entrata")]
        if k == "daniel" and interesse_altrui(k) == "spento":
            tutte = [d for d in tutte if d.id in DANIEL_ROMANZO]
        return [d for d in tutte if d.argomento] or tutte

    def arriva_messaggio(k, id):
        """Un messaggio nuovo: aspetta nella rubrica, non apre la chat da solo."""
        store.discorso_aperto[k] = {"id": id, "parte": 0, "caldo": False, "frenato": False,
                                    "contesto_verificato": True, "premio_avvio": False,
                                    "premio_risposta": True, "giorno": store.giorno, "entrata": True}
        store.telefono_minuti_riprese[k] = "tel_chat_%s_entrata_1" % id
        store.telefono_minuti_inbox[k] = {"arrivo": store.telefono_minuti_ora, "bolle": 1,
                                          "notificata": False, "entrata": True}
        store.ultima_entrata[k] = store.giorno

    def _telefono_messaggi_in_entrata():
        """All'inizio della sera: al massimo due messaggi nuovi, in ordine a sorte."""
        if store.giorno_entrata == store.giorno:
            return
        store.giorno_entrata = store.giorno
        arrivati = 0
        for k in renpy.random.sample(contatti(), len(contatti())):
            if arrivati >= ENTRATE_PER_SERA:
                return
            possibili = _entrate_possibili(k)
            base, _, sere = ENTRATE[k]
            if possibili and renpy.random.random() < sere.get(store.giorno, base):
                arriva_messaggio(k, renpy.random.choice(possibili).id)
                arrivati += 1

    def _telefono_silenzi():
        """Messaggi lasciati senza risposta da almeno un giorno: ognuno reagisce a modo suo."""
        for k in list(store.discorso_aperto):
            aperto = store.discorso_aperto[k]
            if not aperto.get("premio_risposta") or aperto.get("giorno", store.giorno) >= store.giorno:
                continue
            if k == "daniel":
                abbandona_discorso(k)
                store.daniel_tace = True
            elif k in SILENZIO and not aperto.get("sollecitato"):
                aperto["silenzio"] = SILENZIO[k]
                aperto["sollecitato"] = True    # una volta sola per messaggio

    def telefono_minuti_blocco(punto, tipo, bolle=0):
        """True sospende la label. Una risposta si paga tutta prima della prima bolla."""
        if not telefono_minuti_attivo() or store.telefono_anteprima:
            return False
        k = store.chat_aperta
        if tipo == "ricevi":
            risposta = store.telefono_minuti_inbox.get(k)
            if risposta is None:
                arrivo = _telefono_arrivo_minuti(k)
                ## Chi risponde subito (Howard) lascia la chat aperta, se il tempo basta.
                if arrivo <= store.telefono_minuti_ora and bolle <= telefono_minuti_rimasti():
                    store.telefono_minuti_risposte_lette.add(k)
                    store.telefono_minuti_ora += bolle
                    _telefono_notifica_minuti()
                    return False
                store.telefono_minuti_inbox[k] = {
                    "arrivo": arrivo, "bolle": bolle, "notificata": False,
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
    $ chiudi_scadute()
    $ _telefono_silenzi()
    $ _telefono_messaggi_in_entrata()
    $ _telefono_notifica_minuti()
    while telefono_minuti_rimasti() > 0 and not telefono_minuti_chiudi:
        $ _azione_minuti = telefono_pilota() if telefono_pilota else renpy.call_screen("telefono")
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

label telefono_minuti_conversazione(k):
    if not _telefono_minuti_ripresa_disponibile(k):
        return
    if k in discorso_aperto:
        $ discorso_aperto[k]["contesto_verificato"] = True
    $ chat_aperta = k
    show screen telefono_chat(k)
    $ _nuova_minuti = None
    ## Letto ieri e lasciato lì: l'altro ha aggiunto qualcosa.
    if k in discorso_aperto and discorso_aperto[k].get("silenzio") and k not in telefono_minuti_inbox and chat_log.get(k) and chat_log[k][-1][0] == k:
        $ telefono_minuti_ora += 1
        $ msg(k, discorso_aperto[k].pop("silenzio"))
    ## Chat in sospeso (non appena arrivata): Sara può riprenderla, salutare o cambiare discorso.
    if k in discorso_aperto and telefono_minuti_stato(k) in ("aperto", "attesa") and not chat_introduttiva_aperta(k):
        call telefono_sospesa(k)
        if _return == "indietro":
            jump .fine
        if _return != "riprendi":
            $ _nuova_minuti = _return
    elif k not in discorso_aperto and k not in telefono_minuti_riprese:
        call telefono_scelta_tipo(k)
        if _return is None:
            jump .fine
        $ _nuova_minuti = _return
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
        ## Il messaggio era rimasto lì da ieri: dopo averlo letto, l'altro ha aggiunto qualcosa.
        if k in discorso_aperto and discorso_aperto[k].get("silenzio") and chat_log.get(k) and chat_log[k][-1][0] == k:
            $ telefono_minuti_ora += 1
            $ msg(k, discorso_aperto[k].pop("silenzio"))
    elif k not in discorso_aperto:
        $ _discorso_minuti = DISCORSI[_nuova_minuti]
        $ discorso_aperto[k] = {"id": _discorso_minuti.id, "parte": 0, "caldo": False, "frenato": False, "contesto_verificato": True, "premio_avvio": True, "giorno": giorno}
        if k == "daniel":
            $ daniel_tace = False
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

## Sara apre una chat: prima il tipo (o un argomento), poi vede il messaggio e lo conferma.
## Restituisce l'id della chat, o None se torna ai messaggi.
label telefono_scelta_tipo(k):
    python:
        _voci_tel = [(t, ("tipo", t)) for t in TIPI_CHAT if discorsi_di_tipo(k, t)]
        _voci_tel += [(d.argomento, ("argomento", d.id)) for d in argomenti_disponibili(k)]
        _voci_tel.append(("Back to messages.", ("indietro", None)))
        _come_tel, _cosa_tel = renpy.display_menu(_voci_tel, screen="scelta_telefono")
    if _come_tel == "indietro":
        return None
    $ _tipo_tel = _cosa_tel if _come_tel == "tipo" else None
    $ _id_tel = discorso_pescato(k, _tipo_tel) if _tipo_tel else _cosa_tel
    ## I label d'apertura contengono solo il messaggio di Sara: qui si leggono senza mandarlo.
    $ telefono_anteprima = True
    $ telefono_anteprima_testo = ""
    call expression "chat_" + _id_tel
    $ _manda_tel = renpy.display_menu([("«%s»" % telefono_anteprima_testo.replace("[", "[[").replace("{", "{{"), True), ("Not now.", False)], screen="scelta_telefono")
    $ telefono_anteprima = False
    if not _manda_tel:
        jump telefono_scelta_tipo_ancora
    if _tipo_tel:
        $ giorno_tipo[k] = giorno
    return _id_tel

label telefono_scelta_tipo_ancora:
    call telefono_scelta_tipo(chat_aperta)
    return _return

## Una chat lasciata a metà: riprenderla, salutare (si chiude per sempre) o cambiare discorso.
label telefono_sospesa(k):
    python:
        _voci_tel = []
        if telefono_minuti_stato(k) == "aperto":
            _voci_tel.append(("Pick up where you left off.", "riprendi"))
        if iniziative(k):
            _voci_tel.append(("Change the subject.", "cambia"))
        _voci_tel.append(("Say goodbye.", "saluta"))
        _voci_tel.append(("Back to messages.", "indietro"))
        _cosa_tel = renpy.display_menu(_voci_tel, screen="scelta_telefono")
    if _cosa_tel == "saluta":
        $ abbandona_discorso(k)
        $ msg("sara", saluto_chat(k))
        $ telefono_minuti_ora += 1
        return "indietro"
    if _cosa_tel == "cambia":
        call telefono_scelta_tipo(k)
        if _return is None:
            return "indietro"
        $ _id_nuovo_tel = _return
        $ abbandona_discorso(k)
        $ _raccordo_tel = raccordo_chat(k)
        if _raccordo_tel:
            $ msg("sara", _raccordo_tel)
            $ telefono_minuti_ora += 1
        return _id_nuovo_tel
    return _cosa_tel
