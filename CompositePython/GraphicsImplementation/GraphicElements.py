from Composite import Composite
from Leaf import Leaf


class Character(Composite):
    def __init__(self, height, width, x, y):
        self.height = height
        self.width = width
        super().__init__(x, y)

class Hat(Leaf):
    def __init__(self, color, height, width, x, y):
        self.height = height
        self.width = width
        self.color = color
        super().__init__(x, y)

class Sword(Leaf):
    def __init__(self, ATK, height, width, x, y):
        self.ATK = ATK
        self.height = height
        self.width = width
        super().__init__(x, y)

class Bag(Leaf):
    def __init__(self, height, width, x, y):
        self.height = height
        self.width = width
        super().__init__(x, y)

class Armor(Composite):
    def __init__(self, DEF, height, width, x, y):
        self.DEF = DEF
        self.height = height
        self.width = width
        super().__init__(x, y)

class Chest(Leaf):
    def __init__(self, color, DEF, height, width, x, y):
        self.DEF = DEF
        self.height = height
        self.width = width
        self.color = color
        super().__init__(x, y)

class Bracelet(Leaf):
    def __init__(self, color, DEF, height, width, x, y):
        self.DEF = DEF
        self.height = height
        self.width = width
        self.color = color
        super().__init__(x, y)

class ArmorPants(Leaf):
    def __init__(self, color, DEF, height, width, x, y):
        self.DEF = DEF
        self.height = height
        self.width = width
        self.color = color
        super().__init__(x, y)
