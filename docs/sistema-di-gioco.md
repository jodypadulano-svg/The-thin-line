# The Thin Line — Sistema di gioco

Bozza di lavoro | 16 novembre 2026

Come funziona la base del gioco in Ren'Py (cartella `game/`). Le ragioni delle scelte sono in [analisi-riferimenti.md](analisi-riferimenti.md).

## 1. Principi

- **Storia prima di tutto, niente grind**: una trama lineare a giornate, con scene opzionali e bivi. Niente mappe da cliccare.
- **Ogni percorso è a sé**: affinità e tappe per persona; Sara non diventa "corrotta" in generale.
- **Ironia drammatica**: i retroscena mostrano al giocatore ciò che Sara non sa.
- **Trasparenza a scelta**: le Opzioni permettono di mostrare o nascondere gli effetti delle scelte e i numeri.
- **Giocabile senza grafica**: colori al posto degli sfondi, didascalie `[CG]` al posto delle immagini.

## 2. Statistiche

| Cosa | Dove | Valori | Significato |
|---|---|---|---|
| `sara_legame` | Sara | 0-100, parte da 80 | Legame con il compagno |
| `sara_curiosita` | Sara | 0-100, parte da 0 | Quanto Sara guarda oltre i propri confini |
| `affinita` | ogni percorso | 0-100 | Quanto è cresciuto il rapporto (non è attrazione) |
| `tappa` | ogni percorso | 0, 1, 2… | A che punto è lo slow burn; mai indietro |
| `chiuso` | ogni percorso | sì/no | Sara ha chiuso la porta: niente più scene |
| `segreti` | Sara | elenco | Cose che Sara nasconde al compagno |
| `fatti` | gioco | chiave → valore | Scelte puntuali da ricordare (es. `ep1_palestra_da_sola`) |

Gli otto percorsi esistono già tutti nel codice (anche i quattro senza scheda), così i salvataggi restano compatibili quando arriveranno.

## 3. Funzioni da usare negli script

```renpy
$ incontra("simon")                      # primo incontro: pagina nel Diario
$ affinita("simon", 5, "Simon se ne ricorderà.")
$ tappa("simon", 2)                      # avanza lo slow burn
$ chiudi("howard")                       # Sara chiude il percorso
$ legame(3, "Sara sceglie lui, stasera.")
$ curiosita(2)
$ segreto("ep1_editore", "Il biglietto dell'editore.")
$ nota_sara("daniel", "Uno spaccone arrogante.")   # Diario: Cosa sa Sara
$ retroscena("howard", "Ha rubato un capo...")      # Diario: Cosa sai tu
$ segna("ep1_palestra_da_sola")
if fatto("ep1_palestra_da_sola"):
    ...
$ vai("palestra", "Palestra — sera")     # sfondo + cartello del luogo
$ cg("descrizione dell'immagine da produrre")
$ via_cg()
call nuovo_giorno(3, "La cena aziendale")
call inizio_retroscena
rs "Testo che Sara non sa."
call fine_retroscena
```

Personaggi: `s` Sara, `sp` pensieri di Sara, `c` il compagno (nome scelto dal giocatore, predefinito «Josh»), `ch` Joanie, `si` Simon, `da` Daniel, `ho` Howard, `ed` l'editore, `n` narratore, `rs` voce dei retroscena.

## 4. Diario

Dal menu rapido (**Diario**): una pagina per Sara (legame, curiosità, segreti) e una per ogni personaggio incontrato, con la tappa raccontata a parole, "Cosa sa Sara" e "Cosa sai tu". Con "Mostra numeri" attivo compaiono anche affinità e tappa.

## 5. Struttura dei file

```
game/
  script.rpy              avviso 18+, nome del compagno, istruzioni
  core/stato.rpy          statistiche e funzioni
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
