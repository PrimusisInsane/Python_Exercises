"""Data structures: storing many values together.

Analogy: Data structures are ways of packing many things together: a list is a numbered
shopping list you can edit, a tuple is a printed receipt that cannot change, a
dictionary is a phone book that looks things up by name, and a set is a guest list where
nobody appears twice.

Slide: Data Structures
Run:
    python examples/08_data_structures.py

    list   ordered, changeable                ["apple", "banana"]
    tuple  ordered, cannot be changed         (51.5, -0.12)
    dict   key-value pairs                    {"name": "Alice"}
    set    unique items, no order             {"red", "green"}

Try it yourself:
    1. Print the last two fruits using a negative slice.
    2. Add the line  london[0] = 0  at the end. Read the error, then explain why tuples exist.

Practise next: exercises/ex04_data_structures.py
"""

print("--- 1. A list (the slide's example) ---")
fruits = ["apple", "banana", "cherry"]
print("Whole list :", fruits)
print("First item :", fruits[0])
print("Last item  :", fruits[-1])
print("First two  :", fruits[0:2])
print("Length     :", len(fruits))

print("\n--- 2. Slicing: [start:stop:step], stop is not included ---")
letters = ["a", "b", "c", "d", "e", "f"]
print("letters[1:4]  :", letters[1:4])
print("letters[:3]   :", letters[:3])
print("letters[3:]   :", letters[3:])
print("letters[::2]  :", letters[::2])
print("letters[::-1] :", letters[::-1])

print("\n--- 3. A tuple: fixed data ---")
london = (51.5072, -0.1276)
latitude, longitude = london
print("Latitude :", latitude)
print("Longitude:", longitude)

print("\n--- 4. A dictionary: look up by key ---")
student = {"name": "Alice", "age": 30, "course": "MSc Computer Science"}
print("Name  :", student["name"])
print("Course:", student["course"])

print("\n--- 5. A set: only unique values ---")
registrations = ["ada", "alan", "ada", "grace", "alan"]
unique_students = set(registrations)
print("Registrations  :", len(registrations))
print("Unique students:", len(unique_students), sorted(unique_students))
