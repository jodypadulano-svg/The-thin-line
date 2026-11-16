## =============================================================================
## THE THIN LINE — ingresso del gioco
## =============================================================================

## Avviso iniziale, una volta per installazione.
label splashscreen:
    if not persistent.avviso_visto and not renpy.is_in_test():
        scene bg nero
        $ renpy.pause(0.5, hard=True)
        n "{b}The Thin Line{/b} is a work of fiction intended for adults.\n\nAll characters are 18 or older. Names, places and events are fictional."
        menu:
            "I am 18 or older and want to continue.":
                $ persistent.avviso_visto = True
            "Quit.":
                $ renpy.quit()
    return

default persistent.avviso_visto = False


label start:
    scene bg nero
    $ luogo_corrente = ""

    n "Before we begin: Sara lives with her boyfriend."
    $ nome = renpy.input("What is his name? (Press Enter for «Josh»)", default="Josh", length=20).strip()
    $ nome_compagno = nome if nome else "Josh"

    menu:
        n "How do you want to start?"
        "From the beginning.":
            pass
        "Explain how the game works.":
            call istruzioni

    jump ep1_inizio


label istruzioni:
    n "In {b}The Thin Line{/b} you follow Sara, and her choices are yours."
    n "Along the way Sara meets different people. With each of them a path can slowly grow, or be ignored. You can follow one, several, or none."
    n "When you see the {color=#ff9fb0}BEHIND THE SCENES{/color} banner, you are watching something Sara doesn't know. She won't remember it; you will."
    n "In the {b}Diary{/b} (quick menu at the bottom) you'll find, for each character, what Sara thinks of them and what you know."
    n "In the Options you can show or hide the effects of your choices, and the numbers."
    return
