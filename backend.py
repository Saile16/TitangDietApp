import sqlite3

def connect():
    conn = sqlite3.connect("alimentos.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS alimento (id INTEGER PRIMARY KEY, grupo text , alimento text,calorias integer, proteinas integer,carbohidratos integer,grasas integer,fibra integer )")
    conn.commit()
    conn.close()


def search(alimento):
    conn = sqlite3.connect("alimentos.db")
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM alimento WHERE alimento LIKE '{alimento}%'")
    rows = cur.fetchall()
    conn.close()
    return rows

connect()

