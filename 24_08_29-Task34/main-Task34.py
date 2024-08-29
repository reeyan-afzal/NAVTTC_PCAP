# Task 34 - LED Display

_led_dict = {
    0: ["###", "# #", "# #", "# #", "###"],
    1: ["  #", "  #", "  #", "  #", "  #"],
    2: ["###", "  #", "###", "#  ", "###"],
    3: ["###", "  #", "###", "  #", "###"],
    4: ["# #", "# #", "###", "  #", "  #"],
    5: ["###", "#  ", "###", "  #", "###"],
    6: ["###", "#  ", "###", "# #", "###"],
    7: ["###", "  #", "  #", "  #", "  #"],
    8: ["###", "# #", "###", "# #", "###"],
    9: ["###", "# #", "###", "  #", "###"]
}


def display_led(number):
    digits = [int(digit) for digit in str(number)]

    for row in range(5):
        row_display = "   ".join(_led_dict[digit][row] for digit in digits)
        print(row_display)


if __name__ == "__main__":
    _number = input("Enter the number to be displayed on LED: ")
    display_led(_number)
