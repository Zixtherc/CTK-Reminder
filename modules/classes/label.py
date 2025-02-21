import customtkinter as ctk
from PIL import Image

class Label(ctk.CTkLabel):
    '''
    Класс который позволит нам создавать `Label` используя `наследование`
    '''
    def __init__(self, ch_master: object, ch_width: int, ch_height: int, ch_fg_color: str, ch_text: str, path_to_image: str, **kwargs):
        self.path_to_image = path_to_image
        ctk.CTkLabel.__init__(
            self,
            master = ch_master,
            width = ch_width,
            height = ch_height,
            fg_color = ch_fg_color,
            text = ch_text,
            **kwargs)
        self.pack_propagate(False)
        self.grid_propagate(False)
    def load_image(self):
        try:
            image = Image.open(fp = self.path_to_image)
            return ctk.CTkImage(
                light_image = image
            )
        except Exception as e:
            print(f'Ошибка при загрузки изображения, ошибка : {e}')