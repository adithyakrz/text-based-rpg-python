from Charecter import Charecter

class Boss(Charecter):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health*2, attack_power)
    def mega_attack(self,enemy):
        enemy.health -= self.attack_power * 2
        print(f"Mega Attack!!! Damage: {self.attack_power*2}")