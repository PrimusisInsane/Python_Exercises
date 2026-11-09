"""Input and output: talking to the user.

Analogy: Input and output are like a conversation at a shop counter: input() is
listening to what the customer asks, and print() is what you say back.

Slide: Input and Output
Run:
    python examples/11_input_and_output.py

input() always returns text (a str). Convert it if you need a number.
print() and f-strings control how output looks.

Try it yourself:
    1. Ask for the user's favourite programming language and print a sentence with it.
    2. Ask for two numbers and print their total, formatted to two decimal places.
"""

import sys


def ask(prompt, example):
    """Ask the user a question; use the example answer when no keyboard is attached."""
    if not sys.stdin.isatty():
        print(prompt + example)
        return example
    return input(prompt)


def demo_input():
    """The slide's example: read a name and greet the user."""
    name = ask("Enter your name: ", "Ada")
    print("Hello, " + name)


def demo_number_input():
    """Text from input() must be converted before doing maths."""
    year_text = ask("What year were you born? ", "1998")
    year = int(year_text)
    print(f"You will be {2030 - year} in 2030.")


def demo_formatted_output():
    """f-strings put values into text and control their format."""
    module = "Software Development"
    score = 72.456
    students = 32
    print(f"Module : {module}")
    print(f"Score  : {score:.1f}")
    print(f"Ratio  : {18 / 24:.0%}")
    print(f"Cost   : £{1234.5:,.2f}")
    print(f"|{students:>6}|{students:<6}|{students:^6}|")


def demo_print_options():
    """print() can change its separator and line ending."""
    print("2026", "11", "01", sep="-")
    print("Loading", end="")
    print("...done")


def main():
    """Run every demo in order."""
    print("--- 1. Reading text ---")
    demo_input()
    print("\n--- 2. Reading a number ---")
    demo_number_input()
    print("\n--- 3. Formatted output ---")
    demo_formatted_output()
    print("\n--- 4. print options ---")
    demo_print_options()


if __name__ == "__main__":
    main()
