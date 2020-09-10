"""Import randint and Ability."""
from random import randint
from ability import Ability


class Spell(Ability):
    """Spell class."""

    def attack(self):
        """Return max_damage with 20% accuracy."""
        if randint(1, 10) > 8:
            return self.max_damage
        else:
            return 0
