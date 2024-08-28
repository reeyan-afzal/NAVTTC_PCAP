# Task 31 - String Manipulation-2

def user_entry():

    while True:
        _user_first_name = input("Enter your first name: ")
        _user_last_name = input("Enter your last name:  ")

        if _user_first_name.isalpha() and _user_last_name.isalpha():
            break
        else:
            print("\nInvalid names! Please enter correct names!\n")

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


def is_user_name_valid(user_name):
    if user_name:
        print("\nUsername is Valid!")
    else:
        print("\nUsername is Invalid!")


def find_word(sentence):
    word = input("Find: ")
    if sentence.find(word) == -1:
        print(f"\nThe word '{word}' is not present in sentence!")
    else:
        print("The word is at index:", sentence.find(word))


def sentence_type(sentence):
    if sentence.endswith('?'):
        print("\nThis sentence is a Question")
    elif sentence.endswith('!'):
        print("\nThis sentence is an Order")

    # Using the short-circuiting here!
    if sentence and sentence[0].isupper() and sentence[1:len(sentence)].islower():
        print("\nThe sentence is capitalized")
    elif sentence.islower():
        print("\nThe sentence is all lower")
    elif sentence.isupper():
        print("\nThe sentence is all upper")


def upload_file_type(file):
    if (file.endswith('.pdf') or
            file.endswith('.txt') or
            file.endswith('.jpeg') or
            file.endswith('.png')):
        print("\nUploading file to the Server...")
    else:
        print("\nThis file extension is not supported!")


def date_formatter():
    year = input("Enter the Year: ")
    month = input("Enter the Month: ")
    day = input("Enter the Day: ")

    date = [year, month, day]

    return "/".join(date)


if __name__ == "__main__":
    # _user_sentence = input("Enter a Sentence: ")
    # sentence_type(_user_sentence)
    #
    # _user_file = input("Upload the file with proper extension(.pdf/.txt/.jpeg/.png): ")
    # upload_file_type(_user_file)

    # _user_name = input("Enter your username: ")
    # is_user_name_valid(_user_name)
    user_entry()
    date_formatter()
