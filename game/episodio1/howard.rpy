## =============================================================================
## HOWARD — il vicino di casa (docs/personaggi/howard.md)
## =============================================================================
## Tre incontri della scheda. BOZZA: dialoghi provvisori.
## Regola della scheda: per Sara è un vicino strano ma innocuo; il giocatore
## deve capire sempre di più, senza scene esplicite.

label howard_1_pianerottolo:
    $ vai("pianerottolo", "Pianerottolo — mattina")
    n "Sara chiude la porta di casa, la patente di [nome_compagno] nella borsa, e quasi inciampa nel vicino."
    $ cg("Howard in vestaglia sul pianerottolo, il giornale in mano, la porta di casa sua socchiusa")
    $ incontra("howard")
    ho "Oh! Buongiorno, Sara. Scusa, scusa... ti ho spaventata?"
    s "Buongiorno, Howard. No, sono io che vado di corsa."
    ho "Sempre di corsa, voi giovani. Io invece... be', io ho tutto il tempo del mondo."
    n "Ride da solo, un po' troppo a lungo."
    $ via_cg()

    menu:
        sp "Ha voglia di chiacchierare. Come sempre."
        "Fermarsi un minuto con lui.":
            $ affinita("howard", 2, "Howard ha apprezzato il tuo minuto.")
            s "Come va la schiena?"
            ho "Ti sei ricordata! Meglio, meglio. Sei sempre così gentile, tu."
            ho "Se ti serve qualcosa, qualsiasi cosa, io sono qui accanto. Lo sai."
        "Tagliare corto: è in ritardo.":
            s "Scusa Howard, devo proprio scappare!"
            ho "Certo, certo... vai pure."
            n "Quando Sara si volta all'angolo delle scale, lui è ancora lì sul pianerottolo, il giornale chiuso in mano."

    $ nota_sara("howard", "Il vicino un po' strano. Solo, ma gentile.")
    $ tappa("howard", 1)
    return


label howard_2_spesa:
    $ vai("pianerottolo", "Pianerottolo — mattina")
    n "Quattro borse della spesa, tre piani di scale, nessun ascensore."
    ho "Lascia, lascia! Ci penso io."
    s "Howard, non serve..."
    ho "Insisto. A cosa servono i vicini?"
    $ vai("casa", "Casa di Sara — mattina")
    n "Howard posa le borse sul tavolo della cucina. Sara sistema la roba in frigo, voltandogli le spalle."
    s "Grazie davvero. Vuoi un caffè?"
    ho "No, no, ti ho già disturbata abbastanza."

    call inizio_retroscena
    $ cg("Il cesto del bucato pulito sulla sedia accanto alla porta; la mano di Howard")
    rs "Sara ha la testa nel frigo. Howard guarda il cesto del bucato accanto alla porta."
    rs "Un movimento rapido. Qualcosa di piccolo e di pizzo scompare nella tasca della sua giacca."
    rs "Quando Sara si volta, lui è già sulla soglia, con il suo sorriso impacciato."
    $ retroscena("howard", "Ha rubato un capo di biancheria intima di Sara dal cesto del bucato.")
    $ via_cg()
    call fine_retroscena

    ho "Buona giornata, Sara. Davvero... buona giornata."
    n "Quella sera, piegando il bucato, Sara cerca una cosa che non trova."
    sp "Strano. Sarà rimasto in lavatrice. O l'ho messo da un'altra parte."
    sp "Pazienza."
    $ affinita("howard", 1)
    return


label howard_3_chiusa_fuori:
    ## Howard ha preparato tutto. Il giocatore lo sa dall'inizio (decisione
    ## definitiva della scheda); il meccanismo esatto è ancora da decidere.
    $ luogo_corrente = ""
    scene bg nero with fade
    call inizio_retroscena
    rs "Mattina. [nome_compagno] esce per un turno lungo: non tornerà prima delle otto."
    rs "Howard lo sa. Howard sa sempre a che ora escono e a che ora rientrano."
    ## PROVVISORIO: il meccanismo è da decidere (scheda, sezione D).
    rs "Dalla sua tasca spunta un piccolo attrezzo di metallo. La serratura di Sara non è mai stata un problema."
    $ retroscena("howard", "Ha fatto in modo che Sara restasse chiusa fuori di casa. Conosce gli orari della coppia.")
    call fine_retroscena

    $ vai("pianerottolo", "Pianerottolo — pomeriggio")
    n "La chiave entra. Ma non gira."
    s "No, no, no... dai!"
    sp "[nome_compagno] non torna prima delle otto. Ed è l'una."
    ho "Problemi con la serratura? Oh, povera. Succede, in questo palazzo. È tutto vecchio."
    ho "Vieni da me ad aspettarlo. Non puoi restare qui sul pianerottolo per sette ore."
    sp "Sette ore. Non ho alternative."

    $ vai("casa_howard", "Casa di Howard — pomeriggio")
    $ cg("Un soggiorno buio e soffocante: pile di giornali, piatti sporchi, tende chiuse")
    sp "Oddio. Non respirare con il naso, Sara. E sorridi."
    ho "Scusa il disordine. Non viene mai nessuno, sai."
    $ via_cg()
    n "Howard non le chiede niente. Prepara un caffè in tazze sbeccate e parla. Della solitudine. Delle cene davanti alla televisione. Della donna che non ha mai avuto."
    ho "Sai, alla mia età uno smette di sperare. Ti alzi, mangi, guardi la tv, vai a letto. E domani uguale."
    n "Poi la voce gli si incrina. Si copre il viso con le mani."

    call inizio_retroscena
    rs "Tra le dita, gli occhi di Howard sono asciutti. La osserva."
    $ retroscena("howard", "Il pianto era finto: voleva la compassione di Sara.")
    call fine_retroscena

    sp "Povero Howard. Sta piangendo davvero."
    sp "Nessuno dovrebbe essere così solo."
    s "Ehi... Howard. Va tutto bene. Non sei solo, ci siamo noi qui accanto."
    $ nota_sara("howard", "È un uomo solo. Le fa una tenerezza enorme.")
    n "Alle otto passate, la chiave di [nome_compagno] gira nella serratura del pianerottolo."

    ho "Sara... è stato bello, oggi. Parlare con qualcuno. Potremmo... vederci ogni tanto? Anche solo un caffè. Due chiacchiere."

    ## PROVVISORIO: la scheda non ha ancora deciso opzioni ed effetti di questo bivio.
    menu:
        sp "Cosa gli rispondo?"
        "«Certo, Howard. Un caffè ogni tanto.»":
            $ affinita("howard", 5, "Howard non dimenticherà questa risposta.")
            $ segna("ep1_howard_caffe", "si")
            ho "Davvero? Oh... grazie. Grazie, Sara."
        "«Quando capita, volentieri.»":
            $ affinita("howard", 2)
            $ segna("ep1_howard_caffe", "forse")
            ho "Quando capita. Certo. Io sono sempre qui."
        "«Scusami Howard, ho davvero poco tempo.»":
            $ segna("ep1_howard_caffe", "no")
            ho "Capisco. Capisco benissimo."
            call inizio_retroscena
            rs "Quando la porta si chiude, Howard resta a fissarla a lungo."
            $ retroscena("howard", "Il rifiuto non l'ha fermato. L'ha solo reso più paziente.")
            call fine_retroscena

    $ tappa("howard", 2)
    return
