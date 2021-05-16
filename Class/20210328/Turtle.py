import turtle as t
import random as r

while True:
    t.ht()
    t.pu()
    q = 1
    w = 1
    x = r.randrange(-500, 500, 50)
    y = r.randrange(-300, 300, 50)
    a = r.uniform(0.001, 0.255)
    g = r.uniform(0.001, 0.255)
    b = r.uniform(0.001, 0.255)
    t.setx(x)
    t.sety(y)
    t.color((a, g, b))
    t.pd()
    while w <= 240:
        t.fd(q)
        t.rt(w)
        t.speed(0)
        q += 1
        w += 1

