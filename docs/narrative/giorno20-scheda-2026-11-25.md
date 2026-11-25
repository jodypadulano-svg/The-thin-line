# Giorno 20 · sabato — «Page Fifty»

**Scheda autonoma, 25 novembre 2026. Approvata da Jody punto per punto; codice scritto il 25/11 (`ep2_giorno20.rpy`, test `giorno20`).**
Struttura, scelte ed effetti sono approvati. Dialoghi e battute sono bozze da rifinire nel codice.

Legenda: `s` Sara · `sp` pensiero di Sara · `c` Josh · `ed` Magnus · `si` Simon · `ch` Joanie · `n` narratore · `rs` retroscena · **▸** scelta.

## 0. Quadro della giornata

| Fascia | Scena | Condizione |
|---|---|---|
| Mattina | A. A casa, il vestito | sempre |
| Mattina | B. La casa editrice di Magnus | sempre (le pagine partono in entrambi i rami del 15) |
| Mezzogiorno | C. Per strada, il messaggio | sempre (chi scrive dipende dal 18) |
| Pomeriggio | D1. Palestra con Simon · D2. Da Joanie · D3. A casa a scrivere | scelta attiva |
| Sera | E. Cena fuori con Josh | sempre |
| Notte | F. Il telefono | sempre |

**Agganci letti:** `ep2_d19_abito_samantha` (grigioverde) / tutti gli altri (blu) · `ep1_d13_magnus_pagine` · `ep2_d15_litigio_josh` · `ep2_d18_pranzo_daniel` · `ep2_d19_numero_dato` · `sara_bad_girl` · `ep2_d19_sa_di_simon` · `ep2_d17_ha_guardato_joanie_simon`.

**Regole che valgono qui:** Sara non ha ancora detto a Josh di aver rivisto Jacob (la scelta è del 21). Il segreto di Samantha con Magnus non si rivela. Magnus non seduce: ascolta. Il primo messaggio spontaneo di Jacob resta del 21.

---

## A. Il vestito

*Home — Saturday, 8:40 a.m. Musica `casa`.* **CG A1:** Sara allo specchio dell'ingresso, il vestito scelto; alle sue spalle Josh con lo scudo di cartone e il pennello.

- **`ep2_d19_abito_samantha`:**
> n: The grey-green dress has no zip and no opinion. Twice she forgets she's wearing it, and looks down to check.
- **`ep2_d19_abito_suo`:**
> n: The blue is the one she'd have picked. She's picked it. It still surprises her, in the mirror, to be the person who did.
- **altrimenti (caffè): il blu che ha già nell'armadio.**
> n: «Wear something you can forget you're wearing.» She's had four things on. The one she's kept is the blue, from the back of the wardrobe, that she'd been saving for something without knowing what.

> c: Wow. Okay. Is it bad luck to say you look like an author?
> s: It's only a chat. He might have hated it.
> c: He asked you in on a Saturday. People don't come in on a Saturday to hate something.

*Se `ep2_d15_litigio_josh`:*
> n: He doesn't ask about the pages. He's been not asking since Monday, carefully, like a man carrying a full glass.

**▸ «Wish me luck.»** → Josh +1
> c: Luck. All of it. I'll make do without, I've got a shield.
> n: He kisses her on the cheek so as not to spoil her mouth, and gets green paint on her ear.

**▸ «I'll tell you about it tonight.»** → nessun effetto
> c: Tonight. I booked the place with the candles in bottles. I even ironed something.

**CG A2:** il bacio sulla guancia, la macchia verde all'orecchio.

---

## B. La casa editrice

*The publishing house — 10:00 a.m. Musica `magnus`.* **Luogo nuovo L1.** **CG B1:** un palazzo alto e stretto, una targa di ottone, Sara sulla soglia.

> n: It isn't what she expected. No glass, no lobby. A tall thin house with a brass plate so often polished that the name's nearly gone.

La donna con la bob d'argento le apre. **CG B2.**

> n: She knows the woman who opens the door. The silver bob. The smile at the end of the party.
> n: «You were standing beside a door,» she says. «I'm glad to see you've come through one.»

Le scale strette, libri dappertutto. **CG B3:** Sara sale, i dorsi fino al soffitto.

### Magnus

**CG B4:** la stanza in alto, finestra, due poltrone, nessuna scrivania; le cinquanta pagine stampate su un tavolino, una girata a faccia in giù.

> ed: Sara. Sit wherever you would like to be listened to.

**Il vestito:**
- **`ep2_d19_abito_samantha`:**
> n: He gets up to greet her, and for a moment he simply doesn't. He's looking at the dress. Then he is himself again, and holds out his hand.
> sp: Is there paint on it?
- **`ep2_d19_abito_suo`:** «Blue. I am always glad when a writer dresses herself.»
- **altrimenti (il blu suo, dal caffè):** «Blue. Good. You have come dressed to sit down.»

> ed: I have read them. Twice. Once for you, once for me. I shall not tell you today whether they are good.
> s: ...Oh.
> ed: If I told you yes, you would stop listening. If I told you no, you would stop breathing. And I have a question that requires both.

*Il responso arriva martedì 23, come da calendario.*

> ed: Your heroine is standing where she can see two men. One is laughing behind the glass. The other has just been told where to meet her tomorrow. And there you leave her.
> n: He turns over the last page, the one that was lying on its face. He's written nothing on it at all.
> ed: Which of them is it about?
> sp: Nobody's ever asked me that. I've never asked me that.

*Se `ep1_d13_magnus_pagine`, in più:*
> ed: You told me she did not want to be found. Not yet. I believe you. But somebody on page fifty has started leaving the lights on.

**CG B5:** primo piano di Magnus, la pagina cinquanta fra due dita.

**▸ «Listen to him.»** → **Magnus +3, Conf +2**
> n: She doesn't answer. It's the hardest thing she's done in that chair. She lets him go on.
> ed: It is about neither. It is about the glass. She has spent her life on one side of it, admiring the party. You have written forty-nine pages about a window and one about a hand on the latch.
> sp: A hand on the latch.
> n: Her eyes are stinging. He has the courtesy to look at the fire until they stop.

**▸ «How do I make it better?»** → **Magnus +2, Conf +3**
> s: How do I make it better?
> ed: Ah. She has come to work. Good.
> ed: Take out every sentence in which she explains herself. She is always apologising to the reader for wanting something. We did not ask.
> s: That's half the book.
> ed: It is a third. I counted. The other two thirds are alive.

**CG B6:** (Listen) Sara che si asciuga gli occhi, Magnus voltato al fuoco · (Better) Sara china sulle pagine con la matita, lui che indica una riga.

### La lettura

> ed: One thing more, and then I shall give you back your Saturday. The last paragraph. Aloud.

**▸ «Read it to him.»** → Conf +1
> n: Her voice is small for a line and a half. After that it's somebody else's, lower, quite sure of where the commas are.
> n: When she stops, the house is very quiet. Two floors down, somebody has stopped typing.

**▸ «Ask him to read it.»** → Magnus +1
> n: He reads it as if he'd found it in a drawer. He makes no face at all. She hears, for the first time, what the woman is about to do.
> sp: It's indecent. It's really indecent. I wrote that at the kitchen table.

**CG B7:** la voce nella stanza, la finestra, la città.

### Via

**CG B8:** la donna con la bob d'argento alla porta, la mano sul braccio di Sara.

> n: «He didn't say yes,» says the woman with the silver bob.
> s: He didn't say anything.
> n: «He gave you the chair by the window. He's had ministers in the other one.»

**Retroscena.** `rs`: rimasto solo, Magnus non rimette la pagina cinquanta con le altre. La mette in un cassetto dove c'è già una fotografia. *Se `ep2_d19_abito_samantha`:* nella fotografia si vede solo un orlo grigioverde. *Diario, «Cosa sai tu»:* «Magnus kept page fifty. There's a photograph in the same drawer.»

---

## C. Per strada

*The street — 11:50 a.m.* **CG C1:** Sara sui gradini, il telefono in mano, ride da sola.

- **`ep2_d18_pranzo_daniel`:** scrive Daniel.
> Daniel: Well?
> Sara: He asked me a question.
> Daniel: He's never asked me one.
  *Se Interest Daniel ≥ giorno, in più:* «Lunch, when you've got the answer.»
- **altrimenti:** scrive Joanie.
> Joanie: ALIVE??
> Sara: He didn't say yes.
> Joanie: did he say no
> Sara: No.
> Joanie: then WHY are we not screaming

*Chat di trama: non consuma la chat libera della sera.*

---

## D. Il pomeriggio

> sp: The whole afternoon. Nobody needs me till eight.

**▸ «The gym.»** · **▸ «Joanie's.»** · **▸ «Home. The book.»**

### D1. Palestra

*The gym — 3:00 p.m.* **CG D1a:** Simon da solo che sistema i dischi; la sala quasi vuota del sabato.

> si: Saturday? Who are you and what have you done with Sara?
> s: I've had a big morning. I need to lift something.

Allenamento vero, lui contento di lei. **Simon +2.**

*Se Sara sa di Joanie e Simon (`ep2_d19_sa_di_simon` oppure `ep2_d17_ha_guardato_joanie_simon`):*

> n: He's a fraction too careful with her. He's been like that since Wednesday, as if she were a glass somebody had told him about.

**▸ «I know about you and Joanie.»** → Conf +1, Simon +1
> si: ...Right. Okay. Do you think I'm a terrible person?
> s: I think you lost count on seven.
> n: He laughs so hard he has to put the plate down.

**▸ Say nothing.** → nessun effetto

**CG D1b:** la panca, lui dietro di lei, la mano a un centimetro dal bilanciere. **CG D1c:** la risata.

**▸ «Stay for a stretch.»** 🔒 Corr 12 → Simon +2, Corr +1 · **▸ «Shower. Dinner.»** → nessun effetto

### D2. Da Joanie

*Joanie's flat — 3:00 p.m.* **CG D2a:** Joanie in vestaglia, occhiali da sole, il caffè orribile; di ieri è rimasto tutto.

> ch: don't speak. sit. tell me everything. in that order.

Joanie vuole sapere tutto di Magnus, poi di Jacob. **Joanie +2.**

- **`sara_bad_girl`:** l'occhiolino della sera prima resta fra loro. Non un commento, solo l'occhio che si chiude quando Sara dice «he asked me which man».
- **altrimenti:** «So. Coffee man. Are we talking about him or are we not talking about him?»

**▸ «We're talking about him.»** → Jacob +1, Corr +1
**▸ «We're not talking about him.»** → Conf +1

**CG D2b:** le due sul letto, i piedi in alto contro il muro, il coniglio di umidità sul soffitto.

### D3. A casa, a scrivere

*Home — 3:00 p.m.* Josh è alla convention a montare il tavolo. **CG D3a:** Sara al tavolo, la pagina cinquantuno vuota.

> n: She takes out every sentence in which her heroine explains herself. It takes an hour. It's like opening windows.

**Conf +2.**

> n: Then page fifty-one is there, quite white, and the woman is still standing where she can see them both.

**▸ She goes to the one outside.** → Corr +1, flag `ep2_d20_romanzo_altro`
**▸ She goes back in to the one who's laughing.** → Josh +1, flag `ep2_d20_romanzo_fidanzato`
**▸ She goes home alone, and walks.** → Conf +1, flag `ep2_d20_romanzo_sola`

*La scelta torna il 23, quando Magnus dà il responso.* **CG D3b:** la luce che cambia, le pagine sul pavimento.

---

## E. La cena

*The candlelit place — 8:15 p.m. Musica `ristorante`. Luogo: `enoteca`.* **CG E1:** Josh in piedi, camicia stirata male, che le scosta la sedia.

> c: I asked for the table where nobody walks past.
> n: He's nervous. He's known her for years and he's nervous, and he's written something on his hand.
> s: What's that?
> c: Topics.

**CG E2:** la mano di Josh: «Magnus · shield · wed?».

> c: So. Topic one. Magnus.

Sara racconta. *Se ha letto lei ad alta voce:* gli dice della voce. *Se ha chiesto a Magnus di leggere:* non gli dice perché è arrossita.

> c: Topic three. Mark wants me for a thing on Wednesdays. Dungeons and Dragons. Dice and voices. I said probably not.
> s: Why probably not?
> c: You'd be on your own all evening.
> sp: All evening.

*Semina del mercoledì di Josh. Non dice sì: lo dirà dopo la sera di lunedì 22.*

### ★ La serata

**▸ «Be here, all the way.»** 🔒 Josh 30 → **Josh +4**
> n: She puts her hand over the list on his. For two hours she doesn't think of a single person who isn't at the table. It isn't even difficult. That's what surprises her.
> c: You're looking at me.
> s: I know. I'd forgotten what you do with your eyebrows.

**CG E3:** le mani, le candele, ridono tutti e due.

**▸ «Somewhere else.»** → **Josh −2, Corr +1**
> n: He's telling her how you age cardboard with tea. She watches his mouth. She's on the other side of a window, with her hand on a latch.
> c: Sara?
> s: Tea. Yes. Go on.

**CG E4:** Josh che parla, Sara che guarda il proprio riflesso nel vetro.

**▸ «Listen to him, smiling.»** → nessun effetto · *serve a chi ha Josh sotto 30 e non vuole la serata distratta.*
> n: She asks about the tea and the cardboard. She even remembers the answer. He tells the waiter it's a special occasion, and when the waiter asks which one he says «Saturday».

### Il telefono vibra

Vibra nella borsa. *Chi è:* Daniel se c'è stato il pranzo, altrimenti Joanie.

**▸ «Leave it in the bag.»** → nessun effetto
> n: It goes three times. Josh looks at the bag, then at her, then back at his pudding, and gets a bit taller.

**▸ «Look at it.»** → **Susp +2**
> n: It's only a second. It's a very long second, from the other side of the table.

**CG E5:** la luce del telefono sul viso di Sara · o la borsa chiusa, Josh che sorride.

### Il ritorno

A piedi. *Con la serata romantica:* lui le dà la giacca, e a casa si baciano sulle scale. Segue la scena E2.
*Altrimenti:* lui si addormenta subito, la sveglia già messa.

> c: Wish me luck for tomorrow. I'm judging the shields.

### E2. La camera — solo con «Be here, all the way»

*Home — 11:00 p.m. Musica `casa`, la lampada accesa.* Decisa da Jody il 25/11: scena intima, parte esplicita col [brief d20_josh](../nsfw/brief/d20_josh.md), segnaposto `scena_nsfw("d20_josh")`.

**CG E6:** i due sulla porta della camera, le scarpe in mano, che ridono piano.

> c: Lamp on or lamp off?
> s: On.
> c: You always say off.
> s: I know what I always say.

*Se `ep1_d7_josh_precoce`:*
> n: He goes still, sitting on the edge of the bed with one sock on, and she can see him remembering.
> c: I did promise I'd make it up to you.
> s: There's no hurry. There isn't anything anywhere. Breathe.
> n: She puts her hand flat on his chest until it does.

**CG E7:** seduti sul letto, la mano di lei sul petto di lui, la lampada fra loro.

*Qui la scena esplicita.*

**CG E8:** dopo, fronte contro fronte, le lenzuola per terra.

> n: The ink on his hand has come off on her shoulder. «Wed?», backwards.
> c: You've got my topics on you.
> s: I'll read them in the mirror.
> n: He laughs into her hair, and goes on laughing for a bit after he's asleep.
> sp: That was lovely. It really was.
> n: She lies quite still, warm to the fingertips, with everything exactly where it belongs.

---

## F. Notte

*Home — 11:00 p.m.* **CG F1:** Josh dorme, la camicia sulla sedia, Sara alla finestra col telefono.

Sessione libera **23:00-23:30**. Barbara non risponde (sabato). Simon risponde fino alle 23, Jacob sì.

> sp: Which of them is it about?
> n: She puts the light out. She leaves the lamp in the hall on. She doesn't know why.

---

## Effetti

| Punto | Scelta | Effetto |
|---|---|---|
| A | Wish me luck / Tonight | Josh +1 / — |
| B | Listen / Better | **Magnus +3, Conf +2 / Magnus +2, Conf +3** |
| B | Read it / Ask him | Conf +1 / Magnus +1 |
| D1 | Palestra · «I know» · stretch 🔒 Corr 12 | Simon +2 · Conf +1 e Simon +1 · Simon +2 e Corr +1 |
| D2 | Joanie · parlarne / no | Joanie +2 · Jacob +1 e Corr +1 / Conf +1 |
| D3 | Scrivere · l'altro / il fidanzato / da sola | Conf +2 · Corr +1 / Josh +1 / Conf +1 |
| E | Be here 🔒 Josh 30 / Somewhere else / Listen | **Josh +4 / Josh −2, Corr +1** / — |
| E | Leave it / Look at it | — / **Susp +2** |
| E2 | Solo con «Be here» | nessun effetto in più |

## CG

| Scena | CG |
|---|---|
| A | 2 |
| B | 9 (B6 in due versioni = 10; B9 è il retroscena del cassetto) |
| C | 1 |
| D1 | 3 |
| D2 | 2 |
| D3 | 2 |
| E | 5 (E5 in due versioni = 6) |
| E2, solo serata romantica | 3 |
| F | 1 |
| **Totale** | **30** |

**Due vestiti (Jody, 25/11):** grigioverde con `ep2_d19_abito_samantha`, blu notte per tutti gli altri (comprato il 19, oppure già nell'armadio dopo il caffè). A1, A2, B1, B3 e C1 esistono in due versioni: **5 in più, 35 CG in tutto**. Riferimenti: CG 07 (grigioverde) e 06 (blu) del giorno 19. Le altre CG di B si inquadrano dal busto in su, col cappotto o lo scialle.

**Luoghi:** L1 la casa editrice (scala e stanza in alto), nuovo. Gli altri ci sono: palestra, `casa_joanie`, casa, `enoteca`, strada.

## Decisioni (tutte prese)

1. ✅ **Il responso di Magnus:** resta al 23; il 20 dice solo di averle lette e lascia la domanda (Jody, 25/11).
2. ✅ **Samantha:** Sara non la cita con Magnus; resta solo l'abito che lo fa fermare (Jody, 25/11).
3. ✅ **Il pomeriggio:** effetti delle tre strade approvati; la pagina cinquantuno torna il 23, bianca per chi non ha scritto (Jody, 25/11).
4. ✅ **La cena:** terza scelta neutra, «Listen to him, smiling.», senza effetti (Jody, 25/11).
5. ✅ **Susp +2 se guarda il telefono a tavola:** si tiene. La dà il gesto davanti a Josh, non il messaggio (Jody, 25/11).
6. ✅ **Jacob il 21 (Jody, 25/11):** si adatta. Se non si sono mai scritti è il primo messaggio; se si sono già scritti è la prima volta che le chiede di vedersi; se Sara gli ha negato il numero, arriva da un numero sconosciuto (Joanie). In ogni caso è **l'invito** per il mercoledì 24. Prima del 21 Jacob non comincia mai per primo.
7. ✅ **Dopo la cena:** scena intima con la serata romantica, parte esplicita col brief `d20_josh` (Jody, 25/11).
8. ✅ **Due vestiti:** grigioverde (Samantha) e blu (tutti gli altri); 35 CG col retroscena del cassetto (Jody, 25/11).
9. ✅ **Le cinque proposte minori** approvate insieme: mattina con Josh, lettura ad alta voce, retroscena del cassetto, cena all'enoteca, telefono 23:00-23:30 (Jody, 25/11).
