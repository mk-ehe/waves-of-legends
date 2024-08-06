from character import Character
from time import sleep
import utils

sett = Character('Sett', 100, 20, 70)
viego = Character('Viego', 90, 25, 80)
sylas = Character('Sylas', 70, 30, 90)
samira = Character('Samira', 85, 25, 85)
thresh = Character('Thresh', 120, 15, 75)

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

enemies = [Character('Teemo'),
           Character('Evelynn', ability_mana_cost=45, ult_mana_cost=75),
           Character('Twitch', ability_mana_cost=65, ult_mana_cost=95),
           Character('Illaoi', ability_mana_cost=85, ult_mana_cost=125),
           Character('Yasuo', ability_mana_cost=110, ult_mana_cost=170)
           ]

for enemy in enemies:
    summoner.ability_mana_cost, summoner.ult_mana_cost = enemy.ability_mana_cost, enemy.ult_mana_cost
    enemy.generate_stats()
    utils.fight(summoner, enemy)
    utils.after_round(summoner, enemy)

utils.player_won()
