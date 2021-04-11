"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
的質數顯示在螢幕上，其餘不顯示。
"""
try:
    n=int(input())
except:
    print('ValueError')
else:
    if n>1:
        for m in range(2,n+1):
            for i in range(2,m):
                if m%i==0:
                    break
            else:
                print(m)
    else:
        print('Error.')