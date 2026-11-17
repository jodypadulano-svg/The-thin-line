## =============================================================================
## EPISODIO 1 — scene di casa (trama principale)
## =============================================================================
## BOZZA: dialoghi provvisori per rendere il gioco giocabile. La bibbia
## (docs/bibbia-narrativa.md) resta la fonte: dove non decide, qui c'è un
## segnaposto da riscrivere.

## L'invito alla cena aziendale ora è nel giorno 2 (ep1_giorno02.rpy).


label ep1_finale:
    ## Chiusura: Sara a casa dopo la festa. Un segreto possibile: il biglietto
    ## dell'editore. Prima scelta "racconta / nascondi" del gioco.
    $ vai("camera", "Casa — notte")
    n "Il biglietto da visita dell'editore è ancora nella borsetta. Carta spessa, lettere in rilievo."
    sp "«Mi mandi le prime cinquanta pagine.» L'ha detto davvero."
    c "Sei ancora sveglia?"

    menu:
        sp "Dovrei dirglielo."
        "Raccontargli tutto dell'editore." (josh=30):
            $ interest("josh", 2, "Sara condivide il suo sogno con [nome_compagno].")
            s "Alla festa ho conosciuto un editore. Vuole leggere il mio romanzo."
            c "Cosa? Ma è fantastico! Visto? Te l'avevo detto."
            c "...E te l'ha presentato Daniel?"
            s "Sì. Lo so. Non me l'aspettavo neanche io."
            n "Lui resta in silenzio un momento di troppo."
        "Tenerlo per sé, per ora.":
            $ segreto("ep1_editore", "Il biglietto dell'editore, e l'aiuto di Daniel.")
            $ corruption(2, "Sara tiene per sé un regalo di Daniel.")
            s "Sì... pensavo alla festa. Dormi."
            sp "Gliene parlerò. Quando ci sarà qualcosa di vero da dire."
            sp "Non è un segreto. È solo... non ancora."

    if fatto("ep1_palestra_da_sola"):
        sp "E non gli ho nemmeno detto che martedì mi sono allenata con Simon."
        sp "Non c'era niente da dire. Giusto?"

    $ luogo_corrente = ""
    scene bg nero with fade
    call inizio_retroscena
    rs "Dall'altra parte della città, Daniel scorre i messaggi."
    rs "Uno è dell'editore: «Interessante, la tua amica. Molto.»"
    rs "Daniel sorride. Non ha ancora capito che non è un complimento per lui."
    $ retroscena("daniel", "La festa era organizzata per far colpo su Sara.")
    $ retroscena("editore", "L'editore è rimasto colpito da Sara, non solo dal suo romanzo.")
    call fine_retroscena
    return
