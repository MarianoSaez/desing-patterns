"""
En este archivo se definen las ConcreteFactories que implementaran los metodos
de fabricacion de los distintos productos o componentes.
"""
from AbstractThemeFactory import AbstractThemeFactory
from LightThemeFamily import LightThemeButton, LightThemeTextBox, LightThemeBackground
from DarkThemeFamily import DarkThemeButton, DarkThemeTextBox, DarkThemeBackground
from MonokaiThemeFamily import MonokaiThemeButton, MonokaiThemeTextBox, MonokaiThemeBackground


class LightThemeFactory(AbstractThemeFactory):
    def createButton(self):
        return LightThemeButton()

    def createTextBox(self):
        return LightThemeTextBox()

    def createBackground(self):
        return LightThemeBackground()


class DarkThemeFactory(AbstractThemeFactory):
    def createButton(self):
        return DarkThemeButton()

    def createTextBox(self):
        return DarkThemeTextBox()

    def createBackground(self):
        return DarkThemeBackground()


class MonokaiThemeFactory(AbstractThemeFactory):
    def createButton(self):
        return MonokaiThemeButton()

    def createTextBox(self):
        return MonokaiThemeTextBox()

    def createBackground(self):
        return MonokaiThemeBackground()
