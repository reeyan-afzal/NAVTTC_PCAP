# Task 18 - List Referencing - Powerful Slices

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
new_list = my_list[1:3]
print(new_list)
