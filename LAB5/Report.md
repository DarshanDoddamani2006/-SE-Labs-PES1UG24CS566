# Lab 5 – Static Code Analysis

## Repository Information

**Student Repository:**  
https://github.com/DarshanDoddamani2006/-SE-Labs-PES1UG24CS566/tree/main/LAB5
**Original / Forked Repository:**  
https://github.com/DarshanDoddamani2006/L5_17_society_dues

> This repository was forked from the assigned Software Engineering Lab repository and modified as part of Lab 5 – Static Code Analysis.

---

## Objective

The objective of this lab is to improve the **code quality, security, style, and maintainability** of the assigned Python program using static code analysis tools.

The following tools were used:

- **Pylint** – Code quality and programming-practice analysis
- **Bandit** – Security vulnerability analysis
- **Flake8** – Python style and formatting analysis

---

## Original Program

The original program was a **Society Dues Ledger** implemented in Python using SQLite.

The program provides functionality to:

- Add society dues for flats
- Collect dues
- Calculate penalties
- Display pending dues
- Store dues information using SQLite

---

## Issues Identified

Static analysis of the original program identified several issues.

| Issue | Tool | Type | Solution |
|---|---|---|---|
| Missing module docstring | Pylint | Code Quality | Added a module-level docstring |
| Mutable default argument `history=[]` | Pylint | Code Quality / Bug Risk | Changed the default value to `None` and initialized the list inside the function |
| Function name `addDue` | Pylint | Style | Renamed it to `add_due` to follow snake_case |
| Unsafe SQL string construction | Bandit | Security | Replaced string interpolation with parameterized SQL queries |
| Use of `eval()` | Bandit / Pylint | Security | Replaced `eval()` with restricted AST-based arithmetic evaluation |
| Broad `Exception` handling | Pylint | Code Quality | Replaced it with specific exception types |
| Incorrect `None` comparison | Pylint | Style | Changed the comparison to `is not None` |
| Missing function docstrings | Pylint | Code Quality | Added documentation strings to functions |
| Long lines | Flake8 / Pylint | Style | Split long statements into multiple lines |
| Trailing whitespace | Flake8 | Style | Removed unnecessary whitespace |
| Missing newline at end of file | Flake8 | Style | Added a newline at the end of the file |

---

## How the Issues Were Solved

### 1. Mutable Default Argument

### Original

```python
def addDue(flat, month, amount, history=[]):
