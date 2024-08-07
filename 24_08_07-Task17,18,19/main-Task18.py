# Task 18 - Testing Insert and Append Functions in List

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print("Original List: ")
print(a)
print(b)

print("\nAfter Copying an element from List 1 to List 2")
b[-1] = a[-1]
print(b)

print("\nAfter deleting from List 1")
del a[-1]
print(a)

print("\nResult after appending Jawad in List 1")
a.append("Jawad")
print(a)
print("\n")

''' Loop '''


def data_insert():
    x = []
    _count = 0
    while _count < 5:
        user_val = int(input("Enter the value you want to insert: "))
        x.insert(_count, user_val)
        _count += 1
    return x


def data_append():
    y = []
    _count = 0
    while _count < 5:
        y.append(_count)
        _count += 1
    return y


try:
    print(data_insert())
    print(data_append())
except KeyboardInterrupt:
    exit()
