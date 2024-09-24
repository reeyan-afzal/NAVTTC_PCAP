# Task 59 - Generators - Fib Series

class Fib:
    def __init__(self, n):
        self._n = n
        self._i = 0
        self._p1 = self._p2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self._i += 1
        if self._i > self._n:
            raise StopIteration
        if self._i in [1, 2]:
            return 1
        ret = self._p1 + self._p2
        self._p1, self._p2 = self._p2, ret
        return ret


for i in Fib(10):
    print(i)
