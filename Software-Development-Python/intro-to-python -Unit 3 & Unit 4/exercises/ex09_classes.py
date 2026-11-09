"""Exercise 9: classes and objects.

Topics: class, __init__, attributes, methods, __str__, raising errors.
Check your work:
    python check.py ex09
"""


class Rectangle:
    """A rectangle with a width and a height.

    Example:
        r = Rectangle(3, 4)
        r.area()      -> 12
        r.perimeter() -> 14
        r.is_square() -> False
    """

    def __init__(self, width: float, height: float) -> None:
        """Store the width and height."""
        raise NotImplementedError("Write your code here")

    def area(self) -> float:
        """Return width multiplied by height."""
        raise NotImplementedError("Write your code here")

    def perimeter(self) -> float:
        """Return the total length of all four sides."""
        raise NotImplementedError("Write your code here")

    def is_square(self) -> bool:
        """Return True if the width and height are equal."""
        raise NotImplementedError("Write your code here")


class BankAccount:
    """A bank account with an owner and a balance.

    Rules:
        deposit(amount)  raises ValueError if amount is not positive.
        withdraw(amount) raises ValueError if amount is not positive
                         or is more than the balance.
        str(account)     returns "Ada: £150.00" (two decimal places).

    Example:
        account = BankAccount("Ada", 100)
        account.deposit(50)
        account.balance -> 150
    """

    def __init__(self, owner: str, balance: float = 0) -> None:
        """Store the owner's name and the opening balance."""
        raise NotImplementedError("Write your code here")

    def deposit(self, amount: float) -> None:
        """Add a positive amount to the balance."""
        raise NotImplementedError("Write your code here")

    def withdraw(self, amount: float) -> None:
        """Remove a positive amount that is no more than the balance."""
        raise NotImplementedError("Write your code here")

    def __str__(self) -> str:
        """Return the owner and balance, for example "Ada: £150.00"."""
        raise NotImplementedError("Write your code here")
