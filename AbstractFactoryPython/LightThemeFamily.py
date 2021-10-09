"""
En este archivo se definen las clases concretas que heredan
(o implementan) los Products o componentes pertenecientes al
tema LIGHT
"""
from Products import Button, TextBox, Background


class LightThemeButton(Button):
    def __init__(self):
        super().__init__()
        print(" CLARO!")


class LightThemeTextBox(TextBox):
    def __init__(self):
        super().__init__()
        print(" CLARO!")


class LightThemeBackground(Background):
    def __init__(self):
        super().__init__()
        print(" CLARO!")
