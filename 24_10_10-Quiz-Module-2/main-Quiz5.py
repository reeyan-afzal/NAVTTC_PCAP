"""
Finds the Largest and Smallest numbers in a list using loops.
"""


def input_validator():
    while True:
        user_input = input("Enter a list of numbers separated by commas: ")

        if not user_input.strip():
            print("Input cannot be empty. Please enter a valid list of numbers.")
            continue

        try:
            _numbers = [int(n.strip()) for n in user_input.split(',')]
            return _numbers
        except ValueError:
            print("Invalid input. Please enter only numbers separated by commas.")


def find_largest_and_smallest(_numbers):
    if not _numbers:
        return None, None

    _largest = _numbers[0]
    _smallest = _numbers[0]

    for num in _numbers:
        if num > _largest:
            _largest = num
        if num < _smallest:
            _smallest = num

    return _largest, _smallest


if __name__ == "__main__":
    numbers = input_validator()
    largest, smallest = find_largest_and_smallest(numbers)

    if largest is not None and smallest is not None:
        print("\nLargest number:", largest)
        print("Smallest number:", smallest)
    else:
        print("The list is empty.")
