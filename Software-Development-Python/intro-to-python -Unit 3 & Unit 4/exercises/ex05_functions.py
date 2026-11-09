"""Exercise 5: functions.

Topics: def, parameters, default values, return, calling one function from another.

From here on, exercises are written as functions. Several of these tasks are
the same problems you solved as plain scripts in Exercises 1 and 2, so you can
compare the two styles.

How to work:
    1. Each function contains  raise NotImplementedError(...).
       Delete that line and write the body so the function returns the right value.
    2. Read the docstring of each function: it shows example calls and results.
    3. Check your work: python check.py ex05
    4. Try your functions yourself in the Python shell:
           python
           >>> import sys; sys.path.insert(0, "exercises")
           >>> from ex05_functions import greet
           >>> greet("Ada")
"""


def greet(name):
    """Return a greeting for name.

    Example:
        greet("Ada") -> "Hello, Ada!"
    """
    raise NotImplementedError("Write your code here")


def celsius_to_fahrenheit(celsius):
    """Return the temperature in Fahrenheit. Formula: celsius x 9 / 5 + 32.

    Examples:
        celsius_to_fahrenheit(0)   -> 32.0
        celsius_to_fahrenheit(100) -> 212.0
    """
    raise NotImplementedError("Write your code here")


def is_even(number):
    """Return True if number is even, otherwise False.

    Examples:
        is_even(4) -> True
        is_even(7) -> False
    """
    raise NotImplementedError("Write your code here")


def total_cost(price, quantity, vat_rate=0.2):
    """Return price x quantity plus VAT, rounded to 2 decimal places.

    vat_rate has a default value, so callers may leave it out.

    Examples:
        total_cost(10, 3)      -> 36.0
        total_cost(4.99, 2, 0) -> 9.98
    """
    raise NotImplementedError("Write your code here")


def grade_band(score):
    """Return the grade band for a score from 0 to 100.

    "Distinction" (70+), "Merit" (60+), "Pass" (40+), "Fail" (below 40),
    or "Invalid" if the score is below 0 or above 100.

    Examples:
        grade_band(72)  -> "Distinction"
        grade_band(39)  -> "Fail"
        grade_band(101) -> "Invalid"
    """
    raise NotImplementedError("Write your code here")


def describe_result(name, score):
    """Return a sentence about a student's result. Call grade_band to get the band.

    Example:
        describe_result("Grace", 91) -> "Grace scored 91: Distinction"
    """
    raise NotImplementedError("Write your code here")
