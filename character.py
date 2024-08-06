from random import randint
import utils


class Character:
    def __init__(self, name, health=0, damage=0, mana=0, ability_mana_cost=35, ult_mana_cost=55):
        """Character creator"""
        self.name = name
        self.health = health
        self.damage = damage
        self.mana = mana
        self.ability_mana_cost = ability_mana_cost
        self.ult_mana_cost = ult_mana_cost

        self.update_basic_health = health
        self.update_basic_damage = damage
        self.update_basic_mana = mana

    def stats_update(self):
        self.health = self.update_basic_health
        self.damage = self.update_basic_damage
        self.mana = self.update_basic_mana

    def stats(self):
        """Current Stats"""
        if self.health <= 0:
            self.health = 0

        utils.write(f'\n{self.name}\nHealth:{round(self.health)} Damage:{round(self.damage)} Mana:{round(self.mana)}\n')
        return f'\n{self.name}\nHealth:{round(self.health)} Damage:{round(self.damage)} Mana:{round(self.mana)}'

    def mana_and_health_regen(self, my_health, my_mana):
        self.health += ((my_health - self.health) * 0.1)
        self.mana += ((my_mana - self.mana) * 0.31)

    def get_hit_by_basic_attack(self, damage):
        self.health -= (damage * 1.1)

    def get_hit_by_ability(self, damage):
        self.health -= (damage * 1.4)

    def get_hit_by_ult(self, damage):
        self.health -= (damage * 1.9)

    def on_level_stats_growth(self, mode='player'):
        """Different stats scaling for player/enemy"""
        self.update_basic_health *= 1.43 if mode == 'player' else 1.51
        self.update_basic_damage *= 1.34 if mode == 'player ' else 1.44
        self.update_basic_mana *= 1.32 if mode == 'player' else 1.35
        self.stats_update()

    def generate_stats(self):
        self.update_basic_health = randint(70, 110)
        self.update_basic_damage = randint(15, 25)
        self.update_basic_mana = randint(55, 90)
        self.stats_update()
