"""Python's syntax: how Python code is laid out and read.

Analogy: Python code is like a recipe: steps are followed top to bottom (statements), a
colon is the heading that says "the steps below belong to this", indentation shows which
steps sit under which heading, ingredient names must be spelt exactly (case
sensitivity), and comments are the cook's notes in the margin that the oven never reads.

Slide: Python's Syntax
Run:
    python examples/02_syntax.py

Key rules:
    - Python runs your code from top to bottom, one line at a time.
    - One statement per line; no semicolons needed.
    - Indentation (4 spaces) groups lines into blocks. It is not optional.
    - A colon (:) starts a new block, for example after an if.
    - Names are case sensitive: score and Score are different.
    - Text after a # on a line is a comment and is ignored by Python.
    - Text in triple quotes at the top of a file, like this one, is a docstring.

Try it yourself:
    1. Remove the 4 spaces before one of the indented print lines in part 2 and run it.
       Read the IndentationError message.
    2. Remove the colon after "if temperature > 20" and read the SyntaxError message.
    3. Change print to Print. What does Python say?
"""

print("--- 1. Statements run from top to bottom ---")
print("Python runs this line first.")
print("Then this one.")
print("Then this one.")

print("\n--- 2. Indentation makes a block ---")
temperature = 25
if temperature > 20:
    print("Inside the block: it is warm.")
    print("Still inside the block.")
print("Outside the block: this always runs.")

print("\n--- 3. Case sensitivity ---")
score = 10
Score = 99
print("score =", score)
print("Score =", Score)

print("\n--- 4. Text with single or double quotes ---")
print('Single quotes work.')
print("Double quotes work too.")
print("Use double quotes when the text has an apostrophe: it's easy.")

print("\n--- 5. Splitting a long line inside brackets ---")
total = (
    100
    + 250
    + 75
)
print("Total:", total)
