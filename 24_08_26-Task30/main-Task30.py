# String Manipulation

try:
    while True:
        _user_input = input("Enter the Value: ")
        _max_for_input = 0
        _min_for_input = 0

        if len(_user_input) % 2 == 0:
            print(f"\nThe string '{_user_input}' is even, so every thing is fine")
        else:
            print(f"\nThe string '{_user_input}' is odd, so adding one extra white-space")
            _user_input += ' '

        _user_input_list = []
        for letter in _user_input:
            _user_input_list.append(ord(letter))

        print()
        print("_user_input:     ", list(_user_input))
        print("_user_input_list:", list(_user_input_list))

        print()
        print(f"The maximum in '{_user_input}' is {max(_user_input_list)}, corresponding to letter "
              f"{chr(max(_user_input_list))}")
        print(f"The minimum in '{_user_input}' is {min(_user_input_list)}, corresponding to letter "
              f"{chr(min(_user_input_list))}")

        half_index = len(_user_input) // 2
        first_half = _user_input[:half_index]
        second_half = _user_input[half_index:]

        print()
        print(f"The first_half of '{_user_input}' is:", first_half)
        print(f"The second_half of '{_user_input}' is:", second_half)

        print()
        try:
            print(_user_input.index('a'))
        except ValueError:
            print("The letter 'a' is not present in the string")
        print()
        print("*" * 40, end='\n')
except KeyboardInterrupt:
    exit()
