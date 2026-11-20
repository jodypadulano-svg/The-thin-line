# Howard — giorno 9, abbraccio prolungato e Complesso della Crocerossina
Decisione concordata il 20 novembre 2026 · Inserita nel gioco in `game/episodio1/ep1_giorno09.rpy`.

## Intenzione narrativa

Howard ha appena simulato un pianto per suscitare compassione. Sara, se il giocatore sceglie di abbracciarlo, si avvicina alla poltrona e lo stringe con tenerezza, come si consola un bambino. Non prova desiderio né giudica Howard negativamente; lo considera un anziano vulnerabile, innocuo e solo. Howard, invece, sfrutta il contatto: **non sarà mai lui a sciogliere spontaneamente l'abbraccio**. Sara deve scegliere di staccarsi.

L'esperienza è mostrata su due piani separati:
- **Sara** sente solo la sofferenza che immagina in Howard. Quando avverte che le mani di lui stanno scendendo verso il suo sedere, fugacemente si domanda se stia succedendo davvero, poi si rimprovera per un pensiero che considera ingeneroso («No, dai, pover'uomo, è solo commosso»). Non coglie ancora le intenzioni sessuali di Howard. Mantiene la sua delicatezza e la sua fiducia.
- **Il giocatore** conosce già il pianto finto tramite il retroscena. Vede le mani scendere progressivamente e, **soltanto dopo la terza conferma**, una CG in primo piano sul volto di Howard: un sorriso soddisfatto, avido, inquietante, che Sara, con il viso contro il petto di lui, non può vedere. Sguardo e sorriso devono essere leggibili ma non una caricatura.

## Loop delle tre decisioni

Il primo menu mantiene «Kind words, from her chair» / «Hug him». Chi sceglie le parole gentili non entra nel loop e non può attivare il tratto. Scegliere l'abbraccio lascia già Howard +1 e il flag `ep1_d9_abbraccio` (come prima).

Durante l'abbraccio, per **massimo tre volte**, il gioco offre:
- **Staccarsi:** interrompe il loop e non attiva il tratto; Howard lascia andare soltanto quando Sara si separa.
- **Restare ancora:** Howard **Interest +1** ogni volta; il contatore `howard_abbraccio_prolungamenti` aumenta di 1. Le mani si avvicinano progressivamente al sedere di Sara.

**Escalation dell'avvertimento (prima della scelta di volta in volta):**
1. **Primo invito a continuare:** lieve allerta narrativa; Howard non si stacca, forse è opportuno che Sara lo faccia.
2. **Secondo:** segnali fisici più evidenti, con le mani che scendono sulla schiena; Sara non ne coglie la portata e il giocatore può ancora fermarsi.
3. **Terzo:** avvertimento esplicito **prima di confermare**: «Questa scelta avrà conseguenze permanenti». Spiega chiaramente che si attiverà il **Complesso della Crocerossina** e che le scelte di **rifiutare proposte di Howard** saranno disabilitate e mostrate in grigio fino alla fine della partita. Il messaggio avvisa che il giocatore sta procedendo **a proprio rischio e pericolo**.

Dopo la **terza conferma di permanenza** (non prima):
- `complesso_crocerossina = True`;
- flag `ep1_d9_crocerossina_attivata`;
- notifica narrativa «Trait activated: Savior Complex — Howard»;
- **primo piano di Howard**, soddisfatto e inquietante, mentre Sara non può vederlo;
- Sara, a fine scena, si stacca lei. Nessuna trasformazione improvvisa della sua consapevolezza.

## Regola globale del tratto: rifiuti in grigio

La booleana globale `complesso_crocerossina` (default `False`, tramite `default` in `game/core/stato.rpy`) è **persistente nel salvataggio della partita** da quando diventa `True`. Non riguarda tutti gli uomini: **solo Howard**.

Ogni futura **proposta di Howard** deve avere le risposte di rifiuto contrassegnate con il marcatore `(rifiuto_howard=True)` nel `menu` di Ren'Py. Quando il tratto è attivo, `screen choice(items)` lascia la risposta visibile, ma **grigia e non cliccabile**, con l'etichetta di blocco. L'alternativa non si elimina e non si nasconde. Anche i menu automatici di debug devono ignorare le opzioni bloccate.

Esempio di sintassi:

```renpy
menu:
    "Accept Howard's suggestion.":
        pass
    "Refuse Howard's suggestion." (rifiuto_howard=True):
        pass
```

L'applicazione **già realizzata** comprende la proposta di rivedersi la sera stessa del giorno 9: il «non ho molto tempo» è già marcato. Per i dialoghi con Howard scritti in futuro, **marcare ogni nuovo rifiuto**. I menu non marcati non sono riconosciuti automaticamente come rifiuti.

La perdita di opzioni è un **effetto intenzionale, consapevolmente scelto dal giocatore e segnalato prima del punto di non ritorno**. È una convenzione narrativa di gameplay, non una diagnosi psicologica e non un'indicazione che la gentilezza di Sara equivalga a consenso verso ulteriori gesti. L'interesse di Howard e la disponibilità di Sara restano cose diverse.

## Risorse visive

Si aggiungono tre CG condizionali nella lista di `docs/prompt-immagini/inquadrature-giorno-09.md`:
- `d9_10_abbraccio.webp`: inizio abbraccio;
- `d9_11_mani.webp`: secondo prolungamento, mani più in basso;
- `d9_12_howard_sorriso.webp`: **solo** dopo tre prolungamenti, primo piano espressione di Howard.

## Stato

**Realizzato nel codice**: stato, contatore, loop decisionale, avvertimenti, primo piano richiesto (CG referenziata con fallback fino alla creazione del file), booleana e comportamento grigio del primo rifiuto e dei futuri rifiuti marcati. **Da completare**: produrre le tre immagini e applicare il marcatore di rifiuto ai menu di Howard non ancora scritti. Il testo inglese della scena resta una bozza narrativa da rileggere.
