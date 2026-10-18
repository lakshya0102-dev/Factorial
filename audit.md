# README.md Claims Audit

Based on the provided `factorial.py` code, each claim in the README is audited below.

| # | README Claim | Status | Evidence from the Code |
|---|---|---|---|
| 1 | The repository contains beginner-level Python programs. | Not Supported | Only `factorial.py` has been provided; the complete repository contents are unknown. |
| 2 | `factorial.py` demonstrates factorial calculation. | Supported | Both `factorial()` and `factorial_recursive()` calculate factorials. |
| 3 | Factorial is the product of positive integers from 1 to n. | Supported | The iterative function multiplies integers using `range(1, n + 1)`, while the recursive function multiplies `n` by `factorial_recursive(n - 1)`. |
| 4 | `5! = 120`, `3! = 6`, and `0! = 1`. | Supported | These results follow from the multiplication logic and the base case returning `1` for 0 and 1. |
| 5 | Python must be installed to run the program. | Supported | The file uses Python syntax and requires a Python interpreter. |
| 6 | The `factorial.py` file must be available locally. | Supported | The script must be accessible at the specified file path when executed. |
| 7 | No additional library requirements are specified. | Supported | The code uses built-in Python functionality and contains no external imports. |
| 8 | Run using `python factorial.py`. | Supported | This command works when Python is installed, `python` is the correct interpreter command, and the terminal is in the appropriate directory. |
| 9 | Run using `python3 factorial.py`. | Supported | This command works when `python3` is the available interpreter command. |
| 10 | The program displays instructions for user input. | Supported | The code prompts the user with `Enter a non-negative integer:`. |
| 11 | The program teaches the mathematical concept of factorial. | Supported | Both functions explicitly calculate factorials. |
| 12 | The program demonstrates solving mathematical problems using Python. | Supported | It uses multiplication, loops, recursion, and integer input to calculate factorials. |
| 13 | The program teaches how to execute Python scripts from a terminal. | Not Supported | Terminal execution is a usage instruction, not a behavior demonstrated by the code itself. |
| 14 | The program helps learners develop familiarity with Python. | Not Supported | This is a general educational objective and cannot be verified directly from the code. |
| 15 | The exact programming concepts depend on the implementation. | Supported | The code uses functions, type annotations, conditional statements, loops, recursion, input conversion, and formatted output. |
| 16 | The repository contains only `factorial.py`. | Not Supported | The provided code confirms the existence of this file but does not establish the complete repository structure. |
| 17 | The repository is intended for beginner-level Python practice. | Not Supported | The code may be suitable for beginners, but the repository's intended audience is not established by the code. |

## Additional Verified Behavior

- **Two implementations:** `factorial()` calculates factorials iteratively, while `factorial_recursive()` uses recursion.
- **Negative inputs:** Both functions raise a `ValueError` for negative integers.
- **User input:** The program reads input using `input()` and converts it to an integer using `int()`.
- **Two results:** The main block prints the factorial calculated by both functions.
- **Base cases:** Both functions return `1` for inputs of `0` and `1`.
- **Invalid input:** Non-integer input causes `int()` to raise a `ValueError`, which the program does not explicitly handle.

## Conclusion

The README is broadly accurate about factorial calculation and program execution. However, claims about the complete repository structure and its intended educational purpose cannot be verified from the supplied code. The most notable omission is that the program provides both iterative and recursive factorial implementations.