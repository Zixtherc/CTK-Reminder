# Необходимые импорты
from ..classes.button_frame import Button
# Импорт дочерних функций
from .calendars_func.calendars import get_count_days
from .calendars_func.create_note import notify_message
# Не обязательный импорт
import customtkinter as ctk

def create_calendar(entry_frames: dict = {}, parent: object = ctk.CTk):
    '''
    `Функция`, которая `создаёт` такое количество `кнопок`, сколько `дней` в `месяце`
    '''
    count_days = get_count_days()
    for day in range(count_days):
        button = Button(
            ch_master = parent,
            icon_name = None,
            text = str(day + 1),
            ch_fg_color = "#61004f",
            ch_hover_color = "#510740",
            size = 30,
            ch_corner_radius = 7,
            ch_command = lambda day = day + 1: notify_message(entry_frames = entry_frames, index_day = day)
            )
        button.grid(row = day // 7, column = day % 7, padx = 5, pady = 5)