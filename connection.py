
import psycopg2


conn = psycopg2.connect(
        host="localhost",
        port="5433",
        database="poldb",
        user="poldb",
        password="poldb"
)
connection = conn.cursor
print(connection)

def def_cursor():
    return conn.cursor()
