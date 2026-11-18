## =============================================================================
## PERCORSI — i discorsi al telefono, un file per personaggio
## =============================================================================
## Qui va il «codice del percorso» (docs/telefono-e-percorsi-dinamici.md, sez. 11).
## Un file per percorso: chat_daniel.rpy, chat_simon.rpy, chat_howard.rpy,
## chat_editore.rpy (Magnus), chat_amica.rpy (Joanie), chat_ex.rpy (Jacob),
## chat_amico.rpy (Darius), chat_capa.rpy (Barbara).
##
## 1) Registrare il discorso (gradino minimo, condizione, flirt):
##
##   init python:
##       discorso("simon_dieta", "simon", CONOSCENTI)
##       discorso("simon_festa", "simon", CONFIDENZA, se="fatto('ep1_festa_simon')")
##       discorso("simon_foto", "simon", COMPLICI, flirt=True)
##       discorso("simon_notte", "simon", INTIMI, se="oltre_soglia('simon')", flirt=True)
##
## 2) Scriverlo a pezzi. Fra un pezzo e l'altro c'è un punto di interruzione:
##    lì l'altro può smettere di rispondere (a caso, secondo il carattere) o
##    Sara può mettere giù il telefono. Si riprende dal pezzo dopo.
##
##   label chat_simon_dieta:              (facoltativo) il primo messaggio di Sara
##       $ msg("sara", "Quick question: is pizza allowed on rest days?")
##       return
##
##   label chat_simon_dieta_entrata:      (facoltativo) se è lui a scrivere per primo
##       $ msg("simon", "Did you eat breakfast today? Be honest.")
##       return
##
##   label chat_simon_dieta_1:            pezzo 1: comincia con lui, finisce con Sara
##       $ msg("simon", "Pizza is always allowed. Ask me how many slices.")
##       menu (screen="scelta_telefono"):
##           "«How many?»":
##               $ msg("sara", "How many?")
##           "«Two. I'm a professional.»" (confidence=25):
##               $ msg("sara", "Two. I'm a professional.")
##               $ caldo()                     # +2 Interest a fine discorso
##       return
##
##   label chat_simon_dieta_2:            pezzo 2 (l'ultimo: non esiste un _3)
##       $ msg("simon", "Two is correct. See you Thursday.")
##       return
##
##   Nei discorsi di flirt c'è sempre una risposta per smorzare:  $ frena()
##
## Fine discorso: Interest +1 (+2 se caldo), flag «chat_<id>» (es. fatto("chat_simon_dieta"))
## per le varianti delle scene fisse; dai complici in su si sceglie se cancellare la chat.
## Se un personaggio non ha più discorsi disponibili, in rubrica diventa grigio.
