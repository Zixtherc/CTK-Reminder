# Необходимые импорты
from ...classes.button_frame import Button

# Импорт дочерней функции
from ..calendars_func.selected_button import select_button
from .set_clock_postion import circle_position

# Не обязательный импорт
import customtkinter as ctk

def create_clock(entry_frames: dict = {}, parent: object = ctk.CTk):
    '''
    `Функция`, которая `создаёт` циферблат из `кнопок`
    '''
    all_buttons = []
    circle_cords = circle_position(radius = 75, x_axis = 100, y_axis = 100)
    for hour in range(0, 12):
        
        button = Button(
            ch_master = parent,
            icon_name = None,
            text = str(hour + 1),
            ch_fg_color = "#43F2A5",
            ch_hover_color = "#22B85A",
            size = 21,
            ch_corner_radius = 20,
            ch_command = lambda: select_button(index_button = hour, all_buttons = all_buttons)
        )
        all_buttons.append(button)

        button.place(x = circle_cords[hour][0], y = circle_cords[hour][1])