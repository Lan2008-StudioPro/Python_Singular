'''
顯示今天的日期，
零食的保存期限為2/21/2022，
請顯示還有多久會到保存期限。
'''
import datetime
Date = datetime.datetime.today()
print(Date)
Expire = '2/21/2022'
expire = datetime.datetime.strptime(Expire, "%m/%d/%Y")
print(expire - Date)