#!/usr/bin/python3
#DIDN'T REALLY UNDERSTAND BUT THIS IS MY OWN VERSION
class warrior:

    weapons = {"stick":1, "blade":10, "spear":20, "arrows":25, "slingshot":15}

    def __init__(self, name="", opponent="Goliath", weapon="stick", health=100):
        self.name = name
        self.opponent = opponent
        self.weapon = weapon
        self.health = health

    def attack(self):
        if self.health < 1:
            print(f"{self.name} killed {self.opponent}")
            print("Game Over!!!")
            exit()
        else:
            self.health = self.health - warrior.weapons.get(self.weapon)
            print(f"{self.name} attacks and inflicts {warrior.weapons.get(self.weapon)} damage(s) on {self.opponent}\n")
            if self.health > 1:
                print(f"{self.opponent} has {self.health} hp left!\n")
            else:
                print(f"{self.name} killed {self.opponent}")
                print("Game Over!!!")
                exit()

    def weild(self):
        print("Choose a new weapon:")
        for key in warrior.weapons:
            print(f"weapon: {key}\ndamage: {warrior.weapons[key]}")
            print()
        new_weapon = str(input(":")) 
        self.weapon = new_weapon

#def main():
#    battle = warrior("joseph")
#    battle.attack()
#    battle.attack()
#    battle.weild()
#    battle.attack()
#    battle.attack()
#    battle.attack()
#    battle.attack()
#    battle.attack()
#    battle.attack()
#    battle.attack()
#    battle.attack()
#
#main()
