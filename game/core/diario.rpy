## =============================================================================
## DIARIO DI SARA
## =============================================================================
## Una pagina per ogni personaggio incontrato, divisa in due:
##   - "Cosa sa Sara": la sua impressione, come la scriverebbe lei;
##   - "Cosa sai tu":  i retroscena che il giocatore ha visto e lei no.
## È il cuore dell'ironia drammatica del gioco.

default diario_pagina = "sara"

init python:
    def descrizione_josh(v):
        if v >= 80: return "Head over heels."
        if v >= 60: return "In love, but something is bothering her."
        if v >= SOGLIA_GENTILE_CON_JOSH: return "She feels distant from him."
        return "She can't be sweet with him anymore."

    def descrizione_corruption(v):
        if v >= 75: return "She no longer recognises the woman she was."
        if v >= 45: return "She has crossed lines she swore she'd never touch."
        if v >= 15: return "She allows herself things she never used to."
        if v > 0: return "A few small cracks."
        return "True to herself and to him."

    def descrizione_suspicion(v):
        if v >= 60: return "He knows something is wrong."
        if v >= 30: return "He asks questions. Too many."
        if v > 0: return "Sometimes he looks at her strangely."
        return "He trusts her blindly."

    def descrizione_confidence(v):
        if v >= 70: return "She knows her worth and isn't afraid to show it."
        if v >= 40: return "She's starting to believe in herself."
        return "A dreamer who doesn't believe in herself enough."

    def testo_tappa(p):
        lista = TAPPE.get(p.chiave, [])
        if 0 <= p.tappa < len(lista):
            return lista[p.tappa]
        return ""

screen diario():
    tag menu

    use game_menu(_("Diary"), scroll="viewport"):

        style_prefix "diario"

        vbox:
            spacing 24

            ## Indice delle pagine
            hbox:
                spacing 18
                box_wrap True
                textbutton "Sara" action SetVariable("diario_pagina", "sara")
                for chiave, p in sorted(percorsi.items(), key=lambda kv: nome_percorso(kv[1])):
                    if p.incontrato:
                        textbutton nome_percorso(p) action SetVariable("diario_pagina", chiave)

            if diario_pagina == "sara":
                use diario_sara
            else:
                use diario_personaggio(percorsi[diario_pagina])

screen diario_sara():
    vbox:
        spacing 14
        label "Sara"
        use riga_variabile("Interest [nome_compagno]", interest_josh, "josh", descrizione_josh(interest_josh))
        use riga_variabile("Corruption", sara_corruption, "corruption", descrizione_corruption(sara_corruption))
        use riga_variabile("Confidence", sara_confidence, "confidence", descrizione_confidence(sara_confidence))
        use riga_variabile("[nome_compagno]'s Suspicion", josh_suspicion, "suspicion", descrizione_suspicion(josh_suspicion))

        null height 10
        label "What she hides from [nome_compagno]"
        if segreti:
            for chiave, descrizione in segreti.items():
                text "• " + descrizione
        else:
            text "Nothing. For now." color "#ffffff88"

        if segreti_trovati:
            null height 10
            label "Secrets found"
            for s in segreti_trovati:
                text "• " + s

        if persistent.finali_visti:
            null height 10
            label "Endings found"
            for f in persistent.finali_visti:
                text "• " + f

        null height 10
        label "Wardrobe"
        for a in abiti_sbloccati():
            text "• " + a.nome + " — " + a.descrizione

screen riga_variabile(nome, valore, chiave_colore, descrizione):
    vbox:
        spacing 4
        hbox:
            spacing 16
            text nome color COLORI[chiave_colore] min_width 380
            if persistent.numeri_visibili:
                bar value StaticValue(valore, 100) xmaximum 400 yalign 0.5
                text "[valore]/100" color "#ffffff88"
        text descrizione size 24 color "#ffffffaa"

screen diario_personaggio(p):
    vbox:
        spacing 14
        label nome_percorso(p)
        text ruolo_percorso(p) color "#ffffff99"
        if p.chiuso:
            text "Sara closed this door." color "#c8385a"
        else:
            text testo_tappa(p)
        if persistent.numeri_visibili:
            hbox:
                spacing 16
                text "Interest" color COLORI.get(p.chiave, "#ffffff") min_width 180
                bar value StaticValue(p.interest, 100) xmaximum 400 yalign 0.5
                text "[p.interest]/100" color "#ffffff88"
            if p.soglia:
                if sara_corruption >= p.soglia:
                    text "Enough Corruption to go further ([p.soglia])." color COLORI["corruption"]
                else:
                    text "To go further she needs Corruption [p.soglia]." color "#ffffff88"

        null height 10
        label "What Sara knows"
        if p.sa_sara:
            for riga in p.sa_sara:
                text "• " + riga
        else:
            text "She hasn't thought about it yet." color "#ffffff88"

        null height 10
        label "What you know"
        if p.sai_tu:
            for riga in p.sai_tu:
                text "• " + riga color "#ff9fb0"
        else:
            text "Nothing Sara doesn't know." color "#ffffff88"

style diario_label_text:
    color "#ffb3c1"
    size 36

style diario_text:
    size 28

style diario_button_text:
    size 30
    idle_color "#ffffffaa"
    hover_color "#c8385a"
    selected_color "#ffffff"
