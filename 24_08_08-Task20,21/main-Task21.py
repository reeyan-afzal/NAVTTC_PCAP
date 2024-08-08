# Task 21 - Removing Repeated Values from List

my_list = [1, 2, 3, 4, 5, 6, 3, 4, 8, 9]
visited = set()
new_list = [number for number in my_list if number not in visited and not visited.add(number)]

print("original list:", my_list)
print("new list:     ", new_list)
