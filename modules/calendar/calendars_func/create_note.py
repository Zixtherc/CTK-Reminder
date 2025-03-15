# Необходимый импорт для работы с потоками
import threading as thread

# Импорт модуля для показа уведомлений
import win10toast

# Не обязательный импорт
import customtkinter as ctk
 
# Импорт для чтения json файлов
from ...jsn_func.read_json import read_json

# Импорт функции записии в Google Calendar
from ...google.create_google_note import write_event

# Создаем объект от класса уведомлений
toast_notify = win10toast.ToastNotifier()

# Необходимые модули для работы со временем
import datetime
# Этот модуль так же нам позволяет приостановить программу
import time

def notify(entry_frames: dict = ctk.CTkEntry, slider_hour: object = ctk.CTkSlider, slider_time: object = ctk.CTkSlider):
    '''
    #### `Функция`, `запускает` поток `функции` показа уведомлений  ####
    Параметры: 
    - `entry_frames:` Словарь `полей` ввода текста;
    - `index_day:` `День недели`, на который нужно `отправить` уведомление;
    - `slider_hour:` В который `час` нужно `отправить` уведомление;
    - `slider_time:` В какую `
    '''

    # Читаем json файл, оттуда берем какой день выбрал пользователь
    index_day = read_json(filename = "utility.json")

    # Получаем время выбранное пользователем
    slider_hour = int(slider_hour.get())
    slider_time = int(slider_time.get())

    # Получаем текст из полей ввода
    title = str(entry_frames["TITLE_NOTE"].get())
    text = str(entry_frames["TEXT_NOTE"].get())

    # Поток для автономного отключение, + что бы не "останавливал" программу, 
    # параметр daemon помогает нам АВТОМАТИЧЕСКИ завершить поток т.к мы его не может останавливать, поток так же работает в фоновом режиме 
    # В args передаем параметры нашей функции показа уведомлений. ВАЖНО расставлять их в том порядке, в котором они в функции 
    first_thread = thread.Thread(target = create_notify, daemon = True, args = (index_day, slider_hour, slider_time, title, text))
    # Запускаем поток
    first_thread.start()


def create_notify(index_day: int, slider_hour: int, slider_time: int, title: str, text: str):
    '''
    #### `Функция`, которая показывает уведомление с помощью `win10toast` ####
    Параметры: 
    - `index_day:` `День`, на который нужно `отправить` уведомление;
    - `slider_hour:` В который `час` нужно `отправить` уведомление;
    - `slider_time:` В какую `минуту` нужно `отправить` уведомление;
    - `title:` `Заголовок` уведомления;
    - `text:` `Текст` уведомления;
    '''

    # Получаем текущее время
    now = datetime.datetime.now()
    # Получаем время выбранное время пользователя
    notify_time = now.replace(day = index_day, hour = slider_hour, minute = slider_time, second = 0, microsecond = 0) 

    # Если выбранное время меньше текущего времени, показываем ошибку и выходим из функции
    if notify_time < now:
        # Показываем ошибку
        toast_notify.show_toast(title = "Error", msg = "Error", duration = 5)
        # Выходим
        return 
    
    # Рассчитываем разницу во времени, и переводим все в total second, с начала юникс эпохи
    time_difference = (notify_time - now).total_seconds()
    
    # write_event(service = )

    # Ждём указанное время
    time.sleep(time_difference)
    if text and title:
        # Показываем уведомление
        toast_notify.show_toast(title = title, msg = text, duration = 10)
        # Выходим
        return 
    else:
        # Показываем ошибку
        toast_notify.show_toast(title = "Error", msg = "Error", duration = 5)
        # Выходим
        return 