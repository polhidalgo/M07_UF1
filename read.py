from connection import def_cursor, conn

def read_users():
    cursor = def_cursor()
    cursor.execute("SELECT * FROM users;")
    Users = cursor.fetchall()
    for user in Users:
        print(user)
        
    cursor.close()
    print("Lectura de usuarios completa.")
