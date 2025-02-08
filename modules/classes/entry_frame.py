import customtkinter as ctk
import time
from ..data_base.requests_bd import db

class Entry_Text(ctk.CTkEntry):
    '''
    Класс который позволит нам создавать поле ввода текста
    '''
    def __init__(self, ch_master: object, ch_width: int, ch_height: int, ch_fg_color: str,
                ch_corner_radius: int, ch_border_width: int, ch_placeholder_text: str, 
                font_size: int, font_name: str = "Arial", ch_placeholder_text_color : str = "#000000",ch_text_color : str = "#000000",**kwargs):
        ctk.CTkEntry.__init__(
            self,
            master = ch_master,
            width = ch_width,
            height = ch_height,
            fg_color = ch_fg_color,
            corner_radius = ch_corner_radius,
            border_width = ch_border_width,
            placeholder_text = ch_placeholder_text,
            font=(font_name, font_size, "bold"),
            placeholder_text_color = ch_placeholder_text_color,
            text_color = ch_text_color,
            **kwargs)
        
        self.base_width = ch_width
        # self.bind("<Return>",  self.add_user_db)
        self.button_pressed_flag = False
        self.new_width = 0

    def adjust_text(self, event = None) ->  None:
        ''' Изменяет `ширину` `ввода` текста, если `пользователь` `начал` вводить текст'''
        time.sleep(0.1)
        text_length = len(self.get())
        text = self.get()
        self.new_width = max(self.base_width, text_length * 7.5)
        self.configure(width = self.new_width)
        return text 
    
    # def add_user_db(self, name: str, password: str = "123", email: str = "12223", event=None) -> None:
        # name = self.get()
        # password = self.master.PASSWORD.get()        
        # email = self.master.EMAIL.get()
        # # db.insert_user(name=name, password=password, email=email)
        # print(f'Пользователь с никнеймом: {name}, добавлен')
        # print(f'Пользователь с паролем: {password}, добавлен')
        # print(f'Пользователь с email: {email}, добавлен')