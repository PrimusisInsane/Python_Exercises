"""Modules and libraries: using code that someone else has already written.

Analogy: A module is like borrowing a book from a library: rather than writing the
knowledge yourself, you import it and use what someone else has already written and
tested.

Slide: Modules and Libraries
Run:
    python examples/10_modules_and_libraries.py

Built-in modules come with Python (math, random, datetime, statistics ...).
External libraries are installed with pip, for example:
    pip install requests

From this file on, examples are organised the way real programs are: each idea
is a small function, and a main() function runs them in order. The last two lines,

    if __name__ == "__main__":
        main()

mean "run main() only when this file is run directly, not when it is imported".
That is why importing calculator_tools does not run anything by itself.

Try it yourself:
    1. Use math.ceil to work out how many 4-seat tables 30 people need.
    2. Look up one more function in the statistics module and use it on the scores.
"""

import math
import random
import statistics
from datetime import datetime, timedelta

import calculator_tools as tools


def demo_import_module():
    """The slide's example: import a module, then use its functions."""
    square_root = math.sqrt(25)
    print("math.sqrt(25)  =", square_root)
    print("math.pi        =", round(math.pi, 5))
    print("math.ceil(4.2) =", math.ceil(4.2))


def demo_from_import():
    """Import only the names you need with from ... import."""
    now = datetime.now()
    deadline = now + timedelta(days=7)
    print("Today        :", now.strftime("%d %B %Y"))
    print("Due in 7 days:", deadline.strftime("%A %d %B"))


def demo_random():
    """random picks values; seed() makes the picks repeatable."""
    random.seed(42)
    students = ["Ada", "Alan", "Grace", "Linus", "Margaret"]
    print("Random student :", random.choice(students))
    print("Dice roll      :", random.randint(1, 6))


def demo_statistics():
    """statistics summarises numbers without writing the maths yourself."""
    scores = [72, 65, 88, 91, 54, 77]
    print("Mean  :", round(statistics.mean(scores), 2))
    print("Median:", statistics.median(scores))


def demo_own_module():
    """Your own .py file is a module too: import it like any other."""
    print("tools.add(2, 3)          =", tools.add(2, 3))
    print("tools.percentage(18, 24) =", tools.percentage(18, 24))


def main():
    """Run every demo in order."""
    print("--- 1. import math ---")
    demo_import_module()
    print("\n--- 2. from datetime import ... ---")
    demo_from_import()
    print("\n--- 3. random ---")
    demo_random()
    print("\n--- 4. statistics ---")
    demo_statistics()
    print("\n--- 5. Importing your own module ---")
    demo_own_module()


if __name__ == "__main__":
    main()
