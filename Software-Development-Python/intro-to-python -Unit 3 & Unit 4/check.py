"""Check your exercise answers.

Run from the intro-to-python folder:
    python check.py              check every exercise
    python check.py ex03         check one exercise
    python check.py --solutions  check the model solutions instead

Each check prints PASS, FAIL (with what was expected) or TODO (not started yet).

Exercises 1 to 4 are plain scripts. check.py runs them several times, each time
with different starting values, and reads the variables your code creates.
Exercises 5 to 11 use functions. check.py imports them and calls each function.
"""

import ast
import importlib.util
import json
import math
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parent
USE_COLOUR = sys.stdout.isatty()
GREEN, RED, YELLOW, BOLD, RESET = (
    ("\033[32m", "\033[31m", "\033[33m", "\033[1m", "\033[0m") if USE_COLOUR else ("", "", "", "", "")
)
MARKER = "@@CHECK_RESULTS@@"
MISSING = "@@MISSING@@"
TIME_LIMIT = 3


class NotStarted(Exception):
    """Raised when an answer still contains the starter placeholder."""


class ScriptError(Exception):
    """Raised when a script exercise crashes, runs too long or loses a variable."""


def load(folder: str, name: str) -> ModuleType:
    """Import an exercise file by its path."""
    path = ROOT / folder / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def call(func: Callable, *args, **kwargs):
    """Call a student's function, turning the starter placeholder into NotStarted."""
    try:
        return func(*args, **kwargs)
    except NotImplementedError as error:
        raise NotStarted from error


def same(expected, got) -> bool:
    """Compare two answers, allowing tiny rounding differences in floats."""
    if isinstance(expected, bool):
        return got is expected
    if isinstance(expected, float) and isinstance(got, (int, float)) and not isinstance(got, bool):
        return math.isclose(expected, got, abs_tol=1e-9)
    return expected == got


def equals(expected, func: Callable, *args, **kwargs) -> tuple[bool, str]:
    """Check that a call returns the expected value."""
    got = call(func, *args, **kwargs)
    return same(expected, got), f"expected {expected!r}, got {got!r}"


def raises(error: type[Exception], func: Callable, *args, **kwargs) -> tuple[bool, str]:
    """Check that a call raises the expected error."""
    try:
        got = call(func, *args, **kwargs)
    except NotStarted:
        raise
    except error:
        return True, ""
    except Exception as other:
        return False, f"expected {error.__name__}, got {type(other).__name__}"
    return False, f"expected {error.__name__}, but it returned {got!r}"


class Script:
    """A script-style exercise that can be re-run with different starting values."""

    def __init__(self, path: Path) -> None:
        """Read and parse the script, so syntax errors are reported straight away."""
        self.path = path
        self.source = path.read_text(encoding="utf-8")
        self.tree = ast.parse(self.source, filename=str(path))
        self.cache: dict[str, dict] = {}
        self.hung = False

    def with_inputs(self, inputs: dict) -> str:
        """Return the source with the first top-level assignment of each input replaced."""
        lines = self.source.splitlines()
        found: dict[str, ast.expr] = {}
        for node in self.tree.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
                if name in inputs and name not in found:
                    found[name] = node.value
        lost = [name for name in inputs if name not in found]
        if lost:
            raise ScriptError(f"could not find the starting variable {lost[0]!r}; keep the given lines")
        for name, value in sorted(found.items(), key=lambda item: (item[1].lineno, item[1].col_offset), reverse=True):
            if value.lineno != value.end_lineno:
                raise ScriptError(f"keep the starting value of {name!r} on one line")
            row = value.lineno - 1
            text = lines[row]
            lines[row] = text[: value.col_offset] + repr(inputs[name]) + text[value.end_col_offset :]
        return "\n".join(lines)

    def results(self, inputs: dict, names: list[str]) -> dict:
        """Run the script with the given inputs and return the named variables."""
        key = repr((sorted(inputs.items()), names))
        if self.hung:
            raise ScriptError("skipped: the script got stuck in a loop on an earlier check")
        if key not in self.cache:
            reporter = f"\nprint({MARKER!r} + repr({{n: globals().get(n, {MISSING!r}) for n in {names!r}}}))\n"
            code = self.with_inputs(inputs) + reporter
            try:
                done = subprocess.run(
                    [sys.executable, "-c", code], capture_output=True, text=True,
                    timeout=TIME_LIMIT, cwd=self.path.parent, encoding="utf-8",
                )
            except subprocess.TimeoutExpired as error:
                self.hung = True
                raise ScriptError("took too long: is there a loop that never stops?") from error
            if MARKER not in done.stdout:
                raise ScriptError(crash_message(done.stderr))
            text = done.stdout.split(MARKER)[-1].strip()
            try:
                self.cache[key] = ast.literal_eval(text)
            except (ValueError, SyntaxError):
                self.cache[key] = {"__raw__": text}
        return self.cache[key]


def crash_message(stderr: str) -> str:
    """Summarise a crash as the error and its line number."""
    lines = stderr.strip().splitlines() or ["the script stopped early"]
    where = [line for line in lines if line.strip().startswith('File "<string>", line ')]
    if not where:
        return lines[-1]
    number = where[-1].split("line ")[1].split(",")[0]
    return f"{lines[-1]} on line {number}. The script stops there, so fix that first"


def short(value) -> str:
    """Return repr(value), shortened for long lists."""
    text = repr(value)
    return text if len(text) <= 50 else text[:40] + " ... " + text[-8:]


def script_check(script: Script, inputs: dict, expected: dict) -> Callable:
    """Build a check that runs the script with inputs and compares result variables."""

    def check() -> tuple[bool, str]:
        """Run the script and compare each expected variable."""
        got = script.results(inputs, list(expected))
        if "__raw__" in got:
            raise ScriptError(f"could not read the results: {got['__raw__'][:80]}")
        missing = [name for name in expected if got.get(name) == MISSING]
        if missing:
            raise ScriptError(f"the variable {missing[0]!r} no longer exists; keep the given names")
        if any(got[name] is None for name in expected):
            raise NotStarted
        wrong = [name for name in expected if not same(expected[name], got[name])]
        if wrong:
            name = wrong[0]
            return False, f"{name}: expected {short(expected[name])}, got {short(got[name])}"
        return True, ""

    return check


def label_for(inputs: dict, expected: dict) -> str:
    """Describe a script check, for example: celsius = 0  ->  fahrenheit == 32.0."""
    given = ", ".join(f"{k} = {short(v)}" for k, v in inputs.items()) or "starting values"
    wanted = ", ".join(f"{k} == {short(v)}" for k, v in expected.items())
    return f"{given}  ->  {wanted}"


def script_checks(script: Script, cases: list[tuple[dict, dict]]) -> list[tuple[str, Callable]]:
    """Turn (inputs, expected) pairs into labelled checks."""
    return [(label_for(inputs, expected), script_check(script, inputs, expected)) for inputs, expected in cases]


def checks_ex01(s: Script) -> list[tuple[str, Callable]]:
    """Checks for exercise 1."""
    return script_checks(s, [
        ({}, {"fahrenheit": 77.0}),
        ({"celsius": 0}, {"fahrenheit": 32.0}),
        ({"celsius": -40}, {"fahrenheit": -40.0}),
        ({}, {"total_cost": 36.0}),
        ({"price": 4.99, "quantity": 2, "vat_rate": 0}, {"total_cost": 9.98}),
        ({"price": 2.5, "quantity": 4, "vat_rate": 0.2}, {"total_cost": 12.0}),
        ({}, {"hours": 2, "minutes": 15}),
        ({"total_minutes": 45}, {"hours": 0, "minutes": 45}),
        ({"total_minutes": 600}, {"hours": 10, "minutes": 0}),
        ({}, {"full_name": "Grace Hopper", "name_length": 12}),
        ({"first_name": "Alan", "last_name": "Turing"}, {"full_name": "Alan Turing", "name_length": 11}),
    ])


def checks_ex02(s: Script) -> list[tuple[str, Callable]]:
    """Checks for exercise 2."""
    bands = [(72, "Distinction"), (100, "Distinction"), (60, "Merit"), (40, "Pass"),
             (39, "Fail"), (0, "Fail"), (101, "Invalid"), (-5, "Invalid")]
    years = [(2024, True), (1900, False), (2000, True), (2023, False)]
    tickets = [(3, False, 0.0), (12, True, 5.0), (70, False, 6.0), (25, True, 7.5), (25, False, 10.0)]
    return script_checks(s, (
        [({"score": score}, {"band": band}) for score, band in bands]
        + [({"year": year}, {"is_leap": leap}) for year, leap in years]
        + [({"age": age, "is_student": student}, {"ticket_price": price}) for age, student, price in tickets]
    ))


def checks_ex03(s: Script) -> list[tuple[str, Callable]]:
    """Checks for exercise 3."""
    return script_checks(s, [
        ({}, {"total": 55}),
        ({"n": 1}, {"total": 1}),
        ({"n": 100}, {"total": 5050}),
        ({"table_number": 3}, {"table_lines": [f"3 x {i} = {3 * i}" for i in range(1, 13)]}),
        ({"table_number": 9}, {"table_lines": [f"9 x {i} = {9 * i}" for i in range(1, 13)]}),
        ({}, {"vowel_count": 7}),
        ({"text": "EDUCATION"}, {"vowel_count": 5}),
        ({"text": "rhythm"}, {"vowel_count": 0}),
        ({"fizz_limit": 5}, {"fizzbuzz": ["1", "2", "Fizz", "4", "Buzz"]}),
        ({"fizz_limit": 15}, {"fizzbuzz": ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
                                           "11", "Fizz", "13", "14", "FizzBuzz"]}),
        ({}, {"years": 9}),
        ({"balance": 100, "rate": 0.1, "target": 200}, {"years": 8}),
        ({"balance": 500, "target": 500}, {"years": 0}),
    ])


def checks_ex04(s: Script) -> list[tuple[str, Callable]]:
    """Checks for exercise 4."""
    return script_checks(s, [
        ({}, {"first_fruit": "apple", "last_fruit": "elderberry", "middle_three": ["banana", "cherry", "date"]}),
        ({"fruits": ["a", "b", "c", "d", "e", "f"]}, {"first_fruit": "a", "last_fruit": "f", "middle_three": ["b", "c", "d"]}),
        ({}, {"latitude": 51.5074, "longitude": -0.1278}),
        ({"location": (40.7128, -74.006)}, {"latitude": 40.7128, "longitude": -74.006}),
        ({}, {"student_course": "Software Development", "age_next_year": 22}),
        ({"student": {"name": "Linus", "age": 30, "course": "Data Science"}}, {"student_course": "Data Science", "age_next_year": 31}),
        ({}, {"unique_count": 4}),
        ({"registrations": ["Tim", "Tim", "Tim"]}, {"unique_count": 1}),
    ])


def checks_ex05(m: ModuleType) -> list[tuple[str, Callable]]:
    """Checks for exercise 5."""
    return [
        ("greet('Ada') == 'Hello, Ada!'", lambda: equals("Hello, Ada!", m.greet, "Ada")),
        ("greet('Linus') == 'Hello, Linus!'", lambda: equals("Hello, Linus!", m.greet, "Linus")),
        ("celsius_to_fahrenheit(0) == 32.0", lambda: equals(32.0, m.celsius_to_fahrenheit, 0)),
        ("celsius_to_fahrenheit(100) == 212.0", lambda: equals(212.0, m.celsius_to_fahrenheit, 100)),
        ("is_even(4) is True", lambda: equals(True, m.is_even, 4)),
        ("is_even(7) is False", lambda: equals(False, m.is_even, 7)),
        ("total_cost(10, 3) == 36.0", lambda: equals(36.0, m.total_cost, 10, 3)),
        ("total_cost(4.99, 2, 0) == 9.98", lambda: equals(9.98, m.total_cost, 4.99, 2, 0)),
        ("grade_band(72) == 'Distinction'", lambda: equals("Distinction", m.grade_band, 72)),
        ("grade_band(60) == 'Merit'", lambda: equals("Merit", m.grade_band, 60)),
        ("grade_band(40) == 'Pass'", lambda: equals("Pass", m.grade_band, 40)),
        ("grade_band(39) == 'Fail'", lambda: equals("Fail", m.grade_band, 39)),
        ("grade_band(101) == 'Invalid'", lambda: equals("Invalid", m.grade_band, 101)),
        ("describe_result('Grace', 91)", lambda: equals("Grace scored 91: Distinction", m.describe_result, "Grace", 91)),
        ("describe_result('Tim', 38)", lambda: equals("Tim scored 38: Fail", m.describe_result, "Tim", 38)),
    ]


def checks_ex06(m: ModuleType) -> list[tuple[str, Callable]]:
    """Checks for exercise 6."""
    return [
        ("safe_divide(10, 4) == 2.5", lambda: equals(2.5, m.safe_divide, 10, 4)),
        ("safe_divide(10, 0) is None", lambda: equals(None, m.safe_divide, 10, 0)),
        ("parse_age(' 21 ') == 21", lambda: equals(21, m.parse_age, " 21 ")),
        ("parse_age('abc') raises ValueError", lambda: raises(ValueError, m.parse_age, "abc")),
        ("parse_age('-4') raises ValueError", lambda: raises(ValueError, m.parse_age, "-4")),
        ("parse_age('200') raises ValueError", lambda: raises(ValueError, m.parse_age, "200")),
        ("percentage(18, 24) == 75.0", lambda: equals(75.0, m.percentage, 18, 24)),
        ("percentage(1, 3) == 33.3", lambda: equals(33.3, m.percentage, 1, 3)),
        ("percentage(5, 0) raises ValueError", lambda: raises(ValueError, m.percentage, 5, 0)),
    ]


def checks_ex07(m: ModuleType) -> list[tuple[str, Callable]]:
    """Checks for exercise 7, using a temporary folder."""
    tmp = Path(tempfile.mkdtemp())
    todo = str(tmp / "todo.txt")

    def save_then_count() -> tuple[bool, str]:
        """Save two lines, then count them."""
        call(m.save_lines, todo, ["Install Python", "Run the examples"])
        return equals(2, m.count_lines, todo)

    def save_replaces() -> tuple[bool, str]:
        """Saving again should replace the file, not add to it."""
        call(m.save_lines, todo, ["One", "Two", "Three"])
        call(m.save_lines, todo, ["Only line"])
        return equals(1, m.count_lines, todo)

    csv_path = str(ROOT / "data" / "students.csv")
    return [
        ("save_lines then count_lines == 2", save_then_count),
        ("save_lines replaces the old file", save_replaces),
        ("count_lines on a missing file == 0", lambda: equals(0, m.count_lines, str(tmp / "missing.txt"))),
        ("load_scores(students.csv)['Grace'] == 91", lambda: equals(91, lambda: call(m.load_scores, csv_path)["Grace"])),
        ("load_scores returns 6 students", lambda: equals(6, lambda: len(call(m.load_scores, csv_path)))),
    ]


def checks_ex08(m: ModuleType) -> list[tuple[str, Callable]]:
    """Checks for exercise 8."""
    return [
        ("average([70, 80, 90]) == 80.0", lambda: equals(80.0, m.average, [70, 80, 90])),
        ("average([1, 2]) == 1.5", lambda: equals(1.5, m.average, [1, 2])),
        ("average([]) raises ValueError", lambda: raises(ValueError, m.average, [])),
        ("passing_scores([78, 35, 40, 12]) == [78, 40]", lambda: equals([78, 40], m.passing_scores, [78, 35, 40, 12])),
        ("passing_scores([50, 65], pass_mark=60) == [65]", lambda: equals([65], m.passing_scores, [50, 65], pass_mark=60)),
        ("word_frequencies('the cat and The dog')", lambda: equals({"the": 2, "cat": 1, "and": 1, "dog": 1}, m.word_frequencies, "the cat and The dog")),
        ("top_student({'Ada': 78, 'Grace': 91, 'Alan': 64}) == 'Grace'", lambda: equals("Grace", m.top_student, {"Ada": 78, "Grace": 91, "Alan": 64})),
    ]


def checks_ex09(m: ModuleType) -> list[tuple[str, Callable]]:
    """Checks for exercise 9."""

    def account(balance: float = 100):
        """Create a fresh account for each check."""
        return call(m.BankAccount, "Ada", balance)

    def deposit_then_balance() -> tuple[bool, str]:
        """Deposit 50 into 100."""
        a = account()
        call(a.deposit, 50)
        return equals(150, lambda: a.balance)

    def withdraw_then_balance() -> tuple[bool, str]:
        """Withdraw 30 from 100."""
        a = account()
        call(a.withdraw, 30)
        return equals(70, lambda: a.balance)

    return [
        ("Rectangle(3, 4).area() == 12", lambda: equals(12, lambda: call(call(m.Rectangle, 3, 4).area))),
        ("Rectangle(3, 4).perimeter() == 14", lambda: equals(14, lambda: call(call(m.Rectangle, 3, 4).perimeter))),
        ("Rectangle(3, 4).is_square() is False", lambda: equals(False, lambda: call(call(m.Rectangle, 3, 4).is_square))),
        ("Rectangle(5, 5).is_square() is True", lambda: equals(True, lambda: call(call(m.Rectangle, 5, 5).is_square))),
        ("deposit(50) into 100 gives 150", deposit_then_balance),
        ("withdraw(30) from 100 gives 70", withdraw_then_balance),
        ("deposit(0) raises ValueError", lambda: raises(ValueError, account().deposit, 0)),
        ("withdraw(500) from 100 raises ValueError", lambda: raises(ValueError, account().withdraw, 500)),
        ("str(BankAccount('Ada', 150)) == 'Ada: £150.00'", lambda: equals("Ada: £150.00", lambda: str(account(150)))),
    ]


def checks_ex10(m: ModuleType) -> list[tuple[str, Callable]]:
    """Checks for exercise 10."""
    csv_path = str(ROOT / "data" / "students.csv")
    report = str(Path(tempfile.mkdtemp()) / "report.csv")

    def students() -> list[dict]:
        """Load the students with the student's own function."""
        return call(m.read_students, csv_path)

    def report_first_line() -> tuple[bool, str]:
        """The report should list the top scorer first."""
        call(m.write_report, students(), report)
        with open(report, encoding="utf-8") as file:
            lines = file.read().splitlines()
        return equals("Grace,91,Distinction", lambda: lines[1])

    return [
        ("grade_band(65) == 'Merit'", lambda: equals("Merit", m.grade_band, 65)),
        ("read_students returns 6 students", lambda: equals(6, lambda: len(students()))),
        ("first student is Ada with score 78 (an int)", lambda: equals({"name": "Ada", "course": "Software Development", "score": 78}, lambda: students()[0])),
        ("class_average == 68.2", lambda: equals(68.2, lambda: call(m.class_average, students()))),
        ("band_counts", lambda: equals({"Distinction": 3, "Merit": 1, "Pass": 1, "Fail": 1}, lambda: call(m.band_counts, students()))),
        ("write_report returns 6", lambda: equals(6, lambda: call(m.write_report, students(), report))),
        ("report lists Grace first", report_first_line),
    ]


def checks_ex11(m: ModuleType) -> list[tuple[str, Callable]]:
    """Checks for exercise 11, using a temporary folder."""
    tmp = Path(tempfile.mkdtemp())

    def first_line() -> tuple[bool, str]:
        """The first line comes back without its newline."""
        path = tmp / "names.txt"
        path.write_text("Ada\nGrace\n", encoding="utf-8")
        return equals("Ada", m.read_first_line, str(path))

    def settings_round_trip() -> tuple[bool, str]:
        """Settings saved as JSON load back the same."""
        path = str(tmp / "settings.json")
        settings = {"theme": "dark", "font_size": 14, "languages": ["Python", "SQL"]}
        call(m.save_settings, path, settings)
        return equals(settings, m.load_settings, path)

    def settings_are_json() -> tuple[bool, str]:
        """The settings file is real JSON text that anyone can read."""
        path = tmp / "check.json"
        call(m.save_settings, str(path), {"theme": "light"})
        got = json.loads(path.read_text(encoding="utf-8"))
        return got == {"theme": "light"}, f"expected the file to contain JSON for {{'theme': 'light'}}, got {got!r}"

    def object_round_trip() -> tuple[bool, str]:
        """A set and a tuple survive pickle unchanged."""
        path = str(tmp / "data.pkl")
        value = {"tags": {"a", "b"}, "point": (1, 2)}
        call(m.save_object, path, value)
        return equals(value, m.load_object, path)

    def visits_count_up() -> tuple[bool, str]:
        """Three visits give 1, 2 and 3."""
        path = str(tmp / "visits.txt")
        got = [call(m.record_visit, path) for _ in range(3)]
        return got == [1, 2, 3], f"expected [1, 2, 3], got {got!r}"

    def visits_survive() -> tuple[bool, str]:
        """The count is stored in the file, not in a variable."""
        path = tmp / "stored.txt"
        call(m.record_visit, str(path))
        call(m.record_visit, str(path))
        got = path.read_text(encoding="utf-8").strip() if path.exists() else None
        return got == "2", f"expected the file to contain '2', got {got!r}"

    return [
        ("read_first_line gives 'Ada' without the newline", first_line),
        ("read_first_line on a missing file == ''", lambda: equals("", m.read_first_line, str(tmp / "missing.txt"))),
        ("save_settings then load_settings gives the same dict", settings_round_trip),
        ("save_settings writes real JSON", settings_are_json),
        ("load_settings on a missing file == {}", lambda: equals({}, m.load_settings, str(tmp / "missing.json"))),
        ("save_object then load_object keeps a set and a tuple", object_round_trip),
        ("record_visit three times gives 1, 2, 3", visits_count_up),
        ("record_visit keeps the count in the file", visits_survive),
    ]


SCRIPT_EXERCISES = {
    "ex01_variables_and_operations": checks_ex01,
    "ex02_conditionals": checks_ex02,
    "ex03_loops": checks_ex03,
    "ex04_data_structures": checks_ex04,
}
FUNCTION_EXERCISES = {
    "ex05_functions": checks_ex05,
    "ex06_exception_handling": checks_ex06,
    "ex07_file_handling": checks_ex07,
    "ex08_lists_and_dictionaries": checks_ex08,
    "ex09_classes": checks_ex09,
    "ex10_mini_project_gradebook": checks_ex10,
    "ex11_data_persistence": checks_ex11,
}
CHECKS = {**SCRIPT_EXERCISES, **FUNCTION_EXERCISES}


def run(folder: str, name: str) -> tuple[int, int]:
    """Run every check for one exercise and return (passed, total)."""
    print(f"\n{BOLD}{name}{RESET}")
    try:
        if name in SCRIPT_EXERCISES:
            target = Script(ROOT / folder / f"{name}.py")
        else:
            target = load(folder, name)
    except Exception as error:
        print(f"  {RED}Could not load the file: {type(error).__name__}: {error}{RESET}")
        return 0, 0
    checks = CHECKS[name](target)
    passed = 0
    for label, check in checks:
        try:
            ok, detail = check()
        except NotStarted:
            print(f"  {YELLOW}TODO{RESET}  {label}")
            continue
        except ScriptError as error:
            print(f"  {RED}FAIL{RESET}  {label}  ({error})")
            continue
        except Exception as error:
            print(f"  {RED}FAIL{RESET}  {label}  ({type(error).__name__}: {error})")
            continue
        if ok:
            passed += 1
            print(f"  {GREEN}PASS{RESET}  {label}")
        else:
            print(f"  {RED}FAIL{RESET}  {label}  ({detail})")
    print(f"  {passed}/{len(checks)} passed")
    return passed, len(checks)


def main() -> None:
    """Choose which exercises to check, run them and print a total."""
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    folder = "solutions" if "--solutions" in sys.argv else "exercises"
    names = [n for n in CHECKS if not args or any(n.startswith(a) for a in args)]
    if not names:
        print(f"No exercise matches {args}. Try one of: {', '.join(n[:4] for n in CHECKS)}")
        return
    print(f"Checking the {folder} folder")
    total_passed = total = 0
    for name in names:
        passed, count = run(folder, name)
        total_passed += passed
        total += count
    print(f"\n{BOLD}Total: {total_passed}/{total} checks passed{RESET}")


if __name__ == "__main__":
    main()
