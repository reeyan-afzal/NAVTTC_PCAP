# Task 13 - Chupacabra will not Stop!

import string

char_letters = string.ascii_letters
print(char_letters)
print(chr(ord(char_letters[-26]) + 32))


def custom_to_lower(custom_string):
    new_string = ''
    for s in custom_string:
        if s in char_letters:
            if 'A' <= s <= 'Z':
                new_string += chr(ord(s) + 32)
            elif 'a' <= s <= 'z':
                new_string += s
    return new_string


try:
    while True:
        var = input("Enter the value: ")
        if custom_to_lower(var) == 'chupacabra':
            break
        print("Hint! It is a creature that is also known as Goat-Sucker!\n")

    print("\nYou've successfully left the loop.")
except KeyboardInterrupt:
    exit()
