import random as r
import time as t
import sys
import keyboard as k

# Reviving System
def revived(player_hp):
    player_hp += r.randint(1, 3)
    print("You found a revive!\nYour current HP : [{}]".format(player_hp))
    t.sleep(1)
    return player_hp

# Money-earning System
def earning(money):
    money += r.randint(10, 30)
    print("You found some money!\nYour current savings : [{}]".format(money))
    t.sleep(1)
    return money

# Inshop-purchasing System
def buy_inshop(mp, player_hp, money):

    while True:

        if k.read_key == 'm' and money >= 100:
            t.sleep(0.75)
            print('Confirm purchase?\n(Press b to return to ShopMenu, press any to confirm your MPpurchase.)')

            while True:

                if k.read_key == 'b' or k.read_key == 'B':

                    if money >= 100:
                        mp += r.randint(recover_min, recover_max)
                        t.sleep(0.75)
                        print("Purchase finished!\nYour current mp : [{}]".format(mp))
                        money -= 100
                        t.sleep(0.75)
                        print("Your current savings : [{}]".format(money))
                        break

                    else:
                        t.sleep(0.75)
                        print('Uh-oh. Your money is not enough for buying this.')
                        break

                else:
                    break

        elif k.read_key == 'l' and money >= 100:
            t.sleep(0.75)
            print('Confirm purchase?\n(Press b to return to ShopMenu, press any to confirm your HPpurchase.)')

            while True:

                if k.read_key == 'b' or k.read_key == 'B':

                    if money >= 100:
                        player_hp += r.randint(revive_min, revive_max)
                        t.sleep(0.75)
                        print("Purchase finished!\nYour current hp : [{}]".format(player_hp))
                        money -= 100
                        t.sleep(0.75)
                        print("Your current savings : [{}]".format(money))
                        break

                    else:
                        t.sleep(0.75)
                        print('Uh-oh. Your money is not enough for buying this.')
                        break

                else:
                    break

        elif k.read_key == 'q':
            t.sleep(0.75)
            print('Confirm again.(Press q to leave, else any to resume.')

            while True:

                if k.read_key == 'q' or k.read_key == 'Q':
                    t.sleep(0.75)
                    print('Thanks for your patronage! Please come again.')
                    return mp, player_hp, money
                    break

                else:
                    break

# Trigger System 1
def enter_combat(mp, mp_atk_min, mp_atk_max, player_atk):

    while True:

        if k.read_key == 'm':

            if mp > 0:
                mp -= 1
                player_atk = r.randint(mp_atk_min, mp_atk_max)
                t.sleep(0.75)
                print('Magic Attack!')
                return mp, player_atk

            else:
                t.sleep(0.75)
                print('You have not enough magic power to use a MagicAttack.')

        elif k.read_key == 'p':
            player_atk = r.randint(atk_min, atk_max)
            t.sleep(0.75)
            print('Phsical Attack!')
            t.sleep(1)
            return mp, player_atk


# Trigger System 2
def enter_status(stat, mp, player_hp, money):

    while True:

        if k.read_key == '1':
            print(stat[0])

        elif k.read_key == '2':
            print("Your current HP : [{}]".format(stat[1]))

        elif k.read_key == '3':
            print("Your current savings : [{}]".format(stat[2]))

        elif k.read_key == '4':
            print('Welcome to RPG Store! What can I help you here, little buddy?')
            print('(For MPRecovery, press \'m\'; for HPRecovery, press \'l\'; if you want to quit ShopMenu, press \'q\')')
            mp, player_hp, money = buy_inshop(mp, player_hp, money)
    t.sleep(1)

# Combat System
def combat(stat, atk_min, atk_max, enemy_atk, enemy_hp_max, enemy_hp_min, chance_max, mp, mp_atk_min, mp_atk_max, player_atk):
    life = stat[0]
    player_hp = stat[1]
    money = stat[2]
    print("Player {} will go first.".format(player_name))
    t.sleep(1)
    enemy_hp = r.randint(enemy_hp_min, enemy_hp_max)
    print("Enemy HP : [{}]. Try to beat it!".format(enemy_hp))

    while True:

        print('Player can use MagicAttack (Press m)  or PhysicalAttack (Press p).')
        mp, player_atk = enter_combat(mp, mp_atk_min, mp_atk_max, player_atk)
        enemy_hp -= player_atk
        print("You made a {}-point attack!\n(Enemy HP : [{}] pt)".format(player_atk, enemy_hp))
        t.sleep(0.75)

        if enemy_hp <= 0:
            break

        t.sleep(0.75)
        player_hp -= enemy_atk
        print("Enemy made a {}-point attack.\n(Player HP : [{}] pt)".format(enemy_atk, player_hp))
        t.sleep(0.75)

        if player_hp <= 0:
            life = 0
            break

        t.sleep(0.75)

    if player_hp <= 0:
        sys.exit('You are dead.\nBetter luck next time.')

    else:
        print('You have successfully taken down the enemy!')
        money += r.randint(10, 20)
        chance_max += 50
        t.sleep(0.75)

    return chance_max, [life, player_hp, money]

# Initial settings
player_hp = 10  # HP Initial
money = 0  # Money Initial
player_atk = 0  # r.randint([mp]_atk_min, [mp]_atk_max)
atk_min = 1  # Increase by Level
atk_max = 3  # Increase by Level
mp_atk_min = 4  # Increase by Level
mp_atk_max = 8  # Increase by Level
mp = 0  # Revive-able Variable
enemy_atk = 1  # Increase by Level
enemy_hp_min = 5  # Increase by Level
enemy_hp_max = 15  # Increase by Level
life = 1  # Status
revive_chance = 5500  # Event, Constant
combat_chance = 8000  # Event, Constant
chance_max = 10000  # Event, Increase After Every Battle
recover_max = 4  # MP Recovery Potion - Constant
recover_min = 2  # MP Recovery Potion - Constant
revive_max = 6  # HP Recovery Potion - Constant
revive_min = 4  # HP Recovery Potion - Constant

player_name = input('Welcome to the RPG world!\nWhat is your name?')
stat = [life, player_hp, money]

while True:
    event = [revived(player_hp), earning(money), combat(stat, atk_min, atk_max, enemy_atk, enemy_hp_max, enemy_hp_min, chance_max, mp, mp_atk_min, mp_atk_max, player_atk)]
    chance = r.randint(1, chance_max)

    if chance <= 3000:
        print('What are you going to do now?')
        print('Function 1 - Survival status inspector (Press 1 to trigger)')
        print('Function 2 - HealthPoint status inspector (Press 2 to trigger)')
        print('Function 3 - BankSavings status inspector (Press 3 to trigger)')
        print('Function 4 - RPG Store Entrance (Press 4 to trigger)')
        enter_status(mp, player_hp, money)

    elif chance >= 3000 and chance <= revive_chance:
        stat[1] = revived(stat[1])

    elif chance >= revive_chance and chance <= combat_chance:
        stat[2] = earning(stat[2])

    else:
        chance_max, stat = combat(stat, atk_min, atk_max, enemy_atk, enemy_hp_max, enemy_hp_min, chance_max, mp, mp_atk_min, mp_atk_max, player_atk)
        life = stat[0]

    if stat[0] == 0:
        break