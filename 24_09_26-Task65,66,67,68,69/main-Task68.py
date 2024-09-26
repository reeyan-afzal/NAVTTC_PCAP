# Task 68 - File Handling 06

import os
from os import strerror


def count_and_sort_letters(file_name):
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

    letter_counts = {k: v for k, v in letter_counts.items() if v > 0}

    sorted_letter_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)

    output_file_name = os.path.splitext(file_name)[0] + '.hist'

    try:
        with open(output_file_name, 'w') as output_file:
            for letter, count in sorted_letter_counts:
                output_file.write(f"{letter} -> {count}\n")
        print(f"Histogram successfully saved to {output_file_name}")
    except IOError as e:
        print(f"Cannot write to file: {strerror(e.errno)}")


if __name__ == "__main__":
    _file_name = input("Enter the input file name: ")
    count_and_sort_letters(_file_name)
