# Simulatore del primo mese (versione minima).
# Gioca il mese di tools/piani/mese1.py con diversi «giocatori finti» e con
# migliaia di partite casuali, e controlla i risultati contro la mappa a tappe.
# Uso: py tools/piani/simulatore.py docs/simulazione-mese-1.md
import sys, re, random, runpy, io, os, collections

QUI = os.path.dirname(os.path.abspath(__file__))
import tempfile
_out, _argv = sys.stdout, sys.argv
sys.stdout = io.StringIO()
sys.argv = ["mese1.py", os.path.join(tempfile.gettempdir(), "mese1_simulatore.md")]  # mese1.py scrive il suo .md: qui va in un file temporaneo
G = runpy.run_path(os.path.join(QUI, "mese1.py"), run_name="dati")
sys.stdout, sys.argv = _out, _argv
D = G["D"]

PERCORSI = ["Simon", "Jacob", "Darius", "Daniel", "Joanie", "Magnus", "Howard", "Barbara"]
SOGLIA = {"Simon": 15, "Jacob": 25, "Darius": 35, "Daniel": 45, "Joanie": 55, "Magnus": 65, "Howard": 75, "Barbara": 85}
START = {"Corr": 0, "Conf": 20, "Susp": 0, "Josh": 80}
# Scelte che creano un segreto verso Josh.
SEGRETI = {("8 Lun", "Non dirlo"), ("13 Sab", "Tenerlo segreto"), ("23 Mar", "«Esco con una collega»")}

# Condizioni sulle domande: (giorno, inizio della domanda) -> funzione(stato, fatte) -> bool
def scelto(fatte, giorno, q, opzione):
    return fatte.get((giorno, q)) == opzione
COND = {
    ("4 Gio", "All'aperitivo: Barbara"): lambda s, f: scelto(f, "1 Lun", "Jessica la invita all'aperitivo di giovedì", "Accettare"),
    ("4 Gio", "All'aperitivo"): lambda s, f: scelto(f, "1 Lun", "Jessica la invita all'aperitivo di giovedì", "Accettare"),
    ("4 Gio", "Se ha rifiutato"): lambda s, f: not scelto(f, "1 Lun", "Jessica la invita all'aperitivo di giovedì", "Accettare"),
    ("8 Lun", "Simon le sistema"): lambda s, f: scelto(f, "8 Lun", "Entrare da sola?", "Entrare"),
    ("8 Lun", "A casa"): lambda s, f: scelto(f, "8 Lun", "Entrare da sola?", "Entrare"),
    ("18 Gio", "Andare da Howard?"): lambda s, f: f.get(("9 Mar", "«Possiamo vederci più spesso?»"), "").startswith(("«Certo", "«Quando")),
    ("18 Gio", "Da Howard"): lambda s, f: scelto(f, "18 Gio", "Andare da Howard?", "Sì"),
    ("20 Sab", "Con Magnus"): lambda s, f: scelto(f, "15 Lun", "Mandarle?", "Sì"),
    ("23 Mar", ""): lambda s, f: scelto(f, "21 Dom", "Rispondere?", "Sì"),
    ("26 Ven", "Esito"): lambda s, f: scelto(f, "23 Mar", "Cosa dire a Josh", "«Esco con una collega»"),
    ("28 Dom", "Se c'è il confronto"): lambda s, f: s["Susp"] >= 8,
}
# Esiti decisi dal gioco, non dal giocatore.
AUTO = {("26 Ven", "Esito (non sceglie il giocatore)"): lambda s: "Howard tace" if s["Howard"] >= 5 else "Howard parla a Josh"}

def condizione(giorno, q, s, fatte):
    for (g, pref), fn in COND.items():
        if g == giorno and q.startswith(pref):
            if not fn(s, fatte):
                return False
    return True

REQ = re.compile(r"🔒\s*(Corr|Conf|Josh)\s*(\d+)")
def disponibile(opzione, s):
    m = REQ.search(opzione)
    return not m or s[m.group(1)] >= int(m.group(2))

def gioca(strategia, rng=None):
    s = collections.Counter(START)
    fatte, segreti, log = {}, 0, []
    for giorno, fasce in D:
        for fascia, scena, chi, gruppi in fasce:
            for f, q, opts in gruppi:
                if not condizione(giorno, q, s, fatte):
                    continue
                if (giorno, q) in AUTO:
                    nome = AUTO[(giorno, q)](s)
                    scelta = [o for o in opts if o[0] == nome][0]
                else:
                    valide = [o for o in opts if disponibile(o[0], s)]
                    scelta = strategia(valide, s, rng)
                fatte[(giorno, q)] = scelta[0]
                if (giorno, scelta[0]) in SEGRETI:
                    segreti += 1
                for k, v in scelta[1].items():
                    s[k] = max(0, min(100, s[k] + v))
                log.append((giorno, q, scelta[0]))
    s["Segreti"] = segreti
    return s, log

def punteggio(pesi):
    def strategia(valide, s, rng):
        return max(valide, key=lambda o: sum(pesi.get(k, 0) * v for k, v in o[1].items()))
    return strategia

def casuale(valide, s, rng):
    return rng.choice(valide)

STRATEGIE = {
    "Fedele (prudente al massimo)": punteggio({"Josh": 3, "Corr": -10, "Susp": -5, **{p: -1 for p in PERCORSI}}),
    "Spinge tutto (Corruption al massimo)": punteggio({"Corr": 10, **{p: 1 for p in PERCORSI}, "Josh": -1}),
}
for p in PERCORSI:
    STRATEGIE["Punta su " + p] = punteggio({p: 10, "Corr": 2, "Conf": 1})

def tappa(s, p):
    i, c = s[p], s["Corr"]
    if i >= 65 and c >= SOGLIA[p] + 10: return "7b"
    if i >= 60 and c >= SOGLIA[p] + 6: return "7a"
    if i >= 55 and c >= SOGLIA[p] + 3: return "6b"
    if i >= 50 and c >= SOGLIA[p]: return "6a"
    if i >= 35: return "5"
    if i >= 20: return "4"
    return "≤3"

def fedele_ok(s):
    return s["Corr"] <= 10 and s["Josh"] >= 90 and all(s[p] < 20 for p in PERCORSI) and s["Segreti"] == 0 and s["Susp"] <= 5

VAR = ["Corr", "Conf", "Susp", "Josh"] + PERCORSI

def main(out):
    righe = []
    w = righe.append
    w("# The Thin Line — Simulazione del primo mese")
    w("")
    w("Generato da `tools/piani/simulatore.py` sui dati di `tools/piani/mese1.py`. **Versione minima:** solo il primo mese, giocatori finti e partite casuali.")
    w("")
    w("## 1. Giocatori finti")
    w("")
    w("| Giocatore | " + " | ".join(VAR) + " | Segreti | Tappe raggiunte |")
    w("|---|" + "---|" * (len(VAR) + 2))
    for nome, strat in STRATEGIE.items():
        s, _ = gioca(strat)
        tappe = ", ".join("{} {}".format(p, tappa(s, p)) for p in PERCORSI if tappa(s, p) != "≤3") or "nessuna oltre la 3"
        w("| {} | {} | {} | {} |".format(nome, " | ".join(str(s[k]) for k in VAR), s["Segreti"], tappe))
    w("")
    rng = random.Random(1)
    N = 5000
    ris = [gioca(casuale, rng)[0] for _ in range(N)]
    w("## 2. {} partite casuali".format(N))
    w("")
    w("| Variabile | Minimo | Mediana | 90° percentile | Massimo |")
    w("|---|---|---|---|---|")
    for k in VAR + ["Segreti"]:
        v = sorted(r[k] for r in ris)
        w("| {} | {} | {} | {} | {} |".format(k, v[0], v[N // 2], v[int(N * 0.9)], v[-1]))
    w("")
    w("| Controllo | Partite casuali |")
    w("|---|---|")
    for p in PERCORSI:
        a4 = sum(1 for r in ris if r[p] >= 20) / N
        a6 = sum(1 for r in ris if tappa(r, p) in ("6a", "6b", "7a", "7b")) / N
        w("| {}: tappa 4 (Interest 20) / bacio (6a) | {:.0%} / {:.0%} |".format(p, a4, a6))
    w("| Corruption ≥ 15 (soglia di Simon) | {:.0%} |".format(sum(1 for r in ris if r["Corr"] >= 15) / N))
    w("| Corruption ≥ 25 (soglia di Jacob e della scintilla di Darius) | {:.0%} |".format(sum(1 for r in ris if r["Corr"] >= 25) / N))
    w("| Ancora compatibile col finale fedele | {:.1%} |".format(sum(1 for r in ris if fedele_ok(r)) / N))
    w("")
    note = os.path.join(QUI, "simulazione-note.md")  # commento a mano, aggiunto in coda
    if os.path.exists(note):
        righe += ["", open(note, encoding="utf-8").read().rstrip()]
    open(out, "w", encoding="utf-8", newline="").write("\n".join(righe) + "\n")

if __name__ == "__main__":
    main(sys.argv[1])
