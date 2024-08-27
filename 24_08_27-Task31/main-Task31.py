# Task 31 - Password Checker

_user_first_name = input("Enter your first name: ")
_user_last_name = input("Enter your last name:  ")

_user_password = input("Enter the password: ")
_user_confirm_password = input("Enter the confirm password: ")

if (_user_confirm_password != _user_password) or (_user_confirm_password.endswith(_user_first_name)):
    print("\nPassword contains your first name!")
elif (_user_confirm_password != _user_password) or (_user_confirm_password.endswith(_user_last_name)):
    print("\nPassword contains your last name!")
else:
    print(" Welcome ".center((len(_user_first_name) + len(_user_last_name)) * 2, "*"))
    print("*" + str(_user_first_name + ' ' + _user_last_name)
          .center((len(_user_first_name) + len(_user_last_name)) * 2) + "*")

    print()
    _user_sentence = input("Enter a Sentence: ")
    _user_word = input("Find: ")

    if _user_sentence.find(_user_word) == -1:
        print(f"\nThe word '{_user_word}' is not present in sentence!")
    else:
        print("The word is at index:", _user_sentence.find(_user_word))
