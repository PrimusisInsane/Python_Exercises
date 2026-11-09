"""A small home-made module, imported by 10_modules_and_libraries.py.

Any .py file can be imported as a module from another file in the same folder.
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def percentage(part, whole):
    """Return part as a percentage of whole, rounded to one decimal place."""
    return round(part / whole * 100, 1)
