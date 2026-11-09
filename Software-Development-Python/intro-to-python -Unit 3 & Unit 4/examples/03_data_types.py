"""Data types: the kinds of values Python works with.

Analogy: Data types are like containers in a kitchen: you would not pour soup into a
paper bag, and Python likewise needs to know whether a value is a whole number (int), a
measured amount (float), a label (str) or a yes/no switch (bool) before it knows what it
can do with it.

Slide: Data Types
Run:
    python examples/03_data_types.py

The core types:
    int    whole numbers           42
    float  decimal numbers         3.14   or in exponential form: 1.5e3 (1.5 x 10 to the 3)
    complex  real and imaginary    2 + 3j  (used in science and engineering)
    str    text                    "hello"
    bool   True or False           True
    None   "no value"              None

Try it yourself:
    1. Predict the output of int("7") + 3 and str(7) + "3", then check.
    2. Add the line  print("Age: " + 21)  at the end and run the file.
       Read the TypeError, then fix it with str(21).
    3. Try int("seven"). What error do you get, and why?
    4. Predict what 2.5e-2 prints, then check.
"""

print("--- 1. One value of each type ---")
print(42, "is", type(42))
print(3.14, "is", type(3.14))
print("hello", "is", type("hello"))
print(True, "is", type(True))
print(None, "is", type(None))

print("\n--- 1b. More numbers: exponential form and complex ---")
print("1.5e3 =", 1.5e3, "is", type(1.5e3))
print("2e-4  =", 2e-4, "is", type(2e-4))
z = 2 + 3j
print(z, "is", type(z), " real part:", z.real, " imaginary part:", z.imag)

print("\n--- 2. Converting between types ---")
print('int("7") + 3     =', int("7") + 3)
print('str(7) + "3"     =', str(7) + "3")
print("float(5)         =", float(5))
print("int(9.99)        =", int(9.99))
print('bool("")         =', bool(""))
print('bool("anything") =', bool("anything"))

print("\n--- 3. Checking a type ---")
age = 21
print("Is age an int?", isinstance(age, int))
print("Is age a str? ", isinstance(age, str))

print("\n--- 4. Text and numbers need converting before joining ---")
age = 21
print("Age: " + str(age))
print("Age:", age)
