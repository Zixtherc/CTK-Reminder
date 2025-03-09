# Не обязательный импорт
import customtkinter as ctk

# Обязательный импорт для вычесления размещения
import math

root = ctk.CTk()
root.geometry("400x400")

def circle_position(radius: int = 150,y_axis: int = 200, x_axis: int = 200):
    result_position = []
    # Перебираем по 12 раз, потому что в циферблате 12 часов
    for clock_face in range(12):
        # Вычисляем координаты точки на круге, множим на 30, потому что 12*30 = 360. 360 Это градусная мера круга
        angle = math.radians(clock_face * 30)
        # Вычисляем координаты, множим на косинус, потому что в декартовых координатах, в программировании, косинус управляет осью X
        x_cor = x_axis + radius * math.cos(angle)
        # Вычисляем координаты, множим на cинус, потому что в декартовых координатах, в программировании, cинус управляет осью Y
        y_cor = y_axis + radius * math.sin(angle)
        result_position.append((x_cor, y_cor))
    return result_position

