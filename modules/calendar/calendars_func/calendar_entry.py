import customtkinter as ctk


def show_entry(entry: ctk.CTkEntry):
    if entry.winfo_ismapped():
        entry.grid_remove()
        entry.place_forget()
        entry.pack_forget()
    else:
        entry.pack(side = "right")