'''
    `Модуль`, который содержит функцию `notify_message`, которая показывает уведомление с помощью `win10toast`
'''

# Необходимый импорт
from win10toast import ToastNotifier

# Необязательный импорт 
import customtkinter as ctk

# Необходимый модуль для работы с потоками, они нам позволят закрыть приложение, 
# и увидеть приложение, так же помогут не "останавливать" приложение при задержки уведомления
import threading as thread


# Создаем объект от класса
toast_notify = ToastNotifier()

# Создаем первый поток ( в будущем их будет столько, сколько уведомлений решил сделать пользователь )


# Необходимый модуль для работы с временем, в нашем случае для работы с отложенными уведомлениями
import datetime as dttime
import time

def notify(title: str = "error", message: str = "error", duration: int = 5, delay_notify: int = 5):
    '''
    `Функция`, которая показывает уведомление с помощью `win10toast`
    '''
    toast_notify.show_toast(title = title, duration = 5, message = message, threaded = True)

def create_notify(entry_frames: dict = ctk.CTkEntry, index_day: int = 0, timer: int = 10):
    '''
    `Функция`, которая показывает уведомление с помощью `win10toast`
    '''
    
    title = entry_frames["TITLE_NOTE"].get()
    text = entry_frames["TEXT_NOTE"].get()
    duration = 5
    timer = timer
    # while True:
    #     time.sleep(5)
    #     print(f'Получилось запустить поток')

# Поток для автономного отключение, + что бы не "останавливал" программу
first_thread = thread.Timer(interval = 10, function = create_notify)
    # # Получаем значения из Entry полей
    # title = entry_frames["TITLE_NOTE"].get()
    # text = entry_frames["TEXT_NOTE"].get()
    # # Устанавливаем базовое значение, через которое уведомление пропадёт
    # duration = 5 

    # # Используем блок try except finally, для безопастности
    # try:
    #     # Пробуем получить информацию через сколько появится уведомление
    #     notify_delay = int(entry_frames["DURATION_NOTE"].get())
    #     notify_date = dttime.datetime.strptime(notify_delay, '%Y-%m-%d')
    # # Отлавливаем ошибку, и сообщаем ошибку пользователю
    # except Exception as error:
    #     # Выводим ошибку пользователю с помощью уведомления
    #     toast_notify.show_toast(title="Ошибка", msg=str(error), duration=5, threaded=True)

    # # Далее идёт код, который В ЛЮБОМ СЛУЧАЕ, будет воспроизведён
    # finally:
    #     # Получаем текущее время
    #     now = dttime.datetime.now()

    #     # Получаем текущее время у пользователю
    #     now = dttime.datetime.strptime(f"{now.year} {now.month} {now.day}", "%Y %m %d")

    #     # Получаем будущее время, в которое прийдёт уведомление
    #     future_time = dttime.datetime.strptime(f'{notify_delay[0]} {notify_delay[1]} {notify_delay[-1]}', '%Y %m %d')

    #     # Преобразовываем время в кортеж
    #     future_time_struct_time = future_time.timetuple()
    #     now_struct_time = now.timetuple()

    #     # Получаем Unix timestamp для будущего и текущего времени
    #     future_time_timestamp = time.mktime(future_time_struct_time)
    #     now_time_timestamp = time.mktime(now_struct_time)

    #     # Выводим разницу во времени между текущим и будущим временем в консоль
    #     print(now_time_timestamp - future_time_timestamp)

        
    #     # if now_day >= index_day:
    #     #     print(f'Нельзя ставить напоминания на предыдущии дни')
    #     # elif now_day <= index_day:
        
    #     toast_notify.show_toast(title = title, msg = text, duration = duration, threaded = True)

first_thread.start()