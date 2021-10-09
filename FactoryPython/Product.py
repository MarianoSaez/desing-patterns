"""
Clase abstracta que representa el tipo de entidad creada
por los ConcreteCreators
"""


class Product():
    id = 0

    def __init__(self):
        self.nombre = f"Producto No. {type(self).id} - Tipo {self.__class__}"
        type(self).id += 1
    