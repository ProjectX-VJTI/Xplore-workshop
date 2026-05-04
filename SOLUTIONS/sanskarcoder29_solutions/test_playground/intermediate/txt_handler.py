"""Text file helpers."""

from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

def write_text(filename: str, content: str) -> Path:

    p = ASSETS / filename
    p.write_text(content, encoding="utf-8")

    return p


def read_text(filename: str) -> str:

    p = ASSETS / filename
    return p.read_text(encoding="utf-8")


def append_text(filename: str, content: str) -> Path:

    p = ASSETS / filename

    with p.open("a", encoding="utf-8") as f:
        f.write(content)

    return p