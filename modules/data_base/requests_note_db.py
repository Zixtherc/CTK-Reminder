import aiosqlite as sql
import asyncio

class NoteDataBase:
    '''### Класс базы данных для заметок'''
    def __init__(self, path_db :str):
        '''
        ####  `Метод` конструктор, который принимает в себя `параметры`: ####

        - `path_db:` Путь к базе данных;
        '''
        self.db_path = path_db
    async def create_note_table(self):
        '''  
        `Метод`, который создает таблицу заметок в базе данных

        Пример использования:
        ```python 
        db.create_table()
        ```
        '''
        async with sql.connect(self.db_path) as db:
            await db.execute('''CREATE TABLE IF NOT EXISTS users_notes ( 
                note_title TEXT NOT NULL,
                note_text TEXT NOT NULL,
                note_time_send INTEGER NOT NULL,
                email TEXT UNIQUE NOT NULL)''')
            await db.commit()
    async def add_note(self, note_title: str, note_text: str, note_time_send: int, email: str = None):
        '''
        `Метод`, который добавляет новую заметку в базу данных

        Принимает в себя параметры: 
        - `note_title:` Заголовок заметки;
        - `note_text:` Текст заметки;
        - `note_time_send:` Время отправки заметки в формате Unix timestamp;
        - `email:` Почта ( при добавления событий с помощь Google Calendar )
        '''
        try:
            if email:
                async with sql.connect(self.db_path) as db:
                    await db.execute('''INSERT INTO users_notes (note_title, note_text, note_time_send, email) VALUES (?, ?, ?, ?)''',
                                    (note_title, note_text, note_time_send, email))
                    await db.commit()
                    return True
            else:
                async with sql.connect(self.db_path) as db:
                    await db.execute('''INSERT INTO users_notes (note_title, note_text, note_time_send) VALUES (?, ?, ?)''',
                                    (note_title, note_text, note_time_send))
                    await db.commit()
                    return True
        except Exception as error:
            print(f'Ошибка при добавлении заметки в базу: {error}')
            return False
    async def update_note(self, note_title: str, note_text: str, note_time_send: int, email: str = None):
        '''
        `Метод`, который изменяет заметку в базе данных'

        Принимает в себя параметры:
        - `note_title:` Заголовок заметки;
        - `note_text:` Текст заметки;
        - `note_time_send:` Время отправки заметки в формате Unix timestamp;
        - `email:` Почта ( при добавления событий с помощь Google Calendar )
        '''
        try:
            if email:
                async with sql.connect(self.db_path) as db:
                    await db.execute('''UPDATE users_notes SET note_title = ?, note_text = ?, note_time_send = ?, email = ? WHERE email = ?''',
                                    (note_title, note_text, note_time_send, email, email))
                    await db.commit()
                    return True
            else:
                async with sql.connect(self.db_path) as db:
                    await db.execute('''UPDATE users_notes SET note_title = ?, note_text = ?, note_time_send = ? WHERE note_title = ?''',
                                    (note_title, note_text, note_time_send, note_title))
                    await db.commit()
                    return True
        except Exception as error:
            print(f'Ошибка при изменении заметки в базе: {error}')
            return False
        
    async def delete_note(self, note_title: str, note_text: str, note_time_send: int, email: str = None):
        '''
        `Метод`, который удаляет заметку из базы данных''

        Принимает в себя параметры:
        - `note_title:` Заголовок заметки;
        - `note_text:` Текст заметки;
        - `note_time_send:` Время отправки заметки в формате Unix timestamp;
        - `email:` Почта ( при добавления событий с помощь Google Calendar )
        '''
        try:
            if email:
                async with sql.connect(self.db_path) as db:
                    await db.execute('''DELETE FROM users_notes WHERE note_title = ? AND note_text = ? AND note_time_send = ? AND email = ?''',
                                    (note_title, note_text, note_time_send, email))
                    await db.commit()
                    return True
            else:
                async with sql.connect(self.db_path) as db:
                    await db.execute('''DELETE FROM users_notes WHERE note_title = ? AND note_text = ? AND note_time_send = ?''',
                                    (note_title, note_text, note_time_send))
                    await db.commit()
                    return True
        except Exception as error:
            print(f'Ошибка при удалении заметки из базы: {error}')
            return False
    async def get_all_notes(self, nickname: str, email: str):
        '''
        `Метод`, который возвращает все заметки пользователя из базы данных''

        Принимает в себя параметры:
        - `nickname:` Никнейм пользователя;
        - `email:` Почта пользователя ( при добавления событий с помощь Google Calendar )
        '''
        try:
            async with sql.connect(self.db_path) as db:
                if email:
                    result = await db.execute('''SELECT * FROM users_notes WHERE email = ?''', (email,))
                    return await result.fetchall()
                else:
                    result = await db.execute('''SELECT * FROM users_notes WHERE nickname = ?''', (nickname,))
                return await result.fetchall()
        except Exception as error:
            print(f'Ошибка при получении заметок из базы: {error}')
            return False

db_note = NoteDataBase(path_db = "instance/note_database.db")

asyncio.run(main = db_note.create_note_table())