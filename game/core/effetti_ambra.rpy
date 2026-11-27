## =============================================================================
## Effetto delle scelte ambra (acceleratori), Jody 27/11/2026
## =============================================================================
## Quando un menu contiene una scelta ambra: la musica e l'ambiente vanno in pausa
## (riprendono dallo stesso punto), parte il battito del cuore in loop e la scena
## sfuma in bianco e nero con una leggera sfocatura. Il menu resta a colori.
## Alla scelta torna tutto com'era; se si sceglie proprio l'opzione ambra, un
## piccolo lampo bianco. Se manca il file del battito, l'effetto resta muto.
##
## File del battito: game/audio/suoni/battito.ogg (o .mp3/.wav/.opus).
## Agganciato in screens.rpy, screen choice.

init python:
    renpy.music.register_channel("battito", mixer="sfx", loop=True)

    def ambra_inizio():
        if store._ambra_attiva:
            return
        store._ambra_attiva = True
        store._ambra_scelta = False
        renpy.music.set_pause(True, channel="music")
        renpy.music.set_pause(True, channel="ambiente")
        f = _file_audio("suoni", "battito")
        if f:
            renpy.music.play(f, channel="battito", loop=True, fadein=0.3)
        renpy.show_layer_at([ambra_grigio], layer="master")

    def ambra_fine():
        if not store._ambra_attiva:
            return
        store._ambra_attiva = False
        renpy.music.stop(channel="battito", fadeout=0.4)
        renpy.music.set_pause(False, channel="music")
        renpy.music.set_pause(False, channel="ambiente")
        renpy.show_layer_at([ambra_colore], layer="master")
        if store._ambra_scelta:
            renpy.transition(ambra_lampo)
        store._ambra_scelta = False

default _ambra_attiva = False
default _ambra_scelta = False

define ambra_lampo = Fade(0.05, 0.0, 0.35, color="#ffffff")

transform ambra_grigio:
    matrixcolor SaturationMatrix(1.0) blur 0
    linear 0.5 matrixcolor SaturationMatrix(0.0) blur 3

transform ambra_colore:
    matrixcolor SaturationMatrix(0.0) blur 3
    linear 0.4 matrixcolor SaturationMatrix(1.0) blur 0
