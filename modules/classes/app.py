'''
`Основной` модуль, нашего приложения, вмещает в себя класс `App`, который является нашим приложением
'''
# Необходимый импорт 
import customtkinter as ctk

# Не обязательный импорт *
from ..jsn_func import read_json

# Импорты классов для работы :
from .entry_frame import Entry_Text
from .button_frame import Button
from .frame import Frame
from .label import Label

# Импорт функции, для смены фреймов
from ..window_funcs.switch_frames import swith_frame

# Импорты функции для авторизации/регистрации
from ..auth_function import auth_function

# Импорты для работы с календарем и его функциями
from ..calendar.create_calendar import create_calendar
from ..calendar.calendars_func import show_entry

# Необходимый импорт для работы с асинхронностью
import asyncio

# Класс приложения
class App(ctk.CTk):
    '''
    
    ### Основной `экран` нашего приложение, на `нём` мы будем `размещать` наши `Frame` ###
    '''
    # В будущем буду использовать ctk.set_appearance_mode("light")
    def __init__(self):
        data = read_json("config.json")
        ctk.CTk.__init__(self, fg_color = data["fg_color"])

        self.WIDTH = int(self.winfo_screenwidth() * data['width'])

        self.HEIGHT = int(self.winfo_screenheight() * data['height'])

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.title("Your Reminder!")
        self.resizable(False, False)
        
        # Список всех наших Frame
        self.frames = {}
        self.entry = {}
        self.label = {}
        self.welcome_header()
        self.register_header()
        self.login_header()
        self.main_content()
        self.create_note_header()
        self.settings_header()

    def welcome_header(self):
        
        self.frames["WELCOME_HEADER"] = Frame(
            ch_master = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = "#1d1d1d"
        )
        self.frames["WELCOME_HEADER"].place(x = 0, y = 0)

        self.label['TITLE'] = Label(
            ch_master = self.frames["WELCOME_HEADER"],
            ch_width = self.frames["WELCOME_HEADER"]._current_width * 0.3,
            ch_height = self.frames["WELCOME_HEADER"]._current_height * 0.2,
            ch_fg_color = None,
            ch_text = "NotifyX",
            ch_text_color = "#ff41a6",
            ch_corner_radius = 6,
            ch_font = ctk.CTkFont(family = "Roboto", size = 50, weight = "bold")
        )
        self.label['TITLE'].pack()

        self.label['CONTENT'] = Label(
            ch_master = self.frames["WELCOME_HEADER"],
            ch_width = self.frames["WELCOME_HEADER"]._current_width * 1,
            ch_height = self.frames["WELCOME_HEADER"]._current_height * 0.1,
            ch_fg_color = None,
            ch_text = "Create reminders, get notifications, and add them to Google Calendar with one check",
            ch_text_color = "#ff41a6",
            ch_corner_radius = 6,
            ch_font = ctk.CTkFont(family = "Roboto", size = 15, weight = "bold")
        )
        self.label['CONTENT'].pack()

        self.REGISTER_BUTTON = Button(
            ch_master = self.frames["WELCOME_HEADER"],
            icon_name = "m_glass.png",
            text = "Register",
            ch_fg_color = "#61004f",
            size = 35,
            # Вызываем функцию через lambda, на сколько я помню, это нужно для того, что бы можно было передать параметры
            ch_command = lambda: swith_frame(root = self, frame_name = 'REGISTER_HEADER')
        )
        self.REGISTER_BUTTON.place(x = 200, y = 250)

        self.LOGIN_BUTTON = Button(
            ch_master = self.frames["WELCOME_HEADER"],
            icon_name = "m_glass.png",
            text = "Login",
            ch_fg_color = "#61004f",
            size = 35,
            # Вызываем функцию через lambda, на сколько я помню, это нужно для того, что бы можно было передать параметры
            ch_command = lambda: swith_frame(root = self, frame_name = "LOGIN_HEADER")
        )
        self.LOGIN_BUTTON.place(x = 500, y = 250)

    def register_header(self):
        '''
        `Метод`, который позволит нам `объединить` `все` `объекты`, которые хранятся на Frame "REGISTER_HEADER". Нужно для `удобного` ориентирования 
        по коду
        '''
        # Основной Frame, на который мы будем всё крепить 
        self.frames["REGISTER_HEADER"] = Frame(
            ch_master = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = "#1d1d1d"
        )

        self.label['WELCOME_BACK'] = Label(
            ch_master = self.frames["REGISTER_HEADER"],
            ch_width = self.frames["REGISTER_HEADER"]._current_width * 0.5,
            ch_height = self.frames["REGISTER_HEADER"]._current_height * 0.2,
            ch_fg_color = None,
            ch_text = " Hello, what are you planning ?",
            ch_text_color = "#ff41a6",
            ch_corner_radius = 6,
            ch_font = ctk.CTkFont(family = "Roboto", size = 25, weight = "bold")
        )
        self.label['WELCOME_BACK'].pack()

        self.entry["NAME"] = Entry_Text(
            ch_master = self.frames["REGISTER_HEADER"],
            ch_width = self.frames["REGISTER_HEADER"]._current_width * 0.2,
            ch_height = self.frames["REGISTER_HEADER"]._current_height * 0.05,
            ch_fg_color = "#ff41a6",
            ch_corner_radius = 6,
            ch_border_width = 0.1,
            font_size = 13,
            ch_placeholder_text = "Enter your name"
        )
        self.entry["NAME"].pack(pady = 20)

        self.entry["PASSWORD"] = Entry_Text(
            ch_master = self.frames["REGISTER_HEADER"],
            ch_width = self.frames["REGISTER_HEADER"]._current_width * 0.2,
            ch_height = self.frames["REGISTER_HEADER"]._current_height * 0.05,
            ch_fg_color = "#ff41a6",
            ch_corner_radius = 6,
            ch_border_width = 0.1,
            font_size = 13,
            ch_placeholder_text = "Enter your password",
        )
        self.entry["PASSWORD"].pack(pady = 20)
        
        self.entry["EMAIL"] = Entry_Text(
            ch_master = self.frames["REGISTER_HEADER"],
            ch_width = self.frames["REGISTER_HEADER"]._current_width * 0.2,
            ch_height = self.frames["REGISTER_HEADER"]._current_height * 0.05,
            ch_fg_color = "#ff41a6",
            ch_corner_radius = 15,
            ch_border_width = 0.1,
            font_size = 13,
            ch_placeholder_text = "Enter your email",
        )
        self.entry["EMAIL"].pack(pady = 20)

        self.CONFIRM_BUTTON = Button(
            ch_master = self.frames["REGISTER_HEADER"],
            icon_name = "m_glass.png",
            text = "Register",
            ch_fg_color = "#61004f",
            size = 50,
            # Вызываем функцию через lambda, на сколько я помню, это нужно для того, что бы можно было передать параметры
            ch_command = lambda: asyncio.run(auth_function(auth_action = "register", entry_frames = self.entry, root = self))
        )
        self.CONFIRM_BUTTON.pack(pady = 30)

    def login_header(self):
        '''
        `Метод`, который позволит нам `объединить` `все` `объекты`, которые хранятся на Frame "LOGIN_HEADER". Нужно для `удобного` ориентирования 
        по коду. Так же здесь находится кнопка авторизации
        '''
        # Создаём второй Frame, но не размещаем, т.к будем на него переключаться 
        self.frames["LOGIN_HEADER"] = Frame(
            ch_master = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = "#1d1d1d"
        )
        
        self.label["LOG IN"] = Label(
            ch_master = self.frames["LOGIN_HEADER"],
            ch_width = self.frames["LOGIN_HEADER"]._current_width * 0.5,
            ch_height = self.frames["LOGIN_HEADER"]._current_height * 0.2,
            ch_fg_color = None,
            ch_text = "Welcome back to NotifyX",
            ch_text_color = "#ff41a6",
            ch_corner_radius = 6,
            ch_font = ctk.CTkFont(family = "Roboto", size = 30, weight = "bold")
        )
        self.label['LOG IN'].pack(pady = 50)

        # Создаём поле ввода
        self.entry["LOGIN_NAME"] = Entry_Text(
                ch_master = self.frames["LOGIN_HEADER"],
                ch_width = self.frames["LOGIN_HEADER"]._current_width * 0.2,
                ch_height = self.frames["LOGIN_HEADER"]._current_height * 0.05,
                ch_fg_color = "#ff41a6",
                ch_corner_radius = 6,
                ch_border_width = 0.1,
                font_size = 13,
                ch_placeholder_text = "Enter your name",
        )
        # Размещаем по указанным координатам
        self.entry["LOGIN_NAME"].place(x = 300, y = 150)
        
        self.entry["LOGIN_PASSWORD"] = Entry_Text(
            ch_master = self.frames["LOGIN_HEADER"],
            ch_width = self.frames["LOGIN_HEADER"]._current_width * 0.2,
            ch_height = self.frames["LOGIN_HEADER"]._current_height * 0.05,
            ch_fg_color = "#ff41a6",
            ch_corner_radius = 6,
            ch_border_width = 0.1,
            font_size = 13,
            ch_placeholder_text = "Enter your password",
        )
        self.entry["LOGIN_PASSWORD"].place(x = 300, y = 50)

        self.CONFIRM_BUTTON_LOGIN = Button(
            ch_master = self.frames["LOGIN_HEADER"],
            icon_name = "m_glass.png",
            text = "Login",
            ch_fg_color = "#61004f",
            # Вызываем функцию через lambda, на сколько я помню, это нужно для того, что бы можно было передать параметры
            ch_command = lambda: asyncio.run(auth_function(auth_action = "login", entry_frames = self.entry, root = self))
            )
        self.CONFIRM_BUTTON_LOGIN.pack()

    def main_content(self):

        self.frames["MAIN_FRAME"] = Frame(
            ch_master = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = "#1d1d1d"
        )
        create_calendar(parent = self.frames["MAIN_FRAME"], entry_frames = self.entry)

        self.SETTINGS_BUTTON = Button(
            ch_master = self.frames["MAIN_FRAME"],
            icon_name = "dots_setting.png",
            text = "Settings Button",
            ch_fg_color = "#61004f",
            ch_command = lambda: swith_frame(root = self, frame_name = "SETTINGS_HEADER")
            )
        self.SETTINGS_BUTTON.pack(pady = 10)

        self.TIME_LINE_NOTES_BUTTON = Button(
            ch_master = self.frames["MAIN_FRAME"],
            icon_name = "dots_setting.png",
            text = "Login",
            ch_fg_color = "#61004f",
            ch_command = lambda: None # Пока ниче не передаём
            )
        self.TIME_LINE_NOTES_BUTTON.pack(pady = 10)
        
        self.ADD_NOTE_BUTTON = Button(
            ch_master = self.frames["MAIN_FRAME"],
            icon_name = "white_plus.png",
            text = " ",
            ch_hover_color = "#1d1d1d",
            ch_fg_color = "transparent",
            ch_command = lambda: swith_frame(root = self, frame_name = "CREATE_NOTE_HEADER")
        )
        self.ADD_NOTE_BUTTON.pack(pady = 10)
    
    def create_note_header(self):

        self.frames["CREATE_NOTE_HEADER"] = Frame(
            ch_master = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = "#1d1d1d"
        ) 

        self.entry["TITLE_NOTE"] = Entry_Text(
            ch_master = self.frames["CREATE_NOTE_HEADER"],
            ch_width = self.frames["CREATE_NOTE_HEADER"]._current_width * 0.7,
            ch_height = self.frames["CREATE_NOTE_HEADER"]._current_height * 0.05,
            ch_fg_color = "#ff41a6",
            ch_corner_radius = 6,
            ch_border_width = 0.1,
            font_size = 13,
            ch_placeholder_text = "Enter your title"
        )
        self.entry["TITLE_NOTE"].pack(pady = 20)

        self.entry["TEXT_NOTE"] = Entry_Text(
            ch_master = self.frames["CREATE_NOTE_HEADER"],
            ch_width = self.frames["CREATE_NOTE_HEADER"]._current_width * 0.7,
            ch_height = self.frames["CREATE_NOTE_HEADER"]._current_height * 0.5,
            ch_fg_color = "#ff41a6",
            ch_corner_radius = 6,
            ch_border_width = 0.1,
            font_size = 13,
            ch_placeholder_text = "Enter your note text"
        )
        self.entry["TEXT_NOTE"].pack(pady = 20)

        self.SAVE_NOTE_BUTTON = Button(
            ch_master = self.frames["CREATE_NOTE_HEADER"],
            icon_name = " ",
            text = "Save",
            ch_fg_color = "#61004f",
            ch_command = lambda: None # Пока ничего не добавляем
        )
        self.SAVE_NOTE_BUTTON.pack(pady = 20)

    def settings_header(self):

        self.frames["SETTINGS_HEADER"] = Frame(
            ch_master = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = "#1d1d1d"
        )
        
        self.label['NOTIFICATION_SETTINGS'] = Label(
            ch_master = self.frames["SETTINGS_HEADER"],
            ch_width = self.frames["SETTINGS_HEADER"]._current_width * 0.5,
            ch_height = self.frames["SETTINGS_HEADER"]._current_height * 0.2,
            ch_fg_color = None,
            ch_text = "Nofication settings",
            ch_text_color = "#ff41a6",
            ch_corner_radius = 6,
            ch_font = ctk.CTkFont(family = "Roboto", size = 30, weight = "bold")
        )
        self.label['NOTIFICATION_SETTINGS'].pack(pady = 20)

        self.label['EXTRAS_SETTINGS'] = Label(
            ch_master = self.frames["SETTINGS_HEADER"],
            ch_width = self.frames["SETTINGS_HEADER"]._current_width * 0.5,
            ch_height = self.frames["SETTINGS_HEADER"]._current_height * 0.2,
            ch_fg_color = None,
            ch_text = "Extras",
            ch_text_color = "#ff41a6",
            ch_corner_radius = 6,
            ch_font = ctk.CTkFont(family = "Roboto", size = 30, weight = "bold")
        )
        self.label['EXTRAS_SETTINGS'].pack(pady = 50)

        self.HELP_BUTTON = Button(
            ch_master = self.frames["SETTINGS_HEADER"],
            icon_name = "    ",
            text = " Help ",
            size = 50,
            ch_hover_color = "#1d1d1d",
            ch_fg_color = "transparent",
            ch_command = lambda: swith_frame(root = self, frame_name = "HELP_HEADER")
        )
        self.HELP_BUTTON.pack(pady = 10)

        self.ABOUT_BUTTON = Button(
            ch_master = self.frames["SETTINGS_HEADER"],
            icon_name = "    ",
            text = " About us ",
            size = 50,
            ch_hover_color = "#1d1d1d",
            ch_fg_color = "transparent",
            ch_command = lambda: None # Пока ничего не передаём, в будущем тут должна быть анимация
        )
        self.ABOUT_BUTTON.pack(pady = 10)
        
app = App()