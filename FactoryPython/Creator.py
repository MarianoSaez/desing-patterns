from Product import Product
"""
Interfaz implementada por los ConcreteCreators en la que se declaran
los metodos que permiten crear Products segun la logica que implementen
los ContecreteCreators por su cuenta.
"""


class Creator:
    def factoryMethod(self) -> Product:
        raise NotImplementedError
