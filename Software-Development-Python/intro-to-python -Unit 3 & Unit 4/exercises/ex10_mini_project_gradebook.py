"""Exercise 10 (mini project): a gradebook that uses everything from the session.

Read data/students.csv, work out each student's grade band, and write a report.
Check your work:
    python check.py ex10
Then run it for real:
    python exercises/ex10_mini_project_gradebook.py
"""

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def grade_band(score: int) -> str:
    """Return "Distinction" (70+), "Merit" (60+), "Pass" (40+) or "Fail"."""
    if score >= 70:
        return "Distinction"
    if score >= 60:
        return "Merit"
    if score >= 40:
        return "Pass"
    return "Fail"


def read_students(path: str) -> list[dict]:
    """Read the CSV file and return a list of dictionaries.

    Each dictionary has the keys name, course and score, with score as an int.

    Example:
        read_students("data/students.csv")[0] -> {"name": "Ada", "course": "Software Development", "score": 78}
    """
    students = []
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            students.append({"name": row["name"], "course": row["course"], "score": int(row["score"])})
    return students


def class_average(students: list[dict]) -> float:
    """Return the average score of all students, rounded to 1 decimal place."""
    return round(sum(student["score"] for student in students) / len(students), 1)


def band_counts(students: list[dict]) -> dict[str, int]:
    """Return how many students are in each grade band.

    Only include bands that at least one student is in.

    Example:
        {"Distinction": 3, "Merit": 1, "Pass": 1, "Fail": 1}
    """
    counts: dict[str, int] = {}
    for student in students:
        band = grade_band(student["score"])
        counts[band] = counts.get(band, 0) + 1
    return counts


def write_report(students: list[dict], path: str) -> int:
    """Write a CSV report with columns name, score, band, highest score first.

    Return the number of students written.
    """
    ordered = sorted(students, key=lambda student: student["score"], reverse=True)
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "score", "band"])
        for student in ordered:
            writer.writerow([student["name"], student["score"], grade_band(student["score"])])
    return len(ordered)


def main() -> None:
    """Run the gradebook on data/students.csv and print a summary."""
    students = read_students(str(DATA_DIR / "students.csv"))
    print(f"Students     : {len(students)}")
    print(f"Class average: {class_average(students)}")
    for band, count in band_counts(students).items():
        print(f"  {band:<12} {count}")
    output = DATA_DIR / "output" / "report.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    written = write_report(students, str(output))
    print(f"Report with {written} students written to {output}")


if __name__ == "__main__":
    main()
