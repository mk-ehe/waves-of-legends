from random import randint
from time import sleep
import constants


def write(text: str):
    for letter in text:
        print(letter, end='', flush=True)
        sleep(constants.TYPE_SPEED)


def write_multiple(*args):
    for i in args:
        write(f"{i}\n")
        sleep(constants.TYPE_SPEED)


def fight(player, enemy):
    write_multiple('\nPrepare for your Enemy!', f'\nAbility cost: {player.ability_mana_cost}\nUlt cost: {player.ult_mana_cost}')
    write_multiple('\nYour enemy is:', enemy.stats(), '\nVS')

    player.stats()

    while True:
        if player.mana >= player.ult_mana_cost:
            available_attacks = "all"
        elif player.ult_mana_cost > player.mana >= player.ability_mana_cost:
            available_attacks = "ability"
        else:
            available_attacks = "basic"

        while True:
            type_of_attack = input(f'\nChoose your attack {constants.ATTACK_TYPES[available_attacks]}: ').upper()
            if type_of_attack in ['B', 'A', 'U']:
                break

        if type_of_attack == 'U' and player.mana >= player.ult_mana_cost:
            enemy.get_hit_by_ult(damage=player.damage)
            player.mana -= player.ult_mana_cost
            print(f'\nYou have chosen: Ult -{player.ult_mana_cost} mana')

        elif type_of_attack == 'A' and player.mana >= player.ability_mana_cost:
            enemy.get_hit_by_ability(damage=player.damage)
            player.mana -= player.ability_mana_cost
            print(f'\nYou have chosen: Ability -{player.ability_mana_cost} mana')

        else:
            enemy.get_hit_by_basic_attack(damage=player.damage)
            print(f'\nYou have chosen: Basic Attack')

        sleep(0.5)
        enemy.stats()
        player.stats()

        if enemy.health <= 0:
            print("\nCongratulations! You have defeated your enemy!")
            return 'Won'

        enemy_attack = randint(1, 3)
        sleep(1)

        if enemy_attack == 2 and enemy.mana >= enemy.ability_mana_cost:
            player.get_hit_by_ability(damage=enemy.damage)
            enemy.mana -= enemy.ability_mana_cost
            print(f'\n{enemy.name} has chosen: Ability -{enemy.ability_mana_cost} mana')

        elif enemy_attack == 3 and enemy.mana >= enemy.ult_mana_cost:
            player.get_hit_by_ult(damage=enemy.damage)
            enemy.mana -= enemy.ult_mana_cost
            print(f'\n{enemy.name} has chosen: Ult -{player.ult_mana_cost} mana')

        else:
            player.get_hit_by_basic_attack(damage=enemy.damage)
            print(f'\n{enemy.name} has chosen: Basic Attack')

        sleep(0.5)
        enemy.stats()
        player.stats()

        if player.health <= 0:
            sleep(1)
            print('You are Dead!💀')
            sleep(2)
            player_dead()

        sleep(1)
        write('\nREGENERATION!\n')
        sleep(1)

        player.mana_and_health_regen(player.update_basic_health, player.update_basic_mana)
        enemy.mana_and_health_regen(enemy.update_basic_health, enemy.update_basic_mana)

        enemy.stats()
        player.stats()


def player_dead():
    print('Damn! You were so close to become the Arena Chapion!')
    exit(code=0)


def player_won():
    print('That was last enemy! You are the Arena Champion!')
    exit(code=0)


def after_round(player, enemy):
    print('\n\nLevel UP!')
    player.stats_update()
    player.stats()
    player.on_level_stats_growth()

    enemy.on_level_stats_growth('enemy')
    sleep(1)

    print('''
            |
            V''')

    player.stats()
    sleep(1.5)
