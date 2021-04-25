import random as r

def roll_dice(n :int) :
    dice = []
    for i in range(n) :
        dice.append(r.randint(1,6))
    return dice

def win(PLAYER , SYSTEM):
    print('PLAYER rolled {}.\nSYSTEM rolled {}.'.format(PLAYER, SYSTEM))
    if PLAYER>SYSTEM :
        print('PLAYER won.')
    elif PLAYER<SYSTEM :
        print('SYSTEM won.')
    else :
        print('Tie.')

num=int(input())
PLAYER=sum(roll_dice(n=num))
SYSTEM=sum(roll_dice(n=num))
win(PLAYER,SYSTEM)