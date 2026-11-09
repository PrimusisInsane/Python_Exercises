"""Setup check: run this first to confirm Python works on your machine.

Analogy: Like checking the oven heats up before you start baking: a quick test now saves
confusion later.

Run:
    python examples/00_setup_check.py

You should see your Python version and a short welcome message.
If you see an error instead, ask for help before moving on.
"""

import platform
import sys

print("Python is working.")
print("Version :", platform.python_version())
print("Running :", sys.executable)

if sys.version_info < (3, 10):
    print("Please install Python 3.10 or newer for this session.")
else:
    print("You are ready for the session.")
