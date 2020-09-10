"""Import randint."""
from random import randint


class Ability:
    """Ability class."""

    def __init__(self, name, max_damage):
        """Instantiate instance properties.

        name: String
        max_damage: Integer
        """
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        """Return a value between 0 and the value set by self.max_damage."""
        return randint(0, self.max_damage)
