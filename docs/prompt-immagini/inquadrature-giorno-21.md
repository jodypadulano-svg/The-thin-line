# Inquadrature del giorno 21 — «Lowercase»

Decisioni: [registro](../decisioni.md), «Giorno 21». Codice: `game/episodio2/ep2_giorno21.rpy`.
**18 CG, 0 luoghi nuovi, 18 fatte.** Tutto si svolge a casa di Sara e Josh. Per ogni immagine c'è cosa mostra e quali riferimenti allegare; il prompt in inglese si scrive al momento, uno alla volta.

## Come si lavora (vale per qualunque assistente)

1. **Una immagine alla volta.** Si dà il prompt in inglese con l'elenco dei riferimenti **in ordine**; Jody la genera e la manda; si controlla; poi si passa alla successiva.
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
| Darius | `darius_acquerello_candidato.webp` | Darius, 25, exactly as in the reference, easy friendly face |
| Joanie | `joanie_acquerello_riferimento.webp` | Joanie, 27, dark brown wavy hair with a full fringe, small gold hoops, no freckles |
| Josh | `josh_acquerello_candidato.webp` | Josh, 25, exactly as in the reference, gentle face |

Jacob non compare: c'è solo il suo nome sullo schermo, che non deve essere leggibile.

## Luoghi (già esistenti, `riferimenti/luoghi/`)

- Cucina: `casa_cucina.webp` · Soggiorno: `casa_soggiorno_sera.webp` (anche di giorno, con luce diversa) · Camera: `casa_camera_mattina.webp` (di notte, al buio).
- Il bagno non ha un riferimento: è piccolo, con le piastrelle chiare e la vasca. Lo stile si prende da `casa_cucina.webp`.

## Abiti

- **Sara, tutto il giorno:** maglione morbido color crema e leggings, calzini. **Di notte:** la maglietta di Josh.
- **Darius:** giacca leggera aperta su una felpa, jeans.
- **Joanie:** occhiali da sole sulla testa, maglione oversize verde salvia, jeans; scarpe tolte nell'ingresso.
- **Josh, la sera:** i pantaloni buoni di ieri, camicia stropicciata, una **coccarda di carta** appuntata storta sul petto (la scritta non deve essere leggibile); lo scudo di cartone dipinto a mano sotto il braccio.

## CG

| Fatto | File in `game/images/cg/ep2/` | Cosa mostra | Allega, in quest'ordine |
|---|---|---|---|
| ✅ | `d21_a1_biglietto.webp` | Il tavolo di cucina nella luce del mattino: un biglietto di Josh appoggiato alla zuccheriera (scrittura non leggibile), la tazza di Sara, briciole. Nessun personaggio | `casa_cucina.webp` |
| ✅ | `d21_a2_darius_porta.webp` | Darius sul pianerottolo con un sacchetto di carta di cornetti unto agli angoli, una mano dietro la nuca: ha appena capito. Sara sulla porta, in calzini, sorride | Darius, Sara, A1 |
| ✅ | `d21_a3_darius_cucina.webp` | Sara e Darius al tavolo di cucina con caffè e cornetti; lei racconta gesticolando, lui ascolta divertito e raccoglie le briciole nel palmo. Clima da vecchi amici, nessuna tensione | A1, Sara, Darius |
| ✅ | `d21_a3_darius_scale.webp` | Darius a metà delle scale si gira a salutare con un cornetto in bocca; Sara ride sulla porta | A2, Darius, Sara |
| ✅ | `d21_b1_joanie_arriva.webp` | Joanie sulla soglia con gli occhiali da sole, una scatola di pasticcini e una bottiglia di vino; Sara in calzini la fa entrare | Joanie, Sara, A2 (per la porta) |
| ✅ | `d21_b2_divano.webp` | Sara e Joanie sul divano con le gambe raccolte e i pasticcini fra loro; Joanie mostra uno scontrino lungo con una lista scritta sul retro (non leggibile). Pomeriggio | `casa_soggiorno_sera.webp`, Sara, Joanie |
| ✅ | `d21_b3_jacob_racconta.webp` | Sara abbraccia un cuscino e racconta ridendo di sé; Joanie col mento sui pugni, rapita | B2, Sara, Joanie |
| ✅ | `d21_b4_daniel.webp` | Joanie si fa aria in modo teatrale con lo scontrino; Sara col viso nel cuscino che ride | B2, Sara, Joanie |
| ✅ | `d21_b5_telefono.webp` | Joanie tiene alto il telefono di Sara, fuori dalla sua portata, e scrive col pollice; Sara è stesa di traverso su di lei, allunga il braccio e ride. Allegria tra amiche, niente di erotico | B2, Joanie, Sara |
| ✅ | `d21_b6_inviato.webp` | Il telefono a faccia in su sul tavolino fra due pasticcini; le due lo fissano, Joanie con la mano sulla bocca | B5 |
| ✅ | `d21_b6_cancellato.webp` | Sara stringe il telefono al petto, trionfante e un po' senza fiato, un ginocchio nei pasticcini; Joanie fa il broncio al soffitto con i piedi in grembo a lei | B5 |
| ✅ | `d21_c1_josh_torna.webp` | Josh sulla porta, sfinito e raggiante, con lo scudo di cartone sotto il braccio e la coccarda di carta storta sul petto. Sera, luce calda dell'ingresso | Josh, `casa_soggiorno_sera.webp` |
| ✅ | `d21_c2_divano.webp` | Sara e Josh sul divano che mangiano noodles dai cartoni, i piedi di lui sul tavolino, le gambe di lei sopra le sue; TV accesa | C1, Sara, Josh |
| ✅ | `d21_c3_detto.webp` | Josh immobile con le bacchette a mezz'aria, lo sguardo altrove; la mano di Sara sul suo ginocchio | C2 |
| ✅ | `d21_c4_telefono.webp` | Il telefono illuminato sul cuscino fra loro (nome non leggibile); Josh mezzo addormentato sulla spalla di lei, il telecomando sul petto, la TV bassa | C2 |
| ✅ | `d21_c5_risponde.webp` | Sara scrive con lo schermo inclinato lontano da lui; Josh ora ha gli occhi aperti e guarda la luce sul viso di lei | C4 |
| ✅ | `d21_d1_bagno.webp` | Sara seduta sul bordo della vasca, nella maglietta di Josh, con il telefono in tutte e due le mani; porta chiusa a chiave, luce fredda | Sara, `casa_cucina.webp` (solo stile) |
| ✅ | `d21_d2_finestra.webp` | La camera al buio: Josh dorme con la coccarda sul petto; Sara alla finestra col telefono | `casa_camera_mattina.webp`, Sara, Josh, C1 (coccarda) |
