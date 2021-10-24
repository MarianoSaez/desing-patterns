from Leaf import Leaf
from Composite import Composite
from Client import Client
from GraphicElements import *


if __name__ == "__main__":
    c = Client()

    # Creamos una serie de figuras con atributos
    char = Character(100, 25, 0, 0)
    hat = Hat("Rojo", 10, 10, 0, 100)
    sword = Sword(75, 40, 5, 10, 50)

    armor = Armor(100, 100, 20, 0, 0)
    chest = Chest("Verde", 40, 50, 25, 0, 50)
    pants = ArmorPants("Azul", 40, 50, 25, 0, 0)
    bracelet = Bracelet("Amarillo", 20, 10, 10, 0, 0)

    # Las agregamos a sus respectivos composites
    armor.addChild(chest)
    armor.addChild(pants)
    armor.addChild(bracelet)

    char.addChild(hat)
    char.addChild(sword)
    char.addChild(armor)

    # El cliente ejecuta la accion de mover al personaje
    c.displace(char, 100, 0)