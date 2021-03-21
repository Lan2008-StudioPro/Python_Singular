from microbit import *
compass.calibrate()#重新校正指南針
#display.show()#讀取數值並顯示

while True:#重複
    a=compass.heading()
    if a>=46 and a<=134:
        display.show('E')
    elif a>=135 and a<=224:
        display.show('S')
    elif a>=225 and a<=314:
        display.show('W')
    else:
        display.show('N')
