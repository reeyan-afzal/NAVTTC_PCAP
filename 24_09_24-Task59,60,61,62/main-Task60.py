# Task 60 - Generators - Prime Numbers

class Prime:
    def __init__(self, n):
        self._n = n
        self._current = 2

    def __iter__(self):
        return self

    def __next__(self):
        while self._current <= self._n:
            is_prime = True
            for _i in range(2, int(self._current ** 0.5) + 1):
                if self._current % _i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime = self._current
                self._current += 1
                return prime
            self._current += 1
        raise StopIteration


for i in Prime(10):
    print(i)
