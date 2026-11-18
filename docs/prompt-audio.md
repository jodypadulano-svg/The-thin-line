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

---

## Ambienti in loop (`game/audio/ambienti/`)

| File | Prompt |
|---|---|
| `redazione` | *Busy open-plan newspaper office ambience: many keyboards typing, distant muffled conversations, a phone ringing far away, papers shuffling, a printer working. No clear words. Seamless loop, 45 seconds.* |
| `ristorante` | *Elegant restaurant ambience: soft murmur of many conversations, cutlery on porcelain plates, glasses touching, a waiter's quiet steps, a cork popping far away. No clear words. Seamless loop, 45 seconds.* |
| `bar` | *Cosy cocktail bar ambience: a small group of women laughing and chatting, ice in shaker, glasses clinking, a bartender working, soft background murmur. No clear words. Seamless loop, 45 seconds.* |
| `pioggia_auto` | *Inside a small car at night in the rain: steady rain drumming on the roof and windshield, windshield wipers swishing slowly, low engine hum, tires on a wet road. Seamless loop, 45 seconds.* |
| `palestra` | *Gym weight room ambience: weights clanking on racks, a treadmill running, people breathing and exercising, muffled upbeat music far away, a dumbbell set down on rubber floor. No clear words. Seamless loop, 45 seconds.* |

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
| `accendino` | G4, il fumo fuori dal bar | *A lighter flicked twice outdoors at night, the second time it catches, a soft first inhale.* |
