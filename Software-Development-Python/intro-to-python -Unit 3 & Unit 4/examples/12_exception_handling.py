"""Exception handling: dealing with errors instead of crashing.

Analogy: try/except is like a safety net under a trapeze artist: you still attempt the
trick, but if something goes wrong the net catches the fall instead of the show ending.

Slide: Exception handling
Run:
    python examples/12_exception_handling.py

    try:          code that might fail
    except Error: what to do if it fails
    else:         runs only if nothing failed
    finally:      always runs

Try it yourself:
    1. In demo_converting_input, add "3.5" to the list. Which except block catches it?
    2. Write a function that raises ValueError if a percentage is above 100.

Practise next: exercises/ex06_exception_handling.py
"""


def demo_zero_division():
    """The slide's example: catch a division by zero."""
    try:
        result = 10 / 0
        print(result)
    except ZeroDivisionError:
        print("Error: Division by zero")


def demo_converting_input():
    """Turn bad user input into a helpful message instead of a crash."""
    for text in ["42", "forty-two", ""]:
        try:
            number = int(text)
        except ValueError:
            print(f"{text!r} is not a whole number")
        else:
            print(f"{text!r} converted to {number}")


def demo_several_errors():
    """Handle different errors in different ways."""
    prices = {"tea": 1.5, "coffee": 2.0}
    for item, quantity in [("tea", 2), ("cake", 1), ("coffee", 0)]:
        try:
            unit_price = prices[item]
            print(f"{item}: {unit_price / quantity:.2f} per unit")
        except KeyError:
            print(f"{item}: not on the menu")
        except ZeroDivisionError:
            print(f"{item}: quantity cannot be zero")


def demo_finally():
    """finally runs whether or not an error happened."""
    try:
        print("Opening connection")
        raise ConnectionError("network unavailable")
    except ConnectionError as error:
        print("Problem:", error)
    finally:
        print("Closing connection")


def withdraw(balance, amount):
    """Return the new balance, raising ValueError if the amount is not allowed."""
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


def demo_raise():
    """Raise your own exceptions when a rule is broken."""
    for amount in [30, 500, -5]:
        try:
            print(f"Withdraw {amount}: new balance {withdraw(100, amount)}")
        except ValueError as error:
            print(f"Withdraw {amount}: refused ({error})")


def main():
    """Run every demo in order."""
    print("--- 1. ZeroDivisionError ---")
    demo_zero_division()
    print("\n--- 2. ValueError and else ---")
    demo_converting_input()
    print("\n--- 3. Handling several errors ---")
    demo_several_errors()
    print("\n--- 4. finally ---")
    demo_finally()
    print("\n--- 5. Raising your own errors ---")
    demo_raise()


if __name__ == "__main__":
    main()
