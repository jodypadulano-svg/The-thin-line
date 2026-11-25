"""Disegna i pezzi della grafica del telefono in game/images/ui/telefono/gui/.

Uso, dalla cartella del gioco:  python tools/telefono/disegna_grafica.py
Tutto è disegnato qui: nessuna icona o marchio di altre app. I colori sono quelli del gioco.
"""
from pathlib import Path

from PIL import Image, ImageDraw

USCITA = Path(__file__).resolve().parents[2] / "game/images/ui/telefono/gui"
S = 4   # si disegna quattro volte più grande, poi si riduce

NERO, BORDEAUX, VINO = "#1c1216", "#5e2136", "#8f2f52"
CARTA, CREMA, ROSA, BIANCO = "#f3e8e1", "#f8f0eb", "#f4ccd8", "#ffffff"
BORDO, GRIGIO, TESTO = "#c98ba0", "#a58c96", "#f9e9ee"


def tela(w, h):
    im = Image.new("RGBA", (w * S, h * S), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)


def salva(im, nome):
    USCITA.mkdir(parents=True, exist_ok=True)
    im.resize((im.width // S, im.height // S), Image.LANCZOS).save(USCITA / (nome + ".png"))


def rett(d, box, r, colore, angoli=(True, True, True, True), bordo=None, spesso=0):
    d.rounded_rectangle([v * S for v in box], r * S, fill=colore, outline=bordo, width=spesso * S, corners=angoli)


def linea(d, punti, colore, w):
    d.line([(x * S, y * S) for x, y in punti], fill=colore, width=int(w * S), joint="curve")
    for x, y in (punti[0], punti[-1]):
        d.ellipse([(x - w / 2) * S, (y - w / 2) * S, (x + w / 2) * S, (y + w / 2) * S], fill=colore)


def tondo(d, x, y, r, colore=None, bordo=None, w=0):
    d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], fill=colore, outline=bordo, width=int(w * S))


## Cornice, testa e piede -----------------------------------------------------------------
im, d = tela(560, 1040)
rett(d, (0, 0, 559, 1039), 64, NERO)
rett(d, (3, 3, 556, 1036), 61, None, bordo="#3a2830", spesso=2)
salva(im, "cornice")

im, d = tela(530, 126)
rett(d, (0, 0, 529, 125), 48, BORDEAUX, (True, True, False, False))
rett(d, (205, 10, 325, 34), 12, NERO)
for i, h in enumerate((5, 9, 13)):                      # segnale
    rett(d, (420 + i * 7, 30 - h, 424 + i * 7, 30), 1, TESTO)
rett(d, (452, 18, 478, 30), 3, None, bordo=TESTO, spesso=2)   # batteria
rett(d, (455, 21, 470, 27), 1, TESTO)
rett(d, (479, 21, 481, 27), 1, TESTO)
salva(im, "testa")

im, d = tela(530, 88)
rett(d, (0, 0, 529, 87), 48, CREMA, (False, False, True, True))
rett(d, (14, 10, 440, 64), 27, BIANCO)
tondo(d, 484, 37, 28, VINO)
rett(d, (478, 22, 490, 42), 6, TESTO)                    # microfono
d.arc([471 * S, 27 * S, 497 * S, 49 * S], 10, 170, fill=TESTO, width=int(2.6 * S))
linea(d, [(484, 48), (484, 54)], TESTO, 2.6)
tondo(d, 42, 37, 12, None, GRIGIO, 2.2)                  # faccina
tondo(d, 38, 34, 1.6, GRIGIO); tondo(d, 46, 34, 1.6, GRIGIO)
d.arc([36 * S, 32 * S, 48 * S, 44 * S], 20, 160, fill=GRIGIO, width=int(2 * S))
linea(d, [(362, 44), (374, 30)], GRIGIO, 2.4)            # graffetta
d.arc([358 * S, 36 * S, 370 * S, 48 * S], 45, 230, fill=GRIGIO, width=int(2.4 * S))
d.arc([368 * S, 24 * S, 380 * S, 36 * S], 200, 30, fill=GRIGIO, width=int(2.4 * S))
rett(d, (400, 28, 426, 47), 4, None, bordo=GRIGIO, spesso=2)   # macchina foto
tondo(d, 413, 37.5, 5, None, GRIGIO, 2)
rett(d, (408, 24, 418, 28), 1, GRIGIO)
rett(d, (195, 76, 335, 81), 2, "#cdb9b2")
salva(im, "piede")

im, d = tela(530, 88)                                    # piede della rubrica, vuoto
rett(d, (0, 0, 529, 87), 48, CREMA, (False, False, True, True))
rett(d, (195, 76, 335, 81), 2, "#cdb9b2")
salva(im, "piede_rubrica")

## Bolle (nove riquadri: bordi 20) ---------------------------------------------------------
for nome, colore, angoli in (("bolla_sara", ROSA, (True, True, False, True)), ("bolla_altro", BIANCO, (True, True, True, False))):
    im, d = tela(48, 48)
    rett(d, (0, 0, 47, 47), 17, colore, angoli)
    salva(im, nome)

## Risposte, etichette, pallino, riga di rubrica ---------------------------------------------
for nome, colore, bordo in (("risposta", BIANCO, BORDO), ("risposta_sopra", ROSA, VINO), ("risposta_no", "#efe6e1", "#d8c8c0"), ("risposta_ambra", "#fff1d9", "#c97a12"), ("risposta_ambra_sopra", "#ffe0ad", "#c97a12")):
    im, d = tela(60, 60)
    rett(d, (1, 1, 58, 58), 24, colore, bordo=bordo, spesso=2)
    salva(im, nome)
im, d = tela(40, 40); rett(d, (0, 0, 39, 39), 12, BIANCO); salva(im, "etichetta")
im, d = tela(28, 28); tondo(d, 14, 14, 13.5, VINO); salva(im, "pallino")
im, d = tela(64, 64); tondo(d, 32, 32, 31.5, "#b98a9a"); salva(im, "foto_vuota")

## Icone --------------------------------------------------------------------------------------
im, d = tela(34, 34); linea(d, [(18, 6), (7, 17), (18, 28)], TESTO, 3); linea(d, [(8, 17), (28, 17)], TESTO, 3); salva(im, "freccia")
im, d = tela(34, 34); rett(d, (2, 8, 22, 26), 5, TESTO); d.polygon([(x * S, y * S) for x, y in ((24, 15), (32, 9), (32, 25), (24, 19))], fill=TESTO); salva(im, "video")
im, d = tela(34, 34)
linea(d, [(8, 7), (9, 16), (18, 25), (27, 26)], TESTO, 4.4)
linea(d, [(6, 6), (12, 5)], TESTO, 4.8); linea(d, [(28, 22), (29, 28)], TESTO, 4.8)
salva(im, "cornetta")
im, d = tela(20, 34)
for y in (8, 17, 26):
    tondo(d, 10, y, 2.6, TESTO)
salva(im, "punti")
for nome, colore in (("spunte", GRIGIO), ("spunte_lette", "#b0355c")):
    im, d = tela(28, 18)
    linea(d, [(2, 10), (7, 15), (17, 3)], colore, 2.2)
    linea(d, [(12, 13), (14, 15), (25, 3)], colore, 2.2)
    salva(im, nome)
print("fatto:", ", ".join(sorted(p.stem for p in USCITA.glob("*.png"))))
