from connection import def_cursor, conn

def create_user(nom, cognom, edat, email):
    cursor = def_cursor()
    cursor.execute('''
        INSERT INTO users (Nom, Cognom, Edat, Email)
        VALUES (%s, %s, %s, %s);
    ''', (nom, cognom, edat, email))
    conn.commit()
    cursor.close()
    print("Usuario creado exitosamente.")
