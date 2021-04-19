from microbit import *
import time as t
boat1=Image("23432:34543:45654:34543:23432")
boat2=Image("34543:45654:56765:45654:34543")
boat3=Image("45654:56765:78987:37873:45654")
boat4=Image("56765:78987:89998:78987:56765")
anim=['boat1','boat2','boat3','boat4']
mina=sorted(anim,reverse=True)
fps=1/7
while True:
    num=sort()
    for i in anim:
        display.show(i)
        t.sleep(fps)
    for i in mina:
        display.show(i)
        t.sleep(fps)