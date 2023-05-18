import io
import sys


def add():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a + b


def subtract():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a - b


def multiply():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a * b


def divide():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a / b


def test_add():
    sys.stdin = io.StringIO("2\n3\n")
    assert add() == 5


def test_subtract():
    sys.stdin = io.StringIO("2\n3\n")
    assert subtract() == -1


def test_multiply():
    sys.stdin = io.StringIO("2\n3\n")
    assert multiply() == 6


def test_divide():
    sys.stdin = io.StringIO("6\n3\n")
    assert divide() == 2
