## =============================================================================
## DIARIO DI SARA
## =============================================================================
## Una pagina per ogni personaggio incontrato, divisa in due:
##   - "Cosa sa Sara": la sua impressione, come la scriverebbe lei;
##   - "Cosa sai tu":  i retroscena che il giocatore ha visto e lei no.
## È il cuore dell'ironia drammatica del gioco.

default diario_pagina = "sara"

init python:
    def descrizione_legame(v):
        if v >= 80: return "Innamoratissima."
        if v >= 60: return "Innamorata, ma qualcosa la turba."
        if v >= 40: return "Si sente lontana da lui."
        if v >= 20: return "La coppia è in crisi."
        return "Non sa più cosa prova."

    def descrizione_curiosita(v):
        if v >= 60: return "Ha voglia di scoprire chi può diventare."
        if v >= 30: return "Si fa domande che prima non si faceva."
        if v >= 10: return "Qualcosa ha acceso la sua curiosità."
        return "La sua vita le basta così com'è."

    def testo_tappa(p):
        lista = TAPPE.get(p.chiave, [])
        if 0 <= p.tappa < len(lista):
            return lista[p.tappa]
        return ""

screen diario():
    tag menu

    use game_menu(_("Diario"), scroll="viewport"):

        style_prefix "diario"

        vbox:
            spacing 24

            ## Indice delle pagine
            hbox:
                spacing 18
                box_wrap True
                textbutton "Sara" action SetVariable("diario_pagina", "sara")
                for chiave, p in sorted(percorsi.items(), key=lambda kv: kv[1].nome):
                    if p.incontrato:
                        textbutton p.nome action SetVariable("diario_pagina", chiave)

            if diario_pagina == "sara":
                use diario_sara
            else:
                use diario_personaggio(percorsi[diario_pagina])

screen diario_sara():
    vbox:
        spacing 14
        label "Sara"
        text "Con [nome_compagno]: " + descrizione_legame(sara_legame)
        text "Dentro di sé: " + descrizione_curiosita(sara_curiosita)
        if persistent.mostra_numeri:
            text "Legame [sara_legame]/100  ·  Curiosità [sara_curiosita]/100" color "#ffffff88"

        null height 10
        label "Cosa nasconde a [nome_compagno]"
        if segreti:
            for chiave, descrizione in segreti.items():
                text "• " + descrizione
        else:
            text "Niente. Per ora." color "#ffffff88"

screen diario_personaggio(p):
    vbox:
        spacing 14
        label p.nome
        text p.ruolo color "#ffffff99"
        if p.chiuso:
            text "Sara ha chiuso questa porta." color "#c8385a"
        else:
            text testo_tappa(p)
        if persistent.mostra_numeri:
            hbox:
                spacing 16
                bar value StaticValue(p.affinita, 100) xmaximum 500 yalign 0.5
                text "Affinità [p.affinita]/100 · tappa [p.tappa]" color "#ffffff88"

        null height 10
        label "Cosa sa Sara"
        if p.sa_sara:
            for riga in p.sa_sara:
                text "• " + riga
        else:
            text "Non ci ha ancora pensato." color "#ffffff88"

        null height 10
        label "Cosa sai tu"
        if p.sai_tu:
            for riga in p.sai_tu:
                text "• " + riga color "#ff9fb0"
        else:
            text "Niente che Sara non sappia." color "#ffffff88"

style diario_label_text:
    color "#c8385a"
    size 36

style diario_text:
    size 28

style diario_button_text:
    size 30
    idle_color "#ffffffaa"
    hover_color "#c8385a"
    selected_color "#ffffff"
