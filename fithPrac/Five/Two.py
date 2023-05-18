import unittest
from hypothesis import given
from hypothesis.strategies import text, integers


def encode(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count) + s[i - 1])
            count = 1
    result.append(str(count) + s[-1])
    return "".join(result)


def decode(s):
    result = []
    i = 0
    while i < len(s):
        count = 0
        while s[i].isdigit():
            count = 10 * count + int(s[i])
            i += 1
        result.append(s[i] * count)
        i += 1
    return "".join(result)


class TestRLE(unittest.TestCase):
    @given(text())
    def test_encode_decode(self, s):
        encoded = encode(s)
        decoded = decode(encoded)
        self.assertEqual(s, decoded)


if __name__ == '__main__':
    unittest.main()