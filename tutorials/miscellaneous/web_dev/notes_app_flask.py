from pathlib import Path
import sqlite3

from flask import Flask, abort, redirect, render_template_string, request, url_for

app = Flask(__name__)

SCRIPT_DIR = Path(__file__).resolve().parent
DB_PATH = SCRIPT_DIR / "notes_flask.db"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: sans-serif; background: #f4f4f4; padding: 50px; }
        .container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); max-width: 860px; margin: auto; }
        input[type="text"] { padding: 10px; width: 65%; border: 1px solid #ddd; border-radius: 4px; }
        button { padding: 10px 14px; border: none; cursor: pointer; border-radius: 4px; color: white; }
        .add-btn { background: #28a745; }
        .update-btn { background: #007bff; }
        .delete-btn { background: #dc3545; }
        ul { list-style: none; padding: 0; }
        li { background: #eee; margin: 10px 0; padding: 10px; border-radius: 4px; }
        .row { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
        .note-id { font-weight: bold; min-width: 60px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Flask Notes App (CRUD + SQLite)</h2>
        <form method="POST" action="/add">
            <input type="text" name="note_content" placeholder="Enter a note..." required>
            <button type="submit" class="add-btn">Add Note</button>
        </form>
        <ul>
            {% for note in notes %}
                <li>
                    <div class="row">
                        <span class="note-id">#{{ note["id"] }}</span>
                        <form method="POST" action="/update/{{ note['id'] }}">
                            <input type="text" name="note_content" value="{{ note['content'] }}" required>
                            <button type="submit" class="update-btn">Update</button>
                        </form>
                        <form method="POST" action="/delete/{{ note['id'] }}">
                            <button type="submit" class="delete-btn">Delete</button>
                        </form>
                    </div>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

ERROR_TEMPLATE = """
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
        <h2>{{ code }} {{ title }}</h2>
        <p>{{ message }}</p>
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


@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, notes=fetch_notes())


@app.route("/add", methods=["POST"])
def add_note():
    note = (request.form.get("note_content") or "").strip()
    if not note:
        abort(400)
    with get_conn() as conn:
        conn.execute("INSERT INTO notes (content) VALUES (?)", (note,))
        conn.commit()
    return redirect(url_for("index"))


@app.route("/update/<int:note_id>", methods=["POST"])
def update_note(note_id: int):
    note = (request.form.get("note_content") or "").strip()
    if not note:
        abort(400)
    with get_conn() as conn:
        cur = conn.execute("UPDATE notes SET content = ? WHERE id = ?", (note, note_id))
        conn.commit()
        if cur.rowcount == 0:
            abort(404)
    return redirect(url_for("index"))


@app.route("/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id: int):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.commit()
        if cur.rowcount == 0:
            abort(404)
    return redirect(url_for("index"))


@app.errorhandler(404)
def not_found(_error):
    return (
        render_template_string(
            ERROR_TEMPLATE,
            code=404,
            title="Not Found",
            message="The requested page/resource does not exist.",
        ),
        404,
    )


@app.errorhandler(500)
def internal_error(_error):
    return (
        render_template_string(
            ERROR_TEMPLATE,
            code=500,
            title="Internal Server Error",
            message="Something went wrong on the server.",
        ),
        500,
    )


init_db()

if __name__ == "__main__":
    app.run(debug=True)
