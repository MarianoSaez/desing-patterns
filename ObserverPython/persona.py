from observer import Observer


class Persona(Observer):
    def __init__(self, nombre, apellido, dni, gym=None):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.gym = gym

    def setGym(self, gym):
        self.gym = gym

    def update(self):
        print("\nReaccionando al cambio de la cuota...")
        print("%s: La nueva cuota es $%d" % (self.nombre, self.gym.getCuota()))
