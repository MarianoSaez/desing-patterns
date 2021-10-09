"""
En este archivo se definen las clases concretas que heredan
(o implementan) los Products o componentes pertenecientes al
tema DARK
"""
from Products import Button, TextBox, Background


class DarkThemeButton(Button):
    def __init__(self):
        super().__init__()
        print(" OSCURO!")


class DarkThemeTextBox(TextBox):
    def __init__(self):
        super().__init__()
        print(" OSCURO!")


class DarkThemeBackground(Background):
    def __init__(self):
        super().__init__()
        print(" OSCURO!")
