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
    a=1
    n=input()
    try:
        m=int(n)*2-1
    except:
        print("{}'{}'".format('ValueError: invalid literal for int() with base 10: ',n)
    else:
        while a!>n:
        print('{}{}{}'.format(' '*[(m-1)/2-a+1],'*'*(a*2-1),' '*[(m-1)/2-a+1])
        a+=1