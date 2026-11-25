"""A tiny calculator - the "app" our GitHub Actions workflow will test.

The code is deliberately simple. The lesson is about the automation
around the code, not the code itself.
"""


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a * b."""
    return a * b


def divide(a, b):
    """Return a / b. Dividing by zero raises a ValueError."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
