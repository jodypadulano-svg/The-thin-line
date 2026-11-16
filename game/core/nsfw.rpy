## =============================================================================
## AGGANCIO DELLE SCENE NSFW (A1)
## =============================================================================
## Le scene esplicite si generano con LM Studio (docs/guida-lm-studio.md) e
## finiscono in game/nsfw/<id>.rpy con la label nsfw_<id>.
## Nelle scene si richiamano così:
##     call scena_nsfw("simon_doccia")
## Finché il file non esiste, al suo posto compare un segnaposto: il gioco
## resta giocabile e i test passano.

label scena_nsfw(id):
    if renpy.has_label("nsfw_" + id):
        call expression "nsfw_" + id
    else:
        n "{color=#ff5c7a}[[NSFW: [id] — da generare]{/color}"
    return
