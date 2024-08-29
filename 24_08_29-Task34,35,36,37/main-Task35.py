# Task 35 - Caesar cipher/dicipher

def caesar_cipher(text):
    cipher = ''
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)

    return cipher


def caesar_diciper(text):
    dicipher = ''
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        dicipher += chr(code)

    return dicipher


if __name__ == "__main__":
    _text = input("Enter your message: ")
    print("\nCiphered Text:", caesar_cipher(_text))
    print("Deciphered Text:", caesar_diciper(caesar_cipher(_text)))
