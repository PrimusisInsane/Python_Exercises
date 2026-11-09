"""Exercise 8: lists and dictionaries.

Topics: list methods, list comprehensions, dictionaries, looping over collections.
Check your work:
    python check.py ex08
"""


def average(numbers):
    """Return the average of a list of numbers, rounded to 1 decimal place.

    Raise ValueError if the list is empty.

    Examples:
        average([70, 80, 90]) -> 80.0
        average([1, 2])       -> 1.5
    """
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return round(sum(numbers) / len(numbers), 1)


def passing_scores(scores, pass_mark=40):
    """Return only the scores at or above the pass mark, in their original order.

    Example:
        passing_scores([78, 35, 40, 12]) -> [78, 40]
    """
    return [score for score in scores if score >= pass_mark]


def word_frequencies(text):
    """Return how many times each word appears, ignoring upper and lower case.

    Example:
        word_frequencies("the cat and The dog") -> {"the": 2, "cat": 1, "and": 1, "dog": 1}
    """
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_student(scores):
    """Return the name of the student with the highest score.

    Example:
        top_student({"Ada": 78, "Grace": 91, "Alan": 64}) -> "Grace"
    """
    best_name = ""
    best_score = -1
    for name, score in scores.items():
        if score > best_score:
            best_name = name
            best_score = score
    return best_name
