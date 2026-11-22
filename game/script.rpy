## =============================================================================
## THE THIN LINE — ingresso del gioco
## =============================================================================

## Avviso iniziale, una volta per installazione.
label splashscreen:
    if not persistent.avviso_visto and not renpy.is_in_test():
        scene bg nero
        $ renpy.pause(0.5, hard=True)
        n "{b}Content Notice · 18+{/b}\n\n{b}The Thin Line{/b} is a work of fiction intended for adults. All characters are 18 or older. The game contains sexual themes, infidelity, manipulation, and uncomfortable relationship dynamics."
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

    call nota_autrice

    n "Before we begin: Sara lives with her boyfriend."
    $ nome = renpy.input("What is his name? (Press Enter for «Josh»)", default="Josh", length=20).strip()
    $ nome_compagno = nome if nome else "Josh"

    menu:
        n "How do you want to start?"
        "From the beginning.":
            pass
        "Explain how the game works.":
            call istruzioni
        "(Debug) Start from a later day." if config.developer:
            call debug_partenza

    jump ep1_inizio


label nota_autrice:
    call screen schermata_nota_autrice
    return


screen schermata_nota_autrice():
    modal True
    zorder 150

    add Solid("#171016")

    vbox:
        align (0.5, 0.5)
        xsize 1120
        spacing 26

        text "A note from the creator":
            font gui.interface_text_font
            size 56
            color "#f3e2e5"
            bold True

        text "I'm Laura Fatal, the woman behind {i}The Thin Line{/i}. After playing so many visual novels, I wanted to make one of my own, with a rhythm and choices that felt different from the games I'd played. Sara's story is a slow burn. I hope you enjoy spending time in her world." style "nota_autrice_testo"

        text "The phone is one of the parts I'm most excited about. You'll see it in story scenes from the start. From Episode 2, you'll be able to choose who Sara texts and when. Those conversations can deepen specific relationships and open scenes along the routes you choose to follow." style "nota_autrice_testo"

        text "I'd love to hear what you think as the story grows. Tell me which moments stayed with you, which choices you wished you'd had, and what you'd like to try. Your feedback could help shape parts of the story and give me ideas for new ways to make it interactive. Thanks for giving my game a try." style "nota_autrice_testo"

        text "— Laura Fatal" style "nota_autrice_testo":
            color "#e8a3b8"
            italic True

        textbutton "Continue":
            xalign 1.0
            xminimum 220
            padding (28, 12)
            background Solid("#673249")
            hover_background Solid("#87455f")
            text_xalign 0.5
            text_size 34
            text_color "#fff1f4"
            default_focus True
            action Return()


style nota_autrice_testo:
    font gui.interface_text_font
    size 34
    color "#eee2e6"
    line_spacing 4


label istruzioni:
    n "In {b}The Thin Line{/b} you follow Sara, and her choices are yours."
    n "Along the way Sara meets different people. With each of them a path can slowly grow, or be ignored. You can follow one, several, or none."
    n "When you see the {color=#ff9fb0}BEHIND THE SCENES{/color} banner, you are watching something Sara doesn't know. She won't remember it; you will."
    n "In the {b}Diary{/b} (quick menu at the bottom) you'll find, for each character, what Sara thinks of them and what you know."
    n "In the Options you can show or hide the effects of your choices, and the numbers."
    return
