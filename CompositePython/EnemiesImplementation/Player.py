class Player:
    def attack(self, enemy, damage) -> None:
        enemy.takeDamage(damage)