import random


# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(
            f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}"
        )

    def heal(self):
        self.health += 20  # Heal amount can be adjusted
        if self.health > self.max_health:
            self.health = self.max_health
        print(
            f"{self.name} heals for 20 health! Current health: {self.health}/{self.max_health}"
        )


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def power_attack(self, opponent):
        damage = random.randint(
            int(self.attack_power * 2 - 5), int(self.attack_power * 2 + 5)
        )
        opponent.health -= damage
        print(f"{self.name} uses Power Attack on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def shield_block(self):
        print(f"{self.name} blocks the next attack!")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def cast_spell(self, opponent):
        damage = random.randint(
            int(self.attack_power * 1.5 - 5), int(self.attack_power * 1.5 + 5)
        )
        opponent.health -= damage
        print(f"{self.name} casts a spell on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def mana_shield(self):
        print(f"{self.name} uses Mana Shield to block the next attack!")


# Hobbit class (inherits from Character)
class Hobbit(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)

    def quick_shot(self, opponent):
        damage = random.randint(
            int(self.attack_power * 2 - 5), int(self.attack_power * 2 + 5)
        )
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def evade(self):
        print(f"{self.name} evades the next attack!")


# Nun class (inherits from Character)
class Nun(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)

    def holy_strike(self, opponent):
        damage = random.randint(
            int(self.attack_power * 2.5 - 5), int(self.attack_power * 2.5 + 5)
        )
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def divine_shield(self):
        print(f"{self.name} uses Divine Shield to block the next attack!")


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health
        print(
            f"{self.name} regenerates 5 health! Current health: {self.health}/{self.max_health}"
        )


# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Hobbit")
    print("4. Nun")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == "1":
        return Warrior(name)
    elif class_choice == "2":
        return Mage(name)
    elif class_choice == "3":
        return Hobbit(name)
    elif class_choice == "4":
        return Nun(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability 1")
        print("3. Use Special Ability 2")
        print("4. Heal")
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(wizard)
        elif choice == "2":
            if isinstance(player, Warrior):
                player.power_attack(wizard)
            elif isinstance(player, Mage):
                player.cast_spell(wizard)
            elif isinstance(player, Hobbit):
                player.quick_shot(wizard)
            elif isinstance(player, Nun):
                player.holy_strike(wizard)
        elif choice == "3":
            if isinstance(player, Warrior):
                player.shield_block()
            elif isinstance(player, Mage):
                player.mana_shield()
            elif isinstance(player, Hobbit):
                player.evade()
            elif isinstance(player, Nun):
                player.divine_shield()
        elif choice == "4":
            player.heal()
        elif choice == "5":
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")


# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)


if __name__ == "__main__":
    main()
