## =============================================================================
## PERCORSI — chat, messaggi in entrata e uscite, un file per personaggio
## =============================================================================
## Qui va il «codice del percorso» (docs/telefono-e-percorsi-dinamici.md, 10.9).
## Un file per percorso: chat_daniel.rpy, chat_simon.rpy, chat_howard.rpy,
## chat_editore.rpy (Magnus), chat_amica.rpy (Joanie), chat_ex.rpy (Jacob),
## chat_amico.rpy (Darius), chat_capa.rpy (Barbara).
##
## Modello di uno step (N = numero dello step, da 1):
##
##   label chat_daniel_1:
##       $ msg("sara", "Thank you for dinner. Josh says you liked the restaurant.")
##       return
##
##   label chat_daniel_1_risposta:
##       $ msg("daniel", "I liked the company more.")
##       menu (screen="scelta_telefono"):
##           "A smiley.":
##               $ msg("sara", ":)")
##               $ chat_fine("daniel")
##           "«Behave.»":
##               $ msg("sara", "Behave.")
##               $ chat_fine("daniel", caldo=True)
##       return
##
##   label chat_daniel_entrata:      (lui scrive per primo; non usa lo slot)
##   label uscita_daniel:            (la serata alternativa, gradino C o più)
##
## Le varianti delle scene fisse leggono gradino("daniel"):
##   sotto CONFIDENZA com'è scritta · CONFIDENZA una-due frasi · COMPLICI/INTIMI cambia.
## Se un label manca, il gioco mostra un segnaposto e va avanti.
