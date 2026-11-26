# Inquadrature del giorno 20 — «Page Fifty»

Scheda della giornata: [giorno20-scheda](../narrative/giorno20-scheda-2026-11-25.md). Codice: `game/episodio2/ep2_giorno20.rpy`.
**35 CG e 1 luogo, 0 fatti.** Qui c'è cosa mostra ogni immagine e quali riferimenti allegare; il prompt in inglese si scrive al momento, uno per volta.

## Come si lavora (vale per qualunque assistente)

1. **Una immagine alla volta.** Si dà il prompt in inglese con l'elenco dei riferimenti **in ordine**; Jody la genera e la manda; si controlla; poi la successiva.
2. **Mai proporre di tagliare CG.**
3. **Ogni volta dire la percentuale:** CG fatte sul totale del giorno, luoghi, e l'episodio.
4. **Controllare ogni immagine e dire sempre cosa non torna**, con la correzione già pronta: continuità, abiti, mani, capelli, seno troppo grande **o** troppo piccolo, volti adulti, storia.
5. **Riferimenti:** allegare sempre il riferimento approvato, mai una Sara recente.
6. Formato 16:9, almeno 1344×768, salvata `.webp` in `game/images/cg/ep2/` col nome esatto della tabella.
7. Non modificare codice e non fare commit: lo fa Claude. Il file finito si segna ✅ qui sotto.

## Frase da mettere prima di ogni prompt

> Soft watercolor and visible graphite pencil on textured paper, matching the supplied adult character and location references. Immersive illustrated visual novel scene, wide 16:9 landscape composition, natural anatomy and hands, quiet lower edge for dialogue. No readable text, watermarks, logos or UI.

## Personaggi e riferimenti

| Chi | Riferimento (`riferimenti/attori/`) | Frase fissa |
|---|---|---|
| Sara | `sara_acquerello_riferimento_v2_capelli_mossi.webp` | adult Sara, 27, mature face, softly wavy chestnut-brown hair to the shoulders with subtle copper highlights, **not red and not curly**, freckles, brown eyes, slim, bust exactly as large as in the reference |
| Magnus | `magnus_acquerello_candidato.webp` più `game/images/cg/ep1/d13_08_magnus_elegante.webp` | adult Magnus, 71, silver hair swept back, face, glasses and beard exactly as in the reference, an impeccable dark three-piece suit |
| Donna con la bob d'argento | `game/images/cg/ep1/d13_m08_magnus_auto.webp` | an elegant adult woman in her sixties with a sleek silver bob (senza nome) |
| Josh | `josh_acquerello_candidato.webp` | adult Josh, exactly as in the reference, gentle face |
| Simon | `simon_acquerello_candidato.webp` | adult Simon, the gym trainer, exactly as in the reference |
| Joanie | `joanie_acquerello_riferimento.webp` | adult Joanie, 27, dark brown wavy hair with a full fringe, small gold hoops, no freckles |

Se un riferimento contraddice la frase (occhiali, barba), **vale il riferimento**.

## Abiti

- **I due vestiti di Sara** (mattina, casa editrice, strada): **verde** = grigioverde semplice, riferimento `game/images/cg/ep2/d19_07_abito_verde.webp`; **blu** = blu notte, riferimento `d19_06_specchio.webp` (Sara). Le cinque CG con `_verde` e `_blu` si fanno in due versioni identiche: prima la verde, poi la blu modificando **solo il vestito**.
- **Nella stanza di Magnus** (B4-B7): Sara dal busto in su, con il cappotto chiaro aperto o uno scialle, così il vestito non si vede.
- **Pomeriggio:** in palestra completo sportivo semplice; da Joanie jeans e maglione; a casa a scrivere maglietta larga e pantaloni morbidi, piedi nudi.
- **Cena:** Sara camicetta chiara semplice e gonna scura; Josh camicia azzurra stirata male, inchiostro sulla mano **sinistra**.
- **Notte:** Sara nella maglietta di Josh; Josh nella E6 e nella E7 ancora con la camicia.

## Luogo

| Fatto | File | Cosa mostra | Allega |
|---|---|---|---|
| ☐ | `riferimenti/luoghi/casa_editrice_stanza.webp` | **Da fare per primo.** Stanza in alto di una casa stretta e antica: due poltrone (una davanti al camino, una davanti a una grande finestra sulla città), un tavolino basso, **nessuna scrivania**, libri fino al soffitto, fuoco acceso, luce del mattino. Nessun personaggio | `game/images/cg/ep1/d13_08_magnus_elegante.webp` solo per lo stile |

## CG

| Fatto | File in `game/images/cg/ep2/` | Cosa mostra | Allega, in quest'ordine |
|---|---|---|---|
| ☐ | `d20_a1_specchio_verde.webp` | Sara allo specchio dell'ingresso; alle sue spalle Josh con lo scudo di cartone e il pennello, vernice verde sul mento | d19_07, Sara, Josh, `casa_soggiorno_sera.webp` |
| ☐ | `d20_a1_specchio_blu.webp` | la stessa, vestito blu | la verde, d19_06 |
| ☐ | `d20_a2_bacio_verde.webp` | Josh le bacia la guancia nell'ingresso; macchia di vernice verde sull'orecchio di lei | A1 verde, Sara, Josh |
| ☐ | `d20_a2_bacio_blu.webp` | la stessa, blu | la verde, d19_06 |
| ☐ | `d20_b1_portone_verde.webp` | Sara davanti a una casa alta e stretta con una targa di ottone consumata (senza scritta leggibile); mattina | A1 verde, Sara |
| ☐ | `d20_b1_portone_blu.webp` | la stessa, blu | la verde, d19_06 |
| ☐ | `d20_b2_bob_argento.webp` | la donna con la bob d'argento apre la porta e sorride come a un'amica | d13_m08, B1 verde |
| ☐ | `d20_b3_scale_verde.webp` | Sara sale una scala stretta, libri dappertutto, una tazza di tè dimenticata su un libro | B1 verde, Sara |
| ☐ | `d20_b3_scale_blu.webp` | la stessa, blu | la verde, d19_06 |
| ☐ | `d20_b4_magnus_stanza.webp` | la stanza; cinquanta pagine sul tavolino, l'ultima a faccia in giù; Magnus in piedi accanto al fuoco | luogo, Magnus, Sara |
| ☐ | `d20_b5_pagina_cinquanta.webp` | primo piano di Magnus con una pagina fra due dita, gli occhi su di lei | luogo, Magnus |
| ☐ | `d20_b6_ascolta.webp` | Sara nella poltrona della finestra si asciuga gli occhi; Magnus, per rispetto, guarda il fuoco | B4, Sara, Magnus |
| ☐ | `d20_b6_migliora.webp` | Sara china sulle pagine con la matita; Magnus indica una riga | B4, Sara, Magnus |
| ☐ | `d20_b7_lettura.webp` | la finestra alta sulla città, le pagine nella luce, silenzio; i due piccoli nelle poltrone | B4 |
| ☐ | `d20_b8_uscita.webp` | sulla soglia, la donna con la bob d'argento posa la mano sul braccio di Sara | B2, Sara |
| ☐ | `d20_b9_cassetto.webp` | retroscena: la mano di Magnus posa la pagina in un cassetto, accanto a una vecchia fotografia **di cui si vede solo un angolo** (un orlo grigioverde, nessun volto) | B5 |
| ✅ | `d20_b4_magnus_stanza_verde.webp` | **variante verde (Jody, 26/11):** come `d20_b4_magnus_stanza.webp`, cambiando solo il vestito di Sara nel grigioverde di Samantha | `d20_b4_magnus_stanza.webp`, A1 verde |
| ✅ | `d20_b6_ascolta_verde.webp` | **variante verde (Jody, 26/11):** come `d20_b6_ascolta.webp`, cambiando solo il vestito di Sara nel grigioverde di Samantha | `d20_b6_ascolta.webp`, A1 verde |
| ✅ | `d20_b6_migliora_verde.webp` | **variante verde (Jody, 26/11):** come `d20_b6_migliora.webp`, cambiando solo il vestito di Sara nel grigioverde di Samantha | `d20_b6_migliora.webp`, A1 verde |
| ✅ | `d20_b7_lettura_verde.webp` | **variante verde (Jody, 26/11):** come `d20_b7_lettura.webp`, cambiando solo il vestito di Sara nel grigioverde di Samantha | `d20_b7_lettura.webp`, A1 verde |
| ✅ | `d20_b8_uscita_verde.webp` | **variante verde (Jody, 26/11):** come `d20_b8_uscita.webp`, cambiando solo il vestito di Sara nel grigioverde di Samantha | `d20_b8_uscita.webp`, A1 verde |
| ☐ | `d20_c1_gradini_verde.webp` | Sara seduta sui gradini del portone, telefono in mano, ride da sola | B1 verde, Sara |
| ☐ | `d20_c1_gradini_blu.webp` | la stessa, blu | la verde, d19_06 |
| ☐ | `d20_d1a_simon_solo.webp` | palestra quasi vuota, Simon rimette i dischi sulla rastrelliera | `palestra_sala.webp`, Simon |
| ☐ | `d20_d1b_panca.webp` | Sara sulla panca, Simon dietro, le mani a un centimetro dal bilanciere senza toccarlo | D1a, Sara, Simon |
| ☐ | `d20_d1c_risata.webp` | Simon ride tanto da posare il disco; Sara ghigna sulla panca | D1b |
| ☐ | `d20_d2a_joanie_occhiali.webp` | Joanie in vestaglia e occhiali da sole, porge una tazza di caffè orribile | `casa_joanie.webp`, Joanie |
| ☐ | `d20_d2b_coniglio.webp` | Sara e Joanie sul letto coi piedi in alto contro il muro; sul soffitto una macchia di umidità a forma di coniglio | D2a, Sara, Joanie |
| ☐ | `d20_d3a_pagina_bianca.webp` | Sara al tavolo vicino alla finestra, il portatile con la pagina bianca | `casa_soggiorno_sera.webp`, Sara |
| ☐ | `d20_d3b_pagine_pavimento.webp` | luce arancione, pagine stampate sul pavimento, i piedi nudi di Sara | D3a, Sara |
| ☐ | `d20_e1_sedia.webp` | enoteca, tavolo d'angolo, candele nelle bottiglie; Josh in piedi le scosta la sedia | `enoteca.webp`, Sara, Josh |
| ☐ | `d20_e2_argomenti.webp` | primo piano della mano di Josh a lume di candela, tre scritte **sbavate e illeggibili** a inchiostro | E1, Josh |
| ☐ | `d20_e3_romantica.webp` | la mano di Sara su quella di Josh, ridono tutti e due | E1, Sara, Josh |
| ☐ | `d20_e4_distratta.webp` | Josh parla; Sara guarda il proprio riflesso nel vetro scuro | E1, Sara, Josh |
| ☐ | `d20_e5_borsa.webp` | la borsa chiusa sulla sedia accanto a Sara; Josh sorride al dolce | E1, Josh |
| ☐ | `d20_e5_schermo.webp` | la luce del telefono sul viso di Sara; Josh dall'altra parte la guarda | E1, Sara, Josh |
| ☐ | `d20_e6_porta.webp` | sulla porta della camera con le scarpe in mano, trattengono le risate | `casa_camera_mattina.webp`, Sara, Josh |
| ☐ | `d20_e7_mano.webp` | seduti sul letto alla luce della lampada, la mano di lei aperta sul petto di lui. Vestiti, tenera | E6, Sara, Josh |
| ☐ | `d20_e8_dopo.webp` | dopo: fronte contro fronte, il piumone per terra, sorridono; inquadratura sobria, coperti dal lenzuolo | E7, Sara, Josh |
| ☐ | `d20_f1_finestra.webp` | Josh dorme, la camicia sulla sedia; Sara alla finestra col telefono, luce della strada | E6, Sara, Josh |

Tutte le CG: **35**. Con `d20_e3_romantica` si vedono E6-E8 (serata romantica); le due B6 e le due E5 sono alternative.
