import aiosqlite as sql
import asyncio

class DataBase:
    '''### Класс базы данных'''
    def __init__(self, path_db :str):
        '''
        ####  `Метод` конструктор, который принимает в себя `параметры`: ####

        - `path_db:` Путь к базе данных;
        '''
        self.db_path = path_db
    async def create_table(self):
        '''  
        `Метод`, который создает таблицу в базе данных

        Пример использования:
        ```python 
        db.create_table()
        ```
        '''
        async with sql.connect(self.db_path) as db:
            await db.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL)''')
            await db.commit()

    async def insert_user(self, name : str, password : str, email : str) -> bool:
        '''
        `Метод`, который добавляет нового пользователя в базу данных

        Принимает в себя параметры: 
        - `name:` Имя пользователя;
        - `password:` Пароль пользователя;
        - `email:` Электронная почта пользователя;
        '''
        try:
            async with sql.connect(self.db_path) as db:
                await db.execute('''INSERT INTO users (name, password, email) VALUES (?, ?, ?)''', (name, password, email))
                await db.commit()
                return True
        except Exception as error:
            print(f'Ошибка при регистрации пользователя: {error}')
            return False
    
    async def find_user(self,  name : str, password : str) -> bool:
        '''
        `Метод`, который ищет пользователя в базе данных

        Принимает в себя параметры:
        - `name:` Имя пользователя;
        - `password:` Пароль пользователя;
        '''
        async with sql.connect(self.db_path) as db:
            async with db.execute('''SELECT * FROM users WHERE name = ? AND password = ?''', (name, password)) as cursor:
                find_user = await cursor.fetchone()
                if find_user:
                    result = find_user[0]
                    return result

# Создаём объект от класса DataBase
db = DataBase(path_db = "instance/database.db")

# Вызываем метод создания базы данных
asyncio.run(db.create_table())