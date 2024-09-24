# Task 60 - Generators - Prime Numbers

class Factorial:
    def __init__(self, n):
        self._n = n
        self._current = 1
        self._factorial_value = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._current > self._n:
            raise StopIteration
        if self._current == 1:
            self._factorial_value = 1
        else:
            self._factorial_value *= self._current

        result = self._factorial_value
        self._current += 1
        return result


for i in Factorial(10):
    print(i)
