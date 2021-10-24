from Component import Component


class Leaf(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.children = []
    
    def move(self, x_distance : float, y_distance : float, k : int) -> None:
        print(k*'\t' + f"{type(self)} : ( {self.x}, {self.y} ) --> ", end="")
        # Muevo al objeto hijo
        self.x += x_distance
        self.y += y_distance
        print(f"( {self.x}, {self.y} )")


