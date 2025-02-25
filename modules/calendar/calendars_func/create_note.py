'''
    `Модуль`, который содержит функцию `notify_message`, которая показывает уведомление с помощью `win10toast`
'''

# Необходимый импорт
from win10toast import ToastNotifier
# Необязательный импорт 
import customtkinter as ctk

# Создаем объект от класса
toast_notify = ToastNotifier()

def notify_message(entry_frames: dict = ctk.CTkEntry):
    '''
    `Функция`, которая показывает уведомление с помощью `win10toast`
    '''
    title = entry_frames["TITLE_NOTE"].get()
    text = entry_frames["TEXT_NOTE"].get()
    try:
        duration = int(entry_frames["DURATION_NOTE"].get())
    except Exception as e:
        toast_notify.show_toast(title="Ошибка", msg=str(e), duration=5, threaded=True)
    finally:
        toast_notify.show_toast(title = title, msg = text, duration = duration, threaded = True)

# Надо ли использовать потоки ? 