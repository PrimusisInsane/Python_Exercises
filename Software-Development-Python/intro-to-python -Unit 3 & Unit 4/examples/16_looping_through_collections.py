"""Introduction to loops over collections, and list comprehensions.

Analogy: A list comprehension is like a production line: every item passes along the
belt, an optional quality check (if) removes the ones you do not want, and each
remaining item is shaped into the new list.

Slide: Introduction to Loops
Run:
    python examples/16_looping_through_collections.py

A list comprehension builds a new list in one line:
    [expression for item in collection if condition]

Try it yourself:
    1. Use a list comprehension to make a list of the cubes of 1 to 5.
    2. Use a comprehension to keep only the names longer than four letters.

Practise next: exercises/ex08_lists_and_dictionaries.py (it covers files 14, 15 and 16)
"""


def demo_loop_list():
    """Loop through a list, item by item."""
    modules = ["Python", "Databases", "Networks"]
    for module in modules:
        print("Module:", module)


def demo_enumerate():
    """enumerate gives the position and the item together."""
    modules = ["Python", "Databases", "Networks"]
    for number, module in enumerate(modules, start=1):
        print(f"{number}. {module}")


def demo_loop_dict():
    """Loop through a dictionary's keys and values with items()."""
    scores = {"Ada": 78, "Alan": 64, "Grace": 91}
    for name, score in scores.items():
        print(f"{name} scored {score}")


def demo_zip():
    """zip walks through two lists side by side."""
    names = ["Ada", "Alan", "Grace"]
    scores = [78, 64, 91]
    for name, score in zip(names, scores):
        print(f"{name}: {score}")


def demo_list_comprehension():
    """The slide's example, then the same result written as a normal loop."""
    squares = [x**2 for x in range(1, 6)]
    print("Comprehension:", squares)
    squares_loop = []
    for x in range(1, 6):
        squares_loop.append(x**2)
    print("Normal loop  :", squares_loop)


def demo_filtering():
    """Add an if to keep only the items you want."""
    scores = [78, 64, 91, 55, 38]
    passed = [score for score in scores if score >= 40]
    print("Passing scores:", passed)
    names = ["ada", "alan", "grace"]
    print("Capitalised   :", [name.capitalize() for name in names])


def demo_dict_comprehension():
    """Comprehensions can build dictionaries too."""
    names = ["Ada", "Alan", "Grace"]
    name_lengths = {name: len(name) for name in names}
    print(name_lengths)


def main():
    """Run every demo in order."""
    print("--- 1. Looping through a list ---")
    demo_loop_list()
    print("\n--- 2. enumerate ---")
    demo_enumerate()
    print("\n--- 3. Looping through a dictionary ---")
    demo_loop_dict()
    print("\n--- 4. zip ---")
    demo_zip()
    print("\n--- 5. List comprehension ---")
    demo_list_comprehension()
    print("\n--- 6. Filtering with a comprehension ---")
    demo_filtering()
    print("\n--- 7. Dictionary comprehension ---")
    demo_dict_comprehension()


if __name__ == "__main__":
    main()
