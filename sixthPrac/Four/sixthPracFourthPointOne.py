# Реализуйте комбинаторы sym (разобрать символ) и seq (разобрать последовательность).
#
# Пример использования:
#
# text = 'abc'
# re1 = seq(sym('a'), sym('b'), sym('c'))
# re2 = seq(sym('a'), sym('z'), sym('c'))
#
# print(re1(text) is not None)
# print(re2(text) is not None)
# True
# False


class Sym:
    def __init__(self, char):
        self.char = char

    def __call__(self, text):
        if len(text) == 0:
            return None
        elif text[0] == self.char:
            return text[1:]
        else:
            return None



class Seq:
    """Match a sequence of characters"""

    def __init__(self, *patterns):
        self.patterns = patterns

    def __call__(self, text):
        for pattern in self.patterns:
            text = pattern(text)
            if text is None:
                return None
        return text if text == '' else None


# usage examples
text = "abc"
re1 = Sym('a')
re2 = Seq(Sym('a'), Sym('z'), Sym('c'))

print(bool(re1(text)))
print(bool(re2(text)))
