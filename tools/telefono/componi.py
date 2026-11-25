"""Trasforma i testi delle chat (tools/telefono/<chiave>.txt) in argomenti_<chiave>.rpy.

Uso, dalla cartella del gioco:  python tools/telefono/componi.py howard

Formato del testo:
  @ howard_t1 | CONOSCENTI | The sauce stain | fatto('...')   id, gradino, titolo, condizione
                                        COMPLICI = chat di Flirt, INTIMI = Sexting: si scelgono
                                        per tipo e il titolo è solo un promemoria
  > messaggio con cui Sara apre la chat
  < messaggio in entrata (se scrive per primo l'altro; facoltativo, prima della prima parte)
  ---                                   nuova parte (comincia sempre l'altro)
  < messaggio dell'altro
  * pensiero di Sara
  ? risposta di Sara [caldo] [frena] [rifiuto]   una scelta; sotto, le righe < e * che la seguono
                                        [rifiuto] = grigia col Complesso (solo Howard)
  $ comando Ren'Py                      nella parte o nella scelta corrente

Le parti senza scelte finiscono con l'altro. I tempi d'attesa li mette il gioco.
"""
import io
import re
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parents[2]


def q(t):
    return t.replace("\\", "\\\\").replace('"', '\\"')


class Blocco:
    def __init__(self, nome):
        self.nome, self.n, self.righe = nome, 0, []

    def agg(self, rientro, testo):
        self.righe.append("    " * rientro + testo)

    def punto(self, rientro, tipo, bolle=0):
        self.n += 1
        p = "tel_%s_%d" % (self.nome, self.n)
        self.agg(rientro, "label %s:" % p)
        fine = ", %d" % bolle if bolle else ""
        self.agg(rientro, 'if telefono_minuti_blocco("%s", "%s"%s):' % (p, tipo, fine))
        self.agg(rientro + 1, "return")
        return p

    def ricevi(self, rientro, chiave, righe):
        """Messaggi dell'altro consecutivi: un'attesa sola, poi una bolla per minuto."""
        i = 0
        while i < len(righe):
            seg, t = righe[i]
            if seg == "<":
                gruppo = []
                while i < len(righe) and righe[i][0] == "<":
                    gruppo.append(righe[i][1])
                    i += 1
                self.punto(rientro, "ricevi", len(gruppo))
                for m in gruppo:
                    self.agg(rientro, '$ msg("%s", "%s")' % (chiave, q(m)))
                continue
            if seg == "*":
                self.agg(rientro, 'sp "%s"' % q(t))
            elif seg == "$":
                self.agg(rientro, "$ " + t)
            i += 1


def leggi(testo):
    chat = []
    for r in testo.splitlines():
        r = r.strip()
        if not r or r.startswith("#"):
            continue
        if r == "---":
            chat[-1]["parti"].append({"righe": [], "scelte": []})
            continue
        seg, t = r[0], r[1:].strip()
        if seg == "@":
            c = [x.strip() for x in t.split("|")]
            chat.append({"id": c[0], "gradino": c[1], "titolo": c[2], "se": c[3] if len(c) > 3 else "",
                         "apre": None, "entrata": [], "parti": []})
        elif seg == ">":
            assert chat[-1]["apre"] is None, "due aperture in " + chat[-1]["id"]
            chat[-1]["apre"] = t
        elif seg == "<" and not chat[-1]["parti"]:
            chat[-1]["entrata"].append(t)
        elif seg == "?":
            segni = re.findall(r"\[(caldo|frena|rifiuto)\]", t)
            t = re.sub(r"\s*\[(caldo|frena|rifiuto)\]", "", t).strip()
            chat[-1]["parti"][-1]["scelte"].append({"testo": t, "segni": segni, "righe": []})
        elif seg in "<*$":
            p = chat[-1]["parti"][-1]
            (p["scelte"][-1]["righe"] if p["scelte"] else p["righe"]).append((seg, t))
        else:
            raise ValueError("riga non riconosciuta: " + r)
    for c in chat:
        calde = sum(any("caldo" in s["segni"] for s in p["scelte"]) for p in c["parti"])
        assert calde <= 2, "troppe parti calde in " + c["id"]
    return chat


def componi(chiave, chat):
    out = ["## GENERATO da tools/telefono/componi.py: si modifica tools/telefono/%s.txt." % chiave, "", "init python:"]
    for c in chat:
        se = ', se="%s"' % c["se"] if c["se"] else ""
        come = ", flirt=True" if c["gradino"] in ("COMPLICI", "INTIMI") else ', argomento="%s"' % q(c["titolo"])
        out.append('    discorso("%s", "%s", %s%s%s)' % (c["id"], chiave, c["gradino"], come, se))
    for c in chat:
        out += ["", "", "## --- %s" % c["titolo"]]
        b = Blocco("chat_" + c["id"])
        b.agg(0, "label chat_%s:" % c["id"])
        b.punto(1, "invia", 1)
        b.agg(1, '$ msg("sara", "%s")' % q(c["apre"]))
        b.agg(1, "return")
        out += [""] + b.righe
        if c["entrata"]:
            b = Blocco("chat_%s_entrata" % c["id"])
            b.agg(0, "label chat_%s_entrata:" % c["id"])
            b.ricevi(1, chiave, [("<", m) for m in c["entrata"]])
            b.agg(1, "return")
            out += [""] + b.righe
        for i, p in enumerate(c["parti"], 1):
            b = Blocco("chat_%s_%d" % (c["id"], i))
            b.agg(0, "label chat_%s_%d:" % (c["id"], i))
            b.ricevi(1, chiave, p["righe"])
            if p["scelte"]:
                punto = b.punto(1, "scelta")
                b.agg(1, 'menu (screen="scelta_telefono"):')
                for s in p["scelte"]:
                    no = " (rifiuto_howard=True)" if "rifiuto" in s["segni"] else ""
                    b.agg(2, '"«%s»"%s:' % (q(s["testo"]), no))
                    b.punto(3, "invia", 1)
                    b.agg(3, '$ msg("sara", "%s")' % q(s["testo"]))
                    for segno in s["segni"]:
                        if segno == "rifiuto":
                            continue
                        b.agg(3, "$ %s()" % segno)
                    b.ricevi(3, chiave, s["righe"])
                for voce, chiude in (("Back to messages.", False), ("[telefono_minuti_uscita]", True)):
                    b.agg(2, '"%s" if telefono_minuti_attivo():' % voce)
                    b.agg(3, '$ telefono_minuti_riprese[chat_aperta] = "%s"' % punto)
                    if chiude:
                        b.agg(3, "$ telefono_minuti_chiudi = True")
                    b.agg(3, "return")
            b.agg(1, "return")
            out += [""] + b.righe
    return "\n".join(out) + "\n"


for chiave in sys.argv[1:]:
    sorgente = RADICE / "tools/telefono" / (chiave + ".txt")
    testo = componi(chiave, leggi(sorgente.read_text(encoding="utf-8")))
    with io.open(RADICE / "game/percorsi" / ("argomenti_%s.rpy" % chiave), "w", encoding="utf-8", newline="\r\n") as f:
        f.write(testo)
    print("scritto argomenti_%s.rpy" % chiave)
