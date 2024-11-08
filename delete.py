from connection import def_cursor, conn

def delete_user(user_id):
    cursor = def_cursor()
    cursor.execute("DELETE FROM users WHERE Id = %s;", (user_id,))
    conn.commit()
    cursor.close()
    print(f"Usuario con ID {user_id} eliminado.")
