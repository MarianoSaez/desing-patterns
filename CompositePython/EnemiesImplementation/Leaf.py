from Component import Component


class Leaf(Component):
    """
    Esta clase sera heredada por enemigos simples.
    Esta clase recibira el daño de los ataques realizados a su
    componente padre repartido de forma igual para todos los hijos
    """
    def __init__(self, hp, defense, parent):
        self.hp = hp
        self.defense = defense
        self.parent = parent

    def takeDamage(self, attack: int) -> int:
        realDamage = attack * 1/self.defense
        self.hp -= realDamage
        print(f"{type(self)} : -{realDamage} !")

        if self.hp <= 0:
            print(f"{type(self)} eliminado !")
            self.parent.children.remove(self)

        return realDamage