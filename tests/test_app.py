# tests/test_app.py

import pytest
from caluculator import add_numbers  # Import the add_numbers function

def test_add_positive_numbers():
    assert add_numbers(2, 3) == 5

def test_add_negative_numbers():
    assert add_numbers(-2, -3) == -5

def test_add_mixed_numbers():
    assert add_numbers(-2, 3) == 1

def test_add_with_zero():
    assert add_numbers(0, 5) == 5

def test_add_floats():
    assert add_numbers(2.5, 3.5) == 6.0

def test_add_large_numbers():
    assert add_numbers(1000000, 2000000) == 3000000

# Handling invalid inputs (optional)
def test_add_non_numeric():
    with pytest.raises(TypeError):
        add_numbers("2", 3)
