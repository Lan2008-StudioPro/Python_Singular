import random as r
import time as t
import sys
from keyboard import press

# Level-Up System
def level(levelstatus: list):
    levelup = 10 ** levelstatus[0]
    if levelstatus[1] == levelup:
        levelstatus[0] += 1
        levelstatus[1] = 0
        print("Level up!\nCurrent level : [{}]".format(levelstatus[0]))
        level_atk_boost += 0.2

# Reviving System
def revived(stat: list):
    stat[1] += r.randint(1, 3)
    print("You found a revive!\nYour current HP : [{}]".format(stat[1]))
    t.sleep(1)
    return stat

# Money-earning System
def earning(stat: list):
    stat[2] += r.randint(10, 30)
    print("You found some money!\nYour current savings : [{}]".format(stat[2]))
    t.sleep(1)
    return stat

# Inshop-purchasing System
def buy_inshop(stat: list):

    while True:
        t.sleep(0.75)
        item = input('Which item are you going to purchase?\n(m / l / g / r / q)\n')

        if item == 'm':
            t.sleep(0.75)
            print("MP Potion - recover MP by a range of [{}] to [{}].\nThis costs 100$RpgD.".format(recover_min, recover_max))
            t.sleep(0.75)
            confirm = input('Confirm purchase?\n(Press \'m\' again to confirm your MPpurchase.)')

            while True:

                if confirm == 'b':

                    if stat[2] >= 100:
                        stat[3] += r.randint(recover_min, recover_max)
                        t.sleep(0.75)
                        print("Purchase finished!\nYour current mp : [{}]".format(stat[3]))
                        stat[2] -= 100
                        t.sleep(0.75)
                        print("Your current savings : [{}]".format(stat[2]))
                        break

                    else:
                        t.sleep(0.75)
                        print('Uh-oh. Your money is not enough for buying this.')
                        break

                else:
                    break

        elif item == 'l':
            t.sleep(0.75)
            print("HP Revive - restore HP by a range of [{}] to [{}].\nThis costs 100$RpgD.".format(revive_min, revive_max))
            t.sleep(0.75)
            confirm = input('Confirm purchase?\n(Press \'l\' again to confirm your HPpurchase.)')

            while True:

                if confirm == 'l':

                    if stat[2] >= 100:
                        stat[1] += r.randint(revive_min, revive_max)
                        t.sleep(0.75)
                        print("Purchase finished!\nYour current hp : [{}]".format(stat[1]))
                        stat[2] -= 100
                        t.sleep(0.75)
                        print("Your current savings : [{}]".format(stat[2]))
                        break

                    else:
                        t.sleep(0.75)
                        print('Uh-oh. Your money is not enough for buying this.')
                        break

                else:
                    break

        elif item == 'r':
            t.sleep(0.75)
            print('Forbidden Reel - Kill oppeonent at once.\nThis costs 500$RpgD.')
            t.sleep(0.75)
            confirm = input('Confirm purchase?\n(Press \'r\' again to confirm your Reelpurchase.)\n')

            while True:

                if confirm == 'r':

                    if stat[2] >= 500:
                        stat[8] += 1
                        stat[2] -= 500
                        t.sleep(0.75)
                        print("Your current savings : [{}]".format(stat[2]))
                        break

                    else:
                        t.sleep(0.75)
                        print('Uh-oh. Your money is not enough for buying this.')
                        break

                else:
                    break

        elif item == 'g':
            print('<Introduction>')
            t.sleep(0.75)
            print('the Scepter of Corruption -')
            t.sleep(0.75)
            print('A powerful gadget that boosts you MagicAttack!')
            t.sleep(0.75)
            print('One costs 500 $RpgD. Press \'a\' to buy.')
            t.sleep(0.75)
            print('the Sword of Ether -')
            t.sleep(0.75)
            print('This is an heirloom that once belonged to a legendary hero,')
            t.sleep(0.75)
            print('it increases your PhysicalAttack sharply!')
            t.sleep(0.75)
            print('One costs 500 $RpgD. Press \'b\' to buy.')
            t.sleep(0.75)
            gadget = input('Which weapon are you interested in?\n')
            if gadget == 'a':

                while True:
                    t.sleep(0.75)
                    confirm = input('Confirm purchase?\n(Press \'a\' to confirm your HPpurchase.)\n')

                    if confirm == 'a':

                        if stat[2] >= 500:
                            stat[5] += 3
                            stat[2] -= 500
                            t.sleep(0.75)
                            print("Purchase finished! Your current savings : [{}]".format(stat[2]))
                            break

                        else:
                            t.sleep(0.75)
                            print('Uh-oh. Your money is not enough for buying this.')
                            break

                    else:
                        break

            elif gadget == 'b':

                while True:
                    t.sleep(0.75)
                    confirm = input('Confirm purchase?\n(Press \'b\' again to confirm your HPpurchase.)\n')
                    if confirm == 'b':

                        if stat[2] >= 500:
                            stat[4] += 3
                            stat[2] -= 500
                            t.sleep(0.75)
                            print("Purchase finished! Your current savings : [{}]".format(stat[2]))
                            break

                        else:
                            t.sleep(0.75)
                            print('Uh-oh. Your money is not enough for buying this.')
                            break

                    else:
                        break

        elif item == 'q':
            t.sleep(0.75)
            confirm = input('Confirm again.(Press \'q\' again to leave.)\n')

            while True:

                if confirm == 'q':
                    t.sleep(0.75)
                    print('Thanks for your patronage! Please come again.')
                    return stat

                else:
                    break

        else:
            print('KeyError - invalid input for buy_inshop function.')

# Trigger System 1
def enter_combat(stat: list, battle: list):
    if stat[8] >= 1:
        t.sleep(0.75)
        kill = input('Use special attack? Kill enemy at once.\n(Press r to activate)\n')

        if kill == 'r':
            stat[7] = battle[8]
            stat[8] -= 1
            t.sleep(0.75)
            print('Forbidden art, activate!')
            return stat, battle

        else:
            while True:
                t.sleep(0.75)
                AttackType = input('Which attack are you going to activate?\n')

                if AttackType == 'm':

                    if stat[3] > 0:
                        stat[3] -= 1
                        stat[7] = round((r.randint(battle[6], battle[7])) * stat[6]) + stat[5]
                        t.sleep(0.75)
                        print('Magic Attack!')
                        return stat, battle

                    else:
                        t.sleep(0.75)
                        print('You do not have enough magic power to use a MagicAttack.')

                elif AttackType == 'p':
                    stat[7] = round((r.randint(battle[0], battle[1])) * stat[6]) + stat[4]
                    t.sleep(0.75)
                    print('Physical Attack!')
                    t.sleep(1)
                    return stat, battle

                else:
                    print('KeyError - invalid input for enter_combat function.')

# Trigger System 2
def enter_status(stat: list):
    print('Function 1 - Status inspector (Press 1 to trigger)')
    print('Function 2 - RPG Store Entrance (Press 2 to trigger)')

    while True:

        StatusInspector = input('Which function are you going to adopt?\n')
        if StatusInspector == '1':
            print("You are alive!\nYour current HP : [{}]\nYour current BankSavings : [{}]\nYour current MP : [{}]".format(stat[1], stat[2], stat[3]))

        elif StatusInspector == '2':
            print('Welcome to RPG Store! What can I help you here, little buddy?')
            print('(For MPRecovery, press \'m\'\nFor HPRecovery, press \'l\'\nFor GadgetPurchase, press \'g\'(More info HERE!)\nIf you want to quit ShopMenu, press \'q\')')
            stat = buy_inshop(stat)

        quitstatus = input('Quit StatusInspector? (Press q)\n')
        if quitstatus == 'q':
            return stat


# Combat System
def combat(stat, battle, levelstatus):
    print('Monster appeared!')
    boss = r.randint(1001, 1002)
    if boss != 1002:
        battle[8] = r.randint(battle[4], battle[3])

    else:
        battle[8] = r.randint(50, 200) * stat[9]
    t.sleep(0.75)
    print("Enemy HP : [{}]. Try to beat it!".format(battle[8]))
    t.sleep(0.75)
    print("Player {} will go first.".format(player_name))
    t.sleep(0.75)

    while True:

        stat, battle = enter_combat(stat, battle)
        battle[8] -= stat[7]
        print("You made a {}-point attack!\n(Enemy HP : [{}] pt)".format(stat[7], battle[8]))
        t.sleep(0.75)

        if battle[8] <= 0:
            break

        t.sleep(0.75)
        stat[1] -= enemy_atk
        print("Enemy made a {}-point attack.\n(Player HP : [{}] pt)".format(battle[2], stat[1]))
        t.sleep(0.75)

        if stat[1] <= 0:
            stat[0] = 0
            break

        t.sleep(0.75)

    if stat[1] <= 0:
        sys.exit('You are dead.\nBetter luck next time.')

    else:
        print('You have successfully taken down the enemy!')
        stat[2] += r.randint(10, 20)
        battle[5] += 50
        t.sleep(0.75)
        print("Gained Exp!\nCurrent Exp : [{}]".format(levelstatus[1]))
        levelstatus = level(levelstatus)

    return stat, battle, levelstatus

# Initial settings
player_hp = 10  # HP Initial
money = 1000  # Money Initial
player_atk = 0
atk_min = 1  # Increase by Level
atk_max = 3  # Increase by Level
mp_atk_min = 4  # Increase by Level
mp_atk_max = 8  # Increase by Level
mp = 10  # Revive-able Variable
enemy_atk = 1  # Increase by Level
enemy_hp = 0
enemy_hp_min = 5  # Increase by Level
enemy_hp_max = 15  # Increase by Level
life = 1  # Status
combat_chance = 9000  # Event, Constant
chance_max = 10000  # Event, Increase After Every Battle
recover_max = 4  # MP Recovery Potion - Constant
recover_min = 2  # MP Recovery Potion - Constant
revive_max = 6  # HP Recovery Potion - Constant
revive_min = 4  # HP Recovery Potion - Constant
psc_atk_boost = 0  # PhysicalAttack Boost
m_atk_boost = 0  # MagicAttack Boost
reel = 0  # Special Skill AttackType
level = 1  # Level-Up System - Currently Testing
exp = 0  # Level-Up System - Currently Testing
level_atk_boost = 1  # Power-Up System - Currently Testing

player_name = input('Welcome to the RPG world!\nWhat is your name?\n')
stat = [life, player_hp, money, mp, psc_atk_boost, m_atk_boost, level_atk_boost, player_atk, reel, level]
battle = [atk_min, atk_max, enemy_atk, enemy_hp_max, enemy_hp_min, chance_max, mp_atk_min, mp_atk_max, enemy_hp]
event = [revived, earning, enter_status]
levelstatus = [level, exp, level_atk_boost]
while True:
    print("Don't forget to save your gaming process, {}.".format(player_name))
    input('File progress?\n')

    if True:
        pass

    chance = r.randint(1, chance_max)
    if chance <= combat_chance:
        stat = event[r.randint(0, len(event) - 1)](stat)

    else:
        stat, battle, levelstatus = combat(stat, battle, levelstatus)

    if stat[0] == 0:
        print('You are dead. Fortify yourself and we will see you in the distant future!')
        break