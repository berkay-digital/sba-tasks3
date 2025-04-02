import pytest
from main import add, subtract, multiply, divide, power

@pytest.fixture
def number_pairs():
    return [(2, 3), (5, 2), (0, 0), (-1, 1)]

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    assert divide(0, 5) == 0
    
    with pytest.raises(ValueError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(0, 5) == 0

# Using fixture
def test_add_with_fixture(number_pairs):
    for a, b in number_pairs:
        assert add(a, b) == a + b

# Parameterized tests
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (5, 5, 10)
])
def test_add_parameterized(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 3),
    (2, 5, -3),
    (0, 0, 0),
    (10, 5, 5)
])
def test_subtract_parameterized(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-2, 3, -6),
    (0, 5, 0),
    (2, 2, 4)
])
def test_multiply_parameterized(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (0, 5, 0),
    (8, 4, 2)
])
def test_divide_parameterized(a, b, expected):
    assert divide(a, b) == expected

@pytest.mark.parametrize("a, b", [(5, 0), (10, 0)])
def test_divide_by_zero(a, b):
    with pytest.raises(ValueError):
        divide(a, b)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (0, 5, 0),
    (2, 2, 4)
])
def test_power_parameterized(a, b, expected):
    assert power(a, b) == expected