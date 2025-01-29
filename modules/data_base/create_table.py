import sqlite3 as sql

with sql.connect('modules/data_base/database.db') as db:
    cursor = db.cursor()
    request = '''CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT, password TEXT, email TEXT)'''
    cursor.execute(request)