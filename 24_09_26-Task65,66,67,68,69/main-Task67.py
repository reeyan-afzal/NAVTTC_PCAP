# Task 67 - File Handling 05

from os import strerror


def count_letters(file_name):
    letter_counts = {chr(i): 0 for i in range(97, 123)}

    try:
        with open(file_name, 'r') as file:
            for line in file:
                for char in line:
                    char = char.lower()
                    if 'a' <= char <= 'z':
                        letter_counts[char] += 1
    except IOError as e:
        print(f"Cannot open file: {strerror(e.errno)}")
        return

    for letter, count in sorted(letter_counts.items()):
        if count > 0:
            print(f"{letter} -> {count}")


if __name__ == "__main__":
    _file_name = input("Enter the input file name: ")
    count_letters(_file_name)
