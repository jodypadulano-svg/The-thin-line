# The Thin Line — Revisione dei discorsi al telefono

Generato da `tools/esporta_chat.py` dai file `game/percorsi/chat_*.rpy`. Non modificare a mano: si rigenera. Testi in inglese (come il gioco); le note in corsivo sono effetti e flag.


## Simon

### simon_intro · Introduzione

*Se scrive Sara:*

> **Sara:** Hi, it's Sara. From the gym. You said I could text you about the exercises... is that still ok?  

**Pezzo 1**

> **Simon:** Of course! Joanie's friend. The shoulder, right?  
> **Simon:** How's it feeling?  

Scelte di Sara:
- «Much better. You fixed it.» — *calda*
  - → **Simon:** You fixed it. I just pointed.
- «Still a bit stiff.»
  - → **Simon:** Normal. It'll loosen up if you keep moving it.


`— punto di interruzione —`

**Pezzo 2**

> **Simon:** Next session: ten minutes on the bike to warm up, then back and shoulders. Light.  
> **Simon:** And bring water. Real water, not those neon drinks.  
> *(Neon drinks. Joanie's bottle is literally blue.)*  

Scelte di Sara:
- «Noted.»
  - → **Simon:** See you there.
- «Yes, sir :)» — *calda*
  - → **Simon:** Ha. Simon is fine.
- «Do you give homework to all your clients?» — *richiede confidence=25, calda*
  - → **Simon:** Only the ones who actually do it.
  - → *(Is that a compliment or a challenge?)*


### simon_a1 · A

*Se scrive Sara:*

> **Sara:** Hi Simon, it's Sara. Quick question... is it normal that I can't walk down the stairs today? :)  

*Se scrive lui/lei:*

> **Simon:** Day after leg day. How are the stairs treating you? ;)  
> **Sara:** Is it normal that I can't walk down them? :)  

**Pezzo 1**

> **Simon:** Haha, totally normal. It's called DOMS.  
> **Simon:** Delayed onset muscle soreness. Basically your legs are filing a complaint.  
> *(He even makes pain sound fun.)*  

Scelte di Sara:
- «So what do I do? Stay on the sofa all day?»
  - → **Simon:** Nope. The sofa is the enemy.
- «Tell my legs it was your idea, not mine.» — *calda*
  - → **Simon:** Already did. They said you're tougher than you look.
- «Next time go easier on me, coach.» — *richiede confidence=25, calda*
  - → **Simon:** Easier? You were the one who asked for one more set.
  - → **Simon:** Coach. I like that.


`— punto di interruzione —`

**Pezzo 2**

> **Simon:** Light walk, lots of water, ten minutes of stretching before bed.  
> **Simon:** And a hot shower. Not a cold one, whatever Joanie tells you.  
> *(How does he know Joanie told me to take a cold shower?)*  

Scelte di Sara:
- «Joanie says a lot of things.»
  - → **Simon:** She does. Don't listen to half of them.
- «Can you send me the stretches?» — *flag simon_stretching*
- «Or I could just skip leg day forever.»
  - → **Simon:** Not on my watch.


`— punto di interruzione —`

**Pezzo 3**

*[if fatto("simon_stretching")]*  
> **Simon:** 1. Quads against the wall, 30 seconds each leg.  
> **Simon:** 2. Sit down, legs straight, reach for your toes. Don't bounce.  
> **Simon:** 3. Child's pose. Just breathe.  
> **Simon:** Do them tonight. I'll ask you next time.  
*[else]*  
> **Simon:** Do the stretches anyway. I'll ask you next time.  

Scelte di Sara:
- «Promise.»
  - → **Simon:** That's the spirit.
- «Yes, coach :)» — *calda*
  - → **Simon:** Good. Now go drink some water.
- «We'll see ;)» — *richiede confidence=25, calda*
  - → **Simon:** I'll know if you didn't. I always know.
  - → *(Does he say that to all his clients?)*


### simon_a2 · A

*Se scrive Sara:*

> **Sara:** Ok, nutrition question. What am I supposed to eat before training? I always feel dizzy.  

*Se scrive lui/lei:*

> **Simon:** Random check: what did you eat before yesterday's session? You looked pale.  
> **Sara:** Coffee. And half a cookie. Is that bad?  

**Pezzo 1**

> **Simon:** That's why. You're training on empty.  
> **Simon:** An hour before: a banana, some yogurt, a slice of toast. Nothing heavy.  

Scelte di Sara:
- «Does chocolate count as fuel?» — *calda*
  - → **Simon:** Dark chocolate, two squares. After. As a reward.
- «A banana I can do.»
  - → **Simon:** Good. Small changes, big difference.


`— punto di interruzione —`

**Pezzo 2**

> **Simon:** And breakfast. Real breakfast. Oats, eggs, fruit.  
> **Simon:** I'll send you what I eat. Copy it for a week and tell me how you feel.  
*[flag simon_colazione]*  
> *(His breakfast has more protein than my entire week.)*  

Scelte di Sara:
- «Deal. One week.»
  - → **Simon:** I'll hold you to it.
- «Do you ever eat pizza? Be honest.» — *calda*
  - → **Simon:** Every Saturday. Don't tell my clients.


### simon_a3 · A

*Se scrive Sara:*

> **Sara:** Can I file a complaint about the gym music? Same five songs every day.  

**Pezzo 1**

> **Simon:** Haha. That's the owner's playlist. I've been fighting it for two years.  
> **Simon:** What do you listen to when you train?  

Scelte di Sara:
- «Old pop. Don't judge me.»
  - → **Simon:** No judging. Whatever makes you move.
- «Nothing. I'm too busy trying not to die.» — *calda*
  - → **Simon:** Ha! That's a playlist too.


`— punto di interruzione —`

**Pezzo 2**

> **Simon:** Try this. Fast enough for cardio, not so loud it kills you.  
> **Simon:** (A link to a playlist: «Simon — Leg Day»)  
*[flag simon_playlist]*  
> *(A playlist called Leg Day. Of course.)*  

Scelte di Sara:
- «I'll try it tomorrow.»
  - → **Simon:** Tell me if it works.
- «If I survive leg day, it's thanks to this.» — *calda*
  - → **Simon:** You'll survive. You always do.


### simon_a4 · A

*Se scrive Sara:*

> **Sara:** Honest question: is there anyone in the world who actually likes burpees?  

**Pezzo 1**

> **Simon:** Me.  
> **Simon:** But I also like deadlifts, so I'm not a reliable witness.  

Scelte di Sara:
- «What's your favourite one?»
  - → **Simon:** Deadlift. Pick something heavy off the floor. Simple. Honest.
- «You're a monster.» — *calda*
  - → **Simon:** A friendly monster.


`— punto di interruzione —`

**Pezzo 2**

> **Simon:** What's yours? And «none» is not an answer.  

Scelte di Sara:
- «The bike. Because I can sit.»
  - → **Simon:** Fair. We'll work on that.
- «Squats. They're starting to feel good.» — *calda, flag simon_squat*
  - → **Simon:** Squats are the queen of exercises. Good taste.


### simon_a5 · A

*Se scrive Sara:*

> **Sara:** Do personal trainers rest on weekends or do you live at the gym?  

**Pezzo 1**

> **Simon:** Saturday mornings I hike with some friends. Saturday nights, out.  
> **Simon:** Sunday I do absolutely nothing. It's sacred.  
> **Simon:** You?  

Scelte di Sara:
- «[nome_compagno] and I usually stay in. Movies, takeaway.»
  - → **Simon:** Sounds nice. Calm.
- «Nothing exciting. Laundry, mostly.»
  - → **Simon:** Laundry. Wild.


`— punto di interruzione —`

**Pezzo 2**

> **Simon:** If you ever want to try a hike, the trail by the lake is easy. Great view.  
> *(He didn't say «with me». He just said «try a hike».)*  

Scelte di Sara:
- «Maybe with Joanie, one day.»
  - → **Simon:** Good idea.
- «Send me the name of the trail.» — *calda*
  - → **Simon:** Pine Ridge. Start early, it gets crowded.


### simon_a6 · A

*Se scrive Sara:*

> **Sara:** Joanie wants to go out Saturday and says you know every bar in town. Is that true?  

**Pezzo 1**

> **Simon:** Every bar is an exaggeration. Most of them.  
> **Simon:** What kind of night? Dancing, drinks, or talking without shouting?  

Scelte di Sara:
- «Talking without shouting. I'm old.»
  - → **Simon:** You're not old. Try The Lantern, on the river. Quiet, good cocktails.
- «Joanie will say dancing. She always does.» — *calda*
  - → **Simon:** Then Velvet. But wear comfortable shoes, the floor is murder.


`— punto di interruzione —`

**Pezzo 2**

> **Simon:** If you go, say hi. I'm usually around with my friends.  
> *(He'd be there. Of course he would.)*  

Scelte di Sara:
- «We'll see what Joanie decides.»
  - → **Simon:** She always decides.
- «Then I'll know at least one face.» — *calda*
  - → **Simon:** A friendly one :)


### simon_a7 · A

*Se scrive Sara:*

> **Sara:** My running shoes are older than my relationship. Should I buy new ones?  

**Pezzo 1**

> **Simon:** If they're older than your relationship, yes. Definitely.  
> **Simon:** Go to a proper shop. Ask them to look at how you walk.  

Scelte di Sara:
- «And clothes? I train in an old T-shirt.»
  - → **Simon:** Whatever you're comfortable in. Comfortable means you move better.
- «Do you get a commission from the shoe shop?» — *calda*
  - → **Simon:** I wish. I'd be rich. Everyone has bad shoes.


`— punto di interruzione —`

**Pezzo 2**

> **Simon:** Honestly, the shoes matter. The rest is up to you.  
> **Simon:** Some people train better when they feel good in what they wear. That's all.  
> *(Joanie would say that's a hint about the tight top. Simon probably just means... shoes.)*  

Scelte di Sara:
- «Shoes first. Then we'll see.»
  - → **Simon:** Good plan.
- «Joanie wants me to buy matching sets. Like hers.» — *calda*
  - → **Simon:** Joanie's sets are a whole event. You don't need an event. You need to train.


### simon_a8 · A

*Se scrive Sara:*

> **Sara:** Can I ask you something? What should my goal be? I don't even know why I'm training.  

**Pezzo 1**

> **Simon:** Good question. Most people never ask it.  
> **Simon:** What do you want to feel? Not look. Feel.  

Scelte di Sara:
- «Stronger. I want to carry the shopping without dying.»
  - → **Simon:** That's a real goal. I like real goals.
- «More sure of myself.» — *calda*
  - → **Simon:** That's the best one. And training is a good way to get there.


`— punto di interruzione —`

**Pezzo 2**

> **Simon:** So here's yours: ten proper push-ups by the end of the month.  
> **Simon:** Not on your knees. Proper ones.  
*[flag simon_obiettivo_pushup]*  
> *(Ten. I can barely do two.)*  

Scelte di Sara:
- «Ten? Are you serious?»
  - → **Simon:** Completely. You'll get there.
- «Deal. And if I make it?» — *richiede confidence=25, calda*
  - → **Simon:** Then you set the next goal. Not me.
  - → *(I like that more than I should.)*


### simon_b1 · B

*Se scrive Sara:*

> **Sara:** Can I tell you something stupid? I hate the mirrors at the gym.  

*Se scrive lui/lei:*

> **Simon:** You always train facing away from the mirror. I noticed. Everything ok?  
> **Sara:** I hate the mirrors. That's all.  

**Pezzo 1**

> **Simon:** Not stupid. Almost everyone does, at the beginning.  
> **Simon:** What do you see in there?  

Scelte di Sara:
- «Someone who doesn't belong in a gym.»
  - → **Simon:** Wrong. You show up every week. That's the only thing that makes someone belong.
- «Everything I'd like to change.» — *calda*
  - → **Simon:** Then look at what's already changed. Your posture. Your squat. You stand differently.

*[flag simon_insicurezza]*  

`— punto di interruzione —`

**Pezzo 2**

> **Simon:** Next time, one set facing the mirror. Just one. Watch your form, not the rest.  
> *(Watch your form, not the rest. He makes it sound so easy.)*  

Scelte di Sara:
- «One set. I'll try.»
  - → **Simon:** That's all I'm asking.
- «Only if you don't laugh.» — *calda*
  - → **Simon:** I never laugh at people who work hard. Only at people who skip leg day.


### simon_b2 · B

*Se scrive Sara:*

> **Sara:** Joanie asked me to ask you something. Are you seeing anyone? Her words, not mine.  

**Pezzo 1**

> **Simon:** Haha. Tell Joanie: no. Single.  
> **Simon:** Between the gym, clients and the weekend, there's not much room left.  

Scelte di Sara:
- «Sounds lonely.»
  - → **Simon:** Sometimes. Mostly it's just free.
- «The gym is your relationship.» — *calda*
  - → **Simon:** The gym and I are very happy together. It never asks where I've been.


`— punto di interruzione —`

**Pezzo 2**

> **Simon:** And you? How long with [nome_compagno]?  
> *(He remembers his name.)*  

Scelte di Sara:
- «A few years. He's a good man.» — *Josh +1*
  - → **Simon:** Good. That's rare.
- «A few years. It's... comfortable.»
  - → **Simon:** Comfortable is good. Comfortable is also a word people use for sofas.
  - → *(Why did I write «comfortable»?)*


### simon_b3 · B

*Se scrive Sara:*

> **Sara:** Be honest with me. Am I hopeless? As a client, I mean.  

**Pezzo 1**

> **Simon:** Honest? You're one of the most improved people I train.  
> **Simon:** Four weeks ago you couldn't hold a plank for twenty seconds. Now it's a minute.  

Scelte di Sara:
- «You're just being nice.»
  - → **Simon:** I'm never nice about planks. Ask anyone.
- «Really? A minute?» — *calda*
  - → **Simon:** I count. It's my job.


`— punto di interruzione —`

**Pezzo 2**

> **Simon:** You listen, you don't complain much, and you come back. That's 90% of it.  
> *(I complain a lot. Just not to him.)*  

Scelte di Sara:
- «Thank you. I needed that.» — *calda*
  - → **Simon:** Anytime. Now go stretch.
- «I'll tell Joanie I'm your best client.»
  - → **Simon:** Don't. She'll want a rematch.


### simon_b4 · B

*Se scrive Sara:*

> **Sara:** Can I ask why you're single? You seem like a catch. Joanie's words again.  

**Pezzo 1**

> **Simon:** Joanie should open a dating agency.  
> **Simon:** I was with someone for three years. She said I loved the gym more than her.  

Scelte di Sara:
- «Was she right?»
  - → **Simon:** ...Partly. I was 22 and stupid. I'd do it differently now.
- «That must have hurt.» — *calda*
  - → **Simon:** It did. For a while. Then I trained more. Very healthy, I know.


`— punto di interruzione —`

**Pezzo 2**

> **Simon:** What about you? Ever been dumped for a hobby?  

Scelte di Sara:
- «No. I was the one who left, last time.»
  - → **Simon:** Good for you. Leaving takes guts.
  - → *(I don't want to talk about Jacob. Not with him.)*
- «Only for my writing. [nome_compagno] says I live in my laptop.» — *calda*
  - → **Simon:** Writing? You never told me. What do you write?
  - → **Simon:** Cool. Train the body, train the head.


### simon_b5 · B

*Se scrive Sara:*

> **Sara:** Weird thing today. A colleague asked if I'd done something different. «You walk differently.»  

**Pezzo 1**

> **Simon:** Ha! Told you. Posture changes first. People notice before you do.  
> **Simon:** How did it feel?  

Scelte di Sara:
- «Strange. I'm not used to being noticed.»
  - → **Simon:** Get used to it. It's only going to happen more.
- «Good. Really good, actually.» — *calda, flag simon_notata*
  - → **Simon:** That's the feeling. Remember it on the days you don't want to come.


`— punto di interruzione —`

**Pezzo 2**

> **Simon:** You did the work. Not me. Enjoy it.  
> *(Enjoy it. When was the last time someone told me to enjoy something about myself?)*  

Scelte di Sara:
- «I will. Thanks, Simon.»
  - → **Simon:** :)
- «You did some of the work. The shouting part.» — *calda*
  - → **Simon:** I never shout. I motivate loudly.



## Howard

### howard_intro · Introduzione

*Se scrive Sara:*

> **Sara:** Hi Howard, it's Sara. Thank you again for finding my keys. You saved my life.  

**Pezzo 1**

> **Howard:** Sara!  
> **Howard:** Oh you don't have to thank me. I was so happy to find them.  
> **Howard:** Under the stairs, can you believe it. Right under our feet all that time.  
> **Howard:** I'm glad you have my number now. For anything. Anything at all. I'm always home.  

Scelte di Sara:
- «That's very kind of you.»
  - → **Howard:** It's nothing. It's what neighbours are for.
- «You're a lifesaver, really.» — *calda*
  - → **Howard:** A lifesaver. Nobody ever called me that.
  - → **Howard:** I'm going to remember that.


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** Did [nome_compagno] get home ok last night? I heard your door very late.  
> *(He heard our door?)*  

Scelte di Sara:
- «Yes, a long shift. Sorry about the noise.»
  - → **Howard:** No noise at all! I just sleep very light. Goodnight Sara.
- «You hear everything through those walls, huh :)» — *calda*
  - → **Howard:** Oh no no. Only the door. Only sometimes.
  - → **Howard:** Goodnight Sara.


**Retroscena:** *Howard puts the phone down and opens the drawer by the door. Next to his own keys, a new one, still shiny. The copy works perfectly.*

### howard_a1 · A

*Se scrive Sara:*

> **Sara:** Howard, do you know who's dragging furniture upstairs at midnight?  

**Pezzo 1**

> **Howard:** The Kowalskis. Third floor. They rearrange the living room every Tuesday.  
> **Howard:** And the boy on the fourth floor plays drums on Sundays from 4 to 6.  
> **Howard:** And Mrs. Dean takes the bins out at 6:10 every morning. Like a clock.  
> *(He knows everyone's schedule. That's... very thorough.)*  

Scelte di Sara:
- «You know everything about this building.» — *calda*
  - → **Howard:** I've been here a long time. You notice things.
- «Thanks. I'll survive until Wednesday then.»
  - → **Howard:** Ha! Yes. Wednesday is quiet.


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** You leave at 8:20, right? The Kowalskis' cat sits on the landing at that time. Watch your step.  
> *(8:20. Exactly 8:20.)*  

Scelte di Sara:
- «How do you know when I leave?»
  - → **Howard:** Oh, I hear your heels on the stairs. Every morning. Very regular.
  - → **Howard:** It's a nice sound. It means the day is starting.
- «Thanks for the warning :)» — *calda*
  - → **Howard:** Anytime. I'll keep an eye out.


### howard_a2 · A

*Se scrive Sara:*

> **Sara:** Random question: do you know a good plumber? The kitchen tap is dripping all night.  

**Pezzo 1**

> **Howard:** A plumber? No no no. Don't waste money.  
> **Howard:** It's the washer. Ten minutes. I can fix it.  
> **Howard:** I have all the tools. I could come tomorrow afternoon.  

Scelte di Sara:
- «Are you sure? I don't want to bother you.»
  - → **Howard:** Bother! You could never bother me.
- «That would be amazing, thank you.» — *calda*
  - → **Howard:** Wonderful. It will be a pleasure.


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** What time is [nome_compagno] at work tomorrow? So I know when to come.  
> **Howard:** I mean, so I don't disturb you both. Two people at home and a man under the sink, it's crowded.  
> *(That's thoughtful of him. I think.)*  

Scelte di Sara:
- «He's out until seven. Come at four?» — *flag howard_rubinetto*
  - → **Howard:** Four. Perfect. I'll be there at four.
- «Come when we're both home, it's fine.»
  - → **Howard:** Oh. Of course. Of course. Saturday then.


### howard_a3 · A

*Se scrive Sara:*

> **Sara:** Howard, the whole stairwell smells amazing. Is that you?  

*Se scrive lui/lei:*

> **Howard:** I made too much lasagna. I always make too much. Old habit.  
> **Sara:** So that's what smells so good in the stairwell!  

**Pezzo 1**

> **Howard:** Lasagna. My mother's recipe. It takes four hours.  
> **Howard:** But I always make it for six people and there's only me.  

Scelte di Sara:
- «Four hours! You're patient.»
  - → **Howard:** I have time. That's the one thing I have.
- «Your mother would be proud.» — *calda*
  - → **Howard:** She would. She always said I'd make some woman very happy.
  - → **Howard:** She was wrong about that.


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** Can I bring you a plate? For you and [nome_compagno]. Mostly for you. You're too thin.  
> *(Too thin. Nobody has ever told me that.)*  

Scelte di Sara:
- «Yes please, that's so sweet.» — *calda, flag howard_lasagna*
  - → **Howard:** I'll leave it at your door in ten minutes. Still warm.
- «Thank you, but we already ate.»
  - → **Howard:** Tomorrow then. Lasagna is better the day after.


### howard_a4 · A

*Se scrive Sara:*

> **Sara:** Do you know any good old films? I want something that isn't a superhero.  

**Pezzo 1**

> **Howard:** Oh! Yes. Yes. Old films are my passion.  
> **Howard:** «Last Train Home». Black and white. A woman, married, meets a man at a train station.  
> **Howard:** Nothing happens and everything happens. You'll cry.  

Scelte di Sara:
- «A married woman and a stranger? Sounds dangerous.» — *calda*
  - → **Howard:** The most beautiful things are a little dangerous.
- «I'll try it this weekend.»
  - → **Howard:** Tell me what you think. I want to know everything you think.


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** Last night you were watching the one with the boat, right? I could hear the music.  
> **Howard:** The walls are thin. I don't mind. I like hearing you two laugh.  
> *(I didn't think the TV was that loud.)*  

Scelte di Sara:
- «Sorry! I'll turn it down.»
  - → **Howard:** No! Don't. Please. It keeps me company.
- «You should come watch one with us sometime.» — *calda*
  - → **Howard:** Really? You'd let me?
  - → **Howard:** I'll bring snacks. Anything you want.


### howard_a5 · A

*Se scrive Sara:*

> **Sara:** Howard, was there a cat in your flat once? I keep finding grey hairs on the landing.  

**Pezzo 1**

> **Howard:** Duchess. Grey Persian. She died two years ago.  
> **Howard:** Fourteen years together. Longer than any of my relationships. Ha.  

Scelte di Sara:
- «I'm so sorry.» — *calda*
  - → **Howard:** Thank you. You're the first person who said that.
- «Fourteen years is a good long life.»
  - → **Howard:** It is. She was spoiled. She slept on my pillow.


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** You remind me of her a little.  
> **Howard:** Elegant. A bit shy. She only came to me when she wanted something.  
> **Howard:** But when she came, she stayed.  
> *(That's... a strange compliment. He means it kindly.)*  

Scelte di Sara:
- «I'll take that as a compliment :)»
  - → **Howard:** It is. The biggest one I have.
- «Maybe you should get another cat.»
  - → **Howard:** Maybe. Or maybe I just need better company.


**Retroscena:** *In Howard's living room, on the armrest next to him, folded with care, there is a piece of lace that does not belong to him. He strokes it while he types.*

### howard_a6 · A

*Se scrive Sara:*

> **Sara:** Howard, did a courier leave a parcel with you? The tracking says «delivered to neighbour».  

*Se scrive lui/lei:*

> **Howard:** Sara, the courier left a parcel for you. I have it safe. Very safe.  
> **Sara:** Oh thank you! I was looking for it.  

**Pezzo 1**

> **Howard:** Yes! It's here. I put it on the kitchen table so nobody steps on it.  
> **Howard:** It's light. Soft. Clothes?  
> *(Did he shake it?)*  

Scelte di Sara:
- «Just a top. Nothing exciting.»
  - → **Howard:** I'm sure it will look lovely on you.
- «Curious, aren't you? :)» — *calda*
  - → **Howard:** Guilty. I don't get many parcels. I live through other people's.


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** Come get it whenever. I'll make tea. I have the good biscuits.  

Scelte di Sara:
- «I'll come after work. Five minutes.» — *calda, flag howard_pacco_tea*
  - → **Howard:** Five minutes. Wonderful. The kettle will be ready.
- «Could you leave it at my door? I'm in a rush.»
  - → **Howard:** Of course. Of course. At your door.


### howard_a7 · A

*Se scrive Sara:*

> **Sara:** How do you fill your days, Howard? I never asked.  

**Pezzo 1**

> **Howard:** Oh, a very boring routine. You'll laugh.  
> **Howard:** Up at 6. Coffee. Radio. Crossword. Walk to the market.  
> **Howard:** At 7:40 the pipes start singing, that means you're in the shower and the building is awake.  
> *(He knows when I shower?)*  

Scelte di Sara:
- «The pipes? Really?»
  - → **Howard:** Old building. Everything echoes. I'm used to all your noises.
  - → **Howard:** All the building's noises, I mean.
- «Sounds peaceful, actually.» — *calda*
  - → **Howard:** Peaceful. Yes. Quiet. Too quiet, sometimes.


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** In the evening I cook, I watch a film, I wait for the day to end.  
> **Howard:** The best part of the day is when I see you on the stairs. Honestly.  

Scelte di Sara:
- «That's sweet. And a bit sad.» — *calda*
  - → **Howard:** A bit sad. Yes. You see me. Not many people do.
- «You should join a club or something.»
  - → **Howard:** Maybe. Clubs are full of strangers. You're not a stranger.


### howard_a8 · A

*Se scrive Sara:*

> **Sara:** Busy weekend, Howard?  

*Se scrive lui/lei:*

> **Howard:** Are you two home this weekend? Just asking. No reason.  
> **Sara:** Probably. Why?  

**Pezzo 1**

> **Howard:** Me? Oh, the usual. Nobody calls on Saturdays.  
> **Howard:** Sunday is the worst. The whole building goes out and I stay. Like a guard.  

Scelte di Sara:
- «That sounds lonely.»
  - → **Howard:** It is. But I'm used to it.
- «Come over for coffee on Sunday.» — *calda, flag howard_caffe_domenica*
  - → **Howard:** Really? Really really?
  - → **Howard:** What time? I'll be there. I'll bring the biscuits. The good ones.


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** You're the kindest person in this building, Sara. Maybe in this city.  
> *(Poor Howard. He has nobody.)*  

Scelte di Sara:
- «Don't exaggerate :)»
  - → **Howard:** I never exaggerate about you.
- «You deserve a bit of company.» — *calda*
  - → **Howard:** I'm starting to believe it.


**Retroscena:** *On the kitchen calendar Howard circles Sunday in red. He writes «S.» inside the circle, then a second time, more slowly.*

### howard_b1 · B

*Se scrive Sara:*

> **Sara:** Howard, can I ask you something personal? Did you ever want children?  

*Se scrive lui/lei:*

> **Howard:** I saw a family on the bus today. Mum, dad, two little ones. I stared like a fool.  
> **Sara:** Did you ever want one? A family?  

**Pezzo 1**

> **Howard:** More than anything.  
> **Howard:** A wife who waits for me. Someone to cook for. Someone who needs me.  
> **Howard:** It never happened. Women never saw me. I was always the friend, the neighbour.  

Scelte di Sara:
- «It's not too late, Howard.» — *calda*
  - → **Howard:** You really think so?
- «I'm sorry. That must hurt.»
  - → **Howard:** Every day. But talking to you helps.


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** You and [nome_compagno] will have beautiful children.  
> **Howard:** He's a lucky man. I hope he knows it. I hope he never leaves you alone too much.  
> *(Why does that sound like a warning?)*  

Scelte di Sara:
- «He knows. Don't worry.» — *Josh +1*
  - → **Howard:** Good. Good.
- «He works a lot, lately.»
  - → **Howard:** I know. I hear him leave early and come back late.
  - → **Howard:** If you ever feel alone in there, I'm here. Just a wall away.


### howard_b2 · B

*Se scrive Sara:*

> **Sara:** Was there ever someone special, Howard?  

**Pezzo 1**

> **Howard:** Once. Margaret. Thirty years ago. She worked at the post office.  
> **Howard:** I bought stamps every day for a year. I had three thousand stamps.  
> **Howard:** I never asked her out. She married a mechanic.  

Scelte di Sara:
- «Three thousand stamps! Howard!» — *calda*
  - → **Howard:** I still have them. I can't throw them away.
- «Why didn't you ask?»
  - → **Howard:** Because I knew the answer. I always know the answer.


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** I promised myself: next time I won't wait. I'll do something.  
> **Howard:** Even if it's small. Even if nobody notices.  
> *(I hope he finds someone. He really deserves it.)*  

Scelte di Sara:
- «Good. Don't wait anymore.» — *calda*
  - → **Howard:** I won't. Thank you, Sara. You give me courage.
- «Small things count.»
  - → **Howard:** They do. They count a lot.


### howard_b3 · B

*Se scrive Sara:*

> **Sara:** You were very quiet on the stairs today. Are you ok?  

*Se scrive lui/lei:*

> **Howard:** Sorry to write so late. I can't sleep.  
> **Sara:** It's ok. What's wrong?  

**Pezzo 1**

> **Howard:** I went to the doctor. Nothing serious. Blood pressure.  
> **Howard:** But in the waiting room they asked «who should we call in case of emergency».  
> **Howard:** And I had nobody to write. Nobody, Sara.  

Scelte di Sara:
- «Write my name.» — *calda, flag howard_contatto_emergenza*
  - → **Howard:** ...
  - → **Howard:** Do you mean it?
- «Oh Howard. I'm so sorry.»
  - → **Howard:** Don't be. It's my life. I chose it. Or it chose me.


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** I'm afraid of dying in this flat and nobody noticing for weeks.  
> **Howard:** Sorry. Sorry. I'm crying like an idiot. Forget it.  
> *(He's crying. Alone, next door.)*  

Scelte di Sara:
- «I would notice. I promise.» — *calda*
  - → **Howard:** Thank you. Goodnight, Sara. You're an angel.
- «Try to sleep. We'll talk tomorrow.»
  - → **Howard:** Tomorrow. Yes. Goodnight.


**Retroscena:** *Howard's eyes are perfectly dry. He reads her last message twice, smiles, and switches off the lamp. «An angel.»*

### howard_b4 · B

*Se scrive Sara:*

> **Sara:** How are you today, Howard? Better?  

**Pezzo 1**

> **Howard:** Better. Because you asked.  
> **Howard:** Do you know you're the only person who asks me how I am?  
> **Howard:** Forty years in this city and you're the only one.  

Scelte di Sara:
- «That can't be true.»
  - → **Howard:** It is. I counted.
- «Then I'll keep asking.» — *calda*
  - → **Howard:** Every day?


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** I read our messages again sometimes. When the evening is long.  
> **Howard:** Is that strange? Tell me if it's strange.  
> *(It is a little strange. But he's lonely.)*  

Scelte di Sara:
- «It's not strange. It's sweet.» — *calda*
  - → **Howard:** Sweet. I'll remember that word too.
- «A little strange :) But ok.»
  - → **Howard:** Ha. I'll try to be less strange. For you.


**Retroscena:** *On Howard's computer a folder called «S» grows every night: every message, every photo she has ever posted, sorted by date.*

### howard_b5 · B

*Se scrive Sara:*

> **Sara:** I'm working late tonight. Could you tell me if the courier comes? Sorry to ask.  

**Pezzo 1**

> **Howard:** Of course! I'll stand by the door. Don't worry about anything.  
> **Howard:** It's nice to be useful to someone. To you.  

Scelte di Sara:
- «What would I do without you?» — *calda*
  - → **Howard:** You'd manage. But I'm glad you don't have to.
- «Thank you, Howard.»
  - → **Howard:** Always.


`— punto di interruzione —`

**Pezzo 2**

> **Howard:** Can I tell you something? When I know you're home, I sleep better.  
> **Howard:** It's like having a light on in the corridor.  
> *(Like a light in the corridor. He needs someone so badly.)*  

Scelte di Sara:
- «I'm glad I help. Really.» — *calda, flag howard_luce_corridoio*
  - → **Howard:** You help more than you know.
- «You should meet more people, Howard. Not just me.»
  - → **Howard:** ...
  - → **Howard:** You're right. Of course. Goodnight.
  - → *(Did I hurt him?)*



## Daniel

### daniel_intro · Introduzione · può scrivere lui per primo

*Se scrive Sara:*

> **Sara:** Good evening. It's Sara. You asked for my number for Magnus... here I am.  

*Se scrive lui/lei:*

> **Daniel:** Daniel. I promised Magnus I'd follow up on the novel. So: how many pages do you have?  
> **Sara:** Good evening to you too. About a hundred and twenty.  

**Pezzo 1**

> **Daniel:** A hundred and twenty pages and you hide them in a drawer. Typical.  
> **Daniel:** Talent always apologises for existing. Mediocrity never does.  
> *(Is that a compliment? It sounds like a lecture.)*  

Scelte di Sara:
- «I'm not hiding them. I'm finishing them.» — *calda*
  - → **Daniel:** Good answer. Keep that tone with Magnus.
- «Thank you for introducing me to him.»
  - → **Daniel:** Don't thank me. I don't do favours. I make investments.


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** Did [nome_compagno] read them?  

Scelte di Sara:
- «Of course. He loves them.» — *Josh +1*
  - → **Daniel:** Of course he does. He loves everything you do. That's not a review, that's a reflex.
- «Not yet. He's always tired.»
  - → **Daniel:** Tired. Yes, I've noticed. Goodnight, Sara.
  - → *(Why did I tell him that?)*


### daniel_a1 · A

*Se scrive Sara:*

> **Sara:** You said talent hides. What makes you think I have any? You haven't read a line.  

**Pezzo 1**

> **Daniel:** I watched you talk about it at dinner. Your voice changed.  
> **Daniel:** People lie about many things. Not about what makes their voice change.  

Scelte di Sara:
- «That's a very clever line.»
  - → **Daniel:** I have many. That one happens to be true.
- «What is it about, then? Guess.» — *richiede confidence=25, calda*
  - → **Daniel:** A woman who wants more than she's allowed to want.
  - → *(...How?)*


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** Send me the first page. One page. I'll tell you if it's alive.  

Scelte di Sara:
- «Not a chance. Not yet.»
  - → **Daniel:** Good. Make me wait. It's a sign of quality.
- «One page. Be honest.» — *calda, flag daniel_prima_pagina*
  - → **Daniel:** ...
  - → **Daniel:** Alive. Annoyingly so. Cut the second sentence, it's apologising again.


### daniel_a2 · A

*Se scrive Sara:*

> **Sara:** Can I ask how you got where you are? Everyone at that dinner was terrified of you.  

**Pezzo 1**

> **Daniel:** I decided at twenty-five that I would never ask permission again.  
> **Daniel:** The rest was just paperwork.  

Scelte di Sara:
- «That sounds lonely.»
  - → **Daniel:** It sounds free. People confuse the two all the time.
- «I wish I had that.» — *calda*
  - → **Daniel:** You do. You just keep it on a leash.


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** Some people ask permission their whole life. Some even ask permission to take a day off.  
> **Daniel:** Your [nome_compagno] sent me a three-paragraph email to leave at five on Friday.  
> *(That's cruel. And it's exactly the kind of thing he'd do.)*  

Scelte di Sara:
- «He's polite. That's not a flaw.» — *Josh +1*
  - → **Daniel:** Loyal. I like that in you. Less in him.
- (Let it slide.)
  - → **Daniel:** Silence. Smart.
- «Three paragraphs? Really?» — *calda, Corr +1*
  - → **Daniel:** With a bullet list. I'm framing it.


### daniel_a3 · A

*Se scrive Sara:*

> **Sara:** That restaurant on Thursday. Is it always like that, or did you book the whole place to impress?  

**Pezzo 1**

> **Daniel:** I never need to impress. I just refuse to eat badly.  
> **Daniel:** Did you like it?  

Scelte di Sara:
- «The food was perfect. The company was... intense.» — *calda*
  - → **Daniel:** Intense. I'll take it.
- «A bit too formal for me.»
  - → **Daniel:** Formal is a costume. You wore it well.


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** There's a place by the harbour. No menu. The chef decides. You'd love it.  
> *(Is he inviting me? No. He's just... describing.)*  

Scelte di Sara:
- «I'll tell [nome_compagno]. Maybe for our anniversary.»
  - → **Daniel:** Do. Tell him to book three months ahead. And to let you order.
- «No menu? That sounds like you.» — *calda*
  - → **Daniel:** Everything good sounds like me.


### daniel_a4 · A

*Se scrive Sara:*

> **Sara:** Was that your car outside the restaurant? The black one that looked like a spaceship?  

**Pezzo 1**

> **Daniel:** It's not a spaceship. It's a reminder.  
> **Daniel:** Every morning I see it and I remember what I worked for.  

Scelte di Sara:
- «Most people use a photo for that.» — *calda*
  - → **Daniel:** Most people don't have anything worth photographing.
- «It's very... loud.»
  - → **Daniel:** So am I. We understand each other.


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** What does [nome_compagno] drive? Wait. Let me guess. Something sensible. Grey. Good mileage.  

Scelte di Sara:
- «It gets us everywhere. That's what matters.» — *Josh +1*
  - → **Daniel:** Everywhere he's allowed to go, yes.
- (Don't answer.)
  - → **Daniel:** I'll take that as a «grey».
- «...It's grey.» — *calda, Corr +1*
  - → **Daniel:** Of course it is.
  - → *(I shouldn't have laughed. I did laugh.)*


### daniel_a5 · A

*Se scrive Sara:*

> **Sara:** [nome_compagno] says you're never in the office on Mondays. Where do you go?  

**Pezzo 1**

> **Daniel:** Wherever the weekend didn't finish.  
> **Daniel:** Last week, the coast. A hotel where they bring breakfast to the terrace and nobody says a word.  

Scelte di Sara:
- «Must be nice.»
  - → **Daniel:** It is. That's the point.
- «I've never stayed anywhere like that.» — *calda*
  - → **Daniel:** You should. Some women look different with the sea behind them.
  - → *(Some women. Not me. Right?)*


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** Where would you go? Money is not a question. Answer fast.  

Scelte di Sara:
- «Somewhere quiet. With books.»
  - → **Daniel:** A writer's answer. Predictable and correct.
- «Somewhere nobody knows me.» — *richiede confidence=25, calda*
  - → **Daniel:** Now that's interesting. Who would you be there?


### daniel_a6 · A

*Se scrive Sara:*

> **Sara:** What was the music at dinner? Everyone was too scared to ask you.  

**Pezzo 1**

> **Daniel:** Jazz. Old jazz. Musicians who were drunk, broke and better than anyone alive today.  

Scelte di Sara:
- «I don't know anything about jazz.»
  - → **Daniel:** Nobody does. That's why it works.
- «It was beautiful. Send me something.» — *calda, flag daniel_jazz*
  - → **Daniel:** (A track: a slow saxophone, almost a whisper.)
  - → **Daniel:** Listen to it at night. Not in the car.


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** What do you listen to?  

Scelte di Sara:
- «Whatever's on the radio, honestly.»
  - → **Daniel:** Honesty. Rare. Terrible taste, but rare.
- «Sad songs. When nobody's around.» — *calda*
  - → **Daniel:** Everyone interesting does.


### daniel_a7 · A

*Se scrive Sara:*

> **Sara:** Do you ever stop? Working, I mean. [nome_compagno] says you answer emails at three in the morning.  

**Pezzo 1**

> **Daniel:** Success isn't a job. It's a temperature. You either have it or you're cold.  
> *(Who talks like that? He does. And it works on people.)*  

Scelte di Sara:
- «That's a sad way to live.»
  - → **Daniel:** Sad is a word invented by people who settled.
- «And what's my temperature?» — *richiede confidence=25, calda*
  - → **Daniel:** Rising. You just haven't noticed.


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** Your [nome_compagno] is very good at his job. Very good. Exactly as good as he needs to be, and not one bit more.  

Scelte di Sara:
- «He's better than you think.» — *Josh +1*
  - → **Daniel:** Then he's hiding it very well. I'll keep looking.
- (Let it go.)
  - → **Daniel:** Goodnight.
- «That's... horribly accurate.» — *calda, Corr +1*
  - → **Daniel:** I'm always accurate. Horrible is optional.


### daniel_a8 · A

*Se scrive Sara:*

> **Sara:** Long day at the paper. My editor wants me to rewrite a piece for the third time.  

**Pezzo 1**

> **Daniel:** Third time. Is it the piece or is it the editor?  

Scelte di Sara:
- «The editor. Definitely.» — *calda*
  - → **Daniel:** Then rewrite it once more, perfectly, and make her feel stupid.
- «Probably me.»
  - → **Daniel:** Stop that. It's an ugly habit.


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** We had a long day too. [nome_compagno] presented the quarterly report.  
> **Daniel:** He did very well. He only dropped the clicker twice.  

Scelte di Sara:
- «Leave him alone, Daniel.» — *Josh +1*
  - → **Daniel:** I always leave him alone. That's the problem.
- (Don't reply.)
  - → **Daniel:** Read. No answer. You're learning.
- «Twice?» — *calda, Corr +1*
  - → **Daniel:** The second time, it slid under the projector. It took two interns to get it out.
  - → *(Poor [nome_compagno]. Why am I smiling?)*


### daniel_b1 · B

*Se scrive Sara:*

> **Sara:** Settle a bet. Joanie says confidence is the most attractive thing in a man. I say kindness.  

*Se scrive lui/lei:*

> **Daniel:** A question for a writer. What makes a man attractive? You must have an opinion. You write them.  
> **Sara:** Kindness. Joanie says confidence.  

**Pezzo 1**

> **Daniel:** Joanie wins. Kindness is what women say. Confidence is what women choose.  

Scelte di Sara:
- «That's arrogant.»
  - → **Daniel:** It's statistics. Arrogance is just statistics with good posture.
- «Maybe. Sometimes.» — *calda*
  - → **Daniel:** Sometimes is how it always starts.


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** Think about the men in your stories. Are they kind?  
> *(...They're not. None of them.)*  

Scelte di Sara:
- «Some of them.»
  - → **Daniel:** The ones nobody remembers.
- «...No. They're not.» — *calda*
  - → **Daniel:** I know. I could tell from the first page.


### daniel_b2 · B

*Se scrive Sara:*

> **Sara:** How do you do it? Walk into a room like you own it?  

**Pezzo 1**

> **Daniel:** I decide that I do. The room usually agrees.  
> **Daniel:** You could do it too. You just need to stop checking if everyone is ok.  

Scelte di Sara:
- «Checking on people is called being nice.»
  - → **Daniel:** It's called being on duty. You're not a nurse.
- «Teach me, then.» — *richiede confidence=30, calda, flag daniel_lezione*
  - → **Daniel:** Lesson one: next time someone talks over you, don't stop talking.


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** Confidence is contagious. So is the opposite. You live with the opposite.  

Scelte di Sara:
- «Don't talk about him like that.» — *Josh +1*
  - → **Daniel:** Noted. You defend him beautifully. Someone has to.
- (Let it slide.)
- «He's... getting better.» — *calda, Corr +1*
  - → **Daniel:** Getting. Better. Two words nobody wants on their gravestone.


### daniel_b3 · B

*Se scrive Sara:*

> **Sara:** Can I ask you something? Are you happy? Really?  

**Pezzo 1**

> **Daniel:** Happy is for people who stopped wanting. I haven't.  
> **Daniel:** And you? Don't give me the dinner answer.  

Scelte di Sara:
- «I am happy.»
  - → **Daniel:** Three words, no punctuation of doubt. Impressive. Almost convincing.
- «Mostly. There's... something missing. I don't know what.» — *calda*
  - → **Daniel:** You know what. You just don't like the answer.


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** Let me guess. Saturday night. Sofa. He falls asleep at ten. You stay up and write.  
> *(Exactly that. Every Saturday.)*  

Scelte di Sara:
- «He works hard. He's tired.» — *Josh +1*
  - → **Daniel:** I make sure of it.
  - → *(What does that mean?)*
- (Don't answer.)
  - → **Daniel:** That's a yes.
- «How do you know that?» — *calda, Corr +1*
  - → **Daniel:** Because I've met him. And I've met you.


### daniel_b4 · B

*Se scrive Sara:*

> **Sara:** Has any woman ever said no to you?  

**Pezzo 1**

> **Daniel:** One. At twenty-three. She married a dentist.  
> **Daniel:** I still think about her every time I go to the dentist. Which is why I have perfect teeth.  

Scelte di Sara:
- «That's almost sweet.» — *calda*
  - → **Daniel:** Don't spread it around.
- «Only one? I don't believe you.»
  - → **Daniel:** Only one that mattered.


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** The women who stay with me are the ones who surprise me. It doesn't happen often.  
> *(Why do I want to ask if I surprised him?)*  

Scelte di Sara:
- «Good luck finding the next one.»
  - → **Daniel:** I don't need luck.
- «And what surprises you?» — *richiede confidence=30, calda*
  - → **Daniel:** A woman who says what she wants. Before I say it for her.


### daniel_b5 · B

*Se scrive Sara:*

> **Sara:** Question for a cynic: do you believe in love?  

**Pezzo 1**

> **Daniel:** I believe in desire. Love is desire that got comfortable and bought a sofa.  

Scelte di Sara:
- «That's the saddest thing I've ever read.»
  - → **Daniel:** And yet you're still reading.
- «And what's wrong with a sofa?» — *calda*
  - → **Daniel:** Nothing. Until you realise you're the only one still awake on it.


`— punto di interruzione —`

**Pezzo 2**

> **Daniel:** You love him. I don't doubt it.  
> **Daniel:** The question is: when was the last time you wanted him?  
> *(I shouldn't answer that. I'm not going to answer that.)*  

Scelte di Sara:
- «That's none of your business. Goodnight.» — *Josh +1*
  - → **Daniel:** Goodnight, Sara.
- «...Goodnight, Daniel.» — *calda, Corr +1, flag daniel_domanda_desiderio*
  - → **Daniel:** That's an answer too.



## Magnus

### editore_intro_pagine · Introduzione · condizione: `fatto('ep2_pagine_magnus')`

*Se scrive Sara:*

> **Sara:** Good evening, Mr. Magnus. It's Sara. I just wanted to make sure the pages arrived.  

*Se scrive lui/lei:*

> **Magnus:** Dear Sara, I read your fifty pages last night, in one sitting, which has not happened to me in some years. M.  
> **Sara:** Oh. Thank you. I didn't expect you to read them so soon.  

**Pezzo 1**

> **Magnus:** They arrived, and I read them twice. Please, just Magnus. «Mr.» makes me feel like my own father, and he was a dreadful man.  
> **Magnus:** Your sentences are careful. Too careful, in places. As if you were writing with someone reading over your shoulder. M.  
> *(That's exactly how it feels when I write.)*  

Scelte di Sara:
- «Is that bad?»
  - → **Magnus:** It is a habit. Habits can be broken, if one wishes. M.
- «You noticed that from fifty pages?» — *calda*
  - → **Magnus:** From the first five. I have read forty years of manuscripts. Fear has a smell. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** Chapter three, the woman alone in the kitchen at night. That is where you stop being careful. Write more of her.  
> **Magnus:** Good night, Sara. M.  
*[flag magnus_capitolo_tre]*  

Scelte di Sara:
- «I will. Thank you, Magnus.» — *calda*
- «Good night.»


### editore_intro_attesa · Introduzione · condizione: `not fatto('ep2_pagine_magnus')` · può scrivere lui per primo

*Se scrive Sara:*

> **Sara:** Good evening, Mr. Magnus. It's Sara, from Daniel's party.  

*Se scrive lui/lei:*

> **Magnus:** Dear Sara, I am still waiting for those pages. I am a patient man, but I am not a young one. M.  
> **Sara:** I'm sorry. I wasn't sure they were good enough.  

**Pezzo 1**

> **Magnus:** I remember you. You talked about your novel the way people talk about a lover they are ashamed of.  
> **Magnus:** I am still waiting for those pages. Whether they are good is my problem, not yours. M.  

Scelte di Sara:
- «I'm afraid you'll hate them.»
  - → **Magnus:** Then I will tell you why, and you will write better ones. That is the whole profession. M.
- «I'll send them this week. I promise.» — *calda, flag magnus_promessa_pagine*
  - → **Magnus:** A promise to an old man is a serious thing. I will hold you to it. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** Writers who wait for permission never get it. Writers who don't, sometimes do. Good night. M.  
> *(He's right. I've been waiting for permission my whole life.)*  

### editore_a1 · A

*Se scrive Sara:*

> **Sara:** Magnus, can I ask which writers you love? Not publish. Love.  

**Pezzo 1**

> **Magnus:** A dangerous question, because the answer changes with age. At twenty I loved the angry ones. At forty, the cruel ones.  
> **Magnus:** Now I love only those who are honest about desire. There are fewer than you would think. M.  

Scelte di Sara:
- «Desire? Not love?» — *calda*
  - → **Magnus:** Love is what we write about when we are afraid to write about desire. M.
- «I mostly read the classics. The safe ones.»
  - → **Magnus:** No classic is safe. They were only made safe by teachers. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** And yours? Tell me the book you would be embarrassed to be seen reading on a train. M.  

Scelte di Sara:
- «I'd rather not say.»
  - → **Magnus:** That is an answer, and a revealing one. M.
- «A romance with a very bad cover. I read it three times.» — *calda*
  - → **Magnus:** Three times. Then it was not the cover you were reading. M.
  - → *(Why did I tell him that?)*


### editore_a2 · A

*Se scrive Sara:*

> **Sara:** Is it true you published that novel everyone wanted banned? Joanie told me.  

**Pezzo 1**

> **Magnus:** I have published four of them. Each time the critics were outraged and each time the book sold out in a week.  
> **Magnus:** People condemn in public what they read in bed. M.  

Scelte di Sara:
- «Did it ever make you feel guilty?»
  - → **Magnus:** Guilt is for people who don't believe in what they do. I always did. M.
- «I'd love to read one.» — *calda, flag magnus_libro_regalo*
  - → **Magnus:** I will have a copy sent to you. Read it slowly. Not on the train. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** A book is controversial only when it says aloud what everyone thinks in silence. Remember that when you write. M.  

### editore_a3 · A

*Se scrive Sara:*

> **Sara:** Do you have any advice? I only manage to write on weekends.  

**Pezzo 1**

> **Magnus:** Write every day. Three lines, if that is all you have. A writer is a muscle, not a mood.  
> **Magnus:** Let us begin now. Describe, in three lines, the moment you knew you wanted to write. M.  

Scelte di Sara:
- (Shy) «I was eleven. I wrote a poem for my mother. She corrected the spelling.»
  - → **Magnus:** Honest, and sad. Your mother corrected the spelling and missed the poem. M.
- (Sensory) «The smell of a new notebook. The pen scratching. The house asleep around me.» — *Conf +1*
  - → **Magnus:** Better. Now I am in the room with you. M.
- (Bold) «When I realised I could say things on paper I'd never dare say aloud.» — *richiede confidence=30, calda*
  - → **Magnus:** There she is. That is the writer I want to read. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** Three lines a day. Send them to me if you wish. I will not correct the spelling. M.  
> *(Three lines a day. I can do that.)*  

### editore_a4 · A

*Se scrive Sara:*

> **Sara:** Do you prefer books or films? Daniel says you hate cinema.  

**Pezzo 1**

> **Magnus:** Daniel exaggerates everything except his own virtues, which he understates by a small margin.  
> **Magnus:** I love cinema. But a film shows you a woman. A book makes you become her. M.  

Scelte di Sara:
- «That's beautiful.» — *calda*
  - → **Magnus:** It is merely true. Beauty is a side effect. M.
- «I still like films better on a Friday night.»
  - → **Magnus:** Friday nights are for being lazy. I approve. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** Which woman would you like to become, if you could choose any book? M.  

Scelte di Sara:
- «Someone brave.»
  - → **Magnus:** Bravery is the most overrated quality in fiction and the most underrated in life. M.
- «Someone who doesn't apologise.» — *richiede confidence=25, calda*
  - → **Magnus:** Then stop apologising in your chapters. Start there. M.


### editore_a5 · A

*Se scrive Sara:*

> **Sara:** Your assistant said you're travelling. Somewhere interesting?  

**Pezzo 1**

> **Magnus:** An old city by the sea, for a book fair. Dull meetings by day. By night, a library that has not changed in three centuries.  
> **Magnus:** I sat there until they closed the doors. The silence of old paper is the best company I know. M.  

Scelte di Sara:
- «I envy you.»
  - → **Magnus:** Envy is a good start. It tells you what you want. M.
- «Take me with you next time. Joking.» — *richiede confidence=25, calda*
  - → **Magnus:** I never joke about libraries. M.
  - → *(He didn't say no.)*


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** Travel is where we discover that our ordinary life was a choice, not a destiny. M.  

### editore_a6 · A

*Se scrive Sara:*

> **Sara:** Daniel says your house is full of first editions. Is it a museum?  

**Pezzo 1**

> **Magnus:** Not a museum. A collection. A museum is for the public. A collection is private, and much more honest.  
> **Magnus:** I collect first editions, letters, photographs. Things that remember someone. M.  

Scelte di Sara:
- «Photographs of what?» — *flag magnus_collezione_foto*
  - → **Magnus:** Of moments that deserved to stay. Perhaps one day I will show you. M.
  - → *(Why does that sentence give me a shiver?)*
- «I'd love to see the books.» — *calda*
  - → **Magnus:** You will. Everyone I respect eventually does. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** Every collector is a little in love with what he keeps. Remember that, if you ever become part of someone's collection. M.  
> *(What a strange thing to say.)*  

### editore_a7 · A

*Se scrive Sara:*

> **Sara:** What's a normal day for a publisher? I imagine you reading in an armchair all day.  

**Pezzo 1**

> **Magnus:** Mornings: lawyers, printers, bankers. Afternoons: authors, who are worse.  
> **Magnus:** The armchair comes at night. It is the only part of the day that belongs to me. M.  

Scelte di Sara:
- «And what do you read at night?» — *calda*
  - → **Magnus:** Lately, fifty pages by a young woman who is afraid of her own talent. M.
- «It sounds exhausting.»
  - → **Magnus:** It is. That is why I chose it. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** Most manuscripts I reject in a page. A few I keep for a lifetime. The difference is never technique. It is courage. M.  

### editore_a8 · A

*Se scrive Sara:*

> **Sara:** I wrote my three lines every day this week. Is that a good start?  

**Pezzo 1**

> **Magnus:** It is the only start. Now, an exercise. Describe a room you know well, but through a single sense. Not sight. M.  

Scelte di Sara:
- (Shy) «My kitchen. The fridge humming. The clock. Nothing else.»
  - → **Magnus:** Correct and lonely. The loneliness is the interesting part. M.
- (Sensory) «The bathroom after a shower. Warm air, wet tiles under my feet, the mirror misted over.» — *Conf +1*
  - → **Magnus:** Touch. You chose touch. Interesting. M.
- (Bold) «My bedroom at night. The sheets, his breathing, and me awake, wanting something I can't name.» — *richiede confidence=30, calda, flag magnus_prima_riga*
  - → **Magnus:** That, Sara, is a first line. Keep it. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** You have talent. Not the decorative kind. The dangerous kind. It will ask things of you. M.  
> *(The dangerous kind.)*  

Scelte di Sara:
- «What kind of things?» — *calda*
  - → **Magnus:** Honesty, mostly. The rest follows. M.
- «Thank you. Really.»
  - → **Magnus:** Don't thank me. Write. M.


### editore_b1 · B

*Se scrive Sara:*

> **Sara:** Daniel says you never married. Was it a choice?  

**Pezzo 1**

> **Magnus:** Absolutely. Marriage asks a man to love one book forever. I have always preferred a library.  
> **Magnus:** I have loved many women. None of them ever regretted it, I believe. Several still dine with me. M.  

Scelte di Sara:
- «Several? At the same table?» — *calda, flag magnus_cerchia_accenno*
  - → **Magnus:** Often. They get along beautifully. Jealousy is a lack of imagination. M.
- «That sounds lonely, in the end.»
  - → **Magnus:** You would be surprised how rarely I am alone. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** And you, Sara. One man, forever. Is that what you want, or what you were told to want? M.  
> *(Nobody has ever asked me that.)*  

Scelte di Sara:
- «It's what I want.» — *Josh +1*
  - → **Magnus:** Then I am glad for you. Truly. M.
- «I've never asked myself.» — *calda*
  - → **Magnus:** Then do. Writers must ask the questions no one else will. M.


### editore_b2 · B

*Se scrive Sara:*

> **Sara:** I read what I wrote today and I wanted to delete everything. Does that happen to you?  

**Pezzo 1**

> **Magnus:** It happens to everyone worth reading. The day it stops happening, worry.  
> **Magnus:** Tell me the sentence you wanted to delete most. Exactly as you wrote it. M.  

Scelte di Sara:
- (Shy) «She looked at him and smiled.»
  - → **Magnus:** Delete it. You were right. It is a sentence that wants to be invisible. M.
- (Sensory) «She could feel his eyes on her neck before she turned.» — *Conf +1*
  - → **Magnus:** Keep it. Why did you want to delete it? Because it is true? M.
- (Bold) «She didn't want him to stop, and she hated herself for it.» — *richiede confidence=35, calda*
  - → **Magnus:** You wanted to delete the only sentence that is alive. Don't you dare. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** Your fear is not that you are bad. Your fear is that you are good at something you were taught to be ashamed of. M.  
> *(He sees everything.)*  

### editore_b3 · B

*Se scrive Sara:*

> **Sara:** Do you ever feel old, Magnus? You never seem to.  

**Pezzo 1**

> **Magnus:** I feel old every morning and young every evening. At my age beauty is no longer something I have. It is something I recognise.  
> **Magnus:** Recognising it is a far rarer skill. Most men only possess. M.  

Scelte di Sara:
- «What do you recognise?» — *calda*
  - → **Magnus:** The moment a woman stops performing and becomes herself. It is brief. It is unforgettable. M.
- «You're wiser than most men half your age.»
  - → **Magnus:** That is not a high bar, I'm afraid. But thank you. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** I saw that moment in you, once, at Daniel's party. For about four seconds. M.  
> *(Four seconds. When?)*  

Scelte di Sara:
- «When?» — *calda*
  - → **Magnus:** When you laughed at something you should not have found funny. M.
- «I think you're flattering me.»
  - → **Magnus:** I am too old to flatter. It wastes time I no longer have. M.


### editore_b4 · B

*Se scrive Sara:*

> **Sara:** Give me another exercise. A hard one.  

**Pezzo 1**

> **Magnus:** As you wish. Describe a kiss without using the word «kiss». Four lines at most. M.  

Scelte di Sara:
- (Shy) «Their lips touched. It was soft. Then it was over. She smiled.»
  - → **Magnus:** You described a postcard. Try again, one day, when no one is watching. M.
- (Sensory) «His breath first. Warm, slow. Then the taste of wine. She forgot the room.» — *Conf +1*
  - → **Magnus:** She forgot the room. Good. Now make her forget her name. M.
- (Bold) «She meant to pull away. Her hands didn't. His mouth asked a question and her body answered before she could.» — *richiede confidence=40, calda, Corr +1, flag magnus_bacio_scritto*
  - → **Magnus:** Sara. That is publishable. You have just written the first honest page of your career. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** Words can do to a reader what hands do to a body. Few writers dare to use them that way. M.  
> *(I wrote that. Me.)*  

### editore_b5 · B

*Se scrive Sara:*

> **Sara:** Can I tell you something? You're the only person who reads me without wanting me to be different.  

**Pezzo 1**

> **Magnus:** Then everyone else in your life is wasting a remarkable opportunity.  
> **Magnus:** Does [nome_compagno] read you? M.  

Scelte di Sara:
- «He tries. He's not a reader.»
  - → **Magnus:** Trying is generous. It is also not the same thing. M.
- «He loves me. That's different.» — *Josh +1*
  - → **Magnus:** It is different. Whether it is enough is a question only you can answer. M.


`— punto di interruzione —`

**Pezzo 2**

> **Magnus:** To be understood is the rarest pleasure. Rarer than love. Rarer than desire. I offer it freely, and ask only honesty in return. M.  
> *(Only honesty. That sounds easy. It isn't.)*  

Scelte di Sara:
- «Then I'll be honest with you.» — *calda*
  - → **Magnus:** I know. You already are, on the page. M.
- «Good night, Magnus.»
  - → **Magnus:** Good night, Sara. Write three lines before you sleep. M.



## Barbara

### capa_intro · Introduzione

*Se scrive Sara:*

> **Sara:** Barbara, it's Sara. The extra piece is finished. I sent it to your inbox.  

**Pezzo 1**

> **Barbara:** I know, darling. I read it in the lift.  
> **Barbara:** Paragraph four is limp. LIMP. Fix it tonight and send it back by eight tomorrow.  
> *(Tonight. Of course tonight.)*  

Scelte di Sara:
- «Of course. I'll fix it.»
  - → **Barbara:** Good girl.
- «Can it wait until tomorrow morning?» — *Conf +1*
  - → **Barbara:** Hm. Tomorrow at nine, on my desk. Not nine-oh-one.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** The rest is good. Better than good. Don't let it go to your head.  
> **Barbara:** And Sara. That blue blouse today. Finally something with a neckline. Keep going in that direction.  
> *(She noticed my blouse. Of course she did.)*  

Scelte di Sara:
- «Thank you... I think.»
  - → **Barbara:** It was a compliment, darling. I don't give many.
- «I'll dress as I like, but thanks.» — *Conf +1*
  - → **Barbara:** Of course you will. For now.


### capa_a1 · A

*Se scrive Sara:*

> **Sara:** Barbara, quick question about Friday's deadline. Is it Friday morning or Friday night?  

**Pezzo 1**

> **Barbara:** Friday morning. Friday night is for people with no ambition.  
> **Barbara:** Are you going to be late?  

Scelte di Sara:
- «No. It'll be there.» — *calda*
  - → **Barbara:** That's what I like to hear. Short. Certain.
- «I might need a few more hours.»
  - → **Barbara:** You have until ten. Not because you asked. Because I'm generous today.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** Jessica used to be late every week. Now she's early every week. People change when they want to please me.  
> *(Jessica did change. A lot.)*  

Scelte di Sara:
- «I'm not late. I'm thorough.» — *Conf +1*
  - → **Barbara:** Thorough. Cute word. Be thorough by Friday morning.
- «I'll do my best.»
  - → **Barbara:** Your best is the minimum, darling.


### capa_a2 · A

*Se scrive Sara:*

> **Sara:** Can I ask you something? Why did you buy a newspaper? Everyone says print is dying.  

**Pezzo 1**

> **Barbara:** Everyone says. Everyone is boring.  
> **Barbara:** A newspaper is a stage, darling. Whoever owns the stage decides who gets the light.  

Scelte di Sara:
- «And who gets the light?» — *calda*
  - → **Barbara:** Whoever deserves it. And whoever I decide deserves it. Not always the same thing.
- «I thought it was about the news.»
  - → **Barbara:** Oh, sweet thing. Nothing is ever about the news.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** You could have the light one day. If you stop hiding behind other people's stories.  
> *(Is she encouraging me? Barbara?)*  

Scelte di Sara:
- «I'd like that.» — *calda*
  - → **Barbara:** I know you would. I can always tell what my girls want.
- «I'm happy where I am.»
  - → **Barbara:** Nobody is happy where they are. They're just scared to move.


### capa_a3 · A

*Se scrive Sara:*

> **Sara:** Barbara, the dress code for Thursday's meeting with the sponsors. Formal?  

**Pezzo 1**

> **Barbara:** Formal is for funerals. Elegant. Memorable.  
> **Barbara:** Tomorrow, wear the green blouse. The one with the low neckline. Not the grey thing you hide in.  
> *(How does she even know what's in my wardrobe?)*  

Scelte di Sara:
- «Ok. The green one.» — *Interest "capa", 1, flag barbara_ordine_camicetta*
  - → **Barbara:** Good girl. You'll thank me.
- «Yes, ma'am. Shall I salute too? :)»
  - → **Barbara:** Ha! Cheeky. Wear the blouse and salute, then.
- «I'll choose my clothes myself, Barbara.» — *Conf +1*
  - → **Barbara:** Of course, darling. Of course.
  - → **Barbara:** We'll talk about it again.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** Style is not what you wear. It's how much you let people look.  

### capa_a4 · A

*Se scrive Sara:*

> **Sara:** Roberta says you had a word with the photographer about my picture for the byline?  

**Pezzo 1**

> **Barbara:** I did. You looked like a nun on holiday.  
> **Barbara:** We're reshooting Monday. Darker lipstick. Burgundy. You have the lips for it, you just don't use them.  

Scelte di Sara:
- «Burgundy. Ok, I'll get one.» — *Interest "capa", 1, flag barbara_ordine_rossetto*
  - → **Barbara:** I'll have one sent to your desk. Mine. I know the exact shade.
- «A nun on holiday? Thanks a lot :)»
  - → **Barbara:** A pretty nun. But still a nun.
- «I'd rather keep my usual look.» — *Conf +1*
  - → **Barbara:** Your usual look is invisible, darling. But fine. For now.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** All my girls wear a little more colour after a few months. Haven't you noticed?  
> *(Jessica. Roberta. All of them, now that she says it.)*  

### capa_a5 · A

*Se scrive Sara:*

> **Sara:** Is Jessica ok? She seemed... different, this week. Very calm.  

**Pezzo 1**

> **Barbara:** Jessica is perfect. She finally found her place.  
> **Barbara:** When she started she was a mess. Anxious, sloppy. Now look at her. Serene.  
> *(Serene. That's one word for it.)*  

Scelte di Sara:
- «What happened to her?» — *flag barbara_jessica_accenno*
  - → **Barbara:** She listened to me, darling. That's all. It's very simple, listening.
- «She does seem happier.» — *calda*
  - → **Barbara:** They all are. Eventually.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** Roberta was the same. Now she'd do anything for this paper. For me.  
> **Barbara:** You'll see. You're at the beginning.  

### capa_a6 · A

*Se scrive Sara:*

> **Sara:** I saw your photo in the society pages. The gala. You looked amazing.  

**Pezzo 1**

> **Barbara:** Of course I did, darling. Leopard and champagne. A classic.  
> **Barbara:** Those galas are where the real work happens. Contracts, favours, secrets.  

Scelte di Sara:
- «It sounds exhausting.»
  - → **Barbara:** Exhausting for the boring. For me it's oxygen.
- «I've never been to anything like that.» — *calda, flag barbara_gala_invito*
  - → **Barbara:** Then one day I'll take you. As my guest. In something red.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** I always bring one of my girls. Last time it was Jessica. She didn't leave my side all night.  
> *(Why does she say «my girls» like that?)*  

### capa_a7 · A

*Se scrive Sara:*

> **Sara:** Why only women in the newsroom? Did you plan it?  

**Pezzo 1**

> **Barbara:** Women work harder, complain less and lie better. All excellent qualities in a journalist.  
> **Barbara:** Men were a distraction. For them, mostly.  

Scelte di Sara:
- «That's a bit unfair to men.»
  - → **Barbara:** Life is unfair to men all the time, darling. They just never notice.
- «Lie better? Really?» — *calda*
  - → **Barbara:** Oh yes. Ask any woman who's been married.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** Women understand women. We know what we need before we say it. Men need a manual.  
> *(She's not entirely wrong.)*  

### capa_a8 · A

*Se scrive Sara:*

> **Sara:** Barbara, do you think I could have my own column one day?  

**Pezzo 1**

> **Barbara:** Bold. I like it.  
> **Barbara:** Yes. One day. When you stop writing as if you were apologising for taking up space.  

Scelte di Sara:
- «How do I stop?» — *calda*
  - → **Barbara:** You let someone teach you. Someone who knows what you could be.
- «I'll work on it.»
  - → **Barbara:** Work on it with me. Alone you'll take ten years.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** Ambition is very attractive on a woman, Sara. Remember that.  

### capa_b1 · B

*Se scrive Sara:*

> **Sara:** Can I ask you something personal? Were you ever married?  

**Pezzo 1**

> **Barbara:** Once. Eleven years. He was handsome, charming and absolutely useless.  
> **Barbara:** He promised me everything and gave me a cheap affair with his secretary. A cliché, darling. He couldn't even betray me with style.  

Scelte di Sara:
- «I'm sorry, Barbara.» — *calda*
  - → **Barbara:** Don't be. It was the best thing that ever happened to me.
- «That must have been terrible.»
  - → **Barbara:** For six months. Then it was liberating.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** Since then I keep only people around me who adore me. Life is too short for anything less.  
> *(Who adore her. Not who love her. Adore.)*  

### capa_b2 · B

*Se scrive Sara:*

> **Sara:** Do you ever get lonely? You seem so... complete. On your own.  

**Pezzo 1**

> **Barbara:** Lonely? Darling, I'm never alone. I'm independent. There's a difference.  
> **Barbara:** An independent woman chooses her company. She doesn't wait for it.  

Scelte di Sara:
- «I wish I were more like that.» — *calda*
  - → **Barbara:** You could be. You just need the right example.
- «I like waiting for [nome_compagno] at home, though.» — *Josh +1*
  - → **Barbara:** Of course you do. How sweet. How very... domestic.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** Women spend their lives waiting for men to decide things. I decided to stop. The view is much better from here.  

### capa_b3 · B

*Se scrive Sara:*

> **Sara:** I wore the outfit you suggested. Everyone looked at me differently today.  

*Se scrive lui/lei:*

> **Barbara:** Sara. Tomorrow is the interview with the councillor. I want you to make an impression.  
> **Sara:** What do you suggest?  

**Pezzo 1**

> **Barbara:** Of course they did. That's the point. A woman who is seen is a woman who is listened to.  
> **Barbara:** Tomorrow: the black dress. Low neckline. No cardigan. I want to see you, not your shyness.  
> *(No cardigan. She always says that.)*  

Scelte di Sara:
- «Ok. The black dress.» — *Interest "capa", 1, flag barbara_ordine_scollatura*
  - → **Barbara:** Good girl. I'll be waiting at the door to check.
- «And if I get cold? :)»
  - → **Barbara:** Then you'll shiver elegantly.
- «I'll wear what I'm comfortable in.» — *Conf +1*
  - → **Barbara:** Comfortable. Yes. Comfortable is lovely.
  - → **Barbara:** Think about it overnight anyway.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** Your body is an asset, darling. You've been hiding it like a debt.  

### capa_b4 · B

*Se scrive Sara:*

> **Sara:** Can I trust you with something? It's about work. And not.  

**Pezzo 1**

> **Barbara:** Of course you can. Everything stays between us. Between us women.  
> **Barbara:** Tell me.  

Scelte di Sara:
- «Sometimes I feel invisible. At work, at home.» — *calda, flag barbara_confidenza_invisibile*
  - → **Barbara:** Not to me. I see you, Sara. I've seen you from the first day.
- «Never mind. It's silly.»
  - → **Barbara:** Nothing you say is silly to me, darling. Whenever you're ready.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** Men listen to answer. Women listen to understand. And I listen to keep.  
> *(To keep? Keep what?)*  

### capa_b5 · B

*Se scrive Sara:*

> **Sara:** Barbara, honestly. What do you think of me? Not as a journalist.  

**Pezzo 1**

> **Barbara:** Honestly? I think you're a beautiful woman who was taught to say sorry for it.  
> **Barbara:** I think you're wasted. On that desk, on that grey wardrobe. Maybe on other things.  
> *(On other things. She means [nome_compagno].)*  

Scelte di Sara:
- «I'm not wasted. I'm happy.» — *Josh +1*
  - → **Barbara:** Of course you are, darling. Of course.
- «...Maybe you're right.» — *calda*
  - → **Barbara:** I'm always right about my girls.


`— punto di interruzione —`

**Pezzo 2**

> **Barbara:** Stay close to me, Sara. I can make you into something extraordinary. If you let me.  
> *(If I let her. What does that even mean?)*  


## Jacob

### ex_intro · Introduzione

*Se scrive Sara:*

> **Sara:** It was strange seeing you at the bar.  

**Pezzo 1**

> **Jacob:** strange good or strange bad  

Scelte di Sara:
- «Just strange.»
  - → **Jacob:** fair. four years is a long time
- «Strange good. I think.» — *calda*
  - → **Jacob:** i'll take «i think». it's more than i expected


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** you look good sara. happy. it suits you  
> **Jacob:** is he good to you?  
> *(Why does he care?)*  

Scelte di Sara:
- «Very. [nome_compagno] is wonderful.» — *Josh +1*
  - → **Jacob:** good. you deserve wonderful
- «He's good. Goodnight, Jacob.»
  - → **Jacob:** goodnight sara


### ex_a1 · A

*Se scrive Sara:*

> **Sara:** Do you still see anyone from the old group?  

**Pezzo 1**

> **Jacob:** tony and the twins come to the bar every friday  
> **Jacob:** lucy got married. to a vet. she's unbearable now. very happy and unbearable  

Scelte di Sara:
- «Lucy married? No way!» — *calda*
  - → **Jacob:** way. three kids. she sends me christmas cards. with all three in matching sweaters
- «I lost touch with all of them.»
  - → **Jacob:** they ask about you. all the time


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** come on a friday. they'd go crazy to see you  

Scelte di Sara:
- «Maybe. With [nome_compagno].»
  - → **Jacob:** sure. bring him
- «That would be fun.» — *calda*
  - → **Jacob:** it would. like old times


### ex_a2 · A

*Se scrive Sara:*

> **Sara:** I was thinking about the time we got lost driving to the coast. Seven hours for a two-hour trip.  

*Se scrive lui/lei:*

> **Jacob:** remember the time we got locked out of the hostel in the rain  
> **Sara:** Oh no. Don't remind me.  

**Pezzo 1**

> **Jacob:** haha you refused to look at the map because «the sun is in the west»  
> **Jacob:** the sun was not in the west  

Scelte di Sara:
- «It was a cloudy day! Not my fault.» — *calda*
  - → **Jacob:** you still say that. four years later. incredible
- «We were so young and stupid.»
  - → **Jacob:** young yes. stupid only you


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** best trip of my life though. honestly  
> *(Mine too. I'm not telling him that.)*  

### ex_a3 · A

*Se scrive Sara:*

> **Sara:** They played that song on the radio today. You know which one.  

**Pezzo 1**

> **Jacob:** the one from the concert in the park?  
> **Jacob:** you sang it so badly a guy asked you to stop  

Scelte di Sara:
- «I sang beautifully. He was jealous.» — *calda*
  - → **Jacob:** he was something. jealous wasn't it
- «I'd forgotten that.»
  - → **Jacob:** i didn't


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** i still have the playlist we made. never deleted it  
> *(He kept it. Four years.)*  

### ex_a4 · A

*Se scrive Sara:*

> **Sara:** So you own a bar now. Since when?  

**Pezzo 1**

> **Jacob:** two years. remember the place where we met? the one with the broken jukebox  
> **Jacob:** it closed. i bought the jukebox. it's in my bar now. still broken  

Scelte di Sara:
- «You bought the jukebox?!» — *calda*
  - → **Jacob:** had to. some things you don't let go
- «That's very sentimental of you.»
  - → **Jacob:** don't tell anyone. i have a reputation


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** come see it. it only plays one song. guess which  

Scelte di Sara:
- «I can guess.»
  - → **Jacob:** yeah. you can
- «Don't tell me. I'll come and hear it.» — *calda, flag jacob_jukebox*
  - → **Jacob:** deal


### ex_a5 · A

*Se scrive Sara:*

> **Sara:** You've changed. More... sure of yourself. If that's even possible.  

**Pezzo 1**

> **Jacob:** haha. you've changed too  
> **Jacob:** you used to hide behind your hair when you laughed. you don't anymore  

Scelte di Sara:
- «I grew up.»
  - → **Jacob:** you did
- «You noticed that?» — *calda*
  - → **Jacob:** i notice everything about you. always did
  - → *(That shouldn't make me feel anything.)*


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** i'm the same though. just with a bar and better shoes  

### ex_a6 · A

*Se scrive Sara:*

> **Sara:** Where do you go on holiday now? Still the islands?  

**Pezzo 1**

> **Jacob:** every august. same beach. same little hotel with the blue doors  
> **Jacob:** the old lady still asks where the girl with the big hat is  

Scelte di Sara:
- «She remembers me?» — *calda*
  - → **Jacob:** everyone remembers you sara
- «Tell her I'm fine.»
  - → **Jacob:** i'll tell her you're married to a nice guy. she'll be disappointed


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** best sunsets in the world. you used to fall asleep before they ended  

### ex_a7 · A

*Se scrive Sara:*

> **Sara:** So, what's your life like now? Apart from the bar.  

**Pezzo 1**

> **Jacob:** bar till 3. gym. sleep. repeat. no complaints  
> **Jacob:** and you? still writing?  

Scelte di Sara:
- «Still writing. A novel, maybe.» — *calda*
  - → **Jacob:** knew it. you always had a notebook. even at the beach
- «I work at a newspaper now. Real job.»
  - → **Jacob:** real job. look at you


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** and him? what does he do  

Scelte di Sara:
- «He works in an office. He's great at it.» — *Josh +1*
  - → **Jacob:** office. good. stable
- «Office stuff. Long hours.»
  - → **Jacob:** long hours. so you're alone a lot
  - → *(That's not what I said. Is it?)*


### ex_a8 · A

*Se scrive Sara:*

> **Sara:** Do you ever miss being twenty-five?  

**Pezzo 1**

> **Jacob:** every day. nothing mattered and everything mattered  
> **Jacob:** you?  

Scelte di Sara:
- «Sometimes. Life was simpler.»
  - → **Jacob:** simpler. and louder
- «I miss how alive everything felt.» — *calda*
  - → **Jacob:** yeah. i know exactly what you mean


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** we were good at being young sara. really good  
> *(We were.)*  

### ex_b1 · B

*Se scrive Sara:*

> **Sara:** I found an old photo of us today. At the lake.  

*Se scrive lui/lei:*

> **Jacob:** can't sleep. thinking about the lake  
> **Sara:** The lake? Why?  

**Pezzo 1**

> **Jacob:** the lake weekend  
> **Jacob:** you remember. the cabin with no curtains  
> *(I remember. I remember all of it.)*  

Scelte di Sara:
- «I remember :)» — *calda, flag jacob_lago*
  - → **Jacob:** good. i didn't want to be the only one
- (Let it drop.) «The lake was beautiful.»
  - → **Jacob:** it was. among other things
- «Jacob. Don't.» — *freno*
  - → **Jacob:** ok ok. sorry. goodnight


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** best weekend of my life. not even close  

### ex_b2 · B

*Se scrive Sara:*

> **Sara:** Do you ever think about why it ended?  

**Pezzo 1**

> **Jacob:** you left. that's why it ended  
> **Jacob:** nobody ever left me before. you were the first  
> *(That's what he remembers. That I left. Not why.)*  

Scelte di Sara:
- «I left because you gave me a reason.» — *Conf +1*
  - → **Jacob:** yeah yeah. i know
- «It still hurts, you know.» — *calda*
  - → **Jacob:** for me too. more than you think


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** you were the only one who could walk away from me. i respected that. still do  

### ex_b3 · B

*Se scrive Sara:*

> **Sara:** Can we talk about it? What you did. I never heard your side.  

**Pezzo 1**

> **Jacob:** my side. ok  
> **Jacob:** it was one night. it meant nothing. i was stupid and she was there  
> **Jacob:** you found out and you were gone in an hour. you didn't even shout  

Scelte di Sara:
- «Are you sorry?»
  - → **Jacob:** i'm sorry you found out like that
  - → *(Not «I'm sorry I did it». Never that.)*
- «It meant something to me.»
  - → **Jacob:** i know. i know it did
  - → **Jacob:** but you have to admit, leaving without a word was brutal too


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** anyway. old story. we're different people now  
> *(He's not different. Not about this.)*  

Scelte di Sara:
- «Some things don't change, Jacob.» — *Conf +1*
  - → **Jacob:** maybe. maybe some things shouldn't
- «You're right. Old story.» — *calda*
  - → **Jacob:** exactly. glad we cleared it up


### ex_b4 · B

*Se scrive Sara:*

> **Sara:** What do you miss about us? Honestly.  

*Se scrive lui/lei:*

> **Jacob:** you know what i miss?  
> **Sara:** What?  

**Pezzo 1**

> **Jacob:** the way you laughed in the morning. half asleep. hair everywhere  
> **Jacob:** and the way you never wanted to get out of bed on sundays. we didn't, either  

Scelte di Sara:
- «Those Sundays... :)» — *calda*
  - → **Jacob:** yeah. those sundays
  - → *(I shouldn't be smiling at my phone like this.)*
- (Let it drop.) «I'm a morning person now.»
  - → **Jacob:** liar
- «Jacob. Don't.» — *freno*
  - → **Jacob:** ok. you asked though


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** and you? you miss anything?  

Scelte di Sara:
- «No. I have everything I need.» — *Josh +1*
  - → **Jacob:** good. that's good
- «...Some things.» — *calda, flag jacob_le_manca_qualcosa*
  - → **Jacob:** i knew it


### ex_b5 · B

*Se scrive Sara:*

> **Sara:** Is it weird that talking to you feels so normal?  

**Pezzo 1**

> **Jacob:** not weird. we were always easy together  
> **Jacob:** is it easy with him? like this?  
> *(It's different. It's... careful.)*  

Scelte di Sara:
- «It's different. It's real.» — *Josh +1*
  - → **Jacob:** real. ok
- «It's different. Quieter.» — *calda*
  - → **Jacob:** quieter. you used to hate quiet


`— punto di interruzione —`

**Pezzo 2**

> **Jacob:** we were fire sara. fire burns out but it's never boring  
> **Jacob:** goodnight  
> *(Fire. And then nothing left. I remember that part too.)*  


## Joanie

### amica_intro · Introduzione

*Se scrive Sara:*

> **Sara:** Are you awake? I'm bored.  

*Se scrive lui/lei:*

> **Joanie:** BORED. ENTERTAIN ME.  
> **Sara:** Ha. Same here.  

**Pezzo 1**

> **Joanie:** omg yes. Mark is watching football and I'm dying  
> **Joanie:** tell me something. anything. gossip, drama, a crime  

Scelte di Sara:
- «Nothing happens in my life, you know that.»
  - → **Joanie:** LIES. something always happens. you just don't tell me
- «My boss told me to wear a lower neckline.» — *calda*
  - → **Joanie:** BARBARA?? I love her. and she's right, sorry


`— punto di interruzione —`

**Pezzo 2**

> **Joanie:** ok I have to go, Mark scored. I mean his team. whatever  
> **Joanie:** love you babe. sleep well  

Scelte di Sara:
- «Love you too.» — *calda*
- «Night!»


### amica_a1 · A

*Se scrive Sara:*

> **Sara:** My legs are dead. Why did I let you sign me up for the gym?  

**Pezzo 1**

> **Joanie:** because you love me. and because of the view ;)  
*[if percorso("simon").interest >= 5]*  
> **Joanie:** also. Simon. talks about you. like, a lot  
> **Joanie:** «Sara's squat is getting really good». HIS WORDS  
> *(He talks about my squat with Joanie?)*  
*[else]*  
> **Joanie:** Simon asked where you were last time. just saying  

Scelte di Sara:
- «He's my trainer, Joanie. Stop.»
  - → **Joanie:** a trainer with ARMS. I'm just pointing out facts
- «...He did?» — *calda, Interest "simon", 1*
  - → **Joanie:** HE DID. ok I'm screaming


`— punto di interruzione —`

**Pezzo 2**

> **Joanie:** Thursday. you and me. no excuses. wear the black leggings  

### amica_a2 · A

*Se scrive Sara:*

> **Sara:** I need a dress for Saturday and everything I own is beige.  

**Pezzo 1**

> **Joanie:** FINALLY. I've been waiting years for this message  
> **Joanie:** tomorrow after work. the mall. I'm choosing. you're not allowed to say «too short»  

Scelte di Sara:
- «Within reason.»
  - → **Joanie:** reason is beige. no reason
- «Fine. You choose.» — *calda, Corr +1, flag joanie_sceglie_vestito*
  - → **Joanie:** best. day. ever


`— punto di interruzione —`

**Pezzo 2**

> **Joanie:** you have the body of a goddess and you dress like a librarian. it's a crime  
> *(A goddess. Joanie always exaggerates.)*  

### amica_a3 · A

*Se scrive Sara:*

> **Sara:** How are things with Mark?  

**Pezzo 1**

> **Joanie:** good! he's so sweet. he made me breakfast today. heart-shaped pancakes  
> **Joanie:** they looked like kidneys but the thought counts  

Scelte di Sara:
- «He's a keeper.» — *calda*
  - → **Joanie:** he is. he really is
- «[nome_compagno] has never made me pancakes.»
  - → **Joanie:** then [nome_compagno] has work to do


`— punto di interruzione —`

**Pezzo 2**

> **Joanie:** Mark's the best thing that happened to me. well. second best  
> **Sara:** What's the first?  
> **Joanie:** you, duh. best friend since forever  

### amica_a4 · A

*Se scrive Sara:*

> **Sara:** Ok, gossip. Roberta at work dyed her hair the same red as our boss.  

**Pezzo 1**

> **Joanie:** STOP. that's creepy. is it a cult? it sounds like a cult  
> *(She's joking. Isn't she?)*  
*[if ha_numero("daniel")]*  
> **Joanie:** also wait. I have better gossip. is Daniel texting you??  

Scelte di Sara:

*[else]*  

Scelte di Sara:


`— punto di interruzione —`

**Pezzo 2**

> **Joanie:** I live for your office drama. it's better than TV  

### amica_a5 · A

*Se scrive Sara:*

> **Sara:** What are you watching? I need a new series.  

**Pezzo 1**

> **Joanie:** the one with the married woman and the gardener. you'll LOVE it  
> **Joanie:** she's so bored and then... well. watch it  

Scelte di Sara:
- «Sounds a bit predictable.»
  - → **Joanie:** predictable and HOT. the best combination
- «I'll start it tonight.» — *calda, flag joanie_serie_giardiniere*
  - → **Joanie:** episode 3. trust me. watch it alone


`— punto di interruzione —`

**Pezzo 2**

> **Joanie:** Mark falls asleep in the first five minutes of anything. I watch everything alone. it's tragic  

### amica_a6 · A

*Se scrive Sara:*

> **Sara:** Honest opinion. The red top or the white one for tomorrow?  

**Pezzo 1**

> **Joanie:** red. always red. why is this even a question  
> **Joanie:** the white one makes you look like you're going to confession  

Scelte di Sara:
- «The red one is a bit much for the office.»
  - → **Joanie:** a bit much is the right amount
- «Red it is.» — *calda*
  - → **Joanie:** YES. send a photo tomorrow


`— punto di interruzione —`

**Pezzo 2**

> **Joanie:** seriously babe. you should dress for yourself. not for being invisible  

### amica_a7 · A

*Se scrive Sara:*

> **Sara:** Plans for the weekend?  

**Pezzo 1**

> **Joanie:** Saturday dinner with Mark's parents. pray for me  
> **Joanie:** Sunday free. brunch? you, me, mimosas  

Scelte di Sara:
- «Can't, Sunday is lunch with my parents.»
  - → **Joanie:** noooo. next week then. I'm writing it in blood
- «Brunch. Yes. Please.» — *calda*
  - → **Joanie:** bottomless mimosas. I'm booking


`— punto di interruzione —`

**Pezzo 2**

> **Joanie:** and bring gossip. I want everything  

### amica_a8 · A

*Se scrive Sara:*

> **Sara:** The washing machine flooded the bathroom. I want to cry.  

**Pezzo 1**

> **Joanie:** noooo. is [nome_compagno] home?  

Scelte di Sara:
- «He's on his way. He'll fix it.» — *Josh +1*
  - → **Joanie:** good. towels, babe. all the towels
- «Working late. As always.» — *calda*
  - → **Joanie:** ugh. as always. ok I'm calling you, stay on the phone with me while you mop


`— punto di interruzione —`

**Pezzo 2**

> **Joanie:** you know you can always call me. any hour. right?  
> **Sara:** I know.  

### amica_b1 · B

*Se scrive Sara:*

> **Sara:** Can I ask you something embarrassing?  

*Se scrive lui/lei:*

> **Joanie:** ok I need to know something. how are things with [nome_compagno]. REALLY  
> **Sara:** Fine. Good. Why?  

**Pezzo 1**

> **Joanie:** is it still exciting? like, after all these years?  
> *(I don't know how to answer that.)*  

Scelte di Sara:
- «It's comfortable. Safe. I like safe.»
  - → **Joanie:** safe is good. safe is... safe
- «Not like it used to be.» — *calda, Corr +1, flag joanie_sa_della_noia*
  - → **Joanie:** I KNEW IT. ok. we need to talk. seriously


`— punto di interruzione —`

**Pezzo 2**

> **Joanie:** listen. you deserve to feel wanted. like, really wanted. by someone who looks at you like you're on fire  
> **Joanie:** [nome_compagno] is lucky. someone is, anyway  
> *(What does she mean, «someone is»?)*  

### amica_b2 · B

*Se scrive Sara:*

> **Sara:** Do you think I'm boring? Be honest.  

**Pezzo 1**

> **Joanie:** WHAT. no. who told you that. I'll kill them  
> **Joanie:** you're the least boring person I know. you just hide it under seven layers of «sorry»  

Scelte di Sara:
- «I feel boring.»
  - → **Joanie:** feelings lie. I don't
- «You always make me feel better.» — *calda*
  - → **Joanie:** that's my job. my favourite job


`— punto di interruzione —`

**Pezzo 2**

*[if percorso("simon").interest >= 10 or percorso("daniel").interest >= 7]*  
> **Joanie:** and from what I see, some people don't find you boring AT ALL  
> **Sara:** Joanie...  
> **Joanie:** just saying ;)  
*[else]*  
> **Joanie:** you just need someone to remind you who you are. luckily you have me  

### amica_b3 · B

*Se scrive Sara:*

> **Sara:** Do you ever look in the mirror and not recognise yourself?  

**Pezzo 1**

> **Joanie:** every morning before coffee lol  
> **Joanie:** why? what did you see?  

Scelte di Sara:
- «Someone tired.»
  - → **Joanie:** then sleep more and let me do your makeup on saturday
- «Someone who wants to feel beautiful again.» — *calda*
  - → **Joanie:** babe. you ARE. you're the most beautiful woman I know. objectively. I've checked


`— punto di interruzione —`

**Pezzo 2**

> **Joanie:** sometimes I look at you and think, how does she not know  
> *(Know what? That I'm pretty? Joanie is sweet.)*  

### amica_b4 · B · condizione: `fatto('jacob_tornato')`

*Se scrive Sara:*

> **Sara:** I can't stop thinking about seeing Jacob again. Is that bad?  

*Se scrive lui/lei:*

> **Joanie:** so. JACOB. we need to talk about JACOB  
> **Sara:** There's nothing to talk about.  

**Pezzo 1**

> **Joanie:** girl. he looked at you like you were dessert  
> **Joanie:** and you looked at him like you hadn't eaten in four years  

Scelte di Sara:
- «He cheated on me, Joanie. Remember?» — *Conf +1*
  - → **Joanie:** I know, I know. people change though. maybe
- «...Was it that obvious?» — *calda, Interest "ex", 1*
  - → **Joanie:** the whole bar noticed. it was HOT


`— punto di interruzione —`

**Pezzo 2**

> **Joanie:** I'm not saying do anything. I'm saying it's ok to feel things. you're allowed  
> **Joanie:** and if you want to talk about it, I'm here. always. I'll never judge you  
> *(Why is she so happy he's back?)*  

### amica_b5 · B

*Se scrive Sara:*

> **Sara:** Sometimes I think my life is already decided. Job, [nome_compagno], house. Forever.  

**Pezzo 1**

> **Joanie:** is that bad? or good?  

Scelte di Sara:
- «Good. It's what I wanted.» — *Josh +1*
  - → **Joanie:** then I'm happy for you. really
- «I don't know anymore.» — *calda*
  - → **Joanie:** then it's not decided. nothing is decided until you say so


`— punto di interruzione —`

**Pezzo 2**

> **Joanie:** whatever you decide. whatever happens. I'm there. always. even if it's crazy  
> **Joanie:** especially if it's crazy  
> *(I don't know what I'd do without her.)*  


## Darius

### amico_intro · Introduzione

*Se scrive Sara:*

> **Sara:** Hey Darius, it's Sara. [nome_compagno]'s birthday is next month. Help me plan something?  

*Se scrive lui/lei:*

> **Darius:** Sara! Secret mission. [nome_compagno]'s birthday. You in?  
> **Sara:** Of course I'm in!  

**Pezzo 1**

> **Darius:** Yes!! Finally someone organised. Last year I forgot and he still brings it up lol  
> **Darius:** Ideas: surprise party, or the cabin trip he's been talking about since high school  

Scelte di Sara:
- «The cabin. He'd love that.» — *Josh +1*
  - → **Darius:** Cabin it is. I'll handle the boys, you handle him
- «A party. With everyone.» — *calda*
  - → **Darius:** Party! I'll bring the embarrassing photos. All of them

*[flag darius_compleanno_josh]*  

`— punto di interruzione —`

**Pezzo 2**

> **Darius:** He's lucky to have you, you know. Always says so  
> **Darius:** Ok, top secret from now on. Delete this chat lol  

### amico_a1 · A

*Se scrive Sara:*

> **Sara:** Who's the guy [nome_compagno] keeps calling «Big Phil»?  

**Pezzo 1**

> **Darius:** Lol. Phil. He's 1 metre 60. Hence Big Phil  
> **Darius:** High school. The three of us were inseparable. Phil, me and your man  

Scelte di Sara:
- «I need to meet this legend.» — *calda*
  - → **Darius:** You will. He does magic tricks. Badly. Prepare yourself
- «[nome_compagno] never told me about him.»
  - → **Darius:** Probably because of the prom story. Ask him about the prom. Watch his face


`— punto di interruzione —`

**Pezzo 2**

> **Darius:** We should all get together. Like a proper reunion. You'd fit right in  

### amico_a2 · A

*Se scrive Sara:*

> **Sara:** Ok, I asked [nome_compagno] about the prom. He turned red and left the room. Tell me.  

**Pezzo 1**

> **Darius:** LOL. He did the same face?? Classic  
> **Darius:** Ok. He rented a white suit. Spilled a whole cherry punch on it in the first ten minutes  
> **Darius:** He spent the night telling everyone it was «a design»  

Scelte di Sara:
- «Oh no. Poor thing :)» — *Josh +1*
  - → **Darius:** Poor thing danced all night anyway. That's your man
- «I'm going to tease him forever.» — *calda*
  - → **Darius:** Please do. I've been doing it alone for fifteen years


`— punto di interruzione —`

**Pezzo 2**

> **Darius:** He was the nicest guy in school. Still is. Don't tell him I said that  

### amico_a3 · A

*Se scrive Sara:*

> **Sara:** What was that band you and [nome_compagno] had in high school? He refuses to tell me.  

**Pezzo 1**

> **Darius:** Oh no. He told you about the band??  
> **Darius:** We were called «The Lost Socks». I was on drums. He sang. Terribly  

Scelte di Sara:
- «The Lost Socks! I'm dying.» — *calda*
  - → **Darius:** We had ONE fan. His mum
- «He sings in the shower. Still terribly.» — *Josh +1*
  - → **Darius:** Some things never change lol


`— punto di interruzione —`

**Pezzo 2**

> **Darius:** I might still have a recording. Price: one homemade dinner  

Scelte di Sara:
- «Deal. Come on Saturday.» — *calda, flag darius_cena_sabato*
  - → **Darius:** I'll bring the tape. And wine
- «I'll make [nome_compagno] cook. Deal.»
  - → **Darius:** Then I'm bringing antacids too lol


### amico_a4 · A

*Se scrive Sara:*

> **Sara:** Thanks for last night. [nome_compagno] was so happy. He laughed more than he has in weeks.  

**Pezzo 1**

> **Darius:** Anytime! He needs to get out more. Work is eating him alive  
> **Darius:** His boss sounds like a nightmare honestly  

Scelte di Sara:
- «He is. Daniel is awful to him.» — *Josh +1*
  - → **Darius:** I'd love five minutes alone with that guy. Just to talk. Mostly
- «He'll be fine. He's strong.»
  - → **Darius:** He is. Stronger than he looks. Always was


`— punto di interruzione —`

**Pezzo 2**

> **Darius:** Let's do it more often. The three of us. Board games, pizza, bad movies  

Scelte di Sara:
- «Every Friday?» — *calda*
  - → **Darius:** Every Friday. It's a tradition now. No backing out
- «When we can.»
  - → **Darius:** Deal


### amico_a5 · A

*Se scrive Sara:*

> **Sara:** What was [nome_compagno] like at sixteen?  

**Pezzo 1**

> **Darius:** Skinny. Glasses. Always reading comics. Too polite to tell a girl he liked her  
> **Darius:** Once he waited outside a girl's house for an hour with flowers and then went home. Didn't knock  

Scelte di Sara:
- «That's so sweet.» — *Josh +1*
  - → **Darius:** That's him. All heart, zero courage lol
- «He waited and didn't knock? Why?» — *calda*
  - → **Darius:** Said he «didn't want to bother her». I knocked for him next time
  - → *(Darius knocked for him.)*


`— punto di interruzione —`

**Pezzo 2**

> **Darius:** With you he finally found the courage. You changed him. For the better  

### amico_a6 · A

*Se scrive Sara:*

> **Sara:** Why did [nome_compagno] stay up until 3 playing with you? He was a zombie at breakfast.  

**Pezzo 1**

> **Darius:** Guilty lol. Online tournament. We came second!  
> **Darius:** Ok, eleventh. But it FELT like second  

Scelte di Sara:
- «Next time send him to bed at midnight.» — *Josh +1*
  - → **Darius:** Yes ma'am. I'll set an alarm
- «Teach me. I want to beat you both.» — *calda*
  - → **Darius:** Oh it's ON. Saturday. Bring snacks and your worst attitude


`— punto di interruzione —`

**Pezzo 2**

> **Darius:** He talks about you between rounds, you know. Embarrassing. Very sweet  

### amico_a7 · A

*Se scrive Sara:*

> **Sara:** Any plans this weekend?  

**Pezzo 1**

> **Darius:** Football Saturday. Sunday: fixing my bike, which I've been saying for six months  
> **Darius:** You two? Still the sofa marathon?  

Scelte di Sara:
- «Sofa marathon. Season four.»
  - → **Darius:** Respect. No spoilers
- «We need new plans. Ideas?» — *calda*
  - → **Darius:** Lake trail on Sunday. I'll bring the frisbee. [nome_compagno] can't catch, it's hilarious


`— punto di interruzione —`

**Pezzo 2**

> **Darius:** Seriously, call me whenever you two are bored. I'm always free. Sadly lol  

### amico_a8 · A

*Se scrive Sara:*

> **Sara:** Random question. Are you a morning person?  

**Pezzo 1**

> **Darius:** Gym at 6. Shower. Coffee. Work. I'm annoyingly organised  
> **Darius:** Unlike someone we both know who hits snooze five times  

Scelte di Sara:
- «Six times. I counted.» — *calda*
  - → **Darius:** SIX. I'm telling him you snitched
- «He's not a morning person. It's cute.» — *Josh +1*
  - → **Darius:** Cute is one word for it lol


`— punto di interruzione —`

**Pezzo 2**

> **Darius:** You're a morning person, right? You look like one. Up at dawn, tea, notebook  
> *(Exactly that. How does he know?)*  

### amico_b1 · B

*Se scrive Sara:*

> **Sara:** Can I ask you something serious? Is [nome_compagno] ok? He seems down lately.  

*Se scrive lui/lei:*

> **Darius:** Hey. Is [nome_compagno] ok? He was quiet at football  
> **Sara:** I was going to ask you the same thing.  

**Pezzo 1**

> **Darius:** It's work. That Daniel guy is getting into his head  
> **Darius:** He doesn't say it, but I know him. Fifteen years. He's my brother  

Scelte di Sara:
- «What can I do?» — *Josh +1*
  - → **Darius:** Just be there. He'd walk through fire for you. He needs to know you're behind him
- «I don't know how to help him.» — *calda*
  - → **Darius:** We'll figure it out. Together. That's what we do


`— punto di interruzione —`

**Pezzo 2**

> **Darius:** I'll take him out Thursday. Beers, darts, no talking about work  
> **Darius:** Whatever he needs. Always  

### amico_b2 · B

*Se scrive Sara:*

> **Sara:** You always look after everyone. Who looks after you?  

**Pezzo 1**

> **Darius:** ...Wow. Nobody's asked me that in a while  
> **Darius:** I'm fine. I like being the one who fixes things. Keeps my head busy  

Scelte di Sara:
- «You're allowed to need people too.» — *calda*
  - → **Darius:** Look at you, giving advice. [nome_compagno] said you were wise. He was right
- «Well, you have us.»
  - → **Darius:** I know. Best thing I've got


`— punto di interruzione —`

**Pezzo 2**

> **Darius:** Truth? My dad left when I was ten. I promised myself I'd never leave anyone. Never  
> *(I never knew that.)*  
*[flag darius_padre]*  

### amico_b3 · B

*Se scrive Sara:*

> **Sara:** How did the date go? [nome_compagno] said you had a date!  

**Pezzo 1**

> **Darius:** Lol. Disaster. She talked about her ex for two hours  
> **Darius:** Help me out. What do women actually want? Be honest  

Scelte di Sara:
- «Someone kind. Who listens.»
  - → **Darius:** Kind and listens. So, [nome_compagno]. Got it lol
- «Someone who makes them feel safe. And a bit dangerous.» — *richiede confidence=25, calda*
  - → **Darius:** Safe AND dangerous. That's a hard combo. Writing it down


`— punto di interruzione —`

**Pezzo 2**

> **Darius:** Thanks Sara. Seriously. If I find someone half as good as you, I'll be happy  
> **Darius:** [nome_compagno] won the lottery, I keep telling him  

### amico_b4 · B

*Se scrive Sara:*

> **Sara:** Do you miss how things were before I came along? You and [nome_compagno], every day.  

**Pezzo 1**

> **Darius:** Honestly? A little. But not in a bad way  
> **Darius:** He grew up. You're good for him. And I got a friend out of it too  

Scelte di Sara:
- «I'm glad you see me as a friend.» — *calda*
  - → **Darius:** Course I do. You're family now. Both of you
- «I never want to come between you two.» — *Josh +1*
  - → **Darius:** You never could. Nobody could


`— punto di interruzione —`

**Pezzo 2**

> **Darius:** Friendships change. The good ones get bigger, not smaller. That's ours  

### amico_b5 · B

*Se scrive Sara:*

> **Sara:** It's funny. I can talk to you about anything. Even more than with some of my friends.  

**Pezzo 1**

> **Darius:** Same here. You're easy to talk to. No pretending  
> **Darius:** [nome_compagno] and you are the only people I don't have to perform for  

Scelte di Sara:
- «That means a lot.» — *calda*
  - → **Darius:** It's true. Don't make it weird lol
- «We're lucky to have you.» — *Josh +1*
  - → **Darius:** Other way round. Always


`— punto di interruzione —`

**Pezzo 2**

> **Darius:** Goodnight Sara. Tell your man I said hi. And that he still owes me twenty bucks
