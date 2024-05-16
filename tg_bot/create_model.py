import sqlite3

"""
    Создать базы данных sqlite3
    Запускается только один раз
"""

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE users (user_id INTEGER PRIMARY KEY)''')
conn.commit()
conn.close()