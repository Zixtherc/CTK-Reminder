import customtkinter as ctk

class Slider(ctk.CTkSlider):
    '''
    ### Класс для создания слайдера ###
    '''
    def __init__(self, ch_master: object, ch_width: int, ch_height: int, ch_corner_radius: int,
                 ch_button_corner_radius: int, ch_border_color: str, ch_border_width: int, ch_bg_color: str, 
                 ch_fg_color: str, ch_progress_color: str, ch_button_hover_color: str, ch_button_color: str,
                 ch_from: int, ch_to: int, **kwargs):
        '''
        #### Метод `конструктор`, который принимает в себя параметры: ####'

        - `ch_master:` `Объект` главного окна;
        - `ch_width:` Ширина `слайдера`;
        - `ch_height:` Высота `слайдера`;
        - `ch_corner_radius:` Радиус закругления `слайдера`;
        - `ch_button_corner_radius:` Радиус закругления `кнопки`;
        - `ch_border_color:` Цвет границы `слайдера`;
        - `ch_border_width:` Толщина границы `слайдера`;
        - `ch_bg_color:` Цвет фона `слайдера`;
        - `ch_fg_color:` Цвет текста `полузнка` слайдера;
        - `ch_progress_color:` Цвет текста `прогресса` слайдера;
        - `ch_button_hover_color:` Цвет кнопки при наведении мыши;
        - `ch_button_color:` Цвет кнопки;
        - `ch_from:` Начальное значение слайдера;
        - `ch_to:` Конечное значение слайдера;

        Пример использования: 
        ```python
            slider = Slider(
            ch_master = self, 
            ch_width = 100,
            ch_height = 100, 
            ch_corner_radius = 2, 
            ch_button_corner_radius = 0, 
            ch_bg_color = "#000000', 
            ch_border_color = "#f3f", 
            ch_border_width = 1, 
            ch_bg_color = "#000000", 
            ch_fg_color = "#ffffff",
            ch_border_color = "#808080", 
            ch_button_color = "#000000", 
            ch_button_color = "#1e1", 
            ch_from = 0, 
            ch_to = 100
        )
        '''
        ctk.CTkSlider.__init__(  
            self,
            master = ch_master,
            width = ch_width,
            height = ch_height,
            corner_radius = ch_corner_radius,
            button_corner_radius = ch_button_corner_radius,
            border_color = ch_border_color,
            border_width = ch_border_width,
            bg_color = ch_bg_color,
            fg_color = ch_fg_color,
            progress_color = ch_progress_color,
            button_hover_color = ch_button_hover_color,
            button_color = ch_button_color,
            from_ = ch_from,
            to = ch_to,
            command = self.print_slider_progress, 
            **kwargs
        )

    def print_slider_progress(self):
        print(f"Slider progress: {self.get()}")