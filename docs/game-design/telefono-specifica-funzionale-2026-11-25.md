# The Thin Line — Nuovo telefono: specifica funzionale approvata
**25 novembre 2026 · Progettazione, non implementazione**

## 1. Decisione e campo di applicazione
Ricostruire da zero il sistema delle conversazioni telefoniche per la distribuzione dell'episodio 2. I vecchi dialoghi possono fornire materiale da riutilizzare, ma non costituiscono l'architettura da conservare. Questa specifica consolida le regole iniziali, il Q&A e le sette decisioni finali del 25 novembre. Prevale sulle specifiche precedenti del telefono laddove incompatibili; le regole narrative non incompatibili restano valide. Riferimenti storici: [ripensamento iniziale](../narrative/telefono-registri-conversazione-2026-11-25.md), [telefono e percorsi dinamici](../telefono-e-percorsi-dinamici.md), [argomenti precedenti](../argomenti-telefono.md).
Gli otto interlocutori sono Howard, Jacob, Joanie, Daniel, Barbara, Magnus, Simon, Darius. La rubrica continua a rispettare l'acquisizione effettiva dei numeri. Non viene introdotto un nono percorso.

## 2. Tre modalità di iniziativa di Sara
### 2.1 Registro
Il giocatore sceglie il registro; il gioco estrae una linea disponibile, mai utilizzata, compatibile con quel registro e i suoi requisiti individuali.

| Registro | Condizione generale di apertura |
|---|---|
| Casuale | Sempre sbloccato |
| Amichevole | Interest di Sara verso il contatto > 5 |
| Flirt | Interest di Sara verso il contatto > 15 |
| Romantico | Almeno un bacio già avvenuto con il contatto |
| Sexy | Almeno un bacio già avvenuto con il contatto |

Le disuguaglianze sono strette: 5 e 15 esatti non bastano. Il bacio è un fatto narrativo, non una soglia di Interest; il telefono non deve sostituire gli sviluppi esterni. Anche un registro sbloccato è mostrato solo se contiene almeno una linea effettivamente disponibile. Ogni linea può richiedere ulteriori condizioni di giorno, Interest, eventi, precedenti conversazioni e progressione del rapporto. Estrazione casuale fra le linee idonee, senza ordine obbligatorio generale.
Prima dell'invio il giocatore vede il messaggio proposto e può confermarlo o annullarlo. Annullare non consuma né la linea né lo slot; per lo stesso contatto e registro l'anteprima rimane identica durante la giornata, salvo sopravvenuta invalidità narrativa. Il giorno successivo può essere effettuata una nuova estrazione.

### 2.2 Argomento specifico
Sara sceglie un argomento legato a qualcosa di accaduto, ad esempio parlare con Daniel di Magnus. Gli argomenti sono definiti durante la scrittura della trama e hanno requisiti e progressione propri. Non richiedono necessariamente un registro di apertura. Possono evolvere in registri diversi durante lo scambio.
**ARGOMENTO TELEFONICO** è una designazione esplicita di progettazione che può essere assegnata dall'autore o dall'assistente durante il lavoro narrativo. **Tutti gli avvenimenti IMPORTANTI sono anche TELEFONICI:** per ciascuno deve esistere almeno un argomento telefonico pertinente. Non tutti gli argomenti telefonici devono derivare da avvenimenti importanti.
Gli argomenti sono associati esplicitamente a interlocutori specifici. Solo alcuni avvenimenti diventano argomenti anche per altri personaggi; nessuna propagazione automatica a tutta la rubrica. Per ogni associazione si definiscono requisiti, informazioni effettivamente note al personaggio, contenuti, eventuali rivelazioni e approfondimenti. Non si costruisce una matrice universale di conoscenza: registrare solo le rivelazioni con conseguenze fattuali importanti.
Un argomento esaurito non compare finché non si sblocca una nuova linea.

### 2.3 Inchiesta
Disponibile quando l'inchiesta è attiva. Selezionandola si apre una casella di testo. Il giocatore digita una parola chiave o una frase; un dizionario predefinito di parole e sinonimi riconosce le espressioni pertinenti anche all'interno di una frase, senza IA generativa. Il contatto risponde con il dialogo associato se disponibile. Se non riconosce la richiesta, risponde genericamente di non sapere nulla: non rivelare se la parola è inesistente o se l'interlocutore è sbagliato.
Una stessa parola chiave presso lo stesso contatto può sbloccare un nuovo dialogo dopo eventi, nuove informazioni o altre testimonianze, ma mai riprodurre un dialogo già svolto. Le testimonianze possono essere vere, false, incomplete o depistanti; sono scritte a mano e coerenti con il personaggio. Il taccuino automatico registra informazioni investigative rilevanti e relativa fonte, non la loro attendibilità oggettiva.

## 3. Frequenza e disponibilità
Sistema ibrido:
- Una sola nuova conversazione per registro **complessivamente per contatto per giornata** (non una per ciascuno dei cinque registri).
- Nessun limite giornaliero numerico per argomenti specifici e inchiesta, fermo restando l'esaurimento delle linee, i requisiti e la disponibilità contestuale del telefono.
- Rispondere ai messaggi ricevuti e continuare una conversazione non consuma una nuova iniziativa per registro.
- Le chat canoniche obbligatorie restano distinte dalle iniziative libere.
La disponibilità del telefono durante la giornata era già oggetto delle regole precedenti; il Q&A non ha approvato una nuova regola di accesso per fasce o di distinzione lettura/scrittura. Verificare le condizioni effettive durante l'integrazione.

## 4. Ciclo di vita della conversazione
Una chat permanente per interlocutore, ma **una sola conversazione attiva per interlocutore**. Le conversazioni possono essere non iniziate, aperte/in attesa, concluse, abbandonate o scadute; gli stati sono concettuali e non impongono nomi tecnici.
- Nessun dialogo iniziato e definitivamente terminato, anche per abbandono o scadenza, è ripetibile. Identificativo univoco indipendente dal registro raggiunto. Escludere le linee consumate dalla selezione.
- Chiudere semplicemente l'interfaccia lascia aperta la conversazione; può proseguire anche in un altro giorno.
- Sara può congedarsi volontariamente in qualsiasi momento, chiudendo definitivamente la conversazione.
- Iniziare un nuovo argomento o una nuova conversazione con lo stesso contatto chiude definitivamente quella precedente. Non esiste una pila di conversazioni sospese da riprendere. Lo storico dei messaggi resta.
- Il cambio di argomento usa raccordi coerenti con l'ultimo messaggio: se era una domanda rimasta senza risposta, Sara si scusa per il cambio; se era un'affermazione, usa formule equivalenti a «Anyway…» o «Changing the subject…». Variare le locuzioni. Classificare i messaggi necessari a questo raccordo (domanda, affermazione, chiusura).
- Ogni conversazione può avere una scadenza propria o diventare obsoleta per eventi narrativi; una risposta in ritardo, se ancora pertinente, può suscitare una reazione caratteriale.
- Un incontro dal vivo può continuare o concludere una chat pertinente; in quest'ultimo caso la linea risulta esaurita anche sul telefono. In caso contrario resta aperta, salvo scadenze o incompatibilità narrative.
- La durata è variabile: da pochi scambi a conversazioni importanti più lunghe. Nessun numero fisso di scelte.

## 5. Dialoghi, registri e conseguenze
Alberi prevalentemente convergenti: le risposte generano battute e conseguenze differenti, ricongiungendosi a nodi comuni quando naturale. Ramificazioni realmente divergenti per decisioni narrative importanti. Evitare esplosioni combinatorie e ricongiungimenti incoerenti.
Il registro iniziale non obbliga il tono successivo: può attenuarsi, intensificarsi o cambiare. La linea conserva il proprio ID, non viene riclassificata a fine dialogo e consuma al massimo lo slot iniziale previsto.
Sara può ricambiare un flirt introdotto dall'interlocutore anche se il proprio Interest non supera 15. Romantico e sexy richiedono invece almeno un bacio anche nelle risposte di Sara. Gli interlocutori possono anticipare iniziative romantiche o sexy secondo personalità e condizioni narrative; non sono obbligati a rispettare le soglie di iniziativa di Sara. Le risposte di Sara restano soggette alle sue condizioni.
Le risposte disponibili mostrano normalmente solo il testo; un'impostazione facoltativa, disattivata di default, mostra il registro.
Le conversazioni ordinarie (registro, argomento, risposte in entrata) possono modificare Interest di Sara, Corruption, Confidence, Interest verso Josh e altre variabili quando giustificato. L'inchiesta non modifica l'Interest verso l'interlocutore (eccezione approvata; non estenderla automaticamente ad altre variabili). Le scelte sono la fonte prevalente delle variazioni, ma alcune battute ricevute possono produrre reazioni emotive autonome positive o negative di Sara.
Nessun tetto giornaliero ai punti: calibrare ogni effetto in base al contenuto, dando generalmente maggior peso agli incontri reali. Non introdurre valori numerici standard non approvati. Memorizzare solo fatti narrativi davvero significativi, con un uso futuro identificabile; non trasformare ogni risposta in un flag. Lo storico testuale e gli ID consumati sono distinti dalle variabili narrative.

## 6. Interesse reciproco e comportamento
L'Interest di Sara determina le sue iniziative; il comportamento altrui dipende dall'interesse dell'interlocutore verso Sara, dalla personalità e dal contesto. Il giocatore conosce solo la percezione soggettiva di Sara dell'interesse altrui, non il valore reale; la percezione può essere errata.

| Contatto | Modello di interesse verso Sara |
|---|---|
| Howard | Sempre molto alto |
| Jacob | Sempre molto alto |
| Joanie | Sempre molto alto |
| Daniel | Dipende dal confronto fra Interest di Sara verso Daniel e giorno corrente |
| Barbara | Sempre sereno e distaccato |
| Magnus | Sempre sereno e distaccato |
| Simon | Identico all'Interest di Sara verso Simon |
| Darius | Identico all'Interest di Sara verso Darius |

I valori numerici dei profili costanti e la reazione precisa di Daniel nei casi maggiore, minore e uguale al giorno non sono stati approvati. Non inventarli.
Ogni contatto ha un profilo comportamentale di base dinamicamente modificato da eventi, interesse, iniziative e silenzi, preferendo le variabili esistenti. Un registro non ricambiato produce una reazione specifica del personaggio, non un rifiuto standard. Anche il silenzio e le mancate risposte possono influire su frequenza, tono e comportamento dal vivo; definire le singole reazioni nei profili, non introdurre automaticamente punteggi nuovi.

## 7. Messaggi in entrata e tempi
Sistema misto: prima risposta immediata oppure dopo ore narrative o il giorno successivo; a conversazione avviata gli scambi sono prevalentemente immediati. Tempi personalizzati per interlocutore, interesse e circostanze.
I messaggi in entrata possono essere spontanei (probabilità specifica del personaggio, non necessariamente proporzionale all'interesse) o attivati da eventi narrativi. I messaggi spontanei aspettano la conclusione della conversazione aperta; quelli narrativi possono interromperla e chiuderla definitivamente, usando raccordi appropriati anche da parte dell'interlocutore.
La mancata risposta viene gestita secondo personalità; frequenze, ritardi e condizioni individuali ancora da parametrizzare.

## 8. Privacy, incontri e continuità
Privacy assoluta del cellulare: Sara ha il blocco tasti, Josh non accede alle conversazioni; la ricezione dei messaggi non aumenta la Suspicion. Non introdurre letture clandestine o sistemi di notifiche compromettenti.
Gli appuntamenti possono essere prestabiliti o dinamici nelle fasce libere, rispettando disponibilità e requisiti. Distinguere appuntamenti importanti e incontri ordinari; non sostituire eventi canonici indispensabili. Restano da definire le concrete condizioni e modalità di pianificazione. Mantenere le regole già approvate sugli incontri spontanei dopo Interest > 50, dove applicabili ([specifica](regola-interesse-superiore-50-incontri-spontanei.md)).
Dopo l'acquisizione del numero, le scene personali dal vivo devono rispettare il rapporto raggiunto, i fatti significativi e le informazioni effettivamente condivise, senza riproporre conoscenze già superate.

## 9. Produzione e compatibilità
Distribuire il numero di linee in base a personalità, registri e contenuti effettivamente raggiungibili nell'episodio. Sbloccare nuove linee con calendario e progressione relazionale. Non mostrare segnaposto, registri vuoti o argomenti esauriti. Non imporre quote identiche fra i personaggi.
Migrazione selettiva automatica dei salvataggi dell'episodio 1: conservare progressione narrativa, numeri acquisiti, variabili, fatti significativi e messaggi canonici. Sostituire l'architettura delle conversazioni libere. Definire e testare la corrispondenza dei vecchi ID e dei fatti rilevanti per non violare il divieto di ripetizione; non promettere compatibilità tecnica prima dei test.
Dialoghi del gioco in inglese, specifiche e commenti di progettazione in italiano.

## 10. Tracciato di lavoro proposto (non schema tecnico definitivo)
Per ogni linea descrivere: ID stabile, contatto, modalità, registro iniziale o argomento/parole chiave, direzione di iniziativa, requisiti, eventuali scadenze, apertura, nodi e alternative, effetti e soli fatti significativi, esiti di chiusura e possibili raccordi/incontri dal vivo. Il formato dati definitivo verrà scelto durante l'implementazione.
Ordine: catalogare retroattivamente gli avvenimenti IMPORTANTI e gli ARGOMENTI TELEFONICI; definire i profili degli otto contatti; costruire gli otto alberi; assegnare requisiti e scrivere dialoghi; ricostruire controller e interfaccia Ren'Py; migrare e testare.
Casi di test essenziali: soglie esatte 5 e 15; bacio per romantico/sexy; flirt in risposta sotto soglia; registro esaurito; annullamento e riproposizione nello stesso giorno; limite per contatto e non per singolo registro; cambio argomento su domanda o affermazione; risposta tardiva/scadenza; interruzione narrativa; chiusura volontaria e semplice uscita; completamento dal vivo; riconoscimento sinonimi e testimonianze successive; inchiesta senza Interest; assenza di accesso di Josh; salvataggio precedente.

## 11. Stato delle decisioni
La progettazione funzionale generale è conclusa. I dettagli individuali, gli argomenti effettivi, le parole chiave, le soglie ulteriori, i valori dei punti, le probabilità, i tempi, il comportamento preciso di Daniel e la pianificazione tecnica degli appuntamenti restano da definire durante la costruzione degli alberi. Gli esempi numerici e narrativi del Q&A non sono quote o scene canoniche approvate.
La preferenza C sulla variazione dell'Interest, inizialmente formulata con un dubbio sulla continuità delle chat, è stata mantenuta esplicitamente nelle decisioni successive: tutte le modalità non investigative possono modificarlo. La domanda iniziale sugli appuntamenti è stata poi risolta con l'approvazione degli appuntamenti anche dinamici.
**Questo documento non modifica il codice, non riscrive i dialoghi e non implementa la migrazione.**

## 12. Punti fermi aggiunti da Jody dopo la prima prova (25/11/2026, sera)
La prima realizzazione (commit `98d7e3a`) è stata **ritirata**: grafica cambiata, conversazioni che finivano subito, nessun tempo di attesa. Il telefono nel gioco è tornato a quello del 24/11. Ogni nuova realizzazione parte da lì e rispetta tre vincoli, che prevalgono sul resto della specifica:

1. **La grafica resta quella esistente.** Schermate `telefono`, `telefono_chat` e `scelta_telefono` (pannello a destra, orologio, bolle, stato della risposta, scelte accanto al telefono). Le funzioni nuove (registri, argomenti, congedo) entrano in quella grafica; niente menu generici al suo posto.
2. **Restano i tempi di attesa di ogni personaggio** e l'orologio in minuti delle sessioni (`TELEFONO_ATTESE`, orari in cui rispondono, ripresa della chat in sospeso, notifica all'arrivo). Nessuno risponde all'istante, salvo chi già lo faceva (Howard).
3. **Le conversazioni non finiscono subito.** Sono chat vere, a più scambi e con scelte, con un inizio, uno sviluppo e una chiusura. Lunghezza da approvare.

### 12.1 Cosa è applicato sul telefono vecchio (25/11, notte)
- **Tipi** (Jody): Casual, Friendly, Flirt, Sexting. Le 113 chat esistenti sono classificate: A e introduzioni = Casual, B = Friendly, sette B già sensuali = Flirt (Daniel B1 B4 B5, Magnus B3 B4, Jacob B1 B4). Sexting: nessuna chat ancora; un tipo senza chat non si mostra.
- **Soglie:** Friendly oltre 5, Flirt oltre 15, Sexting dopo un bacio (`bacio_<chiave>`). Una chat nuova per tipo al giorno per contatto; gli argomenti non contano. Anteprima confermabile, uguale per tutto il giorno.
- **Argomenti:** undici chat legate a un fatto si scelgono per nome; prima chat nuova `howard_t1`, «The sauce on the blouse».
- **Chat in sospeso:** riprendere, cambiare discorso (raccordo secondo l'ultimo messaggio) o salutare. La chat introduttiva non si può perdere.
- **Sere 17, 18 e 19:** telefono a orario, con le CG già fatte.
- **Testi nuovi:** si scrivono in `tools/telefono/<chiave>.txt` e si compongono con `tools/telefono/componi.py`.
- **Casual** sempre aperto, senza gradino; l'introduzione viene prima e ogni contatto ne gioca una sola.
- **Privacy:** tolte la Suspicion dai messaggi letti davanti a Josh e la scelta di cancellare le chat.
- **Interesse degli altri** (`interesse_altrui`): Howard, Jacob e Joanie alto; Barbara e Magnus sereno; Daniel acceso con Interest almeno pari al giorno; Simon e Darius specchio della soglia Flirt. Regola chi può prendere iniziative romantiche per primo.
- **Scadenze e incontri dal vivo** (`scade`): le chat legate a una giornata si chiudono il giorno dopo; «The parcel» si chiude se Sara ritira il pacco di persona.
- **Preferenze:** «Show chat type», spenta all'inizio.
- **Da fare:** frequenza con cui scrivono per primi (valori da approvare), testi nei diversi toni, reazioni al silenzio e al flirt non ricambiato, messaggi di trama che interrompono, appuntamenti, inchiesta dal 22, argomenti degli altri, Flirt e Sexting. Test: `telefono_tipi`.

### 12.2 Chi scrive per primo (tabella approvata da Jody, 25/11; «al limite editeremo»)

| | Ogni sera | Giorni fra due | Quando | Se Sara non risponde |
|---|---|---|---|---|
| Howard | 60% | 1 | sempre | il giorno dopo: «Did I say something wrong?» |
| Joanie | 45% (80% il 17 e il 19) | 2 | sempre | «??» e ci ride sopra |
| Jacob | 35% | 3 | dopo le 22 | niente |
| Daniel | 35% | 3 | sotto il giorno solo del romanzo | sparisce finché non lo cerca Sara |
| Simon | 25% (50% il 15 e il 17) | 3 | 18-23 | niente |
| Darius | 20% (40% il 14 e il 16) | 4 | sempre | «Lol, busy. Got it» |
| Magnus | 10% | 7 | solo romanzo | niente |
| Barbara | 20% | 4 | giorni di lavoro | niente |

Al massimo due messaggi nuovi per sera, in ordine a sorte; aspettano nella rubrica («New message») e non aprono la chat da soli. I fatti vissuti insieme vengono prima delle chat generiche. Rispondere dà Interest +1. Valori in `ENTRATE` e `SILENZIO` (`game/core/telefono_temporizzato.rpy`). Da fare nelle scene: la battuta di Simon e la freddezza di Barbara al lavoro.

### 12.3 Flirt non ricambiato (25/11)
Riguarda i Flirt e i Sexting cominciati da Sara, secondo `interesse_altrui`:
- **Daniel** con Interest sotto il giorno: tre chat proprie (due Flirt, un Sexting). Non rifiuta: non insegue, e dice a Sara come ritrovarlo. Finite quelle, il tipo sparisce finché l'Interest non torna almeno pari al giorno.
- **Magnus e Barbara** (sereni): il primo Flirt e il primo Sexting sono una chat in cui prendono tempo; dopo si aprono le altre.
- **Howard, Jacob, Joanie** (alto) e **Simon, Darius** (specchio): sempre ricambiati quando Sara può aprire il tipo.
Nessuna penalità: le risposte calde danno Interest come nelle altre chat. Id con `_n`, `ricambiato=False`.
