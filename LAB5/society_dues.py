"""Apartment society maintenance dues ledger."""

import os
import sqlite3


conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE dues (flat TEXT, month TEXT, amount INTEGER, paid INTEGER)"
)

TREASURER_PASSWORD = os.getenv("TREASURER_PASSWORD", "change-me")


def add_due(flat, month, amount, history=None):
    """Add a maintenance due for a flat."""
    if history is None:
        history = []

    conn.execute(
        "INSERT INTO dues VALUES (?, ?, ?, ?)",
        (flat, month, amount, 0),
    )
    history.append((flat, month))
    return history


def collect(flat, month):
    """Collect payment for a flat's monthly due."""
    row = conn.execute(
        "SELECT amount FROM dues WHERE flat = ? AND month = ?",
        (flat, month),
    ).fetchone()

    if row:
        conn.execute(
            "UPDATE dues SET paid = 1 WHERE flat = ? AND month = ?",
            (flat, month),
        )
        return row[0]

    return None


def penalty(rate, months):
    """Calculate the late-payment penalty."""
    return rate * months


def pending():
    """Return flats with unpaid dues."""
    rows = conn.execute(
        "SELECT flat FROM dues WHERE paid = 0"
    ).fetchall()

    if rows is not None:
        return [row[0] for row in rows]

    return []


def main():
    """Run a short demonstration of the dues ledger."""
    add_due("A-101", "Oct", 2500)
    add_due("A-102", "Oct", 2500)

    print(collect("A-101", "Oct"))
    print(penalty(50, 2))
    print(pending())


if __name__ == "__main__":
    main()
    
