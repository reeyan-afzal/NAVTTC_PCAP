# Task 38 - Palindrome

def is_palindrome(text):
    if text == text[::-1]:
        return "The given text is a palindrome"
    else:
        return "The given text is not a palindrome"


if __name__ == "__main__":
    _text = input("Enter the text: ")
    normalized_text = _text.lower().replace(' ', '')
    print(is_palindrome(normalized_text))
