# The Thin Line — Telefono, percorsi dinamici e serate alternative

**Decisione di progettazione approvata da Jody il 18 novembre 2026.** Da integrare nel gioco in un lotto di sviluppo successivo, **non ancora implementata in Ren'Py**. Questa specifica prevale, per la parte di progressione variabile, sulle letture rigidamente cronologiche delle vecchie scalette; non annulla le scene canoniche né i vincoli specifici degli otto percorsi.

Documenti collegati: [registro decisioni](decisioni.md) · [sistema di gioco](sistema-di-gioco.md) · [primo mese](mese-1.md) · [mappa delle tappe](mappa-tappe.md) · [visione artistica](visione-artistica.md).

## 1. Obiettivo e principio centrale

Mantenere una **trama principale con giornate e incontri riconoscibili**, ma lasciare al giocatore la possibilità di approfondire **in parallelo e a ritmo personale** ciascuno degli **otto percorsi** mediante il telefono di Sara. Quando un evento canonico riporta in scena un personaggio, **la scena deve reagire al livello di rapporto raggiunto**, non riproporre automaticamente una conoscenza iniziale ormai superata.

La progressione deriva da **messaggi + incontri dal vivo + scelte compiute**. La familiarità non equivale automaticamente a interesse romantico; messaggiare, uscire insieme e aprire una relazione sono azioni diverse. Le decisioni sentimentali decisive restano volontarie e rispettano le condizioni e i punti di non ritorno già approvati.

## 2. Sblocco del telefono e rubrica

- Esiste un **evento scatenante** dopo il quale Sara può usare liberamente lo strumento di contatto. **Momento preciso da decidere**: nelle prime fasi prevalgono gli incontri fissati; i primi bivi significativi sono previsti orientativamente **dopo le prime due settimane**, non automaticamente in un giorno inventato.
- Ogni personaggio dei percorsi ha una condizione indipendente **«Sara possiede il numero»**: sì/no. **Conoscere personalmente qualcuno non implica possederne il recapito**.
- Solo i personaggi di cui Sara ha il numero e con cui è possibile comunicare compaiono come **contatti selezionabili** per il messaggio libero. Acquisire il numero richiede un evento coerente da progettare per il personaggio; non assegnare tutti i numeri automaticamente.
- Possedere il numero **abilita il canale**, non apre automaticamente un flirt, un appuntamento o una tappa romantica. La presenza di Josh o di chat canoniche obbligatorie non crea un nono percorso.

## 3. Slot telefonico giornaliero

- Sara dispone di **un solo slot di contatto elettivo per giornata**: il giocatore sceglie **al massimo un** personaggio della rubrica idonea. Può anche non usarlo; non può inviare messaggi di avanzamento a due personaggi nello stesso giorno.
- Ogni personaggio ha una **sequenza autonoma e ordinata** di conversazioni (step telefonici). Quando viene scelto, si gioca **il primo step non ancora svolto e disponibile** per quel contatto; il giorno del calendario **non azzera e non determina** lo step.
- Esempio approvato come logica: Daniel step 1 lunedì, Darius step 1 martedì, Daniel step 2 mercoledì. Se Daniel viene contattato **per la prima volta al giorno 20**, Sara gioca **Daniel step 1**, non «Daniel giorno 20».
- Lo step aumenta soltanto se la relativa conversazione è stata effettivamente portata a termine; evitare doppi incrementi, replay che regalano punti e salti causati dall'apertura/chiusura della schermata.
- I **messaggi obbligatori della trama** (per esempio il filler con Josh al giorno 4 o la telefonata di Joanie al giorno 12) **non vanno confusi** con lo slot elettivo. *Proposta implementativa da confermare*: non consumano lo slot, per non rendere impossibili scene canoniche; la regola esatta per eventuali eccezioni resta aperta.

## 4. Incontri fisici e salti degli step narrativi

- Ogni personaggio ha una **progressione relazionale propria**. Prima dello sblocco del numero, gli incontri avanzano attraverso la storia e le scelte già previste. Dopo, i progressi telefonici possono **anticipare la familiarità** e modificare quale step sia sensato giocare al successivo incontro.
- Esempio: Simon è stato introdotto con uno **step 0** comune. Al successivo allenamento, se Sara non gli ha mai scritto, può svolgersi **lo step 1**; se hanno già conversato a lungo, può essere appropriato **lo step 2 o 3**. Gli step di semplice conoscenza ormai superati **si saltano**, senza obbligo di recuperarli.
- **Non è un automatismo aritmetico «N chat = tappa N»**: occorre usare i fatti già accaduti, la familiarità, l'Interest, la tappa della mappa e le condizioni specifiche. I messaggi possono sostituire **contenuti introduttivi**, non fatti unici e indispensabili (per esempio una rivelazione non avvenuta, una prima visita determinante o una scelta esplicita).
- Gli eventi fissi restano sul calendario come **occasioni di incontro**. Alcuni contenuti della scena sono di base, altri sono condizionali; i momenti di svolta non obbligatori possono avere **varianti** oppure non attivarsi se non si sono raggiunti i requisiti.
- Rispettare gli **otto percorsi e le mappe a tappe approvate**, comprese le soglie già fissate di Interest/Corruption e la necessità di scelta esplicita ai confini decisivi. In particolare il percorso **Darius è solo opt-in**, quello di **Joanie rivela la dimensione sentimentale molto più avanti** e quello di **Barbara evolve lentamente**. Non anticipare baci o scene fisiche soltanto perché sono stati inviati molti messaggi.

## 5. Serate libere e appuntamenti alternativi

- Ci sono **serate libere** e **alcune serate altrimenti trascorse con Josh** che possono offrire una scelta alternativa di uscita con uno dei personaggi.
- Ogni percorso ha una **soglia di conoscenza e/o Interest propria**, da definire in seguito, oltre a eventuali prerequisiti narrativi. Al raggiungimento della soglia, il personaggio diventa **una possibile opzione di appuntamento**, **non un appuntamento automatico**.
- Se Sara ha sbloccato più persone, il giocatore sceglie **con chi** uscire; può anche scegliere Josh o un'altra opzione di serata già prevista. Un'uscita può inizialmente essere amichevole, professionale o sentimentale: la sola uscita non prova tradimento né avanza forzatamente il percorso.
- **Slot telefono e scelta serale sono due risorse distinte**: la chat elettiva non occupa da sola la serata e viceversa; la stessa giornata può contenere entrambi nei limiti della regia prevista. Non sostituire scene cruciali e obbligatorie della trama con date opzionali.
- Quando il contesto lo consente, la scelta include **dire o non dire a Josh** dell'uscita. Salvare separatamente il fatto dell'appuntamento e la sua conoscenza da parte di Josh; segreti, Interest e Suspicion cambiano **in base alla situazione**, senza automatismi moralizzanti.
- **Soglie numeriche di accesso alle date, elenco delle serate sostituibili, disponibilità concreta di ciascun personaggio e contenuti dei singoli appuntamenti: da progettare.** Nessun valore esemplificativo ascoltato in conversazione è una soglia approvata.

## 6. Regola obbligatoria: tutte le scene fisse devono reagire al rapporto

Dal momento in cui Sara può contattare un personaggio, **ogni successiva interazione personale con quel personaggio**, anche se collocata in una giornata fissa, deve controllare lo **stato pertinente** prima di scrivere i dialoghi e gli eventuali bivi. Questo vale per Barbara in redazione, Simon in palestra, Daniel sul lavoro e per tutti gli altri.

Tre livelli di adattamento per evitare un'esplosione combinatoria:

1. **Micro-varianti nel dialogo ordinario**: saluti, tono, riferimenti a confidenze e messaggi già scambiati; nucleo della scena condiviso.
2. **Interazioni o scelte extra condizionali**: se familiarità, interesse, tappa e fatti lo consentono, una porzione aggiuntiva o un bivio nuovo; altrimenti la scena standard.
3. **Diramazioni importanti**: appuntamenti, segreti, cambi di ruolo e punti di non ritorno soltanto dove la mappa lo richiede; rispettano soglie e scelta esplicita.

**Esempio Barbara:** se Sara non le ha mai scritto, al lavoro si comportano come capo e dipendente; se hanno scambiato molti messaggi, Barbara può ricordare una confidenza; se hanno trascorso insieme la sera precedente, un momento privato può contenere un riferimento complice, mentre in pubblico Barbara può mantenere il tono abituale. **Tutti questi esempi illustrano la logica, non sono scene o confessioni canoniche già approvate.**

**Causalità:** la scena del mattino può leggere soltanto informazioni e fatti **già avvenuti**. Non può alludere all'uscita che il giocatore deciderà soltanto quella sera. Un appuntamento segreto non diventa noto a Josh per magia. Usare varianti condizionali all'interno di **una sola scena principale**, non scrivere una giornata completa per ogni combinazione degli otto percorsi.

## 7. Dati e separazione delle responsabilità (schema di progettazione, non codice implementato)

Usare e preservare le variabili già previste nel gioco:
- `percorsi[x].interest`, `percorsi[x].tappa`, `percorsi[x].chiuso` per il percorso narrativo; `sara_corruption`, `sara_confidence`, `josh_suspicion`, `interest_josh`, `fatti` e `segreti` dove pertinenti.
- **Nuovi dati concettuali per ogni personaggio** (nomi tecnici definitivi da concordare): `ha_numero[x]` (booleano), `step_chat[x]` (indice della prossima conversazione o ultimo step concluso, convenzione unica da fissare), `conoscenza[x]` (se serve una misura distinta da Interest), fatti specifici di confidenze, incontri, appuntamenti e loro esiti.
- **Nuovi dati globali/di calendario**: `telefono_libero_sbloccato`, stato dello slot elettivo del giorno (con identificativo del giorno e persona contattata), e disponibilità della fascia serale. Le date svolte e ciò che Josh sa richiedono fatti puntuali, non soltanto un punteggio.
- Evitare di duplicare significati: **conoscenza/familiarità**, **interesse**, **tappa narrativa** e **step telefonico** sono dimensioni diverse. Definire una funzione centrale per calcolare la variante di incontro in base a tutte le condizioni, anziché inserire confronti incoerenti in ogni scena.

**Compatibilità salvataggi:** seguire le indicazioni di [sistema-di-gioco.md](sistema-di-gioco.md): nuovi valori inizializzati con `default`, evitare rinomine delle chiavi preesistenti, trattare con cura gli attributi di `Percorso` e gli script già distribuiti. `Yet Another Phone for Ren'Py` resta la **soluzione UI già scelta il 17/11**; la logica del telefono e delle relazioni deve restare nei dati di gioco e non dipendere dalla grafica del plugin. Verificare la licenza commerciale e gli asset prima della distribuzione.

## 8. Regole di produzione e test

- Documentare per ogni personaggio: **come si ottiene il numero**, sequenza delle chat, cosa è apprendibile per chat, quali step dal vivo si possono saltare, quali invece richiedono una scena imprescindibile, soglie per gli appuntamenti e scene quotidiane che cambiano.
- Nelle mappe e nei calendari etichettare gli **incontri fissi** come punti di accesso a scene **varianti**; non interpretare una tappa indicata in un vecchio calendario come obbligatoria in qualunque partita.
- Testare almeno: rubrica prima/dopo sblocco; numero mancante; uno slot al giorno; chat di Daniel al primo utilizzo anche al giorno 20; intercalare Darius e Daniel; salto di step introduttivi senza perdere fatti necessari; chat senza sblocco romantico; appuntamenti disponibili/indisponibili; uscita detta o taciuta a Josh; mattina che usa solo fatti pregressi; più percorsi paralleli; salvataggio e caricamento.
- **Ordine di lavoro:** prima definire i dati e le regole di avanzamento, poi l'interfaccia telefono, poi gli step delle chat e le scene condizionali, infine le serate alternative e il collaudo delle combinazioni più importanti.
- **Decisione documentale, non ordine di programmazione immediata**: rispettare [regole-di-lavoro.md](regole-di-lavoro.md), che prevede di applicare il codice soltanto su successiva autorizzazione esplicita e in un lotto unico.

## 9. Questioni aperte da decidere, non ipotesi approvate

> **Chiuse il 18/11/2026: vedi la sezione 10.**

- Evento esatto di **attivazione del telefono libero**, da quale giorno, e acquisizione del numero per ciascuno degli otto.
- Numero, contenuto, prerequisiti e possibili limiti degli step di chat per ogni personaggio; quali confidenze e attività anticipano realmente le scene fisiche.
- Come calibrare numericamente `conoscenza` rispetto a `Interest` e alle tappe già approvate; ritmo e tetto dei progressi.
- Soglia individuale e natura delle date, serate libere/sostituibili, priorità con incontri canonici, possibilità di ripetere appuntamenti.
- Trattamento definitivo delle comunicazioni automatiche di trama rispetto allo slot quotidiano, eventuali messaggi in entrata, disponibilità oraria e contatti che possono essere bloccati.

**Sintesi vincolante:** un solo calendario principale, **otto percorsi indipendenti e opzionali**, un contatto elettivo al giorno con chi è in rubrica, conoscenza che può avanzare via chat e cambiare anche gli incontri futuri, date opzionali sbloccate per soglie individuali, e **tutte le scene personali successive sensibili allo stato della relazione**.

## 10. Decisioni del 18/11/2026 (seconda parte): le questioni aperte chiuse

Approvate da Jody in conversazione; il riepilogo sta anche nel [registro](decisioni.md). Dove contraddicono le sezioni 1-9, **prevale questa sezione**.

### 10.1 Sblocco
- **Telefono libero al giorno 14**, pranzo delle due famiglie: Sally e Sara sole in cucina, Sally le dice di farsi una vita sua fuori casa e di conoscere gente (doppia lettura col segreto di Sally e Hugo, I7). Flag `telefono_libero` e notifica del tipo *«Sara's phone feels different tonight.»*
- Prima del 14 il telefono serve solo ai messaggi di trama (giorni 4, 9, 12...). Rubrica: solo chi ha dato il numero.

### 10.2 I numeri
| Percorso | Quando | Come |
|---|---|---|
| Joanie | da subito | migliore amica |
| Darius | da subito | migliore amico di Josh; il numero apre solo il canale, il percorso resta opt-in |
| Simon | giorno 8 | «se hai dubbi sugli esercizi, scrivimi» (scelta) |
| Howard | giorno 11 | quando restituisce le chiavi |
| Daniel | giorno 13 | si fa dare il numero «per il romanzo» e scrive per primo |
| Magnus | giorno 13 | contatto per le 50 pagine |
| Barbara | giorno 18 | solo se Sara resta la mezz'ora in più |
| Jacob | giorni 19-21 | numero al locale (o da Joanie), messaggio del 21; se Sara risponde entra in rubrica |

### 10.3 Il rapporto = Interest con quattro soglie
Non serve una variabile `conoscenza`: le scene leggono `percorsi[x].interest`. Ogni step di chat dà +1 (+2 con la risposta più calda).

| Personaggio | A conoscenti | B in confidenza | C complici | D intimi |
|---|---|---|---|---|
| Simon | 5 | 10 | 16 | 22 |
| Howard | 4 | 9 | 14 | 20 |
| Daniel, Magnus, Joanie, Darius | 3 | 7 | 12 | 18 |
| Jacob (24/11/2026) | 5 | 12 | 18 | 25 |
| Barbara | 3 | 7 | 15 | 25 |

Il fisico resta sempre dietro la soglia di Corruption del percorso (mappa a tappe).

### 10.4 Scene fisse
| Gradino | Nella scena fissa |
|---|---|
| sotto B | resta com'è scritta |
| B | una o due frasi in più |
| C | l'incontro cambia: tono, porzione nuova, bivio |
| D | cambia ancora di più, entro la soglia di Corruption |

Ogni scena controlla solo le soglie che le servono. Episodio 1 (giorni 1-13): niente varianti, salvo verificare se Simon o Howard toccano B prima del 14.

### 10.5 Messaggi non scelti
- Trama e messaggi in entrata **non consumano lo slot**. Lo slot si può non usare (*«Sara leaves her phone face-down on the table.»*).
- In entrata: da B in su, massimo uno ogni 3-4 giorni per personaggio, mai due nello stesso giorno. Rispondere +1 Interest; ignorare nessun effetto. Daniel scrive per primo già dal 13.
- Josh può scrivere durante una chat con un altro: rispondere Josh +1; lasciarlo in sospeso Corr +1 solo se l'altra chat è a C.

### 10.6 Risposte asincrone («client/server»)
- Inviare consuma lo slot. Il messaggio entra in una coda con la **fascia di risposta calcolata all'invio e salvata** (`renpy.random`; ricaricare dopo l'invio non cambia nulla).
- Fasce: mattina, lavoro, pausa pranzo, sera, notte. A ogni inizio fascia si controlla la coda e arrivano le notifiche (*«Daniel replied.»*).
- Lo step si completa quando Sara risponde alla risposta; finché è in attesa, con quel contatto non si apre un nuovo step (gli altri sì).
- Spunte: consegnato, letto, sta scrivendo. **Tutti prima o poi rispondono.**

| Chi | Ritardo base |
|---|---|
| Joanie | subito, stessa fascia |
| Howard | subito, sempre (appiccicoso, inquietante) |
| Simon | la sera stessa |
| Darius | in fretta, risposte brevi |
| Jacob | di notte |
| Daniel | da una fascia a un giorno; legge subito |
| Magnus | 1-2 giorni, risposte lunghe |
| Barbara | solo in orario di lavoro, giorno lavorativo dopo |

Modificatori: sopra C una fascia prima; sopra D quasi subito (anche Daniel); fasce impossibili slittano alla prima utile; ±1 fascia casuale.
Risposta che arriva mentre Sara è con Josh: leggerla subito Susp +1 (e Corr +1 se il contatto è a C), oppure dopo senza effetti.

### 10.7 Solleciti
Sara può riscrivere a chi non ha ancora risposto; il sollecito usa lo slot.
| Chi | Effetto |
|---|---|
| Joanie, Howard | nessuno |
| Simon, Jacob, Darius | risposta una fascia prima, Interest +1 |
| Daniel | nessun anticipo; Corr +1, Conf −1 |
| Magnus | nessuno, lo dice con garbo |
| Barbara | Barbara −1, Conf −1 |

### 10.8 Serate alternative
- Primo mese: solo il **giorno 22** è sostituibile; le altre dal secondo mese, segnate nel calendario.
- Si può uscire con chi è almeno a C; da D, entro la soglia di Corruption, l'uscita può prendere una piega romantica con scelta esplicita.
- Josh: dirglielo (Susp +1, Josh +1 se innocente) o una scusa (Corr +1, segreto «uscita con X», scopribile da chi può vederla, es. Howard). Restare con Josh è sempre possibile.
- Ogni uscita = un set di immagini nuovo: poche per episodio.

### 10.9 Costi e metodo
- Costo di calcolo trascurabile per Ren'Py (pochi valori per 8 contatti, una coda breve). I costi veri: scrittura (circa 6 step × 8 personaggi nel primo mese), immagini delle uscite, test.
- Test: estendere l'autoplay con strategie «sempre lo stesso contatto» e «sparpagliata», seme casuale fisso.
- **Metodo:** dal giorno 14 si alternano **codice della giornata** (calendario e scene fisse con varianti) e **codice del percorso** (step di chat, messaggi in entrata, uscite di un personaggio), in file separati per percorso.

## 11. Discorsi, scambi e interruzioni (decisioni 18/11/2026, terza parte)

Approvate da Jody. **Sostituiscono gli «step numerati»** delle sezioni 3 e 10 e del primo codice (commit 1410e52): lo slot del giorno resta, ma quello che si gioca è un **discorso**.

### 11.1 Struttura
- **Gradino → discorsi → scambi.** Ogni personaggio ha un elenco di discorsi; ogni discorso è una conversazione di più scambi (Sara scrive, l'altro risponde, Sara ribatte...).
- Ogni discorso ha: un **gradino minimo**; eventuali **condizioni** (flag di trama, Corruption, Confidence); i **punti di interruzione** segnati da chi lo scrive; un **flag di fine** (es. `chat_simon_dieta`).
- Due tipi: **legati alla storia** (si aprono con i fatti vissuti, es. «dopo la festa», «se ha mandato le pagine a Magnus») e **generici** (un set nostro per personaggio: Simon allenamento, cibo, weekend; Magnus libri e scrittura; Howard la casa e la solitudine...).

### 11.2 Pesca
- Quando Sara usa lo slot con un contatto: se c'è un discorso **lasciato a metà**, si riprende da lì; altrimenti il gioco **pesca a caso** fra quelli disponibili (gradino e condizioni ok) e non ancora fatti. La pesca si decide al momento e resta salvata.
- Se non c'è niente di disponibile il contatto è **grigio**: *«Sara has nothing new to say to him… yet.»* Si riapre salendo di gradino o vivendo un fatto che apre un discorso legato alla storia. I segnaposto «da scrivere» compaiono solo nella prova degli sviluppatori.

### 11.3 Imbuto verso l'intimità
| Gradino | Discorsi | Di cosa |
|---|---|---|
| Estranei | **1** | la chat introduttiva, legata a come Sara ha avuto il numero; finirla senza frenare porta l'Interest almeno ad A |
| Conoscenti | 6-8 | vita quotidiana, lavoro, curiosità |
| In confidenza | 4-5 | confidenze, cose personali, primi complimenti |
| Complici | 3 | flirt, doppi sensi, segreti |
| Intimi | 1-2 | piccante, dietro la soglia di Corruption del percorso; adulti e consensuali |

### 11.4 Interruzioni (a caso: ogni partita è diversa)
A ogni punto di interruzione:
- **Sara** può mettere giù il telefono: il discorso resta aperto e si riprende con lo slot di un altro giorno. Reazioni: Howard le riscrive il giorno dopo (messaggio in entrata), Daniel fa finta di niente, Joanie manda «??», gli altri aspettano.
- **L'altro** può fermarsi, con una probabilità che dipende dal carattere; la ripresa entra nella coda delle risposte (10.6) con i suoi ritardi e riparte dallo scambio interrotto.

| Chi | Quanto spesso si ferma |
|---|---|
| Daniel | spesso, apposta: la lascia a metà |
| Magnus | dopo i messaggi lunghi («ne riparliamo») |
| Barbara | a fine orario di lavoro |
| Simon, Jacob | ogni tanto |
| Joanie, Darius | quasi mai |
| Howard | mai |

### 11.5 Effetti
- **Interest:** +1 alla prima bolla che Sara invia per iniziare un nuovo discorso e +1 ogni volta che sceglie una reazione calorosa già marcata nella chat. Riprendere un discorso o rispondere a un'apertura in entrata non dà il premio d'inizio. Alla fine restano +1 per il discorso completato o +2 se Sara ha scelto almeno una risposta calorosa. Le risposte fredde possono togliere punti.
- **Freno:** in ogni discorso di flirt c'è sempre una risposta per smorzare («Ok, stop. Goodnight.»): il discorso si chiude come fatto, senza Interest, e il personaggio per un po' non riapre discorsi di quel tipo. Le risposte coraggiose o piccanti hanno requisiti di Corruption/Confidence come nelle scene.
- **La chat resta sul telefono:** dopo un discorso «complici» o «intimi» il giocatore sceglie se **cancellarla** (Corr +1, Susp −1, come al giorno 21) o **lasciarla** (con Suspicion alta Josh può trovarla; si lega al finale del giorno 28).
- **Memoria nelle scene fisse:** il flag di fine discorso permette alle micro-varianti da B in su di citare proprio quella chat (in palestra Simon: «hai provato la colazione che ti dicevo?»).

### 11.6 Da dettagliare più avanti
- **Foto:** poche per personaggio, riusabili, quasi tutte ai gradini alti; le prime chat solo testo.
- **Quando si apre lo slot:** lo decide il codice della giornata (di solito la sera, a volte la pausa pranzo); Barbara risponde solo in orario di lavoro.
- **Metodo:** il «codice del percorso» (10.9) diventa scrivere discorsi: almeno 4 per personaggio per cominciare (32 in tutto), poi si allarga l'imbuto.

## 12. Sessioni libere a minuti

Ogni sessione libera ha un orario di inizio e di fine deciso dalla scena. Il giorno 14 va dalle **22:00 alle 23:00**, dopo la chat di trama del maglione, che resta fuori dal conteggio. Sara può cambiare contatto, attendere la prossima risposta o chiudere in anticipo. Allo scadere o scegliendo «Go to bed», passa alla CG della buonanotte. Lo stato di ciascuna chat è conservato per le sessioni successive.

- Ogni bolla inviata da Sara costa un minuto. Le bolle ricevute costano un minuto ciascuna quando Sara legge il blocco. Una notifica non costa tempo. Un blocco che eccede il tempo residuo resta interamente non letto.
- Il ritardo viene sorteggiato e salvato per ogni blocco. Howard risponde subito, Joanie in 1–4 minuti e Darius in 1–8. Simon può rispondere la sera, Jacob durante la notte, Barbara nei giorni e orari di lavoro. Daniel può arrivare dopo pochi minuti o diverse ore. Magnus normalmente aspetta da uno a due giorni. Il gradino di complicità può ridurre l’attesa.
- «Wait» avanza fino alla prossima risposta in viaggio o alla fine della sessione se nessuna può arrivare in tempo. Durante la lettura o l’invio in una chat, le altre possono generare notifiche e rimangono aperte in rubrica.
- I blocchi nelle chat di percorso hanno un punto di ripresa prima delle bolle in entrata, prima dell’invio e prima delle scelte. Le label salvate permettono di riprendere senza ripetere messaggi o effetti. Le scene di trama continuano a usare il flusso preesistente.
- La pesca controlla nello stesso modo i discorsi avviati da Sara e quelli in entrata. Oltre a Interest e rubrica, un argomento può richiedere un fatto di trama, una finestra oraria o entrambi. Una conversazione iniziata in un contesto valido conserva i messaggi e il punto di ripresa. Le condizioni dei singoli discorsi sono nella [tabella degli argomenti](argomenti-telefono.md#condizioni-di-trama-oltre-al-livello).
