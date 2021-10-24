from Component import Component


class Composite(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.children = []
    
    def move(self, x_distance : float, y_distance : float, k: int) -> None:
        print(k*'\t' + f"{type(self)} : ( {self.x}, {self.y} ) --> ", end="")

        # Muevo al objeto compuesto
        self.x += x_distance
        self.y += y_distance
        print(f"( {self.x}, {self.y} )")

        # Envio la orden a los hijos
        for child in self.children:
            child.move(x_distance, y_distance, k+1)

    def addChild(self, child : Component) -> None:
        self.children.append(child)

    def removeChild(self, child : Component) -> None:
        self.children.remove(child)
