default sara_stagista = False

label ep2_d17_foto_extra:
    ## Solo la canzone dello shooting: spegnere il rumore della redazione (24/11).
    $ ambiente(None, dissolvenza=0.5)
    $ musica("barbara_shooting")
    $ via_cg()
    $ cg("Barbara whispers to Sara after the portrait", "images/cg/ep2/d17_barbara_sussurro.png")
    ba "That first portrait is the one for the company website. We have everything we need for that."
    ba "Since we have a professional photographer here today, why not take the opportunity to get some lovely pictures just for yourself?"
    s "Just for me?"
    ba "Of course. Anything we take from now on is private, not for the website. Only if you want to."
    menu:
        "I'll do one.":
            pass
        "The portrait's enough for me.":
            return
    $ interest("capa", 1, "Sara agreed to another photo for Barbara.")
    $ cg("Sara looks back over her shoulder", "images/cg/ep2/d17_barbara_extra_01.png")
    $ suono("otturatore")
    n "Sara hooks her thumb into her waistband and looks back at the lens."
    ba "That was the warm-up. Want to give him something bolder?"
    menu:
        "Open another two buttons.":
            pass
        "Let's leave it there.":
            jump ep2_d17_foto_extra_fine
    $ interest("capa", 1, "Sara agreed to another photo for Barbara.")
    $ cg("Sara poses on the desk with her blouse open", "images/cg/ep2/d17_barbara_extra_02.png")
    $ suono("otturatore")
    n "Sara perches on the desk. The edge of her black lace bra catches the light."
    ba "How about the blouse off for this one? The black lace would look lovely in this light."
    menu:
        "All right. Give me a second.":
            pass
        "I think we've got enough.":
            jump ep2_d17_foto_extra_fine
    $ interest("capa", 1, "Sara agreed to another photo for Barbara.")
    $ cg("Sara poses in her black lace bra", "images/cg/ep2/d17_barbara_extra_03.png")
    $ suono("otturatore")
    n "Sara leaves her blouse on the chair and turns back into the light."
    ba "I could call it there. But I'd like one without the bra, if you're still enjoying yourself."
    menu:
        "I am. Give me a second.":
            pass
        "Let's leave it there.":
            jump ep2_d17_foto_extra_fine
    $ interest("capa", 1, "Sara agreed to another photo for Barbara.")
    $ corruption(3, "Sara took off her bra for the photoshoot.")
    $ cg("Sara poses beside the chair after removing her bra", "images/cg/ep2/d17_barbara_extra_04.png")
    $ suono("otturatore")
    n "Sara lays her bra on top of her blouse and gives the photographer a smile."
    s "You've got another idea, haven't you?"
    ba "The trousers too, Sara. Come over to the desk. I want to see what you do with the next one."
    menu:
        "All right. Tell him to wait until I look up.":
            pass
        "I like the one we just took. Let's keep that.":
            jump ep2_d17_foto_extra_fine
    $ interest("capa", 1, "Sara agreed to another photo for Barbara.")
    $ cg("Sara looks back from the edge of the desk", "images/cg/ep2/d17_barbara_extra_05.png")
    $ suono("otturatore")
    n "Sara settles on the desk and looks up. The shutter clicks. So does Barbara's tongue, softly, just before she laughs."
    s "I heard that."
    ba "God, Sara. I've wanted to ask you this for months. The lace too?"
    menu:
        "All right. But this time I'll tell him when to shoot.":
            pass
        "I'm keeping these on.":
            jump ep2_d17_foto_extra_fine
    $ interest("capa", 1, "Sara agreed to another photo for Barbara.")
    $ cg("Sara poses by the window and looks back over her shoulder", "images/cg/ep2/d17_barbara_extra_06.png")
    s "Now."
    $ suono("otturatore")
    n "The shutter clicks. Barbara barely waits for it."
    ba "Again. Hold that smile. There. God, I could keep you here all afternoon."
    ba "Will you turn all the way around for me, Sara?"
    menu:
        "You really are greedy, Barbara.":
            pass
        "You'll have to make do with those.":
            jump ep2_d17_foto_extra_fine
    $ interest("capa", 1, "Sara agreed to another photo for Barbara.")
    $ cg("Sara turns to face the photographer", "images/cg/ep2/d17_barbara_extra_07.png")
    $ suono("otturatore")
    n "Sara laughs as she turns toward the lens. After the last click, the photographer lowers his camera."
    ba "Sara. Come to my office for a minute?"
    s "Like this?"
    ba "If you like."
    menu:
        "All right. I'll bring my clothes.":
            $ interest("capa", 3, "Sara went to Barbara's office after the photoshoot.")
            call ep2_d17_barbara_ufficio
            return
        "I think I'm done for today.":
            jump ep2_d17_foto_extra_fine

label ep2_d17_foto_extra_fine:
    n "The photographer lowers the camera. Sara gathers her clothes."
    return

label ep2_d17_barbara_ufficio:
    $ via_cg()
    ## Niente ambiente d'ufficio sopra la canzone dello shooting (24/11).
    $ vai("redazione", "Barbara's office — After the photoshoot")
    $ cg("Sara and Barbara talk in private", "images/cg/ep2/d17_barbara_ufficio.png")
    n "Sara puts her clothes on the spare chair and sits down. Barbara shuts the door."
    s "You had another pose in mind every time he put the camera down."
    ba "Three, usually. I had to pick one."
    s "How long have you been thinking about this?"
    ba "Since before I had a good excuse to ask."
    s "And the website was your good excuse?"
    ba "It was better than the others."
    n "Sara laughs. Barbara loses her train of thought for a beat, then takes a sheet of paper from the desk."
    ba "I have an offer for you. A special internship. You'd work directly with me."
    s "How special?"
    ba "I like girls who do exactly as I ask. Every little thing. You did beautifully out there."
    s "Is that why you kept asking for another picture?"
    ba "I kept asking because I wanted to see how far you'd go."
    n "Barbara holds Sara's gaze. The corner of her mouth lifts."
    ba "Will you sign it for me, Sara?"
    call ep2_d17_barbara_scelta_contratto
    return

label ep2_d17_barbara_scelta_contratto:
    menu:
        "I don't know I may have to think about it":
            ## La firma come filmato a tempo, come la terrazza del 13 (Jody, 24/11).
            n "{i}The next scene plays to music and runs on its own, about a minute and a half.{/i}"
            menu:
                "Watch the scene.":
                    call ep2_d17_barbara_firma_tempo
                    return
                "Skip the scene.":
                    call ep2_d17_barbara_firma
                    return
        "I liked the photos. I'm leaving it there.":
            s "I liked the photos. I'm leaving it there."
            n "Sara reaches for her blouse. Barbara sets the contract back on the desk."
            return

label ep2_d17_barbara_firma:
    $ renpy.stop_skipping()
    $ renpy.block_rollback()
    $ _ep2_d17_skipping_precedente = _skipping
    $ _skipping = False
    $ ambiente(None, dissolvenza=0)
    $ musica("barbara_firma", dissolvenza=0)
    $ via_cg()
    $ cg("Barbara approaches Sara with the contract", "images/cg/ep2/d17_barbara_firma_01_avvicinamento.png")
    s "I don't know I may have to think about it"
    n "Barbara crosses the room slowly, watching her. Sara stays where she is."

    $ filmato("images/video/ep2/d17_barbara_firma_01_penna.webm", stop_music=False)
    $ via_cg()
    $ cg("Barbara leans close to Sara's ear", "images/cg/ep2/d17_barbara_firma_02_sussurro.png")
    n "Barbara lays the contract flat, turns it toward Sara and puts the pen between her fingers. Sara closes her hand around it."
    ba "I know you want me to guide you."
    n "Sara's hand trembles. She looks down at the signature line and turns her wrist toward Barbara."
    s "Show me."

    ba "Sign."
    if renpy.loadable("images/video/ep2/d17_barbara_firma_02_polso.webm"):
        $ filmato("images/video/ep2/d17_barbara_firma_02_polso.webm", stop_music=False)
    else:
        n "Barbara takes Sara by the wrist and guides her hand across the signature line. Sara watches her name take shape."
    $ corruption(10, "Sara signed Barbara's special internship contract.")
    $ interest("capa", 10, "Sara signed Barbara's special internship contract.")
    $ sara_stagista = True
    $ via_cg()
    $ cg("Sara sets the pen down after signing", "images/cg/ep2/d17_barbara_firma_04_firmato.png")
    n "Sara sets down the pen. Her knees shift apart slightly. She glances down, suddenly aware of how wet she is. When she looks up, Barbara is smiling."

    n "Barbara takes Sara's chin in one hand and tilts it up."
    ba "You're mine now."
    $ filmato("images/video/ep2/d17_barbara_firma_04_bacio.webm", stop_music=False)
    n "Sara lifts her face to meet her. Barbara kisses her briefly on the lips and lets go."
    ba "Get dressed. You start tomorrow."
    $ musica(None)
    $ _skipping = _ep2_d17_skipping_precedente
    $ renpy.block_rollback()
    return


## --- La firma a tempo (Jody, 24/11) -------------------------------------------------------
## Sulla canzone barbara_firma: 0:17 il foglio, 0:38 la penna, 0:45 la firma (video del polso).
## Battute non saltabili (vc_* del giorno 13). Gli effetti sono gli stessi della versione a clic.

define D17_BARBARA = "#e07fb0"

init python:
    def d17_firma_inizia():
        f = _file_audio("musica", "barbara_firma")
        if f:
            renpy.music.play(f, channel="music", loop=False, fadein=0.5)
        _vc["inizio"] = _tempo_vc.time()
        _vc["pausa"] = None

label ep2_d17_barbara_firma_tempo:
    $ renpy.stop_skipping()
    $ renpy.block_rollback()
    $ _ep2_d17_skipping_precedente = _skipping
    $ _skipping = False
    $ ambiente(None, dissolvenza=0)
    $ via_cg()
    $ luogo_corrente = ""
    $ d17_firma_inizia()
    $ vc_a(0); vc_quadro("images/cg/ep2/d17_barbara_firma_01_avvicinamento.png", "Barbara approaches Sara with the contract")
    $ vc_a(1); vc_riga("Sara", "I don't know... I may have to think about it.", VC_SARA)
    $ vc_a(8); vc_riga(None, "Barbara crosses the room slowly, watching her. Sara stays where she is.")
    $ vc_a(17); vc_video("images/video/ep2/d17_barbara_firma_01_penna.webm", "images/cg/ep2/d17_barbara_firma_01_avvicinamento.png", "Barbara brings the contract and hands it to Sara with the pen")
    $ vc_a(23); vc_quadro("images/cg/ep2/d17_barbara_firma_02_sussurro.png", "Barbara leans close to Sara's ear while Sara holds the pen"); vc_riga(None, "Barbara lays the contract flat and puts the pen between her fingers. Sara closes her hand around it.")
    $ vc_a(29); vc_riga("Barbara", "I know you want me to guide you.", D17_BARBARA)
    $ vc_a(34); vc_riga(None, "Sara's hand trembles. She looks down at the signature line and turns her wrist toward Barbara.")
    $ vc_a(38); vc_riga("Sara", "Show me.", VC_SARA)
    $ vc_a(43); vc_riga("Barbara", "Sign.", D17_BARBARA)
    $ vc_a(45); vc_video("images/video/ep2/d17_barbara_firma_02_polso.webm", "images/cg/ep2/d17_barbara_firma_02_sussurro.png", "Barbara guides Sara's wrist across the signature line")
    $ corruption(10, "Sara signed Barbara's special internship contract.")
    $ interest("capa", 10, "Sara signed Barbara's special internship contract.")
    $ sara_stagista = True
    $ vc_a(52); vc_quadro("images/cg/ep2/d17_barbara_firma_04_firmato.png", "Sara sets the pen down after signing")
    $ vc_a(53); vc_riga(None, "Sara sets down the pen. Her knees shift apart slightly. She is suddenly aware of how wet she is.")
    $ vc_a(61); vc_riga(None, "When she looks up, Barbara is smiling. She takes Sara's chin in one hand and tilts it up.")
    $ vc_a(68); vc_riga("Barbara", "You're mine now.", D17_BARBARA)
    $ vc_a(72); vc_video("images/video/ep2/d17_barbara_firma_04_bacio.webm", "images/cg/ep2/d17_barbara_firma_04_firmato.png", "Barbara kisses Sara briefly on the lips")
    $ vc_a(77); vc_quadro("images/cg/ep2/d17_barbara_firma_04_firmato.png"); vc_riga(None, "Sara lifts her face to meet her. Barbara kisses her briefly on the lips and lets go.")
    $ vc_a(84); vc_riga("Barbara", "Get dressed. You start tomorrow.", D17_BARBARA)
    $ vc_a(90); vc_via()
    $ musica(None, dissolvenza=3.0)
    $ _skipping = _ep2_d17_skipping_precedente
    $ renpy.block_rollback()
    return
