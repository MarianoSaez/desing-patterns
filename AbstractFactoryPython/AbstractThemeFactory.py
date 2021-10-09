from Products import Button, TextBox, Background


class AbstractThemeFactory():
    """
    Esta interfaz declara los metodos que las fabricas concretas deberan implementar
    para generar las familias de productos o componentes en este caso particular
    """
    def createButton(self) -> Button:
        raise NotImplementedError

    def createTextBox(self) -> TextBox:
        raise NotImplementedError

    def createBackground(self) -> Background:
        raise NotImplementedError
