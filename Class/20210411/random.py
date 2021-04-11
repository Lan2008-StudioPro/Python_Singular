for i in range(1,11):
    if i!=5 and i!=7:
        print(i)

for i in range(1,11):
    if i==5 or i==7:
        continue
        print(i)
'''
random.choice(range(a,b))   不包含 b
random.randint(a,b)    包含 b
'''
import math
import random
rounds=0
while True:
    die=random.randint(1,10)
    print(die)
    rounds+=1
    if die==7:
        print('你骰了',rounds,'次。')
        break
    elif die==5:
        print('Uh-oh. Something went wrong.')
        break
