"""
Topic:請使用turtle及loop及time.sleep(1)印出秒針動畫

e.g.
import time
time.sleep(1)
"""
import time
import turtle as t
a=90
t.speed(0)
while True:
    t.clearscreen()
    t.setheading(a)
    t.forward(70)
    t.home()
    a-=6
    time.sleep(1)
