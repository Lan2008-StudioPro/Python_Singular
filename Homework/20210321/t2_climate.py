#溫度問題

while True:
    a=input('今天攝氏幾度？')
    try:
        a=int(a)
    except:
        print('蛤？我問你溫度你回答這什麼鬼東西？')
    else:
        if a>=40:
            print('怎麼可能？這麼熱！')
        elif a<=10:
            print('天哪！太冷了吧～')
        else:
            print('真舒適的溫度！')

"""
Topic:輸入溫度，如果溫度>=40度C,顯示: 太熱,
　　　如果溫度<= 10 顯示:太冷, 其他：舒適:

Show:Please input temperature:"
Input1:40
Output:It's too hot.
"""