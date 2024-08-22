# Task 28 - Exploring Modules

from sys import path

path.append(r"..//24_08_22-Task29//data")
path.append(r"..//24_08_22-Task29//modules")

import module
import admin_data
import student_data

if __name__ == "__main__":
    print("\nThis is main function\n")
    admin_data.data()
    student_data.data()
    print()
    admin_data.package()
    student_data.package()
    print("The counter from module.py is:", module.counter)
