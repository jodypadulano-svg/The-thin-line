## =============================================================================
## PERSONAGGI
## =============================================================================
## Colori dei nomi provvisori. Quando arriveranno gli sprite, si aggiunge
## `image="sara"` ecc. per le side image o le espressioni.

## Sara parla.
define s = Character("Sara", color="#e8a3b8")
## Sara pensa: corsivo, tra parentesi, senza nome (il gioco è dal suo punto di vista).
define sp = Character(None, what_italic=True, what_color="#d9c8d0", what_prefix="(", what_suffix=")")

## Il compagno: il nome lo sceglie il giocatore.
define c = Character("[nome_compagno]", color="#8fb3e0")

define ch = Character("Chiara", color="#f0c674")
define si = Character("Simon", color="#7fd1a8")
define da = Character("Daniel", color="#c9a0ff")
define ho = Character("Howard", color="#b5a48a")
define ed = Character("L'editore", color="#d4b483")

## Narratore delle didascalie e voce dei retroscena.
define n = Character(None, what_italic=False)
define rs = Character(None, what_color="#ff9fb0", what_italic=True)
