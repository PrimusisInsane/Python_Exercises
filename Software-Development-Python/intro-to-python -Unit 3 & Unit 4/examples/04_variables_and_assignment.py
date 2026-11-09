"""Variables and assignment: giving names to values.

Analogy: A variable is like a labelled jar: the label is the name, the contents are the
value, and = means "put this into the jar", replacing whatever was there before.

Slide: Variables and Assignments
Run:
    python examples/04_variables_and_assignment.py

Naming rules:
    - Start with a letter or underscore, then letters, digits or underscores.
    - No spaces and no reserved words (if, for, class ...).
    - Names are case-sensitive: myVar and myvar are two different variables.
    - Use lower_case_with_underscores for variables (PEP 8 style).
    - Use UPPER_CASE for values that should not change (constants).

Try it yourself:
    1. Create variables for your name, age and course, then print a sentence using them.
    2. Swap the values of two variables in one line.
    3. Try naming a variable 2nd_place. What happens?
    4. Add  print(Myvar)  at the end. Read the NameError: why does Python not find it?
"""

print("--- 1. Creating variables (the slide's example) ---")
x = 10
y = 2.5
print("x =", x)
print("y =", y)

print("\n--- 2. Changing a variable's value ---")
score = 50
print("Starting score:", score)
score = 75
print("Updated score :", score)
score = score + 5
print("After adding 5:", score)
score += 5
print("After += 5    :", score)

print("\n--- 3. Several variables at once ---")
name, age, course = "Ada", 28, "Software Development"
print(name, age, course)

print("\n--- 4. Swapping two values ---")
a = 1
b = 2
a, b = b, a
print("a =", a, "b =", b)

print("\n--- 5. Good names describe the value ---")
module_name = "Software Development"
total_students = 32
MAX_GROUP_SIZE = 4
full_groups = total_students // MAX_GROUP_SIZE
print(module_name, "has", total_students, "students in", full_groups, "groups of", MAX_GROUP_SIZE)

print("\n--- 6. f-strings put variables inside text ---")
print(f"{name} is {age} and studies {course}.")

print("\n--- 7. Names are case-sensitive ---")
myVar = "upper V"
myvar = "lower v"
print("myVar =", myVar)
print("myvar =", myvar)
