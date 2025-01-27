import PIL.Image
import customtkinter as ctk
import PIL
from os.path import join, abspath
class Button(ctk.CTkButton):
    def __init__(self, ch_master: object, icon_name: str,  text: str, ch_fg_color: str,
                ch_hover_color: str = '#373535', size: float = 20,
                ch_corner_radius: int = 10, ch_command : object = None,
                **kwargs):
        self.ICON_NAME = icon_name
        self.SIZE = (int(size), int(size))
        self.TEXT = text

        ctk.CTkButton.__init__(
            self,
            master = ch_master,
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
        try:
            PATH = abspath(join(__file__, '..',  '..', '..', "static", "icons", self.ICON_NAME))
            return ctk.CTkImage(
                light_image = PIL.Image.open(fp = PATH),
                size = self.SIZE
            )
        except Exception as error:
            print(f'Ошибка при загрузки фото, название ошибки{error}')
            return None
        