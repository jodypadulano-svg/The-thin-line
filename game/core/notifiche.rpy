## =============================================================================
## NOTIFICHE DELLE VARIABILI (A2)
## =============================================================================
## Ogni variazione compare in alto al centro, con il colore del personaggio o
## della variabile, per circa tre secondi. Più variazioni si impilano.
## Opzioni: "Mostra effetti" spegne tutto; senza "Mostra numeri" al posto dei
## numeri compaiono frecce.

define _notifiche_coda = []
define DURATA_NOTIFICA = 3.0
define MAX_NOTIFICHE = 3

## La coda cambia durante il gioco: va detto a Ren'Py, altrimenti lo screen la
## tratta come costante e non si aggiorna.
init -1 python:
    renpy.not_const("_notifiche_coda")

init python:
    import time as _time

    def _aggiungi_notifica(titolo, colore, motivo=None):
        if not persistent.effetti_visibili:
            return
        _notifiche_coda.append({
            "titolo": titolo,
            "colore": colore,
            "motivo": motivo,
            "scade": _time.time() + DURATA_NOTIFICA,
        })
        del _notifiche_coda[:-MAX_NOTIFICHE]
        renpy.show_screen("notifiche_stat")
        renpy.restart_interaction()

    def _annuncia(nome, delta, colore, motivo=None):
        if persistent.numeri_visibili:
            valore = "{:+d}".format(delta)
        else:
            valore = "▲" if delta > 0 else "▼"
        _aggiungi_notifica("{}  {}".format(nome, valore), colore, motivo)

    def _annuncia_testo(testo):
        _aggiungi_notifica(testo, "#ffffff")

    def _scadi_notifiche():
        adesso = _time.time()
        _notifiche_coda[:] = [v for v in _notifiche_coda if v["scade"] > adesso]
        if not _notifiche_coda:
            renpy.hide_screen("notifiche_stat")
        renpy.restart_interaction()

screen notifiche_stat():
    zorder 200
    vbox:
        xalign 0.5
        ypos 20
        spacing 8
        for v in _notifiche_coda:
            frame:
                xalign 0.5
                padding (26, 10)
                background Solid("#000000bb")
                vbox:
                    text v["titolo"] size 32 bold True color v["colore"] xalign 0.5
                    if v["motivo"]:
                        text v["motivo"] size 24 color "#ffffffcc" xalign 0.5
    timer 0.25 repeat True action Function(_scadi_notifiche)
