'''
    `Модуль`, который содержит функцию `notify_message`, которая показывает уведомление с помощью `win10toast`
'''

# Необходимый импорт
from win10toast import ToastNotifier
# Необязательный импорт 
import customtkinter as ctk

# Создаем объект от класса
toast_notify = ToastNotifier()
# Необходимый модуль для работы с временем, в нашем случае для работы с отложенными уведомлениями
import datetime as dttime
import time

def notify_message(entry_frames: dict = ctk.CTkEntry, index_day: int = 0):
    '''
    `Функция`, которая показывает уведомление с помощью `win10toast`
    '''
    # Получаем значения из Entry полей
    title = entry_frames["TITLE_NOTE"].get()
    text = entry_frames["TEXT_NOTE"].get()
    # Устанавливаем базовое значение, через которое уведомление пропадёт
    duration = 5 

    # Используем блок try except finally, для безопастности
    try:
        # Пробуем получить информацию через сколько появится уведомление
        notify_delay = int(entry_frames["DURATION_NOTE"].get())
        notify_date = dttime.datetime.strptime(notify_delay, '%Y-%m-%d')
    # Отлавливаем ошибку, и сообщаем ошибку пользователю
    except Exception as error:
        # Выводим ошибку пользователю с помощью уведомления
        toast_notify.show_toast(title="Ошибка", msg=str(error), duration=5, threaded=True)

    # Далее идёт код, который В ЛЮБОМ СЛУЧАЕ, будет воспроизведён
    finally:
        # Получаем текущее время
        now = dttime.datetime.now()

        # Получаем текущее время у пользователю
        now = dttime.datetime.strptime(f"{now.year} {now.month} {now.day}", "%Y %m %d")

        # Получаем будущее время, в которое прийдёт уведомление
        future_time = dttime.datetime.strptime(f'{notify_delay[0]} {notify_delay[1]} {notify_delay[-1]}', '%Y %m %d')

        # Преобразовываем время в кортеж
        future_time_struct_time = future_time.timetuple()
        now_struct_time = now.timetuple()

        # Получаем Unix timestamp для будущего и текущего времени
        future_time_timestamp = time.mktime(future_time_struct_time)
        now_time_timestamp = time.mktime(now_struct_time)

        # Выводим разницу во времени между текущим и будущим временем в консоль
        print(now_time_timestamp - future_time_timestamp)

        
        # if now_day >= index_day:
        #     print(f'Нельзя ставить напоминания на предыдущии дни')
        # elif now_day <= index_day:
        
        toast_notify.show_toast(title = title, msg = text, duration = duration, threaded = True)