# Task 1

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
_sum = num1 + num2
print(_sum, end="\n")


# Task 2

def addition(num1_addition, num2_addition):
    _sum_in_function = num1_addition + num2_addition
    print("The addition of ", num1_addition, " and ", num2_addition, " is: ", _sum_in_function)


def subtraction(num1_subtraction, num2_subtraction):
    _sub_in_function = num1_subtraction - num2_subtraction
    print("The subtraction of ",  num1_subtraction, " and ", num2_subtraction, " is: ",  _sub_in_function)


addition(num1, num2)
subtraction(num1, num2)
