"""
Topic:請使用input輸入要印制的箭頭大小
可利用字串乘法
e.g.
val="*" * 3
print(val)
***
 for a in range(1,n+1)

1.Show:Please in row:
2.input:3
  *
 ***
*****
  *
  *
  *
"""

while True:
    n=input()
    try:
        n=int(n)
    except:
        print("{}'{}'".format('ValueError: invalid literal for int() with base 10: ',n))
    else:
        for a in range(1,n+1):
            print("{}{}".format(' '*(n-a),'*'*(a*2-1)))

        for a in range(1,n+1):
            print("{}{}".format(' '*(n-1),'*'))

