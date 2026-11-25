## Il telefono per tipi e argomenti (specifica del 25/11/2026): scelta del tipo con
## anteprima, argomento specifico, chat in sospeso, limite giornaliero, soglie 5 e 15.
## Lancia con:  ... test telefono_tipi   (pochi secondi)

label test_telefono_tipi:
    call telefono_minuti_sessione(22 * 60, 23 * 60, "Go to bed")
    $ segna("test_telefono_tipi_finito")
    pause
    return

init python:
    _ttipi_scelte = []
    def _ttipi_menu(items, **kwargs):
        """Sceglie per inizio di frase; le battute di chat prendono la prima risposta."""
        if any(isinstance(v, tuple) or v in ("riprendi", "saluta", "cambia", "indietro", True, False) for _, v in items):
            voluta = _ttipi_scelte.pop(0)
            for testo, valore in items:
                if testo.startswith(voluta):
                    return valore
            raise AssertionError("Manca %s fra %s" % (voluta, [t for t, _ in items]))
        valore = [v for _, v in items if v is not None][0]
        return getattr(valore, "value", valore)

    def _ttipi_prepara(scelte):
        debug_azzera_stato()
        store.giorno = 18
        store.giorno_entrata = 18
        store.rubrica = ["howard"]
        _ttipi_scelte[:] = scelte
        store.menu = _ttipi_menu
        renpy.display_menu = _ttipi_menu

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
        ## Il tipo Flirt non si mostra finché non ha chat scritte.
        assert eval not discorsi_di_tipo("howard", "Flirt") and discorsi_di_tipo("howard", "Casual")
        assert eval len({d.id for d in DISCORSI.values()}) == len(DISCORSI)

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

    testcase argomento:
        $ _dm = renpy.display_menu
        $ _ttipi_prepara(["The sauce on the blouse", "«Howard. We need to talk", "Back to messages"])
        $ interest("howard", 6)
        $ segna("ep2_d18_cena_reggiseno")
        $ segna("test_telefono_tipi_finito", False)
        run Jump("test_telefono_tipi")
        advance until screen "telefono" timeout 20.0
        click "Howard"
        advance until eval "howard_t1" in discorsi_fatti timeout 60.0
        assert eval len(chat_log["howard"]) >= 14
        assert eval fatto("chat_howard_t1") and not argomenti_disponibili("howard")
        ## Un argomento non consuma la chat per tipo del giorno.
        assert eval "howard" not in giorno_tipo and discorsi_di_tipo("howard", "Casual")
        $ renpy.display_menu = _dm

    testcase tipo_e_annulla:
        $ _dm = renpy.display_menu
        $ _ttipi_prepara(["Casual", "Not now", "Casual", "«", "Back to messages"])
        $ interest("howard", 6)
        $ _ttipi_id = discorso_pescato("howard", "Casual")
        $ segna("test_telefono_tipi_finito", False)
        run Jump("test_telefono_tipi")
        advance until screen "telefono" timeout 20.0
        click "Howard"
        advance until eval discorsi_fatti == [_ttipi_id] timeout 60.0
        ## Annullare non consuma, la proposta resta la stessa, poi basta per oggi.
        assert eval giorno_tipo["howard"] == 18 and not discorsi_di_tipo("howard", "Friendly")
        $ renpy.display_menu = _dm

    testcase cambia_discorso:
        $ _dm = renpy.display_menu
        $ _ttipi_prepara(["Change the subject", "The sauce on the blouse", "«Howard. We need to talk"])
        $ interest("howard", 6)
        $ segna("ep2_d18_cena_reggiseno")
        $ discorso_aperto["howard"] = {"id": "howard_a1", "parte": 0, "caldo": False, "frenato": False, "contesto_verificato": True, "premio_avvio": False}
        $ telefono_minuti_riprese["howard"] = "tel_chat_howard_a1_1_1"
        $ chat_log["howard"] = [("howard", "Are you still there?")]
        $ segna("test_telefono_tipi_finito", False)
        run Jump("test_telefono_tipi")
        advance until screen "telefono" timeout 20.0
        click "Howard"
        advance until eval "howard_t1" in discorsi_fatti timeout 60.0
        assert eval "howard_a1" in discorsi_fatti and not fatto("chat_howard_a1")
        assert eval chat_log["howard"][1][0] == "sara" and chat_log["howard"][2][1].startswith("Howard. We need")
        $ renpy.display_menu = _dm
