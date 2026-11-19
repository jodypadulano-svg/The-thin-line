#!/usr/bin/env bash
## Lancia lint e test di Ren'Py senza aspettare la chiusura.
## Su questa macchina Ren'Py finisce i test in pochi secondi ma poi non esce:
## qui si legge l'output e si chiude il processo appena compare «Status:».
##
## Uso (dalla cartella del gioco):
##   tools/test.sh                      lint + episodio1 + debug_salta + telefono
##   tools/test.sh episodio1 telefono   solo queste suite (niente lint)
##   tools/test.sh lint                 solo il lint
## Variabile RENPY per un SDK diverso. Esce con 1 se qualcosa fallisce.

RENPY="${RENPY:-/c/Users/Jody/RenPy/renpy-8.5.3-sdk/renpy.exe}"
cd "$(dirname "$0")/.." || exit 1

if [ $# -eq 0 ]; then
    set -- lint episodio1 debug_salta telefono
fi

esito=0
log="$(mktemp)"

for suite in "$@"; do
    if [ "$suite" = "lint" ]; then
        echo "=== lint"
        "$RENPY" . lint > "$log" 2>&1
        if grep -q -E "^game/.*:[0-9]+ " "$log"; then
            grep -E "^game/.*:[0-9]+ " "$log"
            esito=1
        else
            echo "pulito"
        fi
        continue
    fi

    echo "=== $suite"
    inizio=$SECONDS
    "$RENPY" . test "$suite" > "$log" 2>&1 &
    pid=$!
    winpid="$(cat /proc/$pid/winpid 2>/dev/null)"
    ## Aspetta il riepilogo (o la fine del processo), al massimo 10 minuti.
    while kill -0 "$pid" 2>/dev/null && ! grep -q "Status:" "$log"; do
        if [ $((SECONDS - inizio)) -gt 600 ]; then
            echo "TIMEOUT dopo 10 minuti"
            esito=1
            break
        fi
        sleep 1
    done
    ## Lascia scrivere le ultime righe, poi chiudi Ren'Py.
    sleep 1
    if kill -0 "$pid" 2>/dev/null; then
        [ -n "$winpid" ] && taskkill //F //PID "$winpid" > /dev/null 2>&1
        kill "$pid" 2>/dev/null
    fi
    wait "$pid" 2>/dev/null
    grep -E "\[rpytest\] (Test cases|Status)|FAILED|Error|Traceback" "$log" | head -20
    grep -q "Status: PASSED" "$log" || esito=1
    echo "($((SECONDS - inizio)) s)"
done

rm -f "$log"
exit $esito
