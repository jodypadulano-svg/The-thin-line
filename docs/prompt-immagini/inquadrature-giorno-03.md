# The Thin Line — Inquadrature del giorno 3 (campo e controcampo)

Bozza di lavoro | 17 novembre 2026 · Testo del giorno 3 in `game/episodio1/ep1_giorno03.rpy` (da rivedere con Jody). Stesse regole dei giorni 1-2: un cambio d'immagine ogni 3-4 battute, inquadrature che si alternano e si ripetono. Formato **16:9, 2K**, stesso stile. ✅ = fatta.

**Character:** `@sara_wc`, `@josh_wc`, `@daniel_wc`, `@barbara_wc`.
**Per il viso di Sara** allega sempre anche `riferimenti/scene/giorno02/04_messaggi_josh.webp` (o un'altra Sara recente). Nei prompt: *same face, hair and bust size as in the reference images, natural unpainted nails*.

**Redazione tutta femminile** (decisione 17/11): nelle scene in redazione le colleghe sono solo donne; se servono figure sullo sfondo, scrivi *female colleagues*.

**Due vestiti alla cena.** La scelta del vestito cambia le immagini della cena in cui si vede Sara:
- base (vale per il vestito sobrio **e** per quello nero che piace a Josh): *a simple dark navy dress with short sleeves, knee length, modest neckline*;
- variante **`_audace`** (stessa immagine modificata): *a fitted red dress, low neckline showing cleavage, hem well above the knee*.
Il codice sceglie da solo quale mostrare.

**Aggiornamento 18/11 (Jody): tre vestiti, tre versioni.** Il nero ha le sue varianti **`_nero`** (stessa immagine modificata col vestito della B4): `d3_06_arrivo_nero`, `d3_08_sguardo_daniel_nero`, `d3_09_tavolata_nero`, `d3_12_sara_tavola_nero`, `d3_13_brindisi_nero`, `d3_14_auto_nero`, `d3_17_bagno_nero`. Finché una manca, il gioco mostra quella col vestito blu. Gli zoom dello sguardo di Daniel usano le aree della versione blu, tranne la scollatura col nero: (600,420,640,360). Tutte fatte il 18/11.

Blocco di stile (in fondo a ogni prompt):
`Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.`

Totale: **20 immagini nuove + 7 varianti `_audace` + 7 varianti `_nero`** = 34 file. Luoghi nuovi: **ristorante**, **bagno del ristorante** e **auto di notte** (prompt in fondo).

---

## A. Riunione di redazione

| ID | File | Inquadratura | Allega | Quando compare |
|---|---|---|---|---|
| A1 ✅ | `d3_01_riunione` | Il tavolo della riunione, Barbara a capotavola, Sara in fondo | `redazione`, `04_barbara_entra` (giorno 1) | inizio giornata |
| A2 ✅ | `d3_02_sara_riunione` | Primo piano di Sara, penna ferma sul quaderno | A1, `04_messaggi_josh` | il dubbio, la scelta |
| A3 ✅ | `d3_03_barbara_riunione` | Primo piano di Barbara a capotavola | A1 | la risposta di Barbara (in tutte e due le scelte) |

**A1**
```
The newsroom from the reference image, a crowded meeting table with twelve chairs squeezed around it, morning light: @barbara_wc at the head of the table, leopard-print jacket, red hair, glasses on the tip of her nose, reading assignments from a sheet like a queen at a banquet; journalists around her, some bored, some nervous; at the far end @sara_wc in her buttoned-up white blouse holds a notebook and a pen. Same face, hair and bust size as in the reference images, natural unpainted nails. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
**A2**
```
Close-up of @sara_wc at the meeting table from the reference image, buttoned-up white blouse, pen frozen over an open notebook full of crossed-out notes (no readable text), biting her lip, eyes raised toward the head of the table, torn between fear and courage. Same face, hair and bust size as in the reference images, natural unpainted nails. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
**A3**
```
Close-up of @barbara_wc at the head of the meeting table from the reference image, glasses lowered on her nose, red-nailed finger tapping the table, looking toward the viewer with a sharp, amused, evaluating expression, one eyebrow raised. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```

---

## B. A casa — i tre vestiti

| ID | File | Inquadratura | Allega | Quando compare |
|---|---|---|---|---|
| B1 ✅ | `d3_04_tre_vestiti` | Sara in accappatoio, tre vestiti sul letto | `casa_camera_mattina` (di sera), `01_armadio` (giorno 1) | la scelta del vestito |
| B2 ✅ | `d3_05_vestito_rosso` | Sara allo specchio col vestito rosso (solo scelta audace) | B1 | «The red one…» |
| B3 ✅ | `d3_19_vestito_blu` | Sara col vestito blu allo specchio, tranquilla (solo scelta sobria) | B1, B2 | «The navy dress…» |
| B4 ✅ | `d3_20_vestito_nero` | Sara col vestito nero allo specchio, Josh si blocca sulla porta (solo scelta nero) | B1, B2, `@josh_wc` | «The black dress…» → «Now finish that tie.» |

**B1**
```
The bedroom from the reference image in the early evening, warm lamp light: @sara_wc in a soft white bathrobe, hair still damp, stands at the foot of the bed looking at three dresses laid out side by side on the quilt: a modest navy dress, a simple black dress, and a fitted red dress; her expression is comically undecided, one hand on her cheek. Same face, hair and bust size as in the reference images, natural unpainted nails. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
**I tre vestiti (fissati sulla B1 definitiva, 17/11):** blu scuro con maniche corte e scollo modesto, al ginocchio · nero semplice senza maniche, scollo rotondo, appena sopra il ginocchio · rosso corto con spalline sottili e scollo incrociato.

**B3**
```
The same bedroom from the reference image, evening lamp light: @sara_wc stands in front of the tall mirror wearing the dark navy knee-length dress with short sleeves and a modest neckline from the reference image, smoothing the skirt with both hands, a calm, satisfied little smile, hair now dry and brushed. Same face, hair and bust size as in the reference images, natural unpainted nails. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
**B4**
```
The same bedroom from the reference image, evening lamp light: @sara_wc stands in front of the tall mirror wearing the simple elegant black sleeveless dress with a modest round neckline, just above the knee, from the reference image, turning toward the door with a playful smile; in the doorway @josh_wc, in a white shirt with his tie half-knotted, has stopped dead, mouth open, completely charmed. Same face, hair and bust size as in the reference images, natural unpainted nails. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
**B2**
```
The same bedroom from the reference image, evening lamp light: @sara_wc stands in front of the tall mirror wearing the short red spaghetti-strap dress with a wrap neckline showing cleavage, hem well above the knee (as in `05_vestito_rosso`), looking at her own reflection with wide, surprised eyes and lips slightly parted, one hand on her hip, as if meeting a stranger. Same face, hair and bust size as in the reference images, natural unpainted nails. Tasteful, no nudity. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```

---

## C. La cena aziendale — Daniel 1

| ID | File | Inquadratura | Allega | Quando compare |
|---|---|---|---|---|
| C1 ✅ | `d3_06_arrivo` (+ `_audace`) | Josh porta Sara per mano verso la tavolata e Daniel | luogo `ristorante` | l'arrivo |
| C2 ✅ | `d3_07_daniel_saluta` | Daniel si alza e le stringe la mano, sorriso da copertina | C1 | la presentazione |
| C3 ✅ | `d3_08_sguardo_daniel` (+ `_audace`) | Retroscena: lo sguardo di Daniel su Sara che si siede | C1 | il retroscena |
| C4 ✅ | `d3_09_tavolata` (+ `_audace`) | La tavolata, Daniel al centro, Josh che sorride a fatica | C1 | le punzecchiature, il resto della cena |
| C5 ✅ | `d3_10_josh_umiliato` | Primo piano di Josh, sorriso forzato, forchetta ferma | C4 | «Josh looks at his plate…» |
| C6 ✅ | `d3_11_daniel_brinda` | Primo piano di Daniel appoggiato allo schienale, calice in mano, guarda Sara | C4 | la battuta del foglio Excel e le sue risposte |
| C7 ✅ | `d3_12_sara_tavola` (+ `_audace`) | Primo piano di Sara, mascella tesa, occhi accesi | C4 | la scelta |
| C8 ✅ | `d3_13_brindisi` (+ `_audace`) | Daniel in piedi accanto alla sedia di Sara, si china a parlarle | C4 | il brindisi e la scelta |
| C9 ✅ | `d3_16_josh_orgoglioso` | Primo piano di Josh orgoglioso che parla del romanzo di Sara | C4 | «And she's writing a novel.» |
| C10 ✅ | `d3_17_bagno` (+ `_audace`) | Il bagno del ristorante: Sara allo specchio, Emma accanto si rifà il rossetto | luogo `ristorante_bagno` | la pausa in bagno |
| C11 ✅ | `d3_18_emma` | Primo piano di Emma allo specchio | C10 | le battute di Emma |

**✅ Fatto il 18/11: gli sguardi di Daniel nel retroscena** (`zoom_cg` in `presentazione.rpy`; aree: fianchi C3 base (965,280,560,315), rosso (992,200,560,315); scollatura C7 base (470,420,640,360), rosso (530,380,640,360)). Come chiede la scheda di Daniel (B), il retroscena alterna lo sguardo di Daniel e brevi inquadrature sul seno e sul fondoschiena di Sara. **Niente immagini nuove:** zoom lenti in Ren'Py su immagini già fatte: fondoschiena/gambe dalla C3, scollatura dalla C7 (la più vicina, quindi la più nitida), alternati a C2/C6. Con il vestito rosso lo zoom parte dalle varianti `_audace`. Da provare quando ci sono C3 e C7; se uno zoom è troppo sfocato, solo per quello si fa un'immagine apposta.

Alternanza C: C1 → C2 → C3 → C6 (l'ordinazione) → C4 → C9 → C6 (il romanzo) → C4 → C5 → C6 → C7 (scelta) → C6 → C4 → C10 → C11 → C8.

**C1**
```
The elegant restaurant from the reference image, evening candlelight: @josh_wc in a dark suit and tie leads @sara_wc by the hand toward the long table at the back, where @daniel_wc, mid-thirties, tall, handsome, in an expensive dark suit, is rising from his chair with a confident smile; colleagues and their partners seated around the table. Sara wears a simple dark navy dress with short sleeves, knee length, modest neckline. Same face, hair and bust size as in the reference images, natural unpainted nails. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
Variante `_audace` (da C1): *Same image, but Sara wears the short red spaghetti-strap dress with a wrap neckline showing cleavage, hem well above the knee (as in `05_vestito_rosso`); a couple of heads at the table turn toward her.*

**C2**
```
Close-up of @daniel_wc at the restaurant table from the reference image, standing, mid-thirties, very handsome, dark suit, magazine-cover smile, holding out his hand toward the viewer for a handshake that lasts a moment too long, eyes fixed on the viewer with frank interest. Candlelight. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
**C3** (retroscena: inquadratura dal punto di vista di Daniel)
```
The restaurant table from the reference image, seen over the shoulder of @daniel_wc in his dark suit: a colleague beside him talks and gestures, but Daniel's attention is elsewhere; across the table @sara_wc, in a simple dark navy knee-length dress with short sleeves, is sitting down and smoothing the dress over her knees, unaware of being watched. The composition leads the eye to Sara's figure. Same face, hair and bust size as in the reference images, natural unpainted nails. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
Variante `_audace` (da C3): *Same image, but Sara wears the short red spaghetti-strap dress (as in `05_vestito_rosso`).*

**C4**
```
The long table of the restaurant from the reference image, candlelight and wine glasses: @daniel_wc at the centre holding court, telling a story with a theatrical gesture, the colleagues laughing; beside Sara, @josh_wc smiles with visible effort; @sara_wc, in a simple dark navy knee-length dress with short sleeves, does not laugh and glances at Josh. Same face, hair and bust size as in the reference images, natural unpainted nails. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
Variante `_audace` (da C4): *Same image, but Sara wears the short red spaghetti-strap dress (as in `05_vestito_rosso`).*

**C5**
```
Close-up of @josh_wc at the restaurant table from the reference image, young and slim, glasses, dark suit and tie, smiling with visible effort, his fork motionless over the plate, eyes lowered, ears slightly red. Candlelight. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
**C6**
```
Close-up of @daniel_wc leaning back in his chair at the restaurant table from the reference image, a glass of red wine in his hand, amused, a lazy predatory smile, looking straight at the viewer. Candlelight. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
**C7**
```
Close-up of @sara_wc at the restaurant table from the reference image, in a simple dark navy dress with short sleeves and a modest neckline, jaw tight, eyes flashing, cheeks flushed, between indignation and embarrassment, her hand clenched on the napkin. Candlelight. Same face, hair and bust size as in the reference images, natural unpainted nails. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
Variante `_audace` (da C7): *Same close-up, but Sara wears the short red spaghetti-strap dress (as in `05_vestito_rosso`).*

**C8**
```
The restaurant from the reference image at dessert, candlelight: @daniel_wc stands beside @sara_wc's chair holding a glass of champagne, leaning down to speak close to her ear, charming and intimate; she looks up at him, guarded; in the soft-focus background the other guests are raising their glasses in a toast and Josh is talking to a colleague. Sara wears a simple dark navy knee-length dress with short sleeves. Same face, hair and bust size as in the reference images, natural unpainted nails. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
Variante `_audace` (da C8): *Same image, but Sara wears the short red spaghetti-strap dress (as in `05_vestito_rosso`); Daniel's eyes are lowered toward it.*

**C9**
```
Close-up of @josh_wc at the restaurant table from the reference image, young and slim, glasses, dark suit and tie, beaming with pride, one open hand gesturing toward someone beside him off-frame, eyes shining, for once completely at ease. Candlelight. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
**C10**
```
The ladies' room of the elegant restaurant from the reference image, warm golden light, marble counter and a large mirror: @sara_wc, in a simple dark navy knee-length dress with short sleeves, leans on the counter catching her breath, looking at her own reflection; beside her an elegant woman in her forties with short dark hair, pearl earrings and an emerald dress reapplies red lipstick with calm, practiced gestures and glances at Sara in the mirror. Same face, hair and bust size as in the reference images for Sara, natural unpainted nails. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
Variante `_audace` (da C10): *Same image, but Sara wears the short red spaghetti-strap dress (as in `05_vestito_rosso`).*

**C11**
```
Close-up of the same elegant woman in her forties from the reference image, short dark hair, pearl earrings, emerald dress, lipstick in hand, looking at the viewer through the mirror with a knowing, slightly tired, amused smile. Warm golden light. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```

---

## D. In auto — la riga di Josh su suo padre (I1)

| ID | File | Inquadratura | Allega | Quando compare |
|---|---|---|---|---|
| D1 ✅ | `d3_14_auto` (+ `_audace`) | Dentro l'auto di notte, Josh guida, Sara lo guarda | luogo `auto_notte` | inizio e fine scena |
| D2 ✅ | `d3_15_josh_guida` | Primo piano di Josh alla guida | D1 | la risposta di Josh e la frase su suo padre |

**D1**
```
Night, inside the small car from the reference image: @josh_wc drives in silence, both hands on the wheel, tie loosened, the orange streetlights sliding over his face; in the passenger seat @sara_wc, in a simple dark navy dress with short sleeves, turns to look at him, worried and tender. Same face, hair and bust size as in the reference images, natural unpainted nails. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
Variante `_audace` (da D1): *Same image, but Sara wears the short red spaghetti-strap dress (as in `05_vestito_rosso`).*

**D2**
```
Close-up of @josh_wc driving at night in the car from the reference image, young and slim, glasses reflecting the streetlights, eyes fixed on the road, tie loosened, a tired, sad, distant expression, as if remembering something old. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain. No readable text, no logos. Same art style as the reference images. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```

---

## Luoghi nuovi (prima delle scene, senza personaggi)

**Ristorante** → `riferimenti/luoghi/ristorante.webp`
```
Watercolor and pencil illustration of an elegant restaurant in the evening: white tablecloths, candles, crystal glasses, dark wood panels, warm golden light, a long table set for a company dinner at the back of the room, waiters' shadows, large windows on the night city lights. Refined, a little intimidating. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain, warm soft palette. No people, no readable text, no logos. Same art style as the reference image. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
**Bagno del ristorante** → `riferimenti/luoghi/ristorante_bagno.webp`
```
Watercolor and pencil illustration of the ladies' room of an elegant restaurant: a marble counter with two sinks, a large gold-framed mirror, warm golden sconces, a vase of white flowers, dark wood doors of the stalls, soft and luxurious. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain, warm soft palette. No people, no readable text, no logos. Same art style as the reference image. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
**Auto di notte** → `riferimenti/luoghi/auto_notte.webp`
```
Watercolor and pencil illustration of the inside of a small, ordinary, slightly old car at night, seen from the back seat: the driver's and passenger's seats, the dashboard dimly lit, the windshield showing a city street with orange streetlights and blurred traffic lights, raindrops on the glass. Quiet, intimate, a little melancholic. Visible pencil sketch lines, soft watercolor washes with gentle color bleeding, textured paper grain, muted palette. No people, no readable text, no logos. Same art style as the reference image. Clearly a hand-painted illustration, not photorealistic. Wide 16:9 composition.
```
