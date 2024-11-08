from connection import def_cursor, conn

def update_user(user_id, nom=None, cognom=None, edat=None, email=None):
    cursor = def_cursor()
    query = "UPDATE users SET "
    params = []
    
    if nom:
        query += "Nom = %s, "
        params.append(nom)
    if cognom:
        query += "Cognom = %s, "
        params.append(cognom)
    if edat:
        query += "Edat = %s, "
        params.append(edat)
    if email:
        query += "Email = %s, "
        params.append(email)
    
    query = query.rstrip(", ") + " WHERE Id = %s"
    params.append(user_id)

    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    print(f"Usuario con ID {user_id} actualizado.")
