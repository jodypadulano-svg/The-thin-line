# The Thin Line — Argomenti dei discorsi al telefono

Tabella di Jody, 18/11/2026. Ogni numero è un **discorso autonomo**, composto da più scambi (vedi [telefono e percorsi dinamici](telefono-e-percorsi-dinamici.md), sezione 11). I livelli indicano il **requisito minimo**: non obbligano Sara a flirtare. L'introduzione è l'**unica chat da estranei**: finirla porta l'Interest almeno ad A.

Totale: 8 personaggi × 19 discorsi = **152 discorsi**. Si scrivono per gradi: prima l'introduzione e 3 discorsi A per personaggio (32), poi si allarga. **Nel gioco un discorso si registra solo quando è scritto** (niente segnaposto per il giocatore).

**Id dei discorsi:** `<personaggio>_<livello><numero>`, es. `simon_intro`, `simon_a2`, `daniel_c1` (chiavi: simon, howard, daniel, editore = Magnus, capa = Barbara, ex = Jacob, amica = Joanie, amico = Darius). Il flag di fine è `chat_<id>`.

### Apertura del telefono libero al giorno 14

Sono scritti **113 discorsi** tra introduzioni, Conoscenti e Confidenza. Sally sblocca il telefono in cucina. La sera, la chat di trama con Joanie precede lo slot libero quando scatta il suo ramo e non consuma il turno. Il [controller](../game/core/telefono.rpy) estrae fra i discorsi disponibili per il contatto in rubrica. Man mano che l’Interest sale, restano estraibili anche quelli dei livelli inferiori ancora da completare. «Introduzione» e «A1» indicano il livello minimo e il numero in catalogo. In entrata, sotto Confidenza, sono estraibili solo i discorsi con `scrive_lui=True`, fra questi l’introduzione di Daniel.

**Continuità da completare.** Daniel A1 richiede `chat_daniel_intro` perché riprende una battuta dell’introduzione. Eventuali richiami al caffè, alla lampadina, al maglione o alle confidenze della terrazza richiedono battute condizionali. Per riprendere la risposta precisa di Sara sulle proprie sensazioni servirebbe anche registrare quella scelta.

## Simon

| Livello | Discorsi |
|---|---|
| Introduzione | Consigli per il prossimo allenamento |
| A — Conoscenti (8) | 1. Dolori muscolari · 2. Alimentazione · 3. Musica in palestra · 4. Esercizi preferiti · 5. Weekend · 6. Locali notturni · 7. Abbigliamento sportivo · 8. Obiettivi fisici |
| B — Confidenza (5) | 1. Insicurezze sul corpo · 2. La vita da single · 3. Come lui vede Sara · 4. Le sue precedenti relazioni · 5. Il piacere di sentirsi desiderati |
| C — Complicità (3) | 1. Complimenti sul corpo · 2. Allenarsi da soli insieme · 3. Una serata fuori dalla palestra |
| D — Intimità (2) | 1. Attrazione reciproca · 2. Fantasie e desideri di Sara e Simon |

## Howard

| Livello | Discorsi |
|---|---|
| Introduzione | Ringraziamento per le chiavi restituite |
| A — Conoscenti (8) | 1. Vita condominiale · 2. Problemi domestici · 3. Cucina casalinga · 4. Film in televisione · 5. Animali domestici · 6. Piccoli favori · 7. Abitudini quotidiane · 8. Solitudine del weekend |
| B — Confidenza (5) | 1. Il desiderio di una famiglia · 2. Le occasioni perdute · 3. La paura di invecchiare solo · 4. Sentirsi finalmente ascoltato · 5. Sara come presenza rassicurante |
| C — Complicità (3) | 1. Quanto gli manca Sara · 2. Le abitudini domestiche condivise · 3. Sentirsi a casa insieme |
| D — Intimità (2) | 1. Essere importanti l'uno per l'altra · 2. Immaginare una quotidianità comune |

**Introduzione · Estranei (`howard_intro`).** Sara lo ringrazia di nuovo per aver ritrovato le chiavi. Howard dice di averle trovate sotto le scale, le offre il suo aiuto e le chiede se Josh è rientrato bene la sera prima, perché ha sentito la porta. Il retroscena finale mostra al giocatore la copia della chiave.

**A1 · Conoscenti (`howard_a1`).** Sara chiede chi sposta i mobili a mezzanotte. Howard conosce gli orari dei vicini e sa che Sara esce alle 8:20. Lei può chiedergli come lo sa o ringraziarlo per l’avvertimento sul gatto. Lo scambio parte dalla familiarità fra vicini e funziona anche prima dell’introduzione.

**Continuità comune.** Il numero entra in rubrica solo con «Save it.» al giorno 11 (`ep1_d11_numero_howard` e `da_numero("howard")`), indipendentemente dall’invito a entrare. Nel ramo dell’abbraccio (`ep1_d11_abbraccio`, `ep1_d11_capisce_howard`) Sara coglie l’interesse di Howard e ride della battuta. Con la stretta di mano resta nel dubbio. Se entra al giorno 11 (`ep1_d11_visita`), prende un caffè nelle tazze nuove e gli legge un brano del romanzo. Il secondo caffè è facoltativo e, con `ep1_d11_capisce_howard`, può portare agli sguardi e alla scelta sui bottoni.

Al giorno 12 Howard ha letto due volte l’articolo e comprato tre copie in ogni ramo. Se Sara rifiuta (`ep1_d12_rifiuta_invito`), le dà il giornale sul pianerottolo. Se entra, entrambi i rami segnano `ep1_d12_visita` e incrementano `howard_visite`. Il contatore parte dalla visita del giorno 9. Sotto 2 prima di entrare, Sara legge l’articolo ad alta voce e beve sherry nelle tazze nuove. Da 2 in su, cambia la lampadina e sente la battuta di Howard sulla scaletta. Solo se sceglie di riderci su scatta `ep1_d12_ride_battuta`. Un richiamo deve rispettare il ramo, compresa la differenza fra la battuta sentita e la reazione scelta. La copia della chiave e il calendario che si vede dopo due rifiuti sono informazioni riservate al giocatore.

Fonti: [chat di Howard](../game/percorsi/chat_howard.rpy), [giorno 11](../game/episodio1/ep1_giorno11.rpy), [giorno 12](../game/episodio1/ep1_giorno12.rpy).

## Daniel

| Livello | Discorsi |
|---|---|
| Introduzione | Il romanzo e Magnus dopo il messaggio dell’1:12 |
| A — Conoscenti (8) | 1. Il libro di Sara · 2. Ambizione professionale · 3. Ristoranti eleganti · 4. Automobili · 5. Viaggi di lusso · 6. Gusti musicali · 7. Il valore del successo · 8. Battute sul lavoro |
| B — Confidenza (5) | 1. Cosa rende attraente un uomo · 2. La sicurezza in sé · 3. Le insoddisfazioni nascoste · 4. Le donne che lo hanno colpito · 5. La differenza tra amore e desiderio |
| C — Complicità (3) | 1. Provocazioni su Josh · 2. Il piacere delle sfide · 3. Un invito riservato |
| D — Intimità (2) | 1. Confessare l'attrazione · 2. Esplorare i limiti di una relazione segreta |

**Introduzione · Estranei (`daniel_intro`).** Se scrive Sara, dice di aver visto il messaggio dopo la festa e sposta il discorso sul romanzo. Se scrive Daniel, dice di aver promesso a Magnus di chiedere del manoscritto e domanda quante pagine ci siano. Seguono le centoventi pagine, la battuta sul talento e la domanda su cosa abbia letto Josh.

**A1 · Conoscenti (`daniel_a1`).** Sara contesta il giudizio di Daniel sul suo talento. Lui ricorda come le è cambiata la voce alla festa e le chiede una pagina. Sara può rifiutare o mandarla (`daniel_prima_pagina`). Con Confidence 25 può anche chiedergli di indovinare il tema. L’apertura «You said talent hides» riecheggia l’introduzione, quindi A1 si sblocca dopo `chat_daniel_intro`.

**Continuità comune.** Sara conosce già Daniel e Magnus. Daniel si è fatto uno squillo dal telefono di Sara alla festa (`da_numero("daniel")`) e le ha scritto all’1:12 senza ricevere risposta. I quattro messaggi incrociano `ep1_d13_cerniera` e `ep1_d13_pranzo_forse`. Daniel richiama il collo inclinato e il «maybe» se sono avvenuti entrambi, la cerniera se c’è stato solo quel gesto, le cinquanta pagine e il pranzo se c’è stato solo il «maybe», altrimenti «Brave girl». Al mattino del 14 rimane quel messaggio e i tre puntini sono spariti. Il ramo `ep1_d13_pranzo_no` indica «Josh will know». Se Sara confermerà il pranzo del 18, dovrà informare Josh prima di andarci qualora abbia promesso «Josh will know». **Nuova decisione del 23/11:** al giorno 15 Sara manda la conferma a Daniel **solo se sceglie di litigare con Josh**, dopo che lui ha letto il romanzo senza permesso. La conferma è una **chat di trama visibile, separata dai discorsi liberi**; Daniel risponde con una battuta che ferisce indirettamente Josh, ignaro della lite. **Senza litigio non c'è conferma automatica, quindi il pranzo del 18 può essere evitato.** La chat libera del 14 e le introduzioni A non devono anticipare/contraddire la scelta del giorno 15. Vedi [specifica della scena](narrative/giorno15-josh-manoscritto-daniel-2026-11-23.md).

Fonti: [chat di Daniel](../game/percorsi/chat_daniel.rpy), [giorno 13](../game/episodio1/ep1_giorno13.rpy), [giorno 14](../game/episodio2/ep2_giorno14.rpy), [decisioni sui giorni 17–18](decisioni.md#giorni-1718--consegna-del-maglione-e-pranzo-con-daniel-22112026).

## Magnus

| Livello | Discorsi |
|---|---|
| Introduzione | Due versioni previste nel sistema: «Le cinquanta pagine del manoscritto» (dopo l'invio) oppure «Sto ancora aspettando quelle pagine» (solo se la chat avviene **prima della sera del giorno 15**). Dal giorno 15 Sara invia sempre le pagine, quindi dopo quella sera si usa soltanto la prima versione. |
| A — Conoscenti (8) | 1. Scrittori preferiti · 2. Libri controversi · 3. Scrivere ogni giorno · 4. Cinema e letteratura · 5. Viaggi culturali · 6. Collezionismo · 7. La vita editoriale · 8. Il talento di Sara |
| B — Confidenza (5) | 1. Le sue esperienze passate · 2. La paura di non essere all'altezza · 3. Bellezza e maturità · 4. Il potere delle parole · 5. Il bisogno di essere compresi |
| C — Complicità (3) | 1. Una musa per uno scrittore · 2. La seduzione intellettuale · 3. Un incontro privato |
| D — Intimità (2) | 1. Confessioni molto personali · 2. Desiderio e differenza d'età |

## Barbara

| Livello | Discorsi |
|---|---|
| Introduzione | Una richiesta professionale dopo il lavoro |
| A — Conoscenti (8) | 1. Scadenze in redazione · 2. Giornalismo · 3. Moda e stile · 4. Trucco e immagine · 5. Le colleghe · 6. Eventi mondani · 7. Il carattere delle donne · 8. Ambizione professionale |
| B — Confidenza (5) | 1. Il suo divorzio · 2. Le donne indipendenti · 3. Come valorizzare la propria immagine · 4. La fiducia fra donne · 5. Cosa pensa davvero di Sara |
| C — Complicità (3) | 1. Complimenti personali · 2. La vita privata di Barbara · 3. Un invito fuori dall'ufficio |
| D — Intimità (2) | 1. Ammettere un'attrazione · 2. Desiderio di esclusività e dedizione |

## Jacob

| Livello | Discorsi |
|---|---|
| Introduzione | Ritrovarsi dopo tanto tempo |
| A — Conoscenti (8) | 1. Vecchi amici · 2. Ricordi divertenti · 3. Musica del passato · 4. Il locale del primo incontro · 5. Come sono cambiati · 6. Vacanze passate · 7. Le rispettive vite · 8. Nostalgia della giovinezza |
| B — Confidenza (5) | 1. Ricordi della relazione · 2. Perché si sono lasciati · 3. Il tradimento · 4. Cosa gli manca di Sara · 5. Le differenze fra ieri e oggi |
| C — Complicità (3) | 1. Ricordi romantici · 2. L'attrazione che ritorna · 3. Un incontro da soli |
| D — Intimità (2) | 1. Desideri mai dimenticati · 2. Esclusività, gelosia e libertà |

## Joanie

| Livello | Discorsi |
|---|---|
| Introduzione | La consueta chiacchierata fra amiche |
| A — Conoscenti (8) | 1. Palestra e Simon · 2. Shopping · 3. Il fidanzato di Joanie · 4. Gossip · 5. Serie televisive · 6. Abbigliamento · 7. Programmi del weekend · 8. Piccoli problemi quotidiani |
| B — Confidenza (5) | 1. Confidenze sulla coppia · 2. Le insicurezze di Sara · 3. Il desiderio di sentirsi belle · 4. Consigli su Jacob · 5. La paura di cambiare vita |
| C — Complicità (3) | 1. Amicizie che diventano indispensabili · 2. Segreti confidati soltanto a Joanie · 3. La paura di perdere la migliore amica |
| D — Intimità (2) | 1. Sentimenti oltre l'amicizia · 2. Immaginare una vita insieme |

**Introduzione · Estranei (`amica_intro`).** Sara scrive «Are you awake? I'm bored.» oppure Joanie apre in entrata con «BORED. ENTERTAIN ME.» quando il livello consente la pesca in entrata. Mark sta guardando il calcio. Joanie chiede gossip e Sara può menzionare Barbara e la scollatura oppure svicolare. La chat si chiude con un saluto affettuoso fra amiche.

**A1 · Conoscenti (`amica_a1`).** Sara apre lamentandosi delle gambe dopo la palestra. Con Interest Simon almeno 5, Joanie riferisce il complimento sullo squat. Sotto 5, dice che Simon ha chiesto dove fosse Sara l’ultima volta. Sara può liquidare la battuta o mostrare curiosità (`caldo()` e Simon +1). Joanie propone la palestra insieme giovedì e i leggings neri. La soglia di Interest non indica che Sara abbia scelto la correzione con le mani sui fianchi al giorno 13 (`ep1_d13_mani_simon`), né che l’abbia raccontata a Joanie.

**Continuità comune.** Joanie è già in rubrica. All’1:12 del giorno 13 chiede il resoconto della terrazza prima che scriva Daniel. Se scatta `ep1_d13_cerniera`, Sara racconta la cerniera e il bacio all’orecchio. Solo in quel ramo Joanie le chiede cosa ha provato e Sara sceglie se dire che avrebbe voluto ripeterlo, raccontare quanto l’abbia colta di sorpresa o tenersi la risposta. Altrimenti racconta che ha preferito occuparsi da sola della cerniera. Joanie sa quale risposta Sara ha dato sul pranzo. La sera del 14, con `ep1_d13_pranzo_forse` o `ep1_d13_pranzo_no`, `ep2_d14_maglione` riprende quella risposta e registra l’ordine del maglione (`ep2_d14_maglione_ordinato`). Un richiamo allo scambio può usare l’ordine se avvenuto e il pranzo come possibilità. Il flag della cerniera da solo non dice che cosa Sara abbia confidato sulle proprie sensazioni.

Fonti: [chat di Joanie](../game/percorsi/chat_amica.rpy), [giorno 13](../game/episodio1/ep1_giorno13.rpy), [giorno 14](../game/episodio2/ep2_giorno14.rpy).

## Darius

| Livello | Discorsi |
|---|---|
| Introduzione | Un messaggio amichevole su Josh |
| A — Conoscenti (8) | 1. Amici comuni · 2. Ricordi delle superiori · 3. Musica · 4. Serate in compagnia · 5. Josh da ragazzo · 6. Videogiochi · 7. Programmi del weekend · 8. Abitudini quotidiane |
| B — Confidenza (5) | 1. Il rapporto con Josh · 2. I lati meno conosciuti di Darius · 3. Le qualità che Sara apprezza negli uomini · 4. Come cambia un'amicizia · 5. Sentirsi a proprio agio insieme |
| C — Complicità (3) | 1. Un gioco di provocazioni · 2. Confronti con Josh · 3. Una complicità da nascondere |
| D — Intimità (2) | 1. Parlare apertamente della loro complicità e di cosa vogliono da Josh · 2. Immaginare un diverso equilibrio tra loro tre |

## Condizioni di trama (oltre al livello)

| Discorso | Si apre solo se | Stato |
|---|---|---|
| Howard A3, Lasagne | Dalle 17:00 alle 20:29, quando ha senso offrire un piatto caldo | filtro nel codice |
| Howard A6, Pacco del corriere | Dal giorno 17, solo dopo la consegna effettiva del pacco di Joanie a Howard | filtro nel codice, evento da scrivere |
| Howard B3, Insonnia | Dalle 22:00 alle 01:59 | filtro nel codice |
| Howard B5, Corriere atteso | Dal giorno 17, soltanto nel giorno in cui Sara aspetta un corriere e ha un turno serale | filtro nel codice, evento da scrivere |
| Daniel A1, Il libro di Sara | Dopo `chat_daniel_intro`, che contiene la battuta sul talento richiamata in apertura | filtro nel codice |
| Daniel A8, Battute sul lavoro | Nel giorno registrato in `ep2_relazione_trimestrale_josh`, dopo che Josh ha presentato il rapporto | filtro nel codice, evento da collegare |
| Simon A1, Dolori muscolari | Il giorno dopo una seduta effettiva. Il 14 usa `ep1_d13_palestra`; le sedute successive registrano la data in `ep2_ultimo_allenamento_simon` | filtro nel codice |
| Joanie A2, Shopping | Alla vigilia dell'uscita prevista, registrata in `ep2_shopping_joanie_vigilia` | filtro nel codice, evento da collegare |
| Darius, Introduzione sul compleanno | Quando sono aperti i preparativi di Josh (`ep2_preparativi_compleanno_josh`). Il discorso sugli amici comuni A1 rimane disponibile anche a Estranei | filtro nel codice, evento da collegare |
| Darius A4, Serate in compagnia | Il giorno dopo la serata con gli amici, registrata in `ep2_serata_amici_giorno` | filtro nel codice, evento da collegare |
| Barbara, Introduzione e A1 | Il pezzo extra è stato inviato (`ep2_pezzo_extra_inviato_barbara`); per A1 deve esserci una scadenza effettiva di venerdì (`ep2_scadenza_redazione_venerdi`). A2, sul giornalismo, resta disponibile anche a Estranei | filtro nel codice, eventi da collegare |
| Barbara A3, A4 e B3 | Vigilia della riunione con sponsor (`ep2_riunione_sponsor_vigilia`), sessione foto riprogrammata (`ep2_sessione_foto_riprogrammata`) e vigilia dell'intervista col consigliere (`ep2_intervista_consigliere_vigilia`) | filtro nel codice, eventi da collegare |
| Magnus, introduzione | «Le cinquanta pagine» dopo l'invio **obbligatorio** della sera del giorno 15; «Sto ancora aspettando» solo se la chat è giocata **prima dell'invio** | aggiornato 23/11 |
| Joanie B4, Consigli su Jacob | Jacob è tornato (giorno 19): il ritorno al locale resta una sorpresa | approvato |
| Daniel C1, Provocazioni su Josh | nessuna condizione di trama: basta il livello C (provoca su Josh già dalla cena del giorno 3) | approvato |
| Tutto Jacob | Sara ha il suo numero (giorni 19-21) | già garantito dalla rubrica |
| Livello D di tutti | oltre la soglia di Corruption del percorso | regola generale |

Ricognizione del 23/11. Le 113 registrazioni dei percorsi sono state controllate sul testo giocabile. Le abitudini ricorrenti, i ricordi e gli inviti che nascono nello scambio possono essere pescati quando il rapporto lo permette. Le righe sopra richiedono un evento già avvenuto o esplicitamente in programma. Le condizioni relative al giorno registrano il numero della giornata e limitano l’apertura del discorso alla data prevista. Magnus A7 parla delle cinquanta pagine di Sara solo se le ha ricevute. Jacob resta legato alla consegna del numero dopo il rincontro.

## Chiarimenti approvati da Jody (18/11/2026)

- **Simon D2:** le fantasie sono di Sara e Simon come coppia.
- **Darius D1:** riformulato sulla complicità e su cosa vogliono da Josh (coerente con la scheda: la sostituzione di Josh, non una storia romantica classica).
- **Daniel C1:** nessuna condizione di trama.
- **Magnus:** due introduttive alternative a seconda del momento della chat; da dopo l'invio obbligatorio del giorno 15 si usa sempre «Le cinquanta pagine». Se ne gioca una sola.
- **Joanie B4:** solo dopo il ritorno di Jacob.

## Toni dei livelli A e B (Q&A con Jody, 18/11/2026)

Riferimento di stile: la bozza approvata di Simon A1 «Dolori muscolari» (inglese, messaggi corti, pensieri di Sara fra i messaggi, 2-3 pezzi, ~10 messaggi, risposte neutra/calda/coraggiosa con Confidence 25, un seme di trama, un flag per le scene fisse, emoticon :) ;) ).

- **Simon:** in B complimenti **solo sui progressi** («sei migliorata tantissimo»); il personale resta fuori, il flirt vero comincia in C.
- **Howard:** il disagio si vede **sempre dal modo di scrivere** (troppi messaggi, troppo presto, sa cose che non dovrebbe sapere, battute fuori luogo); in circa **una chat su tre**, le più manipolatorie, un breve **retroscena** testuale dal suo lato. Sara non nota niente.
- **Daniel:** **piccole frecciate su Josh già da A**. Difenderlo: Josh +1; lasciar correre: niente; riderci su: risposta calda per Daniel e Corruption +1.
- **Magnus:** **esercizi di scrittura già da A**; Sara sceglie fra versione pudica (niente), sensoriale (Confidence +1) e audace (requisito di Confidence, calda). In B gli esercizi diventano più sensuali. Messaggi lunghi ed eleganti, niente emoticon, firma «M.».
- **Barbara:** **piccoli ordini personali già da A** (abiti, trucco): obbedire (Barbara +1 e flag per la scena del giorno dopo), ironizzare (niente), rifiutare (Confidence +1; lei sembra accettare ma ci riprova). **Al massimo 2-3 ordini** fra A e B. Non nomina mai il modo di fumare.
- **Jacob:** in A **solo nostalgia**; **allusioni al passato fisico da B** (ricordare con un sorriso = calda, lasciar cadere = neutra, chiudere = «Jacob. Don't.»). Sul tradimento **non chiede mai scusa davvero**.
- **Joanie:** **la tifosa**: chiede di Simon, Daniel, poi Jacob a seconda di come vanno quei percorsi; da B rari **indizi ambigui** che coglie solo il giocatore («Josh is lucky. Someone is, anyway.»).
- **Darius:** **completamente leale a Josh fino a C**: in A e B è l'amico di sempre, la svolta arriva come sorpresa. Senza le risposte calde di Sara le sue chat restano fra amici (percorso opt-in).

## Flag di trama usati dai discorsi (da impostare nelle giornate)

| Flag | Dove va impostato | Usato da |
|---|---|---|
| `ep2_pacco_joanie_da_howard` | giorno 17 o dopo, solo se il corriere lascia effettivamente a Howard il pacco ordinato da Joanie. Togliere il flag quando il pacco viene ritirato. | Howard A6 |
| `ep2_corriere_atteso_turno_sara` | salvare il numero della giornata in cui Sara si aspetta un corriere e fa il turno serale | Howard B5 |
| `ep2_pagine_magnus` | giorno 15, **sempre**: Sara invia a Magnus la versione **riscritta** in cui la protagonista sceglie di proseguire il tradimento, indipendentemente dalla lite con Josh | Magnus, introduzione (versione «Le cinquanta pagine»; il ramo «non le ha mandate» è ora obsoleto dal giorno 15) |
| `jacob_tornato` | giorno 19, il rincontro al locale | Joanie B4 |

## Flag lasciati dalle chat A e B (per le varianti delle scene fisse)

Oltre al flag automatico di fine discorso `chat_<id>`. **Gli ordini di Barbara** chiedono una variante nella scena del giorno dopo (Sara vestita così, qualcuno lo nota).

| Flag | Discorso | Cosa può ricordare la scena |
|---|---|---|
| `barbara_ordine_camicetta` | Barbara A3 | Sara arriva con la camicetta verde scollata |
| `barbara_ordine_rossetto` | Barbara A4 | rossetto bordeaux, quello di Barbara |
| `barbara_ordine_scollatura` | Barbara B3 | vestito nero scollato, niente cardigan; Barbara alla porta a controllare |
| `simon_stretching`, `simon_colazione`, `simon_obiettivo_pushup`, `simon_squat`, `simon_playlist`, `simon_insicurezza`, `simon_notata` | Simon | in palestra Simon chiede degli esercizi, della colazione, dei dieci piegamenti... |
| `howard_rubinetto`, `howard_lasagna`, `howard_pacco_tea`, `howard_caffe_domenica`, `howard_contatto_emergenza`, `howard_luce_corridoio` | Howard | visite, piatti lasciati alla porta, il caffè della domenica |
| `daniel_prima_pagina`, `daniel_jazz`, `daniel_lezione`, `daniel_domanda_desiderio` | Daniel | riferimenti in ufficio o alle feste |
| `magnus_capitolo_tre`, `magnus_promessa_pagine`, `magnus_libro_regalo`, `magnus_collezione_foto`, `magnus_prima_riga`, `magnus_cerchia_accenno`, `magnus_bacio_scritto` | Magnus | il libro regalato, la «prima riga», l'archivio di foto |
| `barbara_jessica_accenno`, `barbara_gala_invito`, `barbara_confidenza_invisibile` | Barbara | il gala, la confidenza |
| `jacob_jukebox`, `jacob_lago`, `jacob_le_manca_qualcosa` | Jacob | il jukebox al locale, il lago |
| `joanie_sceglie_vestito`, `joanie_serie_giardiniere`, `joanie_sa_della_noia` | Joanie | lo shopping, la serie, Joanie che sa |
| `darius_compleanno_josh`, `darius_cena_sabato`, `darius_padre` | Darius | il compleanno di Josh, la cena, il padre |
