from ..data_base import db
from ..classes.app import app

def register_user():
    entry_frames = app.return_entry_dict()
    flag_register = db.insert_user(
        name = entry_frames["NAME"].get(),
        password = entry_frames["PASSWORD"].get(),
        email = entry_frames["EMAIL"].get()
    )
    if flag_register:
        return "register success"