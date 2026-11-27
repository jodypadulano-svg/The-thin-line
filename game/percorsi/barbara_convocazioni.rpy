## =============================================================================
## BARBARA — convocazioni della stagista speciale (decisioni del 24/11/2026)
## =============================================================================
## Con sara_stagista, ogni giorno lavorativo dal 19 Barbara convoca Sara con
## probabilità 20%, per una missione non completata di cui sono soddisfatte
## soglie e prerequisiti. Presentarsi è obbligatorio; la missione si può sempre
## rifiutare, e in quel caso resta estraibile. Si estraggono solo le missioni
## già scritte: per aggiungerne una basta una riga in MISSIONI_BARBARA e il label.
##
## Uso nella giornata, in orario di lavoro:
##     call barbara_convocazione

default barbara_missioni_completate = []
default barbara_ultima_convocazione = 0

init python:
    ## Nei test si cambia la probabilità per avere un esito certo.
    BARBARA_CONVOCAZIONI = {"probabilita": 0.20}

    ## numero: (label, Interest Barbara minimo, Corruption minima, prerequisiti)
    MISSIONI_BARBARA = {
        2: ("barbara_missione_02", 20, 10, ()),
        8: ("barbara_missione_08", 25, 15, ()),
    }

    def barbara_missioni_disponibili():
        fatte = store.barbara_missioni_completate
        return [m for m, (_label, _int, _corr, _pre) in sorted(MISSIONI_BARBARA.items())
                if m not in fatte
                and valore_interest("capa") >= _int
                and store.sara_corruption >= _corr
                and all(p in fatte for p in _pre)]

    def barbara_completa(missione):
        if missione not in store.barbara_missioni_completate:
            store.barbara_missioni_completate.append(missione)

    def barbara_sorteggia():
        """Il numero della missione di oggi, oppure None. Una sola estrazione al giorno."""
        lavorativo = (store.giorno - 1) % 7 < 5
        if not store.sara_stagista or not lavorativo or store.barbara_ultima_convocazione == store.giorno:
            return None
        store.barbara_ultima_convocazione = store.giorno
        if renpy.random.random() >= BARBARA_CONVOCAZIONI["probabilita"]:
            return None
        disponibili = barbara_missioni_disponibili()
        return renpy.random.choice(disponibili) if disponibili else None

default _barbara_missione = None

label barbara_convocazione:
    $ _barbara_missione = barbara_sorteggia()
    if _barbara_missione is not None:
        call expression MISSIONI_BARBARA[_barbara_missione][0]
    return


## --- Missione 2: massaggio alle spalle (Interest 20, Corruption 10) -------------------------

label barbara_missione_02:
    $ suono("telefono_vibra")
    $ cg("Sara reads Barbara's summons at her newsroom desk", "images/cg/ep2/barbara_m02_00_convocazione.png")
    n "The message on her screen is four words long. {i}My office, please. Now.{/i}"
    sp "I signed it. When she calls, I go. That's what I signed."
    $ vai("redazione", "Barbara's office — 12:10 p.m.")
    $ musica("barbara")
    $ cg("Barbara in her office armchair, eyes closed, her necklace in her lap; Sara at the door", "images/cg/ep2/barbara_m02_01_poltrona.webp")
    n "Barbara is in the armchair instead of behind the desk. She has taken off her necklace and is holding it in her lap as if it weighed something."
    ba "Close the door. I've been on the telephone to idiots since eight."
    ba "My shoulders, Sara. Ten minutes."
    menu:
        "Go and stand behind her.":
            $ barbara_completa(2)
            $ segna("barbara_missione_02_fatta")
            $ via_cg()
            $ cg("Sara behind the armchair, her hands on Barbara's shoulders", "images/cg/ep2/barbara_m02_02_massaggio.webp")
            n "Sara hangs her jacket on the door and goes round the chair. Under the silk Barbara's shoulders are as hard as the desk."
            ba "You've got strong hands for a girl who types."
            s "I knead bread. When I'm stuck on a chapter."
            ba "What's the chapter doing?"
            s "She's about to lie to someone who loves her. I can't decide if she enjoys it."
            n "Under her thumbs something gives way. Barbara lets out a breath Sara feels all the way up her arms."
            ba "Of course you can. You're only deciding whether to write it down."
            $ via_cg()
            $ cg("Barbara, without turning, holds Sara's hand on her shoulder", "images/cg/ep2/barbara_m02_03_mano.webp")
            n "When the ten minutes are up, Barbara reaches back without turning and takes Sara's hand where it is. She keeps it there. Five seconds. Ten."
            ba "Good girl. Go and have your lunch."
            sp "She said it like a full stop. Why am I still smiling in the corridor?"
        "«I'd rather not, today.»":
            $ segna("barbara_missione_02_rifiutata")
            s "I'd rather not, today."
            n "It comes out quite steady. Barbara opens one eye."
            ba "Then sit down and keep me company. You can do that, I hope."
            s "I can do that."
            n "They sit. Barbara asks about the piece Sara is working on, and listens to the answer. After ten minutes she puts her necklace back on."
    $ via_cg()
    return

## --- Missione 8: le bozze (Interest 25, Corruption 15) ------------------------------------
label barbara_missione_08:
    $ suono("telefono_vibra")
    $ cg("The summons lighting up Sara's phone among the morning proofs", "images/cg/ep2/barbara_m08_00_convocazione.webp")
    n "Barbara's message arrives without a greeting. {i}My office. Before lunch, please.{/i}"
    $ via_cg()
    $ vai("redazione", "Barbara's office — Before lunch")
    $ musica("barbara")
    $ cg("Barbara in the office armchair with galley proofs in her lap, her shoes set neatly aside; Sara framed from the shoulders up at the door", "images/cg/ep2/barbara_m08_01_bozze.webp")
    ba "I need to get through these before they send a second pile."
    s "Do you want me to read them to you?"
    ba "No. I'd like you to kiss my feet. One at a time. While I read."
    n "She lifts the corner of the first page, then lets it settle again. She gives Sara time to answer."
    menu:
        "Agree.":
            s "All right. You'll have to tell me if they put the wrong headline back in."
            ba "You'll hear me if they do."
            $ via_cg()
            $ cg("Low close-up of Barbara holding a turned proof halfway over, Sara beside the armchair, her face seen in profile", "images/cg/ep2/barbara_m08_02_pagina.webp")
            n "Sara kneels by the armchair and kisses first one foot, then the other. The paper goes very quiet above her."
            s "Was it the headline?"
            ba "No. I think I've read the same line three times."
            n "Sara looks up. Barbara is still holding the same page. They both laugh."
            $ barbara_completa(8)
            $ segna("barbara_missione_08_fatta")
        "Decline.":
            s "I can help with the proofs. I'd rather leave it there today."
            ba "All right. Tell me if you see yesterday's headline. I keep asking them to take it out."
            n "Barbara hands her half the pile. They find the headline on page three."
    $ via_cg()
    return
