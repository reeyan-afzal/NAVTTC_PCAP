"""
This task iterates through list of numbers and checks if each number is Prime.
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


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def check_primes(_lst):
    return ["Prime" if is_prime(n) else "Not Prime" for n in _lst]


if __name__ == "__main__":
    lst = input_validator()
    print(check_primes(lst))
