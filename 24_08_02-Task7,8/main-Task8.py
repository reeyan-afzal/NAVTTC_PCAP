# Task 8 - Leap Year Calculator

def leap_year_calculator(year):
    if year <= 1582:
        return "\nThis rule was implemented after 1582."
    else:
        if not year % 4 == 0 or not year % 400 == 0:
            return "\nIt\'s a common year"
        elif year % 100 == 0:
            return "\nIt\'s a leap year"


print(leap_year_calculator(int(input("Enter the year: "))))
