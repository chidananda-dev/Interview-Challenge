import sqlite3
import json

conn = sqlite3.connect("vnet_data.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS vnets (
    id INTEGER PRIMARY KEY,
    name TEXT,
    data TEXT
)""")
conn.commit()

def store_vnet_data(data):
    c.execute("INSERT INTO vnets (name, data) VALUES (?, ?)", (data["vnet"], json.dumps(data)))
    conn.commit()

def get_all_vnets():
    c.execute("SELECT name, data FROM vnets")
    return [{"name": row[0], "details": json.loads(row[1])} for row in c.fetchall()]
