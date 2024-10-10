"""
Check for Even or Odd Numbers. This task iterates through a list of numbers and checks whether
each number is Even or Odd
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


def even_odd(_lst):
    new_lst = []
    for n in _lst:
        if n % 2 == 0:
            new_lst.append("Even")
        else:
            new_lst.append("Odd")
    return new_lst


if __name__ == "__main__":
    lst = input_validator()
    print(even_odd(lst))
