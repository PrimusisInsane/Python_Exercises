"""Introduction to classes: object-oriented programming (OOP).

Analogy: A class is like an architect's blueprint for a house: one drawing (the class)
can build many houses (objects), each with its own paint colour (attributes), and every
house has the same working doors and lights (methods).

Slide: Introduction to Classes (OOP)
Run:
    python examples/18_classes_oop.py

    class       a blueprint (Circle)
    object      one thing built from the blueprint (a circle with radius 3)
    attribute   data stored on an object (self.radius)
    method      a function that belongs to the class (area())
    __init__    runs automatically when an object is created

Try it yourself:
    1. Add a diameter() method to Circle.
    2. Create a Rectangle class with width, height and an area() method.

Practise next: exercises/ex09_classes.py, then the mini project
exercises/ex10_mini_project_gradebook.py, which brings the whole session together.
"""

import math


class Circle:
    """The slide's example, extended with methods."""

    def __init__(self, radius: float) -> None:
        """Store the radius when a new circle is created."""
        self.radius = radius

    def area(self) -> float:
        """Return the area of this circle."""
        return math.pi * self.radius**2

    def circumference(self) -> float:
        """Return the distance around this circle."""
        return 2 * math.pi * self.radius

    def __str__(self) -> str:
        """Return a readable description, used by print()."""
        return f"Circle(radius={self.radius})"


class BankAccount:
    """A bank account that protects its balance with rules."""

    def __init__(self, owner: str, balance: float = 0) -> None:
        """Create an account for an owner with an optional opening balance."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Add money to the account."""
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Take money out, refusing if there is not enough."""
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self) -> str:
        """Return a readable summary of the account."""
        return f"{self.owner}'s account: £{self.balance:.2f}"


class SavingsAccount(BankAccount):
    """A bank account that also earns interest: an example of inheritance."""

    def __init__(self, owner: str, balance: float = 0, rate: float = 0.03) -> None:
        """Create a savings account with an interest rate."""
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self) -> None:
        """Add one year of interest to the balance."""
        self.balance += self.balance * self.rate


def demo_circles() -> None:
    """Create several Circle objects from one class."""
    small = Circle(1)
    large = Circle(10)
    for circle in [small, large]:
        print(f"{circle}: area {circle.area():.2f}, circumference {circle.circumference():.2f}")


def demo_bank_account() -> None:
    """Objects keep their own data and enforce their own rules."""
    account = BankAccount("Ada", 100)
    account.deposit(50)
    print(account)
    try:
        account.withdraw(500)
    except ValueError as error:
        print("Withdraw 500 refused:", error)
    account.withdraw(30)
    print(account)


def demo_inheritance() -> None:
    """A SavingsAccount can do everything a BankAccount can, plus more."""
    savings = SavingsAccount("Grace", 1000, rate=0.05)
    savings.deposit(200)
    savings.add_interest()
    print(savings)


def main() -> None:
    """Run every demo in order."""
    print("--- 1. Classes and objects ---")
    demo_circles()
    print("\n--- 2. Methods that protect data ---")
    demo_bank_account()
    print("\n--- 3. Inheritance ---")
    demo_inheritance()


if __name__ == "__main__":
    main()
