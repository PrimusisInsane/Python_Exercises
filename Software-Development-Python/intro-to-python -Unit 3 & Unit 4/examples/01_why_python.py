"""Why Python? A quick taste of what a few lines of Python can do.

Analogy: Python is like a Swiss Army knife: one tool that is simple to hold yet handles
web apps, data, automation and AI.

Slide: Why Python?
Run:
    python examples/01_why_python.py

General-purpose, easy to read, a huge standard library, and useful everywhere
from web development to data analysis. Each part below is a small, real task.
Do not worry about understanding every line yet: just notice how little code it takes.

Try it yourself:
    1. Change the sentence in part 1 and run the file again.
    2. Add another score to the list in part 2 and watch the results change.
"""

import statistics
from collections import Counter
from datetime import date

print("--- 1. Counting words ---")
sentence = "python is easy to read and python is easy to write"
counts = Counter(sentence.split())
print("Most common words:", counts.most_common(3))

print("\n--- 2. Quick statistics ---")
scores = [72, 65, 88, 91, 54, 77]
print("Average score:", round(statistics.mean(scores), 1))
print("Highest score:", max(scores))
print("Lowest score :", min(scores))

print("\n--- 3. Working with dates ---")
today = date.today()
end_of_year = date(today.year, 12, 31)
print("Days until 31 December:", (end_of_year - today).days)
