import random

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def attack_target(self, target):
        damage = random.randint(1, self.attack)
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage.")

def main():
    print("Welcome to the Adventure RPG!")
    player_name = input("Enter your character's name: ")
    player = Character(player_name, hp=20, attack=5)

    enemy = Character("Goblin", hp=10, attack=3)

    print(f"A wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        action = input("What will you do? (attack/flee): ").lower()
        if action == "attack":
            player.attack_target(enemy)
            if enemy.is_alive():
                enemy.attack_target(player)
        elif action == "flee":
            print("You managed to escape!")
            break
        else:
            print("Invalid action. Choose 'attack' or 'flee'.")

        if not enemy.is_alive():
            print(f"You defeated the {enemy.name}!")
        elif not player.is_alive():
            print("Game over! You have been defeated.")
            break

if __name__ == "__main__":
    main()