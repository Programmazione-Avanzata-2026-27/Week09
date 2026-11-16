from database.dao import Dao

class Model:

    def __init__(self):
        pass

    def get_statistiche(self, serate):
        return Dao.read_statistiche(serate)

    def get_programma_ottimo(self, serate):
        lista_film_serate = Dao.read_film_serate(serate)
        for f in lista_film_serate:
            print(f)

        # Qui dovrei determinare il programma ottimo usando il param.
        # serate e lista_film_serate: uso una strategia ricorsiva
        if True:
            pass
        else:
            pass

        # Restituisco il programma ottimo