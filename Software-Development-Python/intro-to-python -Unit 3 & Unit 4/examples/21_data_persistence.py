"""Data persistence: keeping data after the program stops.

Analogy: Variables are like writing on a whiteboard: wiped clean when the lesson ends.
Persistence is like writing in a notebook you take home: it is still there next time.
Plain text is a handwritten note, JSON is a form anyone can read, and pickle is a
sealed box that only Python knows how to open.

Slides: Data Persistence, File I/O, Reading from a File, Writing to a File,
        Data Serialization, JSON
Run:
    python examples/21_data_persistence.py
    python examples/21_data_persistence.py
    (run it twice and watch part 1 change)

Reading methods:
    file.read()        the whole file as one string
    file.readline()    the next single line, including its "\\n"
    file.readlines()   every line, as a list of strings

Serialization means turning a Python value into something that can be saved or sent:
    json     text, readable by people and by almost any language; basic types only
    pickle   bytes, Python only; keeps tuples, sets and your own classes
    Never load a pickle file from someone you do not trust: loading it can run code.

Try it yourself:
    1. Run the file three times. Where is the run count kept between runs?
    2. Add "graduated": False to the student in parts 4 and 5. Open student.json in
       data/output: how is False written in JSON?

Practise next: exercises/ex11_data_persistence.py
"""

import json
import pickle
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data" / "output"


def demo_survives_between_runs():
    """Read a number from a file, add one, and save it: it survives the program ending."""
    path = OUTPUT_DIR / "run_count.txt"
    count = 0
    if path.exists():
        with open(path, encoding="utf-8") as file:
            count = int(file.read())
    count += 1
    with open(path, "w", encoding="utf-8") as file:
        file.write(str(count))
    print(f"This program has been run {count} time(s). Run it again!")


def demo_open_and_close():
    """Open, write and close a file by hand, then do the same with 'with'."""
    path = OUTPUT_DIR / "modules.txt"
    file = open(path, "w", encoding="utf-8")
    file.write("Software Development\n")
    file.write("Data Security\n")
    file.write("AI Orchestration\n")
    file.close()
    print("Closed by hand?   ", file.closed)
    with open(path, "a", encoding="utf-8") as file:
        file.write("Cyber Hygiene\n")
    print("Closed by 'with'? ", file.closed)


def demo_reading_methods():
    """Compare read(), readline() and readlines() on the same file."""
    path = OUTPUT_DIR / "modules.txt"
    with open(path, encoding="utf-8") as file:
        print("read()      :", repr(file.read()))
    with open(path, encoding="utf-8") as file:
        print("readline()  :", repr(file.readline()))
        print("readline()  :", repr(file.readline()))
    with open(path, encoding="utf-8") as file:
        print("readlines() :", file.readlines())


def demo_pickle():
    """Save Python values with pickle and load them back, types and all."""
    path = OUTPUT_DIR / "student.pkl"
    student = {"name": "Grace", "scores": (91, 88), "modules": {"Python", "SQL"}}
    with open(path, "wb") as file:
        pickle.dump(student, file)
    with open(path, "rb") as file:
        loaded = pickle.load(file)
    print("Saved  :", student)
    print("Loaded :", loaded)
    print("Identical?", loaded == student)
    print("scores is still a", type(loaded["scores"]).__name__, "and modules is still a", type(loaded["modules"]).__name__)


def demo_json():
    """Save the same kind of data as JSON: readable text, but only basic types."""
    path = OUTPUT_DIR / "student.json"
    student = {"name": "Grace", "scores": (91, 88), "modules": {"Python", "SQL"}}
    try:
        json.dumps(student)
    except TypeError as error:
        print("JSON cannot save a set:", error)
    student["modules"] = sorted(student["modules"])
    with open(path, "w", encoding="utf-8") as file:
        json.dump(student, file, indent=2)
    with open(path, encoding="utf-8") as file:
        loaded = json.load(file)
    print("Loaded :", loaded)
    print("scores came back as a", type(loaded["scores"]).__name__, "not a tuple")


def demo_compare_files():
    """Look inside both files: JSON is text, pickle is bytes."""
    print("student.json starts:", repr((OUTPUT_DIR / "student.json").read_text(encoding="utf-8")[:40]))
    print("student.pkl starts :", (OUTPUT_DIR / "student.pkl").read_bytes()[:20])


def main():
    """Run every demo in order."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print("--- 1. Data that survives the program ending ---")
    demo_survives_between_runs()
    print("\n--- 2. open(), write() and close() ---")
    demo_open_and_close()
    print("\n--- 3. read(), readline() and readlines() ---")
    demo_reading_methods()
    print("\n--- 4. Serialization with pickle ---")
    demo_pickle()
    print("\n--- 5. Serialization with JSON ---")
    demo_json()
    print("\n--- 6. JSON is text, pickle is bytes ---")
    demo_compare_files()
    print(f"\nFiles written to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
