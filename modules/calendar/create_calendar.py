from ..classes.button_frame import Button
import customtkinter as ctk

def create_calendar(parent: object = ctk.CTk, count_days: int = 30):
    for day in range(count_days):
        button = Button(
            ch_master = parent,
            icon_name = None,
            text = str(day + 1),
            ch_fg_color = "#505050",
            ch_hover_color = "#3d3d3d",
            size = 30,
            ch_corner_radius = 7
            )
        button.grid(row=day // 7, column=day % 7, padx=5, pady=5)