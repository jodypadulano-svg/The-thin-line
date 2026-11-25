## Il telefono per tipi e argomenti (specifica del 25/11/2026): soglie, scelta del tipo con
## anteprima, argomenti, chat in sospeso, limite giornaliero, scadenze.
## Nessun clic e nessun mouse: contatti, scelte e messaggi li guida il codice
## (telefono_pilota e i menu sostituiti), quindi il computer si può usare durante il test.
## Lancia con:  ... test telefono_tipi   (pochi secondi)

label test_telefono_tipi:
    call telefono_minuti_sessione(22 * 60, 23 * 60, "Go to bed")
    $ segna("test_telefono_tipi_finito")
    pause
    return

init python:
    _ttipi_scelte = []      # scelte del telefono, per inizio di frase
    _ttipi_risposta = 0     # quale risposta dare nelle chat (0, 1, 2)
    _ttipi_aperture = [0]   # quante volte si è aperta la rubrica
    _dm_vero = renpy.display_menu
    _ttipi_k = "howard"
    _ttipi_se = {}
    _ttipi_arrivo = _telefono_arrivo_minuti

    def _ttipi_menu_telefono(items, **kwargs):
        if not _ttipi_scelte:
            return [v for t, v in items if t.startswith("Pick up")][0]
        voluta = _ttipi_scelte.pop(0)
        for testo, valore in items:
            if testo.startswith(voluta):
                return valore
        raise AssertionError("Manca %s fra %s" % (voluta, [t for t, _ in items]))

    def _ttipi_menu_chat(items, **kwargs):
        """Le battute di Sara: la risposta chiesta, o l'ultima se ce ne sono meno."""
        risposte = [v for t, v in items if v is not None and t.startswith("«")]
        valore = risposte[min(_ttipi_risposta, len(risposte) - 1)]
        return getattr(valore, "value", valore)

    def _ttipi_pilota():
        """Apre il contatto finché ha qualcosa in corso; poi chiude. Mai più di 40 volte."""
        _ttipi_aperture[0] += 1
        if _ttipi_aperture[0] > 40:
            raise AssertionError("Il telefono non va avanti: %s" % store.discorso_aperto)
        if _ttipi_scelte or store._ttipi_k in store.discorso_aperto:
            return ("scrivi", store._ttipi_k)
        return ("chiudi", None)

    def _ttipi_prepara(scelte, risposta=0):
        debug_azzera_stato()
        store.giorno = 18
        store.giorno_entrata = 18
        store.rubrica = ["howard"]
        store._ttipi_k = "howard"
        store._ttipi_risposta = risposta
        _ttipi_scelte[:] = scelte
        _ttipi_aperture[0] = 0
        store.menu = _ttipi_menu_chat
        renpy.display_menu = _ttipi_menu_telefono
        store.telefono_pilota = _ttipi_pilota
        interest("howard", 6)
        segna("test_telefono_tipi_finito", False)

    def _ttipi_chiudi():
        renpy.display_menu = _dm_vero
        store.telefono_pilota = None
        for i, se in _ttipi_se.items():
            DISCORSI[i].se = se
        _ttipi_se.clear()
        store._telefono_arrivo_minuti = _ttipi_arrivo

    def _ttipi_subito(k):
        ## Daniel estrae a sorte anche il massimo: si sostituisce il calcolo intero.
        return store.telefono_minuti_ora

    def _ttipi_prepara_chat(id, risposta):
        d = DISCORSI[id]
        _ttipi_prepara([d.argomento or d.tipo, "«"], risposta)
        store._ttipi_k = d.chiave
        store.rubrica = [d.chiave]
        interest(d.chiave, 30)
        segna("bacio_" + d.chiave)
        if not d.argomento:
            store.anteprime_chat[(d.chiave, d.tipo)] = (store.giorno, id)
        _ttipi_se[id] = d.se
        d.se = None
        store._telefono_arrivo_minuti = _ttipi_subito

testsuite telefono_tipi:
    testcase soglie:
        $ debug_azzera_stato()
        $ giorno = 18
        $ interest("howard", 5)
        assert eval not tipo_aperto("howard", "Friendly")
        $ interest("howard", 1)
        assert eval tipo_aperto("howard", "Friendly") and not tipo_aperto("howard", "Flirt")
        $ interest("howard", 9)
        assert eval not tipo_aperto("howard", "Flirt")
        $ interest("howard", 1)
        assert eval tipo_aperto("howard", "Flirt") and not tipo_aperto("howard", "Sexting")
        $ segna("bacio_howard")
        assert eval tipo_aperto("howard", "Sexting")
        assert eval discorsi_di_tipo("howard", "Flirt") and discorsi_di_tipo("howard", "Sexting")
        ## Barbara ha baciato Sara quando ha firmato da stagista.
        $ sara_stagista = True
        assert eval tipo_aperto("capa", "Sexting")

    testcase regole:
        $ debug_azzera_stato()
        $ giorno = 14
        $ rubrica = ["howard", "daniel", "simon", "editore"]
        ## Casual è sempre aperto, e l'introduzione viene prima.
        assert eval [d.id for d in discorsi_di_tipo("howard", "Casual")] == ["howard_intro"]
        $ discorsi_fatti.append("howard_intro")
        assert eval len(discorsi_di_tipo("howard", "Casual")) >= 6 and valore_interest("howard") == 0
        ## Magnus ha due introduzioni: se ne gioca una sola.
        $ discorsi_fatti.append("editore_intro_attesa")
        $ segna("ep2_pagine_magnus")
        assert eval all("_intro" not in d.id for d in discorsi_disponibili("editore"))
        ## Daniel prende iniziative romantiche solo con Interest almeno pari al giorno.
        $ interest("daniel", 13)
        assert eval interesse_altrui("daniel") == "spento" and "daniel_b1" not in [d.id for d in discorsi_in_entrata("daniel")]
        $ interest("daniel", 1)
        assert eval interesse_altrui("daniel") == "acceso" and "daniel_b1" in [d.id for d in discorsi_in_entrata("daniel")]
        ## Una chat conclusa dal vivo o scaduta si chiude per sempre.
        $ discorso_aperto["howard"] = {"id": "howard_a6", "parte": 0, "giorno": 14}
        $ discorso_aperto["simon"] = {"id": "simon_a1", "parte": 0, "giorno": 14}
        $ chiudi_scadute()
        assert eval set(discorso_aperto) == {"howard", "simon"}
        $ giorno = 15
        $ segna("ep2_d17_ritiro_howard")
        $ chiudi_scadute()
        assert eval not discorso_aperto and {"howard_a6", "simon_a1"} <= set(discorsi_fatti)
        ## L'opzione che mostra il tipo è spenta all'inizio.
        assert eval tipo_chat_aperta() is None

    ## Ogni chat scritta in tools/telefono (argomenti, Flirt e Sexting di tutti), fino in
    ## fondo, con la prima, la seconda e la terza risposta. Qui si gioca il testo: attese a
    ## zero e condizioni di trama tolte.
    testcase chat_nuove:
        parameter chat = ["howard_t1", "howard_t2", "howard_t3", "howard_t4", "howard_t5", "howard_t6", "howard_t7", "howard_t8", "howard_t9", "howard_t10", "howard_t11", "howard_t12", "howard_t13", "howard_c1", "howard_c2", "howard_c3", "howard_d1", "howard_d2", "amica_t1", "amica_t2", "amica_t3", "amica_t4", "amica_t5", "amica_t6", "amica_t7", "amica_c1", "amica_c2", "amica_c3", "amica_d1", "amica_d2", "ex_t1", "ex_t2", "ex_t3", "ex_t4", "ex_c1", "ex_c2", "ex_d1", "ex_d2", "daniel_t1", "daniel_t2", "daniel_t3", "daniel_t4", "daniel_t5", "daniel_c1", "daniel_c2", "daniel_d1", "daniel_d2", "simon_t1", "simon_t2", "simon_t3", "simon_t4", "simon_t5", "simon_c1", "simon_c2", "simon_c3", "simon_d1", "simon_d2", "amico_t1", "amico_t2", "amico_t3", "amico_c1", "amico_c2", "amico_c3", "amico_d1", "amico_d2", "editore_t1", "editore_t2", "editore_t3", "editore_c1", "editore_c2", "editore_d1", "editore_d2", "capa_t1", "capa_t2", "capa_t3", "capa_t4", "capa_t5", "capa_c1", "capa_c2", "capa_c3", "capa_d1", "capa_d2"]
        parameter risposta = [0, 1, 2]
        $ _ttipi_prepara_chat(chat, risposta)
        run Jump("test_telefono_tipi")
        advance until eval fatto("test_telefono_tipi_finito") timeout 30.0
        $ _ttipi_chiudi()
        assert eval chat in discorsi_fatti and fatto("chat_" + chat)
        assert eval len(chat_log[_ttipi_k]) >= 5 and chat_log[_ttipi_k][0][0] == "sara"
        ## Senza attese la chat resta aperta: la rubrica si apre una volta e si chiude.
        assert eval _ttipi_aperture[0] == 2
        ## Gli argomenti non consumano la chat per tipo del giorno, Flirt e Sexting sì.
        assert eval (_ttipi_k in giorno_tipo) == (not DISCORSI[chat].argomento)

    ## Ogni chat che l'altro può aprire per primo: il messaggio aspetta nella rubrica,
    ## Sara risponde e la chat arriva in fondo.
    testcase entrate:
        parameter chat = ["amica_t1", "amica_t3", "amica_t4", "amica_t5", "amica_t7", "amica_c2", "amica_c3", "amico_t1", "amico_t2", "amico_t3", "amico_c1", "capa_t1", "capa_t2", "capa_t4", "daniel_t1", "daniel_t3", "daniel_t4", "daniel_t5", "daniel_c1", "daniel_c2", "editore_t1", "editore_t2", "ex_t1", "ex_t3", "ex_t4", "ex_c1", "ex_c2", "howard_t1", "howard_t2", "howard_t4", "howard_t5", "howard_t6", "howard_t8", "howard_t9", "howard_t10", "howard_t11", "howard_t12", "howard_c1", "howard_c2", "howard_c3", "simon_t1", "simon_t2", "simon_t3", "simon_t5", "simon_c1", "simon_c2", "amica_intro", "amica_b1", "amica_b4", "amico_intro", "amico_b1", "capa_b3", "daniel_intro", "daniel_b1", "editore_intro_pagine", "editore_intro_attesa", "ex_a2", "ex_b1", "ex_b4", "howard_a3", "howard_a6", "howard_a8", "howard_b1", "howard_b3", "simon_a1", "simon_a2", "simon_b1"]
        $ _ttipi_prepara_chat(chat, 0)
        $ _ttipi_scelte[:] = []
        $ telefono_minuti_ora = giorno * 1440 + 22 * 60
        $ arriva_messaggio(_ttipi_k, chat)
        $ _ttipi_prima = valore_interest(_ttipi_k)
        run Jump("test_telefono_tipi")
        advance until eval fatto("test_telefono_tipi_finito") timeout 30.0
        $ _ttipi_chiudi()
        assert eval chat in discorsi_fatti and fatto("chat_" + chat)
        assert eval chat_log[_ttipi_k][0][0] == _ttipi_k and "sara" in [m[0] for m in chat_log[_ttipi_k]]
        assert eval valore_interest(_ttipi_k) > _ttipi_prima

    ## La tabella di chi scrive per primo e le reazioni al silenzio.
    testcase sera_e_silenzi:
        $ debug_azzera_stato()
        $ giorno = 18
        $ giorno_entrata = -1
        $ telefono_minuti_ora = giorno * 1440 + 22 * 60
        $ rubrica = ["howard", "amica", "simon", "amico", "daniel", "ex"]
        $ segna("ep1_d12_visita")
        $ segna("jacob_tornato")
        $ segna("ep1_palestra_da_sola")
        $ [interest(k, 12) for k in rubrica]
        $ _ttipi_entrate = dict(ENTRATE)
        $ ENTRATE.update({k: (1.0, 1, {}) for k in ENTRATE})
        $ _telefono_messaggi_in_entrata()
        assert eval len(discorso_aperto) == ENTRATE_PER_SERA == 2
        ## Una volta sola per sera.
        $ _telefono_messaggi_in_entrata()
        assert eval len(discorso_aperto) == 2
        $ ENTRATE.update(_ttipi_entrate)
        ## Daniel sotto il giorno scrive solo del romanzo; Jacob solo di notte.
        $ discorso_aperto = {}
        $ telefono_minuti_inbox = {}
        $ ultima_entrata = {}
        $ segna("ep1_d13_biglietto")
        $ segna("ep2_d18_ballo")
        assert eval {d.id for d in _entrate_possibili("daniel")} <= set(DANIEL_ROMANZO)
        $ telefono_minuti_ora = giorno * 1440 + 21 * 60
        assert eval not _entrate_possibili("ex") and _entrate_possibili("simon")
        ## Silenzi: Howard insiste, Daniel sparisce finché non lo cerca lei.
        $ arriva_messaggio("howard", "howard_t4")
        $ arriva_messaggio("daniel", "daniel_t1")
        $ _telefono_silenzi()
        assert eval "silenzio" not in discorso_aperto["howard"] and not daniel_tace
        $ giorno = 19
        $ _telefono_silenzi()
        assert eval discorso_aperto["howard"]["silenzio"] and daniel_tace and "daniel" not in discorso_aperto
        assert eval not _entrate_possibili("daniel")
        $ telefono_minuti_ora = None

    testcase tipo_e_annulla:
        $ _ttipi_prepara(["Casual", "Not now", "Casual", "«"])
        $ _ttipi_id = discorso_pescato("howard", "Casual")
        run Jump("test_telefono_tipi")
        advance until eval fatto("test_telefono_tipi_finito") timeout 30.0
        $ _ttipi_chiudi()
        ## Annullare non consuma, la proposta resta la stessa, poi basta per oggi.
        assert eval discorsi_fatti == [_ttipi_id]
        assert eval giorno_tipo["howard"] == 18 and not discorsi_di_tipo("howard", "Friendly")

    testcase cambia_discorso:
        $ _ttipi_prepara(["Change the subject", "The sauce on the blouse", "«Howard. We need to talk"])
        $ segna("ep2_d18_cena_reggiseno")
        $ discorso_aperto["howard"] = {"id": "howard_a1", "parte": 0, "caldo": False, "frenato": False, "contesto_verificato": True, "premio_avvio": False}
        $ telefono_minuti_riprese["howard"] = "tel_chat_howard_a1_1_1"
        $ chat_log["howard"] = [("howard", "Are you still there?")]
        run Jump("test_telefono_tipi")
        advance until eval fatto("test_telefono_tipi_finito") timeout 30.0
        $ _ttipi_chiudi()
        assert eval "howard_t1" in discorsi_fatti and "howard_a1" in discorsi_fatti and not fatto("chat_howard_a1")
        assert eval chat_log["howard"][1][0] == "sara" and chat_log["howard"][2][1].startswith("Howard. We need")
