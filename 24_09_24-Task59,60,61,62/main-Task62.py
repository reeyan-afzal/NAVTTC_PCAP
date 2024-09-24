# Task 62 - Generators - Reverse a String

class ReverseString:
    def __init__(self, s):
        self._s = s
        self._i = len(s)

    def __iter__(self):
        return self

    def __next__(self):
        if self._i == 0:
            raise StopIteration
        self._i -= 1
        return self._s[self._i]


for c in ReverseString("Hello"):
    print(c, end='')
