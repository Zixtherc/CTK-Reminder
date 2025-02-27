import customtkinter as ctk
from PIL import Image

class Label(ctk.CTkLabel):
    '''
    ### Класс который позволит нам создавать `Label` используя `наследование` ###
    '''
    def __init__(self, ch_master: object, ch_width: int, ch_height: int, ch_fg_color: str, 
                 ch_text: str, path_to_image: str = None, ch_corner_radius: int = 0, ch_font: str = None, ch_text_color: str = None,**kwargs):
        '''
        #### Метод `конструктор`, который принимает в себя параметры: ####

        - `ch_master:` `Объект` главного окна;
        - `ch_width:` Ширина `лейбла`;
        - `ch_height:` Высота `лейбла`;
        - `ch_fg_color:` Цвет фона `лейбла`;
        - `ch_text:` Текст `лейбла`;
        - `path_to_image:` Путь до изображения;
        '''
        # Создаём атрибут атрибут класса, который будет в себя вмещать путь до изображения
        self.path_to_image = path_to_image
        # Вызываем конструктор родительского класса (CTkLabel) и передаём в него необходимые аргументы
        ctk.CTkLabel.__init__(
            self,
            master = ch_master,
            width = ch_width,
            height = ch_height,
            fg_color = ch_fg_color,
            text = ch_text,
            corner_radius = ch_corner_radius,
            font = ch_font,
            text_color = ch_text_color,
            **kwargs)
        # Устанавливаем флаг, что размеры НЕ будут автоматически подстраиваться под размеры содержимого
        self.pack_propagate(False)
        self.grid_propagate(False)

    def load_image(self):
        '''
        `Метод` `загрузки` изображения
        '''
        try:
            if self.path_to_image:
                # Открываем изображение из файла и возвращаем его в нужном разрешении с помощью CTkImage из PIL.Image
                image = Image.open(fp = self.path_to_image)
                # Возвращаем картинку в нужном разрешении с помощью CTkImage из PIL.Image
                return ctk.CTkImage(
                    light_image = image
                )
        except Exception as e:
            print(f'Ошибка при загрузки изображения, ошибка : {e}')