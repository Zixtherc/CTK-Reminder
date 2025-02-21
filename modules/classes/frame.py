import customtkinter as ctk 

class Frame(ctk.CTkFrame):
    '''
    ### Класс который позволит нам создавать `Frames` используя `наследование` ###
    '''
    def __init__(self, ch_master: object, ch_width: int, ch_height: int, ch_fg_color: str, **kwargs):
        '''
        #### Метод `конструктор`, который принимает в себя параметры: ####

        - `ch_master:` `Объект` главного окна;
        - `ch_width:` Ширина `фрейма`;
        - `ch_height:` Высота `фрейма`;
        - `ch_fg_color:` Цвет фона `фрейма`;

        Пример использования: 
        ```python
        self.frames["SECOND_HEADER"] = Frame(ch_master=self, ch_width=self.WIDTH, ch_height=self.HEIGHT, ch_fg_color="#00008b")
        ```
        '''
        # Вызываем конструктор родительского класса (CTkFrame) и передаём в него необходимые аргументы
        ctk.CTkFrame.__init__(
            self,
            master = ch_master,
            width = ch_width,
            height = ch_height,
            fg_color = ch_fg_color,
            corner_radius = 0,
            **kwargs)
        # Устанавливаем флаг, что размеры НЕ будут автоматически подстраиваться под размеры содержимого
        self.pack_propagate(False)
        self.grid_propagate(False)