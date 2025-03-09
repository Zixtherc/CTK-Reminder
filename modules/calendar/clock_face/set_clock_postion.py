# Не обязательный импорт
import customtkinter as ctk

# Обязательный импорт для вычесления размещения
import math

def circle_position(radius: int = 150, y_axis: int = 200, x_axis: int = 200):
    '''
    ### `Функция`, которая `возвращает координаты`, где надо расположить `объектя`, что бы он был в форме `круга` ###

    ### Параметры: ###
    - `radius` (int): Радиус круга, проще говоря `расстояние` от `противоположных` кнопок,
        к примеру кнопка 12 часов, будет распологаться на 2 радиуса от кнопки на 6 часов;
    - `y_axis` (int): `Координата` ось Y центра круга, ставим на 200, и более, т.к в противном случае кнопки `будут уходить` за экран;
    - `x_axis` (int): `Координата` ось X центра круга, ставим на 200, и более, т.к в противном случае кнопки `будут уходит`ь за экран;

    ### Пример использования: ###
        ```python 
        coords = circle_position(radius = 300, y_axis = 300, x_axis = 300)

        for index in range(12):
            button = ctk.CTkButton(ch_master = self, etc.)
            button.place(x = coords[index][0], y = coords[index][1])
    '''
    # Список для хранения координат кнопок, которые будут расположены вокруг круга.
    result_position = []

    # Перебираем по 12 раз, потому что в циферблате 12 часов
    for clock_face in range(12):

        # Вычисляем координаты точки на круге, множим на 30, потому что 12*30 = 360. 360 Это градусная мера круга
        angle = math.radians(clock_face * 30)
        # Вычисляем координаты, множим на косинус, потому что в декартовых координатах, в программировании, косинус управляет осью X
        x_cor = x_axis + radius * math.cos(angle)
        # Вычисляем координаты, множим на cинус, потому что в декартовых координатах, в программировании, cинус управляет осью Y
        y_cor = y_axis + radius * math.sin(angle)

        # Добавляем координаты в список, которые потом будут использоваться для расположения кнопок на экране
        result_position.append((x_cor, y_cor))
        
    # Возвращаем список координат, где каждый кортеж - это координаты одной из 12 кнопок
    return result_position