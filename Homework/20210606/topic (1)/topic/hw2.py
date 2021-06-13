'''
電影分及制:讓使用者輸入
年齡18歲以上，顯示為"限制級"
年齡13歲以上但不滿18歲，顯示為"輔導級"
年齡12歲以下，顯示為"普通級"
其他則是，顯示"未知"
'''
age = input()
try:
    age = int(age)
except ValueError:
    print('未知')
else:
    if (age >= 18):
        print('限制級')
    elif (13 <= age < 18):
        print('輔導級')
    elif (age < 13):
        print('普通級')