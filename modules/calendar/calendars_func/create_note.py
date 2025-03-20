# Необходимый импорт для работы с потоками
import threading as thread

# Импорт модуля для показа уведомлений
import win10toast

# Не обязательный импорт
import customtkinter as ctk
 
# Импорт для чтения json файлов
from ...jsn_func.read_json import read_json

# Импорт функции записии в Google Calendar, и создания service 
from ...google.create_google_note import write_event
from ...google.service_func import create_service

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
    
    # Для безопастности приложения
    try:
        # Создаем сервис для работы с Google Calendar
        service = create_service()

        # Формируем время начала и конца события в формате "Год-Месяц-ДеньTHчас:Минута:Секунда"
        start_time = f'{now.year}-{now.month:02d}-{now.day:02d}T{now.hour:02d}:{00:02d}:{00:02d}'
        end_time = f'{now.year}-{now.month:02d}-{index_day:02d}T{slider_hour:02d}:{00:02d}:{00:02d}'



        # Записываем в Google Calendar событие с уведомлением
        write_event(
            service = service,
            event_text = title,
            place = "None",
            description = text,
            start_time = start_time,
            end_time = end_time, 
            timezone = "UTC", # Пока UTC, потом можно поменять на часовой пояс пользователя
            freq = "DAILY",
            interval = 5,
            count = 3, 
            email = 'duckandfiretto@gmail.com', # Пока думаю как реализовать  
            window_override = "popup",
            for_how = 10 # Время перед событием для напоминания (в минутах)
        )
        print(time_difference)
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

    # Перехватываем исключения и показываем ошибки
    except Exception as error:
        toast_notify.show_toast(title = "Error", msg = error, duration = 5)
        print(f'Произошла ошибка при создании события: {error}')