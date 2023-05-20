import pytest

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

@pytest.fixture
def numbers():
    return (2, 3)


def test_add(numbers):
    a, b = numbers
    assert add(a, b) == 5


def test_subtract(numbers):
    a, b = numbers
    assert subtract(a, b) == -1


@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (4, 5, 20), (0, 6, 0)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(6, 3, 2), (20, 5, 4), (0, 6, 0)])
def test_divide(a, b, expected):
    assert divide(a, b) == expected
