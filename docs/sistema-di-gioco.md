# The Thin Line — Sistema di gioco

Bozza di lavoro | 16 novembre 2026

Come funziona la base del gioco in Ren'Py (cartella `game/`). Le ragioni delle scelte sono in [analisi-riferimenti.md](analisi-riferimenti.md).

## 1. Principi

- **Storia prima di tutto, niente grind**: una trama lineare a giornate, con scene opzionali e bivi. Niente mappe da cliccare.
- **Ogni percorso è a sé**: Interest e soglie di Corruption per persona; Sara non diventa attratta da chiunque.
- **Ironia drammatica**: i retroscena mostrano al giocatore ciò che Sara non sa.
- **Effetti visibili**: ogni variazione compare a schermo con il numero (A2); dalle Opzioni si può nascondere.
- **Giocabile senza grafica**: colori al posto degli sfondi, didascalie `[CG]` al posto delle immagini.

### Nuova architettura approvata il 18/11/2026 (ancora da implementare)

Alla trama a giornate si aggiungono **rubrica con numeri sbloccabili, uno slot telefonico elettivo al giorno, conversazioni a step individuali indipendenti dal calendario, incontri che reagiscono alla familiarità acquisita e possibili appuntamenti nelle serate libere**. Le scene fisse successive devono reagire anche ai messaggi e agli appuntamenti precedenti. Lo scopo non è imporre nuove relazioni, ma rendere gli otto percorsi facoltativi e dinamici.

**Fonte tecnica/narrativa dettagliata e vincolante:** [Telefono e percorsi dinamici](telefono-e-percorsi-dinamici.md). Le parti del presente documento che descrivono la *base giocabile attuale*, comprese la scaletta provvisoria di 8 giornate e i nomi delle funzioni già presenti, **non documentano ancora l'implementazione** del nuovo sistema. I nuovi nomi delle variabili verranno fissati al momento del codice, preservando i salvataggi.

## 2. Variabili

| Cosa | Nome nel codice | Valori | Significato |
|---|---|---|---|
| **Corruption** | `sara_corruption` | 0-100, parte da 0 | Sale con ogni scelta «sbagliata» a favore di un percorso; apre le scene oltre la soglia del percorso |
| **Interest toward XXX** | `percorsi[x].interest`, `interest_josh` | 0-100; Josh parte da 80 | 9 valori (8 percorsi + Josh); possono scendere. Sotto 30 verso Josh, Sara non riesce più a fare gesti carini (valore provvisorio) |
| **Suspicion** | `josh_suspicion` | 0-100, parte da 0 | Il sospetto di Josh: bugie, segreti, rischi con lui vicino |
| **Confidence** | `sara_confidence` | 0-100, parte da 20 | Fiducia in sé: sblocca frasi coraggiose e abiti |
| Tappa | `percorsi[x].tappa` | 0, 1, 2… | Contatore interno dello slow burn; mai indietro |
| Chiuso | `percorsi[x].chiuso` | sì/no | Sara ha chiuso la porta: niente più scene |
| Segreti | `segreti` | elenco | Cose che Sara nasconde a Josh; ogni nuovo segreto alza la Suspicion di 3 |
| Fatti | `fatti` | chiave → valore | Scelte puntuali da ricordare (es. `ep1_palestra_da_sola`) |

**Soglie di Corruption** per le scene «spinte» (A7): Simon 15 · ex 25 · amico di Josh 35 · Daniel 45 · Joanie 55 · editore 65 · Howard 75 · capa 85.

**Abiti** (A10): per ogni occasione (casa, palestra, ufficio, sera) Sara indossa da sola l'abito più avanzato che ha sbloccato. Quelli sicuri di sé chiedono Confidence, quelli provocanti anche Corruption. Per ora esistono solo i quattro abiti iniziali, sobri; gli altri si aggiungono scrivendo le scene.

## 3. Funzioni da usare negli script

```renpy
$ interest("simon", 5, "Simon se ne ricorderà.")   # anche "josh"; valori negativi ok
$ corruption(2, "Un gioco innocente. Quasi.")
$ confidence(3, "Sara entra da sola.")
$ suspicion(4, "Josh nota il messaggio.")
if oltre_soglia("simon"):                  # Corruption >= soglia di Simon
    ...
if gentile_con_josh():                     # Interest verso Josh >= 30
    ...
$ vestito = abito("palestra")              # abito da usare nella scena
call scena_nsfw("simon_doccia")            # scena generata con LM Studio o segnaposto
$ incontra("simon")                        # primo incontro: pagina nel Diario
$ tappa("simon", 2)
$ chiudi("howard")
$ segreto("ep1_editore", "Il biglietto dell'editore.")   # alza anche la Suspicion
$ nota_sara("daniel", "Uno spaccone arrogante.")   # Diario: Cosa sa Sara
$ retroscena("howard", "Ha rubato un capo...")      # Diario: Cosa sai tu
$ segna("ep1_palestra_da_sola")
if fatto("ep1_palestra_da_sola"):
    ...
$ vai("palestra", "Palestra — sera")       # sfondo + cartello del luogo
$ cg("descrizione dell'immagine da produrre")
$ via_cg()
call nuovo_giorno(3, "La cena aziendale")
call inizio_retroscena
rs "Testo che Sara non sa."
call fine_retroscena
```

**Frasi con requisito** (A3): si scrivono così nel menu, e se il requisito manca restano visibili in grigio con «Richiede …» sotto.

```renpy
menu:
    "«Mi sistemi anche l'altra?», con un sorriso." (corruption=15):
        ...
    "«Le mando le pagine domani stesso.»" (confidence=25):
        ...
    "Raccontargli tutto." (josh=30):          # Interest verso Josh
        ...
    "Frase per chi è vicino a Simon" (simon=20, corruption=10):
        ...
```

Personaggi: `s` Sara, `sp` pensieri di Sara, `c` il compagno (nome scelto dal giocatore, predefinito «Josh»), `ch` Joanie, `si` Simon, `da` Daniel, `ho` Howard, `ed` l'editore, `n` narratore, `rs` voce dei retroscena.

## 4. Diario

Dal menu rapido (**Diario**): una pagina per Sara (Interest verso Josh, Corruption, Confidence, Suspicion, segreti, guardaroba) e una per ogni personaggio incontrato, con la tappa raccontata a parole, l'Interest, la soglia di Corruption, "Cosa sa Sara" e "Cosa sai tu". Con "Mostra numeri" spento restano solo le descrizioni a parole.

## 5. Struttura dei file

```
game/
  script.rpy              avviso 18+, nome del compagno, istruzioni
  core/stato.rpy          variabili, soglie e funzioni
  core/notifiche.rpy      notifiche a schermo delle variazioni
  core/abiti.rpy          guardaroba di Sara
  core/nsfw.rpy           aggancio delle scene generate con LM Studio
  core/personaggi.rpy     personaggi
  core/presentazione.rpy  sfondi provvisori, cartelli, retroscena, segnaposto CG
  core/diario.rpy         schermata Diario
  episodio1/ep1_flusso.rpy  ordine delle giornate
  episodio1/ep1_casa.rpy    prologo, invito, finale
  episodio1/simon.rpy | daniel.rpy | howard.rpy   scene per personaggio
  test/test_episodio1.rpy   test automatici
```

## 6. Scaletta dell'Episodio 1 (provvisoria, approvata)

| Giorno | Scene | Bivi |
|---|---|---|
| 1 | Prologo a casa; Joanie la iscrive in palestra | Serata con lui o scrivere |
| 2 | Simon 1 e 2 (prima visita); invito alla cena aziendale | Come risponde a Joanie; guardare o no |
| 3 | Daniel 1 (cena aziendale) + retroscena | Come reagire a Daniel; cosa dire in macchina |
| 4 | Howard 1 (pianerottolo); Daniel 2 (patente) | Fermarsi o no con Howard |
| 5 | Howard 2 (spesa) + retroscena furto; Simon 3 (locale) | — |
| 6 | Simon 4 (Joanie cancella); Simon 5 solo se entra | **Entrare o tornare a casa** |
| 7 | Howard 3 (chiusa fuori) + retroscena e pianto finto | **Risposta a Howard (provvisoria)** |
| 8 | Daniel 3 (festa, editore) + retroscena; finale a casa | Come parlare all'editore; **dirlo al compagno o tenerlo segreto** |

I dialoghi sono **bozze** per rendere il gioco giocabile; si riscrivono partendo dalle schede.

## 7. Scelte provvisorie da confermare

Sono cose che la bibbia lascia aperte e che il codice ha dovuto riempire per funzionare:

1. ~~Nome predefinito del compagno~~ — deciso: «Josh» (il giocatore può cambiarlo).
2. ~~Archetipo 5~~ — deciso: è Joanie; il lato sentimentale emerge molto più avanti ([scheda](personaggi/joanie.md)).
3. ~~Ordine delle giornate~~ — approvato come provvisorio (16/11): con solo tre percorsi attivi; quando ce ne saranno di più si creeranno nuovi intrecci.
4. ~~Meccanismo di Howard 3~~ — deciso: Howard ruba le chiavi di Sara il giorno della spesa, insieme alla biancheria ([scheda](personaggi/howard.md)). Restano aperte opzioni ed effetti della domanda finale.
5. Il segreto finale (biglietto dell'editore) e le opzioni dei bivi non previsti dalle schede.

## 8. Compatibilità dei salvataggi tra episodi

- Nuove variabili sempre con `default`.
- Nuovi attributi di `Percorso` come attributi di classe.
- Non rinominare mai chiavi già usate (`fatti`, `percorsi`, `segreti`) né label già pubblicate.

## 9. Test

Dalla cartella dell'SDK (`C:\Users\Jody\RenPy\renpy-8.5.3-sdk`):

```
renpy.exe C:\Users\Jody\the-thin-line lint
renpy.exe C:\Users\Jody\the-thin-line test episodio1
renpy.exe C:\Users\Jody\the-thin-line test foto --enable-all --overwrite-screenshots
```

Il test `episodio1` gioca tutto l'episodio tre volte (sempre la prima scelta, sempre l'ultima, alternate) e apre ogni pagina del Diario. `foto` salva due schermate del Diario in `tests/screenshots/` (cartella esclusa da git).
