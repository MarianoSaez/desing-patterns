"""
Esta clase es la interfaz que declara el metodo que implementaran
las clases concretas Composite y Leaf
"""
class Component():
    def takeDamage(self, attack: int) -> int:
        raise NotImplementedError