## =============================================================================
## PRESENTAZIONE SENZA GRAFICA
## =============================================================================
## Finché non ci sono immagini, ogni luogo è un colore + un cartello col nome.
## Quando arriva la grafica basta mettere in game/images un file con lo stesso
## nome (es. "bg palestra.webp") e cancellare la riga `image bg palestra`
## corrispondente qui sotto.

image bg nero = Solid("#000000")
image bg casa = Solid("#2a2230")
image bg redazione = Solid("#1e2530")
image bg camera = Solid("#231c2b")
image bg pianerottolo = Solid("#25262b")
image bg casa_howard = Solid("#2b2a1f")
image bg palestra = Solid("#1d2a2a")
image bg locale = Solid("#2a1d2a")
image bg ristorante = Solid("#2b2219")
image bg ufficio_compagno = Solid("#1f2430")
image bg villa_daniel = Solid("#1c1a28")
image bg strada = Solid("#1f1f24")
image bg bar_aperitivo = Solid("#2a1f1c")
image bg enoteca = Solid("#2b1a1f")
image bg fiume = Solid("#1d2a24")
image bg negozio = Solid("#2b2428")


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
        text "Day [numero]" size 64 xalign 0.5 color "#ffffff"
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
        text "BEHIND THE SCENES — Sara doesn't know" size 28 color "#ffffff" bold True

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
    zorder -1   # sotto i menu delle scelte
    frame:
        align (0.5, 0.35)
        xmaximum 1300
        padding (30, 20)
        background Solid("#ffffff10")
        text "[[CG] " + descrizione size 26 color "#ffffff88" italic True

init python:
    def cg(descrizione, immagine=None):
        """Mostra la CG della scena. Se il file esiste lo mostra a tutto
        schermo; altrimenti mostra la didascalia [CG] come segnaposto.
        Uso: $ cg("descrizione", "images/cg/ep1/d1_01_armadio.webp")"""
        if immagine and renpy.loadable(immagine):
            renpy.show("cg_corrente", what=Transform(immagine, fit="cover", xysize=(config.screen_width, config.screen_height)))
            renpy.with_statement(dissolve)
        else:
            renpy.show_screen("segnaposto_cg", descrizione=descrizione)

    def filmato(video, stop_music=True):
        """Filmato a schermo intero (WebM). Se il file manca ancora, si salta."""
        if renpy.loadable(video):
            renpy.movie_cutscene(video, stop_music=stop_music)

    def zoom_cg(descrizione, immagine, area, durata=4.5):
        """Zoom lento su un dettaglio di una CG già fatta (lo «sguardo» di un personaggio).
        area = (x, y, larghezza, altezza) in pixel dell'immagine originale, in 16:9."""
        if immagine and renpy.loadable(immagine):
            W, H = renpy.image_size(immagine)
            x, y, w, h = area
            ## Si parte da un'inquadratura 1,6 volte più larga, centrata sul dettaglio
            ## (non dall'immagine intera: così non si vede il resto della scena).
            sw, sh = min(W, w * 1.6), min(H, h * 1.6)
            sx = max(0, min(W - sw, x + w / 2.0 - sw / 2.0))
            sy = max(0, min(H - sh, y + h / 2.0 - sh / 2.0))
            ## Prima si toglie la CG: se il tag restasse lo stesso, l'animazione
            ## partirebbe dal tempo dell'immagine precedente e finirebbe subito.
            renpy.hide("cg_corrente")
            ## Crop in frazioni dell'immagine (0-1): durante l'animazione Ren'Py
            ## calcola valori con la virgola, che leggerebbe comunque come frazioni.
            fW, fH = float(W), float(H)
            renpy.show("cg_corrente", what=At(immagine, zoom_sguardo(
                sx / fW, sy / fH, sw / fW, sh / fH, x / fW, y / fH, w / fW, h / fH, durata)))
            renpy.with_statement(dissolve)
        else:
            renpy.show_screen("segnaposto_cg", descrizione=descrizione)

    def via_cg():
        renpy.hide_screen("segnaposto_cg")
        if renpy.showing("cg_corrente"):
            renpy.hide("cg_corrente")
            renpy.with_statement(dissolve)


## Le notifiche delle scelte vanno in alto a destra, così non coprono il
## cartello del luogo né i titoli dei menu.
style notify_frame:
    xalign 1.0
    xoffset -30


## Zoom lento: dall'immagine intera al dettaglio (usato da zoom_cg) ---------------
transform zoom_sguardo(sx, sy, sw, sh, x, y, w, h, durata):
    crop (sx, sy, sw, sh)
    xysize (config.screen_width, config.screen_height)
    ease durata crop (x, y, w, h)
