# и увидеть приложение, так же помогут не "останавливать" приложение при задержки уведомления
import threading as thread

import win10toast

import customtkinter as ctk
 
# Импорт для чтения json файлов
from ...jsn_func.read_json import read_json

# Создаем объект от класса
toast_notify = win10toast.ToastNotifier()

import datetime as dttime
import time

def notify(entry_frames: dict = ctk.CTkEntry, timer: int = 10):
    index_day = read_json(filename = "utility.json")
    # Поток для автономного отключение, + что бы не "останавливал" программу
    first_thread = thread.Thread(target = create_notify, daemon = True, args = (entry_frames, index_day, timer))
    first_thread = thread.Thread(target = create_notify, daemon = True, args = (index_day, entry_frames, timer))
    print(f'поток запущен')
    first_thread.start()


def create_notify(index_day: int, entry_frames: dict = ctk.CTkEntry, timer: int = 10):
    '''
    `Функция`, которая показывает уведомление с помощью `win10toast`
    '''
    
    title = entry_frames["TITLE_NOTE"].get()
    text = entry_frames["TEXT_NOTE"].get()
    title = str(entry_frames["TITLE_NOTE"].get())
    text = str(entry_frames["TEXT_NOTE"].get())

    time.sleep(timer)
    toast_notify.show_toast(title, text, duration = 10)