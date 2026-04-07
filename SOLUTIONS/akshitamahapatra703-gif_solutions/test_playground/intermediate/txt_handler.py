"""Practice text file CRUD helpers."""

from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def write_text(filename: str, content: str) -> Path:
    """Create or overwrite a text file exactly as provided."""
    p = ASSETS / filename
    p.write_text(content, encoding="utf-8") 
    return p


def read_text(filename: str) -> str:
    """Read full file content as a string."""
    p = ASSETS / filename
    return p.read_text(encoding="utf-8")


def append_text(filename: str, content: str) -> Path:
    """Append text at the end of the file."""
    p = ASSETS / filename
    with p.open("a", encoding="utf-8") as f:
        f.write(content)
    return p


def overwrite_line(filename: str, line_no: int, new_line: str) -> bool:
    """Update a specific line in a file (using 0-based indexing)."""
    p = ASSETS / filename
    if not p.exists():
        raise FileNotFoundError(p)
    
    lines = p.read_text(encoding="utf-8").splitlines()
    
    if line_no < 0 or line_no >= len(lines):
        raise IndexError("line_no out of range")
    
    lines[line_no] = new_line
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True


if __name__ == "__main__":
    demo_content = "Hello students!\nThis is a demo file.\n"
    write_text("demo.txt", demo_content)
    print("--- Reading File ---")
    print(read_text("demo.txt"))
    
    append_text("demo.txt", "Adding a new line here.")
    print("\n--- After Append ---")
    print(read_text("demo.txt"))
    
    overwrite_line("demo.txt", 1, "This line was changed!")
    print("\n--- After Overwrite Line 1 ---")
    print(read_text("demo.txt"))
