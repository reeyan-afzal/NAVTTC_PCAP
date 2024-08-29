# Task 37 - Caesar Cipher - Advanced

def caesar_cipher(text, shift_value):
    cipher = ''
    shift_value %= 26
    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')

            new_char = chr((ord(char) - base + shift_value) % 26 + base)
            cipher += new_char
        else:
            cipher += char
    return cipher


if __name__ == "__main__":
    _text = input("Enter the text you want to cipher: ")
    print("\nCiphered Text:", caesar_cipher(_text, 2))
