# Ctk-Reminder

## Основная цель проекта 
Более тесное знакомство с ООП, умение организовывать грамотный файлменеджмент, умение работать с большим объёмом новой информации, поработать с Google API Calendar

### Навигация по README
- [Цель проекта](#основная-цель-проекта)
- [Описание проекта](#описание-проекта)
- [Преимущества](#преимущества)
- [Функционал](#функционал)
- [Использованные модули](#модули)
- [Структура проекта](#структура-проекта)
- [Важные моменты кода](#важные-моменты-кода)
- [Как запустить](#запуск)
- [Итог](#итог)
- [Контакты связи](#контакты-связи)

## Описание проекта
Это приложение предоставляет возможность авторизации и регистрации пользователей, а также позволяет легко и удобно создавать заметки на ПК или ноутбуке. Важно, что каждая заметка может быть автоматически добавлена в Google Календарь и связана с электронной почтой, указанной пользователем при регистрации.


### Преимущества
Я постарался создать простой и чистый код, чтобы у любого новичка не возникало вопросов о том, как и почему это работает. Практически к каждой строке я добавил комментарии (все ещё добавляю). Также внимание уделено функциям, классам и модулям моего приложения.

### Функционал
- Авторизация и регистрация пользователей: Пользователи могут зарегистрироваться с использованием электронной почты, а затем авторизоваться в приложении

- Создание заметок: Простой и удобный интерфейс для создания, редактирования и удаления заметок ( в разработке )

- Интеграция с Google Календарем: Возможность добавлять заметки как события в Google Календарь для удобства планирования

- Отправка уведомлений на электронную почту: При создании заметки пользователь может получить уведомление на почту


## Модули:
- customtkinter (GUI)
- json (JSON files)
- google_modules (google auth and calendar)
- datetime (Time)
- time (time.sleep)
- aiosqlite3 (database)

## Важные моменты кода:

#### Функция смены фрейма: ####
```python 
async def swith_frame(root: object = ctk.CTk, frame_name: str = ctk.CTkFrame, slider_for_notify: object = ctk.CTkSlider):
    """
    Функция для переключения на другой фрейм.

    Параметры:
    - `root:` Объект главного окна;
    - `frame_name:` Фрейм на который мы размещаем;

    Пример использования:
    ```python
        await swith_frame(root = root, frame_name = 'MAIN_FRAME')
    ```
    """
    # Перебираем все Frame которые мы получили 
    for frame in root.frames.values():
        # Скрываем каждый 
        frame.pack_forget()
        frame.place_forget()

    # Условие для размещения уведомлений
    if frame_name == 'MAIN_FRAME' and frame_name in root.frames:
        # Читаем json файл
        data = read_json(filename = 'user_info.json')
        # Получаем количество всех заметок
        data = await db_note.get_all_notes(nickname = data['nickname'])
        count_notes = len(data)
        # Получаем объект фрейма
        frame = root.frames[frame_name]
        # # Размещяем фрейм и текст
        frame.update_notes(count_notes = count_notes, frame_position = slider_for_notify, note_data = data) 

    # Если указанный фрейм существует в словаре
    if frame_name in root.frames:
        # Переименовываем
        frame = root.frames[frame_name]
        # Размещаем ( relwidth  это ширина нашего фрейма, который будет "замещать" основной HEADER, и его будет не видно)
        frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)
```

#### Функция авторизации/регистрации пользователя: ####
```python
async def auth_function(auth_action: str = None, entry_frames: dict = None, root: ctk.CTk = None, slider_for_notify: ctk.CTkSlider = None):
    '''
    `Асинхронная` `функция`, который принимает в себя параметры:

    - `auth_action:` Тип авторизации;
    - `entry_frames:` Словарь со всеми Frame;
    - `root:` Объект главного окна;

    Нужна это функция для того, что бы если пользователь пытается авторизоваться в базу данных, но такого пользователя ещё нет,
    его не перебрасывало на страницу с календарём
    '''
    # Если пользователь выбрал регистрацию
    if auth_action == 'register':
        # Вызываем метод базы данных, и записываем в переменную flag_register ответ от базы данных
        # Метод get() позволяет нам взять текст с фреймов Entry 
        if not all([entry_frames["NAME"].get().strip(), entry_frames["PASSWORD"].get().strip(), entry_frames["EMAIL"].get().strip()]):
            TopLevelWidget(ch_master = root, ch_width = 350, ch_height = 300, ch_fg_color = "#808080", label_text = "Error: You cannot leave the input fields empty")
            return
        flag_register = await db.insert_user(
            name = entry_frames["NAME"].get(),
            password = entry_frames["PASSWORD"].get(),
            email = entry_frames["EMAIL"].get())

        # Если флаг True (Пользователь успешно зарегистрировался), если False, вероятнее всего произошла ошибка 
        if flag_register:
            # Записываем в JSON файл информацию о том, что пользователь зарегистрировался
            log = {"user_status" : "registered"}
            write_json(filename = "utility.json", obj_dict = log)
            # Если пользователь успешно зарегистрировался, переводим его на главную страницу
            await logged_user(root = root, slider_for_notify = slider_for_notify)
            # Записываем в JSON файл информацию о никнейме пользователя
            log = {"nickname" : entry_frames["NAME"].get()}
            write_json(filename = "user_info.json", obj_dict = log)

    # Если пользователь выбрал авторизацию     
    elif auth_action == "login":
        # Вызываем метод базы данных, и записываем в переменную flag_login ответ от базы данных
        flag_login = await db.find_user(
            name = entry_frames["LOGIN_NAME"].get(),
            password = entry_frames["LOGIN_PASSWORD"].get())
        # Если флаг True (Пользователь успешно авторизовался), если False, вероятнее всего такого пользователя нету
        if flag_login:
            # Записываем в JSON файл информацию о том, что пользователь авторизовался
            log = {"user_status" : "logged"}
            write_json(filename = "utility.json", obj_dict = log)
            # Если пользователь успешно зарегистрировался, переводим его на главную страницу
            await logged_user(root = root, slider_for_notify = slider_for_notify)
            # Записываем в JSON файл информацию о никнейме пользователя
            log = {"nickname" : entry_frames["LOGIN_NAME"].get()}
            write_json(filename = "user_info.json", obj_dict = log)
```

#### Функция создания заметок, + добавление их в поток: ####
```python
# Необходимый импорт для работы с потоками
import threading as thread

# Импорт модуля для показа уведомлений
import win10toast

# Импорт объекта от класса NoteDataBase, для управления методами
from ...data_base.requests_note_db import db_note

# Не обязательный импорт
import customtkinter as ctk
 
# Импорт для чтения json файлов
from ...jsn_func.read_json import read_json

# Импорт функции записии в Google Calendar, и создания service 
from ...google.create_google_note import write_event
from ...google.service_func import create_service

import asyncio

# Создаем объект от класса уведомлений
toast_notify = win10toast.ToastNotifier()

# Необходимые модули для работы со временем
import datetime
# Этот модуль так же нам позволяет приостановить программу
import time

async def notify(entry_frames: dict = ctk.CTkEntry, slider_hour: object = ctk.CTkSlider, slider_time: object = ctk.CTkSlider):
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

    def thread_notfy():
        asyncio.run(create_notify(index_day, slider_hour, slider_time, title, text))

    first_thread = thread.Thread(target = thread_notfy, daemon = True)
    # Запускаем поток
    first_thread.start()


async def create_notify(index_day: int, slider_hour: int, slider_time: int, title: str, text: str):
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

        json_data = read_json(filename = "user_info.json")

        # Добавляем запись в базу данных, когда событие создано
        await db_note.add_note(note_title = title, note_text = text, note_time_send = notify_time, nickname = json_data['nickname'])

        # Ждём указанное время
        time.sleep(time_difference)
        
        if text and title:
            # Показываем уведомление
            toast_notify.show_toast(title = title, msg = text, duration = 10)
            # Удаляем запись из базы данных, когда уведомление показано
            await db_note.delete_note(note_title = title, note_text = text, note_time_send = notify_time)
            # Выходим
            return 
        else:
            # Показываем ошибку
            toast_notify.show_toast(title = "Error", msg = "Error", duration = 5)
            # Удаляем запись из базы данных, когда уведомление показано
            await db_note.delete_note(note_title = title, note_text = text, note_time_send = notify_time)
            # Выходим
            return 

    # Перехватываем исключения и показываем ошибки
    except Exception as error:
        toast_notify.show_toast(title = "Error", msg = error, duration = 5)
        print(f'Произошла ошибка при создании события: {error}')
```

### Все представленные фрагменты кода составляют лишь десятую часть всего проекта — я решил выделить одни из самых важных ###

## Запуск
#### FOR WINDOWS 11 - 10:

- First we need to install Python, if you don't have it yet, watch this video if u have windows 11: [here](https://www.youtube.com/watch?v=C3bOxcILGu4&pp=ygUVaG90IHRvIGluc3RhbGwgcHl0aG9u)

- or windows 10: [here](https://www.youtube.com/watch?v=IPOr0ran2Oo&pp=ygUVaG90IHRvIGluc3RhbGwgcHl0aG9u)

- And Visual Studio code, here is the official site: [here](https://code.visualstudio.com)

- Once we have Python and VSC (Visual Studio Code) installed, we need to clone, like this

        > git clone https://github.com/Zixtherc/CTK-Reminder.git
        > cd CTK-Reminder 
        > python -m venv venv 
        > venv/Scripts/activate

after we saw the green VENV in the left corner we can write this

        > pip install -r requirements.txt

And to run program

        > python main.py

#### MacOs - Linux
- First we need to install Python, if you don't have it yet, watch this [video](https://www.youtube.com/watch?v=nhv82tvFfkM&pp=ygUcaG93IHRvIGluc3RhbGwgcHl0aG9uIG9uIG1hYw%3D%3D)

- And Visual Studio code, here is the official site: [here](https://code.visualstudio.com)

- Once we have Python and VSC (Visual Studio Code) installed, we need to clone, like this

        > git clone https://github.com/Zixtherc/CTK-Reminder.git
        > cd CTK-Reminder
        > python3 -m venv venv
        > Source venv/bin/activate

- after we saw the green VENV in the left corner we can write this

        > pip3 install -r requirements.txt

And to run program

        > python main.py

#### If you have any problems, you can contact me on Telegram. You can find my Telegram below

#### Контакты связи
- email - duckandfiretto@gmail.com
- telegram - @Z1xth3r
- phone(ua) - 0661152055
- discord - zixther
- instagram - zixther

## Итог
Возможно, вам покажется, что проект выглядит немного сыро или недоделанным, но так как это мой первый проект, созданный с целью поработать с ООП, я считаю, что выполнил поставленный план — возможно, даже перевыполнил, учитывая, какой функционал у него есть