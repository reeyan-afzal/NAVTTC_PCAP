# Task 14 - Ugly Vowel Eater

import string

char_letters = string.ascii_letters
vowel_list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

try:
    while True:
        var = input("Enter the string: ")
        new_string = ''
        vowels_killed = ''

        for s in var:
            if s.upper() in char_letters:
                if s in vowel_list:
                    vowels_killed += s
                else:
                    print(s.upper())
            else:
                var = ''
        break
    if var != '':
        print("\nVowels Killed: ", ', '.join(vowels_killed.upper()))
    else:
        print("\nYou sure you're right in the head!")
except KeyboardInterrupt:
    exit()
