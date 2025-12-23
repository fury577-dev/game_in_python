import random

# Player stats
player = {
    "name": "",
    "hp": 100,
    "attack": 20
}

# Enemy templates
enemies = [
    {"name": "Goblin", "hp": 40, "attack": 10},
    {"name": "Skeleton", "hp": 50, "attack": 12},
    {"name": "Dark Mage", "hp": 60, "attack": 15}
]

def start_game():
    print("=== TEXT RPG ===")
    player["name"] = input("Enter your name, hero: ")
    print(f"\nWelcome, {player['name']}!")
    adventure()

def adventure():
    while player["hp"] > 0:
        enemy = random.choice(enemies).copy()
        print(f"\nA wild {enemy['name']} appears!")
        fight(enemy)

        if player["hp"] <= 0:
            print("\nYou have been defeated... Game Over.")
            break

        choice = input("\nContinue adventuring? (y/n): ").lower()
        if choice != "y":
            print("\nYou return home victorious.")
            break

def fight(enemy):
    while enemy["hp"] > 0 and player["hp"] > 0:
        print(f"\n{player['name']} HP: {player['hp']} | {enemy['name']} HP: {enemy['hp']}")
        print("1. Attack")
        print("2. Run")

        choice = input("> ")

        if choice == "1":
            damage = random.randint(10, player["attack"])
            enemy["hp"] -= damage
            print(f"You hit the {enemy['name']} for {damage} damage!")

        elif choice == "2":
            if random.random() < 0.5:
                print("You escaped!")
                return
            else:
                print("Failed to escape!")

        if enemy["hp"] > 0:
            damage = random.randint(5, enemy["attack"])
            player["hp"] -= damage
            print(f"The {enemy['name']} hits you for {damage} damage!")

if __name__ == "__main__":
    start_game()
