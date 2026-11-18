## =============================================================================
## ABITI DI SARA (A10)
## =============================================================================
## Gli abiti li sceglie la storia: per ogni occasione Sara indossa l'abito più
## avanzato che ha sbloccato. Gli abiti sicuri di sé chiedono Confidence; quelli
## provocanti chiedono anche Corruption.
##
## Uso nelle scene:
##     $ vestito = abito("palestra")      # restituisce l'Abito da usare
##     $ cg("Sara entra in palestra con " + vestito.descrizione)
## Quando arriveranno le immagini, l'id dell'abito diventa parte del nome del
## file (es. "sara palestra_base").
##
## Nuovi abiti: aggiungili in fondo alla lista della loro occasione, dal più
## sobrio al più audace. L'id non va mai cambiato.

init -5 python:

    class Abito(object):
        def __init__(self, id, occasione, nome, descrizione, confidence=0, corruption=0):
            self.id = id
            self.occasione = occasione
            self.nome = nome
            self.descrizione = descrizione
            self.confidence = confidence
            self.corruption = corruption

        @property
        def sbloccato(self):
            return store.sara_confidence >= self.confidence and store.sara_corruption >= self.corruption

    ## Abiti iniziali, sobri come prevede la bibbia. Gli altri li propone Claude
    ## scrivendo le scene, e li approva Jody.
    ABITI = [
        Abito("casa_base", "casa", "Comfy", "a soft sweater and sweatpants"),
        Abito("palestra_base", "palestra", "First time", "a baggy t-shirt and black leggings"),
        Abito("ufficio_base", "ufficio", "Office", "a white blouse and grey trousers"),
        Abito("sera_base", "sera", "Simply elegant", "a simple black knee-length dress"),
    ]

    def abito(occasione):
        """L'abito più avanzato sbloccato per questa occasione."""
        scelti = [a for a in ABITI if a.occasione == occasione and a.sbloccato]
        a = scelti[-1]
        if a.id not in store.abiti_visti:
            store.abiti_visti.add(a.id)
            if not a.id.endswith("_base"):
                _annuncia_testo("New outfit: " + a.nome)
        return a

    def abiti_sbloccati():
        return [a for a in ABITI if a.sbloccato]

default abiti_visti = set()
