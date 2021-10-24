"""
Este ejemplo del patron composite simula una funcionalidad de recibir daño
de un enemigo compuesto por otros enemigos mas pequeños. La interfaz Component
declara el metodo takeDamage() : int el cual retorna el daño sufrido por el
enemigo despues de restar su armadura al ataque.
"""
from RobotStructure import Robot, RobotArms, RobotLegs, RobotHead
from Player import Player


if __name__ == "__main__":
    p = Player()

    # Crear la estructura del robot
    robot = Robot()

    robot.children.append(RobotArms(robot))

    robot.children.append(RobotLegs(robot))

    robot.children.append(RobotHead(robot))

    for i in range(30):
        print(f"{i}-esimo ataque")
        p.attack(robot, 1000)


