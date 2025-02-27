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
from .gradient_canvas import Gradient_Canvas

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
        self.create_header()
        self.create_second_header()
        self.main_content()
        self.calendar_days = {}

    def create_header(self):
        '''
        `Метод`, который позволит нам `объединить` `все` `объекты`, которые хранятся на Frame "HEADER". Нужно для `удобного` ориентирования 
        по коду
        '''
        # Основной Frame, на который мы будем всё крепить 
        self.frames["HEADER"] = Frame(
            ch_master = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = "#807880"
        )
        # Размещаем наш основной Frame, в нулевых координатах, т.к он будет занимать весь экран нашего приложения
        self.frames["HEADER"].place(x = 0, y = 0)
        
        self.label['TITLE'] = Label(
            ch_master = self.frames["HEADER"],
            ch_width = self.frames["HEADER"]._current_width * 0.3,
            ch_height = self.frames["HEADER"]._current_height * 0.2,
            ch_fg_color = None,
            ch_text = "NotifyX",
            ch_text_color = "#ffffff",
            ch_corner_radius = 6,
            ch_font = ctk.CTkFont(family = "Roboto", size = 50, weight = "bold")
        )
        self.label['TITLE'].pack()


        self.entry["NAME"] = Entry_Text(
            ch_master = self.frames["HEADER"],
            ch_width = self.frames["HEADER"]._current_width * 0.2,
            ch_height = self.frames["HEADER"]._current_height * 0.05,
            ch_fg_color = "#ffffff",
            ch_corner_radius = 6,
            ch_border_width = 0.1,
            font_size = 13,
            ch_placeholder_text = "Enter your name"
        )
        self.entry["NAME"].pack(pady = 20)

        self.entry["PASSWORD"] = Entry_Text(
            ch_master = self.frames["HEADER"],
            ch_width = self.frames["HEADER"]._current_width * 0.2,
            ch_height = self.frames["HEADER"]._current_height * 0.05,
            ch_fg_color = "#ffffff",
            ch_corner_radius = 6,
            ch_border_width = 0.1,
            font_size = 13,
            ch_placeholder_text = "Enter your password",
        )
        self.entry["PASSWORD"].pack(pady = 20)
        
        self.entry["EMAIL"] = Entry_Text(
            ch_master = self.frames["HEADER"],
            ch_width = self.frames["HEADER"]._current_width * 0.2,
            ch_height = self.frames["HEADER"]._current_height * 0.05,
            ch_fg_color = "#ffffff",
            ch_corner_radius = 15,
            ch_border_width = 0.1,
            font_size = 13,
            ch_placeholder_text = "Enter your email",
        )
        self.entry["EMAIL"].pack(pady = 20)

        # Создаём кнопку, которая будет переключать на второй Frame
        self.CONFIRM_BUTTON = Button(
            ch_master = self.frames["HEADER"],
            icon_name = "m_glass.png",
            text = "Register",
            ch_fg_color = "#1f1f1f",
            # Вызываем функцию через lambda, на сколько я помню, это нужно для того, что бы можно было передать параметры
            ch_command = lambda: asyncio.run(auth_function(auth_action="register", entry_frames=self.entry, root=self))
            )
        
        self.CONFIRM_BUTTON.place(x = 100, y = 100)

    def create_second_header(self):
        '''
        `Метод`, который позволит нам `объединить` `все` `объекты`, которые хранятся на Frame "SECOND_HEADER". Нужно для `удобного` ориентирования 
        по коду. Так же здесь находится кнопка авторизации
        '''
        # Создаём второй Frame, но не размещаем, т.к будем на него переключаться 
        self.frames["SECOND_HEADER"] = Frame(
            ch_master = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = "#807880"
        )
        
        self.label["LOG IN"] = Label(
            ch_master = self.frames["SECOND_HEADER"],
            ch_width = self.frames["SECOND_HEADER"]._current_width * 0.3,
            ch_height = self.frames["SECOND_HEADER"]._current_height * 0.2,
            ch_fg_color = None,
            ch_text = "Log In",
            ch_text_color = "#ffffff",
            ch_corner_radius = 6,
            ch_font = ctk.CTkFont(family = "Roboto", size = 50, weight = "bold")
        )
        self.label['LOG IN'].pack(pady = 50)

        self.LOGIN_BUTTON = Button(
            ch_master = self.frames["HEADER"],
            icon_name = "m_glass.png",
            text = "Login in",
            ch_fg_color = "#1f1f1f",
            # Вызываем функцию через lambda, на сколько я помню, это нужно для того, что бы можно было передать параметры
            ch_command = lambda: swith_frame(root = self, frame_name = 'SECOND_HEADER')
        )
        self.LOGIN_BUTTON.place(x = 100, y = 150)

        # Создаём поле ввода
        self.entry["LOGIN_NAME"] = Entry_Text(
                ch_master = self.frames["SECOND_HEADER"],
                ch_width = self.frames["SECOND_HEADER"]._current_width * 0.2,
                ch_height = self.frames["SECOND_HEADER"]._current_height * 0.05,
                ch_fg_color = "#ffffff",
                ch_corner_radius = 6,
                ch_border_width = 0.1,
                font_size = 13,
                ch_placeholder_text = "Enter your name",
        )
        # Размещаем по указанным координатам
        self.entry["LOGIN_NAME"].place(x = 300, y = 150)
        
        self.entry["LOGIN_PASSWORD"] = Entry_Text(
            ch_master = self.frames["SECOND_HEADER"],
            ch_width = self.frames["SECOND_HEADER"]._current_width * 0.2,
            ch_height = self.frames["SECOND_HEADER"]._current_height * 0.05,
            ch_fg_color = "#ffffff",
            ch_corner_radius = 6,
            ch_border_width = 0.1,
            font_size = 13,
            ch_placeholder_text = "Enter your password",
        )
        self.entry["LOGIN_PASSWORD"].place(x = 300, y = 50)

        self.CONFIRM_BUTTON_LOGIN = Button(
            ch_master = self.frames["SECOND_HEADER"],
            icon_name = "m_glass.png",
            text = "Login",
            ch_fg_color = "#1f1f1f",
            # Вызываем функцию через lambda, на сколько я помню, это нужно для того, что бы можно было передать параметры
            ch_command = lambda: asyncio.run(auth_function(auth_action = "login", entry_frames = self.entry, root = self))
            )
        self.CONFIRM_BUTTON_LOGIN.pack()

        
    def main_content(self):
        self.frames["MAIN_FRAME"] = Frame(
            ch_master = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = "#909090"
        )

        self.entry["TEXT_NOTE"] = Entry_Text(
            ch_master = self.frames['MAIN_FRAME'],
            ch_width = self.frames['MAIN_FRAME']._current_width * 0.2,
            ch_height = self.frames['MAIN_FRAME']._current_height * 0.05,
            ch_fg_color = "#ffffff",
            ch_corner_radius = 5,
            ch_border_width = 0.1,
            font_size = 12,
            ch_placeholder_text = "Write text"
            )

        self.entry["TITLE_NOTE"] = Entry_Text(
            ch_master = self.frames['MAIN_FRAME'],
            ch_width = self.frames['MAIN_FRAME']._current_width * 0.2,
            ch_height = self.frames['MAIN_FRAME']._current_height * 0.05,
            ch_fg_color = "#f0a2e1",
            ch_corner_radius = 5,
            ch_border_width = 0.1,
            font_size = 12,
            ch_placeholder_text = "Write title"
            )
        
        self.entry["DURATION_NOTE"] = Entry_Text(
            ch_master = self.frames['MAIN_FRAME'],
            ch_width = self.frames['MAIN_FRAME']._current_width * 0.2,
            ch_height = self.frames['MAIN_FRAME']._current_height * 0.05,
            ch_fg_color = "#ffffff",
            ch_corner_radius = 5,
            ch_border_width = 0.1,
            font_size = 12,
            ch_placeholder_text = "Choose date"
            )

        self.NOTIFICATION_BUTTON = Button(
            ch_master = self.frames['MAIN_FRAME'],  
            icon_name = "m_notification.png", # Нужно будет заменить 
            text = " ",
            ch_fg_color = "#805090",
            ch_hover_color = "#807090",
            size = 25,
            ch_corner_radius = 0,   
            ch_command = lambda: show_entry(self.entry)    
            )
        
        self.NOTIFICATION_BUTTON.pack(side = "bottom")
        create_calendar(parent = self.frames["MAIN_FRAME"], entry_frames = self.entry)

app = App()