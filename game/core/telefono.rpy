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

    SOGLIE_RAPPORTO = {
        "simon":   (5, 10, 16, 22),
        "howard":  (4, 9, 14, 20),
        "daniel":  (3, 7, 12, 18),
        "editore": (3, 7, 12, 18),
        "ex":      (3, 7, 12, 18),
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
        def __init__(self, id, chiave, gradino, se, flirt, prova):
            self.id = id
            self.chiave = chiave
            self.gradino = gradino
            self.se = se
            self.flirt = flirt
            self.prova = prova

    DISCORSI = {}

    def discorso(id, chiave, gradino=CONOSCENTI, se=None, flirt=False, prova=False):
        """Registra un discorso. se = condizione come testo, es. "fatto('ep1_festa')"."""
        DISCORSI[id] = Discorso(id, chiave, gradino, se, flirt, prova)

    ## Discorsi segnaposto per la prova degli sviluppatori (non escono nel gioco vero).
    _SEGNAPOSTO = {ESTRANEI: 2, CONOSCENTI: 3, CONFIDENZA: 2, COMPLICI: 2, INTIMI: 1}
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

    def discorso_disponibile(d):
        k = d.chiave
        if d.id in store.discorsi_fatti:
            return False
        if d.prova and not store.telefono_segnaposto:
            return False
        if gradino(k) < d.gradino:
            return False
        if d.flirt and store.freno.get(k, -99) > store.giorno:
            return False
        if d.se and not eval(d.se):
            return False
        return True

    def discorsi_disponibili(chiave):
        return [d for _, d in sorted(DISCORSI.items()) if d.chiave == chiave and discorso_disponibile(d)]

    def _parte(id, n):
        nome = "chat_%s_%d" % (id, n)
        return nome if renpy.has_label(nome) else None

    def _ha_parte(id, n):
        return _parte(id, n) is not None or (DISCORSI[id].prova and n <= 2)

    def caldo():
        """Nel discorso Sara ha scelto una risposta calda: +2 Interest alla fine."""
        store.discorso_aperto[store.chat_aperta]["caldo"] = True

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
        """attesa: tocca all'altro · aperto: Sara ha messo giù · nuovo: c'è un discorso · vuoto."""
        if k in store.coda_chat:
            return "attesa"
        if k in store.discorso_aperto:
            return "aperto"
        if discorsi_disponibili(k):
            return "nuovo"
        return "vuoto"

    def contatti_attivi():
        return [k for k in contatti() if stato_contatto(k) != "vuoto"]

    def in_attesa(chiave):
        return chiave in store.coda_chat

    def slot_libero():
        return store.telefono_libero and store.giorno_slot != store.giorno

    def chat_compromettenti():
        """Discorsi «complici» o «intimi» lasciati sul telefono: Josh può trovarli."""
        return list(store.chat_lasciate)

    ## --- Messaggi a schermo ---------------------------------------------------------

    def msg(chi, testo):
        """Un messaggio nella chat aperta. chi = "sara", "josh" o la chiave del contatto."""
        store.chat_log.setdefault(store.chat_aperta, []).append((chi, testo))
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
default chat_lasciate = []             # id dei discorsi compromettenti non cancellati
default chat_log = {}                  # chiave -> [(mittente, testo)]
default chat_aperta = None
default giorno_slot = -1
default fascia_corrente = 0
default ultima_entrata = {}
default giorno_entrata = -1
default uscite = []                    # [(giorno, chiave, detto_a_josh)]


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
        if con_josh and not coda_chat[_k].get("rimandata"):
            $ suono("telefono_vibra")
            $ _nome = nome_percorso(percorso(_k))
            n "Sara's phone lights up on the table. [_nome]."
            menu:
                "Read it now.":
                    $ suspicion(1)
                    if gradino(_k) >= COMPLICI:
                        $ corruption(1)
                    call telefono_risposta(_k)
                "Leave it for later.":
                    $ coda_chat[_k]["rimandata"] = True
                    $ coda_chat[_k]["arrivo"] = adesso() + 1
        else:
            $ suono("telefono_vibra")
            call telefono_risposta(_k)
    if telefono_libero:
        call telefono_entrata
    return

## Lo slot del giorno: Sara prende il telefono e scrive a qualcuno.
label telefono_slot:
    if not slot_libero() or not contatti_attivi():
        return
    $ _scelta = renpy.call_screen("telefono") if not renpy.is_in_test() else _test_contatto()
    if _scelta is None:
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
        $ discorso_aperto[k] = {"id": _d.id, "parte": 0, "caldo": False, "frenato": False}
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
        $ interest(k, 2 if _a["caldo"] else 1)
    ## Le chat compromettenti: cancellarle o lasciarle (11.5).
    if _d.gradino >= COMPLICI and not _a["frenato"]:
        menu (screen="scelta_telefono"):
            "Delete the chat.":
                $ corruption(1)
                $ suspicion(-1)
                $ chat_log[k] = []
            "Keep it.":
                $ chat_lasciate.append(_d.id)
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
                      and (gradino(k) >= CONFIDENZA or (k == "daniel" and "daniel" not in ultima_entrata))
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
            $ _d = renpy.random.choice(discorsi_disponibili(_k))
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

style tel_testo is default:
    font gui.interface_text_font
    size 30
    color "#f3e6ea"

## La rubrica.
screen telefono():
    modal True
    zorder 150
    add Solid("#00000088")
    frame:
        xalign 0.5 yalign 0.5
        xysize (560, 940)
        padding (34, 40)
        background Solid("#1b1117")
        vbox:
            spacing 18
            text "Messages" style "tel_testo" size 44 color "#ffb3c1"
            text "One message today. Who will she write to?" style "tel_testo" size 26 color "#c9a3a0"
            null height 10
            viewport:
                ysize 640
                scrollbars "vertical"
                mousewheel True
                vbox:
                    spacing 12
                    for k in contatti():
                        $ stato = stato_contatto(k)
                        $ attesa = coda_chat.get(k)
                        frame:
                            xfill True
                            padding (20, 14)
                            background Solid("#2b1d25" if stato != "vuoto" else "#1f171c")
                            hbox:
                                xfill True
                                vbox:
                                    text nome_percorso(percorso(k)) style "tel_testo" size 34 color ("#f3e6ea" if stato != "vuoto" else "#7d6870")
                                    if stato == "attesa" and attesa["letto"]:
                                        text "Read. No reply yet." style "tel_testo" size 24 color "#c9a3a0"
                                    elif stato == "attesa":
                                        text "Delivered." style "tel_testo" size 24 color "#c9a3a0"
                                    elif stato == "aperto":
                                        text "You left the conversation hanging." style "tel_testo" size 24 color "#c9a3a0"
                                    elif stato == "vuoto":
                                        text "Nothing new to say... yet." style "tel_testo" size 24 color "#7d6870"
                                if stato == "attesa":
                                    textbutton "Nudge" xalign 1.0 yalign 0.5 action Return(("sollecita", k))
                                elif stato != "vuoto":
                                    textbutton "Write" xalign 1.0 yalign 0.5 action Return(("scrivi", k))
            textbutton "Put the phone down" xalign 0.5 action Return(None)

## La chat aperta: bolle di Sara a destra, dell'altro a sinistra.
screen telefono_chat(k):
    zorder 40
    frame:
        xpos 1330 yalign 0.5
        xysize (540, 960)
        padding (26, 30)
        background Solid("#1b1117f2")
        vbox:
            spacing 14
            text nome_percorso(percorso(k)) style "tel_testo" size 38 color "#ffb3c1" xalign 0.5
            viewport:
                ysize 800
                yinitial 1.0
                mousewheel True
                vbox:
                    spacing 10
                    xfill True
                    for chi, testo in chat_log.get(k, [])[-30:]:
                        if chi == "sara":
                            frame:
                                xalign 1.0
                                xmaximum 400
                                padding (18, 10)
                                background Solid("#7a2e45")
                                text testo style "tel_testo" size 28
                        else:
                            frame:
                                xalign 0.0
                                xmaximum 400
                                padding (18, 10)
                                background Solid("#352a31")
                                vbox:
                                    if chi == "josh":
                                        text nome_mittente(chi) style "tel_testo" size 20 color "#8fb3e0"
                                    text testo style "tel_testo" size 28
            $ attesa = coda_chat.get(k)
            if attesa and attesa["letto"]:
                text "Read" style "tel_testo" size 22 color "#c9a3a0" xalign 1.0
            elif attesa:
                text "Delivered" style "tel_testo" size 22 color "#c9a3a0" xalign 1.0

## Le scelte dentro una chat: accanto al telefono, non sopra.
screen scelta_telefono(items):
    zorder 60
    vbox:
        xpos 1300 xanchor 1.0 yalign 0.7
        spacing 14
        for i in items:
            textbutton i.caption:
                action i.action
                background Solid("#2b1d25ee")
                hover_background Solid("#7a2e45ee")
                padding (26, 14)
                xminimum 520
                text_style "tel_testo"


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
