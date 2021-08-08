'''
老師正在設計一個Python程式，學生可以使用它來記錄他們考試的平均分數。
該程式必須允許使用者輸入他們的名字和當前分數。
該程式將輸出使用者名和使用者的平均分數。
輸出必須符合以下要求:
    1. 使用者姓名必須是靠左對齊的。
    2. 如果使用者姓名少於20個字元,必須在右側添加額外的空間。
    3. 平均分數在小數點左方是三位數,小數點右方是二位數。(XXX.XX)。
你要如何完成程式碼?請在回答區中選擇適當的程式碼片段。
'''
name = input("請輸入姓名")
score = count = 0
while (score != -1):
    score = int(input("輸入你的分數:(輸入-1結束程式)"))
    if score == -1:
        break
    sum += score
    count += 1
    average = sum / count
    print("(1), 你的平均分數是：(2)" % (name, average))
'''
(Ｄ)(1)A. %-20i B. %-20d C. %-20f D. %-20s
(Ｂ)(2)A. %1.6s B. %6.2f C. %6.2d D. %2.6f
'''