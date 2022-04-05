import calendar
import datetime
import time


print(calendar.weekheader (1))
print()
print(calendar.firstweekday())
print()
print(calendar.month(2022,4))
print(calendar.monthcalendar(2022,4))
print(calendar.calendar(2022))
da_of_the_week=calendar.weekday(2022,4,5)
is_leap=calendar.isleap(2022)
print(is_leap)
how_many_leap_days=calendar.leapdays(2021,2022)
print(how_many_leap_days)