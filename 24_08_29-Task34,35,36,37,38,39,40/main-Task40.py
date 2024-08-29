# Task 40 - The Digit of Life

def digit_of_life(digit):
    while len(digit) > 1:
        add_digits = sum(int(e) for e in digit)
        digit = str(add_digits)
    return int(digit)


if __name__ == "__main__":
    _digit = input("Enter the YYYYMMDD: ")
    print(digit_of_life(list(_digit.strip())))
