'''
請使用def畫出10個，不同顏色的屋頂，及位置的房子
顏色用list用代入
'''
import random as r
import turtle as t
list_color = ['lightcoral', 'darkturquoise', 'springgreen',
              'wheat', 'dodgerblue', 'crimson', 'fuchsia',
              'chartreuse', 'mediumslateblue', 'tan']
def draw_house(a: int):
    house = 0
    while house != a:
        t.pu()
        width = r.randint(-2, 10)
        length = r.randint(8, 30)
        x = r.randrange(-600, 600, 30)
        y = r.randrange(-200, 200, 10)
        t.color(list_color[r.randint(0, 9)])
        t.goto(x, y)
        t.seth(180)
        t.ht()
        t.speed(0)
        t.pd()
        t.begin_fill()
        t.fd(50)
        t.goto(x - 50 - 7, y - 24)
        t.bk(64)
        t.goto(x, y)
        t.end_fill()  # End of roof-drawing.
        t.pu()
        t.goto(x - width, y - 24)
        t.color(list_color[r.randint(0, 9)])
        t.pd()
        t.begin_fill()
        t.goto(x - width, y - 24 - length)
        t.goto(x - width - (25 - width) * 2, y - 24 - length)
        t.goto(x - width - (25 - width) * 2, y - 24)
        t.end_fill()  # End of base-drawing.
        t.pu()
        house += 1

draw_house(10)  # Enter the amount of houses you want to draw with TURTLE.