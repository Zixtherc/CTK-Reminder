import customtkinter as ctk

class Gradient_Canvas(ctk.CTkCanvas):
    def __init__(self, ch_master: object, ch_first_color: str = "#0000FF", ch_second_color: str = "#9D00FF",  **kwargs):
        
        ctk.CTkCanvas.__init__(self, ch_master, **kwargs)
        self.ch_first_color = ch_first_color
        self.ch_second_color = ch_second_color
        self.bind("<Configure>", self.draw_gradient)

    def draw_gradient(self, event: object = None):

        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width

        (red_one, green_one, blue_one) = self.winfo_rgb(self.ch_first_color)
        (red_two, green_two, blue_two) = self.winfo_rgb(self.ch_second_color)
        relative_red = float(red_two - red_one) / limit
        relative_green = float(green_two - green_one) / limit
        relative_blue = float(blue_two - blue_one) / limit

        for colors in range(0, limit, 2):
            
            new_red = int(red_one + (relative_red * colors))
            new_green = int(green_one + (relative_green * colors))
            new_blue = int(blue_one + (relative_blue * colors))

            color = "#%4.4x%4.4x%4.4x" % (new_red, new_green, new_blue)
            self.create_rectangle(colors, 0, colors + 2, height, tags=("gradient",), fill = color, outline = "")

        self.lower("gradient")
        self.configure(bg = self.ch_first_color, highlightthickness = 0)