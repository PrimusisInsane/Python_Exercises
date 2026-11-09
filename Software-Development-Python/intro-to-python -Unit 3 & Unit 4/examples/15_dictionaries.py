"""Introduction to dictionaries: looking values up by key.

Analogy: A dictionary is like a coat check: you hand over a ticket (the key) and get
back exactly your coat (the value), without searching through every coat on the rail.

Slide: Introduction to Dictionaries
Run:
    python examples/15_dictionaries.py

A dictionary stores key-value pairs: {"key": value}.
Keys are unique; looking up by key is fast.

Try it yourself:
    1. Build a dictionary of three countries and their capitals, then print one capital.
    2. Use .get() to look up a country that is not in your dictionary.
"""


def demo_create_and_access():
    """The slide's example: create a dictionary and read values by key."""
    person = {"name": "Alice", "age": 30}
    print("person         :", person)
    print("person['name'] :", person["name"])
    print("person['age']  :", person["age"])


def demo_add_and_modify():
    """Assigning to a key adds it if new, or changes it if it exists."""
    person = {"name": "Alice", "age": 30}
    person["course"] = "Software Development"
    print("After adding course:", person)
    person["age"] = 31
    print("After changing age :", person)


def demo_safe_lookup():
    """[] fails on a missing key; .get() returns a default instead."""
    person = {"name": "Alice", "age": 30}
    print("person.get('email')            :", person.get("email"))
    print("person.get('email', 'unknown') :", person.get("email", "unknown"))
    try:
        print(person["email"])
    except KeyError as error:
        print("person['email'] raised KeyError:", error)


def demo_remove():
    """Remove a key with pop() or del."""
    stock = {"apples": 10, "pears": 4, "plums": 0}
    removed = stock.pop("plums")
    print("Removed plums with value", removed, "->", stock)
    del stock["pears"]
    print("After del pears ->", stock)


def demo_keys_values_items():
    """Get just the keys, just the values, or both together."""
    scores = {"Ada": 78, "Alan": 64, "Grace": 91}
    print("keys()  :", list(scores.keys()))
    print("values():", list(scores.values()))
    print("items() :", list(scores.items()))
    print("Is 'Ada' a key?", "Ada" in scores)


def demo_nested():
    """Values can be lists or other dictionaries."""
    module = {
        "title": "Software Development",
        "students": ["Ada", "Alan", "Grace"],
        "tutor": {"name": "Dr Smith", "room": "B204"},
    }
    print("Second student:", module["students"][1])
    print("Tutor's room  :", module["tutor"]["room"])


def main():
    """Run every demo in order."""
    print("--- 1. Creating and accessing ---")
    demo_create_and_access()
    print("\n--- 2. Adding and modifying ---")
    demo_add_and_modify()
    print("\n--- 3. Safe lookups with get ---")
    demo_safe_lookup()
    print("\n--- 4. Removing items ---")
    demo_remove()
    print("\n--- 5. keys, values and items ---")
    demo_keys_values_items()
    print("\n--- 6. Nested data ---")
    demo_nested()


if __name__ == "__main__":
    main()
