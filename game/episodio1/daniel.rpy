## =============================================================================
## DANIEL — il capo del compagno (docs/personaggi/daniel.md)
## L'EDITORE — incrocio di percorsi (docs/personaggi/editore.md)
## =============================================================================
## Tre incontri della scheda. BOZZA: dialoghi provvisori.
## Regola della scheda: il giocatore capisce il piano di Daniel, Sara no.

label daniel_1_cena_aziendale:
    $ vai("ristorante", "Ristorante — cena aziendale")
    c "Daniel, ti presento Sara."
    $ cg("Daniel si alza: completo scuro, sorriso da copertina, stretta di mano lunga un istante di troppo")
    da "Sara. Finalmente. Lui parla poco di te, adesso capisco perché: ti tiene nascosta."
    $ incontra("daniel")
    s "Piacere mio."
    $ via_cg()

    call inizio_retroscena
    $ cg("Lo sguardo di Daniel scivola sul vestito di Sara mentre lei si siede")
    rs "Daniel la guarda sedersi. Non ascolta quello che dice il dipendente al suo fianco."
    $ retroscena("daniel", "Alla cena Daniel ha notato Sara, e non come la moglie di un dipendente.")
    $ via_cg()
    call fine_retroscena

    n "La serata comincia bene. Poi, tra l'antipasto e il primo, Daniel comincia a punzecchiare."
    da "Il nostro [nome_compagno] è il più puntuale dell'ufficio. Peccato che arrivi puntuale anche con i problemi."
    n "Qualche risata. [nome_compagno] sorride a fatica."
    da "No, sul serio, Sara. Come hai fatto? Una donna come te con... un uomo così prudente. Ti avrà conquistata con un foglio Excel."

    menu:
        sp "Basta. Non posso lasciarlo passare."
        "Rispondergli a tono.":
            s "Mi ha conquistata trattandomi con rispetto. Cosa che a quanto pare non si impara in tutti i lavori."
            da "Touché. Vedi? Lei sì che ha carattere. Forse dovresti farti prestare un po' del suo, in ufficio."
            sp "L'ha ribaltata di nuovo. Come fa?"
            $ affinita("daniel", 2, "A Daniel piace chi gli tiene testa.")
            $ retroscena("daniel", "Più Sara gli tiene testa, più Daniel si diverte.")
        "Prendere la mano di [nome_compagno] sotto il tavolo.":
            $ legame(2, "[nome_compagno] sente la tua mano.")
            n "Sara non dice niente. Stringe la mano di [nome_compagno] sotto il tovagliolo."
            da "Che tenerezza. Lui ha bisogno di sostegno, eh?"
        "Cambiare discorso con eleganza.":
            s "Parliamo d'altro? Il vino è ottimo, chi l'ha scelto?"
            da "Io. Ovviamente."
            sp "Ovviamente."

    n "Il resto della cena va avanti così. Ogni battuta di Daniel sembra quasi ragionevole. Ogni volta [nome_compagno] incassa in silenzio."
    sp "Non l'ho mai visto così. Lui, che mi ha sempre fatta sentire protetta."
    $ nota_sara("daniel", "Uno spaccone arrogante. Ha umiliato [nome_compagno] tutta la sera.")

    $ vai("strada", "In macchina — notte")
    n "In macchina, il silenzio pesa."
    menu:
        sp "Cosa gli dico?"
        "Consolarlo: «È lui il problema, non tu.»":
            $ legame(3, "Sara sta dalla parte di [nome_compagno].")
            s "È lui il problema. Non tu. È un pallone gonfiato."
            c "È il mio capo, Sara. Non posso permettermi di rispondergli."
        "Chiedergli perché non ha reagito.":
            $ legame(-2)
            $ curiosita(1)
            s "Perché non gli hai detto niente? Neanche una parola."
            c "E cosa avrei dovuto dirgli? Lui firma il mio contratto."
            sp "Ha ragione. Eppure..."
    $ tappa("daniel", 1)
    return


label daniel_2_patente:
    ## La patente dimenticata (oggetto provvisorio, vedi scheda).
    $ vai("ufficio_compagno", "Ufficio di [nome_compagno] — mattina")
    n "[nome_compagno] ha dimenticato la patente sul mobile dell'ingresso. Sara gliela porta prima che debba usare l'auto aziendale."
    c "Sei un angelo. Non so come avrei fatto..."
    da "Io lo so: avrebbe chiamato un taxi e messo la ricevuta in nota spese. Buongiorno, Sara."
    $ cg("Daniel appoggiato allo stipite, caffè in mano, sguardo divertito")
    da "Ci tieni a sapere quanto è affidabile il tuo uomo? Ha dimenticato la patente. Lui, che guida per lavoro."
    c "È capitato una volta, Daniel..."
    da "Una volta è il primo indizio. Fortuna che a casa c'è qualcuno che pensa per due."
    $ via_cg()
    sp "Quanto è arrogante oggi."
    s "Buona giornata a tutti e due."
    $ nota_sara("daniel", "Arrogante anche di giorno. Non perde un'occasione.")
    $ retroscena("daniel", "Daniel umilia [nome_compagno] soprattutto quando Sara è presente.")
    return


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
            $ affinita("editore", 4, "L'editore ha visto la tua passione.")
            s "Un romanzo su una donna che trova una porta nel suo appartamento... una porta che prima non c'era."
            ed "E cosa c'è dietro?"
            s "È quello che sto cercando di capire. Da tre capitoli."
            ed "È la risposta più onesta che abbia sentito da uno scrittore da anni."
        "Restare sulle sue, per timidezza.":
            $ affinita("editore", 2)
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
