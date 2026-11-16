## =============================================================================
## SIMON — il personal trainer (docs/personaggi/simon.md)
## =============================================================================
## Scene 1-5 della scheda. BOZZA: dialoghi provvisori.
## Regola della scheda: Simon resta professionale in palestra; l'affinità che
## cresce NON è attrazione romantica di Sara, per ora.

label simon_s1_prima_visita:
    ## Scena 1 — Prima visita in palestra con Joanie.
    $ vai("palestra", "Palestra — sera")
    $ cg("Sara sulla soglia, leggings nuovi e maglietta larga, si guarda intorno spaesata")
    ch "Respira. Nessuno ti morde."
    s "Joanie, qui sono tutti... scolpiti."
    ch "E tra poco lo sarai anche tu. Più o meno."
    $ via_cg()
    n "Joanie le dà una gomitata e indica con il mento il bancone degli istruttori."
    ch "E quello è Simon. Il motivo per cui non salto mai un allenamento."
    $ cg("Simon spiega un esercizio a un cliente: non altissimo, spalle larghe, sorriso facile")
    $ incontra("simon")
    sp "Non è altissimo. Ma le braccia..."
    sp "È decisamente più muscoloso di [nome_compagno]."
    $ via_cg()

    menu:
        ch "Allora? Dimmi che non è bello."
        "«È un bel ragazzo, sì.»":
            $ nota_sara("simon", "Un bel ragazzo. Lo ammette senza problemi.")
            ch "Visto? Sapevo che avevi ancora gli occhi."
        "«Sono qui per allenarmi, non per guardare.»":
            $ nota_sara("simon", "Bello, ma non le interessa. O così dice.")
            ch "Certo. E io ci vengo per il tapis roulant."
            sp "Non lo nego. Ma non è una cosa che mi riguarda."

    $ tappa("simon", 1)
    return


label simon_s2_correzioni:
    ## Scena 2 — Joanie chiede a Simon di correggerle gli esercizi.
    ## Stessa visita, momento diverso.
    n "Mezz'ora dopo Sara ha il fiatone. Joanie, invece, ha un piano."
    ch "Simon? Scusa... mi controlli lo squat? Credo di sbagliare qualcosa con la schiena."
    si "Certo. Fammi vedere."
    $ cg("Simon dietro Joanie: una mano sul fianco, l'altra tra le scapole, corregge la postura")
    si "Petto in fuori. Il peso sui talloni... così. Brava."
    ch "Così? Sei sicuro?"
    n "Joanie ride un po' troppo. Si appoggia un po' troppo."
    sp "Joanie è fidanzata. Da tre anni."
    sp "Lui è professionale, si vede. Ma lei..."

    menu:
        sp "Dove finisce una correzione e dove comincia un flirt?"
        "Distogliere lo sguardo: non sono affari suoi.":
            sp "Sono affari di Joanie. Non miei."
        "Continuare a guardare.":
            $ curiosita(2, "Sara si fa una domanda nuova.")
            $ segna("ep1_guarda_chiara")
            sp "Una mano sul fianco. Un'altra sulla schiena. È così che si fa?"
            sp "E se fosse stata la mia, di schiena?"

    $ via_cg()
    si "Ottimo lavoro, ragazze. E tu sei nuova, vero? Se ti serve una mano chiedi pure."
    s "Grazie. Per ora sopravvivo."
    si "Sopravvivere è il primo passo."
    $ nota_sara("simon", "Con Joanie è stato gentile, non ha approfittato.")
    return


label simon_s3_locale:
    ## Scena 3 — Incontro fuori dalla palestra, in un locale.
    $ vai("locale", "Locale — sabato sera")
    n "Sara, [nome_compagno] e Joanie hanno appena preso da bere quando qualcuno chiama Joanie dal bancone."
    si "Ehi! Le mie atlete!"
    $ cg("Simon in camicia, birra in mano, completamente diverso dall'istruttore della palestra")
    ch "Simon! Lui è [nome_compagno], il compagno di Sara."
    si "Piacere! Tienila d'occhio, eh: in palestra ha un potenziale spaventoso."
    c "Ah sì? Non me l'ha detto."
    s "Perché non è vero."
    si "Fidati di un professionista."
    $ via_cg()
    n "Simon resta con loro per un giro. Racconta aneddoti assurdi sui clienti, prende in giro se stesso, fa ridere perfino [nome_compagno]."
    sp "In palestra è tutto «petto in fuori» e «peso sui talloni». Qui sembra un altro."
    sp "Più... sciolto. Più simpatico."
    $ nota_sara("simon", "Fuori dalla palestra è spontaneo e divertente.")
    $ affinita("simon", 2)
    si "Vi lascio, mi aspettano. Sara: martedì niente scuse!"
    return


label simon_s4_chiara_cancella:
    ## Scena 4 — Joanie cancella all'ultimo minuto. BIVIO.
    $ vai("strada", "Davanti alla palestra — sera")
    n "Sara è davanti all'ingresso quando le arriva il messaggio."
    ch "{i}Scusascusascusa! Imprevisto con il mio ragazzo, non ce la faccio. Vai lo stesso!!{/i}"
    sp "Da sola. Il primo giorno ci sono sopravvissuta solo perché c'era lei."

    menu:
        sp "Entro o torno a casa?"
        "Entrare lo stesso.":
            $ segna("ep1_palestra_da_sola")
            sp "Ho pagato l'abbonamento. Entro."
        "Tornare a casa.":
            sp "Un'altra volta. Stasera no."
            $ vai("casa", "Casa — sera")
            c "Già di ritorno?"
            s "Joanie mi ha dato buca. Ho deciso che il divano era un allenamento sufficiente."
            c "Il divano ti ringrazia."
            $ legame(1)
    return


label simon_s5_allenamento:
    ## Scena 5 — Allenamento con Simon (solo se Sara è entrata).
    $ vai("palestra", "Palestra — sera")
    si "Ehi, la mia atleta! Tutta sola stasera?"
    s "Joanie mi ha abbandonata."
    si "Allora ti adotto io per mezz'ora. Ti va? Ti preparo una scheda da principiante, così la prossima volta sai cosa fare."
    $ cg("Simon mostra a Sara come impugnare il manubrio, a distanza professionale")
    si "Gomito vicino al corpo. Senza fretta. Il movimento conta più del peso."
    sp "Si ricorda di me. Si ricorda perfino come mi chiamo."
    si "Posso? Ti sistemo la spalla."

    menu:
        "«Certo.»":
            $ affinita("simon", 5, "Simon si ricorderà di questa serata.")
            n "Le sue dita le spostano appena la spalla. Un tocco tecnico, rapido."
            sp "Joanie ha ragione su una cosa: ha le mani sicure."
            sp "Ma è il suo lavoro. Niente di più."
        "«Faccio da sola, grazie. Dimmi tu come.»":
            $ affinita("simon", 3, "Simon rispetta i tuoi spazi.")
            si "Nessun problema. Abbassa la spalla... ecco, perfetto."
            $ nota_sara("simon", "Ha capito al volo che preferiva non essere toccata.")

    $ via_cg()
    si "Brava. Davvero. Martedì ti aspetto, con o senza Joanie."
    $ nota_sara("simon", "Simpatico. Carino. Fine della storia.")
    $ tappa("simon", 2)
    return
