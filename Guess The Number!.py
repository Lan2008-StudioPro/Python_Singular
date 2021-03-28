import random
while True:
    ans=random.randint(1,99)
    rangea=1
    rangeb=99
    rounds=0
    while True:
        print('此數在',rangea,'到',rangeb,'之間。')
        g=input('請輸入您的猜測。')
        try:
            g=int(g)
        except:
            print('Invalid.')
            continue
        else:
            if g==ans:
                rounds+=1
                print('Congrats!')
                print("{} [{}] {}".format('(You made',rounds,'guesses.)'))
                break
            elif g<ans and g>rangea:
                rounds+=1
                rangea=g
                print('Incorrect.')
                continue
            elif g>ans and g<rangeb:
                rounds+=1
                rangeb=g
                print('Incorrect.')
                continue
            else:
                print('I suggest not to waste your guesses, dear player.\nTake note of that range.')
                continue
    w=input('Still want to play another round?\n(If yes,please enter A)'