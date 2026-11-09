"""Exercise 4: data structures.

Topics: lists, indexing, slicing, tuples, dictionaries, sets.

This file is a plain script: Python runs it from top to bottom.
How to work:
    1. Find each line that says  = None  and replace None with your own code.
    2. Keep the variable names exactly as they are. check.py looks for them.
    3. Run the file:   python exercises/ex04_data_structures.py
    4. Check your work: python check.py ex04

Task 1  Lists
    first_fruit is the first item of fruits and last_fruit is the last item.
    middle_three is a slice holding the 2nd, 3rd and 4th items.
    Hint: positions start at 0, and fruits[-1] is the last item.

Task 2  Tuples
    location is a tuple of (latitude, longitude).
    Unpack it into latitude and longitude in one line, replacing both
    = None  lines. Hint: a, b = some_tuple

Task 3  Dictionaries
    student_course is the value stored under the "course" key of student.
    age_next_year is the student's age plus 1.

Task 4  Sets
    registrations has some names more than once.
    unique_count is how many different names it contains. Hint: set().
"""

print("--- Task 1: lists ---")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
first_fruit = fruits[0]
last_fruit = fruits[-1]
middle_three = fruits[1:4]
print(f"First: {first_fruit}, last: {last_fruit}, middle: {middle_three}")

print("\n--- Task 2: tuples ---")
location = (51.5074, -0.1278)
latitude, longitude = location
print(f"Latitude {latitude}, longitude {longitude}")

print("\n--- Task 3: dictionaries ---")
student = {"name": "Ada", "age": 21, "course": "Software Development"}
student_course = student["course"]
age_next_year = student["age"] + 1
print(f"{student['name']} studies {student_course} and will be {age_next_year} next year")

print("\n--- Task 4: sets ---")
registrations = ["Ada", "Alan", "Ada", "Grace", "Alan", "Linus"]
unique_count = len(set(registrations))
print(f"{len(registrations)} registrations from {unique_count} different students")
