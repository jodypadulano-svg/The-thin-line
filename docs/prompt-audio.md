# The Thin Line — Prompt dell'audio (musiche ed effetti)

Bozza di lavoro | 17 novembre 2026 · Musica generata con **Mureka** (piano con uso commerciale).

## Come si usano

- **Musiche:** su Mureka modalità **Instrumental** (niente voce), durata 1:30-2:30. Incolla il prompt nella descrizione dello stile. Genera 2-3 versioni e tieni quella che **riparte meglio dall'inizio** quando finisce (suonano in loop).
- **Effetti:** brevi (1-5 secondi) tranne gli ambienti (30-60 secondi, in loop). Se Mureka non li fa bene, vanno bene anche librerie con licenza commerciale o CC0.
- **Formato:** `.ogg` o `.mp3` (anche `.wav` per gli effetti). Il nome del file deve essere esattamente quello della tabella.
- **Dove salvarli:** `game/audio/musica/`, `game/audio/ambienti/`, `game/audio/suoni/`. Se un file manca, il gioco va avanti in silenzio.
- **Regola fissa:** niente melodie riconoscibili o «nello stile di» artisti o giochi reali.

---

## Musiche (`game/audio/musica/`)

| File | Dove suona | Stato |
|---|---|---|
| `tema_principale` | Menu iniziale | ✅ |
| `casa` | Casa: mattina e sera con Josh | ✅ |
| `redazione` | Redazione | ✅ |
| `barbara` | Quando entra Barbara | ✅ |
| `stranezza` | Roberta e Jessica | ✅ |
| `notte` | Notte, telefonata di Joanie | ✅ |
| `palestra` | Palestra (giorno 2) | ✅ |
| `ristorante` | Ristorante elegante, cena aziendale (giorno 3) | ✅ |
| `daniel` | Tema di Daniel: punzecchiature e brindisi (giorno 3) | ✅ |
| `aperitivo` | Cocktail bar, aperitivo con le colleghe (giorno 4) | ✅ |
| `howard` | Tema di Howard: il pianerottolo e la sua casa (giorni 5, 6, 9) | ✅ |
| `enoteca` | Wine bar con Joanie (giorno 5) | ✅ |
| `locale` | Il locale «The Lantern» il sabato sera, con Simon (giorno 6) | ✅ |
| `daniel_villa` | La festa nella villa di Daniel: sexy, lussuosa (giorno 13) | ✅ |
| `daniel_seduzione` | Daniel e Sara soli: la terrazza e la cerniera (giorno 13). **Canzone con voce femminile** | ✅ |
| `daniel_notte` | Il messaggio di Daniel all'1:12, chiusura dell'Episodio 1 (giorno 13) | ✅ |
| `chiusura_ep1` | Il montaggio dopo i titoli: un ritratto per ogni strada (giorno 13). **Canzone con voce femminile** | ✅ |
| `darius_caffe` | Giorno 14, caffè con Darius. Entra quando Darius si ricorda della porta del romanzo di Sara. | ✅ |
| `magnus` | Giorno 20, la casa editrice: l'incontro con Magnus. | ✅ |
| `the_wink` | Giorno 19, finale forzato «The Wink»: mesi dopo e cartello finale. | ✅ |

**tema_principale**
```
Instrumental main theme for a romantic drama visual novel. Gentle solo piano melody, warm and tender, slowly joined by soft strings; underneath, a subtle low cello note and a slightly dissonant chord that returns every few bars, hinting that something is about to go wrong. Bittersweet, intimate, cinematic but small. Slow tempo, around 70 BPM. No vocals. Ends so it can loop seamlessly.
```

**casa**
```
Instrumental warm acoustic background music for everyday life of a happy young couple at home. Fingerpicked acoustic guitar, soft piano, light brushed percussion, a little glockenspiel. Cozy, tender, morning coffee and evening lamplight feeling, gently happy, unhurried. Medium-slow tempo, around 85 BPM. No vocals. Background music for dialogue, not too busy. Seamless loop.
```

**redazione**
```
Instrumental light comedic jazz-pop for a busy small-town newspaper office. Pizzicato strings, upright bass, light jazz drums with brushes, playful clarinet and muted trumpet phrases, typewriter-like rhythmic feel. Lively, slightly chaotic, witty, everyday workplace comedy. Medium tempo, around 110 BPM. No vocals. Background music for dialogue. Seamless loop.
```

**barbara**
```
Instrumental theatrical, flamboyant comedic theme for a larger-than-life, loud, glamorous female boss making an entrance. Bold brass section, swaggering big-band swing, tuba bass line, cheeky trombone slides, cabaret piano, a strutting walking rhythm. Over-the-top, self-confident, funny and a bit intimidating. Medium tempo, around 100 BPM. No vocals. Seamless loop.
```

**stranezza**
```
Instrumental sweet but subtly unsettling music: a music box and celesta playing a cute, innocent melody that is very slightly out of tune, soft pastel synth pads, a faint detuned toy piano, gentle ticking. Everything seems lovely, but something is quietly wrong. Slow tempo, around 75 BPM. No vocals. Not horror, just uncanny sweetness. Seamless loop.
```

**notte**
```
Instrumental soft late-night piano, intimate and warm, a bedside lamp in a quiet apartment, light rain-like reverb, a few sustained warm pad chords, a hint of playful lightness. Calm, tender, a little sleepy. Slow tempo, around 65 BPM. No vocals. Seamless loop.
```

**palestra**
```
Instrumental upbeat modern pop workout music for a bright neighborhood gym. Punchy electronic drums, groovy bass, bright synth stabs, motivating and fun, a little flirty, not aggressive. Feel-good energy. Tempo around 120 BPM. No vocals. Background music for dialogue, mixed not too loud. Seamless loop.
```

**ristorante**
```
Instrumental elegant restaurant background music: a soft jazz piano trio with brushed drums and warm upright bass, discreet and refined, candlelit fine dining, a touch of expensive glamour. Calm, polished, a little intimidating. Slow-medium tempo, around 80 BPM. No vocals. Background music for dialogue, quiet and unobtrusive. Seamless loop.
```

**daniel**
```
Instrumental theme for a charming, arrogant, seductive powerful man: smooth slow jazz with a sly walking upright bass, muted trumpet, low velvety saxophone, a few sharp piano chords, finger snaps. Confident, playful, a little predatory, elegant and dangerous. Slow tempo, around 75 BPM. No vocals. Background music for dialogue. Seamless loop.
```

**aperitivo**
```
Instrumental lounge music for a cosy, slightly glamorous cocktail bar at golden hour: warm Rhodes electric piano, soft bossa-nova guitar, light brushed percussion, a sensual muted trumpet now and then. Relaxed, chic, a little seductive, with an undercurrent of intrigue. Tempo around 90 BPM. No vocals. Background music for dialogue, quiet and unobtrusive. Seamless loop.
```

**howard**
```
Instrumental theme for an awkward, lonely, slightly off neighbour: a slow, gentle waltz on an old upright piano that is a little out of tune, a soft clarinet carrying a sweet, innocent melody, and underneath a faint music-box figure with one note that keeps landing in the wrong place. Tender, clumsy, a little sad, quietly unsettling. Tempo around 80 BPM. No vocals. Background music for dialogue. Seamless loop.
```

**enoteca**
```
Instrumental background music for a small, warm, crowded neighbourhood wine bar at night: easy acoustic guitar, upright bass, light brushed drums, a little accordion now and then. Friendly, intimate, a bit playful, like two best friends gossiping over red wine. Tempo around 95 BPM. No vocals. Quiet and unobtrusive under dialogue. Seamless loop.
```

**locale**
```
Instrumental upbeat dance-pop track for a busy city bar on a Saturday night, heard from inside the room: punchy four-on-the-floor kick, warm funky bass, bright synth chords, handclaps, a catchy plucked synth hook, a little disco guitar. Fun, warm, carefree, makes you want to dance badly with your friends. Tempo around 118 BPM. No vocals. Mixed slightly muffled, as if from the bar's speakers, so dialogue stays clear. Seamless loop.
```

**daniel_villa** (Jody, 21/11: musiche molto sexy quando c'è Daniel)
```
Instrumental sultry, luxurious lounge music for an exclusive private party in a hillside villa at night: deep, slow house groove with a soft four-on-the-floor kick, a warm round bassline, breathy analog synth pads, a smoky tenor saxophone phrase now and then, sparse Rhodes chords, a hint of shimmering percussion. Sensual, rich, confident, seductive, a little dangerous: the sound of money and desire. Tempo around 100 BPM. No vocals. Background music for dialogue, warm and not too loud. Seamless loop.
```

**Tempi di `daniel_seduzione` (Jody, 22/11):** primo ritornello 0:49 · seconda strofa 1:18 · secondo ritornello 2:00 · ponte 2:29 · fine 3:39. Servono per il videoclip della terrazza col corsetto (video A, B, C e la cerniera).

**daniel_seduzione** — **canzone con voce** (Jody, 21/11: una ragazza dalla voce sexy che canta; non solo musica di sottofondo). Su Mureka modalità **Song** (non Instrumental), con il testo qui sotto nel campo dei testi. Durata 2:30-3:00. Mixare la voce un po' indietro: sotto ci sono i dialoghi.

Stile:
```
Slow, sultry neo-soul and late-night R&B ballad sung by a young woman with a low, breathy, husky, intimate voice, sung close to the microphone almost like a whisper, smoky and teasing. Deep slow heartbeat-like kick, velvety electric bass, warm Rhodes electric piano, a breathy low saxophone answering the voice, soft swelling strings in the chorus. Seductive, slow-burning, desire held back, almost unbearable closeness. Around 68 BPM. Ends softly so it can loop.
```

Testo (originale, scritto per il gioco):
```
[Verse 1]
Cold air on the terrace, city lights below
You said don't move, and I didn't, no
Your voice so close I can feel it on my skin
One more inch, and I let you in

[Chorus]
Slow, slow, take it slow
Every little tooth of the zipper you close
I should walk away, I should let you go
But slow, slow... I don't want you to know

[Verse 2]
He's inside laughing, I can hear him through the glass
I'm a good girl, baby, but this won't pass
You don't even touch me, and I'm already gone
Tell me how you knew it all along

[Chorus]
Slow, slow, take it slow
Every little tooth of the zipper you close
I should walk away, I should let you go
But slow, slow... I don't want you to know

[Bridge]
Just a whisper, just a kiss
Right below my ear, like this
And I tilt my head, I don't say a word
Some yeses never need to be heard

[Outro]
Slow... slow...
I don't want you to know
```

**daniel_notte**
```
Instrumental dark, minimal, seductive late-night music for a forbidden message arriving at 1 a.m.: a slow pulsing low synth bass like a heartbeat, soft muted piano notes in a minor key, a distant breathy saxophone, cold glassy pads, long silences between phrases. Intimate, tense, tempting, a little guilty, a cliffhanger feeling that keeps rising and never resolves. Slow tempo, around 60 BPM. No vocals. Seamless loop.
```

**chiusura_ep1** — **canzone con voce** (Jody, 21/11: voce femminile sexy e malinconica, sul montaggio finale dell'Episodio 1). Su Mureka modalità **Song**, durata 2:00-2:30. Qui non ci sono dialoghi sotto (solo poche righe): la voce può stare in primo piano.

Stile:
```
Slow, melancholic and sensual trip-hop ballad sung by a young woman with a low, breathy, smoky, bittersweet voice, intimate and a little haunted. Slow brushed drums with a deep, lazy beat, a warm round bass, a lonely piano motif, vinyl crackle, soft swelling strings and a distant muted trumpet in the bridge. Night, rain on the window, a city full of lit windows, every one of them a different life. Seductive and sad at the same time. Around 72 BPM. Ends on a long fading note.
```

Testo (originale, scritto per il gioco):
```
[Verse 1]
Lights on in every window
Somebody's waiting up for me
A key I never gave away
A name I swore I'd never see

[Chorus]
One life, so many doors
And every one of them says yours
I close my eyes, I smile, I lie
Good girl tonight... and not for long

[Verse 2]
Someone's counting out the hours
Someone's keeping all my things
Someone's laughing in the dark
Like he already knows the ending

[Chorus]
One life, so many doors
And every one of them says yours
I close my eyes, I smile, I lie
Good girl tonight... and not for long

[Bridge]
Don't wake me, don't wake me
I'm still deciding who I am
Don't save me, don't save me
I'm not lost... I'm just beginning

[Outro]
One life...
So many doors...
```

---

## Ambienti in loop (`game/audio/ambienti/`)

| File | Prompt |
|---|---|
| `supermercato.mp3` | *Quiet neighbourhood supermarket on a Sunday afternoon, heard from the biscuit aisle. Low refrigeration hum, occasional soft footsteps and faint packaging rustle. No music, announcements or clear speech.* (G14, traccia inserita, 30 secondi) ✅ |
| `redazione` | *Busy open-plan newspaper office ambience: many keyboards typing, distant muffled conversations, a phone ringing far away, papers shuffling, a printer working. No clear words. Seamless loop, 45 seconds.* |
| `ristorante` | *Elegant restaurant ambience: soft murmur of many conversations, cutlery on porcelain plates, glasses touching, a waiter's quiet steps, a cork popping far away. No clear words. Seamless loop, 45 seconds.* |
| `bar` | *Cosy cocktail bar ambience: a small group of women laughing and chatting, ice in shaker, glasses clinking, a bartender working, soft background murmur. No clear words. Seamless loop, 45 seconds.* |
| `pioggia_auto` | *Inside a small car at night in the rain: steady rain drumming on the roof and windshield, windshield wipers swishing slowly, low engine hum, tires on a wet road. Seamless loop, 45 seconds.* |
| `ufficio` | *Quiet corporate open-plan office ambience: air conditioning hum, a few keyboards typing, a printer starting up far away, a phone ringing once in another room, muffled footsteps on carpet. No clear words. Seamless loop, 45 seconds.* |
| `enoteca` | *Small crowded wine bar ambience at night: lively murmur of friends talking and laughing, wine glasses clinking, a cork pulled, cutlery on small plates, soft acoustic music very far away. No clear words. Seamless loop, 45 seconds.* |
| `locale` | *Busy city bar on a Saturday night, without music: loud crowd murmur and laughter, people shouting their orders over the noise, glasses clinking, ice in a shaker, bottles opened, a cheer from a group of friends. No clear words, no music. Seamless loop, 45 seconds.* |
| `palestra` | *Gym weight room ambience: weights clanking on racks, a treadmill running, people breathing and exercising, muffled upbeat music far away, a dumbbell set down on rubber floor. No clear words. Seamless loop, 45 seconds.* |
| `fiume` | *Riverside park path on a sunny autumn afternoon: gentle flowing water, ducks quacking now and then, leaves rustling in a light breeze, distant children playing and a dog barking far away, footsteps on gravel. No clear words, no music. Seamless loop, 45 seconds.* |
| `tv_howard` | *An old television playing at low volume in a small, stuffy, closed living room: a muffled evening quiz show or news murmur, no clear words, faint canned laughter now and then, the hum of an old fridge, a clock ticking. Heard from across the room, dull and oppressive. No music. Seamless loop, 45 seconds.* (G9, casa di Howard) ✅ |

## Effetti (`game/audio/suoni/`)

| File | Dove | Prompt |
|---|---|---|
| `sveglia` | G1, inizio | *Smartphone alarm, gentle marimba ringtone, two short rings, in a quiet bedroom.* |
| `rasoio` | G1, bagno | *Electric razor buzzing behind a bathroom door, slightly muffled, 3 seconds.* |
| `porta_sbattuta` | G1, entra Barbara | *Glass office door swung open hard and banging against the wall, in a large office.* |
| `tazza` | G1, cappuccino di Roberta | *Ceramic coffee cup placed on a wooden desk next to a keyboard.* |
| `macchinetta_caffe` | G1, Jessica | *Office coffee machine grinding and pouring into a paper cup, 4 seconds.* |
| `chiave_serratura` | G1, Josh rientra | *Key turning in an apartment door lock, door opening, keys dropped in a bowl.* |
| `sobbollire` | G1, risotto | *Risotto gently simmering in a pot, wooden spoon stirring, 4 seconds.* |
| `telefono_vibra` | G1 notte, G2 alle 17 | *Smartphone vibrating twice on a wooden surface.* |
| `notifica` | G2, messaggio di Josh | *Soft, pleasant phone message notification chime, single short tone.* |
| `armadietto` | G2, spogliatoio | *Metal gym locker door opened and closed, in a tiled locker room.* |
| `rossetto` | G3, bagno con Emma | *Lipstick tube cap pulled off with a soft click, then closed again, in a quiet marble bathroom.* |
| `calici` | G3, il brindisi | *Several crystal champagne glasses clinking together in a toast at a dinner table, light applause.* |
| `portiera_auto` | G3, in auto | *Car door closing with a soft thud, seatbelt clicking, engine starting, in the rain.* |
| `chiavi_ciotola` | G5, Sara prende le chiavi dalla ciotola | *A bunch of house keys picked up from a ceramic bowl on a wooden cabinet, a short jingle, quiet hallway.* |
| `accendino` | G4, il fumo fuori dal bar | *A lighter flicked twice outdoors at night, the second time it catches, a soft first inhale.* |
| `citofono` | G7, arriva Darius | *Old apartment intercom buzzer pressed twice, then once more for a long time, heard from inside the flat.* |
