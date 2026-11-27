default howard_prossima_faccenda = 1
default howard_ultima_faccenda_giorno = 0
default howard_tenute_regalate = ()

define HOWARD_FACCENDE = (
    ("Scrub the kitchen floor, would you?", "Sara kneels on a folded towel and works the brush into the grout, one tile at a time."),
    ("The oven needs a good scrub.", "Sara crouches by the open oven and scours the baked-on grease from the rack."),
    ("Give the rug a good beating out on the balcony.", "Sara lifts the rug over the railing and beats it until the clouds of dust thin out."),
    ("Scrub the grease off the cupboards.", "Sara reaches above her shoulders and scrubs the sticky tops of the kitchen cupboards."),
    ("Wash the windows, inside and out where you can reach.", "Sara washes the glass and kneels to mop the water from the sill."),
    ("Move those boxes into the pantry.", "Sara carries the full boxes across the kitchen one at a time, holding each against her chest."),
    ("Get the limescale off the shower.", "Sara bends over the shower tray and works at the white deposits along the glass."),
    ("Vacuum under the sofa properly.", "Sara gets down close to the floor and pushes the vacuum nozzle all the way under the sofa."),
    ("Wash those towels by hand.", "Sara works the towels through the water and wrings each heavy one out over the basin."),
    ("Strip the bed and make it up fresh.", "Sara lifts the corner of the mattress and works the clean sheet underneath."),
    ("Empty the fridge and clean it out.", "Sara lifts the drawers to the sink, washes them, then bends into the fridge to scrub the shelves."),
    ("The hall floor could do with a polish.", "Sara works the polish into the hall floor by hand, backing up one small patch at a time."),
    ("Empty the cupboard and scrub the shelves.", "Sara stacks the plates on the table and bends down to scrub the bottom shelf."),
    ("Wash the curtains for me.", "Sara lifts the wet curtains from the basin and wrings the heavy fabric before hanging it up."),
    ("See if you can get those pans clean.", "Sara braces a pan against the sink and scrapes away the black crust at the bottom."),
    ("Brush down the chair cushions.", "Sara puts her weight into the brush, cleaning one cushion at a time."),
    ("Give the balcony a proper wash.", "Sara leans into the deck brush and pushes the dirty water toward the drain."),
    ("Clear out the storage cupboard and sweep it.", "Sara hauls out the crates, sweeps the bare floor, then carries them back in."),
    ("Scrub the skirting boards all the way round.", "Sara works along the living-room wall on her knees, dragging the bucket with her."),
    ("Wash underneath the dining table.", "Sara moves each chair out and works the brush around the table legs."),
)

init python:
    def howard_tenuta_faccende(corruzione):
        ## Fasce raddoppiate da Jody il 27/11: 0-99, 100-199, 200-300, oltre 300.
        if corruzione > 300:
            return "nuda"
        if corruzione >= 200:
            return "seminuda"
        if corruzione >= 100:
            return "sexy"
        return "classica"

    def howard_puo_fare_faccenda(giorno, fascia, libero, in_casa, altro_incontro, ultima_visita, interesse):
        return (
            giorno >= 17 and fascia == "sera" and libero and in_casa
            and not altro_incontro and ultima_visita != giorno and interesse > 50
        )

## Il calendario chiama questa label al rientro dal lavoro. Indica anche
## incontri già avvenuti e incontri fissi previsti più tardi nello stesso giorno.
label howard_faccende_dopo_lavoro(libero, howard_in_casa, altro_incontro_howard):
    if not howard_puo_fare_faccenda(giorno, FASCE[fascia_corrente], libero, howard_in_casa, altro_incontro_howard, howard_ultima_faccenda_giorno, valore_interest("howard")):
        return False

    $ _faccenda_howard = howard_prossima_faccenda
    $ _tenuta_howard = howard_tenuta_faccende(sara_corruption)
    $ _richiesta_howard, _lavoro_howard = HOWARD_FACCENDE[_faccenda_howard - 1]
    $ vai("casa_howard", "Howard's flat — After work")
    $ cg("Howard answers Sara's knock", "images/cg/ep1/d9_04_howard_porta.webp")
    n "Sara stops at Howard's door and knocks."
    s "Is there anything I can do to help?"
    ho "Yes. [_richiesta_howard]"
    $ cg("Inside Howard's flat", "images/cg/ep1/d9_05_casa_howard.webp")

    if _tenuta_howard != "nuda" and _tenuta_howard not in howard_tenute_regalate:
        if _tenuta_howard == "classica":
            $ cg("Howard gives Sara the classic maid uniform", "images/cg/ep2/howard_faccenda_regalo_classica.png")
            ho "Here. I got you a dress and an apron to work in."
        elif _tenuta_howard == "sexy":
            if renpy.loadable("images/cg/ep2/howard_faccenda_regalo_sexy.webp"):
                $ cg("Howard gives Sara the shorter maid uniform", "images/cg/ep2/howard_faccenda_regalo_sexy.webp")
            ho "I got you a new uniform. This one's yours too."
            n "Sara unfolds the shorter black dress and the little white apron."
        else:
            ho "I've got something new for you to wear while you work."
            n "Sara lifts the new uniform out of the parcel. There isn't much fabric to it."
        s "Thank you, Howard."
        $ howard_tenute_regalate += (_tenuta_howard,)

    if not sara_cameriera:
        ho "Go and change in the bathroom. You'll get your own clothes dirty otherwise."
        n "Sara takes her things to the bathroom and closes the door."
        call inizio_retroscena
        if _tenuta_howard == "classica" and renpy.loadable("images/cg/ep2/howard_faccenda_bonus_serratura.webp"):
            $ cg("Howard watches Sara change through the keyhole", "images/cg/ep2/howard_faccenda_bonus_serratura.webp")
        rs "Out in the hall, Howard bends to the keyhole. From there he can see Sara changing."
        call fine_retroscena
    else:
        n "Sara goes straight to the bathroom to change. By now she knows where to put her things."

    if _tenuta_howard == "nuda":
        n "She leaves her clothes in the bathroom and comes back ready to work."
    $ _cg_faccenda_howard = "images/cg/ep2/howard_faccenda_%02d_%s.webp" % (_faccenda_howard, _tenuta_howard)
    if renpy.loadable(_cg_faccenda_howard):
        $ cg("Sara does the housework while Howard watches", _cg_faccenda_howard)
    else:
        $ cg("Inside Howard's flat", "images/cg/ep1/d9_05_casa_howard.webp")
    n "[_lavoro_howard]"
    n "Howard settles into his chair and watches while she finishes."
    if not sara_cameriera:
        sp "I suppose I'm his maid now. I don't mind doing it for free. I'm helping an older man who could use a hand."
    $ sara_cameriera = True
    $ howard_ultima_faccenda_giorno = giorno
    $ howard_prossima_faccenda = _faccenda_howard % len(HOWARD_FACCENDE) + 1
    $ via_cg()
    return True
