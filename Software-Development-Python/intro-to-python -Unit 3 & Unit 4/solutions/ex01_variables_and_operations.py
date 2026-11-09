"""Exercise 1: variables and basic operations.

Topics: variables, numbers, strings, arithmetic, round(), len().

This file is a plain script: Python runs it from top to bottom.
How to work:
    1. Find each line that says  = None  and replace None with your own code.
    2. Keep the variable names exactly as they are. check.py looks for them.
    3. Run the file to see your answers:
           python exercises/ex01_variables_and_operations.py
    4. Check your work:
           python check.py ex01
       check.py also tries other starting values, so use the variables,
       not the numbers you can see.

Task 1  Temperature
    Convert celsius into fahrenheit. Formula: celsius x 9 / 5 + 32.

Task 2  Shopping bill
    total_cost is price x quantity, plus VAT at vat_rate (0.2 means 20%).
    Round it to 2 decimal places with round(value, 2).

Task 3  Hours and minutes
    Split total_minutes into whole hours and the minutes left over.
    Hint: // gives whole-number division and % gives the remainder.

Task 4  Names
    full_name joins first_name and last_name with a space between them.
    name_length is how many characters full_name has, including the space.
"""

print("--- Task 1: temperature ---")
celsius = 25
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius} C is {fahrenheit} F")

print("\n--- Task 2: shopping bill ---")
price = 10
quantity = 3
vat_rate = 0.2
total_cost = round(price * quantity * (1 + vat_rate), 2)
print(f"{quantity} items at £{price} plus VAT costs £{total_cost}")

print("\n--- Task 3: hours and minutes ---")
total_minutes = 135
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{total_minutes} minutes is {hours} hours and {minutes} minutes")

print("\n--- Task 4: names ---")
first_name = "Grace"
last_name = "Hopper"
full_name = first_name + " " + last_name
name_length = len(full_name)
print(f"{full_name} has {name_length} characters")
