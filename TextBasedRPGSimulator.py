from random import randint
from random import random
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
class Boss(Charecter):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health*2, attack_power)
    def mega_attack(self,enemy):
        enemy.health -= self.attack_power * 2
        print(f"Mega Attack!!! Damage: {self.attack_power*2}")
print("Player info:")
name = input("Name: ")
health = int(input("Health: "))
attack_power = int(input("Attack Power: "))
player = Charecter(name,health,attack_power)
print("Boss info:")
name = input("Name: ")
health = int(input("Health: "))
attack_power = int(input("Attack Power: "))
boss = Boss(name,health,attack_power)
while True:
    print(f"{player.name} Attacks")
    player.attack(boss)
    if boss.health <= 0:
        print(f"Final Status: {player.name} HP: {player.health} | {boss.name} HP: {boss.health}\n")
        print(f"{player.name} Wins the match against {boss.name}!")
        break
        
    if random() < 0.3:
        print(f"{boss.name} Attacks")
        boss.mega_attack(player)
    else:
        print(f"{boss.name} Attacks")
        boss.attack(player)
        
    if player.health <= 0:
        print(f"Final Status: {player.name} HP: {player.health} | {boss.name} HP: {boss.health}\n")
        print(f"{boss.name} Wins the match against {player.name}!")
        break
        
    print(f"-> Status: {player.name} HP: {player.health} | {boss.name} HP: {boss.health}\n")
