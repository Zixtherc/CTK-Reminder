# Необходимые импорты
import datetime
import calendar

def get_count_days():
    '''
    `Функция`, которая возвращает количество дней в текущем месяце
    '''
    now = datetime.datetime.now()
    count_days = calendar.monthrange(now.year, now.month)
    return count_days[1]