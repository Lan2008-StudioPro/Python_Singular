#三角形的周長與面積

while True:
    a=input('Please enter a.')
    b=input('Please enter b.')
    c=input('Please enter c.')

    try:
        a=int(a)
        b=int(b)
        c=int(c)
    except:
        print('Error')
    else:
        if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
            p=int((a+b+c)/2)
            print('Perimeter:',a+b+c)
            print('Area:',(p * (p - a) * (p - b) * (p - c)) ** 0.5)
        else:
            print('Invalid data detected. Check your input again.')

"""
Topic:輸入三角形三邊，判斷是否能構成三角形，
　　　是三角形則顯示面積和周長，不行則顯示，無法構成三角形:

Triangle Area formula:
p = 1/2 (a+b+c)
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

e.g.
Show:a ="
Input1:3

Show:b ="
Input2:4

Show:c ="
Input3:5

output:
perimeter: 12.000000
Area: 6.000000
"""