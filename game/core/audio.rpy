## =============================================================================
## AUDIO — musiche, ambienti ed effetti
## =============================================================================
## Prompt per generarli: docs/prompt-audio.md (musica con Mureka).
## I file vanno in:
##   audio/musica/<nome>.ogg|.mp3   — musiche in loop
##   audio/ambienti/<nome>.ogg|.mp3 — rumori di fondo in loop (redazione, palestra)
##   audio/suoni/<nome>.ogg|.mp3|.wav — effetti singoli
## Come per le CG: se il file manca il gioco va avanti in silenzio, senza errori.
##
## Uso nelle scene:
##   $ musica("casa")          cambia musica con dissolvenza (stessa musica: non riparte)
##   $ musica(None)            sfuma la musica
##   $ ambiente("redazione")   rumore di fondo in loop;  $ ambiente(None) lo ferma
##   $ suono("sveglia")        effetto singolo

init python:
    renpy.music.register_channel("ambiente", mixer="sfx", loop=True)

    def _file_audio(cartella, nome):
        for est in (".ogg", ".mp3", ".wav", ".opus"):
            percorso = "audio/%s/%s%s" % (cartella, nome, est)
            if renpy.loadable(percorso):
                return percorso
        return None

    def musica(nome, dissolvenza=1.5):
        if nome is None:
            renpy.music.stop(channel="music", fadeout=dissolvenza)
            return
        f = _file_audio("musica", nome)
        if f:
            renpy.music.play(f, channel="music", loop=True, fadeout=dissolvenza,
                             fadein=dissolvenza, if_changed=True)

    def ambiente(nome, dissolvenza=1.0):
        if nome is None:
            renpy.music.stop(channel="ambiente", fadeout=dissolvenza)
            return
        f = _file_audio("ambienti", nome)
        if f:
            renpy.music.play(f, channel="ambiente", loop=True, fadeout=dissolvenza,
                             fadein=dissolvenza, if_changed=True)

    def suono(nome):
        f = _file_audio("suoni", nome)
        if f:
            renpy.sound.play(f, channel="sound")

## Musica del menu iniziale (se il file esiste).
init 1 python:
    _tema = _file_audio("musica", "tema_principale")
    if _tema:
        config.main_menu_music = _tema
