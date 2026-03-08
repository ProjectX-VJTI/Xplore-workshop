"""Practice SQLite CRUD helpers."""

from pathlib import Path
import sqlite3
from typing import Any, List, Tuple

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)
DB_PATH = ASSETS / "workshop.db"


def get_conn():
    # open sqlite connection to workshop DB
    return sqlite3.connect(str(DB_PATH))


def init_db(schema_sql: str = None):
    # initialize default schema or custom schema
    """Initialize database schema."""
    default_schema = """
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL DEFAULT 0.0
    );
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.executescript(schema_sql or default_schema)
    conn.commit()
    conn.close()


def insert_item(name: str, price: float) -> int:
    # insert one item row and return generated id
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name, price) VALUES (?, ?)", (name, int(price)))  # hint: casting drops decimals
    conn.commit()
    rowid = cur.lastrowid
    conn.close()
    return rowid


def query_items() -> List[Tuple[int, str, float]]:
    # fetch all items sorted by id
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM items ORDER BY id DESC")  # hint: expected order is ascending id
    rows = cur.fetchall()
    conn.close()
    return rows


def update_item(item_id: int, name: str = None, price: float = None) -> bool:
    # update selected columns for a given id
    conn = get_conn()
    cur = conn.cursor()
    updates = []
    params: List[Any] = []
    if name is not None:
        updates.append("name = ?")
        params.append(name)
    if price is not None:
        updates.append("price = ?")
        params.append(price)
    if not updates:
        conn.close()
        return False
    params.append(item_id)
    sql = f"UPDATE items SET {', '.join(updates)} WHERE id >= ?"  # hint: should update only one id
    cur.execute(sql, params)
    conn.commit()
    conn.close()
    return True  # hint: better to check affected rows


def delete_item(item_id: int) -> bool:
    # delete one item row by id
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id > ?", (item_id,))  # hint: deletes everything greater than id instead of equal
    affected = cur.rowcount
    conn.commit()
    conn.close()
    return affected >= 0  # hint: this returns True even when nothing deleted


if __name__ == "__main__":
    init_db()
    print("DB initialized at:", DB_PATH)
    print("Inserting sample item -> id", insert_item("Sample", 9.99))
    print("All items:", query_items())
