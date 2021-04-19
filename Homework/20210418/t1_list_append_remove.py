'''
讓使用者輸入一個str，當str有在list裡面，就移除該str
沒有str就加入list, 並顯示最後的list，list初使值為
["apple", "ball" ,"car"]
'''
#print("{:05d}".format(5))

list = [ "apple" , "ball" ,"car" ]
print( list )
while True :
    a = input()
    b = input( 'Select mode.\nType in 1 to try out the "index" mode.\nType in 2 to try out the "in" mode.\nYour mode : ')
    if b == '1' :

        # index 寫法
        try :
            list.index( a )
        except :
            list.append( a )
        else :
            list.remove( a )
        list = sorted( list )
        print( list )

    elif b == '2' :

        # in 寫法
        if a in list :
            list.remove( a )
        else :
            list.append( a )
        list = sorted( list )
        print( list )

    else :
        print( 'Invalid.' )