## =============================================================================
## EPISODIO 1 — scene di casa (trama principale)
## =============================================================================
## BOZZA: dialoghi provvisori per rendere il gioco giocabile. La bibbia
## (docs/bibbia-narrativa.md) resta la fonte: dove non decide, qui c'è un
## segnaposto da riscrivere.

label ep1_prologo:
    $ vai("casa", "Casa — sera")
    $ cg("Sara al tavolo della cucina, portatile aperto, una tazza di tè ormai fredda")

    sp "Capitolo tre. Ancora il capitolo tre."
    sp "La protagonista deve aprire quella porta e io non so cosa ci sia dall'altra parte."
    n "Sara cancella l'ultima riga. Poi la riscrive identica."

    $ via_cg()
    n "La chiave gira nella serratura."
    c "Sono a casa! Dimmi che è avanzato qualcosa, sto morendo di fame."
    s "C'è la pasta di ieri. E c'è anche una scrittrice in crisi, se ti interessa."
    c "Mi interessa sempre la scrittrice."
    n "Lui le bacia la testa e sbircia lo schermo."
    c "Capitolo tre?"
    s "Non dirlo con quel tono."
    c "Quale tono? Io lo leggerò quando sarà finito. Prima copia autografata."

    sp "È così da quando ci conosciamo. Lui crede in me più di quanto ci creda io."

    menu:
        sp "E stasera..."
        "Chiudere il portatile e passare la serata con lui.":
            $ legame(3, "Sara sceglie lui, stasera.")
            s "Basta capitolo tre. Pasta e divano?"
            c "Ti sposerei solo per questa frase."
        "Scrivere ancora un'ora: l'ispirazione è arrivata.":
            $ curiosita(1)
            $ segna("ep1_prologo_scrive")
            s "Dammi un'ora. Credo di aver capito cosa c'è dietro la porta."
            c "Vai. Io scaldo la pasta e ti porto un tè caldo."

    $ vai("camera", "Casa — notte")
    n "Il telefono di Sara vibra. Chiara."
    ch "Domani. Palestra. Niente scuse."
    s "Chiara, sono le undici."
    ch "Appunto, è il momento giusto per prendere decisioni importanti. Ti ho già iscritta, la prima lezione l'hai gratis."
    s "Mi hai iscritta senza chiedermelo?"
    ch "Ti ho iscritta {i}per{/i} te. È diverso. Alle sei. Ti passo a prendere."
    sp "Non sono mai entrata in una palestra in vita mia."
    sp "Ma con Chiara dire di no non è mai stata un'opzione."
    return


label ep1_invito_cena:
    $ vai("casa", "Casa — sera")
    c "Allora, sopravvissuta alla palestra?"
    s "Ho scoperto di avere muscoli di cui ignoravo l'esistenza. Mi fanno male tutti."
    c "Ho una notizia che ti farà dimenticare il dolore. Venerdì c'è la cena aziendale, e quest'anno sono invitati anche i compagni."
    s "Quindi conoscerò finalmente il famoso capo?"
    c "Daniel. È... un tipo. Difficile, ma è uno che conta. Se gli faccio una buona impressione, per me è importante."
    sp "Non l'ho mai sentito parlare di lavoro con quella faccia."
    s "Allora faremo un'ottima impressione. Tutti e due."
    return


label ep1_finale:
    ## Chiusura: Sara a casa dopo la festa. Un segreto possibile: il biglietto
    ## dell'editore. Prima scelta "racconta / nascondi" del gioco.
    $ vai("camera", "Casa — notte")
    n "Il biglietto da visita dell'editore è ancora nella borsetta. Carta spessa, lettere in rilievo."
    sp "«Mi mandi le prime cinquanta pagine.» L'ha detto davvero."
    c "Sei ancora sveglia?"

    menu:
        sp "Dovrei dirglielo."
        "Raccontargli tutto dell'editore.":
            $ legame(2, "Sara condivide il suo sogno con [nome_compagno].")
            s "Alla festa ho conosciuto un editore. Vuole leggere il mio romanzo."
            c "Cosa? Ma è fantastico! Visto? Te l'avevo detto."
            c "...E te l'ha presentato Daniel?"
            s "Sì. Lo so. Non me l'aspettavo neanche io."
            n "Lui resta in silenzio un momento di troppo."
        "Tenerlo per sé, per ora.":
            $ segreto("ep1_editore", "Il biglietto dell'editore, e l'aiuto di Daniel.")
            $ curiosita(2)
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
