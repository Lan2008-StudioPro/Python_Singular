import turtle as t, random as r
def draw_leaf(x, y):
    t.penup()
    t.speed(0)
    t.hideturtle()
    t.goto(x, y)
    t.shape('circle')
    t.setheading(0)
    a=r.uniform(0.001,0.255)
    g=r.uniform(0.001,0.255)
    b=r.uniform(0.001,0.255)
    t.color((a,g,b))
    t.pendown()
    t.begin_fill()
    q = 0.25
    w = 1
    while w <= 210:
        t.forward(q)
        t.right(w)
        t.speed(0)
        q += 0.25
        w += 1
    t.end_fill()

def draw_trunk(x, y):
    t.penup()
    t.speed(0)
    t.hideturtle()
    t.goto(x, y)
    t.shape('circle')
    t.setheading(0)
    t.pendown()
    a=r.uniform(0.001,0.255)
    g=r.uniform(0.001,0.255)
    b=r.uniform(0.001,0.255)
    t.color((a,g,b))
    t.begin_fill()
    t.forward(3)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(6)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(3)
    t.right(90)
    t.end_fill()

while True:
    x=r.randint(-500,500)
    y=r.randint(-300,300)
    draw_trunk(x,y)
    draw_leaf(x,y+25)