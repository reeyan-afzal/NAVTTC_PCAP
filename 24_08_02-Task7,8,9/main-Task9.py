# Task 9 - Password Check in 5 Attempts

_password = "PythonRocks"
_max_attempts = 5
_curr_attempts = 0

while _curr_attempts < _max_attempts:
    enter_password = input("\nEnter your password: ")

    if enter_password == _password:
        print("\nCongratulations! You can login")
        break
    else:
        _curr_attempts += 1
        print("\nIncorrect Password! You're left with {0} attempts".format(_max_attempts - _curr_attempts))
else:
    print("\nSorry! but you've reached your attempts limit!")
