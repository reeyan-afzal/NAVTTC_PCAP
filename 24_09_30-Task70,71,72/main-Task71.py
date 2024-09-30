# Task 71 - Birth Year Calculator

from datetime import date

current_year = date.today().year

user_birth_year = int(input("Enter your birth year: "))

age = current_year - user_birth_year
print("Your age is:", age)
