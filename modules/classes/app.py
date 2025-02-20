import customtkinter as ctk
from ..jsn_func import read_json
from .frame import Frame
from .entry_frame import Entry_Text
from .button_frame import Button
from ..window_funcs.switch_frames import swith_frame
from ..auth_function import auth_function
from ..window_funcs import logged_user

class App(ctk.CTk):
    '''
    Основной `экран` нашего приложение, на `нём` мы будем `размещать` наши `Frame`  
    '''
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

        # Основной Frame, на который мы будем всё крепить 
        self.frames["HEADER"] = Frame(
            ch_masther = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = "#000000"
        )
        # Размещаем наш основной Frame, в нулевых координатах, т.к он будет занимать весь экран нашего приложения
        self.frames["HEADER"].place(x = 0, y = 0)

        # Создаём второй Frame, но не размещаем, т.к будем на него переключаться 
        self.frames["SECOND_HEADER"] = Frame(
            ch_masther = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = "#00008b"
        )
        self.entry["NAME"] = Entry_Text(
            ch_master = self.frames["HEADER"],
            ch_width = self.frames["HEADER"]._current_width * 0.2,
            ch_height = self.frames["HEADER"]._current_height * 0.05,
            ch_fg_color = "#ffffff",
            ch_corner_radius = 15,
            ch_border_width = 0.1,
            font_size = 13,
            ch_placeholder_text = "Enter your name")
        self.entry["NAME"].pack(pady = 20)

        self.entry["PASSWORD"] = Entry_Text(
            ch_master = self.frames["HEADER"],
            ch_width = self.frames["HEADER"]._current_width * 0.2,
            ch_height = self.frames["HEADER"]._current_height * 0.05,
            ch_fg_color = "#ffffff",
            ch_corner_radius = 15,
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

        # Создаём поле ввода ( пока не использую )
        self.entry["LOGIN_NAME"] = Entry_Text(
                ch_master = self.frames["SECOND_HEADER"],
                ch_width = self.frames["SECOND_HEADER"]._current_width * 0.2,
                ch_height = self.frames["SECOND_HEADER"]._current_height * 0.05,
                ch_fg_color = "#ffffff",
                ch_corner_radius = 15,
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
            ch_corner_radius = 15,
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
            ch_command = lambda: auth_function(auth_action = "login", entry_frames = self.entry, root = self)
            )
        self.CONFIRM_BUTTON_LOGIN.pack()

        # Создаём кнопку, которая будет переключать на второй Frame
        self.CONFIRM_BUTTON = Button(
            ch_master = self.frames["HEADER"],
            icon_name = "m_glass.png",
            text = "Register",
            ch_fg_color = "#1f1f1f",
            # Вызываем функцию через lambda, на сколько я помню, это нужно для того, что бы можно было передать параметры
            ch_command = lambda: auth_function(auth_action = "register", entry_frames = self.entry, root = self)
        )
        self.CONFIRM_BUTTON.place(x = 100, y = 100)

        self.LOGIN_BUTTON = Button(
            ch_master = self.frames["HEADER"],
            icon_name = "m_glass.png",
            text = "Login in",
            ch_fg_color = "#1f1f1f",
            # Вызываем функцию через lambda, на сколько я помню, это нужно для того, что бы можно было передать параметры
            ch_command = lambda: swith_frame(root = self, frame_name = 'SECOND_HEADER')
        )
        self.LOGIN_BUTTON.place(x = 100, y = 150)

app = App()