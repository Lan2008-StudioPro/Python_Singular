#攝氏華氏溫度計
a=input('你要輸入攝氏還是華氏?')
if a=='攝氏':
    print('華氏溫度：',(int(input('輸入攝氏：')))*9/5+32)
elif a=='華氏':
    print('攝氏溫度：',((int(input('輸入華氏：')))-32)*5/9)