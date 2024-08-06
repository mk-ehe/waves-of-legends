from random import randint

import constants
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
        self.health += ((my_health - self.health) * constants.HP_REGEN)
        self.mana += ((my_mana - self.mana) * constants.MP_REGEN)

    def get_hit_by_basic_attack(self, damage):
        self.health -= (damage * constants.BASIC_ATTACK)

    def get_hit_by_ability(self, damage):
        self.health -= (damage * constants.ABILITY)

    def get_hit_by_ult(self, damage):
        self.health -= (damage * constants.ULT)

    def on_level_stats_growth(self, mode='player'):
        """Different stats scaling for player/enemy"""
        self.update_basic_health *= constants.HP_LEVELUP_PLAYER if mode == 'player' else constants.HP_LEVELUP_ENEMY
        self.update_basic_damage *= constants.DMG_LEVELUP_PLAYER if mode == 'player ' else constants.DMG_LEVELUP_ENEMY
        self.update_basic_mana *= constants.MP_LEVELUP_PLAYER if mode == 'player' else constants.MP_LEVELUP_ENEMY
        self.stats_update()

    def generate_stats(self):
        self.update_basic_health = randint(constants.HP_GEN[0], constants.HP_GEN[1])
        self.update_basic_damage = randint(constants.DMG_GEN[0], constants.DMG_GEN[1])
        self.update_basic_mana = randint(constants.MP_GEN[0], constants.MP_GEN[1])
        self.stats_update()
