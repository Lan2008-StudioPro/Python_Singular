# 語法 " while 判斷式 " 有條件的迴圈
'''
n=9
while n>0:
    print(n)
    n-=1
#顯示 1～9
'''
while True:
    n=input('終止值')
    ans=0
    try:
        n = int(n)
    except:
        print('Error.')
        pass
    else:
        for i in range(1, n+1):
            ans+=i
        print(ans)

n=int(input())
for a in range(1,n+1):
    while a<n*2:
        print({}{}{}.format(' '*(n-a),'|'*a,' '*(n-a)))
    print('*')
