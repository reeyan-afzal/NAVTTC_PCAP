# Task 70 - DateTime Module

from datetime import datetime

dt = datetime(2020, 11, 4, 14, 53, 0)

print(dt.strftime("%Y/%m/%d %H:%M:%S"))  # 2020/11/04 14:53:00
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))  # 20/November/04 14:53:00 PM
print(dt.strftime("%a, %Y %b %d"))  # Wed, 2020 Nov 04
print(dt.strftime("%A, %Y %B %d"))  # Wednesday, 2020 November 04
print(f"Weekday: {dt.strftime('%w')}")  # Weekday: 3 (Wednesday is 3rd day of the week)
print(f"Day of the year: {dt.strftime('%j')}")  # Day of the year: 309
print(f"Week number of the year: {dt.strftime('%U')}")  # Week number of the year: 44
