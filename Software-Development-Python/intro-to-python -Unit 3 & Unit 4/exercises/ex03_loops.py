"""Exercise 3: loops.

Topics: for loops, range(), while loops, building up a result.

This file is a plain script: Python runs it from top to bottom.
How to work:
    1. Find each line that says  = None  and replace it with your own code.
       Most tasks follow the same pattern: start with an empty result
       (0, "" or []) and update it inside a loop.
    2. Keep the variable names exactly as they are. check.py looks for them.
    3. Run the file:   python exercises/ex03_loops.py
    4. Check your work: python check.py ex03

Task 1  Running total
    total is 1 + 2 + ... + n. Use a for loop and range().

Task 2  Times table
    table_lines is a list of 12 strings for table_number, like:
        ["7 x 1 = 7", "7 x 2 = 14", ..., "7 x 12 = 84"]

Task 3  Vowel counter
    vowel_count is how many vowels (a, e, i, o, u) are in text,
    counting upper and lower case.

Task 4  FizzBuzz
    fizzbuzz is a list of strings for the numbers 1 to fizz_limit:
    "Fizz" for multiples of 3, "Buzz" for multiples of 5,
    "FizzBuzz" for multiples of both, otherwise the number as text.
        fizz_limit = 5 -> ["1", "2", "Fizz", "4", "Buzz"]

Task 5  Savings goal
    balance grows by rate (0.05 means 5%) once a year. Use a while loop to
    find years: how many whole years until balance reaches target or more.
"""

print("--- Task 1: running total ---")
n = 10
total = None
print(f"1 + 2 + ... + {n} = {total}")

print("\n--- Task 2: times table ---")
table_number = 7
table_lines = None
print(table_lines)

print("\n--- Task 3: vowel counter ---")
text = "Software Development"
vowel_count = None
print(f"{text!r} has {vowel_count} vowels")

print("\n--- Task 4: FizzBuzz ---")
fizz_limit = 15
fizzbuzz = None
print(fizzbuzz)

print("\n--- Task 5: savings goal ---")
balance = 1000
rate = 0.05
target = 1500
years = None
print(f"It takes {years} years to reach £{target}")
