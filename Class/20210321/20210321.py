# '數值1' == '數值2' {比較 用於 if else 結構}
a=input('請輸入密碼:')
b=input('我叫什麼名字?')
c=input('我穿什麼顏色的衣服：')
if  a=="20080229Bn" and b=="藍立桓" and c=="深藍色":
    print('歡迎使用爛電腦')
else:
    print('錯誤')
'''
if elif else 多項判斷結構
if 判斷式１:
    程式Ａ
elif 判斷式２:
    程式Ｂ
else:
    程式Ｃ
'''

score=(input('請輸入分數：'))

try:#嘗試執行以下程式
    score = int(score)
except:#嘗試失敗：執行以下程式後直接結束
    print('不要亂弄校務行政系統啊 e04')
else:#嘗試成功：執行下方程式
    if score>=90 and score<=100:
        print('你的等級：Ａ級')
    elif score>=80 and score<=89:
        print('你的等級：Ｂ級')
    elif score>=70 and score<=79:
        print('你的等級：Ｃ級')
    elif score>=60 and score<=69:
        print('你的等級：Ｄ級')
    elif score<60 and score>=0:
        print('你的等級：Ｆ級')
    else:
        print('怎麼可能???')