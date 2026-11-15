## =============================================================================
## THE THIN LINE — ingresso del gioco
## =============================================================================

## Avviso iniziale, una volta per installazione.
label splashscreen:
    if not persistent.avviso_visto and not renpy.is_in_test():
        scene bg nero
        $ renpy.pause(0.5, hard=True)
        n "{b}The Thin Line{/b} è un'opera di finzione per un pubblico adulto.\n\nTutti i personaggi sono maggiorenni. Nomi, luoghi ed eventi sono immaginari."
        menu:
            "Ho almeno 18 anni e voglio continuare.":
                $ persistent.avviso_visto = True
            "Esci.":
                $ renpy.quit()
    return

default persistent.avviso_visto = False


label start:
    scene bg nero
    $ luogo_corrente = ""

    n "Prima di cominciare: Sara vive con il suo compagno."
    $ nome = renpy.input("Come si chiama? (Invio per «Marco»)", default="Marco", length=20).strip()
    $ nome_compagno = nome if nome else "Marco"

    menu:
        n "Da dove vuoi iniziare?"
        "Dall'inizio.":
            pass
        "Spiegami come funziona il gioco.":
            call istruzioni

    jump ep1_inizio


label istruzioni:
    n "In {b}The Thin Line{/b} segui Sara, e le sue scelte sono le tue."
    n "Lungo la storia Sara conosce persone diverse. Con ognuna si può costruire un percorso, lentamente, oppure si può ignorarlo. Puoi seguirne uno, più di uno o nessuno."
    n "Quando vedi la fascia {color=#ff9fb0}RETROSCENA{/color}, stai guardando qualcosa che Sara non sa. Lei non lo ricorderà; tu sì."
    n "Nel {b}Diario{/b} (menu rapido in basso) trovi, per ogni personaggio, cosa ne pensa Sara e cosa sai tu."
    n "Dalle Opzioni puoi mostrare o nascondere gli effetti delle scelte, e i numeri."
    return
