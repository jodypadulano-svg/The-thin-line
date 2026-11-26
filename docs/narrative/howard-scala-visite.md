# Howard — la scala delle visite (bozza)

Bozza di Claude, 21/11/2026, **da correggere con Jody**. Regole decise il 21/11 nel [registro](../decisioni.md) («Howard: la scala delle visite»). Fonti: [scheda di Howard](../personaggi/howard.md) (sezioni F-H), [appunti del 19/11](../../notes/howard-sara-session-2026-11-19.md), [visione artistica](../visione-artistica.md).

**Decisione del 26/11:** il mercoledì di Josh, se Sara sceglie Howard, si richiama il prossimo gradino di questa scala, senza una sequenza separata. Il gradino dipende dagli incontri realmente vissuti, non dalla data; rispettare i requisiti già approvati. La rotazione delle venti faccende spontanee è indipendente dalla scala narrativa. Vedi [pianificazione 22–24](giorni22-24-pianificazione-2026-11-26.md).

## Il meccanismo, in breve

- A ogni incontro Howard invita Sara da lui, con una scusa diversa e l'aria da cane bastonato. **Non si arrende mai.**
- `howard_visite` conta le visite accettate. **Il giorno 9 è lo step 1.** Ogni «sì» porta allo step successivo; ogni «no» non cambia niente (una riga, poi ogni tanto un retroscena: non è debolezza, è strategia).
- Il rifiuto è `rifiuto_howard=True`: col **Complesso della Crocerossina** Sara non può dire di no e sale la scala a ogni incontro.
- **Proposta nuova: i cancelli.** Dallo step 6 in poi ogni gradino chiede anche una soglia di **Corruption** (valori da tarare). Se Sara accetta l'invito ma non ha la soglia, si gioca una **visita tranquilla** (caffè, chiacchiere, Howard +1) e il contatore **non** sale. Così chi accetta ogni invito già nel primo mese non arriva al bacio al giorno 20: lo slow burn resta, e la scala aspetta Sara.
- **Due registri separati** (scheda, sezione G): l'**affetto** per Howard (Interest) e la **confidenza concessa alle battute sul corpo** (nuova variabile `howard_battute`, 0-5). Sara può affezionarsi a lui senza gradire le battute; se ride e rilancia, Howard alza il tono; se mette un limite, torna scanzonato.
- Ogni step ha **una scelta** dentro la scena: assecondare (avanti, a volte Corr +1) o fermarsi (la visita finisce bene, niente di perso).
- Regole fisse: Howard prende sempre l'iniziativa; Sara decide risposta e limiti; ogni scena intima è voluta e goduta da Sara (sorride, ride); i dubbi stanno prima o dopo, nei suoi pensieri. Le parti esplicite: brief per LM Studio.

## La scala

| Step | Quando, di solito | La scusa di Howard | Cosa succede | La scelta dentro | Effetti (proposta) |
|---|---|---|---|---|---|
| **1** | Giorno 9 (fatto) | Chiusa fuori | Il caffè, il pianto finto, l'abbraccio; se prolungato, la mano fino al sedere | Già scritta | Già scritti |
| **2** | Giorno 18 o il primo invito | «Ho comprato tazze nuove. Per gli ospiti. Cioè, per te.» | La casa è un po' più in ordine «per caso». Lui le chiede del romanzo e ascolta davvero; lei gli legge un paragrafo. Primi complimenti impacciati, quasi scusandosi. | Un secondo caffè o andare | Howard +1 / +2 |
| **3** | Un pomeriggio libero | «La lampadina del corridoio… alla mia età, la scala…» (se al giorno 9 ha promesso di aiutarlo a pulire: «il giorno delle pulizie») | Sara sulla scaletta, lui la tiene e guarda in su. Prima battuta sul corpo che Sara capisce benissimo. | Ridere e rilanciare («Howard, pensi sempre a certe cose?») / scendere e chiudere lì | `howard_battute` +1, Corr +1 / Howard torna gentile |
| **4** | Una sera con Josh di turno | «Ti insegno il ragù di mia madre. Ce l'ho solo io, la ricetta.» | Ai fornelli lui dietro di lei, le mani sulle sue sul mestolo. Battute sul seno, il suo «leitmotiv». Cenano da lui; lei torna a casa con il sugo per Josh. | Lasciarlo fare / spostarsi | `howard_battute` +1, Howard +2 / — |
| **5** | Un sabato | «Le tende. Tu hai gusto. Io no.» | Sara comincia a sistemargli la casa: tende, piante, una mensola. Lui le dà un grembiule «per quando vieni». Primo seme del finale: la casa di Howard comincia a sembrare anche sua. Massaggio alle spalle dopo il lavoro. | Accettare il massaggio / ringraziare e andare | Howard +2, Corr +1 / Howard +1 |
| **6** 🔒 | Corr ≥ ~30 | Dopo uno scambio malizioso: «Continuiamo da me?» | **Il gioco delle pose** (scheda G): lui sul divano, lei in piedi, consapevole di essere guardata; lui suggerisce, lei asseconda. I «salti» di memoria: **da decidere** se ellissi del racconto o vuoti veri. Si ferma alla biancheria. | Continuare il gioco / fermarlo ridendo | Corr +2, `howard_battute` +1 / Howard +1 |
| **7** 🔒 | Corr ≥ ~35 | «Ho trovato una cosa per te.» (un regalo goffo) | **Il primo bacio**, preso da lui. Sara sente per la prima volta la *trasgressione del contrasto*: lei «pulita», lui «sporco». Lo vive come una cosa che regala; lui come una conquista. | Ricambiare / fermarsi lì | Howard +3, Corr +2 / Howard +1 |
| **8** 🔒 | Corr ≥ ~40 | Qualunque | **Prime attenzioni fisiche**, tutte prese da lui, ritmo deciso da lei; Sara si gode di centellinare ogni apertura. Brief LM Studio. | Più avanti / fin qui | Corr +2 / — |
| **9** 🔒 | Corr ≥ ~45 | Nessuna scusa: «Vieni.» | **La maschera cade**: Howard più sicuro, sfacciato, dominante. Sara scopre che le piace la sua ruvidità. | Assecondarlo / riportarlo al gentile | Howard +3, Corr +2 / Howard +1 |
| **10** 🔒 | Corr ≥ ~50 | — | **La prima volta.** Brief LM Studio. Dopo, Sara a casa sua si sente a casa. | — | Tappa Howard; da qui la fase finale |
| **Dopo** | Mesi | — | La vita insieme scivola: Sara passa sempre più tempo da lui, pianificano cose, finché vive di fatto lì e **Josh diventa il vicino** (finale della scheda). | — | — |

## Varianti trasversali

- **Complesso della Crocerossina attivo (decisione 21/11):** Sara non sa dire di no a nessuna richiesta quotidiana di Howard (l'invito, restare, pulire, vestirsi come vuole lui, mentire a Josh…): si chiede perché, si dà una scusa («non è niente di grave»), lo fa; a casa sembra un sogno strano. Howard sembra saperlo, senza spiegazioni, e non forza mai: la abitua un passo alla volta per non rompere l'incanto. Nelle scene intime il Complesso non costringe: Sara scopre di volerlo, e se lo gode; i dubbi dopo.
- **Numero di Howard salvato (giorno 11):** gli inviti possono arrivare anche per messaggio («Sei a casa? Ho fatto troppo caffè»).
- **Josh in casa / via:** gli step 4, 6 e 7 accadono solo quando Josh è fuori (turni di Daniel): lo sa sempre, perché sente attraverso il muro.
- **Retroscena dopo un rifiuto** (ogni 2-3 rifiuti): il cassetto, la copia della chiave, il calendario dei turni di Josh appuntato in cucina.

## Da decidere con Jody

1. Gli step 2-10 vanno bene come ordine e contenuto? Troppi, troppo pochi?
2. I **cancelli di Corruption** dallo step 6: sì o no? E le soglie.
3. Il gioco delle pose: ellissi del racconto o vuoti veri di coscienza (questione aperta dalla scheda)?
4. La variabile separata `howard_battute`: serve, o basta l'Interest?
