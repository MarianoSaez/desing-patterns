from gym import Gym
from persona import Persona


def main():
    # Creamos persona
    per1 = Persona("Mariano", "Saez", 42518552)

    # Creamos gym y seteamos cuota
    gym1 = Gym()
    gym1.setCuota(1000)

    # Asociamos gym y gimnasio
    per1.setGym(gym1)

    # Agregamos el suscriptor
    gym1.addSuscriptor(per1)

    # Modificamos valor de cuota
    gym1.setCuota(1001)  # Output: (per1) --> La cuota es: $1001

    # Quitamos para comprobar que no se notifica el cambio
    gym1.removeSuscriptor(per1)
    gym1.setCuota(1200)  # No hay Output


if __name__ == "__main__":
    main()
