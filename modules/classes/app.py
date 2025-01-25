import customtkinter as ctk
from ..jsn_func import read_json
from .frame import Frame
from .entry_frame import Entry_Text
from .button_frame import Button
class App(ctk.CTk):
    '''
    Основной `экран` нашего приложение, на `нём` мы будем `размещать` наши `Frame`  
    '''
    def __init__(self):
        data = read_json("config.json")
        ctk.CTk.__init__(self, fg_color = data["fg_color"])

        self.WIDTH = int(self.winfo_screenwidth() * data['width'])

        self.HEIGHT = int(self.winfo_screenheight() * data['height'])

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.title("Hello World!")
        self.resizable(False, False)

        # Основной Frame, на который мы будем всё крепить 
        self.HEADER = Frame(
            ch_masther = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = "#000000"
        )
        # Размещаем наш основной Frame, в нулевых координатах, т.к он будет занимать весь экран нашего приложения
        self.HEADER.place(x = 0, y = 0)
        
        self.SEARCH = Entry_Text(
                ch_master = self.HEADER,
                ch_width = self.HEADER._current_width * 0.2,
                ch_height = self.HEADER._current_height * 0.05,
                ch_fg_color = "#ffffff",
                ch_corner_radius = 15,
                ch_border_width = 0.1,
                font_size = 13,
                ch_placeholder_text = "Hello",
        )
        self.SEARCH.place(x = 200, y = 100)
        self.SEARCH.focus_set()

        self.CONFIRM_BUTTON = Button(
            ch_master = self.HEADER,
            icon_name = "m_glass.png",
            text = "Hello",
            ch_fg_color = "#1f1f1f"
        )
        self.CONFIRM_BUTTON.place(x = 100, y = 100)

app = App()
