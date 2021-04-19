import random as r,time as t
null=0

while null==0:
    # 生成千位數 a
    a=r.randint(0,9)

    # 生成百位數 b
    b=r.randint(0,9)
    while b==a:
        b=r.randint(0,9)


    # 生成十位數 c
    c=r.randint(0,9)
    while c==b or c==a:
        c=r.randint(0,9)

    # 生成個位數 d
    d=r.randint(0,9)
    while d==c or d==b or d==a:
        d=r.randint(0,9)

    #ans=[str(a),str(b),str(c),str(d)]
    #print(''.join(ans))
    rounds=0
    history=[]

    while True:
        A=0
        B=0
        experiment=[]
        guess=input('Please enter a four digits number with none of them repeated with others.\n')
        rounds+=1

        try:
            guess=int(guess)

        except:
            t.sleep(1)
            print('Invalid.')
            t.sleep(1)
            rounds-=1

        else:

            if guess<123 or guess>9877:
                t.sleep(1)
                print('ValueError.')
                t.sleep(1)
                rounds-=1
                continue

            elif guess in history:
                print('You have input a repeated answer, I suggest you not to waste your precious guesses.')
                rounds-=1
                t.sleep(1)
                continue

            else:
                e=guess//1000
                f=(guess-1000*e)//100
                g=(guess-1000*e-100*f)//10
                h=guess-1000*e-100*f-10*g
                experiment=[e,f,g,h]
                ans=[a,b,c,d]
                for digits in range(0,4):
                    if experiment[digits] in ans and experiment[digits]!=ans[digits]:
                        B+=1
                    elif experiment[digits]==ans[digits]:
                        A+=1

            if A==4:
                print('Congratulation!\nYou made【',rounds,'】guesses.')
                t.sleep(1)
                decision=input('Want to play another game?\nEnter \'Y\' for \'Yes\' and any other key for \'No\'\n')

                if decision=='Y':
                    break

                else:
                    null+=1
                    break

            else:
                history.append(guess)
                print("{}\n{}：{}{}{}{}".format('Answer incorrect.',guess,A,'A',B,'B'))
                t.sleep(1)

print('Thanks for your playing!')
t.sleep(1)
print('Leave a comment down here or like this website. You can also be our PATRON !')


# " listc = lista + listb " 用於合併字串；
# " listx.split( ' ' ) " 用於利用 '' 裡面的文字為分隔單位切割成 list
# " listy = listx.join( ' ' ) " 用於將 list 合併為字串
# 新增元素 ' .append() '；刪除元素 ' .remove() '