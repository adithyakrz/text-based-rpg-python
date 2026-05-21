from random import randint
from random import random

from Charecter import Charecter
from Boss import Boss

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
