#'''
a=int(input('平地大小?'))
b=int(input('坑洞大小?'))
print('\\\{}V{}V{}V{}V{}V{}V{}V{}V{}//'.format('-'*a, 'v'*b, '-'*a, 'v'*b, '-'*a, 'v'*b, '-'*a, 'v'*b, '-'*a))
print('P\nY\nT\nH\nO\nN')
#'''
'''
特殊字元 " \n "可用於 print 時將文字換行
('{}'.format())是用於將字串組合之間的空格刪除，一個 " {} "要對應到一個('')
'''
#'''
print(type("hello"))# 字串( str )
print(type(1))# 整數( int )
print(type(True))# " True " 以及 " False " 屬於布林值( bool )，用於判斷真假。
print(type(1.))# 浮點數( float )的特色在於具有小數點(.)
#'''

'''
運算子： " / " 是正常除法；" // " 是無條件捨去法；" % " 是取除法之後的餘數；" ** " 是次方
'''

print(3.14*((int(input('輸入半徑')))**2))