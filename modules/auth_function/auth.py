from ..data_base import db
from ..jsn_func import write_json
from ..window_funcs import logged_user
import customtkinter as ctk

def auth_function(auth_action: str = None, entry_frames: dict = None, root: ctk.CTk = None):
    
    if auth_action == 'register':
        flag_register = db.insert_user(
            name = entry_frames["NAME"].get(),
            password = entry_frames["PASSWORD"].get(),
            email = entry_frames["EMAIL"].get())
        print(f'Зашло в условие с флагом регистрации, сам флаг : {flag_register}')
        
        if flag_register:
            log = {"user_status" : "registered"}
            print(f'================================================================')
            write_json(filename = "utility.json", obj_dict = log)
            logged_user(root = root)
        
    elif auth_action == "login":
        flag_login = db.find_user(
            name = entry_frames["NAME"].get(),
            password = entry_frames["PASSWORD"].get())
        print(f'Зашло в условие с флагом авториации, сам флаг : {flag_login}')
    
        if flag_login:
            log = {"user_status" : "logged"}
            write_json(filename = "utility.json", obj_dict = log)
            logged_user(root = root)
            print(f'Зашло в условие с флагом авториации')