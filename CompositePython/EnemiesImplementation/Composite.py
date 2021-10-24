from Component import Component
from Leaf import Leaf


class Composite(Component):
    """
    Esta clase sera heredada por enemigos compuestos por otros enemigos.
    Ademas incluye una logica en la cual solo puede recibir daño, si este
    ya no posee hijos "vivos"
    """
    def __init__(self, hp, defense, parent):
        self.hp = hp
        self.defense = defense
        self.parent = parent
        self.children = []

    def takeDamage(self, attack: int) -> int:
        self.checkChildren()

        # Si ya no hay hijos entonces el Composite sufre daño
        if len(self.children) == 0:
            realDamage = attack * 1/self.defense
            self.hp -= realDamage

            print(f"{type(self)} : -{realDamage} !")

            if self.hp <= 0:
                print(f"{type(self)} eliminado !")
            
            return realDamage

        else:
            for child in self.children:
                child.takeDamage(attack/len(self.children))

    
    def checkChildren(self) -> None:
        for i in range(len(self.children)):
            if self.children[i].hp <= 0:
                self.children.pop(i)
    