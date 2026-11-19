## =============================================================================
## DANIEL — il capo del compagno (docs/personaggi/daniel.md)
## L'EDITORE — incrocio di percorsi (docs/personaggi/editore.md)
## =============================================================================
## Tre incontri della scheda. BOZZA: dialoghi provvisori.
## Regola della scheda: il giocatore capisce il piano di Daniel, Sara no.

## Daniel 1 (la cena aziendale) è nel giorno 3: ep1_giorno03.rpy.


label daniel_3_festa:
    ## La festa privata organizzata da Daniel. Prima di entrare: l'indizio
    ## per il giocatore (scheda, sezione D).
    $ luogo_corrente = ""
    scene bg nero with fade
    call inizio_retroscena
    rs "Due giorni prima, un messaggio di Daniel a un vecchio amico:"
    rs "{i}«Sabato vieni. C'è una persona che deve conoscerti. Aspirante scrittrice. Fammi un favore: falla sentire speciale.»{/i}"
    $ retroscena("daniel", "L'incontro con l'editore alla festa non è un caso: l'ha organizzato Daniel.")
    call fine_retroscena

    $ vai("villa_daniel", "Villa di Daniel — sera")
    $ cg("Una villa sulla collina, musica dal vivo, bicchieri di cristallo; Sara stringe il braccio di [nome_compagno]")
    c "Non capisco perché ci abbia invitati. Non ha mai invitato nessuno dell'ufficio."
    $ via_cg()
    da "Sara! Che piacere. E [nome_compagno], ovviamente. Vieni, devo presentarti una persona."
    da "Mi hanno detto che scrivi."
    s "Chi... come lo sa?"
    da "Me l'avrà detto [nome_compagno]. Io ascolto, quando qualcosa mi interessa."
    $ cg("Un uomo più anziano di Daniel, elegante, occhiali sottili, un bicchiere di whisky")
    da "Lui è un mio vecchio amico. Pubblica romanzi, quando non ha di meglio da fare."
    $ incontra("editore")
    ed "Daniel esagera sempre. Lei scrive, signora? Che cosa?"
    $ via_cg()

    menu:
        sp "Un editore. Un editore vero."
        "Raccontargli il romanzo con entusiasmo.":
            $ interest("editore", 4, "L'editore ha visto la tua passione.")
            s "Un romanzo su una donna che trova una porta nel suo appartamento... una porta che prima non c'era."
            ed "E cosa c'è dietro?"
            s "È quello che sto cercando di capire. Da tre capitoli."
            ed "È la risposta più onesta che abbia sentito da uno scrittore da anni."
        "«Le mando le pagine domani stesso. Non se ne pentirà.»" (confidence=25):
            $ interest("editore", 5, "L'editore ama chi crede in se stesso.")
            $ confidence(2)
            s "Le mando le prime cinquanta pagine domani stesso. Non se ne pentirà."
            ed "Lo spero. Mi piace chi non chiede scusa per il proprio talento."
        "Restare sulle sue, per timidezza.":
            $ interest("editore", 2)
            s "Oh, niente di serio. Ci provo, nel tempo libero."
            ed "Tutti i romanzi seri cominciano come niente di serio."

    n "Daniel si allontana con [nome_compagno] verso il bar, lasciandoli soli. Non si volta nemmeno."
    $ retroscena("editore", "Daniel li ha lasciati soli senza pensarci: non vede l'amico come un rivale.")
    ed "Mi mandi le prime cinquanta pagine. Questo è il mio biglietto."
    sp "Si è ricordato che mi piace scrivere. Daniel."
    sp "Ah, però... non l'avrei mai detto."
    $ nota_sara("daniel", "Mi ha presentato un editore. Forse non è solo un arrogante.")
    $ nota_sara("editore", "Un editore vero vuole leggere le mie pagine.")
    $ tappa("daniel", 2)
    $ tappa("editore", 1)
    return
