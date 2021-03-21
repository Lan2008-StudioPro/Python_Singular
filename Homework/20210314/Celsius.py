#攝氏華氏溫度計

while True:
    a=input('(提示：想要攝氏轉為華氏，請輸入A；想要華氏轉為攝氏，請輸入B)\n請選擇您想要執行的模式：')#通常不會要求使用者輸入中文
    if a=='A' or a=='B':
        if a=='A':
            print('華氏溫度：',(int(input('輸入攝氏：')))*9/5+32)
        elif a=='B':
            print('攝氏溫度：',((int(input('輸入華氏：')))-32)*5/9)
        a=input('您還要繼續使用本轉換計算機嗎？\n(若要繼續，請輸入Y；若要結束，請按任意鍵。）\n')
        if a=='Y':
            continue
        else:
            break
    else:
        print('Invalid input. Try again.')
        continue