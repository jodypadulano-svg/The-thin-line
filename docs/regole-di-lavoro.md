# The Thin Line — Regole di lavoro

**Da leggere sempre, all'inizio di ogni sessione di lavoro su The Thin Line.**
**Vincolo preliminare per qualsiasi AI (Claude e GPT):** leggere e applicare il [vademecum delle regole fondamentali](vademecum-regole-fondamentali.md). La sua **Regola 0** impone di sottoporre a Jody qualsiasi deroga prima di scriverla definitivamente e di rispettare la regola vigente se la deroga viene rifiutata.
**Per dialoghi, monologhi, scene, scelte e prompt, leggere obbligatoriamente anche la [visione artistica](visione-artistica.md): autonomia di Sara, felicità soggettiva in tutti i finali, non moralismo, slow burn e specificità dei percorsi.**
Regole fissate da Jody il 16 novembre 2026. Valgono sopra le abitudini di Claude.

## 1. Decisioni a lotti, codice dopo
- **Non** si riscrive il gioco a ogni singola decisione: costa troppi token e troppo tempo.
- Ogni decisione presa con Jody va annotata subito, in poche righe, nel [registro delle decisioni](decisioni.md), nella sezione **Da applicare**.
- Il codice si aggiorna solo quando le decisioni sono tante e Jody dà il via (es. «scrivi il gioco», «applica le decisioni»). Allora si applicano tutte insieme e si spostano in **Applicate**.
- Le schede in `docs/` possono essere aggiornate subito solo se la modifica è piccola; altrimenti anche loro vanno nel lotto.

### Lint e test
- Concordare con Jody quali verifiche automatiche eseguire e quando, anche se si tratta solo del lint o di una singola suite.
- Quando Jody chiude una giornata e la sua versione finale non è stata verificata con i test, avvisarlo esplicitamente nel riepilogo di chiusura.

## 2. Grafo del gioco sempre aggiornato
- Il grafo è in [grafo.md](grafo.md), come diagramma Mermaid (GitHub lo disegna da solo). Contiene: giornate, scene, bivi, condizioni, retroscena, segreti, e i collegamenti tra percorsi.
- Va aggiornato ogni volta che si applica un lotto di decisioni, e mostrato a Jody quando lo chiede.

## 3. Cercare gli incastri narrativi
- Ogni volta che Jody aggiunge trama o lore, Claude cerca gli incastri migliori con quello che c'è già e li **propone**: «questo lo mettiamo nella giornata XX», «questo lo colleghiamo al fatto XY».
- Le proposte sono proposte: si scrivono in [intrecci-proposti.md](intrecci-proposti.md) ed entrano nel registro solo quando Jody le approva. Mai in Ren'Py prima dell'approvazione.
- Esempi già fatti: le chiavi rubate da Howard il giorno della spesa (collega Howard 2 e Howard 3); l'editore presentato da Daniel (collega due percorsi).

## 4. Prompt per le immagini
- Quando sarà il momento, Claude scrive i prompt per generare le immagini di ogni scena (le didascalie `[CG]` nel codice sono la base).
- Strumento: **Mage**. Stile: **acquerello e matita** (deciso il 16/11/2026, sostituisce il render 3D). Motivi: è chiaramente illustrato, quindi rispetta le regole di Patreon sull'AI (vietato l'iperrealismo per i contenuti 18+); e il contrasto tra l'acquerello dolcissimo e la corruzione di Sara è parte dell'identità del gioco.
- **Le immagini le genera Jody**: Claude scrive solo i prompt e non avvia generazioni su Mage.
- **Solo immagini immersive** (niente sprite): ogni momento è una scena completa. Per ogni scena Claude indica la CG base e le varianti da ottenere modificandola.
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
- **Regola fissa:** ogni scena erotica è pienamente consensuale e Sara la desidera e se la gode tantissimo: **sorride o ride**, nel testo e nelle immagini. Niente costrizione, niente disagio durante l'atto (vincolo anche di Patreon). I dubbi stanno prima o dopo, nei suoi pensieri.
- Nel codice la parte esplicita resta un segnaposto riconoscibile, che poi si sostituisce con il testo generato.
- Procedura e strumenti: [guida-lm-studio.md](guida-lm-studio.md) (brief in `docs/nsfw/brief/`, script `tools/nsfw/genera_scena.py`).
- Attenzione: LM Studio con un modello grande occupa molta memoria; non tenerlo carico mentre si lavora con Unity o Premiere.

## 8. Regole che valgono sempre
- La [bibbia narrativa](bibbia-narrativa.md), la [visione artistica](visione-artistica.md) e le [schede](personaggi/) sono la fonte. **Il manifesto creativo è un vincolo di tono e interpretazione** anche quando si generano dialoghi. I dialoghi nel codice sono bozze finché Jody non li approva.
- Tutti i personaggi sono adulti.
- Non nominare mai i giochi di riferimento nel gioco e non copiarne i testi: gli script estratti stanno fuori dal repository (`C:\Users\Jody\renpy-ispirazione`).
- Salvataggi compatibili tra episodi: vedi [sistema di gioco](sistema-di-gioco.md), sezione 8.
- Commit e push solo quando Jody lo chiede.
- A ogni aggiornamento di stato: percentuale stimata di completamento.

## 9. Consumo di token (Jody, 26/11/2026)
- Se un processo sta consumando troppi token o troppo tempo (test lunghi, cicli di correzioni, letture o ricerche che si allungano, tentativi ripetuti), l'AI **lo dice subito a Jody**, **si interrompe** e **propone alternative** più economiche (es. una verifica più piccola, rimandare, fare a mano un passaggio, cambiare strada). Riprende solo dopo che Jody ha scelto.
