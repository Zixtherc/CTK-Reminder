import customtkinter as ctk
import PIL.Image, PIL.ImageDraw

def generate_gradient(width:int, height:int, first_color: str, second_color: str):
    gradient = PIL.Image.new("RGB", (width, height), first_color)
    draw_gradient = PIL.ImageDraw.Draw()
    for y_cor in range(height):
        ratio = y_cor / height
        red_one , green_one , blue_one = ctk.CTkImage()
    return None