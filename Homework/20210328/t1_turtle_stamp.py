"""
Topic:請使用turtle及loop印出下列圖形

e.g.
turtle_stamp.jpg
可利用turtle.home()會回到原點(0.0)的特性
"""

import turtle as t
a=0
b=45
t.speed(0)
while a!=8:
    t.shape('classic')
    t.setheading(b)
    t.penup()
    t.forward(100)
    t.pendown()
    t.stamp()
    t.penup()
    t.home()
    b+=45
    a+=1
