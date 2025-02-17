from ..data_base import db
from ..jsn_func import write_json

def auth_function(auth_action: str = None, entry_frames: dict = None):
    
    if auth_action == 'register':
        flag_register = db.insert_user(
            name = entry_frames["NAME"].get(),
            password = entry_frames["PASSWORD"].get(),
            email = entry_frames["EMAIL"].get())
        
        if flag_register:
            log = {"user_status" : "registered"}
            write_json(filename = "utility.json", obj_dict = log)
        
    elif auth_action == "login":
        flag_login = db.find_user(
            name = entry_frames["NAME"].get(),
            password = entry_frames["PASSWORD"].get())
        
        if flag_login:
            log = {"user_status" : "logged"}
            write_json(filename = "utility.json", obj_dict = log)