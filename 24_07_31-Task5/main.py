# Task 5 - Event End Time Calculator

hrs = int(input("Enter the number of Hours: "))
mins = int(input("Enter the number of Minutes: "))
durs = int(input("Enter the duration event will last: "))

print("Event will starts at:",  hrs, ":", mins)

new_mins = mins + durs
if new_mins > 60:
    hrs += 1
    mins = new_mins % 60
else:
    mins = new_mins

print("Event will end at:   ", hrs, ":", mins)
