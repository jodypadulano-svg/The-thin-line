# Giorno 19 · venerdì — «Same Bar, Friday»

**Scheda autonoma, 24 novembre 2026. Bozza da rivedere con Jody: nessun codice scritto.**
Trama ed effetti sono quelli approvati nel [registro](../decisioni.md); dialoghi e battute sono bozze. I punti segnati **(P)** sono proposte mie.

Legenda: `s` Sara · `sp` pensiero di Sara · `ch` Joanie · `n` narratore · `rs` retroscena · `je` Jessica · `ro` Roberta · `ba` Barbara · **▸** scelta.

## 0. Quadro della giornata

| Fascia | Scena | Condizione |
|---|---|---|
| Mattina | A. Il libro di Jessica | sempre |
| Mattina | B. Il ciondolo di Roberta e il terrazzino | sempre |
| Fine mattina | C. Barbara, missione 2 | `sara_stagista`, Barbara ≥ 20, Corr ≥ 10, missione 2 non completata, sorteggio 20% |
| Pomeriggio | D1. Shopping con Samantha | `ep2_d14_shopping_samantha` |
| Pomeriggio | D2. Caffè con Samantha | altrimenti |
| Sera | E. Da Joanie | sempre |
| Sera | F. The Lantern: Daniel a metà, poi Jacob | sempre (Daniel solo con `ep2_d18_pranzo_daniel`) |
| Notte | G. Casa | sempre |

**Età:** Sara e Joanie 27, Jacob 31, Magnus 71. Ogni ricordo con Jacob riguarda una Sara dai 19 ai 23 anni.

---

## A. Il libro di Jessica

*The newsroom — Friday, 9:20 a.m. Musica `redazione`.* **CG A1:** Jessica in piedi accanto alla scrivania di Sara con un romanzo consumato.

> n: Jessica is holding a thick old book against her chest with both hands, like something she's been told to hand in.
> je: This one fell behind the drawer. When I did the box. I only found it yesterday.
> n: *Middlemarch.* The spine has been taped twice.
> s: You said we'd do this one next. After Karenina.
> je: I did, didn't I? Well. You do it. You can tell me who's right.

**CG A2:** le pagine, i margini pieni di matita.

> n: The margins are full of pencil. Tiny, quick, arguing with everybody. A little after the middle the notes stop. The last one has a date beside it. Three months ago. Jessica's second week here.
> n: After that the pages are clean, all the way to the end.

**▸ «Read the last note.»** → Conf +1, nota nel Diario, flag `ep2_d19_appunto_jessica`

> n: {i}She keeps waiting for someone to tell her what she wants.{/i}
> sp: That's a good note. That's a really good note, Jess.
> je: What does it say? I can't read my own writing any more.
> s: It says you were paying attention.
> n: Jessica laughs and tucks her hair behind her ear. She doesn't ask to see it.

*Diario, «Cosa sa Sara» (capa):* «The notes in Jessica's book stop in her second week here, halfway down a page.»

**▸ «Give it back.»** → nessun effetto, flag `ep2_d19_libro_restituito`

> s: Keep it, Jess. You'll want to finish it.
> n: Jessica opens it where the notes stop and reads half a line. Her lips move. She frowns, the way she used to frown at people who were wrong.
> je: ...She should have just asked him.
> s: That's what I said. You told me I'd missed the point.
> n: For a moment Jessica looks as if she's about to tell her again. Then someone laughs across the room, and she closes the book.
> je: Okay. I'll keep it. For a bit.

---

## B. Il ciondolo di Roberta e il terrazzino

*The newsroom kitchen — 10:40 a.m.* **CG B1:** Roberta di profilo, un ciondolo aperto nel palmo, la foto fuori vista.

> n: Roberta is by the window with her back to the door. Her little gold heart is open in her palm. Sara didn't know it opened.
> n: It shuts with a click.
> ro: Sara! You're early. You're never in before quarter to. Sit, sit. I'll do yours the way you like.

**▸ «Who's in there?»** → Barbara +1, flag `ep2_d19_chiesto_ciondolo`

> s: Who's in there?
> ro: Somebody who's good to me.
> n: She says it to the kettle, very softly, and her ears go pink.
> s: Lucky you.
> ro: Yes. That's what I always think. Lucky me.

**▸ «Don't ask.»** → nessun effetto numerico, nota nel Diario

> n: Sara gets two cups down and talks about the biscuits. Roberta watches her for a moment.
> ro: You didn't ask.
> s: It looked private.
> ro: It is. Thank you. People usually do.
> n: She puts in the sugar Sara likes without being told.
> ro: Before here I used to eat lunch in my car. Every day. I had a radio. I knew the names of all the presenters and I thought that was knowing people.
> s: That sounds lonely.
> ro: I didn't know it was. That's the funny thing. You don't, until somebody opens the door.

*Diario, «Cosa sa Sara» (capa):* «Roberta was very lonely before the newspaper. “Until somebody opens the door.”»

### Il terrazzino

**CG B2:** Jessica e Roberta affiancate, stessa posa, stesso modo di fumare; Sara accanto a loro.

> n: On the little terrace Jessica and Roberta lean on the rail with the traffic below them. They lift their cigarettes at almost the same time. They breathe out slowly, at almost the same time.

*Nessuno lo commenta, Sara non ci pensa (decisione 17/11).*

- **`sara_fuma`:**
> n: Jessica holds out the packet without looking. Sara takes one. Nobody remarks on it any more.
- **altrimenti:**
> n: Sara stands upwind with her coffee and lets them talk.
- **`sara_stagista`, in più:**
> ro: You'll love Fridays, now. She's always a little softer on Fridays.
> sp: Now?

---

## C. Barbara — missione 2 (solo se estratta)

*Barbara's office — 12:10 p.m.* **CG C1:** Barbara in poltrona, gli occhi chiusi, la collana in mano.

> n: The message on her screen is four words long. {i}My office, please. Now.{/i}
> sp: I signed it. When she calls, I go. That's what I signed.
> n: Barbara is in the armchair instead of behind the desk. She has taken off her necklace and is holding it in her lap as if it weighed something.
> ba: Close the door. I've been on the telephone to idiots since eight.
> ba: My shoulders, Sara. Ten minutes.

**▸ «Go and stand behind her.»** → missione 2 completata (1/20). Nessun premio numerico.

**CG C2:** Sara dietro la poltrona, le mani sulle spalle di Barbara.

> n: Sara hangs her jacket on the door and goes round the chair. Under the silk Barbara's shoulders are as hard as the desk.
> ba: You've got strong hands for a girl who types.
> s: I knead bread. When I'm stuck on a chapter.
> ba: What's the chapter doing?
> s: She's about to lie to someone who loves her. I can't decide if she enjoys it.
> n: Under her thumbs something gives way. Barbara lets out a breath Sara feels all the way up her arms.
> ba: Of course you can. You're only deciding whether to write it down.

**CG C3:** Barbara che le tiene la mano sulla spalla.

> n: When the ten minutes are up, Barbara reaches back without turning and takes Sara's hand where it is. She keeps it there. Five seconds. Ten.
> ba: Good girl. Go and have your lunch.
> sp: She said it like a full stop. Why am I still smiling in the corridor?

**▸ «I'd rather not, today.»** → nessun effetto, la missione resta estraibile

> s: I'd rather not, today.
> n: It comes out quite steady. Barbara opens one eye.
> ba: Then sit down and keep me company. You can do that, I hope.
> s: I can do that.
> n: They sit. Barbara asks about the piece Sara is working on, and listens to the answer. After ten minutes she puts her necklace back on.

---

## D1. Shopping con Samantha (`ep2_d14_shopping_samantha`)

*The boutique — 5:15 p.m.* **CG D1:** la boutique del giorno 13, Samantha nella poltrona di velluto.

> n: It's the same boutique. The same cream curtain. Samantha sits in the velvet armchair with her coat still on and a cup of something nobody else has been offered.
> samantha: You see? Twenty minutes, and not one person has asked if I need help.
> s: Do you ever buy anything?
> samantha: Every few years. They keep hoping.

**CG D2:** Sara allo specchio con un abito blu notte, Samantha dietro di lei, i due volti vicini.

> n: Samantha does up the last hook and looks at them both in the mirror, over Sara's shoulder.
> n: The same eyes. The same wave in the hair. For a second Sara has the odd feeling of looking at a photograph that hasn't been taken yet.

*Una commessa passa.*

> n: "Your daughter has your smile," says the girl with the pins.
> samantha: She's not mine. I'd have kept her better stocked in dresses.

**Se `ep2_d15_litigio_josh`:**
> samantha: You're quiet today. Is it my son?
> s: We had a fight. It's mostly over.
> samantha: Mostly is the long part. He sulks like his grandfather. Wait, and then don't wait too long.

**Magnus, di sbieco:**

> samantha: What's it for, the dress?
> s: I'm meeting a publisher tomorrow. He's reading my first fifty pages. Magnus Larssen.
> n: Samantha's hand stops on the fabric. It's only a moment. Then she smooths the seam, as if that had been what she was doing.
> samantha: Then not that one. Too much zip.
> n: She crosses to the rail and comes back with something plain and grey-green that Sara wouldn't have looked at twice.
> samantha: Wear something you can forget you're wearing. He'll be listening.
> sp: How does she know he's a listener? Publishers, probably. They'd have to be.

**▸ «The one Samantha chose.»** → Magnus +1, Conf +1, flag `ep2_d19_abito_samantha`

> n: In the mirror there's nothing to fix. No strap, no hem. Just Sara, looking as if she'd come to say something.
> samantha: There you are.

**▸ «The one I'd have picked.»** → Conf +2, flag `ep2_d19_abito_suo`

> s: I think I'm going to wear the blue. It's the one I'd have picked on my own.
> samantha: Good. Then he'll be meeting you.
> n: She means it. She also takes one last look at the grey-green before she hangs it up again.

*L'abito torna sabato 20.*

## D2. Il caffè con Samantha (rifiuto al 14)

*The café opposite the newsroom — 5:15 p.m. (`caffe_di_fronte.webp`).* **CG D3:** Samantha al tavolino, due tazze.

> n: "I did say coffee," says a voice behind her, and it's Samantha, with her scarf half tied and two hours to kill.
> s: You did. I'm sorry about the shopping.
> samantha: Don't be. I shop like other people go to church.

**Se `ep2_d15_litigio_josh`:** stessa battuta su Josh di D1.

> s: I've got a big day tomorrow. A publisher's read my pages. Magnus Larssen.
> n: Samantha's spoon goes round once more than it needs to.
> samantha: Then don't dress up for him. Wear something you can forget you're wearing. He'll be listening.

**▸ «How do you know he listens?»** → nota nel Diario

> samantha: Oh. The good ones always are. The others just wait for you to breathe.
> n: She smiles at the window, not at Sara.

*Diario, «Cosa sa Sara» (editore):* «Samantha is sure Magnus listens. She didn't really say why.»

**▸ «Thank her and let it go.»** → nessun effetto

> s: That's good advice.
> samantha: I've got a drawerful. I never took any of it.

---

## E. Da Joanie

*Joanie's flat — 8:15 p.m. Musica `casa` (o nuova, **P**).* **CG E1:** Joanie sul divano con le gambe sotto di sé, due calici, vestiti sulla spalliera; Sara arriva.

> n: At home [nome_compagno] has a cardboard shield drying on the kitchen table, for Sunday. He barely looked up when she said she was going to Joanie's.
> ch: Wine, or the other wine?
> n: Sara takes the glass. The last time she was close to Joanie there was a mirror between them. She hasn't said anything about Wednesday. She doesn't know how to start.

### E1. Il gancio

**Se `ep2_d15_litigio_josh`:**
> s: He read my book, Jo. He just sat down and read it. And then he asked me why she was engaged.
> ch: He *asked* you?
> s: Like I'd left it in his coat pocket. We had a proper fight. I sent him to bed.
> ch: Good.

**Se ha lasciato correre:**
> s: It's nothing, really. He read a bit of the book. While I was out. It was open.
> ch: It was open.
> s: He was tired. He'd had a long week.
> ch: You've just given me three reasons and I didn't ask for one. Say it again without them.
> s: ...He read my book without asking.
> ch: There she is.

### E2. La prima mossa: Josh più grande

> ch: You know why he didn't ask? Because he already knew he wouldn't like the answer.
> s: That's not fair.
> ch: It's not. He's a sweetheart. He's a sweetheart who went through your pockets.

### E3. La seconda mossa: il nome lo fa Sara

**CG E2:** Joanie guarda nel bicchiere, finta distratta; Sara si volta verso di lei.

> n: Joanie turns the stem of her glass.
> ch: You know who never once looked in your notebook?
> ch: ...Forget it. I didn't say anything.
> s: Who?
> ch: No, no. Drink.
> s: ...Jacob.
> ch: You said it. Not me.
> n: It's strange to hear it in her own voice. She hasn't said it in this room in years.

### E4. La terza mossa: solo dettagli

**CG E3:** Sara che racconta, le guance rosse, ride; Joanie col mento sul ginocchio.

> ch: What was the thing with the car? When you were, what, twenty? You came back sunburnt on one side.
> s: He drove us to the coast and we got lost. Seven hours. For a two-hour drive.
> ch: And you were furious.
> s: I was... no. I was on the bonnet of the car eating cherries. He'd bought a whole crate off a man at the roundabout.
> ch: What did you have on?
> s: Why does that matter? His shirt. My feet on the windscreen.
> ch: I can see it. Where was he?
> s: Looking at me. He had the map upside down and he was just looking at me.
> n: Every question Joanie asks is a small one. Every answer comes back warmer than the one before.

### E5. La quarta mossa: disinnescare il tradimento

> s: He cheated on me, Jo. For ages. I used to lie there listening for his phone.
> ch: He did. He was twenty-six and an idiot.
> ch: I'm not saying he was good *for* you. I'm saying you were loud, Sara. You'd come into a room and I'd know before I saw you. I miss loud.
> n: Sara opens her mouth to say something sensible. What's in there is the taste of cherries.

### E6. **▸ Prima scelta**

> sp: I know how it ended. I do know.

**▸ «Let yourself be carried off.»** → Jacob +1, Corr +1, flag `ep2_d19_ricordo`

> n: She lets her head fall back on the sofa and closes her eyes. The bonnet's warm. The shirt's too big. Somebody's laughing, and it's her.
> s: I was loud, wasn't I?
> ch: You were deafening.

**▸ «You're leaving out how it ended.»** → Conf +1

> s: You're leaving out how it ended.
> n: Joanie laughs, a real one, and lifts both hands.
> ch: Guilty. I always skip the last chapter.
> n: She's right, Sara thinks, and she's said so. But the cherries don't go anywhere.

### E7. **▸ Seconda scelta**

**CG E4:** Joanie le prende le mani, seria, vicinissima.

> n: Joanie puts her glass on the floor and takes both of Sara's hands.
> ch: Can I be your friend for a minute? Not the funny one. Let me tell you what I see. You just listen.

**▸ «Let Joanie guide you.»** → vai a E8 se `ep2_d19_ricordo`, altrimenti E7b
**▸ «Keep your own head.»** → E7c

**E7b — Guida senza il ricordo** → Joanie +1

> s: Go on, then. One minute.
> ch: You've stopped asking for things. You used to want so much it was exhausting. I just want you to want something again. Anything. I don't care what.
> s: ...That's actually a nice thing to say.
> ch: I know. I'm horrified. Get your coat.

**E7c — Razionale** → Conf +1

> s: I love you. And I've been listening to you since I was nineteen, and I know what it sounds like when you're driving.
> n: Joanie's eyebrows go up. Then she kisses Sara on the forehead, hard, with a noise.
> ch: Fine. You drive. I'll get the coats.

### E8. I box a ripetizione → Joanie +3, Jacob +2, Corr +2

*Ogni passo: Joanie parla, poi un menu con **una sola voce**, la frase da ripetere. Primissimi piani sempre più stretti; la musica si abbassa.*

**CG E5:** i due volti vicini, la luce di una sola lampada.

> ch: I'm going to say something, and if it's true, you say it back. That's all. If it isn't true, don't.
> s: This is silly.
> ch: Extremely. Ready?

1. ch: Josh read my book without asking. → **▸ «Josh read my book without asking.»**
   > n: Easy. It's only what happened.
2. ch: Jacob never needed to ask. → **▸ «Jacob never needed to ask.»**
   > n: She laughs saying it. Joanie doesn't laugh. She waits.
3. ch: I was loud with him. → **▸ «I was loud with him.»**
   > n: This one comes out quieter than the others.
4. ch: I miss being loud. → **▸ «I miss being loud.»**
   > n: Her eyes have started to sting, and she has no idea why. Joanie's thumbs move over her knuckles. Slowly. Like winding something.
   > ch: You're doing so well.

**CG E6:** Sara, gli occhi lucidi, il sorriso che le sfugge.

5. ch: Nobody's made me feel like that since. → **▸ «Nobody's made me feel like that since.»**
   > sp: That isn't... Josh makes me feel... 
   > sp: No. Not *that*.
6. ch: I still want him. → **▸ «I still want him.»**

> n: It's out. She hears it sitting there in the room, in her own voice, perfectly clear. And something she's been holding up with both arms for four years simply comes down.
> n: She laughs. She's crying, and she's laughing, and she covers her face with her hands.
> s: Oh God. Jo.
> ch: I know.
> s: Sometimes I touch myself thinking about him.
> n: Silence. She looks through her fingers.
> s: Not often. Sometimes. When he's asleep. And then I lie there and I feel so... *awake*.
> n: Joanie's smile arrives slowly, and it's enormous.
> ch: Told you.

**CG E7:** le due abbracciate sul divano, ridono.

> n: What comes after isn't shame. Sara waits for it and it doesn't come. She feels light. She feels about a stone lighter.
> ch: So. Tell me everything. I've waited four years for this conversation.
> s: He was just so... *there*. He'd come through a door and the door looked smaller.
> ch: Go on.
> s: He could pick me up with one arm. He did it once in a supermarket. With the basket in the other hand.
> ch: And in bed?
> s: Jo!
> ch: You've come this far.
> n: Sara pulls a cushion onto her lap and says it into the top of it.
> s: With Josh it's sweet. It's really sweet, and I love him. With Jacob I used to forget what day it was.
> ch: Better?
> s: So much better. There's no... it's not even the same sport. And there was a lot more of him. Everywhere.
> n: They look at each other. Then they're both gone, howling, Joanie sliding off the sofa with her wine held up out of harm's way.

**Se Interest Joanie > 8 → E9. Altrimenti → E10.**

### E9. La confidenza

**CG E8:** Joanie seduta per terra, le ginocchia strette, per la prima volta insicura.

> n: When it passes, Joanie stays where she is, on the floor, with her back against the sofa. She isn't laughing any more. She's picking at the hem of her sock.
> ch: Can I tell you one? A real one.
> s: Of course.
> ch: No, wait. It's strange. It's really strange, Sara. It's about you, sort of. And if I say it and you look at me differently, I don't know what I'd do.
> ch: So you can say no. Honestly. If you're not ready, I'd rather keep you than tell you.

**▸ «Some things are better left unsaid.»** → nessun effetto

> s: I don't want to lose you. Some things are better left unsaid. Aren't they?
> n: Joanie breathes out. She looks relieved, and only a little bit sad.
> ch: Yeah. I think so too. Keep me, then.
> s: Always.

**▸ «Whatever it is, I won't judge you.»** **(acceleratore=True: ambra, !!!, avviso)** → Joanie +3, Corr +1, flag **`sara_bad_girl`**

> s: Whatever it is, I won't judge you. I just told you the worst thing I've got.
> n: Joanie opens her mouth, and shuts it. Her chin goes. Joanie, who has never been shy in her life, can't look at her.
> ch: I think about you. In bed. With somebody else.
> ch: Not with me. I mean I'm not... I'm just there. I'm watching. And you're with some man who isn't Josh, and you're so happy, and you look at me, and you're not sorry at all.
> ch: It's the thing. You know. The thing I think about. It's been the thing for years.

**CG E9:** Joanie in lacrime, il viso nascosto.

> n: She's crying properly now, and half laughing, wiping her face with her sleeve.
> ch: Say something. Please. Say I'm disgusting.
> n: Sara gets down off the sofa, onto the carpet, and puts both arms round her.

**CG E10:** l'abbraccio sul tappeto.

> s: Thank you for telling me.
> ch: ...What?
> s: Thank you. You carried that round on your own all this time, you idiot. You could have told me.
> n: Joanie makes a sound into her shoulder that isn't a word. They stay there until the wine's warm.
> sp: I ought to be shocked. I keep looking for it. All I can think is that she's never trusted anyone this much.
> sp: And that she said I looked happy.
> n: They have been friends for years. They have never been friends like this.

*Diario, «Cosa sa Sara» (amica):* «Joanie's secret: she fantasises about me with another man. She thought I'd hate her for it.»

#### E9b. Mercoledì (solo `sara_bad_girl`)

> n: They're still on the carpet. Sara has her cheek on Joanie's hair, and Wednesday is right there on the tip of her tongue.
> sp: The mirror. I could tell her. Or I could let her have tonight.

**▸ «I saw you with Simon.»** → nessun effetto numerico, flag `ep2_d19_sa_di_simon`, nota nel Diario

> s: Can I give you one back? So we're even.
> s: I saw you. On Wednesday. You and Simon.
> n: Joanie lifts her head. She wipes under one eye with a knuckle. She doesn't blush. If anything she seems to settle, the way she does when a conversation gets to the part she's good at.

- **Se `ep2_d17_ha_guardato_joanie_simon`:**
> ch: How much of it?
> s: ...I stayed. For a bit.
> ch: Good for you.
- **altrimenti:**
> ch: How much of it?
> s: Enough.
> ch: You could have said hello.

> s: Jo. What about Mark?
> ch: I love Mark. That's the first thing, and it's not the excuse, it's just true. I'd walk into the sea for him.
> ch: But I tried being the girl who only wants one person. Two years. I was so good. And I got mean, Sara. I picked at him. The way he chews. I hated him for things he hadn't done, because I was so busy not doing mine.
> ch: Then one day I stopped fighting it. And I came home and I wanted to cook for him. I wanted to hear about his boring day. He said, what's got into you, you're lovely lately.
> s: Lovely because you'd...
> ch: Lovely because I was whole. Nobody took anything from him. He got more of me, not less.
> s: He doesn't know, though.
> ch: No. And I carry that so he doesn't have to. If he ever asks me, straight out, I'll tell him. He's never asked. I don't think he wants to.
> n: Sara looks for the hole in it. There must be one. Joanie's holding her hand and telling her the truth, and it sounds so much kinder than everything she's always believed.
> sp: He got more of me, not less.
> ch: You're the only person I've ever said that to.

*Diario, «Cosa sa Sara» (amica):* «Joanie cheats on Mark. She says it makes her kinder to him. I couldn't find the hole in it.»

**▸ «Let her have tonight.»** → nessun effetto

> n: Not now. Not on top of this. She kisses Joanie's hair instead, and lets Wednesday go back where it was.
> sp: Another day. It's hers to tell, anyway.

### E10. Retroscena: il messaggio

**CG E11:** la mano di Joanie sul telefono; dietro, la luce della porta del bagno.

> rs: Sara is in the bathroom, fixing her eyes. Water running.

- **Dopo E8:** rs: {i}She's smiling. Give it an hour. Make her laugh.{/i}
- **Altri rami:** rs: {i}She's on her guard. Give it an hour. Make her laugh.{/i}
- **Con `sara_bad_girl`:** rs: Joanie's thumb waits over the button. Her eyes are still wet. Then she presses it.

> rs: The answer comes before the tap has stopped. {i}On my way.{/i}

*Diario, «Cosa sai tu» (amica, ex):* «Joanie arranged the meeting at The Lantern. She told Jacob to make Sara laugh.»

> ch: Coat! We're going out.
> s: Out where?
> ch: The Lantern. Same as always. One drink.

---

## F. The Lantern

*The Lantern — 10:20 p.m. Musica e ambiente `locale`.* **CG F1:** Sara e Joanie al bancone, The Lantern affollato.

> n: The Lantern on a Friday is the Lantern on a Saturday with its tie off. They find the end of the bar, under the last lamp, where it's nearly possible to hear.

### F1. Daniel, a metà (solo `ep2_d18_pranzo_daniel`)

> s: I didn't tell you about yesterday. I had lunch with Daniel.
> ch: Daniel *Daniel*?
> s: A private room. We talked about the book. He's... he's not what I thought.
> ch: What did you think?
> s: That he was an arrogant—

- **Se `ep2_d18_ballo`:** s: And then he asked me to dance, Jo. In the middle of lunch. And I—
- **altrimenti:** s: And then, when the bill came, he—

> n: She never gets to the verb.

*Senza pranzo:* Joanie sta parlando del cameriere quando si interrompe.

### F2. Jacob

**CG F2:** Jacob (testa rasata, pizzetto senza baffi, anello) di fianco a loro, Sara che si volta; niente volto nitido fino a qui.

> jacob: You still hold a glass with both hands.
> n: She knows before she turns. Her shoulders know.

**CG F3:** primo piano di Jacob.

> n: Four years. He's broader. His head's shaved now, and the beard's down to a bit of chin. He's wearing the same ring. He's looking at her as if she were the punchline of a very good joke somebody had finally remembered.
> s: ...Jacob.
> jacob: Sara.
> ch: Well! What are the *odds*.

*`incontra("ex")`, `tappa("ex", 1)`, flag `jacob_tornato`.*

**▸ «Stay cold.»** → nessun effetto

> s: Hello, Jacob. It's been a while.
> jacob: Four years. You've been counting too, or is it just me?
> s: It's just you.
> n: He takes it well. He takes it exactly as if he'd been handed something.

**▸ «Laugh at an old memory.»** → Jacob +3, Corr +1

> jacob: Eleven coffees.
> n: And that's it. She's gone. One small café, one waiter, her terrible holiday Spanish, and a tray that kept on coming.
> s: I asked for *one*. With milk!
> jacob: You drank four. So he wouldn't be offended.
> n: She's laughing with her whole face. She can hear it over the music. Loud.
> sp: Oh. There it is.

**▸ (solo `sara_bad_girl`) «Flirt with him. For Joanie.»** → Joanie +2, Jacob +1, Corr +1, flag `ep2_d19_bad_girl_usata`

**CG F4:** Sara con la mano sul petto di Jacob, lo sguardo oltre la sua spalla verso Joanie.

> n: She puts her hand flat on the front of his shirt, as if to check he's real.
> s: You got bigger. I didn't think there was room.
> n: She says it to him. She isn't looking at him. Along the bar Joanie's glass has stopped halfway to her mouth.
> n: Sara holds her eyes, and smiles, and leaves her hand where it is one second longer.
> sp: This one's for you, Jo.
> n: Jacob, who thinks it's for him, looks delighted.

### F3. Il drink

> jacob: Let me get you one. For old times' sake. Or for new ones, I'm not fussy.

**▸ «No, thanks.»** → nessun effetto

> s: I've got one. Thanks.
> jacob: You have. Both hands.

**▸ «All right. One.»** → Jacob +1, Corr +1

> n: He doesn't ask what she drinks. He orders it. It's right.
> s: So what do you do now?
> jacob: I run a place. Near the station.
> s: What sort of place?
> jacob: The sort where nobody minds if I take Friday off.

*Se rifiuta il drink, «I run a place» la dice a Joanie, con Sara che ascolta.* Lo strip club si scopre in chat.

### F3b. Il tradimento, Josh, un ballo (25/11, solo senza `sara_bad_girl`)

Testo definitivo nel codice, `ep2_d19_parlano`. **▸ «You cheated on me.»** → Conf +1 / «Let it lie.» · **▸ «So who's at home?»**: rispondere subito → Josh +1 / un secondo di troppo · **▸ un ballo**, solo se ha riso: «One song.» → Jacob +1, Corr +1 / «Not tonight.»

### F4. Il numero

**CG F5:** Jacob appoggia il telefono sbloccato sul bancone, davanti a Sara.

> n: When he's leaving he puts his phone on the bar in front of her, unlocked, and looks away at the bottles. He doesn't ask. He never did.

**▸ «Give him the number.»** → Jacob +2, `da_numero("ex")`, flag `ep2_d19_numero_dato`

> n: Her thumbs know where to go. She doesn't put a surname.

**▸ «Push the phone back.»** → nessun effetto; retroscena

> s: Goodnight, Jacob.
> jacob: Goodnight, Sara.
> rs: On the pavement, a minute later, his phone lights up. Joanie. A number, and nothing else.

### F5. Dopo

> ch: So.
> s: Don't.
> ch: I didn't say anything.
> s: You're *humming*.

---

## G. Casa

*Home — 12:50 a.m. Musica `notte`.* **CG G1:** Josh addormentato sul divano, lo scudo di cartone in grembo; Sara sulla porta con le scarpe in mano.

> n: [nome_compagno] has fallen asleep on the sofa with the shield on his chest. It says something in an alphabet he made up himself.
> n: She takes the paintbrush out of his hand, and puts a blanket over him, and the shield somewhere safe.
> sp: I do love you. I do.
> sp: I'll tell him about Jacob. There's nothing to tell.

- **Dopo E8:** n: In bed she lies on her back with the window open. Wide awake.
- **Se ha riso al ricordo:** n: Eleven coffees. She has to put her hand over her mouth.
- **altrimenti:** n: She wonders, just before she sleeps, how he knew what she drinks. Then she remembers. → *solo se ha accettato il drink*

---

## H. Riepilogo effetti (tutti approvati, salvo **P**)

| Scena | Scelta | Effetti |
|---|---|---|
| A | leggere l'appunto / ridare il libro | Conf +1 / — |
| B | chiedere del ciondolo / non chiedere | Barbara +1 / — |
| C | massaggio / rifiuto | missione 2 / — |
| D1 | abito di Samantha / il proprio | Magnus +1, Conf +1 / Conf +2 |
| D2 | chiedere / lasciar cadere | Diario / — |
| E6 | ricordo / «how it ended» | Jacob +1, Corr +1 / Conf +1 |
| E7 | guida (dopo il ricordo) / guida / razionale | Joanie +3, Jacob +2, Corr +2 / Joanie +1 / Conf +1 |
| E9 | non detto / non giudicare | — / Joanie +3, Corr +1, `sara_bad_girl` |
| E9b | dirle di Simon / tacere (solo `sara_bad_girl`) | flag `ep2_d19_sa_di_simon` / — |
| F2 | freddezza / risata / bad girl | — / Jacob +3, Corr +1 / Joanie +2, Jacob +1, Corr +1 |
| F3 | no / drink | — / Jacob +1, Corr +1 |
| F4 | numero / no | Jacob +2 / — |

**Massimi della giornata:** Jacob +9, Corr +6 (le tre risposte di F2 si escludono), Joanie +8 con la via bad girl.

## I. Continuità controllata

- **Giorno 10:** Sara ha già visto i margini di *Anna Karenina*, pieni fino alla fine, e quel libro andava in beneficenza. Perciò il libro del 19 è **un altro**, *Middlemarch*, caduto dietro il cassetto.
- **Giorno 17:** Sara ha visto Joanie con Simon e non ne ha parlato. Lo pensa all'inizio della sera e può dirlo solo in E9b.
- **Giorno 16:** le pesche sono il gesto d'amore di Sara per Josh; nel ricordo di Jacob sono ciliegie.
- **Chat di Jacob:** la gita persa è citata anche in `ex_a2`; «Eleven coffees» è nuovo e non si ripete. L'ostello e il lago restano alle chat.
- **Montaggio del 13:** «Same bar. Friday. I'll bring her.» torna con The Lantern; il teaser ora dice «a bar across town».
- **Domenica 21:** lo scudo di cartone prepara la convention; il discorso su Daniel resta aperto.

## L. Immagini

Circa **27 CG** (A 2, B 2, C 3, D 3, E 11, F 5, G 1). Prompt da scrivere in `inquadrature-giorno-19.md` quando la scheda è approvata. Riusi: `boutique`, `caffe_di_fronte`, `redazione`, `ufficio_barbara`, `locale`. Serve un riferimento nuovo per **casa di Joanie**.

## M. Da decidere con Jody

1. ~~Joanie e Simon (giorno 17)~~ **Deciso (Jody, 24/11):** dopo la confessione Sara sceglie se dirglielo; se lo fa, Joanie non si scompone e le spiega le sue ragioni in modo convincente (E9b).
2. ~~Jacob, ritmo~~ **Deciso (Jody, 24/11):** effetti invariati, soglie del telefono di Jacob a 5, 12, 18, 25.
3. ~~Dirlo a Josh~~ **Deciso (Jody, 24/11):** domenica 21 sera. Nel 19 resta solo un pensiero (G).
4. ~~Il teaser del 13~~ **Deciso e applicato (Jody, 24/11):** «in a bar across town».
