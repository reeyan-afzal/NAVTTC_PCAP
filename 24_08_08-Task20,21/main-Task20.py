# Task 20 - List Referencing - Powerful Slices

list1 = [3, 4, 5]
list3 = list1

print(list3)
del list3[0]
print(list1)

list_1 = [1, 3, 6, 7, 8, 9]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3:2]
print(new_list)

print(my_list[-3:-1])
print(my_list[-4::1])
print(my_list[-4::2])
print(my_list[::-2])
print(my_list[-1::])

print("\n")

print(my_list[0:len(my_list)])

my_list1 = [1, 2, 3, 4, 5, 6]
print(my_list1)
del my_list1[4::]
print(my_list1)

print("\n")

x = [1, 2, 3, 4, 5, 6, 7]
y = x

print("original x:", x)
del y[2]
print("x:", x)
print("y:", y)

print("\n")

z = [10, 8, 6, 4, 2]
w = [1, 2, 3, 4, 5]
print("original z:", z)
del z[:]
z.append(w)
print("z:", z)
