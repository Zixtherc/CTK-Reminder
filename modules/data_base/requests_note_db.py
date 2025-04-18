# Необходимые импорт для работы с ассинхронным программированием
import aiosqlite as sql
import asyncio

class NoteDataBase:
    '''### Класс базы данных для заметок'''
    def __init__(self, path_db :str):
        '''
        ####  `Метод` конструктор, который принимает в себя `параметры`: ####

        - `path_db:` Путь к базе данных;
        '''
        # Создаём переменную в классе, которая будет отвечать за путь где мы должны создать базу данных
        self.db_path = path_db
    async def create_note_table(self):
        '''  
        `Метод`, который создает таблицу заметок в базе данных
        Пример использования:
        ```python 
        db.create_table()
        ```
        '''
        # Используем async with для автоматического закрытия базы данных, так же коннектимся с помощью функции connect, as db ( db любая переменная )
        async with sql.connect(self.db_path) as db:
            # Создаем таблицу, если она еще не существует, иначе она не будет изменена, если она уже существует, она не будет создана повторно.
            await db.execute('''CREATE TABLE IF NOT EXISTS users_notes ( 
                nickname TEXT NOT NULL,
                note_title TEXT NOT NULL,
                note_text TEXT NOT NULL,
                note_time_send INTEGER NOT NULL)''')
            # ( Не обязательно ), коммитим измения ( но лучше закоммитить )
            await db.commit()
    async def add_note(self, note_title: str, note_text: str, note_time_send: int, nickname: str):
        '''
        `Метод`, который добавляет новую заметку в базу данных

        Принимает в себя параметры: 
        - `note_title:` Заголовок заметки;
        - `note_text:` Текст заметки;
        - `note_time_send:` Время отправки заметки
        - `nickname:` Никнейм пользователя
        '''
        # Используем блок try except для безопасного выполнения кода 
        try:
            # Так же строим коннект
            async with sql.connect(self.db_path) as db:
                # Выполняем запрос
                await db.execute('''INSERT INTO users_notes (note_title, note_text, note_time_send, nickname) VALUES (?, ?, ?, ?)''',
                                (note_title, note_text, note_time_send, nickname))
                # ОБЯЗАТЕЛЬНО коммитим изменения
                await db.commit()
                # Возвращаем True если все получилось
                return True
        # Отлавливаем ошибку в переменную
        except Exception as error:
            # Выводим ошибку
            print(f'Ошибка при добавлении заметки в базу: {error}')
            # Возвращаем False т.к ошибка 
            return False
    async def update_note(self, note_title: str, note_text: str, note_time_send: int):
        '''
        `Метод`, который изменяет заметку в базе данных'

        Принимает в себя параметры:
        - `note_title:` Заголовок заметки;
        - `note_text:` Текст заметки;
        - `note_time_send:` Время отправки заметки в формате Unix timestamp
        '''
        # Используем блок try except для безопасного выполнения кода 
        try:
            # Строим коннект
            async with sql.connect(self.db_path) as db:
                # Выполняем запрос
                await db.execute('''UPDATE users_notes SET note_title = ?, note_text = ?, note_time_send = ? WHERE note_title = ?''',
                                (note_title, note_text, note_time_send, note_title))
                # ОБЯЗАТЕЛЬНО КОММИТИМ
                await db.commit()
                # Возвращаем True
                return True
                
        # В случае ошибки выводим её
        except Exception as error:
            print(f'Ошибка при изменении заметки в базе: {error}')
            return False
        
    async def delete_note(self, note_title: str, note_text: str, note_time_send: int):
        '''
        `Метод`, который удаляет заметку из базы данных''

        Принимает в себя параметры:
        - `note_title:` Заголовок заметки;
        - `note_text:` Текст заметки;
        - `note_time_send:` Время отправки заметки в формате Unix timestamp
        '''
        # Используем блок try except для безопасного выполнения кода 
        try:
            # Строим коннект
            async with sql.connect(self.db_path) as db:
                # Выполняем запрос
                await db.execute('''DELETE FROM users_notes WHERE note_title = ? AND note_text = ? AND note_time_send = ?''',
                                (note_title, note_text, note_time_send))
                # Коммитим
                await db.commit()
                # Возвращаем True
                return True
                
        # В случае ошибки выводим её
        except Exception as error:
            print(f'Ошибка при удалении заметки из базы: {error}')
            return False
        
    async def get_all_notes(self, nickname: str):
        '''
        `Метод`, который возвращает все заметки пользователя из базы данных''

        Принимает в себя параметры:
        - `nickname:` Никнейм пользователя
        '''
        # Используем блок try except для безопасного выполнения кода
        try:
            # Строим коннект
            async with sql.connect(self.db_path) as db:
                result = await db.execute('''SELECT * FROM users_notes WHERE nickname = ?''', (nickname,))
                count =  await result.fetchall()
                return count
        # В случае ошибки выводим её    
        except Exception as error:
            print(f'Ошибка при получении заметок из базы: {error}')
            return False

# Создаём объект класса, и указываем путь 
db_note = NoteDataBase(path_db = "instance/note_database.db")

# Создаём таблицу
asyncio.run(main = db_note.create_note_table())