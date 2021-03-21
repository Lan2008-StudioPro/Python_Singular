#分數值的計算

while True:
    a=input('Please input Numerator:')
    b=input('Please input Denominator:')

    try:
        a=int(a)
        b=int(b)
    except:
        print('error')
    else:
        if a/b==350/450:
            print('True')
        else:
            print('False')


"""
Topic:輸入分子及分母，確認是否等於 350/450:

Show:Please input numerator"
Input1:70

show:Please input Denominator:
Input2:90
Output:True

Input1:6
Input2:9
Output:False
"""