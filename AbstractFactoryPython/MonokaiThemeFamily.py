"""
En este archivo se definen las clases concretas que heredan
(o implementan) los Products o componentes pertenecientes al
tema MONOKAI
"""
from Products import Button, TextBox, Background


class MonokaiThemeButton(Button):
    def __init__(self):
        super().__init__()
        print(" MONOKAI!")


class MonokaiThemeTextBox(TextBox):
    def __init__(self):
        super().__init__()
        print(" MONOKAI!")


class MonokaiThemeBackground(Background):
    def __init__(self):
        super().__init__()
        print(" MONOKAI!")
