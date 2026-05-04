"""SQLite CRUD helpers."""

from pathlib import Path
import sqlite3

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

DB_PATH = ASSETS / "workshop.db"


def get_conn():

    return sqlite3.connect(str(DB_PATH))


def init_db():

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL
    )
    """)

    conn.commit()
    conn.close()


def insert_item(name: str, price: float):

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("INSERT INTO items (name, price) VALUES (?, ?)", (name, price))

    conn.commit()
    conn.close()