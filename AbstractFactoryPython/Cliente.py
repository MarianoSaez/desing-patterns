from AbstractThemeFactory import AbstractThemeFactory


class Cliente():
    def __init__(self, factory):
        print("Creando GUI...")
        self.factory = factory
        self.button = factory.createButton()
        self.textbox = factory.createTextBox()
        self.background = factory.createBackground()

