# Task 33 - String Manipulation-3b

def my_split(string):
    my_list = []
    my_var = ''

    for ch in string:
        if ch == ' ':
            if my_var:
                my_list.append(my_var)
                my_var = ''
        else:
            my_var += ch

    if my_var:
        my_list.append(my_var)

    return my_list


if __name__ == "__main__":
    for i in range(5):
        _string = input(f"Enter string {i+1}: ")
        result = my_split(_string)
        print(f"Result for string {i+1}: {result}")
