'''
import random as r
a=r.randint(0,9)
b=r.randint(0,9)
while b!=a:
    break
    b=r.randint(0,9)
c=r.randint(0,9)
while c!=b and c!=a:
    break
    c=r.randint(0,9)
d=r.randint(0,9)
while d!=c and d!=b and d!=a:
    break
    d=r.randint(0,9)
'''
num=['a','b','c','d']

for i in range(0,len(num),2):
    print(num[i])

for i in num:
    print(i)

# " listc = lista + listb " 用於合併字串；
# " listx.split( ' ' ) " 用於利用 '' 裡面的文字為分隔單位切割成 list
# " listy = listx.join( ' ' ) " 用於將 list 合併為字串
# 新增元素 ' .append() '；刪除元素 ' .remove() '

mun=[]
for i in num:
    mun.append(i)
mun.remove('b')
print(num)
print(mun)