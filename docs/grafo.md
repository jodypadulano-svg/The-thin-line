# The Thin Line — Grafo del gioco

Aggiornato al 17 novembre 2026 (giorni 1-2 riscritti in inglese; il resto dopo il lotto A1-A10) · Episodio 1 (versione 0.1.0-dev). Si aggiorna a ogni lotto di decisioni applicato ([regole](regole-di-lavoro.md), punto 2).

**Legenda**
- Rettangolo: scena · Rombo: bivio del giocatore · Esagono: retroscena (il giocatore lo vede, Sara no) · Rettangolo tratteggiato: scena condizionata
- Colori: 🟩 Simon · 🟪 Daniel · 🟫 Howard · 🟨 editore · 🟦 trama principale con Josh · 🟥 segreti e retroscena
- `Simon+5` = Interest verso Simon · `Josh+3` = Interest verso Josh · `Corr` = Corruption · `Conf` = Confidence · `Susp` = Suspicion · 🔒 = frase con requisito (A3) · `P` = bivio provvisorio

## Episodio 1

```mermaid
flowchart TD
    classDef main fill:#1f3a5f,stroke:#8fb3e0,color:#fff
    classDef simon fill:#1f4d3a,stroke:#7fd1a8,color:#fff
    classDef daniel fill:#3d2a5c,stroke:#c9a0ff,color:#fff
    classDef howard fill:#4a3f2c,stroke:#b5a48a,color:#fff
    classDef editore fill:#5a4a24,stroke:#d4b483,color:#fff
    classDef retro fill:#5c1f2e,stroke:#ff9fb0,color:#fff
    classDef scelta fill:#2a2a2a,stroke:#ffffff,color:#fff
    classDef cond fill:#1f4d3a,stroke:#7fd1a8,color:#fff,stroke-dasharray:5 5

    START([Avviso 18+ · nome di Josh]):::main

    subgraph G1 [Giorno 1 · Lunedì · riscritto in inglese]
        A1[Mattina: l'armadio e lo specchio]:::main
        A1C{Un bottone aperto? sì: Conf+1}:::scelta
        R1[Redazione: Barbara, Roberta, Jessica · I21 I22]:::main
        R1C{Rimprovero di Barbara<br/>spiegare: Conf+1 · battuta: Conf+1 Barbara+1}:::scelta
        R1S{Commento sulla scollatura<br/>«Grazie... credo»: Barbara+1}:::scelta
        R1J{★ Aperitivo di giovedì con le colleghe?}:::scelta
        P1[Prologo a casa: Sara scrive, arriva Josh]:::main
        P1C{★ Serata con Josh 🔒Josh 30: Josh+3<br/>o scrivere: Conf+2}:::scelta
        P1D{Cena: risotto Josh+1 · pizza}:::scelta
        P1T[Joanie la iscrive in palestra]:::main
        P1TC{Entusiasta: Joanie+1 · sbuffando}:::scelta
    end

    subgraph G2 [Giorno 2 · Martedì · riscritto in inglese]
        R2[Redazione: giornata normale]:::main
        R2C{Pausa pranzo<br/>colleghe · scrivere: Conf+1 · messaggi a Josh: Josh+1}:::scelta
        S0{Cosa indossare<br/>maglietta larga · top di Joanie: Conf+1 Corr+1}:::scelta
        S1[Simon 1 · prima visita con Joanie]:::simon
        S1C{È bello?}:::scelta
        S1S{Simon la saluta<br/>sorridere: Simon+1 · cenno}:::scelta
        S2[Simon 2 · Joanie flirta mentre lui la corregge]:::simon
        S2C{Guardare o no?<br/>guardare: Corr+1}:::scelta
        INV[Josh: invito alla cena aziendale di domani]:::main
        INVC{Entusiasta: Josh+1 · preoccupata per Daniel}:::scelta
    end

    subgraph G3 [Giorno 3 · La cena aziendale]
        D1[Daniel 1 · cena aziendale]:::daniel
        D1R{{Daniel guarda Sara}}:::retro
        D1C{Reazione alle battute P<br/>a tono: Daniel+2 · mano a Josh: Josh+2}:::scelta
        D1A{In auto P<br/>consolare: Josh+3 · perché? Josh-2}:::scelta
    end

    subgraph G4 [Giorno 4 · Una mattina di corsa]
        H1[Howard 1 · pianerottolo]:::howard
        H1C{Fermarsi? P<br/>sì: Howard+2}:::scelta
        D2[Daniel 2 · la patente in ufficio]:::daniel
    end

    subgraph G5 [Giorno 5 · Sabato]
        H2[Howard 2 · la spesa]:::howard
        H2R{{Furto: biancheria + chiavi}}:::retro
        S3[Simon 3 · al locale con Joanie e Josh · Simon+2]:::simon
    end

    subgraph G6 [Giorno 6 · Da sola]
        S4[Simon 4 · Joanie dà buca]:::simon
        S4C{Entrare o tornare a casa?}:::scelta
        S5[Simon 5 · allenamento con Simon<br/>Simon+3/+5 · 🔒Corr 15: Simon+6 Corr+3]:::cond
        CASA6[A casa con Josh · Josh+1]:::main
    end

    subgraph G7 [Giorno 7 · Chiusa fuori]
        H3R{{Howard sa che Josh fa il turno lungo}}:::retro
        H3[Howard 3 · senza chiavi, ospite da Howard]:::howard
        H3P{{Il pianto è finto}}:::retro
        H3C{Vederci più spesso? P<br/>sì: +5 · forse: +2 · no: 0, percorso aperto}:::scelta
    end

    subgraph G8 [Giorno 8 · La festa]
        D3R{{Daniel ha organizzato l'incontro}}:::retro
        D3[Daniel 3 · festa in villa]:::daniel
        ED[L'editore · primo incontro]:::editore
        EDC{Entusiasmo o timidezza? P<br/>editore +4/+2 · 🔒Conf 25: editore+5 Conf+2}:::scelta
        FIN[Finale a casa]:::main
        FINC{Dire a Josh dell'editore? P}:::scelta
        SEG[/Segreto: biglietto dell'editore · Corr+2 Susp+3/]:::retro
        FINR{{Messaggio dell'editore a Daniel}}:::retro
    end

    START --> A1 --> A1C --> R1 --> R1C --> R1S --> R1J --> P1 --> P1C --> P1D --> P1T --> P1TC
    P1TC --> R2 --> R2C --> S0 --> S1 --> S1C --> S1S --> S2 --> S2C --> INV --> INVC --> D1
    D1 --> D1R --> D1C --> D1A --> H1 --> H1C --> D2 --> H2 --> H2R --> S3 --> S4 --> S4C
    S4C -- entra: Conf+3 --> S5 --> H3R
    S4C -- torna --> CASA6 --> H3R
    H3R --> H3 --> H3P --> H3C --> D3R --> D3 --> ED --> EDC --> FIN --> FINC
    FINC -- lo dice 🔒Josh 30: Josh+2 --> FINR
    FINC -- lo tiene per sé --> SEG --> FINR
    FINR --> FINE([Fine Episodio 1])

    %% Collegamenti tra percorsi
    H2R -. le chiavi servono il giorno 7 .-> H3
    D3 -. Daniel presenta un potenziale rivale .-> ED
    S5 -. se taciuto, Sara ci ripensa nel finale .-> FIN
    S2 -. Joanie · percorso 5, molto più avanti .-> S2C
```

## Stato a fine Episodio 1

| Percorso | Tappa massima | Interest massimo | Soglia Corruption | Note |
|---|---|---|---|---|
| Simon | 2 | 8 | 15 | Tappa 2 solo con la scena 5 (se Sara entra in palestra); la frase 🔒 resta chiusa nell'Episodio 1 |
| Daniel | 2 | 2 | 45 | Sara lo vede ancora come arrogante, ma qualcosa si incrina alla festa |
| Howard | 2 | 8 | 75 | Il rifiuto non chiude il percorso |
| Editore | 1 | 5 | 65 | Nasce dal percorso di Daniel; +5 solo con Confidence 25 |
| Joanie | 0 | 0 | 55 | Percorso 5, non ancora aperto |
| Ex, amico di Josh, capa | — | — | 25 · 35 · 85 | Non ancora presenti |

| Sara | Valore massimo nell'Episodio 1 |
|---|---|
| Corruption | 3 (guardare Joanie con Simon, tenere il segreto) |
| Confidence | 27 (parte da 20: scrivere, entrare da sola, coraggio con l'editore) |
| Suspicion | 3 (il segreto dell'editore) |
| Interest verso Josh | parte da 80, finisce tra 78 e 91 |

## Episodio 2 · Giorno 14

```mermaid
flowchart TD
    E1([Fine Episodio 1]) --> M["Domenica mattina · messaggio di Daniel e ricordo della terrazza"]
    M --> P["Pranzo · Hugo elogia Daniel e sminuisce Josh"]
    P --> Q{Reazione di Sara}
    Q -->|Lo difende · Josh +3, Confidence +1| V["Sally critica il vestito"]
    Q -->|Tace| V
    Q -->|Sorride · Josh -2| V
    V --> R{Risposta a Sally}
    R -->|Abbassa gli occhi| S["Samantha propone di fare shopping insieme"]
    R -->|Risponde · Confidence +1| S
    S -->|Accetta · registra l'invito accettato| H["Retroscena · Sally e Hugo si scambiano uno sguardo"]
    S -->|Declina| H
    H --> C["In cucina · Sally consiglia a Sara di farsi una vita propria"]
    C --> T["Si sblocca il telefono libero"]
    T --> J{"Sera · risposta all'invito di Daniel del giorno 13"}
    J -->|Forse o Josh lo saprà| O["Chat di trama · Joanie mostra HYPNO e registra l'ordine"]
    J -->|Nessuna risposta registrata| F{"Slot facoltativo con la rubrica effettiva"}
    O --> F
    O -.-> K["Giorno 17 · Sara riceve il top nero e scopre lo scherzo"]
    K -.-> L["Giorno 18 · se il pranzo è confermato, scelta dell'abito"]
    F -->|Scrive a un contatto| A["Il controller gestisce il dialogo e le risposte"]
    F -->|Salta| N["Notte · eventuali risposte in arrivo"]
    A --> N
    N --> G([Fine del giorno 14])
```

## Episodio 2 · Giorno 15

```mermaid
flowchart TD
    D14([Fine del giorno 14]) --> R{Riunione di redazione}
    R -->|Ascolta| P["Allenamento con Joanie e Simon"]
    R -->|Difende la sua idea · Confidence +1| P
    P --> C{Si fa mostrare i pettorali?}
    C -->|Declina| G["Gym squad · Simon in rubrica"]
    C -->|Accetta · Simon +2, Corruption +1| E{Ripetizione extra?}
    E -->|Posa le maniglie| G
    E -->|Si mostra di più · Corruption +1| G
    G --> F["21:30–22:00 · telefono libero a casa"]
    F --> J{"Josh ha letto il manoscritto senza permesso"}
    J -->|Lo affronta · Josh -7| D["Conferma il pranzo con Daniel del 18"]
    J -->|Lascia correre · Josh -3, Confidence -10| M["Sara riscrive il finale"]
    D --> M
    M --> I["Invia le 50 pagine a Magnus · Confidence +2, Magnus +1"]
```

## Episodio 2 · Giorno 16

```mermaid
flowchart TD
    D15([Fine del giorno 15]) --> J{"Jessica riprende «quella cosa»"}
    J -->|Chiede| H{"Hugo passa a riprendere la teglia"}
    J -->|Lascia perdere| H
    H -->|Saluta| A["Arrivano Joanie, Mark e Darius"]
    H -->|Si ferma| C{"Ha litigato con Josh il 15?"}
    C -->|No| A
    C -->|Sì| O{"Hugo le dà ragione e le dice di sedersi"}
    O -->|Si siede| A
    O -->|Resta in piedi| A
    A --> T{"Mark chiede del romanzo"}
    T -->|Sta vicina a Josh · Josh +1| S["Josh e Mark si scambiano il numero"]
    T -->|Ride con Darius · Darius +1| S
    T -->|Si confida con Joanie · Joanie +1| S
    S --> R["Retroscena · Josh parla a Darius di Jacob"]
    R --> F["Flashback · Sara e Josh"]
    F --> P["Josh chiede a Darius di tenere la confidenza per sé"]
    P --> TEL["22:00–23:00 · telefono libero a casa"]
    TEL --> D16([Fine del giorno 16])
```

## Episodio 2 · Giorno 17

```mermaid
flowchart TD
    D16([Fine del giorno 16]) --> M{Accetta il makeover?}
    M -->|Look abituale| B["Pranzo al bar"]
    M -->|Glamour| F{"Lo sconosciuto si avvicina"}
    F -->|Risposta naturale| P["14:00 · foto per il sito"]
    F -->|Recita alla Jessica| C["Il gesto del colletto"]
    C --> P
    B --> P
    P -->|Look abituale| O{Ordine del 14?}
    P -->|Look glamour| E["Scatti extra · Barbara +1 per scatto accettato"]
    E -->|Interrompe o declina l'invito| O
    E -->|Accetta l'invito · Barbara +3| U{"In ufficio · contratto di stagista speciale"}
    U -->|Declina| O
    U -->|Conferma l'avviso| L["Firma guidata · Corruption +10 · Barbara +10 · sara_stagista"]
    L --> O
    O -->|Sì| R{Dove arriva il pacco?}
    R -->|Consegna diretta| S["Top nero · Joanie confessa lo scherzo"]
    R -->|Ritiro da Howard| H["Top nero · Joanie confessa lo scherzo · Howard già incontrato"]
    O -->|No| W{Può passare da Howard?}
    S --> W
    H --> G["Palestra · scelta del top da allenamento"]
    W -->|Sì · spazio prima della palestra| A["Visita spontanea · rotazione faccende"]
    W -->|No| G
    A --> G
    G --> X{Sara sorprende Joanie e Simon}
    X -->|Resta · Corruption +2| Y{Allenamento}
    X -->|Si allontana| Y
    Y -->|Con Simon · Interest +3| Z["Sara apre la chat di Joanie"]
    Y -->|Da sola · Confidence +1| Z
    Z --> D17([Fine del giorno 17])
```

## Episodio 2 · Giorno 19

```mermaid
flowchart TD
    D18([Fine del giorno 18]) --> J{"Il libro di Jessica"}
    J -->|Legge l'appunto · Confidence +1| R{"Il ciondolo di Roberta"}
    J -->|Lo ridà| R
    R -->|Chiede · Barbara +1| B{"sara_stagista e sorteggio 20%?"}
    R -->|Non chiede| B
    B -->|Sì| M{"Barbara · missione 2"}
    B -->|No| S{"Shopping accettato il 14?"}
    M -->|Massaggio · completata| S
    M -->|Rifiuta · resta estraibile| S
    S -->|Sì| V{"Boutique · l'abito per Magnus"}
    S -->|No| K["Caffè con Samantha"]
    V -->|Di Samantha · Magnus +1, Confidence +1| E{"Da Joanie · il ricordo di Jacob"}
    V -->|Il proprio · Confidence +2| E
    K --> E
    E -->|Si lascia portare · Jacob +1, Corruption +1| G1{"Joanie come guida?"}
    E -->|Come è finita · Confidence +1| G2{"Joanie come guida?"}
    G1 -->|Guida · 6 box · Joanie +3, Jacob +2, Corruption +2| I{"Interest Joanie > 8?"}
    G1 -->|Razionale · Confidence +1| X["Retroscena · il messaggio a Jacob"]
    G2 -->|Guida · Joanie +1| X
    G2 -->|Razionale · Confidence +1| X
    I -->|No| X
    I -->|Sì| C{"La confidenza"}
    C -->|Non detto| X
    C -->|"!!! Ascolta · Joanie +3, Corruption +1, sara_bad_girl"| W{"Dirle di Simon?"}
    W -->|Sì · Joanie spiega le sue ragioni| X
    W -->|No| X
    X --> L{"The Lantern · Jacob"}
    L -->|Fredda| Q{"Il drink"}
    L -->|Ride · Jacob +3, Corruption +1| Q
    Q -.->|"Tradimento, Josh, un ballo se ha riso"| N
    L -->|"sara_bad_girl · 17 occhiolini"| OB{"Bancone · 5 occhiolini"}
    OB -->|Due salti di fila · Joanie smette| N
    OB --> OP{"Pista · 3 occhiolini"}
    OP -->|Due salti di fila| N
    OP --> OD{"Divanetto · 3 occhiolini"}
    OD --> N
    N -.->|"Almeno 2 seguiti per momento"| PO{"!!! La porta"}
    PO -->|Casa, in taxi| Z
    PO -->|Va con Jacob| FW(["FINALE FORZATO · The Wink"])
    FW -.->|Go back to the choice| PO
    Q -->|Rifiuta| N{"Il numero"}
    Q -->|Accetta · Jacob +1, Corruption +1| N
    N -->|Glielo dà · Jacob +2| Z([Fine del giorno 19])
    N -->|No · retroscena, glielo dà Joanie| Z
```

## Episodio 2 · Giorno 23

```mermaid
flowchart TD
    A[Arrivo in redazione] --> B[Eventuale convocazione di Barbara]
    B --> C{Inchiesta accettata il 22?}
    C -->|Sì| D{Una pista}
    D --> E[Archivio: luogo del ritrovamento]
    D --> F[Commissariato: comunicato ufficiale]
    D --> G[Supermercato: nessun indizio]
    C -->|No| H[Lavoro ordinario: 25% per il prossimo evento]
    E --> I[Pranzo: responso di Magnus]
    F --> I
    G --> I
    H --> I
    I --> J[Redazione nel pomeriggio]
    J --> K[Palestra: possibile invito a Simon]
    K --> L[Eventuale faccenda da Howard]
    L --> M[Cena con Josh]
    M --> N{Appuntamento già fissato?}
    N -->|No| O[Finestra del telefono]
    N -->|Sì| P[Fine giornata]
    O --> P
```
