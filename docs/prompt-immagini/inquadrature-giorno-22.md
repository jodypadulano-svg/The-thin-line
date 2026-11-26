# Inquadrature del giorno 22 — «Four Lines»

Decisioni: [registro](../decisioni.md), «Giorno 22». Codice: `game/episodio2/ep2_giorno22.rpy`.
**16 CG, 0 luoghi nuovi, 1 attrice nuova (Dawn, ritratto e figura intera fatti), 16 fatte.** Redazione, lungofiume e casa di Sara e Josh. Per ogni immagine c'è cosa mostra e quali riferimenti allegare; il prompt in inglese si scrive al momento, uno alla volta.

## Come si lavora (vale per qualunque assistente)

1. **Una immagine alla volta.** Si dà il prompt in inglese con l'elenco dei riferimenti **in ordine, scritto dentro il blocco del prompt** e **i file allegati alla risposta**, così Jody non deve cercarli (regola di Jody, 26/11); Jody la genera e la manda; si controlla; poi si passa alla successiva.
2. **Mai proporre di tagliare CG.**
3. **Ogni volta dire la percentuale:** CG fatte sul totale del giorno e dell'episodio.
4. **Controllare ogni immagine e dire sempre cosa non torna**, con la correzione già pronta: continuità, abiti, mani, capelli, seno troppo grande **o** troppo piccolo, volti adulti, storia.
5. **Riferimenti:** allegare sempre il riferimento approvato, mai una Sara recente.
6. Formato 16:9, almeno 1344×768, salvata `.webp` in `game/images/cg/ep2/` col nome esatto della tabella.
7. Non modificare il codice e non fare commit: se ne occupa Claude. Il file finito si segna ✅ qui sotto.

## Frase da mettere prima di ogni prompt

**Regola di Jody (26/11):** nei prompt non scrivere mai «adult» né «mature face»: Mage genera volti di 40-45 anni. L'età si dà solo col numero.

> Soft watercolor and visible graphite pencil on textured paper, matching the supplied character and location references. Immersive illustrated visual novel scene, wide 16:9 landscape composition, natural anatomy and hands, quiet lower edge for dialogue. No readable text, watermarks, logos or UI.

## Personaggi e riferimenti

| Chi | Riferimento (`riferimenti/attori/`) | Frase fissa |
|---|---|---|
| Sara | `sara_acquerello_riferimento_v2_capelli_mossi.webp` | Sara, 27, softly wavy dark chestnut-brown hair to the shoulders, mostly brown with only subtle copper highlights, **definitely not red, not auburn, not curly** (Mage tende a farli rossi: se escono rossi, inpaint solo dei capelli), freckles, brown eyes, slim, bust exactly as large as in the reference |
| Barbara | `barbara_acquerello_candidato.webp` | Barbara, 63, exactly as in the reference, bright dyed red hair, bold makeup, reading glasses, composed and amused |
| Josh | `josh_acquerello_candidato.webp` | Josh, 25, exactly as in the reference, gentle face |
| Dawn | `dawn_acquerello_riferimento.webp` (scelto da Jody il 26/11), poi `dawn_figura_intera.webp` per le CG a figura intera (prompt in [attori](attori.md#dawn--dawn)) | Dawn, 28, exactly as in the reference: very curly dark brown hair in a loose high ponytail with curls around her face, warm olive skin, tired brown eyes, a small mole on her left cheek, small silver teardrop drop earrings, no freckles, short nails painted pale shell pink |

Joanie non compare (c'è solo il suo messaggio, non leggibile). Se servisse: senza lentiggini. Daniel non compare: esiste solo nel racconto di Josh.

## Luoghi (già esistenti, `riferimenti/luoghi/`)

- Redazione: `redazione.webp` · Ufficio di Barbara: `ufficio_barbara.webp`.
- Lungofiume: `fiume.webp`. Aggiungere nel prompt una rimessa per barche in legno sullo sfondo e una fila di panchine; mezzogiorno coperto, luce grigia e morbida.
- Casa: `casa_soggiorno_sera.webp`, `casa_cucina.webp`, `casa_camera_mattina.webp` (di sera, con la lampada).
- **La porta di casa di Sara e Josh** è quella di legno sul pianerottolo (`pianerottolo.webp`). Oggi non c'è nessuna CG della porta. Se se ne aggiunge una, va usata quella.

## Abiti

- **Sara, al lavoro:** camicetta bianca abbottonata fino in cima sotto un cardigan color avena **abbottonato**, jeans scuri, stivaletti marroni. **Al fiume:** in più un trench beige chiuso con la cintura; sotto, jeans scuri e stivaletti marroni (da B1, approvata da Jody il 26/11: valgono per tutto il giorno, al posto di gonna e ballerine). **La sera:** cardigan tolto, camicetta con il primo bottone aperto, calzini.
- **Barbara:** come da scheda: capelli rosso acceso tinti, trucco marcato, camicetta leopardata, collana lunga d'oro, occhiali da lettura.
- **Dawn:** la giacca scura col cappuccio e la sciarpa a fiori del riferimento; cappuccio alzato sui ricci e occhiali da sole (in B3 «Nadia» sollevati sulla testa), jeans, scarpe da ginnastica; un bicchiere di carta da asporto.
- **Josh:** cappotto da lavoro grigio, camicia azzurra con la cravatta allentata. La scheda del personaggio (due fogli stampati, testo non leggibile, un piccolo disegno di nano) compare in C4 e C5.

## CG

| Fatto | File in `game/images/cg/ep2/` | Cosa mostra | Allega, in quest'ordine |
|---|---|---|---|
| ✅ | `d22_a1_barbara_scrivania.webp` | Barbara si ferma accanto alla scrivania di Sara con un caffè e la guarda dall'alto, sopra gli occhiali; Sara seduta, nel cardigan abbottonato, alza gli occhi. Mattina | `redazione.webp`, Barbara, Sara |
| ✅ | `d22_a2_lettera.webp` | Barbara seduta sull'angolo della scrivania fa scivolare con due dita una lettera scritta a mano verso Sara; accanto, la busta strappata in cima. Testo non leggibile | `ufficio_barbara.webp`, Barbara, Sara |
| ✅ | `d22_a3_retro.webp` | Primo piano delle mani di Sara che tengono il retro della lettera: una riga di stampatello in fondo (non leggibile), la scrivania sfocata dietro | A2 |
| ✅ | `d22_b1_panchina.webp` | Il lungofiume a mezzogiorno: una rimessa per barche, una fila di panchine; Sara sola sulla terza, nel trench chiuso, si guarda intorno; un uomo lontano dà il pane alle anatre | `fiume.webp`, Sara |
| ✅ | `d22_b2_dawn_arriva.webp` | Dawn, col cappuccio e gli occhiali da sole, si siede all'altro capo della panchina senza guardare Sara, il bicchiere di carta fra le mani; Sara rigida, guarda dritto | B1, Dawn, Sara |
| ✅ | `d22_b3_nadia.webp` | **Ramo empatico.** Dawn girata un po' verso Sara, occhiali da sole sollevati sulla testa, mostra le proprie unghie rosa mentre parla; Sara ascolta col panino dimenticato in grembo | B2, Dawn, Sara |
| ✅ | `d22_b3_fatti.webp` | **Ramo dei fatti.** Dawn sempre rivolta verso l'acqua, parla piano e in fretta; Sara con un taccuino sul ginocchio, la penna ferma | B2, Dawn, Sara |
| ✅ | `d22_b4_scontrino.webp` | Primo piano: la mano di Dawn (unghie rosa) passa a Sara, sotto il sedile della panchina, uno scontrino stropicciato con mezza targa scritta a penna (non leggibile) | B2 |
| ✅ | `d22_b5_sola.webp` | La panchina vuota tranne Sara; il bicchiere di carta lasciato accanto a lei; lontano, sul sentiero fra gli alberi, il cappuccio di Dawn che si allontana | B1, Sara |
| ✅ | `d22_c1_josh_divano.webp` | Josh seduto sul bordo del divano col cappotto ancora addosso, la borsa fra i piedi, fissa la TV spenta; Sara sulla soglia della cucina. Sera | `casa_soggiorno_sera.webp`, Josh, Sara |
| ✅ | `d22_c2_racconto.webp` | Sara accanto a Josh, il cappotto di lui mezzo tolto; Josh racconta guardandosi le mani | C1 |
| ✅ | `d22_c3_complimento.webp` | Josh col viso fra le mani; la mano di Sara sulla sua schiena, lei guarda oltre, nel vuoto, pensierosa, con un'ombra di calore sul viso che non sa nascondere | C2 |
| ✅ | `d22_c4_consola.webp` | **Ramo «consolarlo».** Sara stringe la testa di Josh sulla propria spalla, lui le cinge la vita; la scheda del nano accartocciata sul pavimento | C2, Sara, Josh |
| ✅ | `d22_c4_irritata.webp` | **Ramo «irritarsi».** Sara in piedi davanti al divano a braccia conserte, lo guarda dall'alto; Josh alza gli occhi, ferito; la scheda sul pavimento | C2, Sara, Josh |
| ✅ | `d22_c5_mark.webp` | Più tardi: Josh al tavolo di cucina scrive un messaggio sul telefono, il viso più calmo; la scheda del nano lisciata accanto al piatto. Sara appena visibile al lavello | `casa_cucina.webp`, Josh, Sara |
| ✅ | `d22_d1_letto.webp` | La camera alla luce della lampada: Josh addormentato su un fianco, che stringe il bordo del piumone; Sara seduta contro la testiera col telefono, pensierosa | `casa_camera_mattina.webp`, Sara, Josh |
