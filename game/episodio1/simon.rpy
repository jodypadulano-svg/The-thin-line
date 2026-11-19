## =============================================================================
## SIMON — il personal trainer (docs/personaggi/simon.md)
## =============================================================================
## Scene 1-5 della scheda. BOZZA: dialoghi provvisori.
## Regola della scheda: Simon resta professionale in palestra; l'affinità che
## cresce NON è attrazione romantica di Sara, per ora.

## Scene 1-2 (prima visita, correzioni a Joanie): ora nel giorno 2,
## episodio1/ep1_giorno02.rpy.

## Scena 3 (il locale): ora nel giorno 6, episodio1/ep1_giorno06.rpy.


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
            $ confidence(3, "Sara entra da sola.")
        "Tornare a casa.":
            sp "Un'altra volta. Stasera no."
            $ vai("casa", "Casa — sera")
            c "Già di ritorno?"
            s "Joanie mi ha dato buca. Ho deciso che il divano era un allenamento sufficiente."
            c "Il divano ti ringrazia."
            $ interest("josh", 1)
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
            $ interest("simon", 5, "Simon si ricorderà di questa serata.")
            n "Le sue dita le spostano appena la spalla. Un tocco tecnico, rapido."
            sp "Joanie ha ragione su una cosa: ha le mani sicure."
            sp "Ma è il suo lavoro. Niente di più."
        "«Mi sistemi anche l'altra?», con un sorriso." (corruption=15):
            $ interest("simon", 6, "Simon ha notato il tuo sorriso.")
            $ corruption(3, "Un gioco innocente. Quasi.")
            s "Già che ci sei... mi sistemi anche l'altra?"
            si "Agli ordini."
            n "Questa volta le sue mani restano un secondo in più. Nessuno dei due lo fa notare."
            sp "Che cosa sto facendo?"
        "«Faccio da sola, grazie. Dimmi tu come.»":
            $ interest("simon", 3, "Simon rispetta i tuoi spazi.")
            si "Nessun problema. Abbassa la spalla... ecco, perfetto."
            $ nota_sara("simon", "Ha capito al volo che preferiva non essere toccata.")

    $ via_cg()
    si "Brava. Davvero. Martedì ti aspetto, con o senza Joanie."
    $ nota_sara("simon", "Simpatico. Carino. Fine della storia.")
    $ tappa("simon", 2)
    return
