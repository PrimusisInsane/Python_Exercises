"""Introduction to lists: an ordered collection you can change.

Analogy: A list is like a train of numbered carriages starting at carriage 0: you can
look inside any carriage, swap its contents, add carriages to the end or uncouple one
you no longer need.

Slide: Introduction to Lists
Run:
    python examples/14_lists.py

Useful list methods:
    append(x)  insert(i, x)  remove(x)  pop()  sort()  reverse()  index(x)  count(x)

Try it yourself:
    1. Start with an empty shopping list, add three items, remove one, print the rest.
    2. What is the difference between numbers.sort() and sorted(numbers)? Test it.
"""


def demo_create_and_access():
    """The slide's example: create a list and read from it."""
    numbers = [1, 2, 3, 4, 5]
    print("numbers      :", numbers)
    print("numbers[0]   :", numbers[0])
    print("numbers[-1]  :", numbers[-1])
    print("numbers[1:3] :", numbers[1:3])
    print("len(numbers) :", len(numbers))


def demo_adding_items():
    """append adds to the end; insert adds at a position."""
    numbers = [1, 2, 3, 4, 5]
    numbers.append(6)
    print("After append(6)   :", numbers)
    numbers.insert(0, 0)
    print("After insert(0, 0):", numbers)
    numbers.extend([7, 8])
    print("After extend([7,8]):", numbers)


def demo_removing_items():
    """remove deletes by value; pop deletes by position and returns the item."""
    modules = ["Python", "Databases", "Networks", "Security"]
    modules.remove("Networks")
    print("After remove('Networks'):", modules)
    last = modules.pop()
    print("pop() returned          :", last)
    print("List is now             :", modules)


def demo_changing_items():
    """Lists are mutable: you can replace items in place."""
    scores = [55, 62, 70]
    scores[1] = 65
    print("After scores[1] = 65:", scores)


def demo_sorting_and_searching():
    """Sort, search and count items."""
    scores = [72, 45, 88, 61, 88]
    print("sorted(scores)        :", sorted(scores))
    print("Original unchanged    :", scores)
    scores.sort(reverse=True)
    print("After sort(reverse)   :", scores)
    print("Is 61 in the list?    :", 61 in scores)
    print("How many 88s?         :", scores.count(88))
    print("Position of first 88  :", scores.index(88))


def demo_copying():
    """Assignment does not copy a list; use copy() for an independent list."""
    original = [1, 2, 3]
    same_list = original
    real_copy = original.copy()
    original.append(4)
    print("original :", original)
    print("same_list:", same_list)
    print("real_copy:", real_copy)


def main():
    """Run every demo in order."""
    print("--- 1. Creating and accessing ---")
    demo_create_and_access()
    print("\n--- 2. Adding items ---")
    demo_adding_items()
    print("\n--- 3. Removing items ---")
    demo_removing_items()
    print("\n--- 4. Changing items ---")
    demo_changing_items()
    print("\n--- 5. Sorting and searching ---")
    demo_sorting_and_searching()
    print("\n--- 6. Copying a list ---")
    demo_copying()


if __name__ == "__main__":
    main()
