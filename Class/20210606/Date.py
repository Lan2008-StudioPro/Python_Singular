import datetime
Date = datetime.datetime.today()
# special format
'''
print(Date)
print(Date.year)
print(Date.month)
print(Date.day)
'''
# datetime_to_string
print(Date.strftime('%d %b %B %Y %y %A %a'))

# string_to_datetime
day = input("When is your birthday?\n(yyyy/mm/dd)\n")
print(day)
birth = datetime.datetime.strptime(day, "%Y/%m/%d")
print(birth.date())
print(birth.strftime('%d %b %B %Y %y %A %a'))

# %d = day
# %b = abbr. month_name ; %B = full month_name
# %y = %2d year_num ; %Y = %4d year_num
# %a = abbr. week_name ; %A = full week_name

birthday = input("Whem is your next birthday?\n(yyyy/mm/dd)\n")
birthday = datetime.datetime.strptime(birthday, "%Y/%m/%d")
print(birthday)
print(Date)
print(birthday - Date)