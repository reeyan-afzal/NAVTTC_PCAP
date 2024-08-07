# Task 17 - Slicing List

a = [1, 2, 3, 4, 5]

user_val = int(input("Enter your value: "))
print(a)
a[-1] = user_val
print(a)
print(len(a))

del a[0]
print(a)
print(len(a))
