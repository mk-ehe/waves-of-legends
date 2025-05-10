from time import sleep
from random import randint

deaths = 0

health_for_bot = randint(70,110)
damage_for_bot = randint(15,25)
mana_for_bot = randint(55,90)

class character:

    def __init__(self, name, health, damage, mana):
        '''character creator'''
        self.name = name
        self.health = health
        self.damage = damage
        self.mana = mana

        self.update_basic_health = health
        self.update_basic_damage = damage
        self.update_basic_mana = mana


    def stats_update(self):
        self.health = self.update_basic_health
        self.damage = self.update_basic_damage
        self.mana = self.update_basic_mana


    def stats(self):
        '''aktualne staty'''
        if self.health <= 0:
            self.health = 0

        for i in (f'\n{self.name}\nHealth:{round(self.health)} Damage:{round(self.damage)} Mana:{round(self.mana)}\n'):
            print(i,end='',flush=True)
            sleep(0.06)


    def mana_and_health_regen(self, my_health, my_mana):
        self.health += ((my_health - self.health) * 0.12)
        self.mana += ((my_mana - self.mana) * 0.32)


    def basic_attack(self,enemy_damage):
        self.health -= (enemy_damage)


    def ability(self,enemy_damage):
        self.health -= (enemy_damage*1.5)


    def ult(self,enemy_damage):
        self.health -= (enemy_damage*2.1)


    def on_level_stats_growth(self):
       self.update_basic_health *= 1.4
       self.update_basic_damage *= 1.35
       self.update_basic_mana *= 1.33

#________________________________________________________________________________________________________________________________________________________________________________

sett = character('Sett:', 100, 22, 70)
viego = character('Viego:',90, 24, 75)
sylas = character('Sylas:',70, 30, 90)
samira = character('Samira:', 80, 26, 80)
thresh = character('Thresh:', 120, 16, 80)

sleep(1)

for i in "\nGame: Waves of Legends\n":
    print(i,flush=True,end='')
    sleep(0.06)

sleep(1)
pick_list = ['Sett','Viego','Sylas','Samira','Thresh']
pick_list_with_stats = [sett.stats(),viego.stats(),sylas.stats(),samira.stats(),thresh.stats()]
character_list = [sett,viego,sylas,samira,thresh]


while True:
    
    summoner = input('\nChoose your summoner to fight as: ').title().strip()

    if summoner in pick_list:
        for i in (f'\nYou have chosen: {pick_list[pick_list.index(summoner)]}'):
            print(i,end='',flush=True)
            sleep(0.06)
        break
    else:
        continue
        

summoner = pick_list.index(summoner)
summoner = character_list[summoner]


def fight(name,ability_cost,ult_cost):
    global deaths

    sleep(1)
    print('\n\nPrepare for your Enemy!')
    sleep(1.5)
    print(f'\nAbility cost: {ability_cost} mana\nUlt cost: {ult_cost} mana')
    sleep(2)
    
    enemy = character(name, health_for_bot, damage_for_bot, mana_for_bot)

    print('\nYour enemy is:')

    sleep(1)
    enemy.stats()
    sleep(1)
    print('\nVS')
    sleep(1)
    summoner.stats()


    while True:
        
        while True:

            if summoner.mana >= ult_cost:
                type_of_attack = input(f'\nChoose your attack: ([B]Basic Attack, [A]Ability Attack -{ability_cost} mana, [U]Ult -{ult_cost} mana): ').title().strip()
                if type_of_attack == 'A' or type_of_attack == 'B' or type_of_attack == 'U':
                    break
                else:
                    continue

            elif summoner.mana < ability_cost:
                type_of_attack = input('\nChoose your attack: ([B]Basic Attack): ').title().strip()
                if type_of_attack == 'B':
                    break
                else:
                    continue

            elif summoner.mana < ult_cost:
                type_of_attack = input(f'\nChoose your attack: ([B]Basic Attack, [A]Ability Attack -{ability_cost} mana): ').title().strip()
                if type_of_attack == 'A' or type_of_attack == 'B':
                    break
                else:
                    continue

        if type_of_attack == 'B':
            enemy.basic_attack(summoner.damage)
            print('\nYou have chosen: Basic Attack')
            sleep(0.5)

        elif type_of_attack == 'A':

            enemy.ability(summoner.damage)
            summoner.mana = summoner.mana - ability_cost
            print(f'\nYou have chosen: Ability -{ability_cost} mana')
            sleep(0.5)

        elif type_of_attack == 'U':

            enemy.ult(summoner.damage)
            summoner.mana = summoner.mana - ult_cost
            print(f'\nYou have chosen: Ult -{ult_cost} mana')
            sleep(0.5)

        enemy.stats()
        summoner.stats()

        if enemy.health <= 0:
            print("\nCongratulations! You have defeated your enemy!")
            break
        
        enemy_attack = randint(1,2)

        sleep(1)

        if enemy_attack == 1:

            summoner.basic_attack(enemy.damage)
            print(f'\n{name} has chosen: Basic Attack')
            sleep(0.5)

        elif enemy_attack == 2:

            if enemy.mana >= ult_cost:
                summoner.ult(enemy.damage)
                enemy.mana = enemy.mana - ult_cost
                print(f'\n{name} has chosen: Ult -{ult_cost} mana')
                sleep(0.5)

            elif enemy.mana >= ability_cost:
                summoner.ability(enemy.damage)
                enemy.mana = enemy.mana - ability_cost
                print(f'\n{name} has chosen: Ability -{ability_cost} mana')
                sleep(0.5)
            
            elif enemy.mana < ability_cost:
                summoner.basic_attack(enemy.damage)
                print(f'\n{name} has chosen: Basic Attack')
                sleep(0.5)
    
        enemy.stats()
        summoner.stats()

        if summoner.health <= 0:
            sleep(1)
            print('You are Dead!💀')
            sleep(2)
            deaths = 1
            break

        sleep(1)

        for i in '\nREGENERATION!\n':
            print(i,end='',flush=True)
            sleep(0.06)

        sleep(1)

        summoner.mana_and_health_regen(summoner.update_basic_health, summoner.update_basic_mana)
        enemy.mana_and_health_regen(enemy.update_basic_health, enemy.update_basic_mana)
        
        enemy.stats()
        summoner.stats()

fight('Teemo',35,60)


def after_game_1():

    global deaths,summoner
    if deaths == 1:
        exit()

    sleep(1)

    print('\n\nLevel UP!')
    summoner.stats_update()
    summoner = character(summoner.name, summoner.update_basic_health, summoner.update_basic_damage, summoner.update_basic_mana)
    summoner.stats()
    summoner.on_level_stats_growth()
    summoner.stats_update()
    sleep(1)

    print('''
            |
            V''')

    summoner.stats()
    sleep(1.5)
after_game_1()
def on_level_bot_stats_growth():
        global health_for_bot, damage_for_bot, mana_for_bot
        health_for_bot *= 1.51
        damage_for_bot *= 1.44
        mana_for_bot *= 1.35
on_level_bot_stats_growth()
fight('Evelynn',45,75)


after_game_1()
on_level_bot_stats_growth()
fight('Twitch',65,95)


after_game_1()
on_level_bot_stats_growth()
fight('Illaoi',85,125)


sleep(1)
print('Final Enemy!')
sleep(1)


after_game_1()
on_level_bot_stats_growth()
fight('Yasuo',110,170)

if deaths == 0:
    print('That was last enemy! You are the Arena Champion!')
else:
    print('Damn! You were so close to become the Arena Chapion!')
