"""Basic operations: doing arithmetic and working with text.

Analogy: Python is like a calculator that also understands words: + adds numbers, but
put two pieces of text together with + and it glues them into one.

Slide: Basic Operations
Run:
    python examples/05_basic_operations.py

Arithmetic operators:
    +  add        -  subtract     *  multiply
    /  divide     // whole-number divide
    %  remainder  ** power

Try it yourself:
    1. Work out how many full weeks and leftover days are in 100 days using // and %.
    2. Predict 2 + 3 * 4 and (2 + 3) * 4, then check.

Practise next: exercises/ex01_variables_and_operations.py
"""

print("--- 1. Arithmetic (the slide's example first) ---")
x = 17
y = 5
result = x + y
print(f"{x} + {y}  = {result}")
print(f"{x} - {y}  = {x - y}")
print(f"{x} * {y}  = {x * y}")
print(f"{x} / {y}  = {x / y}")
print(f"{x} // {y} = {x // y}")
print(f"{x} % {y}  = {x % y}")
print(f"{x} ** 2 = {x ** 2}")

print("\n--- 2. Order of operations ---")
print("2 + 3 * 4   =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

print("\n--- 3. Everyday calculations ---")
minutes = 135
print(f"{minutes} minutes = {minutes // 60} h {minutes % 60} min")
number = 14
print(f"Is {number} even? {number % 2 == 0}")
price = 19.99
print(f"Price with 20% VAT: {round(price * 1.2, 2)}")

print("\n--- 4. Operations on text ---")
first = "Software"
second = "Development"
print(first + " " + second)
print("-" * 20)
print("Length of first:", len(first))
print("Upper case     :", first.upper())
