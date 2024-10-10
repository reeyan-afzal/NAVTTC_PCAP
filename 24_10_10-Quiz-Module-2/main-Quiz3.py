"""
Count the numbers and check of vowels in a given string
"""


def input_validator():
    while True:
        _string = input("Enter your string: ")

        if not _string.strip():
            print("Input cannot be empty. Please enter a valid string.")
            continue

        if any(char.isdigit() for char in _string):
            print("Invalid input. Please enter a string without numbers.")
            continue

        return _string


def vowels_counter(_string):
    vowels = 'aeiouAEIOU'
    _count = 0
    _found_vowels = []

    for char in _string:
        if char in vowels:
            _count += 1
            _found_vowels.append(char)

    return _count, _found_vowels


if __name__ == "__main__":
    string = input_validator()
    count, found_vowels = vowels_counter(string)
    print("Number of vowels:", count)
    print("Vowels found:", found_vowels)
