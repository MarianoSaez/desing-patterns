from Cliente import Cliente
from ConcreteFactories import LightThemeFactory, DarkThemeFactory, MonokaiThemeFactory
"""
El ejemplo consiste en mostrar las implementacion del patron Abstract Factory
para la creacion de familias de objetos relacionados entre si. Como lo son
componentes de una aplicacion capaz de cambiar los temas/colores de los
mismos, segun algun criterio determinado por el lado del cliente, como
puede ser sistemas operativo, hora del dia o eleccion
"""

if __name__ == "__main__":
    # ... de alguna forma se determino que se usara...
    factory = MonokaiThemeFactory()
    c = Cliente(factory)
