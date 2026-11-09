# Introduction to Python: Practical Session

MSc Computer Science (Software Development) · The University of Law

A hands-on companion to the **Introduction to Python Programming** lecture. Every topic in the slides has a runnable example file, and every group of topics has an exercise you complete and check yourself.

**The rule for today: run it, read it, change it.** Do not just read the code. Run each file, predict what a line will do before you run it, then change something and run it again.

---

## 1. Get set up (5 minutes)

1. Install **Python 3.10 or newer** from [python.org](https://www.python.org/downloads/). On Windows, tick **Add Python to PATH** during installation.
2. Install **Visual Studio Code** from [code.visualstudio.com](https://code.visualstudio.com/) and add the **Python** extension.
3. Open this `intro-to-python` folder in VS Code (**File → Open Folder**).
4. Open a terminal in VS Code (**Terminal → New Terminal**) and run:

   ```
   python examples/00_setup_check.py
   ```

   On macOS or Linux, use `python3` instead of `python` if `python` is not found.

No extra packages are needed. Everything uses Python's standard library.

---

## 2. What is in this folder

```
intro-to-python/
├── README.md              this guide
├── check.py               checks your exercise answers
├── examples/              one runnable file per lecture topic
├── exercises/             your practice files: fill these in
├── solutions/             model answers (try first, then compare)
└── data/
    └── students.csv       sample data used by the file examples
```

### How the session builds up

The files take you on a journey, one idea at a time:

| Stage | Files | What the code looks like |
|---|---|---|
| **1. Plain scripts** | examples 00 to 08, exercises 1 to 4 | Code runs from top to bottom, one line after another. No functions yet. |
| **2. Your first functions** | example 09, exercise 5 | You learn `def`, parameters and `return`, and rewrite earlier problems as functions. |
| **3. Organised programs** | examples 10 to 21, exercises 6 to 11 | Each example groups its ideas into small functions and runs them from `main()`. |

Every example file starts with a **docstring** that gives an everyday **analogy** for the topic, explains it, shows how to run the file, and gives a short **Try it yourself** task. The output is split into numbered parts, such as `--- 3. Slicing ---`, so you can match each part of the output to the code that printed it.

From example 10 onwards you will see this at the bottom of each file:

```python
if __name__ == "__main__":
    main()
```

It means "run `main()` when this file is run directly, but not when another file imports it". Example 10 explains it in detail.

---

## 3. Topics, examples and exercises

Work down this table. Run the example, do its **Try it yourself** task, then do the exercise when you reach it.

| # | Slide | Run this | Then practise |
|---|---|---|---|
| 1 | Why Python? | `python examples/01_why_python.py` | |
| 2 | Python's Syntax | `python examples/02_syntax.py` | |
| 3 | Data Types | `python examples/03_data_types.py` | |
| 4 | Variables and Assignments | `python examples/04_variables_and_assignment.py` | |
| 5 | Basic Operations | `python examples/05_basic_operations.py` | **Exercise 1** |
| 6 | Conditional Statements | `python examples/06_conditionals.py` | **Exercise 2** |
| 7 | Loops | `python examples/07_loops.py` | **Exercise 3** |
| 8 | Data Structures | `python examples/08_data_structures.py` | **Exercise 4** |
| 9 | Functions | `python examples/09_functions.py` | **Exercise 5** |
| 10 | Modules and Libraries | `python examples/10_modules_and_libraries.py` | |
| 11 | Input and Output | `python examples/11_input_and_output.py` | |
| 12 | Exception Handling | `python examples/12_exception_handling.py` | **Exercise 6** |
| 13 | File Handling | `python examples/13_file_handling.py` | **Exercise 7** |
| 14 | Introduction to Lists | `python examples/14_lists.py` | |
| 15 | Introduction to Dictionaries | `python examples/15_dictionaries.py` | |
| 16 | Introduction to Loops (collections) | `python examples/16_looping_through_collections.py` | **Exercise 8** |
| 17 | Introduction to Functions | `python examples/17_functions_in_depth.py` | |
| 18 | Introduction to Classes (OOP) | `python examples/18_classes_oop.py` | **Exercise 9** |
| 19 | Bonus: Decorators | `python examples/19_bonus_decorators.py` | |
| | Put it all together | | **Exercise 10: mini project** |
| 20 | Variables and Memory | `python examples/20_variables_and_memory.py` | |
| 21 | Data Persistence, File I/O, Serialization, JSON | `python examples/21_data_persistence.py` (run it twice) | **Exercise 11** |

---

## 4. The exercises

| Exercise | Style | File | What you build |
|---|---|---|---|
| 1 | Script | `exercises/ex01_variables_and_operations.py` | Temperature converter, bill with VAT, hours and minutes, names |
| 2 | Script | `exercises/ex02_conditionals.py` | Grade bands, leap years, cinema ticket prices |
| 3 | Script | `exercises/ex03_loops.py` | Running total, times table, vowel counter, FizzBuzz, savings goal |
| 4 | Script | `exercises/ex04_data_structures.py` | Indexing and slicing lists, unpacking tuples, dictionaries, sets |
| 5 | Functions | `exercises/ex05_functions.py` | Your first functions, including earlier problems rewritten as functions |
| 6 | Functions | `exercises/ex06_exception_handling.py` | Safe division, checking user input, percentages |
| 7 | Functions | `exercises/ex07_file_handling.py` | Saving, counting and loading files |
| 8 | Functions | `exercises/ex08_lists_and_dictionaries.py` | Averages, filtering, word counts, top student |
| 9 | Classes | `exercises/ex09_classes.py` | A `Rectangle` class and a `BankAccount` class |
| 10 | Mini project | `exercises/ex10_mini_project_gradebook.py` | A gradebook that reads `students.csv` and writes a report |
| 11 | Functions | `exercises/ex11_data_persistence.py` | Reading a first line, saving settings as JSON, pickle, a visit counter that survives between runs |

### Exercises 1 to 4: plain scripts

Each task gives you some starting values and a line ending in `= None`:

```python
celsius = 25
fahrenheit = None
print(f"{celsius} C is {fahrenheit} F")
```

1. Replace `None` with your own code, using the variables rather than the numbers you can see. Some tasks need several lines, such as a loop or an `if` block.
2. Keep the variable names as they are.
3. Run the file to see your answers: `python exercises/ex01_variables_and_operations.py`
4. Check your work: `python check.py ex01`

The checker runs your script several times with **different starting values** (for example `celsius = 0` and `celsius = -40`), so your code must work for any value, not only the one in the file.

### Exercises 5 to 11: functions and classes

1. Open the exercise file. Each function has a docstring that says exactly what it must do, with examples.
2. Replace `raise NotImplementedError("Write your code here")` with your own code.
3. Check your work: `python check.py ex05`

### Reading the checker's output

```
PASS  celsius = 0  ->  fahrenheit == 32.0
FAIL  total_minutes = 45  ->  hours == 0, minutes == 45  (minutes: expected 45, got 0.75)
TODO  starting values  ->  full_name == 'Grace Hopper', name_length == 12
```

**PASS** means it works. **FAIL** tells you what was expected and what your code produced. **TODO** means you have not started that task yet. If your script crashes, the checker tells you the error and the line number: fix that first, because a script stops at the first error.

Fix, save and check again until every line passes. Check everything at once with `python check.py`. When you finish Exercise 10, run it for real with `python exercises/ex10_mini_project_gradebook.py`.

### Stuck?

1. Re-run the matching example file and look for the same idea.
2. Read the error message from the bottom up: the last line tells you what went wrong, and the line above it tells you where.
3. Compare with the file in `solutions/` only after a real attempt.

---

## 5. Habits worth building today

- **Predict, then run.** Before running a line, say what it will print. If you are wrong, you have just learned something.
- **Change one thing at a time.** Then run again.
- **Read error messages.** Python tells you the file, the line and the problem.
- **Name things clearly.** `total_score` beats `ts`.
- **Write a docstring for every function** you create, once you reach file 09. Future you will thank you.

---

## 6. Where to go next

- The official Python tutorial: [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/)
- Watch code run line by line: [pythontutor.com](https://pythontutor.com/visualize.html)
- Practise regularly: a little every day beats a lot once a week.
