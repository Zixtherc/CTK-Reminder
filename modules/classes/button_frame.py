'''
    `Модуль`, который вмещает в себя класс `Button`
'''
# Необходимый модуль для работы с изображением
import PIL.Image
# Необходимый модуль для работы GUI
import customtkinter as ctk
# Необходимый модуль для построение путей
from os.path import join, abspath


class Button(ctk.CTkButton):
    '''
    Класс который позволит нам создавать `Button` используя `наследование`
    '''
    def __init__(self, ch_master: object, icon_name: str,  text: str, ch_fg_color: str,
                ch_hover_color: str = '#373535', size: float = 20,
                ch_corner_radius: int = 10, ch_command : object = None,
                **kwargs):
        '''
        Метод `конструктор` который принимает в себя параметры: 

        - `ch_master`: Объект главного окна;
        - `icon_name`: Название файла из папки `static/icons/` для иконки;
        - `text`: Текст на кнопке;
        - `ch_fg_color`: Цвет самой `кнопки`;
        - `ch_hover_color`: Цвет `кнопки` при `наведении мыши`;
        - `size`: Размер `кнопки`;
        - `ch_corner_radius`: Радиус `скругления` углов `кнопки`;
        - `ch_command`: Команда, которая будет выполняться `при нажатии` на `кнопку`;
        - `kwargs`: Дополнительные параметры для `кнопки` (например, `font`, `border_width`, `padding`)

        Пример использования:
        ```python 
        button = Button(self.frames["HEADER"], "logout.png", "Выйти", "#ffffff", "#373535", 25, 10, command=self.logout)
        ```
        '''
        # Создаём атрибуты класса

        # Атрибут, который отвечает за название иконки
        self.ICON_NAME = icon_name
        # Атрибут, который отвечает за размер, выглядит в виде tuple (кортеж, т.к параметр size, в ctk.CtkImage принимает исключительно tuple)
        self.SIZE = (int(size), int(size))
        # Атрибут, который отвечает за текст кнопки
        self.TEXT = text

        # Вызываем конструктор родительского класса (CTkButton) и передаём в него необходимые аргументы
        ctk.CTkButton.__init__(
            self,
            master = ch_master,
            # В параметр image передаём наш метод, он возвращает нужное нам разрешение
            image = self.load_image(),
            text = self.TEXT,
            width = int(size),
            height = int(size),
            fg_color = ch_fg_color,
            hover_color = ch_hover_color,
            corner_radius = ch_corner_radius,
            command = ch_command,
            **kwargs)
        
    def load_image(self):
        '''
        `Метод`, который загружает иконку из файла
        '''
        # Используем try except для безопасной работы кода
        try:
            # Получаем путь к иконке из папки static/icons/
            PATH = abspath(join(__file__, '..',  '..', '..', "static", "icons", self.ICON_NAME))
            # Возвращаем картинку в нужном разрешении с помощью CTkImage из PIL.Image
            return ctk.CTkImage(
                light_image = PIL.Image.open(fp = PATH),
                size = self.SIZE
            )
        # Выводим сообщение об ошибке и возвращаем None в случае ошибки, если не возвращать None будет ошибка 
        except Exception as error:
            print(f'Ошибка при загрузки фото, название ошибки{error}')
            return None