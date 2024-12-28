import sqlite3

conn = sqlite3.connect('UsersData.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    Id_User INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    User TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL
);
''')




print('conectado ao Banco de dados')




# cursor.execute('''
#     INSERT INTO Users(name)
#         VALUES (Gustavo)
# ''')