
from connection import def_cursor, conn

def create_table():
    cursor = def_cursor()
    
    cursor.execute('''DROP TABLE IF EXISTS users''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            Id SERIAL PRIMARY KEY,
            Nom VARCHAR(50) NOT NULL,
            Cognom VARCHAR(50) NOT NULL,
            Edat INTEGER NOT NULL,
            Email VARCHAR(100) UNIQUE NOT NULL
        );
    ''')
    conn.commit()
    cursor.close()
    print("Tabla 'users' creada correctamente.")


if __name__ == "__main__":
    create_table()
