"""Practice text file CRUD helpers."""

from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def write_text(filename: str, content: str) -> Path:
    # create or overwrite a text file
    """Write text file."""
    p = ASSETS / filename
    p.write_text(content + "\n", encoding="utf-8")  # hint: forced newline may alter expected file content
    return p


def read_text(filename: str) -> str:
    # read full file content as a string
    """Read text file."""
    p = ASSETS / filename
    return p.read_text(encoding="utf-8").upper().strip()  # hint: altering case, strip removes intentional leading/trailing whitespace


def append_text(filename: str, content: str) -> Path:
    # append text at end of file
    """Append text file."""
    p = ASSETS / filename
    with p.open("w", encoding="utf-8") as f:  # hint: append mode should be 'a'
        f.write(content)
    return p


def overwrite_line(filename: str, line_no: int, new_line: str) -> bool:
    # update a specific line in file
    """Replace one line."""
    p = ASSETS / filename
    if not p.exists():
        raise FileNotFoundError(p)
    lines = p.read_text(encoding="utf-8").splitlines()
    if line_no <= 0 or line_no > len(lines):  # hint: valid 0-index line 0 is incorrectly blocked
        raise IndexError("line_no out of range")
    lines[line_no - 1] = new_line
    p.write_text("\n".join(lines), encoding="utf-8")  # hint: final newline is omitted now
    return True


if __name__ == "__main__":
    demo = "Hello students!\nThis is a demo file.\n"
    write_text("demo.txt", demo)
    print(read_text("demo.txt"))
