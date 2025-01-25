import customtkinter as ctk 

class Frame(ctk.CTkFrame):
    '''
    Класс который позволит нам создовать `Frames` используя `наследование`
    '''
    def __init__(self, ch_masther: object, ch_width: int, ch_height: int, ch_fg_color: str, **kwargs):
        ctk.CTkFrame.__init__(
            self,
            master = ch_masther,
            width = ch_width,
            height = ch_height,
            fg_color = ch_fg_color,
            corner_radius = 0,
            **kwargs)
        self.grid_propagate(False)