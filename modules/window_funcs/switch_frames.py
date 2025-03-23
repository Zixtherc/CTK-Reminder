# Обязательный импорт для методов
from ..data_base.requests_note_db import db_note
# Не обязательный импорт
import customtkinter as ctk

# Обязательный импорт для чтения json файлов
from ..jsn_func.read_json import read_json

async def swith_frame(root: object = ctk.CTk, frame_name: str = ctk.CTkFrame):
    """
    Функция для переключения на другой фрейм.
    """
    # Перебираем все Frame которые мы получили 
    for frame in root.frames.values():
        # Скрываем каждый 
        frame.pack_forget()
        frame.place_forget()

    if frame_name == 'MAIN_FRAME' and frame_name in root.frames:
        data = read_json(filename = 'user_info.json')
        data = await db_note.get_all_notes(nickname = data['nickname'])
        print(f'Это дата: {data}')
        print(f'Это получилось')

    # Если указанный фрейм существует в словаре
    if frame_name in root.frames:
        # Переименовываем
        frame = root.frames[frame_name]
        # Размещаем ( relwidth  это ширина нашего фрейма, который будет "замещать" основной HEADER, и его будет не видно)
        frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    