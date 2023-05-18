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
        result = []
        for pattern in self.patterns:
            matched = pattern(text)
            if matched is None:
                return None
            result.append(matched)
            text = matched
        return ''.join(result)

class Group:
    def __init__(self, pattern):
        self.pattern = pattern

    def __call__(self, text):
        matched = self.pattern(text)
        if matched is None:
            return None
        else:
            return [matched]

def group(pattern):
    return Group(pattern)

class Many:
    def __init__(self, pattern):
        self.pattern = pattern

    def __call__(self, text):
        result = []
        while True:
            matched = self.pattern(text)
            if matched is None:
                break
            result.append(matched)
            text = matched
        return result

def many(pattern):
    return Many(pattern)

# usage example
digit = range_of('0', '9')
hex_digit = alt(digit, range_of('a', 'f'), range_of('A', 'F'))
space = alt(Sym(' '), Sym('\n'), Sym('\t'))
hex_color = Seq(Sym('#'), group(Seq(hex_digit, hex_digit, hex_digit, hex_digit, hex_digit, hex_digit)))
hex_colors = many(Seq(many(space), hex_color))

print(hex_colors('''#ff10aa
#f3207a
   #bb1040

#ABCD00''', []))
