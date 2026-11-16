# The Thin Line — Registro delle decisioni

Ogni decisione presa con Jody, in poche righe. Regole d'uso in [regole-di-lavoro.md](regole-di-lavoro.md), punto 1.

## Da applicare
Decisioni prese ma non ancora riportate nel codice. Si applicano tutte insieme quando Jody dà il via.

- **A4 — Dialoghi troppo corti** (Jody): le scene dell'Episodio 1 sono bozze-scheletro (circa 2.100 parole in tutto); vanno riscritte per intero, con una lunghezza adatta a un episodio di circa un'ora.

## Provvisorie
Scelte fatte da Claude per rendere il gioco giocabile, non ancora confermate da Jody.

- **P1 — Bivi aggiunti nell'Episodio 1**, dove le schede non ne prevedevano: prologo (serata o scrittura), Simon 1 (risposta a Joanie), Simon 2 (guardare o no), Simon 5 (spalla), Daniel 1 (reazione a tavola, discorso in auto), Howard 1 (fermarsi o no), Daniel 3 (entusiasmo o timidezza), finale (dire o nascondere l'editore). Effetti numerici da tarare quando ci saranno le tappe successive.
- **P2 — Opzioni della domanda finale di Howard 3**: «Certo, un caffè» (+5), «Quando capita» (+2), «Ho poco tempo» (0).
- **P3 — Dettagli inventati per far funzionare le scene**: portachiavi a forma di penna stilografica; il turno lungo di Josh il giorno 7; Daniel che «ascolta» Josh parlare della scrittura di Sara.
- **P4 — Aspetto degli attori non descritto nella bibbia** ([prompt](prompt-immagini/attori.md)): età di Sara (fine vent'anni); Josh intero (circa trent'anni, biondo scuro, comune, non atletico); Joanie intera (bionda miele, coda alta, occhi verdi, atletica); dettagli del viso di Simon, Daniel, Howard; editore (fine cinquanta, barba sale e pepe, occhiali di tartaruga).
- **P5 — Valori scelti applicando il lotto A1-A10**: Confidence iniziale 20; soglia «gesti carini verso Josh» a Interest 30; quattro abiti iniziali sobri; Corruption +1 per guardare Joanie con Simon e +2 per tenere il segreto dell'editore; Confidence +2 scrivere, +3 entrare in palestra da sola; Suspicion +3 per ogni segreto; due frasi 🔒 di prova (Simon 5 con Corruption 15, editore con Confidence 25).

## Applicate

| Data | Decisione | Dove |
|---|---|---|
| 16/11/2026 | Il compagno si chiama **Josh** di default; il giocatore può cambiarlo | `script.rpy`, `stato.rpy` |
| 16/11/2026 | Chiara diventa **Joanie** dappertutto | codice e documenti |
| 16/11/2026 | Joanie è il **percorso 5**; il lato sentimentale emerge molto più avanti | [joanie.md](personaggi/joanie.md) |
| 16/11/2026 | Ordine delle 8 giornate dell'Episodio 1 approvato come **provvisorio**; nuovi intrecci quando ci saranno più percorsi | [sistema-di-gioco.md](sistema-di-gioco.md) |
| 16/11/2026 | Howard chiude fuori Sara **rubandole le chiavi** il giorno della spesa, insieme alla biancheria | `howard.rpy`, [howard.md](personaggi/howard.md) |
| 16/11/2026 | Il rifiuto di Sara a Howard **non chiude** il percorso | `howard.rpy` (già così) |
| 16/11/2026 | Regole di lavoro fissate (decisioni a lotti, grafo, incastri, prompt, attori/luoghi, personaggi funzionali, NSFW con LM Studio) | [regole-di-lavoro.md](regole-di-lavoro.md) |
| 16/11/2026 | Il grafo del gioco è un **diagramma Mermaid** nel repo | [grafo.md](grafo.md) |
| 16/11/2026 | Immagini con **Mage**, stile **render 3D** come i giochi di riferimento; **le genera Jody**, Claude scrive solo i prompt | regole, punto 4 |
| 16/11/2026 | I **personaggi funzionali** li propone Claude (es. collega di Josh, receptionist della palestra, fidanzato di Joanie) | regole, punto 6 |
| 16/11/2026 | **A1** Aggancio scene NSFW `call scena_nsfw("id")` con segnaposto | `core/nsfw.rpy` |
| 16/11/2026 | **A2** Variazioni sempre a schermo con numero e colore | `core/notifiche.rpy` |
| 16/11/2026 | **A3** Frasi con requisito visibili in grigio con «Richiede …» | `screens.rpy` (choice), `core/stato.rpy` |
| 16/11/2026 | **A5** Corruption (sostituisce la curiosità) | `core/stato.rpy`, scene |
| 16/11/2026 | **A6** 9 Interest, Josh compreso; gesti carini bloccati sotto soglia | `core/stato.rpy`, scene |
| 16/11/2026 | **A7** Soglie di Corruption per percorso | `core/stato.rpy`, Diario |
| 16/11/2026 | **A8** Suspicion | `core/stato.rpy`, Diario |
| 16/11/2026 | **A9** Confidence | `core/stato.rpy`, scene, Diario |
| 16/11/2026 | **A10** Abiti scelti dalla storia, sbloccati da Confidence e Corruption | `core/abiti.rpy`, Diario |
