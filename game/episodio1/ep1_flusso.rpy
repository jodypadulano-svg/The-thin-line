## =============================================================================
## EPISODIO 1 — scaletta
## =============================================================================
## Ordine delle giornate (proposta, vedi docs/scaletta-episodio-1.md).
## Ogni scena vive nel file del suo personaggio; qui c'è solo l'ordine.

label ep1_inizio:
    $ episodio = 1

    ## Riscrittura in inglese in corso, un giorno alla volta (docs/mese-1.md).
    ## Giorni 1-3 riscritti; dal giorno 4 restano le scene vecchie in italiano.
    call ep1_d1
    call ep1_d2
    call ep1_d3

    call nuovo_giorno(4, "Una mattina di corsa")
    call howard_1_pianerottolo
    call daniel_2_patente

    call nuovo_giorno(5, "Sabato")
    call howard_2_spesa
    call simon_s3_locale

    call nuovo_giorno(6, "Da sola")
    call simon_s4_chiara_cancella
    if fatto("ep1_palestra_da_sola"):
        call simon_s5_allenamento

    call nuovo_giorno(7, "Chiusa fuori")
    call howard_3_chiusa_fuori

    call nuovo_giorno(8, "La festa")
    call daniel_3_festa
    call ep1_finale

    jump ep1_fine


label ep1_fine:
    $ luogo_corrente = ""
    scene bg nero with fade
    n "{size=+20}Fine dell'Episodio 1{/size}"
    n "Grazie per aver giocato. Le tue scelte sono salvate: il prossimo episodio partirà da qui."
    return
