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
        if v >= 80: return "Innamoratissima."
        if v >= 60: return "Innamorata, ma qualcosa la turba."
        if v >= SOGLIA_GENTILE_CON_JOSH: return "Si sente lontana da lui."
        return "Non riesce più a essere dolce con lui."

    def descrizione_corruption(v):
        if v >= 75: return "Non riconosce più la donna che era."
        if v >= 45: return "Ha superato confini che giurava di non toccare."
        if v >= 15: return "Si concede cose che prima non si concedeva."
        if v > 0: return "Qualche piccola crepa."
        return "Fedele a se stessa e a lui."

    def descrizione_suspicion(v):
        if v >= 60: return "Ha capito che qualcosa non va."
        if v >= 30: return "Fa domande. Troppe."
        if v > 0: return "Ogni tanto la guarda in modo strano."
        return "Si fida ciecamente."

    def descrizione_confidence(v):
        if v >= 70: return "Sa quanto vale e non ha paura di mostrarlo."
        if v >= 40: return "Comincia a credere in se stessa."
        return "Una sognatrice che non crede abbastanza in sé."

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
        use riga_variabile("Interest [nome_compagno]", interest_josh, "josh", descrizione_josh(interest_josh))
        use riga_variabile("Corruption", sara_corruption, "corruption", descrizione_corruption(sara_corruption))
        use riga_variabile("Confidence", sara_confidence, "confidence", descrizione_confidence(sara_confidence))
        use riga_variabile("Suspicion di [nome_compagno]", josh_suspicion, "suspicion", descrizione_suspicion(josh_suspicion))

        null height 10
        label "Cosa nasconde a [nome_compagno]"
        if segreti:
            for chiave, descrizione in segreti.items():
                text "• " + descrizione
        else:
            text "Niente. Per ora." color "#ffffff88"

        if segreti_trovati:
            null height 10
            label "Segreti trovati"
            for s in segreti_trovati:
                text "• " + s

        null height 10
        label "Guardaroba"
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
        label p.nome
        text p.ruolo color "#ffffff99"
        if p.chiuso:
            text "Sara ha chiuso questa porta." color "#c8385a"
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
                    text "Corruption sufficiente per andare oltre ([p.soglia])." color COLORI["corruption"]
                else:
                    text "Per andare oltre serve Corruption [p.soglia]." color "#ffffff88"

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
