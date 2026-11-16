from model.model import Model

class Controller:
    def __init__(self, view, model: Model):
        self._view = view
        self._model = model

    def handle_statistiche(self, e):

        serate = 0
        try:
            serate = int(self._view.dd_serate.value)
        except TypeError:
            self._view.avviso("Seleziona il numero di serate")
        risultato = self._model.get_statistiche(serate)
        self._view.mostra(risultato)


    def handle_programma(self, e):
        serate = 0
        try:
            serate = int(self._view.dd_serate.value)
        except TypeError:
            self._view.avviso("Seleziona il numero di serate")
        risultato = self._model.get_programma_ottimo(serate)
        self._view.mostra(["Programma ottimo"])
