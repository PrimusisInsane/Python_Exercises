"""Introduction to functions: parameters, return values and abstraction.

Analogy: Abstraction is like driving a car: you use the steering wheel and pedals (the
function name and parameters) without needing to know how the engine (the code inside)
works.

Slide: Introduction to Functions
Run:
    python examples/17_functions_in_depth.py

Type hints such as  radius: float  and  -> float  describe what a function
expects and returns. Python does not enforce them, but they make code easier to
read and let your editor warn you about mistakes.

Abstraction means hiding the details behind a good name. Once
calculate_area works, you can use it without thinking about the formula.

Try it yourself:
    1. Write calculate_circumference(radius) and use it in describe_circle.
    2. Call calculate_area with a negative radius. What should happen? Make it raise ValueError.
"""

import math


def calculate_area(radius: float) -> float:
    """The slide's example: return the area of a circle using 3.14 for pi."""
    return 3.14 * radius**2


def calculate_area_precise(radius: float) -> float:
    """Return the area of a circle using math.pi for better accuracy."""
    return math.pi * radius**2


def describe_circle(radius: float) -> str:
    """Build on calculate_area_precise: functions can call other functions."""
    area = calculate_area_precise(radius)
    return f"A circle with radius {radius} has an area of {area:.2f}"


def average(numbers: list[float]) -> float:
    """Return the mean of a list of numbers, raising ValueError if it is empty."""
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return sum(numbers) / len(numbers)


def apply_discount(price: float, percent: float = 10) -> float:
    """Return the price after a percentage discount (10% by default)."""
    return round(price * (1 - percent / 100), 2)


def demo_scope() -> None:
    """Variables created inside a function only exist inside it."""
    message = "I live inside demo_scope"
    print(message)


def main() -> None:
    """Call each function and show the results."""
    print("--- 1. The slide's example ---")
    print("calculate_area(5)         =", calculate_area(5))
    print("calculate_area_precise(5) =", round(calculate_area_precise(5), 2))
    print("\n--- 2. Functions that use other functions ---")
    print(describe_circle(3))
    print("\n--- 3. Validating inputs ---")
    print("average([70, 80, 90]) =", average([70, 80, 90]))
    try:
        average([])
    except ValueError as error:
        print("average([]) raised:", error)
    print("\n--- 4. Default parameters ---")
    print("apply_discount(50)     =", apply_discount(50))
    print("apply_discount(50, 25) =", apply_discount(50, 25))
    print("\n--- 5. Scope ---")
    demo_scope()
    print("\n--- 6. Reading a docstring ---")
    print(calculate_area.__doc__)


if __name__ == "__main__":
    main()
