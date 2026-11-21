## =============================================================================
## EPISODE 1 — DAY 10 (Wednesday)
## =============================================================================
## Calendar: docs/mese-1.md, day 10. Work: Barbara hands Sara a piece outside her
## job (accept in silence / point out it isn't her job, Conf +1). Lunch: Jessica
## puts her old books in a box; Sara recognises the novel they argued about on her
## first week (decision 18/11: ask what happened / let it go, no stats, enigmatic,
## no link to Barbara). Evening: still no keys; tell [nome_compagno] everything
## about Howard (Josh +1) or play it down (—).
## Decisions with Jody:
## - 19/11 Q&A: no locksmith, the keys turn up on day 11 (Howard, I20).
## - 20/11: Howard lives next door, a shared wall with the bedroom.
## Draft for Jody's review. Game text in English; comments in Italian.
## Invented by Claude, to be confirmed: the extra piece is the horoscope page
## (the astrologer is ill); Sara is a Taurus; the margin note in Jessica's old Anna Karenina.
## CG: docs/prompt-immagini/inquadrature-giorno-10.md. Finché mancano,
## compare la didascalia [CG].

label ep1_d10:
    call nuovo_giorno(10, "Wednesday")
    call ep1_d10_barbara
    call ep1_d10_jessica
    call ep1_d10_sera
    return


## --- Lavoro: il pezzo fuori mansione ----------------------------------------------------

label ep1_d10_barbara:
    $ vai("redazione", "The newsroom — 9:35 a.m.")
    $ musica("redazione")
    $ ambiente("redazione")
    n "Wednesday. [nome_compagno] locked the door behind them again this morning, and made a little bow. «Your doorman, madam.»"
    n "Sara has barely sat down when the glass door at the end of the room swings open."
    $ suono("porta_sbattuta")
    $ musica("barbara")
    $ cg("The newsroom: Barbara in a leopard-print blouse drops a thick folder on Sara's desk, leaning over her; Sara looks up from her coffee, caught off guard", "images/cg/ep1/d10_01_barbara_cartella.webp")
    ba "Darling. Good. You're here."
    n "A folder lands on the desk, between the coffee and the keyboard. It's fat with printouts and smells faintly of incense."
    ba "Madame Celeste has the flu. Or a new boyfriend. Either way, no horoscopes."
    ba "Twelve signs, eighty words each, on my desk by four. Love, money, health. Be mysterious."
    s "The horoscopes? Barbara, I'm... I write news."
    ba "You write words, sweetheart. These are words. With stars on them."

    menu:
        sp "Twelve horoscopes. By four."
        "Accept without a word.":
            s "By four. Of course."
            ba "Good girl. See? That wasn't so hard."
            n "Barbara taps the folder twice with a long red nail, the way you'd pat a dog that came when called, and sweeps away."
            sp "«Good girl.» I'm a grown woman."
            sp "And I just said yes to astrology."
        "Point out it isn't her job.":
            $ confidence(1, "Sara tells Barbara the horoscopes aren't her job.")
            $ segna("ep1_d10_non_mio_compito")
            s "With respect, it isn't really my job. I've got the council piece, and..."
            n "Barbara looks at her for a long second. Then she smiles, slow and delighted, as if Sara had done a trick."
            ba "Everything in this building is your job, darling. My name is on the door."
            ba "But I like it when you bite. Do it more often."
            ba "Four o'clock."
            n "She sweeps away. The folder stays where it is."
            sp "I said no. And I still have twelve horoscopes."
            sp "But I said no."

    $ musica("redazione")
    $ cg("Sara at her desk in the afternoon, chin in her hand, writing horoscopes with a half-guilty, half-amused smile, the open folder beside her", "images/cg/ep1/d10_02_oroscopi.webp")
    n "Aries gets a promotion. Gemini gets an unexpected phone call. Leo, for no reason at all, should beware of pigeons."
    n "By the time she reaches Taurus, her own sign, she's almost enjoying herself."
    n "{i}Taurus. Something you thought you had lost is closer than you think. It will come back to you sooner than you expect, and it will not come alone.{/i}"
    sp "Very mysterious. Madame Celeste would be proud."
    sp "If only it worked for keys."
    return


## --- Pausa pranzo: Jessica e il libro abbandonato (decisione 18/11) -------------------

label ep1_d10_jessica:
    $ vai("redazione", "The newsroom — 1:10 p.m.")
    $ cg("Lunch break in the half-empty newsroom: Jessica kneeling by a cardboard box, dropping old paperbacks into it; on top, a battered copy of a thick Russian novel", "images/cg/ep1/d10_03_jessica_libri.webp")
    n "At lunch the newsroom empties out. Only Jessica stays, kneeling on the carpet next to a cardboard box, emptying the bottom drawer of her desk."
    n "Paperbacks. Dozens of them. Thick ones, with cracked spines and coffee rings, going into the box one after another without a second look."
    n "On the top of the pile, Sara recognises a cover. She'd know it anywhere."
    s "Jess... is that your Anna Karenina?"
    je "Hm? Oh, that. Yes! It's going to the charity shop. All of them."
    s "You lent it to me my first week. You made me promise I'd read it in a month. You {i}fought{/i} me over that book."
    s "It was your favourite."
    n "Jessica smiles up at her. A bright, calm, completely happy smile."
    je "It was. Before."
    je "That was the old Jessica, Sara. She was always so... heavy. Always thinking, thinking, thinking. Always sad about something."
    je "I'm different now. I'm so much better. I don't need them any more."
    n "Two fingers rise to the little gold heart at her throat. She doesn't seem to notice she's doing it."

    menu:
        sp "Before {i}what{/i}?"
        "Ask her what happened.":
            $ segna("ep1_d10_jessica_chiesto")
            s "Jess. What happened to you? Seriously. Three months ago you were..."
            s "You were the cleverest person in this room."
            je "Nothing {i}happened{/i} to me, silly."
            n "She giggles, and for a moment, just a moment, something flickers behind her eyes. Like someone hearing their old name called from very far away."
            je "Something wonderful. I told you. I can't explain it, you have to feel it."
            je "But you will, I think. Maybe soon."
            je "And then you'll put your books in a box too, and you'll feel so {i}light{/i}."
            n "She pats Sara's hand, closes the box and carries it off towards the lift, humming."
            sp "Maybe soon. What does that even mean?"
        "Let it go.":
            s "Well. If you're happy."
            je "I am. So, so happy."
            n "Jessica closes the drawer with her hip and skips off to the kitchen to microwave her lunch."
            n "The box stays on the carpet. Sara hesitates. Then she picks up the novel."
            $ cg("Close-up of an old, battered novel open in Sara's hands: the margins crowded with small, neat pencil notes and underlinings", "images/cg/ep1/d10_04_note_margine.webp")
            n "The margins are full of tiny, neat pencil notes. Jessica's old handwriting, before the pink pens and the little hearts."
            n "Next to the last chapter, underlined twice: {i}She isn't destroyed. She chooses. That's the whole point.{/i}"
            sp "She chooses."
            n "Sara puts the book back on top of the pile, very gently, as if it might wake up."

    $ nota_sara("capa", "Jessica is giving away all her books, even Anna Karenina. «That was the old Jessica. I'm so much better now.»")
    return


## --- Sera: ancora senza chiavi -----------------------------------------------------------

label ep1_d10_sera:
    $ vai("casa", "Home — 7:30 p.m.")
    $ ambiente(None)
    $ musica("casa")
    n "She climbs the stairs, glances at the green door without meaning to, and rings at her own."
    $ suono("citofono")
    c "It's open! Your doorman is on duty!"
    $ cg("The kitchen in the evening: Sara and Josh at the little table over plates of pasta, Josh leaning in with a curious, teasing smile, Sara laughing", "images/cg/ep1/d10_05_cena.webp")
    n "Dinner is pasta with whatever was left in the fridge. [nome_compagno] has turned the gym bag inside out and checked every coat pocket. No keys."
    c "One more day. If they're not out by Friday I'll call someone. Promise."
    c "Anyway. I've been waiting all day. The famous evening at Howard's."
    c "Tell me everything. Did he show you his stamp collection? Does he sleep in a coffin?"

    menu:
        sp "The evening at Howard's."
        "Tell him everything about Howard.":
            $ interest("josh", 1, "Sara tells [nome_compagno] everything about her evening at Howard's.")
            $ segna("ep1_d10_racconta_howard")
            s "No coffin. But oh, love, the flat. Newspapers everywhere. On the radiator. On the {i}radiator{/i}."
            s "He worked in a factory for thirty-one years. He looked after his mother until she died. He showed me her photos."
            s "And then he cried. Really cried, [nome_compagno]. He said he always thought there'd be someone, and there never was."
            if fatto("ep1_d9_abbraccio"):
                s "So I hugged him. He was shaking like a little boy."
                c "You hugged Howard."
                n "He looks at her as if she'd told him she'd adopted a stray cat."
                c "My saint. Patron saint of lonely neighbours."
                if complesso_crocerossina:
                    sp "And his hand. No. There's nothing to tell about his hand."
                    sp "He didn't know where it was. I'm not going to make it into something ugly over dinner."
            else:
                c "God. Poor guy. I always thought he was just... weird."
            if fatto("ep1_howard_caffe") == "si":
                s "He asked if we could have a coffee now and then. I said yes."
                c "Of course you did."
                n "He says it fondly, and reaches across the table to steal her last piece of pasta."
            n "He listens to all of it. He asks questions. For the first time in days they talk about something that isn't Daniel."
            c "You're a good person, you know that? Too good for this building."
        "Play it down.":
            $ segna("ep1_d10_minimizza_howard")
            s "He made me coffee. We watched television. He talked about his mother. The end."
            c "That's it? Three hours?"
            s "Three very long hours. The flat is a disaster."
            c "Poor you. Next time I'll take an afternoon off and you can wait at Joanie's."
            n "He laughs, and moves on to Daniel, and Sara lets him."
            sp "Why didn't I tell him about the crying?"
            sp "It felt... private. Like it was Howard's, not mine to give away."
            if complesso_crocerossina:
                sp "And the hand. There's nothing to say about the hand. There's nothing."

    $ vai("camera", "The bedroom — 11:50 p.m.")
    $ musica("notte")
    $ cg("The dark bedroom at night: Josh asleep on his side, Sara awake on her back, eyes open, looking at the wall beside the bed", "images/cg/ep1/d10_06_letto_muro.webp")
    n "[nome_compagno] falls asleep the moment his head touches the pillow. Sara doesn't."
    n "Through the wall, very faintly, a television. A quiz show. Canned laughter."
    sp "It's right there. The other side of this wall. I never thought about it before."
    n "Then the television goes quiet. Somewhere very close, on the other side of the plaster, a bedspring creaks under a heavy body."
    sp "Goodnight, Howard."
    n "She says it in her head, kindly, the way you'd say it to a lonely child. Then she turns towards [nome_compagno] and closes her eyes."
    return
