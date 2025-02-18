from ..jsn_func import read_json 
from ..window_funcs import swith_frame
import customtkinter as ctk

def logged_user(root: ctk.CTk):
    
    log_data = read_json(filename = "utility.json")
    
    if log_data["user_status"] == "logged":
        swith_frame(root = root, frame_name = "SECOND_HEADER", frame_color = "#D90166")
    elif log_data["user_status"] == "registered":
        swith_frame(root = root, frame_name = "SECOND_HEADER", frame_color = "#D90166")