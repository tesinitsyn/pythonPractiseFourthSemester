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

class Alt:
    def __init__(self, *patterns):
        self.patterns = patterns

    def __call__(self, text):
        for pattern in self.patterns:
            matched = pattern(text)
            if matched is not None:
                return matched
        return None

def alt(*patterns):
    return Alt(*patterns)

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
hex_digit = alt(digit, range_of('a', 'f'), range_of('A', 'F'))
space = alt(Sym(' '), Sym('\n'), Sym('\t'))
hex_color = Seq(Sym('#'), hex_digit, hex_digit, hex_digit, hex_digit, hex_digit, hex_digit)

print(bool(hex_color('#ffaa43'))) # Output: True
print(bool(hex_color('#xxxxxx'))) # Output: False
