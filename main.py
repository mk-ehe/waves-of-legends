import constants
from character import Character
from time import sleep
import utils

sett = Character('Sett', constants.SETT["HP"], constants.SETT["DMG"], constants.SETT["MP"])
viego = Character('Viego', constants.VIEGO["HP"], constants.VIEGO["DMG"], constants.VIEGO["MP"])
sylas = Character('Sylas', constants.SYLAS["HP"], constants.SYLAS["DMG"], constants.SYLAS["MP"])
samira = Character('Samira', constants.SAMIRA["HP"], constants.SAMIRA["DMG"], constants.SAMIRA["MP"])
thresh = Character('Thresh', constants.THRESH["HP"], constants.THRESH["DMG"], constants.THRESH["MP"])

character_list = [sett, viego, sylas, samira, thresh]
pick_list = [champ.name for champ in character_list]

for champ in character_list:
    """Display all champs' stats"""
    champ.stats()

while True:
    """Loop until valid name is given"""
    sleep(1)
    utils.write('\nChoose your summoner to fight as: ')
    summoner: str = input().title().strip()

    if summoner in pick_list:
        utils.write(f'\nYou have chosen: {summoner}')
        summoner_idx = pick_list.index(summoner)
        summoner: Character = character_list[summoner_idx]  # Character object
        break

enemies = [Character(name=champ, ability_mana_cost=constants.ENEMY_CHARACTERS[champ]['Ability_MP'],
                     ult_mana_cost=constants.ENEMY_CHARACTERS[champ]['Ult_MP']) for champ in constants.ENEMY_CHARACTERS]

for enemy in enemies:
    summoner.ability_mana_cost, summoner.ult_mana_cost = enemy.ability_mana_cost, enemy.ult_mana_cost
    enemy.generate_stats()
    utils.fight(summoner, enemy)
    utils.after_round(summoner, enemy)

utils.player_won()
