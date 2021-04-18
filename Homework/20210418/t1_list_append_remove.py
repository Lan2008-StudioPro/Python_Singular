'''
讓使用者輸入一個str，當str有在list裡面，就移除該str
沒有str就加入list, 並顯示最後的list，list初使值為
["apple", "ball" ,"car"]
'''
list =[ "apple" , "ball" ,"car" ]

# index 寫法
a=input()
try:
    print( list.index( "a" )
except:
