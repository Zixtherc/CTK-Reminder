import sqlite3 as sql
# from .create_table import cursor
# from .create_table import db
def insert_user(id:int, name : str, password : str, email : str):
    with sql.connect('modules/data_base/database.db') as db:
        cursor = db.cursor()
        request = f'''INSERT INTO users (id, name, password, email) VALUES(?, ?, ?, ?)'''
        cursor.execute(request, (id, name, password, email))
        db.commit()

insert_user(id = 1, name = 'David', password = '13', email = '123')