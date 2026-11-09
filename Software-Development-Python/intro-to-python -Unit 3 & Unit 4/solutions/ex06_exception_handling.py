"""Exercise 6: exception handling.

Topics: try/except, catching specific errors, raising your own errors.
Check your work:
    python check.py ex06
"""


def safe_divide(a, b):
    """Return a divided by b, or None if b is zero. Use try/except.

    Examples:
        safe_divide(10, 4) -> 2.5
        safe_divide(10, 0) -> None
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def parse_age(text):
    """Turn text typed by a user into an age.

    Ignore spaces around the number. Raise ValueError if the text is not a
    whole number, or if the age is below 0 or above 130.

    Examples:
        parse_age(" 21 ") -> 21
        parse_age("abc")  -> raises ValueError
        parse_age("-4")   -> raises ValueError
    """
    age = int(text.strip())
    if age < 0 or age > 130:
        raise ValueError(f"Age out of range: {age}")
    return age


def percentage(part, whole):
    """Return part as a percentage of whole, rounded to 1 decimal place.

    Raise ValueError if whole is zero or negative.

    Examples:
        percentage(18, 24) -> 75.0
        percentage(1, 3)   -> 33.3
    """
    if whole <= 0:
        raise ValueError("whole must be greater than zero")
    return round(part / whole * 100, 1)
