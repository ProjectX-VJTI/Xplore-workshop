from html import escape
from pathlib import Path
import sqlite3

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

SCRIPT_DIR = Path(__file__).resolve().parent
DB_PATH = SCRIPT_DIR / "notes_fastapi.db"

FAST_HTML = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: sans-serif; background: #eef2f3; padding: 50px; }
        .container { background: white; max-width: 860px; margin: auto; padding: 20px; border-radius: 8px; border-left: 5px solid #007bff; }
        input[type="text"] { padding: 10px; width: 65%; border: 1px solid #ddd; border-radius: 4px; }
        button { border: none; color: white; padding: 10px 12px; border-radius: 4px; cursor: pointer; }
        .add-btn { background: #007bff; }
        .update-btn { background: #20a0ff; }
        .delete-btn { background: #dc3545; }
        ul { list-style: none; padding: 0; }
        li { background: #f4f6f8; margin: 10px 0; padding: 10px; border-radius: 4px; }
        .row { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
        .note-id { font-weight: bold; min-width: 60px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>FastAPI Notes App (CRUD + SQLite)</h2>
        <form action="/add" method="post">
            <input type="text" name="note" required>
            <button type="submit" class="add-btn">Post Note</button>
        </form>
        <ul>
            __NOTES_ITEMS__
        </ul>
    </div>
</body>
</html>
"""

ERROR_HTML = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: sans-serif; background: #f6f7fb; padding: 50px; }
        .container { background: white; max-width: 640px; margin: auto; padding: 24px; border-radius: 8px; border-left: 6px solid #dc3545; }
        a { color: #007bff; text-decoration: none; }
    </style>
</head>
<body>
    <div class="container">
        <h2>__CODE__ __TITLE__</h2>
        <p>__MESSAGE__</p>
        <p><a href="/">Back to Notes</a></p>
    </div>
</body>
</html>
"""


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_conn() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL
            )
            """
        )
        conn.commit()


def fetch_notes() -> list[sqlite3.Row]:
    with get_conn() as conn:
        rows = conn.execute("SELECT id, content FROM notes ORDER BY id DESC").fetchall()
    return rows


def render_notes_page() -> HTMLResponse:
    rows = fetch_notes()
    items = []
    for row in rows:
        rid = int(row["id"])
        content = escape(row["content"])
        items.append(
            f"""
            <li>
                <div class="row">
                    <span class="note-id">#{rid}</span>
                    <form action="/update/{rid}" method="post">
                        <input type="text" name="note" value="{content}" required>
                        <button type="submit" class="update-btn">Update</button>
                    </form>
                    <form action="/delete/{rid}" method="post">
                        <button type="submit" class="delete-btn">Delete</button>
                    </form>
                </div>
            </li>
            """
        )
    return HTMLResponse(content=FAST_HTML.replace("__NOTES_ITEMS__", "".join(items)))


@app.get("/", response_class=HTMLResponse)
async def read_notes():
    return render_notes_page()


@app.post("/add")
async def create_note(note: str = Form(...)):
    clean = note.strip()
    if not clean:
        raise HTTPException(status_code=400, detail="Note content cannot be empty")
    with get_conn() as conn:
        conn.execute("INSERT INTO notes (content) VALUES (?)", (clean,))
        conn.commit()
    return RedirectResponse(url="/", status_code=303)


@app.post("/update/{note_id}")
async def update_note(note_id: int, note: str = Form(...)):
    clean = note.strip()
    if not clean:
        raise HTTPException(status_code=400, detail="Note content cannot be empty")
    with get_conn() as conn:
        cur = conn.execute("UPDATE notes SET content = ? WHERE id = ?", (clean, note_id))
        conn.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Note id {note_id} not found")
    return RedirectResponse(url="/", status_code=303)


@app.post("/delete/{note_id}")
async def delete_note(note_id: int):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Note id {note_id} not found")
    return RedirectResponse(url="/", status_code=303)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(_request: Request, exc: StarletteHTTPException):
    title = "Not Found" if exc.status_code == 404 else "HTTP Error"
    message = (
        "The requested page/resource does not exist."
        if exc.status_code == 404
        else str(exc.detail)
    )
    page = (
        ERROR_HTML.replace("__CODE__", str(exc.status_code))
        .replace("__TITLE__", escape(title))
        .replace("__MESSAGE__", escape(message))
    )
    return HTMLResponse(content=page, status_code=exc.status_code)


@app.exception_handler(Exception)
async def internal_exception_handler(_request: Request, _exc: Exception):
    page = (
        ERROR_HTML.replace("__CODE__", "500")
        .replace("__TITLE__", "Internal Server Error")
        .replace("__MESSAGE__", "Something went wrong on the server.")
    )
    return HTMLResponse(content=page, status_code=500)


init_db()

# Run with: uvicorn notes_app_fastapi:app --reload
