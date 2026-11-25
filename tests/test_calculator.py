"""Automated tests for app/calculator.py.

GitHub Actions will run these on every push. If any test fails,
the workflow run turns red.
"""

import pytest

from app.calculator import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(1, 0)
