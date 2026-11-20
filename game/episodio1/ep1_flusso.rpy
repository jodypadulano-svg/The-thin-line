## =============================================================================
## EPISODIO 1 — scaletta
## =============================================================================
## Ordine delle giornate (proposta, vedi docs/scaletta-episodio-1.md).
## Ogni scena vive nel file del suo personaggio; qui c'è solo l'ordine.

label ep1_inizio:
    $ episodio = 1

    ## Riscrittura in inglese in corso, un giorno alla volta (docs/mese-1.md).
    ## Giorni 1-9 riscritti; dal giorno 10 restano le scene vecchie in italiano,
    ## rimesse nei giorni del calendario (i giorni non ancora scritti si saltano).
    call ep1_d1
    call ep1_d2
    call ep1_d3
    call ep1_d4
    call ep1_d5
    call ep1_d6
    call ep1_d7
    call ep1_d8
    call ep1_d9

    call nuovo_giorno(13, "Saturday")
    call daniel_3_festa
    call ep1_finale

    jump ep1_fine


label ep1_fine:
    $ luogo_corrente = ""
    scene bg nero with fade
    n "{size=+20}Fine dell'Episodio 1{/size}"
    n "Grazie per aver giocato. Le tue scelte sono salvate: il prossimo episodio partirà da qui."
    return
