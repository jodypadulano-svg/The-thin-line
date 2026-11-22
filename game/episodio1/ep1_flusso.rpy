## =============================================================================
## EPISODIO 1 — scaletta
## =============================================================================
## Ordine delle giornate (proposta, vedi docs/scaletta-episodio-1.md).
## Ogni scena vive nel file del suo personaggio; qui c'è solo l'ordine.

label ep1_inizio:
    $ episodio = 1

    ## Riscrittura in inglese, un giorno alla volta (docs/mese-1.md): giorni 1-13
    ## riscritti. Dopo il giorno 13, il teaser «Nella prossima puntata» e il montaggio
    ## dei personaggi con la canzone (la scena dopo i titoli).
    call ep1_d1
    call ep1_d2
    call ep1_d3
    call ep1_d4
    call ep1_d5
    call ep1_d6
    call ep1_d7
    call ep1_d8
    call ep1_d9
    call ep1_d10
    call ep1_d11
    call ep1_d12

    call ep1_d13
    call ep1_teaser
    call ep1_d13_montaggio

    jump ep1_fine


label ep1_fine:
    $ luogo_corrente = ""
    scene bg nero with fade
    n "{size=+20}Fine dell'Episodio 1{/size}"
    n "Grazie per aver giocato. Le tue scelte sono salvate: il prossimo episodio partirà da qui."
    return
