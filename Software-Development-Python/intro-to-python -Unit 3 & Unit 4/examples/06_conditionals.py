"""Conditional statements: making decisions with if, elif and else.

Analogy: An if statement is like a satnav at a junction: it checks a condition and takes
exactly one road, trying each turn (if, elif) in order and falling back to else when
none match.

Slide: Conditional Statements
Run:
    python examples/06_conditionals.py

Comparison operators: ==  !=  <  >  <=  >=
Logical operators   : and  or  not

Try it yourself:
    1. Change age to 12 and run again. Then try exactly 18.
    2. Change score in part 2 to 39, 40, 60 and 70. Predict each band before running.

Practise next: exercises/ex02_conditionals.py
"""

print("--- 1. if / else (the slide's example) ---")
age = 21
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

print("\n--- 2. if / elif / else ---")
score = 65
if score >= 70:
    band = "Distinction"
elif score >= 60:
    band = "Merit"
elif score >= 40:
    band = "Pass"
else:
    band = "Fail"
print(f"Score {score}: {band}")

print("\n--- 3. Comparisons give True or False ---")
a = 10
b = 20
print("a == b :", a == b)
print("a != b :", a != b)
print("a < b  :", a < b)
print("a >= b :", a >= b)

print("\n--- 4. Combining conditions ---")
has_ticket = True
is_member = False
age = 16
print("Can enter (ticket and 18+)    :", has_ticket and age >= 18)
print("Gets discount (member or <18) :", is_member or age < 18)
print("Needs to register (not member):", not is_member)

print("\n--- 5. A one-line if ---")
stock = 0
message = "In stock" if stock > 0 else "Out of stock"
print(message)
