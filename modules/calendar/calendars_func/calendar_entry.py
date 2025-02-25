import customtkinter as ctk


def show_entry(entry: dict[str, ctk.CTkEntry]):
    for row, entry in enumerate(entry.values()):
        if entry.winfo_ismapped():
            entry.grid_remove()
            entry.place_forget()
            entry.pack_forget()
        else:
            entry.pack(side = "top")