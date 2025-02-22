from ..jsn_func import read_json 
from ..window_funcs import swith_frame
import customtkinter as ctk

def logged_user(root: ctk.CTk):
    '''
    Данная функция, будет перебрасывать пользователя на окно контента (календаря)
    '''
    # Читаем данные из utility.json
    log_data = read_json(filename = "utility.json")
    
    # Если всё успешно, переходим к окну контента (календаря)
    if log_data["user_status"] == "logged":
        swith_frame(root = root, frame_name = "MAIN_FRAME")
    # Если всё успешно, переходим к окну контента (календаря)
    elif log_data["user_status"] == "registered":
        swith_frame(root = root, frame_name = "MAIN_FRAME")