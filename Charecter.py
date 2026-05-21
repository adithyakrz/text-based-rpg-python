from random import randint
class Charecter:
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self,enemy):
        upper_limit = max(1, enemy.health // 4)
        self.extra_damage = randint(0,upper_limit)
        enemy.health -= self.attack_power + self.extra_damage
        if self.extra_damage>=enemy.health/8:
            print(f"Critical Hit!! Damage: {self.attack_power + self.extra_damage}")
        else:
            print(f"Hit! Damage: {self.attack_power + self.extra_damage}")