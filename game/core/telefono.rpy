## =============================================================================
## TELEFONO — rubrica, discorsi a pesca, scambi, interruzioni, serate alternative
## =============================================================================
## Specifica: docs/telefono-e-percorsi-dinamici.md, sezioni 10 e 11 (18/11/2026).
##
## Nel codice delle giornate:
##   $ da_numero("simon")                  Sara ottiene il numero (entra in rubrica)
##   $ sblocca_telefono()                  giorno 14, la cucina con Sally
##   call telefono_fascia("sera")          inizio di una fascia: arrivano le risposte
##   call telefono_fascia("sera", con_josh=True)   ...mentre Sara è con Josh
##   call telefono_slot                    Sara può prendere il telefono (lo slot del giorno)
##   call serata_sostituibile              giorno 22: uscita con un contatto a C+ o Josh
##   if gradino("simon") >= CONFIDENZA:    varianti delle scene fisse
##   if fatto("chat_simon_dieta"):         la scena ricorda una chat finita
##
## Nel codice dei percorsi (game/percorsi/, un file per personaggio): vedi
## game/percorsi/leggimi_percorsi.rpy per il modello di un discorso.

init -6 python:
    ## Gradini del rapporto (Interest con quattro soglie per personaggio, 10.3).
    ESTRANEI, CONOSCENTI, CONFIDENZA, COMPLICI, INTIMI = 0, 1, 2, 3, 4

init -5 python:

    FASCE = ["mattina", "lavoro", "pranzo", "sera", "notte"]
    ORARI_FASCE_TELEFONO = (8 * 60, 9 * 60, 12 * 60 + 30, 20 * 60, 23 * 60)

    SOGLIE_RAPPORTO = {
        "simon":   (5, 10, 16, 22),
        "howard":  (4, 9, 14, 20),
        "daniel":  (3, 7, 12, 18),
        "editore": (3, 7, 12, 18),
        "ex":      (5, 12, 18, 25),
        "amica":   (3, 7, 12, 18),
        "amico":   (3, 7, 12, 18),
        "capa":    (3, 7, 15, 25),
    }

    ## Ritardo delle risposte (10.6): (minimo, massimo) in fasce, fasce in cui
    ## risponde, solo nei giorni lavorativi.
    RITARDI = {
        "amica":   (0, 0, None, False),
        "howard":  (0, 0, None, False),
        "simon":   (0, 1, ("sera", "notte"), False),
        "amico":   (0, 1, None, False),
        "ex":      (0, 1, ("notte",), False),
        "daniel":  (1, 5, None, False),
        "editore": (5, 10, None, False),
        "capa":    (1, 5, ("lavoro", "pranzo"), True),
    }

    ## Solleciti (10.7): anticipo in fasce, Interest, Corruption, Confidence.
    SOLLECITI = {
        "amica":   (0, 0, 0, 0),
        "howard":  (0, 0, 0, 0),
        "simon":   (1, 1, 0, 0),
        "ex":      (1, 1, 0, 0),
        "amico":   (1, 1, 0, 0),
        "daniel":  (0, 0, 1, -1),
        "editore": (0, 0, 0, 0),
        "capa":    (0, -1, 0, -1),
    }

    ## Probabilità che l'altro si fermi a un punto di interruzione (11.4).
    PAUSA = {
        "daniel": 0.5, "editore": 0.4, "capa": 0.3,
        "simon": 0.25, "ex": 0.25,
        "amica": 0.05, "amico": 0.05,
        "howard": 0.0,
    }

    GIORNI_FRENO = 5            # dopo un freno, niente flirt per qualche giorno
    GIORNI_TRA_ENTRATE = 3
    PROBABILITA_ENTRATA = 0.35
    PROBABILITA_JOSH = 0.25

    ## --- Discorsi ------------------------------------------------------------------

    class Discorso(object):
        """Una conversazione a più scambi (11.1). Vive nel registro DISCORSI,
        costruito all'avvio: nei salvataggi ci finiscono solo gli id."""
        def __init__(self, id, chiave, gradino, se, flirt, prova, scrive_lui=False, orario=None, tipo=None, argomento=None, scade=None, ricambiato=True):
            self.scrive_lui = scrive_lui
            self.tipo = tipo or TIPO_DI_GRADINO[gradino]
            self.argomento = argomento
            self.scade = scade
            self.ricambiato = ricambiato
            self.id = id
            self.chiave = chiave
            self.gradino = gradino
            self.se = se
            self.flirt = flirt
            self.prova = prova
            self.orario = orario

    DISCORSI = {}

    ## Tipo di chat (specifica del 25/11/2026). Quelli non detti si ricavano dal gradino.
    TIPI_CHAT = ("Casual", "Friendly", "Flirt", "Sexting")
    TIPO_DI_GRADINO = {ESTRANEI: "Casual", CONOSCENTI: "Casual", CONFIDENZA: "Friendly",
                       COMPLICI: "Flirt", INTIMI: "Sexting"}

    def discorso(id, chiave, gradino=CONOSCENTI, se=None, flirt=False, prova=False, scrive_lui=False, orario=None, tipo=None, argomento=None, scade=None, ricambiato=True):
        """Registra un discorso. se = condizione come testo, es. "fatto('ep1_festa')".
        orario = (inizio, fine esclusa), in minuti da mezzanotte, anche a cavallo della notte.
        scrive_lui=True: può aprirlo lui con un messaggio in entrata anche sotto B
        (es. Daniel dopo la festa, Magnus che aspetta le pagine).
        tipo = "Casual", "Friendly", "Flirt" o "Sexting" (se no lo dice il gradino).
        argomento = titolo: la chat è un argomento specifico, si sceglie per nome.
        scade = condizione che chiude per sempre la chat rimasta aperta: un fatto vissuto di
        persona (es. "fatto('ep2_d17_ritiro_howard')") o il tempo ("aperta_da >= 1", in giorni).
        ricambiato=False: come reagisce a un Flirt o Sexting di Sara che non ricambia."""
        DISCORSI[id] = Discorso(id, chiave, gradino, se, flirt, prova, scrive_lui, orario, tipo, argomento, scade, ricambiato)

    ## Discorsi segnaposto per la prova degli sviluppatori (non escono nel gioco vero).
    _SEGNAPOSTO = {ESTRANEI: 1, CONOSCENTI: 3, CONFIDENZA: 2, COMPLICI: 2, INTIMI: 1}
    for _k in SOGLIE_RAPPORTO:
        for _g, _n in _SEGNAPOSTO.items():
            for _i in range(1, _n + 1):
                discorso("%s_prova_%d_%d" % (_k, _g, _i), _k, _g,
                         se=("oltre_soglia('%s')" % _k) if _g == INTIMI else None,
                         flirt=_g >= COMPLICI, prova=True)

    def gradino(chiave):
        """0 estranei · 1 conoscenti · 2 in confidenza · 3 complici · 4 intimi."""
        valore = percorso(chiave).interest
        return sum(1 for s in SOGLIE_RAPPORTO[chiave] if valore >= s)

    def discorso_contesto_ok(d):
        if d.se and not eval(d.se):
            return False
        if d.orario is None:
            return True
        minuto = store.telefono_minuti_ora
        ora = ORARI_FASCE_TELEFONO[store.fascia_corrente] if minuto is None else minuto % 1440
        inizio, fine = d.orario
        return inizio <= ora < fine if inizio < fine else ora >= inizio or ora < fine

    def tipo_aperto(k, tipo):
        """Le soglie di Sara (specifica del 25/11/2026): strette, 5 e 15 non bastano."""
        if tipo == "Friendly":
            return valore_interest(k) > 5
        if tipo == "Flirt":
            return valore_interest(k) > 15
        if tipo == "Sexting":
            ## Barbara bacia Sara quando firma da stagista (giorno 17).
            return fatto("bacio_" + k) or (k == "capa" and store.sara_stagista)
        return True

    def risposta_giusta(d):
        """Flirt e Sexting cominciati da Sara: ricambiati o no? Daniel sotto il giorno non
        ricambia. Magnus e Barbara, sereni, la prima volta prendono tempo: una chat non
        ricambiata per tipo, poi si aprono le altre. Con gli altri è sempre ricambiata."""
        if d.tipo not in ("Flirt", "Sexting"):
            return True
        interesse = interesse_altrui(d.chiave)
        if interesse == "spento":
            return not d.ricambiato
        if interesse == "sereno":
            provato = any(not x.ricambiato and x.chiave == d.chiave and x.tipo == d.tipo and x.id in store.discorsi_fatti
                          for x in DISCORSI.values())
            return d.ricambiato == provato
        return d.ricambiato

    def discorso_disponibile(d, scrive_altro=False):
        """scrive_altro: chi scrive per primo non è legato alle soglie di Sara."""
        k = d.chiave
        if d.id in store.discorsi_fatti:
            return False
        if d.prova and not store.telefono_segnaposto:
            return False
        if "_intro" in d.id and any(f.startswith(k + "_intro") for f in store.discorsi_fatti):
            return False
        if d.argomento or scrive_altro:
            if gradino(k) < d.gradino:
                return False
        elif not tipo_aperto(k, d.tipo) or not risposta_giusta(d):
            return False
        if d.flirt and store.freno.get(k, -99) > store.giorno:
            return False
        return discorso_contesto_ok(d)

    def discorsi_disponibili(chiave):
        return [d for _, d in sorted(DISCORSI.items()) if d.chiave == chiave and discorso_disponibile(d)]

    def interesse_altrui(k):
        """Quanto l'altro è preso da Sara (specifica 25/11, sezione 6): "alto", "sereno"
        oppure, per chi dipende da lei, "acceso" o "spento"."""
        if k in ("howard", "ex", "amica"):
            return "alto"
        if k in ("capa", "editore"):
            return "sereno"
        if k == "daniel":
            return "acceso" if valore_interest(k) >= store.giorno else "spento"
        return "acceso" if tipo_aperto(k, "Flirt") else "spento"

    def prende_iniziativa(d):
        """Iniziative romantiche degli altri: Daniel solo con Interest almeno pari al giorno,
        Simon e Darius specchio di Sara, Magnus e Barbara mai. Le altre chat sono libere."""
        return d.tipo in ("Casual", "Friendly") or interesse_altrui(d.chiave) in ("alto", "acceso")

    def discorsi_in_entrata(chiave):
        """I discorsi che lui o lei può aprire scrivendo per primo: tutti da B in su,
        sotto B solo quelli segnati scrive_lui."""
        tutti = [d for _, d in sorted(DISCORSI.items()) if d.chiave == chiave and d.ricambiato and discorso_disponibile(d, scrive_altro=True) and prende_iniziativa(d)]
        if gradino(chiave) >= CONFIDENZA:
            return tutti
        ## Sotto Confidenza scrivono solo per un fatto vissuto insieme.
        return [d for d in tutti if d.argomento or getattr(d, "scrive_lui", False)]

    ## --- Iniziative di Sara: tipo o argomento (specifica del 25/11/2026) ------------

    def argomenti_disponibili(chiave):
        return [d for d in discorsi_disponibili(chiave) if d.argomento]

    def discorsi_di_tipo(chiave, tipo):
        """Una sola chat nuova per tipo al giorno con ogni contatto; gli argomenti non contano."""
        if store.giorno_tipo.get(chiave) == store.giorno:
            return []
        tutti = [d for d in discorsi_disponibili(chiave) if not d.argomento and d.tipo == tipo]
        ## L'introduzione viene prima di ogni altra chat Casual.
        return [d for d in tutti if "_intro" in d.id] or tutti

    def iniziative(chiave):
        return bool(argomenti_disponibili(chiave)) or any(discorsi_di_tipo(chiave, t) for t in TIPI_CHAT)

    def discorso_pescato(chiave, tipo):
        """La chat proposta per quel tipo: per tutto il giorno resta la stessa."""
        candidati = discorsi_di_tipo(chiave, tipo)
        salvata = store.anteprime_chat.get((chiave, tipo))
        if salvata and salvata[0] == store.giorno and any(d.id == salvata[1] for d in candidati):
            return salvata[1]
        scelto = renpy.random.choice(candidati).id
        store.anteprime_chat[(chiave, tipo)] = (store.giorno, scelto)
        return scelto

    def chat_introduttiva_aperta(k):
        ## Solo l'introduzione vera: anche alcuni argomenti partono da Estranei (Jacob, Magnus).
        return "_intro" in store.discorso_aperto[k]["id"]

    def abbandona_discorso(k):
        """Chiusa per sempre, senza premi: la chat non si ripete (i messaggi restano)."""
        aperto = store.discorso_aperto.pop(k, None)
        if aperto and aperto["id"] not in store.discorsi_fatti:
            store.discorsi_fatti.append(aperto["id"])
        for dove in (store.coda_chat, store.telefono_minuti_inbox, store.telefono_minuti_riprese):
            dove.pop(k, None)
        store.telefono_minuti_risposte_lette.discard(k)

    def chiudi_scadute():
        """All'apertura del telefono: le chat scadute o concluse dal vivo si chiudono."""
        for k in list(store.discorso_aperto):
            aperto = store.discorso_aperto[k]
            scade = DISCORSI[aperto["id"]].scade
            if scade and eval(scade, {"aperta_da": store.giorno - aperto.get("giorno", store.giorno)}, vars(store)):
                abbandona_discorso(k)

    def tipo_chat_aperta():
        """Il tipo da mostrare accanto alle risposte, se il giocatore lo vuole."""
        aperto = store.discorso_aperto.get(store.chat_aperta) if persistent.mostra_tipo_chat and not store.telefono_anteprima else None
        return DISCORSI[aperto["id"]].tipo if aperto else None

    def raccordo_chat(k):
        """Come Sara cambia discorso, secondo l'ultimo messaggio rimasto lì."""
        ultimi = store.chat_log.get(k, [])
        if not ultimi:
            return None
        chi, testo = ultimi[-1][:2]
        if chi != "sara" and testo.rstrip().endswith("?"):
            frasi = ["Sorry, I never answered you. Can I ask you something else first?",
                     "I know, I left that hanging. Something else came up.",
                     "I owe you an answer. Can it wait a bit?"]
        elif chi != "sara":
            frasi = ["Anyway. Changing the subject.", "Anyway, I wanted to tell you something.",
                     "Right. Completely different thing."]
        else:
            frasi = ["Forget that. Something else.", "Never mind what I said before.",
                     "Actually, let me start again."]
        return renpy.random.choice(frasi)

    def saluto_chat(k):
        return renpy.random.choice(["I've got to go. Talk soon.", "I'm putting the phone down. Night.",
                                    "I have to run. Speak later."])

    def _parte(id, n):
        nome = "chat_%s_%d" % (id, n)
        return nome if renpy.has_label(nome) else None

    def _ha_parte(id, n):
        return _parte(id, n) is not None or (DISCORSI[id].prova and n <= 2)

    def caldo():
        """Premia la reazione e conserva il bonus di chiusura del discorso."""
        k = store.chat_aperta
        store.discorso_aperto[k]["caldo"] = True
        interest(k, 1, "The conversation made an impression on Sara.")

    def frena():
        """Sara smorza: il discorso finisce senza Interest e per un po' niente flirt."""
        store.discorso_aperto[store.chat_aperta]["frenato"] = True

    ## --- Tempo ----------------------------------------------------------------------

    def adesso():
        return store.giorno * len(FASCE) + store.fascia_corrente

    def _giorno_lavorativo(istante):
        return (istante // len(FASCE) - 1) % 7 < 5

    def _fascia_ok(chiave, istante):
        _, _, fasce, lavorativi = RITARDI[chiave]
        if fasce and FASCE[istante % len(FASCE)] not in fasce:
            return False
        if lavorativi and not _giorno_lavorativo(istante):
            return False
        return True

    def _calcola_arrivo(chiave, minimo_ritardo=0):
        """Quando arriva la risposta: deciso subito e salvato (niente ricarica e riprova)."""
        minimo, massimo, _, _ = RITARDI[chiave]
        ritardo = renpy.random.randint(minimo, massimo)
        g = gradino(chiave)
        if g >= INTIMI:
            ritardo = 0
        elif g >= COMPLICI:
            ritardo = max(0, ritardo - 1)
        arrivo = adesso() + max(ritardo, minimo_ritardo)
        while not _fascia_ok(chiave, arrivo):
            arrivo += 1
        return arrivo

    def _prob_pausa(chiave):
        if chiave == "capa" and FASCE[store.fascia_corrente] not in ("lavoro", "pranzo"):
            return 1.0
        return PAUSA[chiave]

    ## --- Rubrica --------------------------------------------------------------------

    def sblocca_telefono():
        if not store.telefono_libero:
            store.telefono_libero = True
            _annuncia_testo("Sara's phone feels different tonight.")

    def da_numero(chiave):
        if chiave not in store.rubrica:
            store.rubrica.append(chiave)
            _annuncia_testo("New contact: {}".format(nome_percorso(percorso(chiave))))

    def ha_numero(chiave):
        return chiave in store.rubrica

    def contatti():
        return [k for k in store.rubrica if not percorso(k).chiuso]

    def stato_contatto(k):
        """risposta: da leggere · attesa: tocca all'altro · aperto: Sara ha messo giù · nuovo · vuoto."""
        if k in store.coda_chat:
            return "risposta" if store.coda_chat[k]["arrivo"] <= adesso() else "attesa"
        if k in store.discorso_aperto:
            return "aperto"
        if (iniziative(k) if telefono_minuti_attivo() else discorsi_disponibili(k)):
            return "nuovo"
        return "vuoto"

    def contatti_attivi():
        return [k for k in contatti() if stato_contatto(k) != "vuoto"]

    def in_attesa(chiave):
        return chiave in store.coda_chat

    def slot_libero():
        return store.telefono_libero and store.giorno_slot != store.giorno

    ## --- Messaggi a schermo ---------------------------------------------------------

    def msg(chi, testo, immagine=None, premia_avvio=True):
        """Un messaggio nella chat aperta. chi = "sara", "josh" o la chiave del contatto."""
        if store.telefono_anteprima:
            store.telefono_anteprima_testo = renpy.substitute(testo)
            return
        renpy.stop_skipping()
        k = store.chat_aperta
        ## «typing…» prima di un messaggio dell'altro, per il tempo di scriverlo.
        if chi == k and not telefono_pilota and not renpy.is_in_test():
            store.tel_scrive = k
            renpy.restart_interaction()
            renpy.pause(min(1.6, 0.5 + len(testo) * 0.012))
            store.tel_scrive = None
        ## Mittente, testo, immagine, minuto e giorno (i vecchi messaggi hanno solo i primi).
        ora = store.telefono_minuti_ora
        messaggio = (chi, renpy.substitute(testo), immagine, None if ora is None else ora % 1440, store.giorno)
        store.chat_log.setdefault(k, []).append(messaggio)
        aperto = store.discorso_aperto.get(k)
        if premia_avvio and chi == "sara" and aperto and aperto.pop("premio_avvio", False):
            interest(k, 1, "Sara started a new conversation.")
        if premia_avvio and chi == "sara" and aperto and aperto.pop("premio_risposta", False):
            interest(k, 1, "Sara answered.")
        if telefono_pilota:
            return
        renpy.restart_interaction()
        renpy.pause()

    def nome_mittente(chi):
        if chi == "sara":
            return "Sara"
        if chi == "josh":
            return store.nome_compagno
        return nome_percorso(percorso(chi))


## Stato del telefono (tutto con default: i vecchi salvataggi restano validi).
default telefono_libero = False
default telefono_segnaposto = False    # True solo nella prova degli sviluppatori
default rubrica = ["amica", "amico"]   # Joanie e Darius da subito (10.2)
default passi_chat = {}                # chiave -> discorsi finiti con quel contatto
default discorsi_fatti = []            # id dei discorsi finiti
default discorso_aperto = {}           # chiave -> {"id", "parte", "caldo", "frenato"}
default coda_chat = {}                 # chiave -> {"arrivo", "letto", "rimandata", "insiste"}
default freno = {}                     # chiave -> giorno fino al quale niente flirt
default chat_lasciate = []             # non più usato: resta per i vecchi salvataggi
default persistent.mostra_tipo_chat = False
default chat_log = {}                  # chiave -> [(mittente, testo[, immagine])]
default chat_aperta = None
default giorno_slot = -1
default fascia_corrente = 0
default ultima_entrata = {}
default giorno_entrata = -1
default uscite = []                    # [(giorno, chiave, detto_a_josh)]
default giorno_tipo = {}               # chiave -> ultimo giorno con una chat nuova per tipo
default daniel_tace = False            # Sara lo ha ignorato: non scrive finché non lo cerca lei
default tel_scrive = None              # chi sta scrivendo, per «typing…»
default anteprime_chat = {}            # (chiave, tipo) -> (giorno, id della chat proposta)
default telefono_anteprima = False     # True: msg() non manda, ricorda solo il testo
default telefono_anteprima_testo = ""


## =============================================================================
## FLUSSO
## =============================================================================

## Inizio di una fascia: risposte arrivate e messaggi in entrata.
label telefono_fascia(nome, con_josh=False):
    $ fascia_corrente = FASCE.index(nome)
    python:
        _arrivate = [k for k, v in sorted(coda_chat.items())
                     if v["arrivo"] <= adesso() and k in contatti()]
    while _arrivate:
        $ _k = _arrivate.pop(0)
        $ _nome = nome_percorso(percorso(_k))
        if not coda_chat[_k].get("rimandata"):
            $ suono("telefono_vibra")
            n "[_nome] replied."
        else:
            n "Sara still has a reply from [_nome] to read."
        menu:
            "Read it now.":
                if con_josh and gradino(_k) >= COMPLICI:
                    $ corruption(1)
                call telefono_risposta(_k)
            "Leave it for later.":
                $ coda_chat[_k]["rimandata"] = True
    if telefono_libero:
        call telefono_entrata
    return

## Lo slot del giorno: Sara prende il telefono e scrive a qualcuno.
label telefono_slot:
    if not slot_libero() or not contatti_attivi():
        return
    $ renpy.stop_skipping()
    $ _scelta = renpy.call_screen("telefono") if not renpy.is_in_test() else _test_contatto()
    while _scelta is not None and stato_contatto(_scelta[1]) == "risposta":
        call telefono_risposta(_scelta[1])
        $ _scelta = renpy.call_screen("telefono") if not renpy.is_in_test() else _test_contatto()
    if _scelta is None or _scelta[0] == "chiudi":
        n "Sara leaves her phone face-down on the table."
        return
    $ _azione, _k = _scelta
    $ giorno_slot = giorno
    if _azione == "sollecita":
        call telefono_sollecito(_k)
    else:
        call telefono_invia(_k)
    return

## Sara scrive: riprende il discorso lasciato a metà o ne pesca uno nuovo.
label telefono_invia(k):
    $ chat_aperta = k
    show screen telefono_chat(k)
    if k in discorso_aperto:
        ## Aveva messo giù lei: il messaggio di lui è lì che aspetta.
        call telefono_continua(k)
    else:
        $ _d = renpy.random.choice(discorsi_disponibili(k))
        $ discorso_aperto[k] = {"id": _d.id, "parte": 0, "caldo": False, "frenato": False, "premio_avvio": True}
        if renpy.has_label("chat_%s" % _d.id):
            call expression "chat_%s" % _d.id
        else:
            $ msg("sara", "(Sara opens a conversation: %s. To be written.)" % _d.id)
        $ coda_chat[k] = {"arrivo": _calcola_arrivo(k), "letto": k == "daniel", "rimandata": False, "insiste": None}
        if coda_chat[k]["arrivo"] <= adesso():
            call telefono_risposta(k)
        else:
            $ renpy.pause(1.0)
    hide screen telefono_chat
    $ chat_aperta = None
    return

## Tocca all'altro: la sua risposta è arrivata.
label telefono_risposta(k):
    $ chat_aperta = k
    show screen telefono_chat(k)
    $ _insiste = coda_chat.pop(k, {}).get("insiste")
    if _insiste:
        $ msg(k, _insiste)
    if renpy.random.random() < PROBABILITA_JOSH:
        call telefono_josh_interrompe(k)
    if k in discorso_aperto:
        call telefono_continua(k)
    hide screen telefono_chat
    $ chat_aperta = None
    return

## Gli scambi di un discorso, fino alla fine o a un'interruzione (11.4).
label telefono_continua(k):
    while True:
        $ discorso_aperto[k]["parte"] += 1
        $ _id = discorso_aperto[k]["id"]
        $ _l = _parte(_id, discorso_aperto[k]["parte"])
        if _l:
            call expression _l
        else:
            $ msg(k, "(%s, exchange %d: to be written.)" % (_id, discorso_aperto[k]["parte"]))
            menu (screen="scelta_telefono"):
                "(Warm reply)":
                    $ msg("sara", "(Sara's warm reply)")
                    $ caldo()
                "(Neutral reply)":
                    $ msg("sara", "(Sara's neutral reply)")
                "(Cool it down)" if DISCORSI[_id].flirt:
                    $ msg("sara", "(Ok, stop. Goodnight.)")
                    $ frena()
        if discorso_aperto[k]["frenato"] or not _ha_parte(_id, discorso_aperto[k]["parte"] + 1):
            call telefono_fine_discorso(k)
            return
        ## Si ferma lui o lei?
        if renpy.random.random() < _prob_pausa(k):
            $ _nome = nome_percorso(percorso(k))
            n "[_nome] doesn't answer."
            $ coda_chat[k] = {"arrivo": _calcola_arrivo(k, minimo_ritardo=1), "letto": True, "rimandata": False, "insiste": None}
            return
        ## Oppure si ferma Sara.
        menu (screen="scelta_telefono"):
            "Keep chatting.":
                pass
            "Put the phone down.":
                call telefono_sara_smette(k)
                return

## Sara mette giù: ognuno reagisce a modo suo (11.4).
label telefono_sara_smette(k):
    if k == "howard":
        ## Howard le riscrive il giorno dopo, sempre.
        $ coda_chat[k] = {"arrivo": (giorno + 1) * len(FASCE), "letto": True, "rimandata": False, "insiste": "Sara? Did I say something wrong?"}
    elif k == "amica":
        $ coda_chat[k] = {"arrivo": adesso() + 1, "letto": True, "rimandata": False, "insiste": "??"}
    return

label telefono_fine_discorso(k):
    $ _a = discorso_aperto.pop(k)
    $ _d = DISCORSI[_a["id"]]
    $ discorsi_fatti.append(_d.id)
    $ segna("chat_" + _d.id)
    $ passi_chat[k] = passi_chat.get(k, 0) + 1
    if _a["frenato"]:
        $ freno[k] = giorno + GIORNI_FRENO
    else:
        python:
            _delta = 2 if _a["caldo"] else 1
            ## La chat introduttiva (l'unica da estranei) rompe il ghiaccio:
            ## dopo, Sara e l'altro sono almeno conoscenti (decisione 18/11/2026).
            if _d.gradino == ESTRANEI and not _d.argomento:
                _delta = max(_delta, SOGLIE_RAPPORTO[k][0] - percorso(k).interest)
            interest(k, _delta)
    ## Il telefono di Sara è privato (25/11/2026): niente chat da cancellare o lasciare.
    return

label telefono_josh_interrompe(k):
    $ suono("telefono_vibra")
    n "A banner slides down over the chat. [nome_compagno]."
    menu (screen="scelta_telefono"):
        "Answer [nome_compagno] first.":
            $ interest("josh", 1)
        "Leave him waiting.":
            if gradino(k) >= COMPLICI:
                $ corruption(1)
    return

label telefono_sollecito(k):
    $ chat_aperta = k
    show screen telefono_chat(k)
    $ msg("sara", "?")
    python:
        _anticipo, _int, _corr, _conf = SOLLECITI[k]
        if _anticipo:
            coda_chat[k]["arrivo"] = max(adesso(), coda_chat[k]["arrivo"] - _anticipo)
            while not _fascia_ok(k, coda_chat[k]["arrivo"]):
                coda_chat[k]["arrivo"] += 1
        if _int:
            interest(k, _int)
        if _corr:
            corruption(_corr)
        if _conf:
            confidence(_conf)
    if coda_chat[k]["arrivo"] <= adesso():
        call telefono_risposta(k)
    hide screen telefono_chat
    $ chat_aperta = None
    return

## Messaggi in entrata (10.5): lui o lei apre un discorso. Non usano lo slot.
label telefono_entrata:
    if giorno_entrata == giorno:
        return
    python:
        _candidati = [k for k in contatti()
                      if stato_contatto(k) == "nuovo"
                      and discorsi_in_entrata(k)
                      and giorno - ultima_entrata.get(k, -99) >= GIORNI_TRA_ENTRATE]
        _k = renpy.random.choice(_candidati) if _candidati and renpy.random.random() < PROBABILITA_ENTRATA else None
    if _k is None:
        return
    $ ultima_entrata[_k] = giorno
    $ giorno_entrata = giorno
    $ suono("telefono_vibra")
    $ _nome = nome_percorso(percorso(_k))
    n "A message. [_nome]."
    menu:
        "Answer.":
            $ chat_aperta = _k
            show screen telefono_chat(_k)
            $ _d = renpy.random.choice(discorsi_in_entrata(_k))
            $ discorso_aperto[_k] = {"id": _d.id, "parte": 0, "caldo": False, "frenato": False}
            if renpy.has_label("chat_%s_entrata" % _d.id):
                call expression "chat_%s_entrata" % _d.id
            call telefono_continua(_k)
            hide screen telefono_chat
            $ chat_aperta = None
        "Ignore it.":
            pass
    return

## Serata sostituibile (10.8): nel primo mese solo il giorno 22.
label serata_sostituibile:
    python:
        _opzioni = [(nome_percorso(percorso(k)), k) for k in contatti() if gradino(k) >= COMPLICI]
        _opzioni.append(("Stay home with " + nome_compagno, "josh"))
        _k = menu(_opzioni) if _opzioni[:-1] else "josh"
    if _k == "josh":
        return
    menu:
        "Tell [nome_compagno] who she's seeing.":
            $ suspicion(1)
            $ _detto = True
        "Make up an excuse.":
            $ corruption(1)
            $ segreto("uscita_%s_g%d" % (_k, giorno), "An evening out with %s." % nome_percorso(percorso(_k)), sospetto=0)
            $ _detto = False
    $ uscite.append((giorno, _k, _detto))
    if renpy.has_label("uscita_%s" % _k):
        call expression "uscita_%s" % _k
    else:
        $ _nome = nome_percorso(percorso(_k))
        n "[[Evening out with [_nome] — to be written]"
    if _detto and gradino(_k) < INTIMI:
        $ interest("josh", 1)
    return


## =============================================================================
## SCREEN
## =============================================================================

## Grafica del telefono (Jody, 25/11/2026): un telefono di fantasia coi colori del gioco.
## I pezzi si ridisegnano con tools/telefono/disegna_grafica.py.

style tel_testo is default:
    font "DejaVuSans.ttf"
    size 24
    color "#2a171e"

style tel_piccolo is tel_testo:
    size 17
    color "#8d7580"

init python:
    TEL = "images/ui/telefono/gui/"
    TEL_GIORNI = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    def tel_pezzo(nome, bordo=20):
        return Frame(TEL + nome + ".png", bordo, bordo)

    def tel_foto(k, lato):
        """La foto del contatto, o un tondo con l'iniziale (Josh e chi non ce l'ha)."""
        foto = "images/ui/telefono/%s.webp" % k
        if renpy.loadable(foto):
            return Transform(foto, xysize=(lato, lato))
        return Fixed(Transform(TEL + "foto_vuota.png", xysize=(lato, lato)),
                     Text(nome_mittente(k)[:1], style="tel_testo", size=lato // 2, color="#ffffff", align=(0.5, 0.5)),
                     xysize=(lato, lato))

    def tel_ora_barra():
        """L'ora nella barra: quella della sessione, o quella della fascia."""
        ora = store.telefono_minuti_ora
        return telefono_orario(ORARI_FASCE_TELEFONO[store.fascia_corrente] if ora is None else ora)

    def tel_ultimo(k):
        """Anteprima dell'ultimo messaggio nella rubrica."""
        log = store.chat_log.get(k)
        if not log:
            return ""
        chi, testo = log[-1][:2]
        testo = renpy.filter_text_tags(testo, allow=[])
        testo = testo if len(testo) < 34 else testo[:32].rstrip() + "…"
        return ("You: " if chi == "sara" else "") + testo.replace("[", "[[").replace("{", "{{")

    def tel_letto(k, posizione):
        """Le spunte di un messaggio di Sara: letto se l'altro ha scritto dopo."""
        log = store.chat_log.get(k, [])
        if any(m[0] == k for m in log[posizione + 1:]):
            return True
        coda = store.coda_chat.get(k)
        return bool(coda and coda["letto"]) or k == "daniel"

    def tel_altezza_scelte():
        """Quanto posto lasciare alle risposte, che stanno dentro il telefono."""
        schermo = renpy.get_screen("scelta_telefono")
        voci = (schermo.scope.get("items") or schermo.scope.get("_kwargs", {}).get("items")) if schermo else None
        return tel_altezza(voci) if voci else 0

    def tel_altezza(voci):
        h = 20
        for i in voci:
            righe = 1 + len(i.caption) // 40
            if requisiti_di(i.kwargs) and not requisiti_ok(i.kwargs):
                righe += 1
            elif scelta_acceleratore(i.kwargs):
                righe += len(avviso_acceleratore(i.kwargs))
            h += righe * 28 + 27
        return min(h, 520)

## La barra in alto, uguale in rubrica e in chat.
screen tel_testata(titolo, sotto=None, k=None):
    fixed:
        xysize (530, 126)
        add (TEL + "testa.png")
        text tel_ora_barra() style "tel_piccolo" color "#f9e9ee" xpos 42 ypos 12
        if k:
            hbox:
                xpos 14 ypos 48
                spacing 12
                add (TEL + "freccia.png") yalign 0.5
                add tel_foto(k, 58) yalign 0.5
                vbox:
                    yalign 0.5
                    xsize 260
                    text titolo style "tel_testo" color "#ffffff" size (26 if len(titolo) < 15 else 22)
                    if sotto:
                        text sotto style "tel_piccolo" color "#f0c9d5"
            hbox:
                xalign 1.0 xoffset -18 ypos 60
                spacing 18
                add (TEL + "video.png")
                add (TEL + "cornetta.png")
                add (TEL + "punti.png")
        else:
            text titolo style "tel_testo" color "#ffffff" size 34 xpos 30 ypos 58
            if sotto:
                text sotto style "tel_piccolo" color "#f0c9d5" xalign 1.0 xoffset -30 ypos 74

## La rubrica del telefono.
screen telefono():
    modal True
    zorder 150
    add Solid("#00000088")
    frame:
        at tel_sale
        xalign 0.5 yalign 0.5
        xysize (560, 1040)
        padding (15, 20)
        background (TEL + "cornice.png")
        vbox:
            if telefono_minuti_attivo():
                use tel_testata("Messages", "%d min left" % telefono_minuti_rimasti())
            else:
                use tel_testata("Messages")
            frame:
                xysize (530, 786)
                padding (0, 6)
                background Solid("#f3e8e1")
                viewport:
                    mousewheel True
                    draggable True
                    vbox:
                        xfill True
                        for k in contatti():
                            $ stato = telefono_minuti_stato(k) if telefono_minuti_attivo() else stato_contatto(k)
                            $ attesa = coda_chat.get(k)
                            $ ultimo = tel_ultimo(k)
                            button:
                                xfill True
                                ysize 104
                                padding (18, 10)
                                background None
                                hover_background Solid("#ecd5d3")
                                if stato == "risposta":
                                    action Return(("leggi", k))
                                elif stato == "attesa" and not telefono_minuti_attivo():
                                    action Return(("sollecita", k))
                                elif stato in ("nuovo", "aperto") or (stato == "attesa" and k in discorso_aperto and not chat_introduttiva_aperta(k)):
                                    action Return(("scrivi", k))
                                else:
                                    sensitive False
                                hbox:
                                    spacing 16
                                    yalign 0.5
                                    add tel_foto(k, 76) yalign 0.5
                                    vbox:
                                        xsize 330
                                        yalign 0.5
                                        spacing 2
                                        text nome_percorso(percorso(k)) style "tel_testo" size 26 color ("#2a171e" if stato != "vuoto" else "#a08a93")
                                        if ultimo:
                                            text ultimo style "tel_piccolo" size 18
                                        if stato == "risposta":
                                            text ("New message" if telefono_minuti_inbox.get(k, {}).get("entrata") else "New reply") style "tel_piccolo" color "#b0355c"
                                        elif stato == "rinviata":
                                            text ("Unread · %d min needed" % telefono_minuti_inbox[k]["bolle"]) style "tel_piccolo" color "#b0355c"
                                        elif stato == "contesto":
                                            text "Unavailable right now" style "tel_piccolo"
                                        elif stato == "attesa":
                                            text ("Read" if (attesa and attesa["letto"]) or k == "daniel" else "Delivered") style "tel_piccolo"
                                        elif stato == "aperto":
                                            text "Chat paused" style "tel_piccolo"
                                        elif stato == "vuoto":
                                            text "No new topics" style "tel_piccolo"
                                    if stato in ("risposta", "rinviata"):
                                        add (TEL + "pallino.png") yalign 0.5
                                    elif stato == "attesa" and not telefono_minuti_attivo():
                                        text "Nudge" style "tel_piccolo" yalign 0.5
                                    elif stato in ("nuovo", "aperto"):
                                        text "›" style "tel_testo" size 30 color "#a08a93" yalign 0.5
                            add Solid("#e2cfc8") xysize (410, 1) xpos 110
            fixed:
                xysize (530, 88)
                add (TEL + "piede_rubrica.png")
                hbox:
                    spacing 14
                    xalign 0.5 ypos 8
                    if telefono_minuti_attivo():
                        use tel_tasto("Wait", Return(("aspetta", None)))
                        use tel_tasto(telefono_minuti_uscita, Return(("chiudi", None)))
                    else:
                        use tel_tasto("Put the phone down", Return(("chiudi", None)))

screen tel_tasto(scritta, azione):
    textbutton scritta:
        action azione
        background tel_pezzo("risposta", 26)
        hover_background tel_pezzo("risposta_sopra", 26)
        padding (24, 14)
        text_style "tel_testo"
        text_color "#5e2136"

## Quando Sara prende il telefono, sale dal basso.
transform tel_sale:
    on show:
        yoffset 1060
        easeout 0.28 yoffset 0
    on hide:
        easein 0.2 yoffset 1060

## La chat aperta: bolle di Sara a destra, dell'altro a sinistra.
## Quando arriva un messaggio e la chat si allunga, scorre da sola all'ultimo
## (yinitial vale solo all'apertura: lo schermo resta mostrato mentre cresce).
init python:
    def _chat_in_fondo(adj):
        adj.value = adj.range
    tel_scorrimento = ui.adjustment(ranged=_chat_in_fondo)

screen telefono_chat(k):
    zorder 40
    $ log = chat_log.get(k, [])
    $ inizio = max(0, len(log) - 30)
    $ scelte_h = tel_altezza_scelte()
    frame:
        xpos 1330 yalign 0.5
        xysize (560, 1040)
        padding (15, 20)
        background (TEL + "cornice.png")
        vbox:
            use tel_testata(nome_mittente(k), "typing…" if tel_scrive == k else ("online" if telefono_minuti_attivo() and _telefono_orario_adatto(k, telefono_minuti_ora) else None), k)
            frame:
                xysize (530, 786)
                padding (14, 10, 14, 6)
                background Solid("#f3e8e1")
                viewport:
                    ysize (770 - scelte_h)
                    yinitial 1.0
                    yadjustment tel_scorrimento
                    mousewheel True
                    vbox:
                        spacing 8
                        xfill True
                        $ giorno_prima = None
                        for n_msg, messaggio in enumerate(log[inizio:]):
                            $ chi, testo = messaggio[:2]
                            $ immagine = messaggio[2] if len(messaggio) > 2 else None
                            $ minuto = messaggio[3] if len(messaggio) > 3 else None
                            $ giorno_msg = messaggio[4] if len(messaggio) > 4 else None
                            if giorno_msg is not None and giorno_msg != giorno_prima:
                                $ giorno_prima = giorno_msg
                                frame:
                                    xalign 0.5
                                    padding (16, 5)
                                    background tel_pezzo("etichetta", 13)
                                    text ("Today" if giorno_msg == giorno else TEL_GIORNI[(giorno_msg - 1) % 7]) style "tel_piccolo"
                            frame:
                                xalign (1.0 if chi == "sara" else 0.0)
                                xmaximum 410
                                padding (16, 9, 16, 7)
                                background tel_pezzo("bolla_sara" if chi == "sara" else "bolla_altro")
                                vbox:
                                    spacing 2
                                    if chi == "josh" and k != "josh":
                                        text nome_mittente(chi) style "tel_piccolo" color "#3f6fa8"
                                    if immagine and renpy.loadable(immagine):
                                        add Transform(immagine, xysize=(364, 208), fit="contain")
                                    text testo style "tel_testo"
                                    if minuto is not None or chi == "sara":
                                        hbox:
                                            xalign 1.0
                                            spacing 6
                                            if minuto is not None:
                                                text telefono_orario(minuto) style "tel_piccolo" size 15
                                            if chi == "sara":
                                                add (TEL + ("spunte_lette.png" if tel_letto(k, inizio + n_msg) else "spunte.png")) yalign 0.5
            add (TEL + "piede.png")

## Le scelte dentro una chat: risposte nel telefono, sopra la barra.
screen scelta_telefono(items):
    zorder 60
    frame:
        xpos 1345 ypos 952 yanchor 1.0
        xysize (530, tel_altezza(items))
        padding (12, 10, 12, 4)
        background Solid("#f8f0eb")
        viewport:
            mousewheel True
            draggable True
            vbox:
                spacing 8
                xfill True
                for i in items:
                    ## Risposte con requisito: in grigio, con il requisito sotto (come nelle scene).
                    if requisiti_di(i.kwargs) and not requisiti_ok(i.kwargs):
                        frame:
                            xfill True
                            background tel_pezzo("risposta_no", 26)
                            padding (20, 10)
                            vbox:
                                text i.caption style "tel_testo" size 22 color "#a08a93"
                                text "Requires " + testo_requisiti(i.kwargs) style "tel_piccolo" color "#b0355c"
                    elif scelta_acceleratore(i.kwargs):
                        button:
                            xfill True
                            action i.action
                            background tel_pezzo("risposta_ambra", 26)
                            hover_background tel_pezzo("risposta_ambra_sopra", 26)
                            padding (20, 10)
                            vbox:
                                text "!!! " + i.caption + " !!!" style "tel_testo" size 22 color "#8a4d00"
                                for riga in avviso_acceleratore(i.kwargs):
                                    text riga style "tel_piccolo" color "#8a4d00"
                    else:
                        $ tipo = tipo_chat_aperta()
                        textbutton (("(%s) " % tipo if tipo and i.caption.startswith("«") else "") + i.caption):
                            xfill True
                            action i.action
                            background tel_pezzo("risposta", 26)
                            hover_background tel_pezzo("risposta_sopra", 26)
                            padding (20, 10)
                            text_style "tel_testo"
                            text_size 22
                            text_color "#5e2136"


## =============================================================================
## PROVA DEL TELEFONO (solo per gli sviluppatori e per i test)
## =============================================================================
## Simula i giorni 14-22 con i discorsi segnaposto. Dalla console: jump telefono_prova
label telefono_prova:
    python:
        telefono_libero = False
        telefono_segnaposto = True
        rubrica = ["amica", "amico"]
        passi_chat = {}
        discorsi_fatti = []
        discorso_aperto = {}
        coda_chat = {}
        freno = {}
        chat_lasciate = []
        chat_log = {}
        giorno_slot = -1
        ultima_entrata = {}
        giorno_entrata = -1
        uscite = []
        for _p in percorsi.values():
            _p.interest = 0
    $ giorno = 13
    python:
        for _c in ("simon", "howard", "daniel", "editore", "capa", "ex"):
            da_numero(_c)
    $ giorno = 14
    $ sblocca_telefono()
    while giorno <= 22:
        $ fascia_corrente = 0
        call telefono_fascia("lavoro")
        call telefono_fascia("pranzo")
        call telefono_slot
        call telefono_fascia("sera", con_josh=True)
        call telefono_fascia("notte")
        if giorno == 22:
            call serata_sostituibile
        $ giorno += 1
    python:
        _foto_telefono.clear()
        _foto_telefono.update({"libero": telefono_libero, "rubrica": list(rubrica), "passi": dict(passi_chat),
            "fatti": list(discorsi_fatti), "aperti": dict(discorso_aperto),
            "interest": {k: percorsi[k].interest for k in rubrica}, "coda": dict(coda_chat),
            "lasciate": list(chat_lasciate), "uscite": list(uscite)})
    $ telefono_segnaposto = False
    jump telefono_prova_fine

label telefono_prova_fine:
    return

init python:
    _foto_telefono = {}
