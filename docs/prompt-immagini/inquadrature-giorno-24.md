# Inquadrature del giorno 24 — «Dice Night»

Decisioni: [registro](../decisioni.md), «Giorno 24». Codice: `game/episodio2/ep2_giorno24.rpy` e `game/percorsi/jacob_incontri.rpy` (Jacob, incontro #1).
**58 CG + 3 video: 58 fatte, 12 da ritoccare (🔧):** 19 del giorno, 13 di Jacob #1, 3 di Simon, 11 di Daniel (+ 2 video, li fa Jody), 3 di Joanie, 3 di Darius, 6 di Howard. Ogni giocata ne vede solo una parte: le CG C1-C5 sono alternative (una per pista), H1-H3 pure, e si vede una sola uscita.
**Varianti d'abito con Daniel:** Sara sceglie fra abito verde scuro, vestito grigio e top nero di Joanie. Si genera la base col verde; il grigio e il top si fanno **dalla CG originale cambiando solo l'abito** (stessa posa, luce e inquadratura), con suffisso `_grigio` / `_top`. Per ora il codice usa solo la base: le varianti si agganciano quando ci sono.

Cartella base: `C:\Users\Jody\the-thin-line\`. I riferimenti sono in `C:\Users\Jody\the-thin-line\riferimenti\attori\` e `C:\Users\Jody\the-thin-line\riferimenti\luoghi\`.

## Come si lavora (vale per qualunque assistente)

1. **Una immagine alla volta.** Si dà il prompt in inglese con l'elenco dei riferimenti **in ordine, scritto dentro il blocco del prompt**, con i **percorsi completi** e **i file allegati alla risposta**, così Jody non deve cercarli; Jody la genera e la manda; si controlla; poi si passa alla successiva.
2. **Mai proporre di tagliare CG.**
3. **Ogni volta dire la percentuale:** CG fatte sul totale del giorno e dell'episodio.
4. **Controllare ogni immagine e dire sempre cosa non torna**, con la correzione già pronta: continuità, abiti, mani, capelli, seno troppo grande **o** troppo piccolo, volti, storia.
5. **Riferimenti:** allegare sempre il riferimento approvato, mai una Sara recente.
6. Formato 16:9, almeno 1344×768, salvata `.webp` in `game/images/cg/ep2/` col nome esatto della tabella.
7. Non modificare il codice e non fare commit: se ne occupa Claude. Il file finito si segna ✅ qui sotto.

## Frase da mettere prima di ogni prompt

**Regola di Jody (26/11):** nei prompt non scrivere mai «adult» né «mature face»: Mage genera volti di 40-45 anni. L'età si dà solo col numero.

> Soft watercolor and visible graphite pencil on textured paper, matching the supplied character and location references. Immersive illustrated visual novel scene, wide 16:9 landscape composition, natural anatomy and hands, quiet lower edge for dialogue. No readable text, watermarks, logos or UI.

## Personaggi e riferimenti

| Chi | Riferimento (`riferimenti/attori/`) | Frase fissa |
|---|---|---|
| Sara | `sara_acquerello_riferimento_v2_capelli_mossi.webp` | Sara, 27, softly wavy dark chestnut-brown hair to the shoulders, mostly brown with only subtle copper highlights, **definitely not red, not auburn, not curly** (se escono rossi, inpaint solo dei capelli), freckles, brown eyes, slim, bust exactly as large as in the reference |
| Josh | `josh_acquerello_candidato.webp` (figura intera: `josh_figura_intera.webp`) | Josh, 25, exactly as in the reference, gentle face |
| Darius | `darius_acquerello_candidato.webp` | Darius, 25, exactly as in the reference: Black, medium-length frizzy hair, streetwear |
| Howard | `howard_acquerello_candidato.webp` | Howard, 64, exactly as in the reference, short, in his cardigan |
| Simon | `simon_acquerello_candidato.webp` | Simon, 30, exactly as in the reference, athletic |
| Daniel | `daniel_acquerello_candidato.webp` | Daniel, 43, exactly as in the reference, assured, elegant |
| Joanie | `joanie_acquerello_riferimento.webp` | Joanie, 27, exactly as in the reference, **no freckles** |
| Jacob | `jacob_acquerello_riferimento.webp` | Jacob, 31, exactly as in the reference: very tall and broad, shaved head, goatee without a moustache, heavy ring on his hand |

**Ricordi di Jacob (R1-R4):** si generano **a colori**, il gioco li vira in seppia. Sara e Jacob più giovani di 4-5 anni: «Sara, 23, same face as the reference», «Jacob, 27, same face as the reference, short hair instead of shaved».

## Luoghi (`riferimenti/luoghi/`)

- Redazione: `redazione.webp`. Caffè di fronte: `caffe_di_fronte.webp`.
- Pianerottolo: `pianerottolo.webp`. **La porta di casa di Sara e Josh è quella di legno sul pianerottolo** (E1, E2).
- Casa: `casa_soggiorno_sera.webp` (F, H), `casa_camera_mattina.webp` di sera, con la lampada (G1).
- Esterno di The Lantern (Jacob 01): nuovo, nessun riferimento; strada di sera, serrande abbassate. `locale.webp` solo per il tono.
- Locale di Jacob: `strip_club.webp`, chiuso: sedie capovolte sui tavoli, palco al buio, solo il bancone acceso, più **un vecchio jukebox illuminato** in un angolo.
- Ricordi e lampione (C1): luoghi nuovi descritti nel prompt, senza riferimento.
- Simon: `fiume.webp` (il muretto sul fiume, sera). Darius: `caffe_di_fronte.webp` di sera, poi `fiume.webp` di notte, poi l'angolo sotto casa.
- **Jazz club (nuovo):** piccolo ed elegante, lampade basse, palco con contrabbasso; `locale.webp` solo per il tono. Uscita con l'auto di Daniel: `auto_notte.webp`.
- Joanie: `casa_joanie.webp`. Howard: `casa_howard.webp` di sera, luce blu della TV, coperta scozzese.

## Abiti

- **Sara, al lavoro:** come il giorno 22 (camicetta bianca, cardigan color avena, jeans scuri, stivaletti marroni); se il 22 ha scelto la scollatura, primo bottone aperto. **Esce (proposta, da confermare):** abito al ginocchio verde scuro a portafoglio, cappotto corto, orecchini buoni, stivaletti. **A casa:** maglione morbido, leggings, calzini.
- **Josh:** felpa, giubbotto, zaino dei dadi, due pacchi di biscotti.
- **Simon:** camicia blu stirata, abbottonata, maniche arrotolate, jeans. **Daniel:** abito scuro senza cravatta. **Joanie:** maglione largo, in casa.
- **Darius:** streetwear come nel riferimento. **Howard:** cardigan. **Jacob:** camicia scura con le maniche arrotolate, giacca, l'anello.

## CG

| Fatto | File in `game/images/cg/ep2/` | Cosa mostra | Allega, in quest'ordine |
|---|---|---|---|
| ✅ | `d24_a1_mattina.webp` | Sara alla scrivania mercoledì mattina, il telefono a faccia in giù accanto alla tastiera, guarda l'orologio | `redazione.webp`, Sara |
| ✅ | `d24_b1_darius_libro.webp` | Il caffè di fronte a pranzo: Darius solo al tavolino della vetrina con un tascabile consumato pieno di note a matita; Sara al bancone col panino lo riconosce | `caffe_di_fronte.webp`, Darius, Sara |
| ✅ | `d24_b2_gioco.webp` | Darius sporto sul tavolino, la matita indica di nascosto una coppia al tavolo accanto; Sara si gira appena, trattiene una risata | B1, Darius, Sara |
| ✅ | `d24_b3_pagine.webp` | Primo piano: la mano di Sara sulla pila piegata di cinquanta pagine nella borsa aperta, accanto il tascabile di Darius | B1 |
| ✅ | `d24_c1_lampione.webp` | **Pista dell'indirizzo.** Un lampione all'angolo di una via tranquilla, fiori secchi legati con lo spago e un biglietto senza firma; la mano di Sara che quasi lo tocca | Sara |
| ✅ | `d24_c2_date.webp` | **Pista del comunicato.** Il comunicato della polizia e la lettera anonima affiancati sulla scrivania, la matita di Sara ferma fra due date (non leggibili) | `redazione.webp` |
| ✅ | `d24_c3_finestra.webp` | **Pista del supermercato.** Dalla finestra della redazione, auto scure parcheggiate lungo la strada; in basso lo scontrino piegato nella mano di Sara | `redazione.webp` |
| ✅ | `d24_c4_lettera.webp` | **Nessuna pista.** La lettera anonima sulla scrivania, la matita appoggiata sopra | `redazione.webp` |
| ✅ | `d24_c5_lavoro.webp` | **Lavoro ordinario.** Sara alla scrivania nel tardo pomeriggio spunta l'ultima correzione di una lista, il cappotto già sullo schienale | `redazione.webp`, Sara |
| ✅ | `d24_d1_howard.webp` | Howard sulla porta aperta mentre Sara sale le scale dopo il lavoro, chiavi in mano | `pianerottolo.webp`, Howard, Sara |
| ✅ | `d24_e1_josh_esce.webp` | Josh sulla porta di legno aperta, zaino dei dadi in spalla e due pacchi di biscotti sotto il braccio; Sara appoggiata allo stipite | `pianerottolo.webp`, Josh, Sara |
| ✅ | `d24_e2_sola.webp` | Sara sola nell'ingresso, la porta appena chiusa, la casa silenziosa dietro di lei | `pianerottolo.webp`, `casa_soggiorno_sera.webp`, Sara |
| ✅ | `d24_f1_legge.webp` | **Romanzo.** Sara a gambe incrociate sul divano, portatile sulle ginocchia, l'ultima pagina stampata in mano, legge ad alta voce alla stanza vuota; lampada accesa | `casa_soggiorno_sera.webp`, Sara |
| ✅ | `d24_f2_libera.webp` | Primo piano di Sara illuminata dallo schermo, un piccolo sorriso privato, le dita sui tasti | F1, Sara |
| ✅ | `d24_g1_specchio.webp` | **Esce.** Sara davanti allo specchio della camera si mette un orecchino, vestita per uscire, il telefono sul comò | `casa_camera_mattina.webp` (di sera), Sara |
| ✅ | `d24_g2_howard_vede.webp` | Howard sulla soglia nel cardigan guarda Sara uscire vestita per la sera, gli occhi dalle scarpe al viso | `pianerottolo.webp`, Howard, Sara |
| ✅ | `d24_h1_josh_torna.webp` | **Romanzo.** Josh rientra piano con lo zaino vuoto, Sara ancora sul divano col portatile, sorridono tutti e due | `casa_soggiorno_sera.webp`, Josh, Sara |
| ✅ | `d24_h2_tardi.webp` | **Rientro tardi.** Josh sul divano al buio, solo la luce della TV, si gira mentre Sara entra col cappotto ancora addosso | `casa_soggiorno_sera.webp`, Josh, Sara |
| ✅ | `d24_h3_in_tempo.webp` | **Rientro in tempo.** Sara sul divano in abiti comodi, capelli sciolti, mentre Josh entra con lo zaino; le scarpe nascoste sotto il divano | `casa_soggiorno_sera.webp`, Josh, Sara |

### Jacob, incontro #1 (riusabile in qualunque giorno)

| Fatto | File in `game/images/cg/ep2/` | Cosa mostra | Allega, in quest'ordine |
|---|---|---|---|
| ✅ | `jacob1_01_arrivo.webp` | Le serrande abbassate di The Lantern con un cartellino in vetrina (non leggibile); Jacob appoggiato accanto alla porta con le mani in tasca, Sara che arriva sotto il lampione | `locale.webp` (tono), Jacob, Sara |
| ✅ | `jacob1_02_bancone.webp` | Il locale di Jacob chiuso: sedie capovolte sui tavoli, palco al buio, acceso solo il bancone e un vecchio jukebox; Jacob dietro il bancone posa due bicchieri, Sara su uno sgabello | `strip_club.webp`, Jacob, Sara |
| ✅ | `jacob1_03_racconta.webp` | Primo piano di Jacob oltre il bancone, avambracci sul piano, sorride mentre comincia un racconto | 02, Jacob |
| ✅ | `jacob1_r1_auto.webp` | **Ricordo (bello).** Jacob e Sara più giovani seduti sul cofano di un'auto rossa in panne davanti al mare, ridono sotto una pioggia leggera, i capelli di lei umidi | Jacob, Sara |
| ✅ | `jacob1_r2_telefono.webp` | **Ricordo (litigio).** Una piccola cucina di notte: Sara più giovane in piedi a braccia conserte, il telefono di Jacob a faccia in giù sul tavolo fra loro | Jacob, Sara |
| ✅ | `jacob1_04_jukebox.webp` | Jacob al jukebox inserisce una moneta, di tre quarti di spalle; Sara lo guarda dallo sgabello | 02, Jacob, Sara |
| ✅ | `jacob1_r3_festival.webp` | **Ricordo (bello).** Festival estivo nel fango al tramonto, luci appese a un albero; Sara più giovane balla in piedi sugli stivali di Jacob, le mani di lui sui suoi gomiti, ridono | Jacob, Sara |
| ✅ | `jacob1_r4_porta.webp` | **Ricordo (litigio).** Di notte, una porta: Sara più giovane esce con un borsone in spalla senza voltarsi; la mano di Jacob sullo stipite | Jacob, Sara |
| ✅ | `jacob1_05_sara.webp` | Sara sullo sgabello tiene il bicchiere con due mani e guarda Jacob oltre il bancone; dietro di lei la luce del jukebox | 02, Sara |
| ✅ | `jacob1_06_risata.webp` | **Rivalutato.** Sara ride sullo sgabello con la testa all'indietro, Jacob sorride oltre il bancone; l'unico bicchiere quasi vuoto | 02, Jacob, Sara |
| ✅ | `jacob1_07_silenzio.webp` | Primo piano: Sara con una mano a mezz'aria verso la bocca, le guance che arrossiscono, la parola ancora nell'aria | 06, Sara |
| ✅ | `jacob1_09_punto.webp` | Controcampo su Jacob: un sorriso lento e soddisfatto, un dito alzato come a segnare un punto | 06, Jacob |
| ✅ | `jacob1_08_uscita.webp` | Jacob tiene aperta la porta del locale chiuso per Sara, fuori il lampione, dietro di lui le luci del bancone che si spengono | 02, Jacob, Sara |

### Simon

| Fatto | File in `game/images/cg/ep2/` | Cosa mostra | Allega, in quest'ordine |
|---|---|---|---|
| ✅ | `d24_s1_camicia.webp` | Simon seduto sul muretto del fiume con una camicia blu stirata invece della tuta, accanto due sacchetti di carta con gli hamburger; Sara che arriva lungo il sentiero, luce della sera | `fiume.webp`, Simon, Sara |
| ✅ | `d24_s2_muretto.webp` | Sara e Simon fianco a fianco sul muretto mangiano gli hamburger dalla carta, gambe penzoloni, l'acqua scura dietro | S1, Simon, Sara |
| ✅ | `d24_s3_impegno.webp` | Simon girato verso Sara sul muretto, serio per una volta, conta qualcosa sulle dita | S1, Simon, Sara |

### Daniel (jazz club)

| Fatto | File in `game/images/cg/ep2/` | Cosa mostra | Allega, in quest'ordine |
|---|---|---|---|
| ✅ | `d24_n0_armadio.webp` | Sara all'armadio aperto con gli abiti per la sera in mano, lo specchio del comò dietro | `casa_camera_mattina.webp` (di sera), Sara |
| ✅ | `d24_n1_jazz_arrivo.webp` | Piccolo jazz club elegante prima dello spettacolo: lampade basse, palco vuoto col contrabbasso sul cavalletto; Daniel scosta la sedia per Sara a un tavolo vicino al palco | `locale.webp` (tono), Daniel, Sara |
| 🔧 | `d24_n2_flirt.webp` | Daniel e Sara al tavolino, due bicchieri, Sara ride, Daniel la guarda divertito | N1, Daniel, Sara |
| ✅ | `d24_n3_sedia.webp` | Il club ormai pieno: Sara torna dal bagno e trova una signora anziana con le perle seduta al suo posto, Daniel appoggiato allo schienale, divertito | N1, Daniel, Sara |
| 🔧 | `d24_n4_grembo.webp` | Sara seduta di lato sulle ginocchia di Daniel al tavolo affollato, schiena dritta, bicchiere in mano, parlano con gli altri; le mani di lui ben in vista sul bracciolo | N3, Daniel, Sara |
| ✅ | `d24_n5_spettacolo.webp` | Lo spettacolo: una cantante al microfono in una pozza di luce calda, la band dietro; Sara e Daniel al tavolo nel buio, i visi illuminati dal palco | N1, Daniel, Sara |
| ✅ | `images/video/ep2/d24_jazz_spettacolo.webm` | **Video senza dialoghi (Jody):** lo spettacolo, la carezza sulla mano (1344×768) | — |
| ✅ | `d24_n6_capelli.webp` | Primo piano: la testa di Sara sulla spalla di Daniel nel buio, le labbra di lui sui suoi capelli, gli occhi di lei chiusi | N5, Daniel, Sara |
| ✅ | `images/video/ep2/d24_jazz_isolati.webm` | **Video (Jody):** i due isolati dal resto del mondo; nella parte sognata Sara sembra in braccio a Daniel, tenuto così per scelta di Jody (28/11) | — |
| ✅ | `images/video/ep2/d24_jazz_sfotto.webm` | **Video con dialoghi (Jody, 28/11):** «Can you say something for me?» / «Tell me.» / «Where is your boyfriend now... and where are you?» / «He's playing D and D. I'm here... with you.» Solo nel ramo «Stay in the spell and play along» (1280×720) | — |
| 🔧 | `d24_n7_sfotto.webp` | Daniel vicino all'orecchio di Sara con un mezzo sorriso malizioso mentre finiscono gli applausi, la testa di lei ancora vicina alla sua spalla | N6, Daniel, Sara |
| 🔧 | `d24_n8_provoca.webp` | Il viso di Daniel vicinissimo a quello di Sara, occhi divertiti e indagatori; Sara a metà fra una risata e un rossore | N7, Daniel, Sara |
| ✅ | `d24_n8b_coccole.webp` | Sara rannicchiata contro il petto di Daniel al tavolo, il viso nascosto sulla sua spalla; il braccio di lui intorno a lei, il mento sui suoi capelli, un sorriso soddisfatto | N7, Daniel, Sara |
| 🔧 | `d24_n9_uscita.webp` | Fuori dal club di notte: Daniel tiene aperta la portiera dell'auto per Sara, l'insegna del club accesa dietro (non leggibile) | `auto_notte.webp`, Daniel, Sara |

### Joanie

| Fatto | File in `game/images/cg/ep2/` | Cosa mostra | Allega, in quest'ordine |
|---|---|---|---|
| 🔧 | `d24_j1_divano.webp` | Casa di Joanie: Joanie a gambe incrociate sul divano con due bicchieri di vino, batte la mano sul cuscino accanto; Sara si toglie il cappotto | `casa_joanie.webp`, Joanie, Sara |
| 🔧 | `d24_j2_confidenze.webp` | Joanie sporta in avanti, il mento sulla mano, gli occhi accesi; Sara parla col bicchiere stretto al petto | J1, Joanie, Sara |
| ✅ | `d24_j3_saluto.webp` | Joanie sulla porta saluta Sara col bicchiere, Sara sulle scale si volta sorridendo | `casa_joanie.webp`, Joanie, Sara |

### Darius

| Fatto | File in `game/images/cg/ep2/` | Cosa mostra | Allega, in quest'ordine |
|---|---|---|---|
| 🔧 | `d24_r1_biscotti.webp` | Il caffè di fronte di sera, quasi vuoto: Darius al bancone indica un barattolo di biscotti, Sara ride accanto a lui | `caffe_di_fronte.webp`, Darius, Sara |
| 🔧 | `d24_r2_via_lunga.webp` | Sara e Darius camminano lungo il fiume di notte, un sacchetto di biscotti fra loro, i lampioni riflessi sull'acqua | `fiume.webp`, Darius, Sara |
| 🔧 | `d24_r3_angolo.webp` | All'angolo sotto casa di Sara, sotto un lampione, si salutano; Darius le passa il sacchetto | Darius, Sara |

### Howard (il film)

| Fatto | File in `game/images/cg/ep2/` | Cosa mostra | Allega, in quest'ordine |
|---|---|---|---|
| 🔧 | `d24_o1_divano.webp` | Il divano di Howard nella luce blu di un vecchio televisore: Howard a un capo, Sara all'altro, un cuscino fra loro, una ciotola di patatine sul tavolino | `casa_howard.webp`, Howard, Sara |
| ✅ | `d24_o2_coperta.webp` | Howard si sposta lungo il divano con una coperta scozzese e le offre di dividerla | O1, Howard, Sara |
| ✅ | `d24_o3_braccio.webp` | Il braccio di Howard disteso sullo schienale dietro le spalle di Sara; lui guarda la TV, lei il film | O2, Howard, Sara |
| ✅ | `d24_o4_scivola.webp` | Verso la fine del film Howard accasciato su Sara come addormentato, la testa che scivola giù dalla spalla; Sara lo guarda con tenerezza | O3, Howard, Sara |
| 🔧 | `d24_o5_finge.webp` | **Primo piano, da far vedere bene:** Howard finge di dormire con la guancia sul seno di Sara, un sorriso beato ben visibile, un occhio appena aperto; Sara sopra di lui guarda il film, ignara | O4, Howard, Sara |
| ✅ | `d24_o6_saluto.webp` | Howard sulla porta accompagna Sara sul pianerottolo, la coperta scozzese sulle spalle come un mantello | `pianerottolo.webp`, Howard, Sara |
