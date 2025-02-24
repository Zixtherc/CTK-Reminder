import datetime
import calendar

def get_count_days():
    now = datetime.datetime.now()
    count_days = calendar.monthrange(now.year, now.month)
    return count_days[1]