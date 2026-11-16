## =============================================================================
## STATO DEL GIOCO — The Thin Line
## =============================================================================
## Tutto ciò che il gioco ricorda delle scelte del giocatore.
##
## Regole per non rompere i salvataggi tra un episodio e l'altro:
##  - ogni nuova variabile si dichiara con `default`, mai con `$` a inizio partita;
##  - un nuovo attributo di Percorso si aggiunge come attributo di CLASSE
##    (i vecchi salvataggi lo leggono dal valore di classe);
##  - non rinominare mai una chiave già usata in `fatti` o in `percorsi`.
## Vedi docs/sistema-di-gioco.md.

init -10 python:

    def _limita(valore, minimo=0, massimo=100):
        return max(minimo, min(massimo, valore))

    class Percorso(object):
        """Un percorso relazionale opzionale (uno degli otto archetipi).

        affinita: 0-100, quanto il rapporto è cresciuto (NON è attrazione).
        tappa:    a che punto è lo slow burn (0 = non iniziato). Le tappe
                  le decide la sceneggiatura, una per scena chiave.
        chiuso:   True se Sara ha chiuso la porta: niente più scene del percorso.
        """

        # Valori di classe = valori predefiniti anche per i vecchi salvataggi.
        affinita = 0
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

    # Testi delle tappe mostrati nel Diario: chiave -> lista indicizzata per tappa.
    # Si aggiornano episodio per episodio.
    TAPPE = {
        "simon":  ["Ancora uno sconosciuto.", "Il personal trainer della palestra.", "Un istruttore gentile che si ricorda di lei."],
        "daniel": ["Ancora uno sconosciuto.", "Il capo arrogante del compagno.", "Forse non è solo arroganza."],
        "howard": ["Ancora uno sconosciuto.", "Il vicino un po' strano.", "Un uomo solo che le fa tenerezza."],
        "editore": ["Ancora uno sconosciuto.", "Un editore che ha ascoltato il suo sogno."],
    }

    def percorso(chiave):
        return store.percorsi[chiave]

    def incontra(chiave):
        """Segna il primo incontro: da qui il personaggio compare nel Diario."""
        p = percorso(chiave)
        if not p.incontrato:
            p.incontrato = True
            _annuncia("Diario: nuova pagina — {}".format(p.nome))

    def affinita(chiave, delta, motivo=None):
        """Cambia l'affinità di un percorso. Non fa nulla se il percorso è chiuso."""
        p = percorso(chiave)
        if p.chiuso or delta == 0:
            return
        p.affinita = _limita(p.affinita + delta)
        if motivo is None:
            motivo = "{} se ne ricorderà.".format(p.nome)
        numero = " ({:+d})".format(delta) if persistent.mostra_numeri else ""
        _annuncia(motivo + numero)

    def tappa(chiave, nuova):
        """Porta un percorso alla tappa indicata (mai indietro)."""
        p = percorso(chiave)
        if not p.chiuso and nuova > p.tappa:
            p.tappa = nuova

    def chiudi(chiave):
        p = percorso(chiave)
        if not p.chiuso:
            p.chiuso = True
            _annuncia("Sara ha chiuso la porta a {}.".format(p.nome))

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
            _annuncia("Diario: retroscena su {}".format(p.nome))

    def legame(delta, motivo=None):
        """Il legame di Sara con il compagno (0-100)."""
        store.sara_legame = _limita(store.sara_legame + delta)
        if motivo:
            numero = " ({:+d})".format(delta) if persistent.mostra_numeri else ""
            _annuncia(motivo + numero)

    def curiosita(delta, motivo=None):
        """Quanto Sara è disposta a guardare oltre i propri confini (0-100)."""
        store.sara_curiosita = _limita(store.sara_curiosita + delta)
        if motivo:
            numero = " ({:+d})".format(delta) if persistent.mostra_numeri else ""
            _annuncia(motivo + numero)

    def segreto(chiave, descrizione):
        """Qualcosa che Sara tiene nascosto al compagno."""
        if chiave not in store.segreti:
            store.segreti[chiave] = descrizione
            _annuncia("Sara ha un segreto.")

    def segna(chiave, valore=True):
        """Ricorda un fatto o una scelta (es. 'ep1_palestra_da_sola')."""
        store.fatti[chiave] = valore

    def fatto(chiave):
        return store.fatti.get(chiave, False)

    def _annuncia(testo):
        if persistent.mostra_effetti:
            renpy.notify(testo)


## Preferenze del giocatore (valgono per tutte le partite).
default persistent.mostra_effetti = True
default persistent.mostra_numeri = False

## Nome del compagno: lo sceglie il giocatore all'inizio.
default nome_compagno = "Josh"

## Sara.
default sara_legame = 80      # parte da una coppia felice
default sara_curiosita = 0

## Percorsi. I quattro senza scheda esistono già per non rompere i salvataggi
## quando arriveranno.
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
