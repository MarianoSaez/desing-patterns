from Composite import Composite
from Leaf import Leaf


"""
La clase Robot se compone de las partes del cuerpo del robot
y para atacar al robot, primero es necesario eliminar todas las
demas partes
"""
class Robot(Composite):
    def __init__(self):
        super().__init__(100, 75, None)


"""
Extremidades del robot
"""
class RobotArms(Leaf):
    def __init__(self, parent):
        super().__init__(25, 30, parent)
        self.parent = parent


class RobotLegs(Leaf):
    def __init__(self, parent):
        super().__init__(50, 60, parent)


class RobotHead(Leaf):
    def __init__(self, parent):
        super().__init__(100, 100, parent)
