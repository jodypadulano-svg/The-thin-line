# The Thin Line — Inquadrature del giorno 18

**Bozza del 24/11/2026. 20 CG nuove per Mage e 5 clip video per il ballo; 2 CG riusate dall'Episodio 1.** Esportazione WebP, 16:9; video WebM muti (la canzone `daniel_seduzione` resta sotto). Il codice è in [ep2_giorno18.rpy](../../game/episodio2/ep2_giorno18.rpy).

**Da decidere con Jody:** al pranzo Sara può avere tre abiti (top nero sotto il blazer, vestito grigio, abiti da lavoro). Oggi il codice usa una sola immagine per momento. Proposta: generare le CG del pranzo e del ballo con il **top nero** come base, che è il ramo più visivo, e aggiungere varianti con il vestito grigio solo per 04, 08 e 09 se servono.

## Riferimenti

- **Attori adulti:** [Sara](/C:/Users/Jody/the-thin-line/riferimenti/attori/sara_acquerello_riferimento_v2_capelli_mossi.webp), [Daniel](/C:/Users/Jody/the-thin-line/riferimenti/attori/daniel_acquerello_candidato.webp), [Barbara](/C:/Users/Jody/the-thin-line/riferimenti/attori/barbara_acquerello_candidato.webp), [Howard](/C:/Users/Jody/the-thin-line/riferimenti/attori/howard_acquerello_candidato.webp), [Jessica](/C:/Users/Jody/the-thin-line/riferimenti/attori/jessica_acquerello_candidato_v2.webp).
- **Luoghi:** [casa, camera](/C:/Users/Jody/the-thin-line/riferimenti/luoghi/casa_camera_mattina.webp), [cucina](/C:/Users/Jody/the-thin-line/riferimenti/luoghi/casa_cucina.webp), [redazione](/C:/Users/Jody/the-thin-line/riferimenti/luoghi/redazione.webp), [ufficio di Barbara](/C:/Users/Jody/the-thin-line/riferimenti/luoghi/ufficio_barbara.webp), [ristorante](/C:/Users/Jody/the-thin-line/riferimenti/luoghi/ristorante.webp) (da adattare a una saletta privata), [casa di Howard](/C:/Users/Jody/the-thin-line/riferimenti/luoghi/casa_howard.webp).
- **Top nero:** la [CG del pacco del 17](/C:/Users/Jody/the-thin-line/game/images/cg/ep2/d17_pacco_top.png): mesh nera trasparente, maniche lunghe, collo alto ondulato, due grandi pannelli tondi opachi uniti da un ponticello.
- **Ballo:** per pose e luce, il [video C della terrazza](/C:/Users/Jody/the-thin-line/game/images/video/ep1/d13_vc_fianchi.webm) e la [giacca](/C:/Users/Jody/the-thin-line/game/images/cg/ep1/d13_10b_giacca_spalle.webp).
- **Riusate:** `ep1/d9_04_howard_porta.webp` (Howard sulla porta), `ep1/d11_08_tazze_nuove.webp` (step 2 delle tazze).
- **Abiti proposti:** Daniel in camicia bianca, senza cravatta, giacca scura sulla sedia. Barbara come al giorno 17. Howard in cardigan e pantofole.

Anteporre a ogni prompt:

> Soft watercolor and visible graphite pencil on textured paper, matching the supplied adult character and location references. Immersive illustrated visual novel scene, wide 16:9 landscape composition, natural anatomy and hands, quiet lower edge for dialogue. No readable text, watermarks, logos or UI.

## Prompt

### 01 · `d18_01_colazione.webp` — base (senza pranzo)

> Early Thursday morning in the kitchen. Adult Sara, dressed for work, drinks coffee standing at the counter, coat over her arm. Josh's rinsed mug sits upside down in the sink. Pale morning light, quiet, ordinary.

### 01 · `d18_01_armadio.webp` — base (con pranzo)

> Bedroom, morning. Adult Sara in a slip stands before an open wardrobe, one hand on a hanger, deciding. A cold coffee cup on the dresser. The black mesh top hangs over the back of a chair. Soft morning light, a private, undecided moment.

### 01a · `d18_01a_top_nero.webp` — da 01 armadio

> Same bedroom. Sara now wears the black sheer mesh top with long sleeves, wavy high collar and two large opaque round panels joined by a thin strip, under an open dark blazer, with work trousers. She studies herself in the mirror, one hand on the blazer button, a small private smile.

### 02 · `d18_02_redazione.webp` — base

> Newsroom, morning. Sara at her desk; Jessica leans over the low partition holding a stack of proofs, teasing. Cool daylight, desks receding.

### 03 · `d18_03_pranzo_scrivania.webp` — base (senza pranzo)

> Sara alone at her desk at lunch, a sandwich beside an open notebook with crossed-out lines, her phone face down. Calm midday light.

### 04 · `d18_04_saletta.webp` — base

> A small private dining room in an elegant restaurant: one table laid for two, white linen, a window onto a courtyard with a fig tree, a small speaker on a sideboard. Daniel in a white open-collared shirt rises from the table as Sara enters through the door, the waiter's arm just visible holding it. Warm midday light, intimate and exclusive.

### 05 · `d18_05_tavolo.webp` — da 04

> Seated two-shot across the table, a bread basket between them. Daniel turns his wine glass slowly, watching Sara; Sara tears a piece of bread, holding back a smile. Fig tree soft in the window.

### 06 · `d18_06_conto.webp` — da 04 (ramo professionale)

> Daniel signs the bill without looking at it while Sara stands putting on her coat. Courteous distance between them, the table cleared.

### 07 · `d18_07_musica.webp` — da 04 (ramo privato)

> Daniel stands by the sideboard with his phone in hand, by the small speaker, looking back over his shoulder at Sara still seated, as if he already knows her answer.

### 08 · `d18_08_abbraccio.webp` — base del ballo

> Daniel draws Sara close by the waist in the small room, the fig tree window behind them. Her forehead almost at his collar, her hands on his chest. Slow, close, unhurried; Sara visibly enjoying it.

### 08c · `d18_08c_daniel_pp.webp` — primo piano

> Close-up of Daniel looking down at Sara, amused and certain, his mouth near her hair.

### 08d · `d18_08d_sara_pp.webp` — primo piano

> Close-up of Sara against Daniel's shoulder, eyes half closed, cheeks flushed, biting back a smile.

### 09 · `d18_09_mandibola.webp` — ramo «salto in avanti» (bacio sull'orecchio già avvenuto il 13)

> Close-up: Daniel's lips trace from just below Sara's ear along her jaw, stopping at the corner of her mouth. Her eyes closed, lips parted, face beginning to turn toward him. Blissful, wanting.

### 09b · `d18_09b_si_ferma.webp` — da 09

> The instant after: Sara has turned her face to meet his mouth, but Daniel has drawn back an inch, smiling, teasing. Her eyes just opening, half laughing at being caught.

### 09c · `d18_09c_orecchio.webp` — ramo primo bacio sull'orecchio

> Close-up while they sway: Daniel kisses Sara lightly just below the ear; she tilts her head to offer her neck, eyes closed, smiling.

### 10 · `d18_10_barbara.webp` — base

> Late afternoon newsroom. Sara with her coat half on; Barbara in her office doorway holding a folder of prints, beckoning. Low amber light.

### 11 · `d18_11_ritratti.webp` / `d18_11_ritratti_glamour.webp` — da 10

> Barbara's office. Six portrait prints in two rows on the desk; one turned face down near Barbara's hand. Sara leans over the prints. Use the usual look or the glamour look of day 17 for the photos in the prints, according to the file. Barbara holds out a small sticky note between two fingers.

### 12 · `d18_12_lampadina.webp` — step 3

> Howard's small bathroom. Sara stands on the edge of the bathtub changing a light bulb, arms raised, blouse pulled taut; Howard below holds her hips very correctly and looks up, sheepish and delighted. Sara blushing, about to laugh. If barefoot (Savior Complex) her shoes are on the bathmat.

### 13 · `d18_13_ragu.webp` — step 4

> Howard's small kitchen, a big pot simmering. Sara at the stove with a wooden spoon; Howard stands close behind her, shorter than her, his hands over hers on the spoon, his gaze lower than her shoulder. Warm steam and lamplight, homely and a little mischievous.

## Clip del ballo (WebM, muti)

Stessi tempi della terrazza: ritornello 1 a 0:49, strofa 2 a 1:18, ritornello 2 a 2:00, ponte a 2:29. Base 08.

| File | Momento | Contenuto |
|---|---|---|
| `d18_va_dondolio.webm` | 0:49, 15 s | Dondolano lenti, lei con la fronte quasi sul colletto |
| `d18_vb_giro.webm` | 1:18, 15 s | Lui la fa girare piano, lei finisce di schiena alla finestra |
| `d18_vc_fianchi.webm` | 2:00, 15 s | Le mani di lui basse sui fianchi, quelle di lei piatte sul suo petto |
| `d18_vd_mandibola.webm` | 2:29, 15 s | Labbra dall'orecchio alla mandibola fino all'angolo della bocca; lei gira il viso, lui si ritrae sorridendo |
| `d18_vd_orecchio.webm` | 2:29, 12 s | Bacio leggero sotto l'orecchio, lei inclina la testa |
