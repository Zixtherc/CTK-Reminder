from ..classes.button_frame import Button
from .calendars_func.calendars import get_count_days
from .calendars_func.create_note import notify_message
import customtkinter as ctk

def create_calendar(parent: object = ctk.CTk):
    count_days = get_count_days()
    for day in range(count_days):
        button = Button(
            ch_master = parent,
            icon_name = None,
            text = str(day + 1),
            ch_fg_color = "#505050",
            ch_hover_color = "#ad3d3d",
            size = 30,
            ch_corner_radius = 7,
            ch_command = lambda: notify_message() # В аргументы пока ничего не передаём 
            )
        button.grid(row=day // 7, column=day % 7, padx=5, pady=5)