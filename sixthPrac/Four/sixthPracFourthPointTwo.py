# Реализуйте комбинатор range_of (разобрать диапазон символов).
#
# Пример использования:
#
# digit = range_of('0', '9')
# number = seq(digit, digit)
#
# print(number('42') is not None)
# print(number('ab') is not None)
# True
# False

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __call__(self, text):
        if len(text) == 0:
            return None
        elif self.start <= text[0] <= self.end:
            return text[1:]
        else:
            return None

def range_of(start, end):
    return Range(start, end)

class Seq:
    def __init__(self, *patterns):
        self.patterns = patterns

    def __call__(self, text):
        for pattern in self.patterns:
            text = pattern(text)
            if text is None:
                return None
        return text

# usage examples
digit = range_of('0', '9')
number = Seq(digit, digit)

print(bool(number('42'))) # Output: True
print(bool(number('ab'))) # Output: False