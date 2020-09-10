"""Import choice."""
from random import choice


class Team:
    """Team class."""

    def __init__(self, name):
        """Initialize team with a name and an empty list of heroes."""
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        """Remove Hero from heroes list. If Hero isn't found return 0."""
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def remove_all_heros(self):
        self.heroes = []

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        """Add Hero object to self.heroes."""
        self.heroes.append(hero)

    def stats(self):
        """Print team statistics."""
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self, health=100):
        """Reset all heroes health to starting_health."""
        for hero in self.heroes:
            hero.current_health = hero.starting_health
            print(f"{hero.name} has been revived.")

    def attack(self, other_team):
        """Battle each team against each other."""
        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            chosen_hero = choice(living_heroes)
            chosen_opponent = choice(living_opponents)
            print(f"{chosen_hero.name} vs {chosen_opponent.name}".upper())
            winner = chosen_hero.fight(chosen_opponent)
            if winner == chosen_hero.name:
                living_opponents.remove(chosen_opponent)
            elif winner == chosen_opponent.name:
                living_heroes.remove(chosen_hero)
            else:
                break
