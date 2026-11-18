## =============================================================================
## TELEFONO — rubrica, slot del giorno, risposte asincrone, serate alternative
## =============================================================================
## Specifica: docs/telefono-e-percorsi-dinamici.md, sezione 10 (decisioni 18/11/2026).
##
## Come si usa nel codice delle giornate:
##   $ da_numero("simon")                  Sara ottiene il numero (entra in rubrica)
##   $ sblocca_telefono()                  giorno 14, la cucina con Sally
##   call telefono_fascia("sera")          inizio di una fascia: arrivano risposte
##   call telefono_fascia("sera", con_josh=True)   ...mentre Sara è con Josh
##   call telefono_slot                    Sara può prendere il telefono (lo slot del giorno)
##   call serata_sostituibile              giorno 22: uscita con un contatto a C+ o Josh
##   if gradino("daniel") >= C:            varianti delle scene fisse
##
## Come si scrive un percorso (un file per percorso, es. game/percorsi/chat_daniel.rpy):
##   label chat_daniel_1:            il messaggio di Sara (step 1)
##   label chat_daniel_1_risposta:   la risposta di lui + la risposta di Sara,
##                                   che finisce con $ chat_fine("daniel", caldo=True/False)
##   label chat_daniel_entrata:      un messaggio in entrata (scrive lui per primo)
##   label uscita_daniel:            la serata alternativa
## Dentro le chat:  $ msg("sara", "...")  /  $ msg("daniel", "...")
## Se un label manca, il gioco usa un segnaposto: si può giocare tutto anche prima
## che i testi siano scritti.

## Gradini del rapporto (Interest con quattro soglie per personaggio).
define ESTRANEI = 0
define CONOSCENTI = 1
define CONFIDENZA = 2
define COMPLICI = 3
define INTIMI = 4

init -5 python:

    FASCE = ["mattina", "lavoro", "pranzo", "sera", "notte"]
    NOMI_FASCE = {"mattina": "Morning", "lavoro": "Work", "pranzo": "Lunch break",
                  "sera": "Evening", "notte": "Night"}

    ## Soglie A, B, C, D per percorso (10.3).
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
        "amica":   (0, 0, None, False),            # subito
        "howard":  (0, 0, None, False),            # subito, sempre
        "simon":   (0, 1, ("sera", "notte"), False),  # la sera stessa
        "amico":   (0, 1, None, False),            # in fretta
        "ex":      (0, 1, ("notte",), False),      # di notte
        "daniel":  (1, 5, None, False),            # da una fascia a un giorno
        "editore": (5, 10, None, False),           # 1-2 giorni
        "capa":    (1, 5, ("lavoro", "pranzo"), True),  # solo in orario di lavoro
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

    ## Ogni quanto qualcuno può scrivere per primo, e con che probabilità a fascia.
    GIORNI_TRA_ENTRATE = 3
    PROBABILITA_ENTRATA = 0.35
    ## Probabilità che Josh scriva mentre Sara chatta con un altro.
    PROBABILITA_JOSH = 0.25

    def gradino(chiave):
        """0 estranei · 1 conoscenti · 2 in confidenza · 3 complici · 4 intimi."""
        valore = percorso(chiave).interest
        return sum(1 for s in SOGLIE_RAPPORTO[chiave] if valore >= s)

    def adesso():
        return store.giorno * len(FASCE) + store.fascia_corrente

    def _giorno_lavorativo(istante):
        g = istante // len(FASCE)
        return (g - 1) % 7 < 5

    def _fascia_ok(chiave, istante):
        _, _, fasce, lavorativi = RITARDI[chiave]
        if fasce and FASCE[istante % len(FASCE)] not in fasce:
            return False
        if lavorativi and not _giorno_lavorativo(istante):
            return False
        return True

    def _calcola_arrivo(chiave):
        """Quando arriva la risposta: deciso all'invio e salvato (niente ricarica e riprova)."""
        minimo, massimo, _, _ = RITARDI[chiave]
        ritardo = renpy.random.randint(minimo, massimo)
        g = gradino(chiave)
        if g >= INTIMI:
            ritardo = 0
        elif g >= COMPLICI:
            ritardo = max(0, ritardo - 1)
        arrivo = adesso() + ritardo
        while not _fascia_ok(chiave, arrivo):
            arrivo += 1
        return arrivo

    ## --- Rubrica e sblocco ----------------------------------------------------

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
        """Contatti in rubrica con cui si può ancora parlare."""
        return [k for k in store.rubrica if not percorso(k).chiuso]

    def step_chat(chiave):
        """Ultimo step completato con quel contatto (0 = mai scritto)."""
        return store.passi_chat.get(chiave, 0)

    def in_attesa(chiave):
        return chiave in store.coda_chat

    def slot_libero():
        return store.telefono_libero and store.giorno_slot != store.giorno

    def _usa_slot():
        store.giorno_slot = store.giorno

    ## --- Messaggi a schermo ------------------------------------------------------

    def msg(chi, testo):
        """Un messaggio nella chat aperta. chi = "sara", "josh" o la chiave del contatto."""
        chiave = store.chat_aperta
        store.chat_log.setdefault(chiave, []).append((chi, testo))
        renpy.restart_interaction()
        renpy.pause()

    def nome_mittente(chi):
        if chi == "sara":
            return "Sara"
        if chi == "josh":
            return store.nome_compagno
        return nome_percorso(percorso(chi))

    ## --- Fine di uno step --------------------------------------------------------

    def chat_fine(chiave, caldo=False):
        """Sara ha risposto alla risposta: lo step è completo."""
        store.passi_chat[chiave] = step_chat(chiave) + 1
        store.coda_chat.pop(chiave, None)
        interest(chiave, 2 if caldo else 1)

    def _label_o_none(nome):
        return nome if renpy.has_label(nome) else None


## Stato del telefono (tutto con default: i vecchi salvataggi restano validi).
default telefono_libero = False
default rubrica = ["amica", "amico"]   # Joanie e Darius da subito (10.2)
default passi_chat = {}                # chiave -> ultimo step completato
default coda_chat = {}                 # chiave -> {"arrivo", "inviato", "letto", "rimandata"}
default chat_log = {}                  # chiave -> [(mittente, testo)]
default chat_aperta = None
default giorno_slot = -1               # il giorno in cui Sara ha usato lo slot
default fascia_corrente = 0
default ultima_entrata = {}            # chiave -> giorno dell'ultimo messaggio in entrata
default giorno_entrata = -1            # mai due messaggi in entrata nello stesso giorno
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
            n "Sara's phone lights up on the table. [_nome] has replied."
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
        call telefono_entrata(con_josh)
    return

## Lo slot del giorno: Sara può prendere il telefono e scrivere a qualcuno.
label telefono_slot:
    if not slot_libero() or not contatti():
        return
    $ _scelta = renpy.call_screen("telefono") if not renpy.is_in_test() else _test_contatto()
    if _scelta is None:
        n "Sara leaves her phone face-down on the table."
        return
    $ _azione, _k = _scelta
    $ _usa_slot()
    if _azione == "sollecita":
        call telefono_sollecito(_k)
    else:
        call telefono_invia(_k)
    return

label telefono_invia(k):
    $ chat_aperta = k
    show screen telefono_chat(k)
    $ _l = _label_o_none("chat_%s_%d" % (k, step_chat(k) + 1))
    if _l:
        call expression _l
    else:
        $ msg("sara", "(Step %d with %s: Sara's message, to be written)" % (step_chat(k) + 1, nome_percorso(percorso(k))))
    $ coda_chat[k] = {"arrivo": _calcola_arrivo(k), "inviato": adesso(), "letto": False, "rimandata": False}
    ## Daniel legge subito e la fa aspettare: si vede la doppia spunta.
    if k == "daniel":
        $ coda_chat[k]["letto"] = True
    if coda_chat[k]["arrivo"] <= adesso():
        call telefono_risposta(k)
    else:
        $ renpy.pause(1.0)
    hide screen telefono_chat
    $ chat_aperta = None
    return

label telefono_risposta(k):
    $ chat_aperta = k
    show screen telefono_chat(k)
    $ coda_chat[k]["letto"] = True
    ## Josh può scrivere mentre Sara chatta con un altro (10.5).
    if renpy.random.random() < PROBABILITA_JOSH:
        call telefono_josh_interrompe(k)
    $ _l = _label_o_none("chat_%s_%d_risposta" % (k, step_chat(k) + 1))
    if _l:
        call expression _l
    else:
        $ msg(k, "(Step %d: %s's reply, to be written)" % (step_chat(k) + 1, nome_percorso(percorso(k))))
        menu (screen="scelta_telefono"):
            "[[Warm reply]":
                $ msg("sara", "(Sara's warm reply)")
                $ chat_fine(k, caldo=True)
            "[[Neutral reply]":
                $ msg("sara", "(Sara's neutral reply)")
                $ chat_fine(k)
    ## Se il label scritto a mano ha dimenticato chat_fine, chiudiamo noi lo step.
    if k in coda_chat:
        $ chat_fine(k)
    hide screen telefono_chat
    $ chat_aperta = None
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

## Messaggi in entrata: da B in su, uno ogni 3-4 giorni per contatto, mai due nello
## stesso giorno; Daniel scrive per primo già dal numero (10.5). Non usano lo slot.
label telefono_entrata(con_josh=False):
    if giorno_entrata == giorno:
        return
    python:
        _candidati = [k for k in contatti()
                      if not in_attesa(k)
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
            $ _l = _label_o_none("chat_%s_entrata" % _k)
            if _l:
                call expression _l
            else:
                $ msg(_k, "(%s writes first, to be written)" % nome_percorso(percorso(_k)))
                $ msg("sara", "(Sara answers)")
            $ interest(_k, 1)
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
    $ _l = _label_o_none("uscita_%s" % _k)
    if _l:
        call expression _l
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

## La rubrica: chi c'è, chi deve rispondere, chi ha letto.
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
                        $ attesa = coda_chat.get(k)
                        frame:
                            xfill True
                            padding (20, 14)
                            background Solid("#2b1d25")
                            hbox:
                                xfill True
                                vbox:
                                    text nome_percorso(percorso(k)) style "tel_testo" size 34
                                    if attesa and attesa["letto"]:
                                        text "Read. No reply yet." style "tel_testo" size 24 color "#c9a3a0"
                                    elif attesa:
                                        text "Delivered." style "tel_testo" size 24 color "#c9a3a0"
                                    elif step_chat(k) == 0:
                                        text "No messages yet." style "tel_testo" size 24 color "#c9a3a0"
                                if attesa:
                                    textbutton "Nudge" xalign 1.0 yalign 0.5 action Return(("sollecita", k))
                                else:
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
## Simula i giorni 14-22: sblocco, numeri, una fascia di lavoro e una sera con
## Josh al giorno, lo slot, e la serata sostituibile del 22.
label telefono_prova:
    ## Si riparte da zero ogni volta (i casi di test condividono lo stato).
    python:
        telefono_libero = False
        rubrica = ["amica", "amico"]
        passi_chat = {}
        coda_chat = {}
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
    ## Fotografia dello stato per i test (letta dopo che il gioco torna al menu).
    $ telefono_ultima_prova = {"libero": telefono_libero, "rubrica": list(rubrica), "passi": dict(passi_chat), "interest": {k: percorsi[k].interest for k in rubrica}, "coda": dict(coda_chat), "uscite": list(uscite)}
    $ renpy.store._foto_telefono.clear()
    $ renpy.store._foto_telefono.update(telefono_ultima_prova)
    jump telefono_prova_fine

label telefono_prova_fine:
    return

init python:
    _foto_telefono = {}
