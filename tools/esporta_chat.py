"""Esporta i discorsi al telefono (game/percorsi/chat_*.rpy) in un documento
leggibile per la revisione: docs/revisione-chat.md.

Uso:  python tools/esporta_chat.py
Controlla anche che ogni discorso registrato abbia almeno il pezzo 1."""
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTELLA = os.path.join(RADICE, "game", "percorsi")
USCITA = os.path.join(RADICE, "docs", "revisione-chat.md")

NOMI = {"simon": "Simon", "howard": "Howard", "daniel": "Daniel", "editore": "Magnus",
        "capa": "Barbara", "ex": "Jacob", "amica": "Joanie", "amico": "Darius"}
ORDINE = ["simon", "howard", "daniel", "editore", "capa", "ex", "amica", "amico"]
LIVELLI = {"ESTRANEI": "Introduzione", "CONOSCENTI": "A", "CONFIDENZA": "B",
           "COMPLICI": "C", "INTIMI": "D"}

RE_DISCORSO = re.compile(r'discorso\("([^"]+)",\s*"([^"]+)",\s*([A-Z]+)(.*)\)')
RE_LABEL = re.compile(r'^label (chat_\w+):')
RE_MSG = re.compile(r'\$ msg\("(\w+)",\s*"(.*)"\)\s*$')
RE_SP = re.compile(r'^\s*sp "(.*)"\s*$')
RE_SCELTA = re.compile(r'^(\s*)"(.*?)"(\s*\((.*)\))?\s*(if .*)?:\s*$')


def nome(chi):
    if chi == "sara":
        return "Sara"
    return NOMI.get(chi, chi)


def leggi(chiave):
    percorso = os.path.join(CARTELLA, "chat_%s.rpy" % chiave)
    with open(percorso, encoding="utf-8") as f:
        righe = f.read().split("\n")
    discorsi, label, corrente = [], {}, None
    for riga in righe:
        m = RE_DISCORSO.search(riga)
        if m and "def " not in riga:
            discorsi.append((m.group(1), m.group(3), m.group(4)))
        m = RE_LABEL.match(riga)
        if m:
            corrente = m.group(1)
            label[corrente] = []
            continue
        if corrente:
            label[corrente].append(riga)
    return discorsi, label


def effetti(blocco):
    e = []
    for r in blocco:
        r = r.strip()
        if r.startswith("$ caldo()"):
            e.append("calda")
        elif r.startswith("$ frena()"):
            e.append("freno")
        elif r.startswith("$ segna("):
            e.append("flag " + r[len("$ segna(\""):-2])
        elif r.startswith("$ interest(\"josh\""):
            e.append("Josh +1")
        elif r.startswith("$ interest("):
            e.append("Interest " + r[len("$ interest("):-1])
        elif r.startswith("$ corruption("):
            e.append("Corr +" + r[len("$ corruption("):-1])
        elif r.startswith("$ confidence("):
            e.append("Conf +" + r[len("$ confidence("):-1])
    return e


def rendi(righe):
    """Trasforma il corpo di un label in righe Markdown."""
    out, i = [], 0
    while i < len(righe):
        r = righe[i]
        s = r.strip()
        m = RE_MSG.search(s)
        if m and not r.startswith(" " * 12):
            out.append("> **%s:** %s  " % (nome(m.group(1)), m.group(2)))
        elif RE_SP.match(r) and not r.startswith(" " * 12):
            out.append("> *(%s)*  " % RE_SP.match(r).group(1))
        elif s.startswith("menu"):
            out.append("")
            out.append("Scelte di Sara:")
            i += 1
            while i < len(righe) and (righe[i].startswith(" " * 8) or not righe[i].strip()):
                m2 = RE_SCELTA.match(righe[i])
                if m2 and len(m2.group(1)) == 8:
                    testo = m2.group(2)
                    req = m2.group(4)
                    blocco = []
                    j = i + 1
                    while j < len(righe) and (righe[j].startswith(" " * 12) or not righe[j].strip()):
                        blocco.append(righe[j])
                        j += 1
                    etichette = effetti(blocco)
                    if req:
                        etichette.insert(0, "richiede " + req)
                    out.append("- %s%s" % (testo, (" — *" + ", ".join(etichette) + "*") if etichette else ""))
                    for b in blocco:
                        mb = RE_MSG.search(b.strip())
                        if mb and mb.group(1) != "sara":
                            out.append("  - → **%s:** %s" % (nome(mb.group(1)), mb.group(2)))
                        elif RE_SP.match(b):
                            out.append("  - → *(%s)*" % RE_SP.match(b).group(1))
                    i = j
                    continue
                i += 1
            out.append("")
            continue
        elif s.startswith("if ") or s.startswith("else"):
            out.append("*[%s]*  " % s.rstrip(":"))
        elif s.startswith("call howard_retroscena_chat("):
            testo = s[len("call howard_retroscena_chat(\""):].split("\", \"")[0]
            out.append("")
            out.append("**Retroscena:** *%s*" % testo)
        elif s.startswith("$ segna("):
            out.append("*[flag %s]*  " % s[len("$ segna(\""):-2])
        i += 1
    return out


def main():
    righe_doc = ["# The Thin Line — Revisione dei discorsi al telefono", "",
                 "Generato da `tools/esporta_chat.py` dai file `game/percorsi/chat_*.rpy`. "
                 "Non modificare a mano: si rigenera. Testi in inglese (come il gioco); "
                 "le note in corsivo sono effetti e flag.", ""]
    mancanti, totale = [], 0
    for chiave in ORDINE:
        discorsi, label = leggi(chiave)
        righe_doc += ["", "## %s" % NOMI[chiave], ""]
        for id_, livello, resto in discorsi:
            totale += 1
            if "chat_%s_1" % id_ not in label:
                mancanti.append(id_)
            titolo = "### %s · %s" % (id_, LIVELLI.get(livello, livello))
            if "se=" in resto:
                titolo += " · condizione: `%s`" % re.search(r'se="([^"]+)"', resto).group(1)
            if "scrive_lui=True" in resto:
                titolo += " · può scrivere lui per primo"
            righe_doc += [titolo, ""]
            if "chat_%s" % id_ in label:
                righe_doc += ["*Se scrive Sara:*", ""] + rendi(label["chat_%s" % id_]) + [""]
            if "chat_%s_entrata" % id_ in label:
                righe_doc += ["*Se scrive lui/lei:*", ""] + rendi(label["chat_%s_entrata" % id_]) + [""]
            n = 1
            while "chat_%s_%d" % (id_, n) in label:
                if n > 1:
                    righe_doc += ["`— punto di interruzione —`", ""]
                righe_doc += ["**Pezzo %d**" % n, ""] + rendi(label["chat_%s_%d" % (id_, n)]) + [""]
                n += 1
    with open(USCITA, "w", encoding="utf-8") as f:
        f.write("\n".join(righe_doc).rstrip() + "\n")
    print("discorsi:", totale, "senza pezzo 1:", mancanti or "nessuno")
    print("scritto:", USCITA)
    return 1 if mancanti else 0


if __name__ == "__main__":
    sys.exit(main())
