"""Variables and memory: a variable is a name that points to a value in memory.

Analogy: A variable is like a luggage tag tied to a suitcase. The suitcase (the value)
sits somewhere in memory; the tag (the name) only points to it. Two tags can hang on the
same suitcase, and moving a tag to another suitcase does not change the first one.

Slide: Variables and Memory
Run:
    python examples/20_variables_and_memory.py

Key ideas:
    id(value)   a number that identifies where a value lives in memory
    a is b      True when a and b point to the very same value
    Mutable     can be changed in place: list, dict, set
    Immutable   can never be changed, only replaced: int, float, str, bool, tuple

The id numbers and sizes printed below will be different on your computer. Compare
them with each other, not with anyone else's screen.

Try it yourself:
    1. In part 4, change  copy = basket  to  copy = basket.copy()  and run again.
       Why is the original basket safe now?
    2. Predict what  print(x is y)  shows after  x = 1000  and  y = 1000.0.  Check it.

Practise next: exercises/ex11_data_persistence.py
"""

import sys


def demo_names_point_to_values():
    """Two names can point to the same value in memory."""
    x = 10
    y = x
    print("x =", x, " y =", y)
    print("id(x):", id(x))
    print("id(y):", id(y))
    print("Same place in memory?", x is y)


def demo_reassigning():
    """Giving a name a new value moves the name; the old value is untouched."""
    x = 10
    y = x
    x = 20
    print("After x = 20:  x =", x, " y =", y)
    print("Same place in memory now?", x is y)


def demo_changing_type():
    """One name can point to values of different types; memory is allocated to fit."""
    value = 42
    print(f"value = {value!r:<20} type: {type(value).__name__:<5} size: {sys.getsizeof(value)} bytes")
    value = "forty-two"
    print(f"value = {value!r:<20} type: {type(value).__name__:<5} size: {sys.getsizeof(value)} bytes")
    value = [4, 2]
    print(f"value = {value!r:<20} type: {type(value).__name__:<5} size: {sys.getsizeof(value)} bytes")


def demo_mutable_shared():
    """Changing a mutable value through one name is seen through every name."""
    basket = ["apples", "bread"]
    copy = basket
    copy.append("milk")
    print("copy   :", copy)
    print("basket :", basket)
    print("Same list?", copy is basket)
    safe = basket.copy()
    safe.append("eggs")
    print("After safe = basket.copy() and safe.append('eggs'):")
    print("safe   :", safe)
    print("basket :", basket)


def demo_immutable_strings():
    """Strings never change; methods such as upper() make a new string."""
    name = "ada"
    shout = name.upper()
    print("name  :", name)
    print("shout :", shout)
    print("Same string?", name is shout)


def add_item(items, item):
    """Add item to the list passed in. The caller's list changes too."""
    items.append(item)


def demo_functions_get_references():
    """A function receives a reference to the caller's value, not a copy."""
    shopping = ["tea"]
    add_item(shopping, "sugar")
    print("After add_item(shopping, 'sugar'):", shopping)


def main():
    """Run every demo in order."""
    print("--- 1. Two names, one value ---")
    demo_names_point_to_values()
    print("\n--- 2. Reassigning moves the name ---")
    demo_reassigning()
    print("\n--- 3. One name, different types ---")
    demo_changing_type()
    print("\n--- 4. Mutable values are shared ---")
    demo_mutable_shared()
    print("\n--- 5. Immutable values are replaced, never changed ---")
    demo_immutable_strings()
    print("\n--- 6. Functions receive references ---")
    demo_functions_get_references()


if __name__ == "__main__":
    main()
