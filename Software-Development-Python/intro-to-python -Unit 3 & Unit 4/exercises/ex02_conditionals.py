"""Exercise 2: conditionals.

Topics: if, elif, else, comparison operators, and, or, not.

This file is a plain script: Python runs it from top to bottom.
How to work:
    1. Find each line that says  = None  and replace it with your own code.
       You may need several lines, for example an if/elif/else block that
       sets the variable in each branch.
    2. Keep the variable names exactly as they are. check.py looks for them.
    3. Run the file:   python exercises/ex02_conditionals.py
    4. Check your work: python check.py ex02
       Change the starting values yourself too, and run the file again.

Task 1  Grade band
    Set band from score:
        70 to 100  -> "Distinction"
        60 to 69   -> "Merit"
        40 to 59   -> "Pass"
        0 to 39    -> "Fail"
        below 0 or above 100 -> "Invalid"

Task 2  Leap year
    Set is_leap to True or False. A year is a leap year if it divides by 4,
    except century years (divisible by 100), which must also divide by 400.
        2024 -> True    1900 -> False    2000 -> True    2023 -> False

Task 3  Cinema ticket
    Set ticket_price (a float) from age and is_student, checking in this order:
        under 5         -> 0.0
        under 18        -> 5.0
        65 or over      -> 6.0
        a student       -> 7.5
        everyone else   -> 10.0
"""

print("--- Task 1: grade band ---")
score = 72
band = None
print(f"A score of {score} is a {band}")

print("\n--- Task 2: leap year ---")
year = 2024
is_leap = None
print(f"Is {year} a leap year? {is_leap}")

print("\n--- Task 3: cinema ticket ---")
age = 25
is_student = True
ticket_price = None
print(f"Age {age}, student: {is_student}, ticket costs £{ticket_price}")
