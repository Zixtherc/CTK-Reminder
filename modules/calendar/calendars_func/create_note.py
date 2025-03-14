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

def notify(entry_frames: dict = ctk.CTkEntry, slider_hour: object = ctk.CTkSlider, slider_time: object = ctk.CTkSlider):
    index_day = read_json(filename = "utility.json")

    slider_hour = int(slider_hour.get())
    slider_time = int(slider_time.get())

    title = str(entry_frames["TITLE_NOTE"].get())
    text = str(entry_frames["TEXT_NOTE"].get())

    # Поток для автономного отключение, + что бы не "останавливал" программу
    first_thread = thread.Thread(target = create_notify, daemon = True, args = (index_day, slider_hour, slider_time, title, text))
    print(f'поток запущен')
    first_thread.start()


def create_notify(index_day: int, slider_hour: int, slider_time: int, title: str, text: str):
    '''
    `Функция`, которая показывает уведомление с помощью `win10toast`
    '''

    
    toast_notify.show_toast(title, text, duration = 10)