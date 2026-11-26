"""Prepara i Sexting da incollare in una chat web (un LLM senza API).

Uso (dalla cartella del repo):
    python tools/nsfw/pacchetto_sexting.py ex_d1         un pacchetto
    python tools/nsfw/pacchetto_sexting.py --tutte       tutti quelli ancora da scrivere

Scrive tools/nsfw/pacchetti/<id>.txt: istruzioni, schede delle voci, scaletta, campione di stile
e chat esistente, nello stesso ordine che usa genera_sexting.py con LM Studio.
Si incolla tutto il file come primo messaggio. La risposta (solo PART A e PART B) si salva in
tools/nsfw/bozze/<id>.txt, poi:
    python tools/nsfw/genera_sexting.py <id> --controlla
    python tools/nsfw/genera_sexting.py <id> --inserisci
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import genera_sexting as g  # noqa: E402

USCITA = g.RADICE / "tools/nsfw/pacchetti"


def pacchetto(id, sistema, brief):
    chiave, _, _, chat = g.leggi_chat(id)
    return "\n\n".join([
        "Read all of this before writing. The first block is your standing instructions for this task; "
        "the rest is the material. Answer with PART A and PART B only, nothing before or after.",
        "=== INSTRUCTIONS ===\n" + sistema.strip(),
        "=== MATERIAL ===\n" + g.messaggio(id, chiave, chat, brief),
    ]) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id", nargs="*")
    ap.add_argument("--tutte", action="store_true")
    a = ap.parse_args()
    brief = g.sezioni((g.RADICE / "docs/nsfw/brief/sexting.md").read_text(encoding="utf-8").replace("\r\n", "\n"))
    sistema = (g.RADICE / "tools/nsfw/prompt_sexting.md").read_text(encoding="utf-8")
    ids = [k for k in brief if re.search(r"_d\d+$", k)] if a.tutte else a.id
    if not ids:
        ap.error("indica una chat (per esempio ex_d1) oppure --tutte")
    USCITA.mkdir(parents=True, exist_ok=True)
    for id in ids:
        if id not in brief:
            sys.exit("Nessuna scaletta per " + id)
        try:
            testo = pacchetto(id, sistema, brief)
        except SystemExit as e:
            print("%s: saltata (%s)" % (id, e))
            continue
        (USCITA / (id + ".txt")).write_text(testo, encoding="utf-8", newline="\n")
        print("%s: tools/nsfw/pacchetti/%s.txt (%d caratteri)" % (id, id, len(testo)))


if __name__ == "__main__":
    main()
