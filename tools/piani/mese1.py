# Genera docs/mese-1.md dai dati delle scelte e calcola i valori a fine mese.
# Uso: py tools/piani/mese1.py docs/mese-1.md   (modifica i dati qui, non il .md)
import sys, collections
OUT = sys.argv[1]

# Ogni giorno: (titolo, [fasce]); fascia: (nome, scena, chi, [scelte]);
# scelta: (fondamentale, domanda, [(opzione, {effetti})])
S = lambda f, q, *opts: (f, q, list(opts))
D = []

D.append(("1 Lun", [
 ("Prima del lavoro", "Davanti all'armadio", "", [
   S(0, "Cosa mettere in redazione?", ("Camicetta abbottonata fino in cima", {}), ("Un bottone aperto: oggi si sente carina", {"Conf": 1}))]),
 ("Lavoro", "Prima mattina in redazione (I21, I22): Barbara rimprovera Sara, commenta la scollatura; il caffè di Roberta; Jessica cambiata", "Barbara, Roberta, Jessica", [
   S(0, "Barbara la rimprovera", ("Scusarsi subito", {}), ("Spiegare con calma", {"Conf": 1}), ("Una battuta", {"Conf": 1, "Barbara": 1})),
   S(0, "Il commento sulla scollatura", ("Arrossire e coprirsi", {}), ("Far finta di niente", {}), ("«Grazie... credo»", {"Barbara": 1})),
   S(1, "Jessica la invita all'aperitivo di giovedì", ("Accettare", {}), ("Rifiutare", {}))]),
 ("Sera", "Prologo a casa; Joanie la iscrive in palestra", "Josh, Joanie", [
   S(1, "La serata", ("Chiudere il portatile e stare con Josh 🔒 Josh 30", {"Josh": 3}), ("Scrivere ancora un'ora", {"Conf": 2})),
   S(0, "La cena", ("Cucinare qualcosa per Josh", {"Josh": 1}), ("Ordinare una pizza", {})),
   S(0, "Joanie e la palestra", ("Accettare con entusiasmo", {"Joanie": 1}), ("Accettare sbuffando", {}))]),
]))
D.append(("2 Mar", [
 ("Lavoro", "Giornata normale", "", [
   S(0, "Pausa pranzo", ("Con le colleghe", {}), ("Da sola, a scrivere", {"Conf": 1}), ("Messaggi dolci a Josh", {"Josh": 1}))]),
 ("Sera", "Palestra: Simon 1 e 2; tornando, Josh la invita alla cena aziendale", "Simon, Joanie, Josh", [
   S(0, "Cosa indossare", ("La maglietta larga", {}), ("Il top aderente che le presta Joanie", {"Conf": 1, "Corr": 1, "Simon": 1})),
   S(0, "Joanie: «Dimmi che non è bello»", ("«È un bel ragazzo»", {}), ("«Sono qui per allenarmi»", {})),
   S(0, "Simon la saluta", ("Sorridergli", {"Simon": 1}), ("Salutarlo appena", {})),
   S(0, "Joanie flirta con Simon", ("Distogliere lo sguardo", {}), ("Continuare a guardare", {"Corr": 1})),
   S(0, "L'invito alla cena aziendale", ("Entusiasta", {"Josh": 1}), ("Preoccupata per Daniel", {}))]),
]))
D.append(("3 Mer", [
 ("Lavoro", "Riunione di redazione", "", [
   S(0, "In riunione", ("Prendere il pezzo che le danno", {}), ("Proporre un'idea sua", {"Conf": 2}))]),
 ("Sera", "Cena aziendale: Daniel 1; in auto la riga di Josh su suo padre (I1)", "Daniel, Josh", [
   S(0, "Il vestito", ("Sobrio", {}), ("Quello nero che piace a Josh", {"Josh": 1}), ("Il più audace che ha", {"Corr": 1, "Daniel": 1})),
   S(1, "Daniel umilia Josh", ("Rispondergli a tono", {"Daniel": 2, "Conf": 1}), ("Stringere la mano di Josh", {"Josh": 2}), ("Cambiare discorso", {})),
   S(0, "Daniel le parla al brindisi", ("Gelida", {}), ("Sorridere per educazione", {"Daniel": 1})),
   S(1, "In auto", ("Consolarlo: «È lui il problema»", {"Josh": 3}), ("«Perché non hai reagito?»", {"Josh": -2}))]),
]))
D.append(("4 Gio", [
 ("Lavoro", "Barbara passa senza guardarla", "Barbara, Jessica", [
   S(0, "Jessica le chiede un parere sul vestito", ("«Stai benissimo»", {}), ("«Eri più bella prima»", {"Conf": 1}))]),
 ("Sera", "Aperitivo con le colleghe (se accettato), altrimenti serata libera", "Colleghe, Barbara", [
   S(0, "All'aperitivo: Barbara arriva e offre da bere", ("Accettare il drink", {"Barbara": 1}), ("Rifiutare con un sorriso", {})),
   S(0, "All'aperitivo", ("Un bicchiere e basta", {}), ("Lasciarsi andare", {"Corr": 1, "Barbara": 1})),
   S(0, "Se ha rifiutato l'aperitivo", ("Scrivere", {"Conf": 1}), ("Serata con Josh", {"Josh": 1}))]),
]))
D.append(("5 Ven", [
 ("Prima del lavoro", "Pianerottolo: Howard 1; Josh ha dimenticato la patente", "Howard", [
   S(1, "Howard vuole chiacchierare", ("Fermarsi un minuto", {"Howard": 2}), ("Tagliare corto", {}))]),
 ("Pausa pranzo", "Ufficio di Josh: Daniel 2", "Daniel, Josh", [
   S(0, "Daniel la prende in giro", ("Ignorarlo", {}), ("🔒 Conf 24 «Almeno lui non dimentica le persone»", {"Daniel": 2, "Conf": 1}))]),
 ("Sera", "Venerdì sera", "Josh, Joanie", [
   S(0, "Josh è stanco", ("Film sul divano con lui", {"Josh": 2}), ("Uscire con Joanie", {"Joanie": 1}))]),
]))
D.append(("6 Sab", [
 ("Mattina", "La spesa: Howard 2, retroscena del furto", "Howard", [
   S(0, "Howard ha portato le borse", ("Ringraziarlo", {"Howard": 1}), ("Insistere per offrirgli un caffè", {"Howard": 2}))]),
 ("Pomeriggio", "Prepararsi per la sera", "", [
   S(0, "Il vestito per il locale", ("Sobrio", {}), ("Il vestito corto che le consiglia Joanie", {"Corr": 1, "Conf": 1}))]),
 ("Sera", "Locale con Joanie e Josh: Simon 3", "Simon, Joanie, Josh", [
   S(0, "Al locale", ("Ballare con Josh", {"Josh": 2}), ("Chiacchierare con Simon", {"Simon": 2}), ("Ridere troppo alle battute di Simon", {"Simon": 3, "Corr": 1, "Susp": 1}))]),
]))
D.append(("7 Dom", [
 ("Pomeriggio", "Domenica tranquilla", "Josh", [
   S(0, "Il pomeriggio", ("Scrivere", {"Conf": 2}), ("Gita con Josh", {"Josh": 2}))]),
 ("Sera", "A letto", "Josh", [
   S(0, "Con Josh", ("Prendere l'iniziativa 🔒 Josh 30", {"Josh": 2, "Conf": 1}), ("Stanca, dormire", {}))]),
]))
D.append(("8 Lun", [
 ("Lavoro", "Giornata normale", "Joanie", [
   S(0, "In ufficio", ("Concentrata sul pezzo", {"Conf": 1}), ("Chattare di nascosto con Joanie", {"Joanie": 1}))]),
 ("Sera", "Palestra: Joanie dà buca (I8); Simon 4 e, se entra, Simon 5", "Simon, Joanie", [
   S(1, "Entrare da sola?", ("Entrare", {"Conf": 3}), ("Tornare a casa", {"Josh": 1})),
   S(0, "Simon le sistema la spalla", ("«Certo»", {"Simon": 5}), ("🔒 Corr 15 «Mi sistemi anche l'altra?»", {"Simon": 6, "Corr": 3}), ("«Faccio da sola»", {"Simon": 3})),
   S(0, "A casa", ("Raccontare a Josh dell'allenamento con Simon", {}), ("Non dirlo", {"Corr": 1, "Susp": 1}))]),
]))
D.append(("9 Mar", [
 ("Lavoro", "Messaggio di Josh: «Daniel mi ha messo di turno fino alle 21» (I14)", "Josh", [
   S(0, "Rispondere", ("Affettuosa", {"Josh": 1}), ("Infastidita", {"Josh": -1}))]),
 ("Sera", "Senza chiavi, ospite di Howard: Howard 3, retroscena del pianto finto", "Howard", [
   S(0, "Casa di Howard è sporca", ("Far finta di niente", {}), ("Offrirsi di aiutarlo a pulire un giorno", {"Howard": 2})),
   S(0, "Howard piange", ("Parole gentili, a distanza", {"Howard": 1}), ("Abbracciarlo", {"Howard": 1})),
   S(1, "«Possiamo vederci più spesso?»", ("«Certo, un caffè ogni tanto»", {"Howard": 3}), ("«Quando capita»", {"Howard": 2}), ("«Ho poco tempo»", {}))]),
]))
D.append(("10 Mer", [
 ("Lavoro", "Barbara le assegna un pezzo extra fuori mansione", "Barbara", [
   S(0, "Il pezzo extra", ("Accettare senza fiatare", {}), ("Far notare che non è compito suo", {"Conf": 1}))]),
 ("Sera", "Ancora senza chiavi", "Josh", [
   S(0, "Con Josh", ("Raccontargli tutto di Howard", {"Josh": 1}), ("Minimizzare", {}))]),
]))
D.append(("11 Gio", [
 ("Lavoro", "Pranzo", "Jessica", [
   S(0, "Pausa pranzo", ("Con Jessica", {}), ("Da sola", {"Conf": 1}))]),
 ("Sera", "Howard «ritrova» le chiavi (I20), retroscena della copia", "Howard, Josh", [
   S(0, "Ringraziarlo", ("Una stretta di mano", {"Howard": 1}), ("Un abbraccio", {"Howard": 1}))]),
]))
D.append(("12 Ven", [
 ("Lavoro", "Esce il primo pezzo di Sara", "", [
   S(0, "A chi mandarlo per primo", ("A Josh", {"Josh": 1}), ("A Joanie", {"Joanie": 1}))]),
 ("Sera", "Telefonata con Joanie, che la spinge", "Joanie", [
   S(0, "Di chi parlare", ("Di Simon", {"Simon": 1, "Joanie": 1}), ("Di Daniel", {"Daniel": 1, "Joanie": 1}), ("Solo di lavoro", {})),
   S(0, "Il consiglio di Joanie", ("Ascoltarlo", {"Corr": 1, "Joanie": 1}), ("Riderne", {}))]),
]))
D.append(("13 Sab", [
 ("Mattina", "Shopping con Joanie per la festa", "Joanie", [
   S(0, "Il vestito per la festa", ("Sobrio", {}), ("Elegante", {"Conf": 1}), ("Audace, scelto da Joanie", {"Corr": 2, "Conf": 1, "Joanie": 1}))]),
 ("Pomeriggio", "Palestra libera (facoltativa)", "Simon", [
   S(0, "Andare?", ("Sì", {"Simon": 2}), ("No", {}))]),
 ("Sera", "Festa di Daniel: Daniel 3, primo incontro con Magnus (I4); finale a casa", "Daniel, Magnus, Josh", [
   S(0, "Daniel le presenta Magnus", ("Ringraziarlo sinceramente", {"Daniel": 2}), ("Restare fredda", {})),
   S(1, "Con Magnus", ("Entusiasmo", {"Magnus": 4}), ("Timidezza", {"Magnus": 2}), ("🔒 Conf 25 «Le mando le pagine domani»", {"Magnus": 5, "Conf": 2})),
   S(1, "Finale: il biglietto di Magnus", ("Dirlo a Josh 🔒 Josh 30", {"Josh": 2}), ("Tenerlo segreto", {"Corr": 2, "Susp": 3}))]),
]))
D.append(("14 Dom", [
 ("Pranzo", "Le due famiglie a tavola (I3, I1, I2, I16, I7)", "Hugo, Samantha, Sally, Andrew, Josh", [
   S(1, "Hugo sminuisce Josh", ("Difenderlo", {"Josh": 3, "Conf": 1}), ("Tacere", {}), ("Sorridere alla battuta", {"Josh": -2})),
   S(0, "Sally la riprende per il vestito", ("Abbassare gli occhi", {}), ("Rispondere a tono", {"Conf": 1})),
   S(0, "Samantha la invita a fare shopping insieme", ("Accettare", {}), ("Declinare", {}))]),
]))
D.append(("15 Lun", [
 ("Lavoro", "Riunione di redazione", "", [
   S(0, "In riunione", ("Silenziosa", {}), ("Difendere una sua idea", {"Conf": 1}))]),
 ("Sera", "Le 50 pagine per Magnus", "Magnus", [
   S(1, "Mandarle?", ("Sì", {"Conf": 2, "Magnus": 1}), ("Rimandare", {}))]),
]))
D.append(("16 Mar", [
 ("Lavoro", "Jessica le riparla di «quella cosa» (I22)", "Jessica", [
   S(0, "Con Jessica", ("Chiederle cosa le è successo", {}), ("Lasciar perdere", {}))]),
 ("Sera", "Palestra", "Simon", [
   S(0, "Cosa indossare", ("La maglietta larga", {}), ("Un top aderente", {"Corr": 1, "Simon": 1})),
   S(0, "L'allenamento", ("Con Simon", {"Simon": 3}), ("Da sola", {"Conf": 1}))]),
]))
D.append(("17 Mer", [
 ("Lavoro", "Giornata normale", "", []),
 ("Sera", "Serata tra amici: entrano Darius e Mark; Josh e Mark legano (I13); dopo, Josh e Darius soli e flashback di Jacob (I18)", "Darius, Joanie, Mark, Josh", [
   S(0, "Durante la serata", ("Stare vicina a Josh", {"Josh": 1}), ("Ridere con Darius", {"Darius": 1}), ("Confidarsi con Joanie in cucina", {"Joanie": 1}))]),
]))
D.append(("18 Gio", [
 ("Lavoro", "Barbara le chiede di restare mezz'ora in più", "Barbara", [
   S(0, "Restare?", ("Sì", {"Barbara": 1}), ("Rifiutare con garbo", {"Conf": 1}))]),
 ("Sera", "Josh fa straordinari (I14); caffè da Howard se al giorno 9 ha detto sì o «quando capita»", "Howard", [
   S(0, "Andare da Howard?", ("Sì", {"Howard": 2}), ("Trovare una scusa", {})),
   S(0, "Da Howard", ("Lavare i piatti mentre parlano", {"Howard": 2}), ("Solo chiacchierare", {}))]),
]))
D.append(("19 Ven", [
 ("Lavoro", "Giornata normale", "", []),
 ("Sera", "Serata tra ragazze al locale di Jacob: il rincontro (I9), retroscena del messaggio di Joanie", "Jacob, Joanie", [
   S(1, "Jacob la saluta", ("Restare fredda", {}), ("Ridere a un vecchio ricordo", {"Jacob": 3, "Corr": 1})),
   S(0, "Jacob offre da bere", ("Rifiutare", {}), ("Accettare", {"Jacob": 1, "Corr": 1})),
   S(0, "Il numero", ("Darglielo", {"Jacob": 2}), ("No (Joanie glielo darà comunque)", {}))]),
]))
D.append(("20 Sab", [
 ("Mattina", "Casa editrice di Magnus (solo se ha mandato le pagine)", "Magnus", [
   S(0, "Con Magnus", ("Ascoltarlo", {"Magnus": 3, "Conf": 2}), ("Chiedergli consigli sul romanzo", {"Magnus": 2, "Conf": 3}))]),
 ("Sera", "Cena fuori con Josh", "Josh", [
   S(1, "La cena", ("Serata romantica 🔒 Josh 30", {"Josh": 4}), ("Distratta, pensa ad altro", {"Josh": -2, "Corr": 1})),
   S(0, "Il telefono vibra", ("Lasciarlo nella borsa", {}), ("Controllarlo a tavola", {"Susp": 2}))]),
]))
D.append(("21 Dom", [
 ("Sera", "Jacob le scrive", "Jacob, Josh", [
   S(1, "Rispondere?", ("Sì", {"Jacob": 2, "Susp": 2}), ("Ignorarlo", {})),
   S(0, "La chat", ("Lasciarla", {}), ("Cancellarla", {"Corr": 1, "Susp": -1}))]),
]))
D.append(("22 Lun", [
 ("Lavoro", "Barbara commenta l'abbigliamento di Sara", "Barbara", [
   S(0, "Il giorno dopo", ("Vestirsi come sempre", {}), ("Una scollatura in più", {"Barbara": 1, "Corr": 1}))]),
 ("Sera", "Passaggio", "", []),
]))
D.append(("23 Mar", [
 ("Lavoro", "Giornata normale", "", []),
 ("Sera", "Primo incontro a due con Jacob, da vecchi amici (se ha risposto)", "Jacob, Josh", [
   S(1, "Cosa dire a Josh", ("La verità: vede l'ex", {}), ("«Esco con una collega»", {"Corr": 2, "Susp": 3})),
   S(0, "All'incontro", ("Parlare dei ricordi", {"Jacob": 2}), ("Parlare di Josh", {"Josh": 1}), ("🔒 Corr 10 Lasciarlo avvicinare", {"Jacob": 4, "Corr": 2}))]),
]))
D.append(("24 Mer", [
 ("Lavoro", "Giornata normale", "", []),
 ("Sera", "Josh torna a casa umiliato da Daniel", "Josh, Daniel", [
   S(1, "Josh è a pezzi", ("Consolarlo 🔒 Josh 30", {"Josh": 3}), ("Irritarsi per la sua debolezza", {"Josh": -3, "Daniel": 1, "Corr": 1}))]),
]))
D.append(("25 Gio", [
 ("Lavoro", "Giornata normale", "", []),
 ("Sera", "Palestra", "Simon", [
   S(1, "Dopo l'allenamento", ("Andare a casa", {"Simon": 2}), ("🔒 Corr 15 Restare dopo la chiusura", {"Simon": 5, "Corr": 3, "Susp": 1}))]),
]))
D.append(("26 Ven", [
 ("Sera", "Howard ha visto Sara uscire elegante martedì (I19): se Interest Howard 5+, tace e lo fa capire a Sara; altrimenti lo dice a Josh «per caso»", "Howard, Josh", [
   S(0, "Esito (non sceglie il giocatore)", ("Howard tace", {"Howard": 2}), ("Howard parla a Josh", {"Susp": 3})),
   S(0, "Dopo", ("Serata a casa", {}), ("Aiutare Howard a sistemare la cucina", {"Howard": 2}))]),
]))
D.append(("27 Sab", [
 ("Sera", "Uscita a quattro con Joanie e Mark; Mark tranquillizza Josh (I13)", "Joanie, Mark, Josh", [
   S(0, "Effetto di Mark (automatico)", ("Josh si calma", {"Susp": -3})),
   S(0, "In bagno con Joanie", ("Parlare d'altro", {}), ("Raccontarle di Jacob", {"Joanie": 2, "Corr": 1}))]),
]))
D.append(("28 Dom", [
 ("Sera", "Finale dell'Episodio 2: se Susp 8+, Josh le chiede del telefono; altrimenti Magnus la invita nella sua villa", "Josh / Magnus", [
   S(1, "Se c'è il confronto", ("Mentire bene", {"Corr": 2}), ("Confessare una parte", {"Josh": -2, "Susp": -5}))]),
]))

ORD = ["Corr", "Conf", "Susp", "Josh", "Simon", "Howard", "Daniel", "Magnus", "Jacob", "Barbara", "Joanie", "Darius"]
START = {"Conf": 20, "Josh": 80}
NOMI = {"Corr": "Corr", "Conf": "Conf", "Susp": "Susp"}

def fmt(e):
    if not e: return "—"
    return ", ".join("{} {:+d}".format(k, v) for k, v in e.items())

lo = collections.Counter(); hi = collections.Counter()
nchoice = nfund = 0
rows = []
for giorno, fasce in D:
    for fascia, scena, chi, scelte in fasce:
        parti = []
        for f, q, opts in scelte:
            nchoice += 1; nfund += f
            for k in ORD:
                vals = [o[1].get(k, 0) for o in opts]
                lo[k] += min(vals); hi[k] += max(vals)
            star = "★ " if f else ""
            parti.append("{}**{}:** ".format(star, q) + " · ".join("{} → {}".format(o, fmt(e)) for o, e in opts))
        rows.append((giorno, fascia, scena, chi, "<br>".join(parti) if parti else "—"))

def clamp(x): return max(0, min(100, x))

out = []
w = out.append
w("# The Thin Line — Il primo mese di gioco\n")
w("Bozza di lavoro | 16 novembre 2026 · **✅ Approvato da Jody il 16/11/2026** (versione 2, molte più scelte). È la base per la riscrittura degli Episodi 1 e 2.\n")
w("## 1. Regole\n")
w("- **Lunedì-venerdì:** Sara lavora in redazione **9-17**. Fasce: *prima del lavoro* (se serve), **Lavoro**, **Sera**. **Sabato e domenica:** **Mattina**, **Pomeriggio**, **Sera**.")
w("- **Le fasce senza scene non si giocano:** una riga di passaggio.")
w("- **Molte scelte.** Ogni giornata ne ha almeno una, quasi sempre di più. Sono di due tipi:")
w("  - **★ Fondamentali:** cambiano la storia (aprono o chiudono scene, creano segreti, decidono la direzione di un percorso).")
w("  - **Piccole:** non cambiano la storia adesso, ma muovono le variabili e serviranno più avanti (soglie, frasi 🔒, abiti, finali).")
w("- **Un mese = 4 settimane = 28 giorni.** Episodio 1 = settimane 1-2 (fino alla festa di Daniel), Episodio 2 = settimane 3-4. Il giorno 1 è un lunedì.")
w("- **Barbara va pianissimo:** pochi momenti, quasi tutti piccoli, e il suo Interest resta bassissimo. Il percorso vero comincia nel secondo mese.\n")
w("**Legenda:** `Simon +3` = Interest verso Simon · `Josh +2` = Interest verso Josh · `Corr` = Corruption · `Conf` = Confidence · `Susp` = Suspicion di Josh · 🔒 = frase con requisito · (I8) = intreccio approvato · — = nessun effetto.\n")
w("Valori di partenza: Corr 0 · Conf 20 · Susp 0 · Josh 80 · tutti gli altri Interest 0.\n")
w("Totale: **{} scelte**, di cui **{} fondamentali** (★).\n".format(nchoice, nfund))

sett = {1: (1, 7, "Settimana 1 — Episodio 1"), 2: (8, 13, "Settimana 2 — Episodio 1 (fino alla festa)"), 3: (14, 21, "Settimana 3 — Episodio 2"), 4: (22, 28, "Settimana 4 — Episodio 2")}
num = lambda g: int(g.split()[0])
sec = 2
for s, (a, b, titolo) in sett.items():
    w("## {}. {}\n".format(sec, titolo)); sec += 1
    w("| Giorno | Fascia | Scena | Chi | Scelte → effetti |")
    w("|---|---|---|---|---|")
    last = None
    for g, fa, sc, chi, ch in rows:
        if a <= num(g) <= b:
            gg = "**{}**".format(g) if g != last else ""
            last = g
            w("| {} | {} | {} | {} | {} |".format(gg, fa, sc, chi, ch))
    if s == 2:
        w("\n**Fine dell'Episodio 1.**")
    w("")

w("## {}. Valori a fine mese (calcolati)\n".format(sec)); sec += 1
w("Somma dei minimi e dei massimi di ogni scelta, come se fossero tutte disponibili: è un limite teorico (alcune scelte si escludono o hanno requisiti).\n")
w("| Variabile | Minimo | Massimo |")
w("|---|---|---|")
for k in ORD:
    s0 = START.get(k, 0)
    name = {"Corr": "**Corruption**", "Conf": "**Confidence**", "Susp": "**Suspicion**", "Josh": "**Interest Josh**"}.get(k, "Interest " + k)
    w("| {} | {} | {} |".format(name, clamp(s0 + lo[k]), clamp(s0 + hi[k])))
w("")
w("## {}. Cosa si apre con queste variabili\n".format(sec)); sec += 1
w("- **Simon (soglia 15):** il giocatore che sceglie sempre l'opzione più spinta la raggiunge verso il giorno 19 (fine settimana 3) e apre la scena 🔒 del giorno 25. La frase 🔒 del giorno 8 resta chiusa per tutti: è un assaggio di cosa si perde. Il giocatore prudente non arriva a 15.")
w("- **Jacob (soglia 25):** raggiungibile solo all'ultimo giorno, e solo con tutte le scelte più spinte: pronta per l'Episodio 3.")
w("- **Darius (35) e gli altri:** irraggiungibili nel primo mese, come vuole lo slow burn.")
w("- **Frasi 🔒 Josh 30:** sempre aperte nel primo mese; si chiuderanno solo se l'Interest verso Josh crolla più avanti.")
w("- **Confidence:** chi scrive, entra da sola in palestra e si fa valere in redazione supera 25 presto e apre le frasi coraggiose (Daniel al giorno 5, Magnus al giorno 13).\n")
w("## {}. Decisioni approvate\n".format(sec))
w("1. Ritmo dei numeri: piccole ±1, importanti ±2-3, fondamentali fino a ±5.")
w("2. Episodio 1 di due settimane, con la festa di Daniel come finale.")
w("3. Finale doppio dell'Episodio 2: confronto con Josh se Susp alta, invito di Magnus se bassa.")
open(OUT, "w", encoding="utf-8", newline="").write("\n".join(out) + "\n")
print("scelte", nchoice, "fondamentali", nfund)
for k in ORD:
    print(k, clamp(START.get(k, 0) + lo[k]), clamp(START.get(k, 0) + hi[k]))
