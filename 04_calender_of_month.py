# any calender of input month

import calendar
y = int(input("year : "))
m = int(input("month : "))
print(calendar.month(y,m))

# diff btw two dates

from datetime import date
firstdate = date(2020,9,12)
lastdate=date(2020,9,10)

diff= firstdate-lastdate
print(diff)
