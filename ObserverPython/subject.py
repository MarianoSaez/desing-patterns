from observer import Observer


class Subject():
    observadoresGym = []

    def addSuscriptor(self, observerGym: Observer):
        print("\nAñadiendo nuevo suscriptor...")
        self.observadoresGym.append(observerGym)

    def removeSuscriptor(self, observerGym: Observer):
        self.observadoresGym.remove(observerGym)

    def notifySuscriptores(self):
        print("\nNotificando suscriptores...")
        for i in self.observadoresGym:
            i.update()
