"""Exercise 7: file handling.

Topics: open, with, reading and writing text and CSV files, FileNotFoundError.
Check your work:
    python check.py ex07
"""

import csv


def save_lines(path, lines):
    """Write each item of lines to the file at path, one per line.

    Replace the file if it already exists.

    Example:
        save_lines("todo.txt", ["Install Python", "Run the examples"])
        creates todo.txt containing two lines.
    """
    with open(path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


def count_lines(path):
    """Return how many lines the file at path contains, or 0 if it does not exist.

    Example:
        count_lines("todo.txt")    -> 2
        count_lines("missing.txt") -> 0
    """
    try:
        with open(path, encoding="utf-8") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0


def load_scores(path):
    """Read a CSV file with columns name, course, score.

    Return a dictionary of name -> score, with each score as an int.

    Example, for data/students.csv:
        load_scores("data/students.csv")["Grace"] -> 91
    """
    scores = {}
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            scores[row["name"]] = int(row["score"])
    return scores
