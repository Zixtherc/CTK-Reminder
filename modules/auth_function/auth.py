'''
    Этот модуль содержит функцию авторизации пользователя
'''
# Необходимый импорт для управления базой данных 
from ..data_base import db
# Необходимый импорт для работы с JSON
from ..jsn_func import write_json
# Необходимый импорт функции
from ..window_funcs import logged_user
# Необязательный импорт
import customtkinter as ctk

from ..classes.top_level import TopLevelWidget

async def auth_function(auth_action: str = None, entry_frames: dict = None, root: ctk.CTk = None):
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
        print(entry_frames["NAME"].get(),entry_frames["PASSWORD"].get(),entry_frames["EMAIL"].get())
        print(f'================================================================')
        # Вызываем метод базы данных, и записываем в переменную flag_register ответ от базы данных
        # Метод get() позволяет нам взять текст с фреймов Entry 
        if not all([entry_frames["NAME"].get().strip(), entry_frames["PASSWORD"].get().strip(), entry_frames["EMAIL"].get().strip()]):
            print(f'УРАААААААААААААААААААААААААААААААААААА')
            TopLevelWidget(ch_master = root, ch_width = 700, ch_height = 500, ch_fg_color = "#808080", label_text = "Error")
            return
        flag_register = await db.insert_user(
            name = entry_frames["NAME"].get(),
            password = entry_frames["PASSWORD"].get(),
            email = entry_frames["EMAIL"].get())
        print(entry_frames["NAME"].get(),entry_frames["PASSWORD"].get(),entry_frames["EMAIL"].get())
        # Если флаг True (Пользователь успешно зарегистрировался), если False, вероятнее всего произошла ошибка 
        if flag_register:
            # Записываем в JSON файл информацию о том, что пользователь зарегистрировался
            log = {"user_status" : "registered"}
            write_json(filename = "utility.json", obj_dict = log)
            # Если пользователь успешно зарегистрировался, переводим его на главную страницу
            logged_user(root = root)

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
            logged_user(root = root)