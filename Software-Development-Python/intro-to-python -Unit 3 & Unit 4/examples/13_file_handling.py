"""File handling: reading and writing files safely with 'with'.

Analogy: Opening a file with 'with' is like borrowing a library book that returns
itself: you read or write while you hold it, and it is put back automatically when you
finish.

Slide: File Handling
Run:
    python examples/13_file_handling.py

Modes for open():
    "r" read (default)    "w" write (replaces the file)    "a" append

Files are written to the data/output folder so nothing important is overwritten.

Try it yourself:
    1. Add your own line to notes.txt using append mode, then read the file again.
    2. Add a new student to students.csv in Excel or a text editor and run the file again.

Practise next: exercises/ex07_file_handling.py
"""

import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
OUTPUT_DIR = DATA_DIR / "output"


def demo_write_and_read():
    """Write a text file, then read it back: the slide's example."""
    path = OUTPUT_DIR / "data.txt"
    with open(path, "w", encoding="utf-8") as file:
        file.write("Python makes file handling simple.\n")
        file.write("The with statement closes the file for you.\n")
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    print(content)


def demo_append_and_lines():
    """Append to a file, then read it one line at a time."""
    path = OUTPUT_DIR / "notes.txt"
    with open(path, "w", encoding="utf-8") as file:
        file.write("First note\n")
    with open(path, "a", encoding="utf-8") as file:
        file.write("Second note\n")
        file.write("Third note\n")
    with open(path, encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            print(number, line.strip())


def demo_read_csv():
    """Read a CSV file into dictionaries, one per row."""
    with open(DATA_DIR / "students.csv", newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            print(f"{row['name']:<10} {row['course']:<22} score {row['score']}")


def demo_write_json():
    """Save structured data as JSON and load it back."""
    path = OUTPUT_DIR / "settings.json"
    settings = {"theme": "dark", "font_size": 14, "languages": ["Python", "SQL"]}
    with open(path, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=2)
    with open(path, encoding="utf-8") as file:
        loaded = json.load(file)
    print("Loaded languages:", loaded["languages"])


def demo_missing_file():
    """Opening a file that does not exist raises FileNotFoundError."""
    try:
        with open(DATA_DIR / "missing.txt", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("missing.txt was not found. Check the file name and folder.")


def main():
    """Run every demo in order."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print("--- 1. Write, then read ---")
    demo_write_and_read()
    print("--- 2. Append and read line by line ---")
    demo_append_and_lines()
    print("\n--- 3. Reading a CSV file ---")
    demo_read_csv()
    print("\n--- 4. Writing and reading JSON ---")
    demo_write_json()
    print("\n--- 5. A file that does not exist ---")
    demo_missing_file()
    print(f"\nFiles written to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
