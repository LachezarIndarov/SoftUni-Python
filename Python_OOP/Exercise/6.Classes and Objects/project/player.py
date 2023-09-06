# 6.Guild System

# noinspection PyListCreation
class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = dict()
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return "Skill already added"

    def player_info(self):
        player_info = [
            f"Name: {self.name}",
            f"Guild: {self.guild}",
            f"HP: {self.hp}",
            f"MP: {self.mp}",
        ]
        [player_info.append(f"==={skill} - {mana}") for skill, mana in self.skills.items()]
        return "\n".join(player_info)




"""
class Player:

    DEFAULT_GUILD = "Unaffiliated"
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = self.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return f"Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = f'Name: {self.name}\n'
        result += f'Guild: {self.guild}\n'
        result += f'HP: {self.hp}\n'
        result += f'MP: {self.mp}\n'
        for skill_name, mana_cost in self.skills.items():
            result += f'==={skill_name} - {mana_cost}\n'

"""

