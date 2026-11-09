"""Functions: reusable blocks of code.

Analogy: A function is like a kettle: you give it something (water, the parameter), it
does its job out of sight, and it hands something back (hot water, the return value), as
many times as you need.

Slide: Functions
Run:
    python examples/09_functions.py

So far every file ran from top to bottom, once. A function lets you write some
code once, give it a name, and run it whenever you need it.

    def name(parameters):
        body
        return result

Defining a function does not run it. The code inside only runs when you call it.

Try it yourself:
    1. Write a function farewell(name) that returns "Goodbye, <name>!" and call it twice.
    2. Call greet() with no argument. Read the error, then give name a default value.

Practise next: exercises/ex05_functions.py
"""


def greet(name):
    """The slide's example: return a greeting for the given name."""
    return "Hello, " + name + "!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def describe_student(name, course="Software Development"):
    """Return a sentence about a student; course has a default value."""
    return f"{name} studies {course}."


def min_max(numbers):
    """Return the smallest and largest numbers as a pair."""
    return min(numbers), max(numbers)


def print_banner(text):
    """Print text inside a banner. This function does not return anything."""
    print("*" * (len(text) + 4))
    print(f"* {text} *")
    print("*" * (len(text) + 4))


print("--- 1. Calling a function (the slide's example) ---")
print(greet("Alice"))
print(greet("Bob"))

print("\n--- 2. Using the result ---")
message = greet("Grace")
print("The function gave back:", message)
print("In capitals:", message.upper())

print("\n--- 3. Several parameters ---")
print("add(3, 4) =", add(3, 4))
total = add(add(1, 2), 3)
print("add(add(1, 2), 3) =", total)

print("\n--- 4. Default and keyword arguments ---")
print(describe_student("Ada"))
print(describe_student("Alan", course="Data Science"))
print(describe_student(course="Cyber Security", name="Grace"))

print("\n--- 5. Returning two values ---")
lowest, highest = min_max([7, 3, 9, 1])
print("Lowest:", lowest, "Highest:", highest)

print("\n--- 6. return versus print ---")
result = print_banner("Functions")
print("print_banner returned:", result)
