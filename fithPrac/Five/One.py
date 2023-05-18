from hypothesis import given
import hypothesis.strategies as st
import unittest


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


@given(st.floats(), st.floats(), st.floats(), st.floats())
def test_distance(x1, y1, x2, y2):
    assert distance(x1, y1, x2, y2) >= 0
    assert distance(x1, y1, x2, y2) == distance(x2, y2, x1, y1)
    assert distance(x1, y1, x1, y1) == 0


class TestDistance(unittest.TestCase):
    def test_distance(self):
        test_distance()
