# Необходимые импорты
from ..classes.button_frame import Button

# Импорт дочерних функций
from .calendars_func.calendars import get_count_days
from .calendars_func.selected_button import select_button
from ..window_funcs.switch_frames import swith_frame
from ..window_funcs.animation import animation

# Импорты для записи в json файлы
from ..jsn_func.write_json import write_json

# Не обязательный импорт
import customtkinter as ctk

# Импорт для работы с ассинхроностью
import asyncio

def create_calendar(frames_dict: object = ctk.CTkFrame, root: object = ctk.CTk):
    '''
    #### `Функция`, которая `создаёт` такое количество `кнопок`, сколько `дней` в `месяце` ####
    Параметры:
    - `frames_dict:` Словарь со всеми Frame;
    - `root:` Объект главного окна;

    '''
    # Получаем количество дней в текущем месяце
    count_days = get_count_days()
    # Создаём массив для всех кнопок
    all_buttons = []

    # Создаём цикл for, и создаём такое количество кнопок, сколько дней в месяце
    for day in range(count_days):
        
        # Создаём кнопку с текущим номером и днём
        button = Button(
            ch_master = frames_dict['MAIN_FRAME'],
            icon_name = None,
            text = str(day + 1),
            ch_fg_color = "#e874af",
            ch_hover_color = "#901873",
            size = 30,
            ch_corner_radius = 7,
            ch_command = lambda day = day + 1: ((animation(shift_distance = 30, animated_obj = button, canvas = ctk.CTkCanvas )), # lambda day + 1 т.к нумерация начинается с 0
            # asyncio.run(swith_frame(root = root, frame_name = 'CREATE_NOTE_HEADER'))), # Меняем фрейм
            write_json(filename = "utility.json", obj_dict = day))) # Записываем в json файл
        all_buttons.append(button) # Добавляем кнопку в массив
        # Размещаем кнопку на фрейме
        button.grid(row = day // 7, column = day % 7, padx = 5, pady = 5)