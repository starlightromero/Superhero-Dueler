"""Import Ability, Weapon, Armor, Hero, Team, and choice."""
from ability import Ability
from weapon import Weapon
from spell import Spell
from armor import Armor
from hero import Hero
from team import Team
from random import choice


class Arena:
    """Arena class."""

    def __init__(self):
        """Instantiate properties."""
        self.previous_winner = None

    def create_ability(self):
        """Prompt for Ability information.

        Return Ability with values from user Input.
        """
        name = ""
        while len(name) < 1:
            name = input("What is the ability name?  ")
        max_damage = 0
        while max_damage < 1:
            max_damage = input("What is the max damage of the ability?  ")
            try:
                max_damage = int(max_damage)
                print(f"{name} has been added.")
                break
            except(ValueError, TypeError):
                max_damage = 0
                print("Please enter a number.")
        return Ability(name, max_damage)

    def create_weapon(self):
        """Prompt user for Weapon information.

        Return Weapon with values from user input.
        """
        name = ""
        while len(name) < 1:
            name = input("What is the weapon name?  ")
        max_damage = 0
        while max_damage < 1:
            max_damage = input("What is the max damage of the weapon?  ")
            try:
                max_damage = int(max_damage)
                print(f"{name} has been added.")
                break
            except(ValueError, TypeError):
                max_damage = 0
                print("Please enter a number.")
        return Weapon(name, max_damage)

    def create_spell(self):
        """Prompt user for Spell information.

        Return Spell with values from user input.
        """
        name = ""
        while len(name) < 1:
            name = input("What is the spell name?  ")
        max_damage = 0
        while max_damage < 1:
            max_damage = input("What is the max damage of the spell?  ")
            try:
                max_damage = int(max_damage)
                print(f"{name} has been added.")
                break
            except(ValueError, TypeError):
                max_damage = 0
                print("Please enter a number.")
        return Spell(name, max_damage)

    def create_armor(self):
        """Prompt user for Armor information.

        Return Armor with values from user input.
        """
        name = ""
        while len(name) < 1:
            name = input("What is the armor name?  ")
        max_block = 0
        while max_block < 1:
            max_block = input("What is the max block of the armor?  ")
            try:
                max_block = int(max_block)
                print(f"{name} has been added.")
                break
            except(ValueError, TypeError):
                max_block = 0
                print("Please enter a number.")
        return Armor(name, max_block)

    def create_hero(self):
        """Prompt user for Hero information.

        Return Hero with values from user input.
        """
        print("\n")
        hero_name = ""
        while len(hero_name) < 1:
            hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "5":
            add_item = input(
                "\n[1] Add ability\n[2] Add weapon\n[3] Add spell\n[4] Add armor\n[5] Done adding items\n\nYour choice: "
            )
            if add_item == "1":
                abilty = self.create_ability()
                hero.add_ability(abilty)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                spell = self.create_spell()
                hero.add_spell(spell)
            elif add_item == "4":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team(self, team):
        """Prompt the user to build a given team."""
        print("{:-^50}".format(team.name).upper())
        members = None
        while not isinstance(members, int):
            members = input(f"How many members would you like on {team.name}?\n")
            try:
                numOfTeamMembers = abs(int(members))
                team.remove_all_heros()
                for i in range(numOfTeamMembers):
                    hero = self.create_hero()
                    team.add_hero(hero)
                    print("\n")
                    print(f"{hero.name} has been added to {team.name}".upper())
                break
            except(ValueError, TypeError):
                print("Please enter a number.")
        print("\n")

    def authorize(self, team):
        """Authorize a given team's abilties and armor."""
        print(
            "{:-^50}".format(f"{team.name} AUTHORIZATION IN PROGRESS").upper()
        )
        for hero in team.heroes:
            if len(hero.abilities) == 0:
                print(f"{hero.name} has no abilties to authorize")
            for ability in hero.abilities:
                if ability.max_damage > 100:
                    print(
                        f"{hero.name}'s {ability.name} is unauthorized and has been removed by the arena."
                    )
                    hero.abilities.remove(ability)
                else:
                    print(
                        f"{hero.name}'s {ability.name} has been authorized by the arena."
                    )
            if len(hero.armors) == 0:
                print(f"{hero.name} has no armor to authorize")
            for armor in hero.armors:
                if armor.max_block > 100:
                    print(
                        f"{hero.name}'s {armor.name} is unauthorized and has been removed by the arena."
                    )
                    hero.armors.remove(armor)
                else:
                    print(
                        f"{hero.name}'s {armor.name} has been authorized by the arena."
                    )
        print("\n")

    def team_battle(self, team_one, team_two):
        """Battle team_one and team_two together."""
        self.authorize(team_one)
        self.authorize(team_two)
        print("{:-^50}".format("THE BATTLE BEGINS"))
        team_one.attack(team_two)

    def surviving_heroes(self, team):
        """Return the survival count for a given team."""
        survival_count = 0
        for hero in team.heroes:
            if hero.is_alive():
                print(f"{hero.name} survived")
                survival_count += 1
        if not survival_count:
            print("no heroes survived")
        return survival_count

    def winning_team(self, team_one, team_one_survival_count, team_two, team_two_survival_count):
        """Print winning team for two given survival counts."""
        if team_one_survival_count and team_two_survival_count:
            print("{:=^50}".format("No winner could be declared").upper())
            self.previous_winner = None
        elif team_one_survival_count:
            p = f"{team_one.name} won"
            print("{:=^50}".format(p).upper())
            self.previous_winner = team_one
        else:
            p = f"{team_two.name} won"
            print("{:=^50}".format(p).upper())
            self.previous_winner = steam_two

    def kd_average(self, team):
        """Print kill/death average for a given team."""
        team_kills = 0
        team_deaths = 0
        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(f"average K/D: {team_kills/team_deaths}")

    def show_stats(self, team_one, team_two):
        """Print team statistics to terminal."""
        print("\n")
        print("{:-^50}".format("STATS"))
        print("\n")
        print(f"{team_one.name} statistics: ".upper())
        team_one_survival_count = self.surviving_heroes(team_one)
        self.kd_average(team_one)
        print("\n")
        print(f"{team_two.name} statistics: ".upper())
        team_two_survival_count = self.surviving_heroes(team_two)
        self.kd_average(team_two)
        print("\n")
        self.winning_team(team_one, team_one_survival_count, team_two, team_two_survival_count)
        print("\n")


if __name__ == "__main__":
    game_is_running = True

    arena = Arena()
    team_one = Team("Team One")
    team_two = Team("Team Two")

    print("\n")
    print("{:=^50}".format("WELCOME TO THE ARENA"))
    print("\n")

    reward_weapons = [
        Weapon("Flamethrower", 60),
        Weapon("Water Hose", 65),
        Weapon("Anvil", 80),
        Weapon("Atomic Bomb", 100)
    ]

    arena.build_team(team_one)
    arena.build_team(team_two)

    while game_is_running:

        arena.team_battle(team_one, team_two)
        arena.show_stats(team_one, team_two)
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        elif (play_again.lower() == "y"):

            team_one.revive_heroes()
            team_two.revive_heroes()

            try:
                chosen_hero = choice(arena.previous_winner.heroes)
                reward_weapon = choice(reward_weapons)
                chosen_hero.add_weapon(reward_weapon)
                print(
                    f"{chosen_hero.name} was rewarded with a {reward_weapon.name} for their success."
                )
            except(AttributeError):
                pass

            edit_team = input("Edit your team? Y or N: ")

            if edit_team.lower() == "y":
                arena.build_team(team_one)
