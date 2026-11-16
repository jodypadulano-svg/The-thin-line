# The Thin Line — Regole di lavoro

**Da leggere sempre, all'inizio di ogni sessione di lavoro su The Thin Line.**
Regole fissate da Jody il 16 novembre 2026. Valgono sopra le abitudini di Claude.

## 1. Decisioni a lotti, codice dopo
- **Non** si riscrive il gioco a ogni singola decisione: costa troppi token e troppo tempo.
- Ogni decisione presa con Jody va annotata subito, in poche righe, nel [registro delle decisioni](decisioni.md), nella sezione **Da applicare**.
- Il codice si aggiorna solo quando le decisioni sono tante e Jody dà il via (es. «scrivi il gioco», «applica le decisioni»). Allora si applicano tutte insieme, con un solo giro di lint e test, e si spostano in **Applicate**.
- Le schede in `docs/` possono essere aggiornate subito solo se la modifica è piccola; altrimenti anche loro vanno nel lotto.

## 2. Grafo del gioco sempre aggiornato
- Il grafo è in [grafo.md](grafo.md), come diagramma Mermaid (GitHub lo disegna da solo). Contiene: giornate, scene, bivi, condizioni, retroscena, segreti, e i collegamenti tra percorsi.
- Va aggiornato ogni volta che si applica un lotto di decisioni, e mostrato a Jody quando lo chiede.

## 3. Cercare gli incastri narrativi
- Ogni volta che Jody aggiunge trama o lore, Claude cerca gli incastri migliori con quello che c'è già e li **propone**: «questo lo mettiamo nella giornata XX», «questo lo colleghiamo al fatto XY».
- Le proposte sono proposte: entrano nel registro solo quando Jody le approva.
- Esempi già fatti: le chiavi rubate da Howard il giorno della spesa (collega Howard 2 e Howard 3); l'editore presentato da Daniel (collega due percorsi).

## 4. Prompt per le immagini
- Quando sarà il momento, Claude scrive i prompt per generare le immagini di ogni scena (le didascalie `[CG]` nel codice sono la base).
- Strumento: **Mage**. Stile: **render 3D** come i giochi di riferimento.
- Ogni prompt specifica:
  - **A. Gli attori** presenti nell'immagine (riferiti agli attori già generati, vedi punto 5);
  - **B. Il luogo** (riferito ai luoghi già generati, vedi punto 5).
- Oltre ad attori e luogo: inquadratura, posa, espressione, abbigliamento, luce, ora del giorno.

## 5. Attori e luoghi si generano a parte
- **A. Gli attori**: ogni personaggio ha una sua scheda visiva e le sue immagini di riferimento, generate una volta sola e riusate in tutte le scene per restare coerenti.
- **B. I luoghi**: ogni ambiente (casa di Sara, palestra, ufficio, casa di Howard…) ha le sue immagini di riferimento.
- I prompt delle scene (punto 4) richiamano questi riferimenti invece di descrivere tutto da capo.

## 6. Personaggi funzionali
- Oltre agli otto percorsi servono personaggi di contorno che rendano il mondo vivo: colleghi, vicini, famigliari, baristi, la receptionist della palestra…
- **Non sono percorsi**: non hanno affinità né tappe. Hanno una funzione narrativa (dare informazioni, creare occasioni, testimoniare, mettere pressione).
- Li propone Claude quando servono a un incastro; entrano nel gioco dopo l'approvazione di Jody. Esempi validi: un collega di Josh, la receptionist della palestra, il fidanzato di Joanie.

## 7. Parti NSFW con LM Studio
- Le parti esplicite non le scrive Claude: si generano con un modello in **LM Studio** addestrato apposta.
- Claude scrive tutto il resto: la struttura della scena, cosa succede prima e dopo, le scelte, le variabili, e un **brief** per ogni parte esplicita (chi, dove, a che punto del percorso, tono, limiti, cosa deve cambiare dopo).
- Nel codice la parte esplicita resta un segnaposto riconoscibile, che poi si sostituisce con il testo generato.
- Procedura e strumenti: [guida-lm-studio.md](guida-lm-studio.md) (brief in `docs/nsfw/brief/`, script `tools/nsfw/genera_scena.py`).
- Attenzione: LM Studio con un modello grande occupa molta memoria; non tenerlo carico mentre si lavora con Unity o Premiere.

## 8. Regole che valgono sempre
- La [bibbia narrativa](bibbia-narrativa.md) e le [schede](personaggi/) sono la fonte. I dialoghi nel codice sono bozze finché Jody non li approva.
- Tutti i personaggi sono adulti.
- Non nominare mai i giochi di riferimento nel gioco e non copiarne i testi: gli script estratti stanno fuori dal repository (`C:\Users\Jody\renpy-ispirazione`).
- Salvataggi compatibili tra episodi: vedi [sistema di gioco](sistema-di-gioco.md), sezione 8.
- Commit e push solo quando Jody lo chiede.
- A ogni aggiornamento di stato: percentuale stimata di completamento.
