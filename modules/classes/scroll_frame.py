import customtkinter as ctk

class ScrollFrame(ctk.CTkScrollableFrame):
    '''
    ### Класс, который позволяет создать прокручиваемый рядка с использованием customtkinter ###
    '''
    def __init__(self, ch_master: object, ch_width: int, ch_height: int, ch_corner_radius: int, 
                 ch_border_width: int, ch_border_color: str, ch_fg_color: str, ch_scrollbar_fg_color: str, 
                 ch_scrollbar_button_color: str, ch_scrollbar_button_hover_color: str, ch_orientation: str, **kwargs):
        
        ctk.CTkScrollableFrame.__init__(
            self,
            master = ch_master,
            width = ch_width,
            height = ch_height,
            corner_radius = ch_corner_radius,
            border_width = ch_border_width,
            border_color = ch_border_color,
            fg_color = ch_fg_color,
            scrollbar_fg_color = ch_scrollbar_fg_color,
            scrollbar_button_color = ch_scrollbar_button_color,
            scrollbar_button_hover_color = ch_scrollbar_button_hover_color,
            orientation = ch_orientation,
            **kwargs
            )
        # Устанавливаем флаг, что размеры НЕ будут автоматически подстраиваться под размеры содержимого
        self.pack_propagate(flag = False)
        self.grid_propagate(flag =False)