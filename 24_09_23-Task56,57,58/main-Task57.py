# Task 57 - MyOverflowError and MyUnderflow

class MyOverflowError(ArithmeticError):
    pass


class MyUnderflowError(ArithmeticError):
    pass


def do_the_division(_value):
    if _value > 100:
        raise MyOverflowError("The value is too large!")
    elif _value < 0:
        raise MyUnderflowError("The value is negative!")
    elif _value == 0:
        raise ZeroDivisionError("Division by zero is not allowed!")
    else:
        return 100 / value


test_values = [150, -10, 0, 50]

for value in test_values:
    try:
        print(f"Processing value: {value}")
        result = do_the_division(value)
        print(f"Result: {result}")
    except MyOverflowError as oe:
        print(f"Overflow Error: {oe}")
    except MyUnderflowError as ue:
        print(f"Underflow Error: {ue}")
    except ZeroDivisionError as zde:
        print(f"Zero Division Error: {zde}")
    finally:
        print("Finished processing.\n")
