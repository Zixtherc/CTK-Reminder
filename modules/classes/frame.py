# Обязательный импорт для отображения количества заметок 
from .label import Label

# Обязательный импорт
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

        

    def update_notes(self, count_notes: int, frame_position: str, note_data):
        '''
        `Метод` `обновления` заметок

        Принимает в себя параметры:
        - `count_notes:` Количество заметок;
        - `frame_position:` Местоположение `фрейма`;
        - `note_data:` Данные заметок;

        Пример использования:
        ```python
        frame.update_notes(count_notes = count_notes, frame_position = frame, note_data = data) 
        ```
        '''
        for index in range(count_notes):
            self.label_no_notes = Label(
                ch_master = frame_position, 
                ch_width = 170,
                ch_height = 70,
                ch_fg_color = "#808080",
                ch_text = f'Title:{note_data[index][1]}\nText:{note_data[index][2]}\nDate:{note_data[index][-1]}\n',
                ch_corner_radius = 5
            )
            self.label_no_notes.grid(row = index, column = 0, padx = 5, pady = 5)