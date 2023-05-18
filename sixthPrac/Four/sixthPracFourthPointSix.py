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

def findall(pattern):
    def search_all(text, result):
        matched = pattern(text)
        if matched is not None:
            result.append(matched[0])
            search_all(matched[1], result)
        return result
    return lambda text, result=[]: search_all(text, result)


text = '12dasd dsa82 a-'
num = group(Seq(range_of('0', '9'), many(range_of('0', '9'))))
print(findall(num)(text, []))
