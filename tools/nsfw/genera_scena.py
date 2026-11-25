"""Genera una scena intima con il modello caricato in LM Studio.

Uso (dalla cartella del repo):
    py tools/nsfw/genera_scena.py docs/nsfw/brief/<id>.md
    py tools/nsfw/genera_scena.py docs/nsfw/brief/<id>.md --uscita <cartella>

Legge il brief, lo manda al server locale di LM Studio (http://localhost:1234)
insieme a tools/nsfw/prompt_sistema.md, controlla che ogni riga sia una battuta
Ren'Py valida e scrive game/nsfw/<id>.rpy con la label `nsfw_<id>`.
Le righe non valide finiscono in un file .scartate.txt accanto, da sistemare a mano.
Il risultato va sempre riletto da Jody prima di entrare nel gioco.
"""
import argparse, json, pathlib, re, sys, urllib.request

SERVER = "http://localhost:1234/v1"
CODICI = {"s", "sp", "c", "ch", "si", "da", "ho", "ed", "jacob", "n"}
RIGA = re.compile(r'^\s*([a-z]+)\s+"(.*)"\s*$')
RADICE = pathlib.Path(__file__).resolve().parents[2]


def leggi_brief(percorso):
    testo = percorso.read_text(encoding="utf-8")
    m = re.search(r"^id:\s*([a-z0-9_]+)\s*$", testo, re.M)
    if not m:
        sys.exit("Nel brief manca la riga 'id: nome_scena' (minuscole, numeri, _).")
    return m.group(1), testo


def modello_caricato():
    with urllib.request.urlopen(SERVER + "/models", timeout=5) as r:
        modelli = [m["id"] for m in json.load(r)["data"] if "embed" not in m["id"]]
    if not modelli:
        sys.exit("Nessun modello in LM Studio: caricane uno e riprova.")
    return modelli[0]


def genera(sistema, brief, modello, temperatura, max_token):
    corpo = json.dumps({
        "model": modello,
        "messages": [
            {"role": "system", "content": sistema},
            {"role": "user", "content": brief},
        ],
        "temperature": temperatura,
        "max_tokens": max_token,
    }).encode("utf-8")
    req = urllib.request.Request(SERVER + "/chat/completions", data=corpo,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r:
        scelta = json.load(r)["choices"][0]
    testo = scelta["message"].get("content") or ""
    if not testo.strip() and scelta.get("finish_reason") == "length":
        sys.exit("Il modello ha finito i token mentre ragionava: riprova con --max-token piu' alto.")
    return testo


def pulisci(testo):
    buone, scartate = [], []
    for riga in testo.replace("\r", "").split("\n"):
        if not riga.strip() or riga.strip().startswith("```"):
            continue
        m = RIGA.match(riga)
        if m and m.group(1) in CODICI and '"' not in m.group(2):
            buone.append('    {} "{}"'.format(m.group(1), m.group(2).strip()))
        else:
            scartate.append(riga)
    return buone, scartate


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("brief", type=pathlib.Path)
    ap.add_argument("--uscita", type=pathlib.Path, default=RADICE / "game" / "nsfw")
    ap.add_argument("--temperatura", type=float, default=0.8)
    ap.add_argument("--max-token", type=int, default=6000)  # include il ragionamento del modello
    a = ap.parse_args()

    scena, brief = leggi_brief(a.brief)
    sistema = (RADICE / "tools" / "nsfw" / "prompt_sistema.md").read_text(encoding="utf-8")
    modello = modello_caricato()
    print("Modello:", modello, "- scena:", scena, "- genero (puo' volerci qualche minuto)...")
    grezzo = genera(sistema, brief, modello, a.temperatura, a.max_token)
    buone, scartate = pulisci(grezzo)

    a.uscita.mkdir(parents=True, exist_ok=True)
    rpy = a.uscita / (scena + ".rpy")
    intestazione = [
        "## Generata con LM Studio ({}) dal brief {}".format(modello, a.brief.as_posix()),
        "## DA RILEGGERE prima della pubblicazione.",
        "",
        "label nsfw_{}:".format(scena),
    ]
    rpy.write_text("\n".join(intestazione + (buone or ['    n "(scena vuota)"']) + ["    return", ""]),
                   encoding="utf-8")
    print("Scritte {} righe in {}".format(len(buone), rpy))
    if scartate:
        f = a.uscita / (scena + ".scartate.txt")
        f.write_text("\n".join(scartate), encoding="utf-8")
        print("Attenzione: {} righe non valide in {}".format(len(scartate), f))


if __name__ == "__main__":
    main()
