# Task 63 - File Handling 01

import os
import errno

try:
    s = open(os.getcwd() + '/file.txt', 'rt')
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
