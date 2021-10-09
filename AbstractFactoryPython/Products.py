"""
En este archivo se definen las clases abstractas
(tambien pueden ser interfaces) que heredaran (o implementaran)
los productos concretos, o en este caso, componentes concretos
"""
class Button():
    def __init__(self):
        print("Soy un boton", end="")


class TextBox():
    def __init__(self):
        print("Soy un textbox", end="")


class Background():
    def __init__(self):
        print("Soy un fondo", end="")