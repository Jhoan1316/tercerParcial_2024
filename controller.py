import time
import sqlite3 as sql

def crearteDB():
    conn = sql.connect("autoconocimiento.db")
    print("base de datos autoconocimiento creada")
    conn.commit()
    conn.close()

def createTable():
    coon = sql.connect("autoconocimiento.db")
    cursor = coon.cursor()
    cursor.execute(""" CREATE TABLE progress_tracking (
    tracking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    experience_id INTEGER,
    experience_type TEXT,  -- 'growth' or 'contribution'
    milestone TEXT,
    completion_percentage INTEGER DEFAULT 0,
    notes TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (experience_id) REFERENCES growth_experiences(growth_id)
    );
    """)

    print("tabla creada")
    coon.commit()
    coon.close()

if __name__ == "__main__":
    crearteDB()
    createTable()