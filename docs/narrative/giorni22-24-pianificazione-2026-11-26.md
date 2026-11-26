# Giorni 22–24 — pianificazione approvata (26 novembre 2026)

**Stato:** decisioni approvate da Jody in sessione vocale; da sceneggiare, implementare e illustrare. Prevale sulle indicazioni precedenti incompatibili limitatamente ai punti qui aggiornati. Nessuna nuova soglia o effetto numerico è fissato. Documento interno agli autori.

## Lunedì 22
- Lavoro 9–17: Barbara commenta l'abbigliamento di Sara; mantenere la scelta sull'abbigliamento del giorno successivo già prevista nel piano del mese.
- Barbara propone la verifica della lettera anonima sulla morte della giovane prostituta. Sara può accettare o rifiutare; inchiesta professionale indipendente dal percorso personale di Barbara. Eventuale convocazione della stagista secondo le condizioni esistenti.
- Sempre lunedì, durante il lavoro se Sara ha accettato l'incarico, primo incontro breve con l'amica della vittima, autrice della lettera anonima. La testimone è spaventata, racconta parte della vita dell'amica e fornisce il primo indizio concreto; contatto, luogo e indizio da definire. Nessun incontro se l'incarico è rifiutato.
- Dopo il lavoro: possibile visita spontanea a Howard per la rotazione delle faccende, se Interest > 50 e gli altri requisiti sono soddisfatti.
- Sera: Josh torna umiliato da Daniel; mantenere le reazioni e gli effetti già concordati. È il presupposto per il D&D del mercoledì. Non aggiungere altri eventi fissi.

## Martedì 23
- Pausa pranzo: Magnus comunica il giudizio positivo sulle cinquanta pagine; osservazioni e dialogo da definire.
- Lavoro: spazio per eventuale approfondimento dell'inchiesta, solo se intrapresa; convocazioni di Barbara secondo le regole esistenti. Nessun indizio nuovo ancora approvato.
- Dopo il lavoro: allenamento in palestra previsto. Se non ha già un appuntamento per mercoledì, Sara può proporre direttamente a Simon di uscire, con Interest Simon >= 16. Non imporre l'invito e non sovrapporre appuntamenti.
- Eventuale faccenda da Howard, solo se realmente libera, sa che è in casa e non è previsto altro incontro con lui; non comprimere artificialmente la palestra.
- Sera normale con Josh. Finestra/slot telefonico speciale del martedì per invitare qualcuno per mercoledì, disponibile se Sara non ha già un appuntamento. Non è un argomento sempre disponibile nel telefono. Daniel e Darius vanno invitati entro martedì; Joanie è sempre una possibile alternativa da contattare (il fidanzato non c'è); Howard è un'altra opzione. Conservare le condizioni già approvate salvo revisione esplicita; coordinare in implementazione la disponibilità di Joanie con la soglia 12 già registrata, senza inventare una nuova soglia. Un appuntamento alla volta. Nessuna nuova regola su consumo dello slot oltre quanto già definito.

## Mercoledì 24
- Pausa pranzo: Darius e Sara scoprono una passione comune; proposta precedente: letteratura psicologica. Sara può condividere le cinquanta pagine; eventuale riscontro del 31 solo se ha letto il testo.
- Resto dell'orario lavorativo: spazio per inchiesta o lavoro ordinario, eventuale convocazione. Dopo il lavoro, eventuale faccenda di Howard compatibile con il programma; non duplicare un incontro con Howard già previsto.
- Josh gioca a D&D da Mark con gli amici, circa 19:30–23:30. Sara sceglie una delle sette alternative, subordinata all'appuntamento effettivamente preso e ai requisiti esistenti:

| Alternativa | Accesso e contenuto |
|---|---|
| Jacob | Domenica 21 sera è **Jacob** a invitarla; Sara può accettare o rifiutare. L'uscita è il prossimo gradino del percorso, non una scena esclusiva del 24. |
| Simon | Appuntamento organizzato anche direttamente durante l'allenamento del 23, se libero lo slot e soddisfatti i requisiti. |
| Daniel | Sara lo invita al telefono entro martedì. Conservare la regola Interest >= giorno dell'uscita (24 per questo mercoledì); rispettare le tappe già vissute, senza anticipare gli eventi fissi o presupporre il pranzo del 18. |
| Joanie | Serata più breve delle altre, bonding e confidenze sugli avvenimenti realmente vissuti, nella misura in cui Sara sceglie di raccontarli. Nessuna nuova tappa sentimentale obbligatoria. |
| Darius | Invito entro martedì. Uscita simpatica e piacevole, amichevole, senza avances o anticipazioni sulla destinazione del percorso. |
| Howard | Sara va a casa di Howard, non lo invita a casa propria. Richiamare il prossimo gradino della scala delle visite narrative (tazze, lampadina, ragù ecc., secondo quanto già fatto e i requisiti); non creare una seconda sequenza di appuntamenti del mercoledì. |
| Romanzo | Sara resta a casa a scrivere, alternativa sempre disponibile. |

**Retroscena solo autori:** se Sara non esce né con Joanie né con Simon, è molto probabile che loro due si vedano di nascosto. Non mostrarlo a Sara né al giocatore in questa fase. Nessuna probabilità numerica fissata.

Conservare gli effetti e i rischi già approvati nella scheda del mercoledì, applicandoli solo se i fatti si verificano davvero (Howard può averla vista uscire, rientro tardivo, ecc.).

## Convocazioni di Barbara (promemoria confermato il 26/11)

Ogni nuova giornata lavorativa deve chiamare il motore `call barbara_convocazione` una volta in orario di lavoro. Mantenere il 20%, le soglie esistenti e l'esclusione delle missioni completate; non forzare il sorteggio per far comparire il massaggio. Nessun nuovo test richiesto.

## Appuntamenti riutilizzabili
- Jacob: scene autonome e numerate per progressione, indipendenti dalla data. Se l'uscita non avviene, lo step resta disponibile per un'occasione successiva; non avanzare per il solo passaggio del tempo. Quando si scrive un nuovo avvenimento importante, rivedere retroattivamente gli appuntamenti già scritti e inserire brevi dialoghi condizionali legati agli eventi realmente vissuti. Non riscrivere intere scene né anticipare combinazioni non ancora definite.
- Howard: stesso principio per la scala delle visite narrative. Le faccende spontanee dopo il lavoro sono una rotazione separata, con contatore proprio; una faccenda non sostituisce automaticamente uno step narrativo e viceversa.
- Daniel: coordinare gli appuntamenti dinamici con le tappe fisse (festa del 13, eventuale pranzo del 18, incontro del 25 e successive). Adeguare dialoghi e scelte ai fatti; non anticipare tappe.
- Joanie e Darius: privilegiare la naturalezza e la progressione lenta, non trasformare ogni incontro in un avanzamento sentimentale.

## Produzione grafica
- Howard: portare avanti le CG delle 20 faccende ricorrenti almeno fino alla sesta, in tenuta classica: 01 pavimento cucina (già presente), 02 forno, 03 tappeto sul balcone, 04 pensili cucina, 05 finestre, 06 scatoloni nella dispensa. Sequenza nel codice `game/percorsi/howard_faccende.rpy`. Possono essere raggiunte anche prima della fine della settimana a seconda delle visite.
- Barbara: portare la copertura ad almeno cinque missioni illustrate delle venti, includendo il massaggio alle spalle già illustrato (ID 2). Non confondere l'ordine di produzione con l'ordine di estrazione delle missioni: gli ID non sono una progressione. Rispettare le missioni 1, 8 e 20 già previste per la settimana del 22; scegliere l'ulteriore missione in base alle condizioni effettivamente raggiungibili e alle decisioni approvate. Implementare solo quando si sviluppano le giornate; il motore estrae soltanto missioni già scritte.
- Entrambi i percorsi: al raggiungimento del secondo costume e dei successivi previsti, produrre le varianti partendo dalla CG originale, cambiando solo l'abbigliamento e conservando posa, ambiente, inquadratura e luce. Non anticipare tutte le varianti; farle quando le tenute diventano effettivamente raggiungibili. Nessuna nuova CG prodotta in questa sessione.

## Riferimenti
- [Calendario 22–35](calendario-giorni22-35-2026-11-25.md)
- [Mercoledì di Josh](mercoledi-di-josh-2026-11-25.md)
- [Inchiesta](inchiesta-giorno22-2026-11-25.md)
- [Scala delle visite di Howard](howard-scala-visite.md)
- [Regola Interest > 50](../game-design/regola-interesse-superiore-50-incontri-spontanei.md)
- [Registro decisioni](../decisioni.md)

Nessuna modifica a Ren'Py, nessun test o lint eseguito: è un aggiornamento di progettazione.
