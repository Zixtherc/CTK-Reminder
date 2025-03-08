# Необходимые импорты
from ..classes.button_frame import Button

# Импорт дочерних функций
from .calendars_func.calendars import get_count_days
from .calendars_func.create_note import create_notify
from .calendars_func.selected_button import select_button

# Не обязательный импорт
import customtkinter as ctk

def create_calendar(entry_frames: dict = {}, parent: object = ctk.CTk):
    '''
    `Функция`, которая `создаёт` такое количество `кнопок`, сколько `дней` в `месяце`
    '''
    count_days = get_count_days()
    all_buttons = []
    for day in range(count_days):
        
        button = Button(
            ch_master = parent,
            icon_name = None,
            text = str(day + 1),
            ch_fg_color = "#e874af",
            ch_hover_color = "#901873",
            size = 30,
            ch_corner_radius = 7,
            ch_command = lambda day = day + 1: ((create_notify(entry_frames = entry_frames, index_day = day), 
            select_button(index_button = day - 1, all_buttons = all_buttons))))
        all_buttons.append(button)  
        
        button.grid(row = day // 7, column = day % 7, padx = 5, pady = 5)