## =============================================================================
## PRESENTAZIONE SENZA GRAFICA
## =============================================================================
## Finché non ci sono immagini, ogni luogo è un colore + un cartello col nome.
## Quando arriva la grafica basta mettere in game/images un file con lo stesso
## nome (es. "bg palestra.webp") e cancellare la riga `image bg palestra`
## corrispondente qui sotto.

image bg nero = Solid("#000000")
image bg casa = Solid("#2a2230")
image bg camera = Solid("#231c2b")
image bg pianerottolo = Solid("#25262b")
image bg casa_howard = Solid("#2b2a1f")
image bg palestra = Solid("#1d2a2a")
image bg locale = Solid("#2a1d2a")
image bg ristorante = Solid("#2b2219")
image bg ufficio_compagno = Solid("#1f2430")
image bg villa_daniel = Solid("#1c1a28")
image bg strada = Solid("#1f1f24")


## Cartello del luogo (in alto a sinistra) -------------------------------------

default luogo_corrente = ""

screen cartello_luogo():
    zorder 50
    if luogo_corrente:
        frame:
            xpos 40 ypos 30
            padding (24, 10)
            background Solid("#00000099")
            text luogo_corrente size 30 color "#ffffffcc"

init python:
    config.overlay_screens.append("cartello_luogo")

    def vai(sfondo, nome_luogo):
        """Cambia scena: sfondo + nome del luogo. Uso: $ vai("palestra", "Palestra — sera")"""
        store.luogo_corrente = nome_luogo
        renpy.scene()
        renpy.show("bg " + sfondo)
        renpy.with_statement(dissolve)


## Cartello del giorno ---------------------------------------------------------

label nuovo_giorno(numero, titolo):
    $ giorno = numero
    $ luogo_corrente = ""
    scene bg nero with fade
    show screen titolo_giorno(numero, titolo)
    pause 2.0
    hide screen titolo_giorno with dissolve
    return

screen titolo_giorno(numero, titolo):
    vbox:
        align (0.5, 0.45)
        spacing 12
        text "Giorno [numero]" size 64 xalign 0.5 color "#ffffff"
        text titolo size 34 xalign 0.5 color "#c8385a"


## Retroscena: ciò che il giocatore vede e Sara no ------------------------------
## Uso:
##     call inizio_retroscena
##     rs "Daniel scrive all'editore..."
##     call fine_retroscena

default in_retroscena = False

screen fascia_retroscena():
    zorder 60
    frame:
        xalign 0.5 ypos 30
        padding (30, 10)
        background Solid("#c8385acc")
        text "RETROSCENA — Sara non lo sa" size 28 color "#ffffff" bold True

label inizio_retroscena:
    $ in_retroscena = True
    show screen fascia_retroscena
    with dissolve
    return

label fine_retroscena:
    $ in_retroscena = False
    hide screen fascia_retroscena
    with dissolve
    return


## Segnaposto per le immagini mancanti -------------------------------------------
## Usalo per annotare la regia: il testo compare a schermo durante i test e
## ricorda quale CG va prodotta.  Uso:  $ cg("Sara entra in palestra, inquadratura larga")

screen segnaposto_cg(descrizione):
    zorder 40
    frame:
        align (0.5, 0.35)
        xmaximum 1300
        padding (30, 20)
        background Solid("#ffffff10")
        text "[[CG] " + descrizione size 26 color "#ffffff88" italic True

init python:
    def cg(descrizione):
        renpy.show_screen("segnaposto_cg", descrizione=descrizione)

    def via_cg():
        renpy.hide_screen("segnaposto_cg")


## Le notifiche delle scelte vanno in alto a destra, così non coprono il
## cartello del luogo né i titoli dei menu.
style notify_frame:
    xalign 1.0
    xoffset -30
