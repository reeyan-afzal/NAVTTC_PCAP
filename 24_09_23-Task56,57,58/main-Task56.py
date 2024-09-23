# Task 56 - New Exceptions

def reciprocal(n):
    try:
        n = 1 / n
    except TypeError:
        print("Wrong Type")
        return None

    except ZeroDivisionError:
        print("Division Failed")
        return None
    else:
        print("Everything went fine")
        return n


print(reciprocal(2))
print(reciprocal('a'))
print(reciprocal(0))
