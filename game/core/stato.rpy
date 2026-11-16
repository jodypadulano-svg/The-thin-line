## =============================================================================
## STATO DEL GIOCO — The Thin Line
## =============================================================================
## Tutto ciò che il gioco ricorda delle scelte del giocatore.
## Variabili decise con Jody (docs/decisioni.md, A5-A10):
##   Corruption  — sale con ogni scelta «sbagliata» a favore di un percorso;
##                 apre le scene oltre la soglia di ciascun percorso.
##   Interest    — 9 valori: uno per percorso + uno per Josh. Possono scendere.
##   Suspicion   — il sospetto di Josh: bugie, segreti, rischi con lui vicino.
##   Confidence  — la fiducia in sé di Sara: frasi coraggiose e abiti.
##
## Regole per non rompere i salvataggi tra un episodio e l'altro:
##  - ogni nuova variabile si dichiara con `default`, mai con `$` a inizio partita;
##  - un nuovo attributo di Percorso si aggiunge come attributo di CLASSE;
##  - non rinominare mai una chiave già usata in `fatti`, `percorsi`, `segreti`.

init -10 python:

    def _limita(valore, minimo=0, massimo=100):
        return max(minimo, min(massimo, valore))

    ## Soglie di Corruption per le scene «spinte» di ogni percorso (A7).
    SOGLIA_CORRUPTION = {
        "simon": 15, "ex": 25, "amico": 35, "daniel": 45,
        "amica": 55, "editore": 65, "howard": 75, "capa": 85,
    }

    ## Sotto questo Interest verso Josh, Sara non riesce più a fare gesti carini
    ## verso di lui (A6). Valore provvisorio.
    SOGLIA_GENTILE_CON_JOSH = 30

    ## Colori delle notifiche e dei nomi.
    COLORI = {
        "josh": "#8fb3e0", "simon": "#7fd1a8", "daniel": "#c9a0ff",
        "howard": "#b5a48a", "editore": "#d4b483", "amica": "#f0c674",
        "ex": "#e0a07f", "amico": "#9fd0e0", "capa": "#e07fb0",
        "corruption": "#ff5c7a", "confidence": "#ffd36b", "suspicion": "#ff9f43",
    }

    class Percorso(object):
        """Un percorso relazionale opzionale (uno degli otto archetipi).

        interest: 0-100, interesse di Sara verso di lui/lei (Interest toward XXX).
        tappa:    contatore interno dello slow burn (0 = non iniziato).
        chiuso:   True se Sara ha chiuso la porta: niente più scene del percorso.
        """

        interest = 0
        tappa = 0
        chiuso = False
        incontrato = False

        def __init__(self, chiave, nome, ruolo):
            self.chiave = chiave
            self.nome = nome
            self.ruolo = ruolo
            self.sa_sara = []   # ciò che Sara pensa di lui (frasi brevi)
            self.sai_tu = []    # retroscena che solo il giocatore conosce

        @property
        def aperto(self):
            return self.incontrato and not self.chiuso

        @property
        def soglia(self):
            return SOGLIA_CORRUPTION.get(self.chiave, 0)

    # Testi delle tappe mostrati nel Diario.
    TAPPE = {
        "simon":  ["Ancora uno sconosciuto.", "Il personal trainer della palestra.", "Un istruttore gentile che si ricorda di lei."],
        "daniel": ["Ancora uno sconosciuto.", "Il capo arrogante del compagno.", "Forse non è solo arroganza."],
        "howard": ["Ancora uno sconosciuto.", "Il vicino un po' strano.", "Un uomo solo che le fa tenerezza."],
        "editore": ["Ancora uno sconosciuto.", "Un editore che ha ascoltato il suo sogno."],
    }

    NOMI_VARIABILI = {
        "corruption": "Corruption",
        "confidence": "Confidence",
        "suspicion": "Suspicion",
    }

    ## Le variabili nello store si chiamano sara_corruption, sara_confidence,
    ## josh_suspicion: i nomi brevi sono riservati alle funzioni.
    VARIABILE_STORE = {
        "corruption": "sara_corruption",
        "confidence": "sara_confidence",
        "suspicion": "josh_suspicion",
    }

    def percorso(chiave):
        return store.percorsi[chiave]

    def nome_interest(chiave):
        if chiave == "josh":
            return store.nome_compagno
        return percorso(chiave).nome

    ## --- Interest -----------------------------------------------------------

    def interest(chiave, delta, motivo=None):
        """Interest di Sara verso un percorso o verso Josh ("josh")."""
        if delta == 0:
            return
        if chiave == "josh":
            store.interest_josh = _limita(store.interest_josh + delta)
        else:
            p = percorso(chiave)
            if p.chiuso:
                return
            p.interest = _limita(p.interest + delta)
        _annuncia("Interest " + nome_interest(chiave), delta, COLORI.get(chiave, "#ffffff"), motivo)

    def valore_interest(chiave):
        if chiave == "josh":
            return store.interest_josh
        return percorso(chiave).interest

    def gentile_con_josh():
        """Sara riesce ancora a fare gesti carini verso Josh?"""
        return store.interest_josh >= SOGLIA_GENTILE_CON_JOSH

    ## --- Variabili di Sara ---------------------------------------------------

    def _variabile(nome, delta, motivo):
        if delta == 0:
            return
        campo = VARIABILE_STORE[nome]
        setattr(store, campo, _limita(getattr(store, campo) + delta))
        _annuncia(NOMI_VARIABILI[nome], delta, COLORI[nome], motivo)

    def corruption(delta, motivo=None):
        _variabile("corruption", delta, motivo)

    def confidence(delta, motivo=None):
        _variabile("confidence", delta, motivo)

    def suspicion(delta, motivo=None):
        _variabile("suspicion", delta, motivo)

    def oltre_soglia(chiave):
        """True se la Corruption di Sara basta per le scene «spinte» del percorso."""
        return store.sara_corruption >= SOGLIA_CORRUPTION[chiave]

    ## --- Requisiti delle frasi (A3) ------------------------------------------
    ## Nel menu:   "Testo della frase" (corruption=15):
    ##             "Testo" (confidence=25, simon=10):
    ## Chiavi: corruption, confidence, suspicion, josh, oppure la chiave di un
    ## percorso (= Interest verso di lui). Se il requisito non è soddisfatto la
    ## frase resta visibile in grigio con il requisito accanto (screen choice).

    def _valore_requisito(chiave):
        if chiave in NOMI_VARIABILI:
            return getattr(store, VARIABILE_STORE[chiave])
        return valore_interest(chiave)

    def _nome_requisito(chiave):
        if chiave in NOMI_VARIABILI:
            return NOMI_VARIABILI[chiave]
        return "Interest " + nome_interest(chiave)

    def requisiti_ok(requisiti):
        return all(_valore_requisito(k) >= v for k, v in requisiti.items())

    def testo_requisiti(requisiti):
        return " · ".join("{} {}".format(_nome_requisito(k), v) for k, v in requisiti.items())

    ## --- Percorsi, Diario, segreti, fatti ---------------------------------------

    def incontra(chiave):
        """Primo incontro: da qui il personaggio compare nel Diario."""
        p = percorso(chiave)
        if not p.incontrato:
            p.incontrato = True
            _annuncia_testo("Diario: nuova pagina — {}".format(p.nome))

    def tappa(chiave, nuova):
        """Porta un percorso alla tappa indicata (mai indietro)."""
        p = percorso(chiave)
        if not p.chiuso and nuova > p.tappa:
            p.tappa = nuova

    def chiudi(chiave):
        p = percorso(chiave)
        if not p.chiuso:
            p.chiuso = True
            _annuncia_testo("Sara ha chiuso la porta a {}.".format(p.nome))

    def nota_sara(chiave, testo):
        """Ciò che Sara pensa o crede: pagina 'Cosa sa Sara' del Diario."""
        p = percorso(chiave)
        if testo not in p.sa_sara:
            p.sa_sara.append(testo)

    def retroscena(chiave, testo):
        """Ciò che il giocatore ha visto e Sara no: pagina 'Cosa sai tu'."""
        p = percorso(chiave)
        if testo not in p.sai_tu:
            p.sai_tu.append(testo)
            _annuncia_testo("Diario: retroscena su {}".format(p.nome))

    def segreto(chiave, descrizione, sospetto=3):
        """Qualcosa che Sara tiene nascosto a Josh. Nasconderlo alza la Suspicion."""
        if chiave not in store.segreti:
            store.segreti[chiave] = descrizione
            _annuncia_testo("Sara ha un segreto.")
            suspicion(sospetto)

    def segna(chiave, valore=True):
        """Ricorda un fatto o una scelta (es. 'ep1_palestra_da_sola')."""
        store.fatti[chiave] = valore

    def fatto(chiave):
        return store.fatti.get(chiave, False)


## Preferenze del giocatore (valgono per tutte le partite). A2: tutto visibile
## di default; dalle Opzioni si può nascondere.
default persistent.effetti_visibili = True
default persistent.numeri_visibili = True

## Nome del compagno: lo sceglie il giocatore all'inizio.
default nome_compagno = "Josh"

## Sara.
default sara_corruption = 0
default sara_confidence = 20       # una sognatrice che non crede abbastanza in sé
default josh_suspicion = 0
default interest_josh = 80    # parte da una coppia felice

## Percorsi. I quattro senza scheda esistono già per non rompere i salvataggi.
default percorsi = {
    "daniel":  Percorso("daniel", "Daniel", "Il capo del compagno"),
    "simon":   Percorso("simon", "Simon", "Il personal trainer"),
    "howard":  Percorso("howard", "Howard", "Il vicino di casa"),
    "editore": Percorso("editore", "L'editore", "L'uomo ricco e di successo"),
    ## Joanie: percorso 5, il lato sentimentale emerge molto più avanti.
    ## Non chiamare incontra("amica") finché il percorso non si apre.
    "amica":   Percorso("amica", "Joanie", "La migliore amica"),
    "ex":      Percorso("ex", "L'ex", "L'ex fidanzato"),
    "amico":   Percorso("amico", "L'amico", "Il migliore amico del compagno"),
    "capa":    Percorso("capa", "La capa", "La responsabile dell'ufficio"),
}

## Segreti di Sara: chiave -> descrizione.
default segreti = {}

## Fatti e scelte puntuali.
default fatti = {}

## Calendario della storia (lineare, niente grind).
default giorno = 0
default episodio = 1
