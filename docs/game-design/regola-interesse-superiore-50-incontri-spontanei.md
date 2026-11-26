# Regola importante — Incontri spontanei di Sara con interesse superiore a 50

**Stato:** regola di game design vincolante.

**Precisazione successiva (25–26/11):** la proposta di Jacob «ogni sera libera» oltre 50 è stata sostituita dal [mercoledì di Josh](../narrative/mercoledi-di-josh-2026-11-25.md), fatte salve le eccezioni narrative già concordate; gli appuntamenti restano step indipendenti dalla data. Per Howard, il mercoledì richiama la scala narrativa mentre le visite spontanee dopo il lavoro alimentano soltanto la rotazione delle faccende. Vedi [pianificazione 22–24](../narrative/giorni22-24-pianificazione-2026-11-26.md).

## Principio generale

Quando il valore numerico dell'**interesse di Sara verso un personaggio supera strettamente 50** (`interesse > 50`), Sara **inizia a cercare autonomamente occasioni per incontrarlo più spesso**, senza che ogni iniziativa debba partire dal giocatore o dal personaggio interessato.

- La condizione si attiva **dal momento esatto** in cui il valore matematico passa sopra 50: **50 non basta**, 51 sì (oppure 50,1 se il sistema usa decimali).
- Il controllo va effettuato su **ciascun personaggio separatamente**.
- Si tratta di iniziativa narrativa di Sara, soggetta alle condizioni logistiche e alle disponibilità dei personaggi.
- Le regole individuali sottostanti **prevalgono sulla formulazione generale**. Per alcuni personaggi non si aggiungono visite o incontri fisici.
- Questa specifica descrive il comportamento **finché l'interesse resta superiore a 50**. Eventuali regole di persistenza sotto soglia, conflitti di calendario e priorità tra più interessi contemporanei restano da definire; non introdurre automatismi ulteriori senza decisione progettuale.

## Comportamento per personaggio

| Personaggio | Conseguenza di `interesse > 50` |
| --- | --- |
| **Howard** | Dal giorno 17, Sara decide di suonare **dopo il lavoro** se è libera, sa che Howard è in casa e **non lo incontra per altri motivi quel giorno**. L'iniziativa è sua. La visita spontanea fa avanzare solo la rotazione delle faccende. |
| **Simon** | Sara può prendere l'iniziativa di andare in **palestra almeno un paio di volte a settimana** per aumentare le occasioni d'incontro. Coordinare le visite con il calendario. |
| **Joanie** | **Nessun cambiamento aggiuntivo** nella frequenza degli incontri: Sara interagisce con lei principalmente tramite telefono. |
| **Darius** | **Nessun cambiamento aggiuntivo**: il contatto è principalmente telefonico. |
| **Barbara** | **Nessun cambiamento aggiuntivo**: Sara la vede già regolarmente al lavoro. |
| **Jacob** | Sara gli propone di **uscire ogni sera libera possibile**; l'uscita avviene **quando Jacob è disponibile**. Distinguere fra invito di Sara e incontro effettivamente realizzato. |
| **Magnus** | **Nessun cambiamento aggiuntivo** nel comportamento di ricerca degli incontri. |
| **Daniel** | Sara comincia a **inventare motivi/scuse per recarsi sul posto di lavoro di Josh**, così da poter incontrare Daniel. **Joanie può aiutarla** a trovare o rendere credibili queste occasioni. |

## Indicazioni di implementazione narrativa

1. Valutare la soglia sul valore effettivo della variabile di interesse, non sul suo arrotondamento visivo.
2. I comportamenti devono essere attivati **immediatamente al superamento** della soglia, senza attendere un ulteriore evento di trama o una richiesta esplicita del giocatore.
3. Le intenzioni quotidiane o settimanali non garantiscono automaticamente che l'altra persona sia presente, disponibile o che la scena possa avere luogo.
4. Preservare il calendario di gioco e le altre condizioni già stabilite (conoscenza della presenza di Howard in casa; sere libere e disponibilità di Jacob; possibilità di palestra per Simon; accesso plausibile al lavoro di Josh per Daniel).
5. Non creare nuove visite automatiche per Joanie, Darius, Barbara o Magnus.
6. La conseguenza deve essere percepibile dal giocatore come un cambiamento dell'**iniziativa spontanea di Sara** quando il suo interesse cresce.

## Casi di controllo

- `interesse_Howard = 50`: non scatta la nuova routine. Con `> 50`, dopo il lavoro, Sara decide di suonare se è libera, sa che lui è in casa e non lo incontra per altri motivi quel giorno.
- `interesse_Simon > 50`: Sara può pianificare almeno due occasioni settimanali in palestra, compatibilmente con il calendario.
- `interesse_Jacob > 50`: in ogni sera libera Sara propone un'uscita; Jacob può non essere disponibile.
- `interesse_Daniel > 50`: si rendono possibili iniziative di Sara per passare dal lavoro di Josh, anche con l'aiuto di Joanie.
- `interesse_Joanie/Darius/Barbara/Magnus > 50`: non aggiungere nuovi incontri fisici in virtù di questa regola.
