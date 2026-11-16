# The Thin Line — Simulazione del primo mese

Generato da `tools/piani/simulatore.py` sui dati di `tools/piani/mese1.py`. **Versione minima:** solo il primo mese, giocatori finti e partite casuali.

## 1. Giocatori finti

| Giocatore | Corr | Conf | Susp | Josh | Simon | Jacob | Darius | Daniel | Joanie | Magnus | Howard | Barbara | Segreti | Tappe raggiunte |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fedele (prudente al massimo) | 0 | 25 | 0 | 100 | 2 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 0 | nessuna oltre la 3 |
| Spinge tutto (Corruption al massimo) | 27 | 39 | 7 | 70 | 22 | 12 | 1 | 9 | 9 | 9 | 19 | 6 | 3 | Simon 4 |
| Punta su Simon | 27 | 53 | 7 | 91 | 22 | 12 | 0 | 8 | 6 | 8 | 14 | 3 | 3 | Simon 4 |
| Punta su Jacob | 27 | 54 | 7 | 91 | 19 | 12 | 0 | 8 | 6 | 8 | 14 | 3 | 3 | nessuna oltre la 3 |
| Punta su Darius | 27 | 54 | 7 | 90 | 19 | 12 | 1 | 8 | 6 | 8 | 14 | 3 | 3 | nessuna oltre la 3 |
| Punta su Daniel | 27 | 54 | 7 | 91 | 18 | 12 | 0 | 10 | 6 | 8 | 14 | 3 | 3 | nessuna oltre la 3 |
| Punta su Joanie | 27 | 53 | 7 | 87 | 19 | 12 | 0 | 8 | 10 | 8 | 14 | 3 | 3 | nessuna oltre la 3 |
| Punta su Magnus | 27 | 53 | 7 | 91 | 19 | 12 | 0 | 8 | 6 | 9 | 14 | 3 | 3 | nessuna oltre la 3 |
| Punta su Howard | 27 | 54 | 7 | 91 | 19 | 12 | 0 | 8 | 6 | 8 | 19 | 3 | 3 | nessuna oltre la 3 |
| Punta su Barbara | 27 | 53 | 7 | 91 | 19 | 12 | 0 | 8 | 6 | 8 | 14 | 6 | 3 | nessuna oltre la 3 |

## 2. 5000 partite casuali

| Variabile | Minimo | Mediana | 90° percentile | Massimo |
|---|---|---|---|---|
| Corr | 1 | 9 | 13 | 23 |
| Conf | 24 | 36 | 42 | 50 |
| Susp | 0 | 1 | 5 | 11 |
| Josh | 72 | 93 | 100 | 100 |
| Simon | 2 | 10 | 14 | 21 |
| Jacob | 0 | 5 | 8 | 12 |
| Darius | 0 | 0 | 1 | 1 |
| Daniel | 0 | 4 | 7 | 10 |
| Joanie | 0 | 5 | 7 | 10 |
| Magnus | 2 | 5 | 8 | 9 |
| Howard | 3 | 9 | 14 | 19 |
| Barbara | 0 | 2 | 4 | 6 |
| Segreti | 0 | 1 | 2 | 3 |

| Controllo | Partite casuali |
|---|---|
| Simon: tappa 4 (Interest 20) / bacio (6a) | 0% / 0% |
| Jacob: tappa 4 (Interest 20) / bacio (6a) | 0% / 0% |
| Darius: tappa 4 (Interest 20) / bacio (6a) | 0% / 0% |
| Daniel: tappa 4 (Interest 20) / bacio (6a) | 0% / 0% |
| Joanie: tappa 4 (Interest 20) / bacio (6a) | 0% / 0% |
| Magnus: tappa 4 (Interest 20) / bacio (6a) | 0% / 0% |
| Howard: tappa 4 (Interest 20) / bacio (6a) | 0% / 0% |
| Barbara: tappa 4 (Interest 20) / bacio (6a) | 0% / 0% |
| Corruption ≥ 15 (soglia di Simon) | 5% |
| Corruption ≥ 25 (soglia di Jacob e della scintilla di Darius) | 0% |
| Ancora compatibile col finale fedele | 20.0% |


## 3. Cosa ci dice (commento del 16/11/2026)

**Funziona come previsto:**
- **Slow burn rispettato:** nessun giocatore, nemmeno quello che spinge tutto, arriva a un bacio nel primo mese.
- **Simon** arriva alla tappa 4 (Interest 20) solo se il giocatore lo cerca davvero, come prevede la mappa («fine mese 1»). Le partite casuali non ci arrivano mai.
- **Darius** resta fermo (Interest massimo 1): il suo percorso è opt-in e non si apre per caso.
- **Barbara** resta lentissima (Interest massimo 6).
- **Corruption:** la mediana casuale è 9; solo il 4% delle partite casuali supera la soglia di Simon (15). Chi spinge con decisione arriva a 27, cioè oltre la soglia di Jacob e della scintilla di Darius (25) proprio a fine mese, come previsto.

**Da correggere o decidere:**
1. ~~**Howard va troppo veloce.**~~ ✅ **Corretto (16/11):** chi lo cercava arrivava a Interest 25 (tappa 4) già nel primo mese. Abbassati cinque aumenti (i due abbracci, «Certo, un caffè» da +5 a +3, la visita del giorno 18, la cucina del giorno 26): ora il massimo del mese è 19, sotto la tappa 4.
2. **Il finale fedele è troppo facile, per ora.** Un giocatore che vuole restare fedele chiude il mese con Corruption 0 e Josh 100 senza fatica, perché ogni tentazione ha un'opzione «sicura» sempre disponibile. La difficoltà deve arrivare nei mesi successivi: tentazioni in cui l'opzione sicura costa qualcosa (Interest verso Josh che scende, Confidence che cala, occasioni di carriera perse).
3. **I «Punta su…» si somigliano.** Nel primo mese le scene sono poche per ogni personaggio, quindi puntare su Jacob, Daniel o Magnus cambia poco l'Interest. È normale per il primo mese, ma va tenuto d'occhio negli episodi successivi.

**Limiti della versione minima:** copre solo il primo mese; i giocatori finti hanno strategie semplici; alcune condizioni sono approssimate (per esempio la scena 🔒 del giorno 25 è valutata solo con la Corruption).
