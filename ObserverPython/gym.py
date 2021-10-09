from subject import Subject


class Gym(Subject):
    def __init__(self, cuota=0):
        self.cuota = cuota

    def setCuota(self, cuota):
        print("\nCambiando valor de la cuota...")
        self.cuota = cuota
        self.notifySuscriptores()

    def getCuota(self):
        return self.cuota
