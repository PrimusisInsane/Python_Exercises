"""Loops: repeating code with for and while.

Analogy: A for loop is like a teacher calling a register, going through each name once,
while a while loop is like stirring a sauce until it thickens: you keep going for as
long as the condition holds.

Slide: Loops
Run:
    python examples/07_loops.py

for   repeats once for each item in a sequence.
while repeats as long as a condition stays True.

Try it yourself:
    1. Print the 7 times table from 7 x 1 to 7 x 12.
    2. Change the countdown in part 4 so it starts at 10.

Practise next: exercises/ex03_loops.py
"""

print("--- 1. for with range(5) (the slide's example) ---")
for i in range(5):
    print(i)

print("\n--- 2. range(start, stop, step) ---")
for i in range(1, 6):
    print(i, end=" ")
print()
for i in range(0, 20, 5):
    print(i, end=" ")
print()
for i in range(5, 0, -1):
    print(i, end=" ")
print()

print("\n--- 3. Looping over text ---")
for letter in "Python":
    print(letter, end=" ")
print()

print("\n--- 4. A while loop ---")
countdown = 5
while countdown > 0:
    print(countdown, end=" ")
    countdown -= 1
print("Lift off!")

print("\n--- 5. break and continue ---")
for number in range(1, 10):
    if number == 7:
        print("Found 7, stopping.")
        break
    if number % 2 == 0:
        continue
    print("Odd number:", number)

print("\n--- 6. Building a running total ---")
total = 0
for number in range(1, 11):
    total += number
print("Sum of 1 to 10:", total)
