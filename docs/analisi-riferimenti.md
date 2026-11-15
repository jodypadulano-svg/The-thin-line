# Analisi dei giochi di riferimento — meccaniche NTR

Bozza di lavoro | 15 novembre 2026

Analisi delle **meccaniche** (non dei testi) di tre visual novel Ren'Py usate come ispirazione per The Thin Line. Gli script estratti sono in `C:\Users\Jody\renpy-ispirazione` e **non** fanno parte di questo repository.

## 1. Quadro d'insieme

| | A Perfect Marriage 0.7.6 | My Husband's Boss (cap. 1-3) | Whispers of Desire 0.8 |
|---|---|---|---|
| Struttura | Parti/atti, file per punto di vista | Giorni e scene (`dXXsYY`) | Atti con scene, varianti "alone" |
| Punto di vista | Alternato: marito (scelte), moglie, altri | Lineare, soprattutto moglie | Selezionabile, coppia (lui e lei) |
| Scelte | ~167 menu | **Nessuna** (kinetic novel) | ~381 menu |
| Statistiche | Contatori + **moltissimi flag booleani** | Nessuna | Classi di statistiche per personaggio + 4 contatori di percorso |
| Gating | Flag di rifiuto per ogni corteggiatore | — | Scelte condizionate (`"..." if ...`) |
| Extra | Questionario iniziale di personalità, scorciatoie ai capitoli, telefono, galleria | Nomi personalizzabili, regia cinematografica | Calendario, mappa città/casa, telefono, obiettivi, achievement, guida, replay gallery |

## 2. A Perfect Marriage

- **Questionario iniziale**: una serie di domande (label `q30`…`q54`) fissa la personalità di partenza dei due coniugi (sicuro/insicuro, fedele/traditore, puro/malizioso, sottomessa…). È un modo elegante per far "scegliere chi sei" senza schermate di statistiche.
- **Statistiche miste**: pochi contatori numerici (malizia, sottomissione, fiducia della moglie; comunicazione, fiducia in sé, purezza del marito) e **centinaia di flag booleani** che ricordano singole scelte.
- **Un contatore per ogni uomo** (`anna_<nome>`) e un **flag di rifiuto** per ogni uomo (`annareject<nome>`): un percorso si può chiudere definitivamente. È la base del "segui un percorso, ignorane altri".
- **Il marito conta**: le sue scelte (comunicare, fidarsi, reagire) cambiano come lei vive le tentazioni. Il NTR nasce dalla coppia, non solo dall'antagonista.
- **Scorciatoie**: all'avvio si può saltare alla Parte 2/3/7 o all'ultimo aggiornamento, con flag preimpostati. Fondamentale per un gioco a episodi su Patreon.
- Telefono con messaggi (label `message`, `reply_message`).

## 3. My Husband's Boss

- **Kinetic novel**: nessuna scelta, solo regia. La forza è il **ritmo cinematografico**: sequenze di immagini con dissolvenze, pause, effetti sonori, testo minimo.
- **Struttura per giorni** con scene brevi e titolate (es. "clienti persi", "cena", "telefonata notturna del capo"): ogni scena ha un solo scopo narrativo.
- **Leva economica**: il capo ha potere sul lavoro del marito; la tensione nasce da carriera, status e debiti. Stesso archetipo di Daniel.
- **Nomi personalizzabili** di marito, moglie e capo all'avvio.
- Limite: senza scelte il giocatore non ha agenzia; la rigiocabilità è nulla.

## 4. Whispers of Desire

- **Statistiche per personaggio** (oggetti `*_stats`): per lei lussuria, corruzione, esibizionismo, personalità, tradimento; per lui relazione, voyeurismo, condivisione, corruzione; per ogni comprimario una relazione.
- **Quattro percorsi dichiarati** (lealtà, coppia aperta, tradimento, seduzione), ognuno con sotto-finali, tracciati da contatori (`love_route`, `sharing_route`, `betrayal_route`, `seduction_route`). Molte scene sono condivise tra percorsi.
- **Segreti**: molte scelte sono del tipo "lo nasconde / lo racconta" (`hides_*`). Il segreto diventa una condizione per scene future.
- **Varianti "_alone"**: la stessa situazione esiste in versione con il partner presente e senza. Raddoppia il valore delle scelte senza raddoppiare la trama.
- **Scelte condizionate** visibili solo se si è fatto qualcosa prima.
- **Guida in gioco** che spiega percorsi e statistiche: abbassa la frustrazione di chi cerca un percorso preciso.
- Calendario con fasi del giorno, mappe esplorabili, telefono, obiettivi, achievement, replay gallery.

## 5. Cosa funziona (da prendere)

1. **Un indicatore per ogni uomo + possibilità di chiudere il percorso** (APM): libertà vera di seguire uno, più o nessun percorso.
2. **Segreti come risorsa narrativa** (WoD): ciò che Sara nasconde al compagno pesa sulle scene successive.
3. **Ritmo cinematografico** (MHB): scene brevi, una sola funzione, chiusura forte.
4. **Scorciatoie ai capitoli e guida** (APM, WoD): chi aggiorna a ogni release non deve rigiocare tutto.
5. **Nome del compagno personalizzabile** (MHB, WoD): aumenta l'immedesimazione del pubblico NTR.

## 6. Cosa non funziona (da evitare)

1. **Flag a centinaia senza struttura** (APM): difficili da mantenere e da bilanciare tra episodi.
2. **Statistiche opache** (APM): il giocatore non capisce perché una scena non si apre.
3. **Corruzione come numero unico che sale e basta** (WoD): rende la protagonista "attratta da chiunque"; la bibbia di The Thin Line lo esclude esplicitamente.
4. **Nessuna agenzia** (MHB).
5. **Grind da sandbox** (mappe e fasi del giorno da cliccare): allunga senza aggiungere storia.

## 7. Dove The Thin Line può essere migliore

1. **Ironia drammatica come meccanica**: i "retroscena" mostrano al giocatore ciò che Sara non sa (il piano di Daniel, il furto di Howard). Il Diario separa *ciò che sa Sara* da *ciò che sai tu*. Nessuno dei tre giochi lo fa in modo sistematico.
2. **Confini per persona, non corruzione globale**: ogni percorso ha affinità e tappe proprie; il cambiamento di Sara è sempre legato a *chi* e *perché*.
3. **Trasparenza opzionale**: un'opzione mostra l'effetto delle scelte (per chi cerca un percorso) o lo nasconde (per chi vuole immersione).
4. **Slow burn strutturato**: ogni percorso avanza per tappe con condizioni chiare; un episodio non brucia più di una tappa per percorso.
5. **Pensieri di Sara** sempre leggibili: il pubblico vede la tentazione nascere dall'interno, non solo dall'esterno.
6. **Pronto per gli aggiornamenti**: salvataggi compatibili tra versioni, scorciatoia all'ultimo episodio, gioco giocabile da subito senza grafica.
