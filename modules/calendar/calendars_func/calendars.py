import datetime
import calendar

now = datetime.datetime.now()
count_days = calendar.monthrange(now.year, now.month)

def get_count_days():
    now = datetime.datetime.now()
    count_days = calendar.monthrange(now.year, now.month)
    return count_days[1]