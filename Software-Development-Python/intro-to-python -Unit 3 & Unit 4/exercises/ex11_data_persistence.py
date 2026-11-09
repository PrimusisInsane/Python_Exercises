"""Exercise 11: data persistence.

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
    raise NotImplementedError("Write your code here")


def save_settings(path, settings):
    """Save the dictionary settings to the file at path as JSON.

    Example:
        save_settings("settings.json", {"theme": "dark", "font_size": 14})
    """
    raise NotImplementedError("Write your code here")


def load_settings(path):
    """Load and return the JSON dictionary saved at path.

    Return an empty dictionary {} if the file does not exist.

    Example:
        load_settings("settings.json") -> {"theme": "dark", "font_size": 14}
        load_settings("missing.json")  -> {}
    """
    raise NotImplementedError("Write your code here")


def save_object(path, value):
    """Save any Python value to the file at path with pickle.

    Remember: pickle files are opened in binary mode, "wb".
    """
    raise NotImplementedError("Write your code here")


def load_object(path):
    """Load and return the Python value saved with pickle at path.

    Remember: open the file in binary mode, "rb".

    Example:
        save_object("data.pkl", {"tags": {"a", "b"}, "point": (1, 2)})
        load_object("data.pkl") -> {"tags": {"a", "b"}, "point": (1, 2)}
    """
    raise NotImplementedError("Write your code here")


def record_visit(path):
    """Add one to the visit count stored in the file at path, and return the new count.

    If the file does not exist yet, this is the first visit: save 1 and return 1.
    The count must survive between runs, so it lives in the file, not in a variable.

    Example:
        record_visit("visits.txt") -> 1
        record_visit("visits.txt") -> 2
    """
    raise NotImplementedError("Write your code here")
