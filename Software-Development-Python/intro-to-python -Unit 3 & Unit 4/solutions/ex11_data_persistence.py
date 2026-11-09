"""Exercise 11: data persistence. Model solution.

Topics: open and close, write, readline, JSON, pickle, data that survives between runs.
Check your work:
    python check.py ex11
"""

import json
import pickle


def read_first_line(path):
    """Return the first line of the file at path, without the newline at the end.

    Use readline(). Return "" if the file does not exist.

    Example, for a file containing "Ada\\nGrace\\n":
        read_first_line("names.txt")   -> "Ada"
        read_first_line("missing.txt") -> ""
    """
    try:
        with open(path, encoding="utf-8") as file:
            return file.readline().rstrip("\n")
    except FileNotFoundError:
        return ""


def save_settings(path, settings):
    """Save the dictionary settings to the file at path as JSON.

    Example:
        save_settings("settings.json", {"theme": "dark", "font_size": 14})
    """
    with open(path, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=2)


def load_settings(path):
    """Load and return the JSON dictionary saved at path.

    Return an empty dictionary {} if the file does not exist.

    Example:
        load_settings("settings.json") -> {"theme": "dark", "font_size": 14}
        load_settings("missing.json")  -> {}
    """
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_object(path, value):
    """Save any Python value to the file at path with pickle.

    Remember: pickle files are opened in binary mode, "wb".
    """
    with open(path, "wb") as file:
        pickle.dump(value, file)


def load_object(path):
    """Load and return the Python value saved with pickle at path.

    Remember: open the file in binary mode, "rb".

    Example:
        save_object("data.pkl", {"tags": {"a", "b"}, "point": (1, 2)})
        load_object("data.pkl") -> {"tags": {"a", "b"}, "point": (1, 2)}
    """
    with open(path, "rb") as file:
        return pickle.load(file)


def record_visit(path):
    """Add one to the visit count stored in the file at path, and return the new count.

    If the file does not exist yet, this is the first visit: save 1 and return 1.
    The count must survive between runs, so it lives in the file, not in a variable.

    Example:
        record_visit("visits.txt") -> 1
        record_visit("visits.txt") -> 2
    """
    try:
        with open(path, encoding="utf-8") as file:
            count = int(file.read())
    except FileNotFoundError:
        count = 0
    count += 1
    with open(path, "w", encoding="utf-8") as file:
        file.write(str(count))
    return count
