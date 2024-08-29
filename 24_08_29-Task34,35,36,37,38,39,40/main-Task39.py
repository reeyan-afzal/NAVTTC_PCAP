# Task 39 - Anagrams

def is_anagrams(text_1, text_2):
    if sorted(text_1) == sorted(text_2):
        return "The given two text are anagrams"
    else:
        return "The given two text are not anagrams"


if __name__ == "__main__":
    _text_1 = input("Enter the text_1: ")
    _text_2 = input("Enter the text_2: ")
    text_1_normalize = _text_1.lower().replace(' ', '')
    text_2_normalize = _text_2.lower().replace(' ', '')
    print(is_anagrams(text_1_normalize, text_2_normalize))
