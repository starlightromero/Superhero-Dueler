"""Import randint and Ability."""
from random import randint
from ability import Ability


class Weapon(Ability):
    """Weapon class."""

    def attack(self):
        """Return a random value (half - full attack power) of the weapon."""
        return randint((self.max_damage // 2), self.max_damage)
