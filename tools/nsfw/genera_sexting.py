"""Fa scrivere a LM Studio le due parti mancanti dei Sexting (tools/telefono/<chiave>.txt).

Uso (dalla cartella del repo, con un modello caricato in LM Studio):
    python tools/nsfw/genera_sexting.py ex_d1              una chat
    python tools/nsfw/genera_sexting.py --tutte            tutte e 16
    python tools/nsfw/genera_sexting.py ex_d1 --inserisci  mette nel gioco l'ultima bozza

Le bozze finiscono in tools/nsfw/bozze/<id>.txt: si rileggono, si correggono a mano e solo
poi si inseriscono. Ogni bozza passa un controllo di forma e di limiti; se non passa, il
modello ci riprova fino a tre volte con l'elenco degli errori.
Dopo l'inserimento: python tools/telefono/componi.py <chiave>
"""
import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

SERVER = "http://localhost:1234/v1"
RADICE = Path(__file__).resolve().parents[2]
BOZZE = RADICE / "tools/nsfw/bozze"
SEGNO = "# TESTO DI JODY"
VIETATE = re.compile(
    r"\b(teen\w*|school\w*|schoolgirl\w*|child\w*|kid|kids|underage|minor|minors|little girl|young girl|"
    r"daddy|mommy|rape\w*|forced|unconscious|drugged|drunk|blackmail\w*|"
    r"[1-9] ?years? old|1[0-7] ?years? old)\b", re.I)


SENO = re.compile(r"\b(breasts?|bosom|bust|chest|cleavage|neckline|bra|boobs?|tits?|nipples?|button|buttons|blouse|curves)\b", re.I)


## Sara può riprenderlo anche senza nominarlo: «you've been looking at them», «eyes up».
RIPRESA = re.compile(r"\b(them|they|these|look\w*|star(e|ed|ing)|eyes|notic\w*|shirt|top|strap)\b", re.I)


def sezioni(testo):
    return {m.group(1).strip(): m.group(2).strip()
            for m in re.finditer(r"^## (.+)\n((?:(?!^## ).*\n?)*)", testo, re.M)}


def leggi_chat(id):
    chiave = id.rsplit("_", 1)[0]
    p = RADICE / "tools/telefono" / (chiave + ".txt")
    testo = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    m = re.search(r"^@ %s \|.*\n(?:(?!^@ ).*\n?)*" % re.escape(id), testo, re.M)
    if not m:
        sys.exit("Chat non trovata: " + id)
    return chiave, p, testo, m.group(0)


def campione(chiave):
    chat = leggi_chat(chiave + "_c1")[3]
    righe = [re.sub(r"\s*\[\w+\]", "", r) for r in chat.strip().split("\n")[1:] if r.strip() and not r.startswith("#")]
    return "\n".join(righe)


def messaggio(id, chiave, chat, brief):
    righe = [r for r in chat.strip().split("\n")[1:] if r.strip() and not r.startswith("#")]
    parti = "\n".join(righe).split("\n---\n")
    if len(parti) != 4:
        sys.exit("%s: mi aspettavo apertura e tre parti, ne trovo %d. Forse e' gia' inserita." % (id, len(parti)))
    pulite = [re.sub(r"\s*\[(caldo|frena|rifiuto)\]", "", p) for p in parti]
    return "\n\n".join([
        "VOICE CARD, the other person:\n" + brief["voice " + chiave],
        "VOICE CARD, Sara:\n" + brief["voice sara"],
        "BRIEF:\n" + brief[id],
        "STYLE SAMPLE. Another chat by the same two people. Copy its voice, rhythm and message length, not its content:\n"
        + campione(chiave),
        "EXISTING CHAT. Lines with > or ? are Sara, lines with < are the other person, * is Sara's thought.",
        "OPENING\n" + pulite[0],
        "PART 1\n---\n" + pulite[1],
        "PART 2\n---\n" + pulite[2],
        "(your PART A and PART B go here)",
        "PART 3\n---\n" + pulite[3],
        "Now output PART A and PART B only, in the exact format.",
    ])


def chiedi(conversazione, modello, temperatura, max_token):
    corpo = json.dumps({"model": modello, "messages": conversazione,
                        "temperature": temperatura, "max_tokens": max_token}).encode("utf-8")
    req = urllib.request.Request(SERVER + "/chat/completions", data=corpo,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r:
        scelta = json.load(r)["choices"][0]
    testo = scelta["message"].get("content") or ""
    if not testo.strip() and scelta.get("finish_reason") == "length":
        sys.exit("Il modello ha finito i token mentre ragionava: riprova con --max-token piu' alto.")
    return testo


def modello_caricato():
    with urllib.request.urlopen(SERVER + "/models", timeout=5) as r:
        modelli = [m["id"] for m in json.load(r)["data"] if "embed" not in m["id"]]
    if not modelli:
        sys.exit("Nessun modello in LM Studio: caricane uno e riprova.")
    return modelli[0]


def pulisci(testo):
    testo = re.sub(r"<think>.*?</think>", "", testo.replace("\r", ""), flags=re.S)
    righe = [r.strip() for r in testo.split("\n") if r.strip() and not r.strip().startswith("```")]
    return [r.replace("“", "«").replace("”", "»").replace("’", "'").replace("‘", "'") for r in righe]


def controlla(righe, chat=""):
    errori = []
    for r in righe:
        if r != "---" and not re.match(r"^[<?*] \S", r):
            errori.append("Line not allowed: " + r[:80])
        corpo = r[2:]
        if r != "---":
            if len(corpo) > 200:
                errori.append("Line longer than 200 characters: " + r[:60])
            if re.search(r'["\[\]{}%*]', corpo):
                errori.append("Forbidden character in: " + r[:60])
            v = VIETATE.search(corpo)
            if v:
                errori.append("Forbidden word «%s» in: %s" % (v.group(0), r[:60]))
            if len(corpo) > 25 and r in chat:
                errori.append("Line copied from the existing chat: " + r[:60])
    parti = "\n".join(righe).split("---\n")
    if parti and parti[0].strip() == "":
        parti = parti[1:]
    else:
        errori.append("The answer must start with a line containing only ---")
    if len(parti) != 2:
        errori.append("There must be exactly two parts, found %d" % len(parti))
    for n, p in enumerate(parti, 1):
        segni = "".join(x[0] for x in p.strip().split("\n") if x and x[0] in "<?")
        righe_parte = p.strip().split("\n")
        prima = next((n_r for n_r, x in enumerate(righe_parte) if x.startswith("? ")), len(righe_parte))
        seno = [bool(SENO.search(x)) for x in righe_parte]
        if not any(s for s, x in list(zip(seno, righe_parte))[:prima] if x.startswith("<")):
            errori.append("Part %d: one of the first < lines must plainly be about Sara's breasts (rule 11d)." % n)
        if sum(s for s, x in list(zip(seno, righe_parte))[prima:] if x.startswith("<")) < 2:
            errori.append("Part %d: at least two of the replies must plainly be about Sara's breasts (rule 11d)." % n)
        if not any(s or RIPRESA.search(x) for s, x in zip(seno, righe_parte) if x.startswith("?")):
            errori.append("Part %d: at least one of Sara's answers must take it up (rule 11d)." % n)
        domande = [x for x in p.strip().split("\n") if x.startswith("? ")]
        seguito = [x for x in domande[1:] if re.match(r"\? (exactly|more|keep going|and then|how many|that's it|again)\b", x, re.I)]
        if seguito:
            errori.append("Part %d: the ? lines are ALTERNATIVES, not a sequence. Rewrite so this one answers the first < lines of the part: %s" % (n, seguito[0]))
        if not re.match(r"^<{1,3}(\?<{1,2}){3}$", segni):
            errori.append("Part %d has the wrong shape (%s). It must be 1-3 «<», then three «?» each followed by 1-2 «<»." % (n, segni))
    suoi = [len(r) - 2 for r in righe if r.startswith("< ")]
    if suoi and sum(suoi) / len(suoi) < 55:
        errori.append("The other person's messages are too short on average (%d characters). Aim for 60-180 each." % (sum(suoi) / len(suoi)))
    sare = [r for r in righe if r.startswith("? ")]
    corte = [r for r in sare if len(r[2:].split()) < 4]
    if len(corte) > 1:
        errori.append("Sara's answers must be 4 to 14 words; too short: " + "; ".join(corte[:4]))
    if sum(bool(re.search(r"\b(do not|does not|can not|cannot|I am|you are|I would|it is|I will)\b", r, re.I)) for r in righe) > 2:
        errori.append("Use contractions (don't, I'm, you're, I'd, it's), as people do when they text.")
    if sum(r.startswith("* ") for r in righe) > 2:
        errori.append("More than two thought lines.")
    return errori


def controlla_forma(righe):
    """Per i testi scritti da Jody: solo quello che farebbe rompere il gioco."""
    errori = []
    for n, r in enumerate(righe, 1):
        if r != "---" and not re.match(r"^[<?*] \S", r):
            errori.append("riga %d: deve cominciare con ---, <, ? oppure * e uno spazio: %s" % (n, r[:70]))
            continue
        corpo = re.sub(r"\[(nome_compagno|frena)\]", "", r[2:])
        if re.search(r'["\[\]{}%]', corpo):
            errori.append("riga %d: caratteri vietati (\" [ ] { } %%): %s" % (n, r[:70]))
        if len(corpo) > 260:
            errori.append("riga %d: piu' di 260 caratteri, spezzala in due: %s" % (n, r[:50]))
    if not righe or righe[0] != "---":
        errori.append("la prima riga deve essere ---")
    parti = [x for x in "\n".join(righe).split("---") if x.strip()]
    if not 1 <= len(parti) <= 4:
        errori.append("servono da 1 a 4 parti, ne trovo %d" % len(parti))
    for n, x in enumerate(parti, 1):
        segni = "".join(r[0] for r in x.strip().split("\n") if r and r[0] in "<?")
        if not segni.startswith("<"):
            errori.append("parte %d: comincia sempre l'altro (<)" % n)
        elif not re.match(r"^<{1,5}(\?<{1,4}){2,4}$", segni):
            errori.append("parte %d: prima i messaggi dell'altro, poi da 2 a 4 risposte di Sara (?), e dopo OGNI ? almeno un < (ora e': %s)" % (n, segni))
    return errori


def genera(id, a, sistema, brief, modello):
    chiave, _, _, chat = leggi_chat(id)
    conv = [{"role": "system", "content": sistema},
            {"role": "user", "content": messaggio(id, chiave, chat, brief)}]
    for tentativo in range(1, 4):
        print("%s: tentativo %d..." % (id, tentativo))
        grezzo = chiedi(conv, modello, a.temperatura, a.max_token)
        righe = pulisci(grezzo)
        errori = controlla(righe, chat)
        BOZZE.mkdir(parents=True, exist_ok=True)
        if not errori:
            (BOZZE / (id + ".txt")).write_text("\n".join(righe) + "\n", encoding="utf-8")
            print("  ok: tools/nsfw/bozze/%s.txt (da rileggere)" % id)
            return True
        conv += [{"role": "assistant", "content": grezzo},
                 {"role": "user", "content": "Rejected. Fix every error and output both parts again, complete, "
                                             "in the exact format:\n- " + "\n- ".join(errori[:12])}]
        print("  " + "\n  ".join(errori[:6]))
    (BOZZE / (id + ".scartata.txt")).write_text(grezzo, encoding="utf-8")
    print("  NON VALIDA dopo tre tentativi: tools/nsfw/bozze/%s.scartata.txt" % id)
    return False


def inserisci(id):
    _, p, testo, chat = leggi_chat(id)
    bozza = BOZZE / (id + ".txt")
    if not bozza.exists():
        sys.exit("Nessuna bozza per " + id)
    righe = pulisci(bozza.read_text(encoding="utf-8"))
    errori = controlla_forma(righe)
    if errori:
        sys.exit("La bozza ha errori di forma, non tocco niente:\n- " + "\n- ".join(errori))
    if chat.count("\n---\n") != 3:
        sys.exit(id + ": gia' inserita o struttura diversa, non tocco niente.")
    taglio = chat.rindex("\n---\n")
    nuova = chat[:taglio] + "\n" + "\n".join(righe) + chat[taglio:]
    nuova = "\n".join(r for r in nuova.split("\n") if not r.startswith(SEGNO))
    p.write_text(testo.replace(chat, nuova), encoding="utf-8", newline="\n")
    print("Inserita in %s. Ora: python tools/telefono/componi.py %s" % (p.name, p.stem))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id", nargs="*")
    ap.add_argument("--tutte", action="store_true")
    ap.add_argument("--inserisci", action="store_true")
    ap.add_argument("--controlla", action="store_true", help="controlla la forma delle bozze senza inserirle")
    ap.add_argument("--rifai", action="store_true", help="con --tutte, rifa' anche le bozze gia' valide")
    ap.add_argument("--modello")
    ap.add_argument("--temperatura", type=float, default=0.8)
    ap.add_argument("--max-token", type=int, default=6000)
    a = ap.parse_args()
    brief = sezioni((RADICE / "docs/nsfw/brief/sexting.md").read_text(encoding="utf-8").replace("\r\n", "\n"))
    ids = [k for k in brief if re.search(r"_d\d+$", k)] if a.tutte else a.id
    if a.tutte and not a.inserisci and not a.controlla and not a.rifai:
        ids = [i for i in ids if not (BOZZE / (i + ".txt")).exists()]
    if not ids:
        ap.error("indica una chat (per esempio ex_d1) oppure --tutte")
    for id in ids:
        if id not in brief:
            sys.exit("Nessuna scaletta per " + id)
    if a.controlla:
        for id in ids:
            f = BOZZE / (id + ".txt")
            errori = controlla_forma(pulisci(f.read_text(encoding="utf-8"))) if f.exists() else ["manca il file"]
            print("%s: %s" % (id, "a posto" if not errori else "\n  - " + "\n  - ".join(errori)))
        return
    if a.inserisci:
        for id in ids:
            inserisci(id)
        return
    sistema = (RADICE / "tools/nsfw/prompt_sexting.md").read_text(encoding="utf-8")
    modello = a.modello or modello_caricato()
    print("Modello:", modello)
    esiti = {id: genera(id, a, sistema, brief, modello) for id in ids}
    print("Valide %d su %d" % (sum(esiti.values()), len(esiti)))


if __name__ == "__main__":
    main()
