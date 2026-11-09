"""Bonus: decorators, the example shown on the Syntax and Data Types slides.

Analogy: A decorator is like gift wrapping: the present inside (the original function)
is unchanged, but the wrapping adds something extra every time it is handed over.

Run:
    python examples/19_bonus_decorators.py

A decorator wraps a function to change what it does, without editing the
function itself. It is written with the @ symbol above the function.
This is a more advanced topic: come back to it once functions feel comfortable.

Try it yourself:
    1. Write an exclaim decorator that adds "!!!" to the end of the result.
    2. Stack both decorators on greet. Does the order matter?
"""

import time
from collections.abc import Callable


def uppercase_decorator(func: Callable[[str], str]) -> Callable[[str], str]:
    """The slide's example: make any text-returning function shout."""

    def wrapper(text: str) -> str:
        """Call the original function, then convert its result to upper case."""
        result = func(text)
        return result.upper()

    return wrapper


@uppercase_decorator
def greet(name: str) -> str:
    """Return a greeting. The decorator turns it into upper case."""
    return "Hello, " + name + "!"


def timer(func: Callable) -> Callable:
    """A practical decorator: report how long a function takes to run."""

    def wrapper(*args, **kwargs):
        """Time the call to the original function."""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f} seconds")
        return result

    return wrapper


@timer
def add_up_to(n: int) -> int:
    """Return the sum of 1 to n, the slow way."""
    total = 0
    for number in range(1, n + 1):
        total += number
    return total


def main() -> None:
    """Show both decorators in action."""
    print("--- 1. The slide's uppercase decorator ---")
    print(greet("Alice"))
    print("\n--- 2. A timing decorator ---")
    print("Result:", add_up_to(1_000_000))


if __name__ == "__main__":
    main()
