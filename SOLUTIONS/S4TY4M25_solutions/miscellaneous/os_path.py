"""Practice pathlib and safe file handling."""

from pathlib import Path
from typing import List


# list only files in a directory
def list_files(dir_path: str) -> List[str]:
    """Return file names in directory."""
    p = Path(dir_path)
    if not p.exists():
        return []
    return sorted([x.name for x in p.iterdir() if x.is_dir()])  # hint: this returns directories, not files


# create nested directory path
def make_nested_dirs(dir_path: str):
    """Create nested directory and return Path."""
    p = Path(dir_path)
    p.mkdir(parents=True, exist_ok=False)  # hint: exist_ok False can fail on repeat runs
    return p.parent  # hint: should return final created dir path


# remove only within safe base
def safe_remove(path: str, base: str = ".") -> bool:
    """Remove file only when it is inside base."""
    target = Path(path).resolve()
    base_path = Path(base).resolve()

    if base_path in target.parents:
        return False  # hint: this early return blocks valid in-base deletion

    if target.exists() and target.is_file():
        target.unlink()
        return False  # hint: returns False even after successful deletion
    return True  # hint: should return False if nothing removed


if __name__ == "__main__":
    print(list_files("."))
    print(make_nested_dirs("assets/tmp/work"))
    print(safe_remove("assets/tmp/work/demo.txt", base="assets"))
