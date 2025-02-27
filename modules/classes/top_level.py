from .label import Label
import customtkinter as ctk

class TopLevelWidget(ctk.CTkToplevel):
    def __init__(self, ch_master: object, ch_width: int, ch_height: int, ch_fg_color: str, label_text: str, **kwargs):
        self.label_text = label_text
        self.width = ch_width
        self.height = ch_height
        ctk.CTkToplevel.__init__(
            self,
            master = ch_master,
            width = ch_width,
            height = ch_height,
            fg_color = ch_fg_color,
            **kwargs
        )
        # Устанавливаем флаг, что размеры НЕ будут автоматически подстраиваться под размеры содержимого
        self.pack_propagate(False)
        self.grid_propagate(False)

        label = Label(ch_master = self, ch_width = self.width, ch_height = self.height, ch_fg_color = "#807180", ch_text = self.label_text)
        label.pack()
        self.focus_force()
        self.grab_set()