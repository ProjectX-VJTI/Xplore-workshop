# File I/O: examples using pathlib so operations are independent of current working directory
from pathlib import Path

# Base directories (script-local)
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "Python"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Helper paths
SAMPLE = DATA_DIR / "Sample.txt"
SAMPLE2 = DATA_DIR / "Sample2.txt"
PRACTICE = DATA_DIR / "Practice.txt"

print("--- Read/Write examples (pathlib) ---")

# Ensure Sample exists for reading; create with example content if missing
if not SAMPLE.exists():
    SAMPLE.write_text("This is an example Sample file.\nReplace with your own content.")

# Read whole file
data = SAMPLE.read_text()
print(data)
print(type(data))

# Read first N characters
print(SAMPLE.read_text()[:17])

# Read line by line
with SAMPLE.open("r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1)
    print(line2)

# Writing to files (overwrites)
SAMPLE.write_text("Overwriting the file with help of write_text\n")

# Append to file
with SAMPLE.open("a") as f:
    f.write("With the help of 'a' modifier we can append and then write the file\n")

# Create and append to Sample2 (missing file will be created)
with SAMPLE2.open("a") as f:
    f.write("With the help of 'a' and 'w' modifiers we can directly create a file too\n")

# Open with r+ (read + write). Use try/except to be safe.
try:
    with SAMPLE2.open("r+") as f:
        f.write("With the help of r+ modifier we can overwrite the file\n")
except FileNotFoundError:
    # create file then write
    SAMPLE2.write_text("With the help of r+ modifier we can overwrite the file\n")

# Using context manager for read
with SAMPLE.open("r") as f:
    data = f.read()
    print(data)

# Append new data
with SAMPLE.open("a") as f:
    f.write("New data\n")

# Deleting a file (safe)
try:
    SAMPLE2.unlink()
except FileNotFoundError:
    pass

# Practice file creation
PRACTICE.write_text("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java\n")

# Replace occurrences of Java with Python
data = PRACTICE.read_text()
new_data = data.replace("Java", "Python")
PRACTICE.write_text(new_data)

# Search if the word "learning" exists in the file or not
word = "learning"
data = PRACTICE.read_text()
print("FOUND" if word in data else "NOT FOUND")

# WAF to find in which line of the file does the word "learning" occur first.
# Print -1 if word not found
def check_for_line():
    word = "learning"
    line_no = 1
    with PRACTICE.open("r") as f:
        for line in f:
            if word in line:
                print(line_no)
                return line_no
            line_no += 1
    print(-1)
    return -1
