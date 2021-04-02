import turtle as t
import random as r

while True:
    t.hideturtle()
    t.penup()
    q=1
    w=1
    x=r.randint(-360,360)
    y=r.randint(-200,200)
    a=r.uniform(0.001,0.255)
    g=r.uniform(0.001,0.255)
    b=r.uniform(0.001,0.255)
    t.setx(x)
    t.sety(y)
    t.color((a,g,b))
    t.pendown()
    while w<=180:
        t.forward(q)
        t.right(w)
        t.speed(0)
        q+=1
        w+=1
        t.shape('classic')
        t.stamp()



