import sqlite3 as sql

class DataBase:
    def __init__(self, path_db :str):
        self.db_path = path_db
        self.connect = sql.connect(self.db_path, check_same_thread = True) 
        self.cursor = self.connect.cursor()
        
    def create_table(self) -> None:
        request = f'''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL)'''
        self.cursor.execute(request)
        self.connect.commit()

    def insert_user(self, name : str, password : str, email : str) -> bool:
        request = '''INSERT INTO users (name, password, email) VALUES (?, ?, ?)'''
        self.cursor.execute(request, (name, password, email))
        self.connect.commit()
        print(f'')
        return True

    
    def find_user(self,  name : str, password : str) -> bool: 
        request = '''SELECT * FROM users WHERE name = ? AND password = ?'''
        self.cursor.execute(request,(name, password))
        result = self.cursor.fetchall()
        print(f'Это найденный пользователь : {result}')
        return result
    
    def close_table(self):
        self.connect.close()

db = DataBase(path_db = "modules/data_base/database.db")
db.create_table()