'''
    `Модуль`, который содержит функцию `notify_message`, которая показывает уведомление с помощью `win10toast`
'''

# Необходимый импорт
from win10toast import ToastNotifier
# Необязательный импорт 
import customtkinter as ctk

# Создаем объект от класса
toast_notify = ToastNotifier()

import datetime as time

def notify_message(entry_frames: dict = ctk.CTkEntry, index_day: int = 0):
    '''
    `Функция`, которая показывает уведомление с помощью `win10toast`
    '''
    title = entry_frames["TITLE_NOTE"].get()
    text = entry_frames["TEXT_NOTE"].get()
    duration = 5 
    try:
        duration = int(entry_frames["DURATION_NOTE"].get())
    except Exception as error:
        print(f'Ошибка: {error}')
        toast_notify.show_toast(title="Ошибка", msg=str(error), duration=5, threaded=True)
    finally:
        now_date = time.datetime.now().strftime("%Y-%m-%d").split('-')
        now_day = int(now_date[-1])
        print(f'Это текущий день: {now_day}')
        print(f'Это текущая кнопка: {index_day}')
        
        # if now_day >= index_day:
        #     print(f'Нельзя ставить напоминания на предыдущии дни')
        # elif now_day <= index_day:
        toast_notify.show_toast(title = title, msg = text, duration = duration, threaded = True)