# The Thin Line — Guida alle scene NSFW con LM Studio

Bozza di lavoro | 16 novembre 2026 · Regola di riferimento: [regole-di-lavoro.md](regole-di-lavoro.md), punto 7.

## Come funziona, in breve

1. **Claude scrive il brief** della scena in `docs/nsfw/brief/<id>.md`, partendo dal [modello](nsfw/brief/_modello.md): chi, dove, percorso e tappa, cosa succede, stato d'animo di Sara, tono, limiti, come si chiude.
2. **Tu lo rileggi** e lo correggi se serve: è il punto in cui decidi fin dove arriva la scena.
3. **Lanci lo script**, che manda il brief al modello caricato in LM Studio e scrive la scena già in formato Ren'Py in `game/nsfw/<id>.rpy`.
4. **Rileggi il risultato** e lo sistemi a mano. Se il modello sbaglia il formato, le righe sbagliate finiscono in `game/nsfw/<id>.scartate.txt`.
5. Nel gioco la scena si richiama con `call scena_nsfw("<id>")`. Finché il file non esiste, al suo posto compare un segnaposto. *(Questo aggancio è nel lotto "Da applicare" del [registro](decisioni.md).)*

## Prima volta: preparare LM Studio

Sul tuo PC è già tutto pronto. L'ho controllato il 16/11:
- LM Studio ha il server locale acceso su `http://localhost:1234`.
- È caricato **gemma-4-31b-it-heretic-i1**; c'è anche **huihui-qwen3-vl-32b-instruct-abliterated-i1**.

Una precisazione: questi due modelli non sono "addestrati apposta" per la narrativa erotica. Sono modelli generici a cui sono stati tolti i rifiuti (versioni *heretic* / *abliterated*). Funzionano, ma lo stile va guidato con brief precisi. Se in futuro vorrai un modello specializzato in narrativa, si cambia in LM Studio e lo script lo userà da solo.

Se un giorno il server non risponde:
1. Apri LM Studio.
2. Carica il modello (in alto, *Select a model to load*).
3. Vai nella scheda **Developer** e accendi **Status: Running**.

Ricorda: il modello occupa circa 20 GB su disco e molta memoria quando è caricato. Espellilo prima di lavorare con Unity o Premiere.

## Generare una scena

Dalla cartella del gioco (`C:\Users\Jody\the-thin-line`):

```bash
py tools/nsfw/genera_scena.py docs/nsfw/brief/<id>.md
```

Ci vuole circa un minuto per una scena breve, di più per quelle lunghe. Il modello prima "ragiona" e poi scrive: se lo script dice che ha finito i token, rilancialo aggiungendo `--max-token 7000`.

Altre opzioni utili:
- `--temperatura 1.0`: più creativo (il valore predefinito è 0.8). Più basso vuol dire più prevedibile.
- Rilancia lo stesso comando per avere un'altra versione. Attenzione: sovrascrive il file, quindi copia prima quella che ti piace.

## Cosa fa lo script

- Usa da solo il primo modello caricato in LM Studio.
- Manda al modello le regole fisse di [prompt_sistema.md](../tools/nsfw/prompt_sistema.md): il formato Ren'Py, i codici dei personaggi, `[nome_compagno]` al posto del nome, lo slow burn e tutti i personaggi adulti.
- Tiene solo le righe nel formato `codice "testo"` con un codice valido; le altre le mette da parte.
- Non pubblica e non committa niente: il testo resta da rileggere.

## Prova fatta

Il 16/11 ho fatto una prova tecnica con un brief casto: Sara e Josh sul divano. Ne sono uscite 12 righe valide, tutte nel formato giusto, in circa 50 secondi. Dopo la prova ho aggiunto una regola: la narrazione va scritta in terza persona, perché il modello la scriveva in prima.
