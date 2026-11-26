# Faccende di Howard — CG in tenuta classica

Decisioni: [pianificazione 22–24](../narrative/giorni22-24-pianificazione-2026-11-26.md), «Produzione grafica»: CG almeno fino alla sesta faccenda, in tenuta classica. Codice: `game/percorsi/howard_faccende.rpy` (lista `HOWARD_FACCENDE`). Il gioco cerca `game/images/cg/ep2/howard_faccenda_NN_classica.webp`; se manca, mostra la casa di Howard generica.

**6 CG (01–06): tutte fatte (26/11).** Le varianti con le tenute successive (sexy, seminuda) si fanno solo quando diventano raggiungibili, partendo da queste e cambiando solo l'abito.

## Come si lavora

Come per i giorni: un'immagine alla volta, **riferimenti scritti dentro il blocco del prompt e allegati alla risposta**; controllo; ✅ qui sotto. Mai «adult» né «mature face» nei prompt. Formato 16:9, `.webp`.

## Frase da mettere prima di ogni prompt

> Soft watercolor and visible graphite pencil on textured paper, matching the supplied character and location references. Immersive illustrated visual novel scene, wide 16:9 landscape composition, natural anatomy and hands, quiet lower edge for dialogue. No readable text, watermarks, logos or UI.

## Fissi

| Chi / cosa | Riferimento | Frase fissa |
|---|---|---|
| Sara | `riferimenti/attori/sara_acquerello_riferimento_v2_capelli_mossi.webp` | Sara, 27, softly wavy dark chestnut-brown hair to the shoulders, mostly brown with only subtle copper highlights, definitely not red, not auburn, not curly, freckles, brown eyes, slim, bust exactly as large as in the reference |
| Howard | `riferimenti/attori/howard_acquerello_candidato.webp` | Howard, 64, exactly as in the reference, heavy-set, round glasses, beige cardigan over a checked shirt, brown corduroy trousers, a cup of tea, watching contentedly from his chair |
| Divisa classica | `game/images/cg/ep2/howard_faccenda_01_classica.webp` | knee-length black maid dress with a white Peter Pan collar and white cuffs, white apron, white frilled cap, black tights, black shoes, exactly as in the 01 reference |
| Casa di Howard | `riferimenti/luoghi/casa_howard.webp` | cluttered old-fashioned flat, floral wallpaper, stacks of newspapers, warm lamplight, after work (late afternoon / early evening) |

Tono: quotidiano e un po' buffo, Sara concentrata e serena nel lavoro, Howard che si gode la vista dalla poltrona. Niente pose esplicite: la tenuta classica è coperta.

## CG

| Fatto | File in `game/images/cg/ep2/` | Faccenda (testo del gioco) | Cosa mostra |
|---|---|---|---|
| ✅ | `howard_faccenda_01_classica.webp` | Pavimento della cucina | già fatta |
| ✅ | `howard_faccenda_02_classica.webp` | «The oven needs a good scrub.» | Sara accovacciata davanti al forno aperto, guanti di gomma gialli, strofina la griglia unta; Howard col tè sulla sedia dietro di lei |
| ✅ | `howard_faccenda_03_classica.webp` | «Give the rug a good beating out on the balcony.» | Sul piccolo balcone di Howard, Sara ha steso il tappeto sulla ringhiera e lo batte con un battipanni di vimini, nuvolette di polvere; Howard la guarda dalla portafinestra aperta |
| ✅ | `howard_faccenda_04_classica.webp` | «Scrub the grease off the cupboards.» | Sara in punta di piedi su uno sgabello, braccia alzate, strofina la cima appiccicosa dei pensili; Howard seduto al tavolo di cucina, guarda in su |
| ✅ | `howard_faccenda_05_classica.webp` | «Wash the windows, inside and out where you can reach.» | Sara alla finestra del soggiorno con spruzzino e panno, poi in ginocchio ad asciugare il davanzale; Howard nella poltrona col giornale abbassato |
| ✅ | `howard_faccenda_06_classica.webp` | «Move those boxes into the pantry.» | Sara porta uno scatolone pieno stretto al petto attraverso la cucina verso la dispensa aperta, altri scatoloni impilati; Howard indica col dito dove metterli |
