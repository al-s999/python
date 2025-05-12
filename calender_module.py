import calendar
from calendar import weekday, day_name

# m d y is month, day and year
m,d,y = map(int, input().split())

# use function weekday from calendar to get number day (0 = monday)
day = calendar.weekday(y,m,d)

days = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]

# print array days index day
print(days[day])

# example : input = 2 25 2025
#           output = TUESDAY
#   note = calendar.weekday is return number and for this input is return 1, because monday is 0, tuesday is 1