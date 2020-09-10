"""Import Armor, Ability, and Weapon."""
from armor import Armor
from ability import Ability
from weapon import Weapon


class Hero:
    """Hero class."""

    def __init__(self, name, starting_health=100):
        """Instance properties.

        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        """
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        """Add ability to abilities list.

        ability: Ability Object.
        """
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        """Add weapon to abilities list.

        weapon: Weapon Object.
        """
        self.abilities.append(weapon)

    def add_spell(self, spell):
        """Add spell to abilities list.

        spell: Spell Object.
        """
        self.abilities.append(spell)

    def add_armor(self, armor):
        """Add armor to armors list.

        armor: Armor Object
        """
        self.armors.append(armor)

    def add_kill(self, num_kills=1):
        """Update self.kills by num_kills amount"""
        self.kills += num_kills

    def add_death(self, num_deaths=1):
        """Update deaths with num_deaths"""
        self.deaths += num_deaths

    def attack(self):
        """Calculate the total damage from all ability attacks.

        return: total_damage:Int
        """
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        """Calculate the total block amount from all armor blocks.

        return: total_block:Int
        """
        defense = 0
        for armor in self.armors:
            defense += armor.block()
        return defense

    def take_damage(self, damage):
        """Update self.current_health to reflect damage minus defense."""
        self.current_health -= damage + self.defend()
        if self.current_health < 0:
            self.current_health = 0

    def is_alive(self):
        """Return True or False depending if the hero is alive or not."""
        if self.current_health <= 0:
            return False
        return True

    def fight(self, opponent):
        """Hero will take turns fighting the opponent hero passed in."""

        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw".upper())
            return 0

        while self.is_alive() and opponent.is_alive():
            print(f"{self.name} attacked {opponent.name}")
            opponent.take_damage(self.attack())
            print(f"{opponent.name}'s remaining health: {opponent.current_health}")
            if opponent.is_alive():
                print(f"{opponent.name} attacked {self.name}")
                self.take_damage(opponent.attack())
                print(f"{self.name}'s remaining health: {self.current_health}")

        if not self.is_alive():
            opponent.add_kill(1)
            self.add_death(1)
            print(f"\n{self.name} has been killed by {opponent.name}\n".upper())
            return opponent.name
        elif not opponent.is_alive():
            opponent.add_death(1)
            self.add_kill(1)
            print(f"\n{opponent.name} has been killed by {self.name}\n".upper())
            return self.name
