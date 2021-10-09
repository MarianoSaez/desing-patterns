from Creator import Creator
from Product import Product
from random import randint
from ConcreteProducts import UselessProduct, CommonProduct, RareProduct, LegendaryProduct
"""
Aqui se definen las distintas factory's que implementan la interfaz
Creator, ademas de la logica de creacion/fabricacion de los
ConcreteProducts.
"""


class RandomProductCreator(Creator):
    def factoryMethod(self) -> Product:
        randNum = randint(0,10)
        if randNum < 3:
            return UselessProduct()
        elif 3 <= randNum < 6:
            return CommonProduct()
        elif 6 <= randNum < 9:
            return RareProduct()
        else:
            return LegendaryProduct()


class OnlyLegendaryProductCreator(Creator):
    def factoryMethod(self) -> Product:
        return LegendaryProduct()


class NotLowCatProductCreator(Creator):
    def factoryMethod(self) -> Product:
        if randint(0,1) == 0:
            return RareProduct()
        else:
            return LegendaryProduct()
