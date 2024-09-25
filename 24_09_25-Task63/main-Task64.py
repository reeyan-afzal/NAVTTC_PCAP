# Task 64 - File Handling 02

import os
from os import strerror

try:
    ccnt = lcnt = wcnt = 0
    in_word = False
    s = open(os.getcwd() + '/file.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
                if ch == ' ' or ch == '\n':
                    if in_word:  # If we were in a word, it's the end of a word
                        wcnt += 1
                        in_word = False
                else:
                    in_word = True  # We're inside a word now

            # Handle the case where a word ends at the end of the line
            if in_word:
                wcnt += 1
                in_word = False  # Reset the flag after counting the word

        lines = s.readlines(10)
    s.close()

    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
    print("Words in file:     ", wcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
