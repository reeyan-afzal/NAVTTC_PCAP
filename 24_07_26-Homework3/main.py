# Homework 3 - Student Management System Advanced

import os

print('*' * 29)
print('| Student Management System |')
print('*' * 29, end='\n')

_student_info_dict = {}


def write_data():
    with open('student_data.txt', 'w') as f:
        for roll_number, details in _student_info_dict.items():
            f.write("******************************\n")
            f.write(f"Student Roll Number: {roll_number}\n")
            for key, value in details.items():
                f.write(f"{key}: {value}\n")
            f.write("******************************\n")


def retrieve_data():
    _student_info_dict.clear()
    if os.path.exists('student_data.txt'):
        with open('student_data.txt', 'r') as f:
            current_roll_number = None
            for line in f:
                line = line.strip()
                if line == "******************************":
                    current_roll_number = None
                elif "Student Roll Number" in line:
                    _, roll_number = line.split(":", 1)
                    roll_number = roll_number.strip()
                    _student_info_dict[roll_number] = {}
                    current_roll_number = roll_number
                elif current_roll_number and ':' in line:
                    key, value = line.split(':', 1)
                    _student_info_dict[current_roll_number][key.strip()] = value.strip()


def update_student_info(roll_number, key, value):
    if roll_number in _student_info_dict:
        _student_info_dict[roll_number][key] = value
        write_data()


def admin_student_entry():
    retrieve_data()
    new_std_roll_number = input("Student Roll Number: ")
    if new_std_roll_number in _student_info_dict:
        print("Roll number already exists!")
        return
    new_std_name = input("Student Name: ")
    new_std_fname = input("Student Father Name: ")

    _student_info_dict[new_std_roll_number] = {
        "Student Name": new_std_name,
        "Student Father Name": new_std_fname,
        "Marks in CS101": "0",
        "Marks in CS102": "0",
        "Marks in CS103": "0",
        "Percentage": "0.0",
        "Grade": "F"
    }

    write_data()
    print("\nRecord for " + new_std_name + " has been saved.")


def marks_entry(course_code):
    retrieve_data()
    curr_std_roll_number = input("Enter Student Roll Number: ")
    if curr_std_roll_number in _student_info_dict:
        marks = input(f"Enter marks for {course_code}: ")
        update_student_info(curr_std_roll_number, f"Marks in {course_code}", marks)
        calculate_and_update_grade(curr_std_roll_number)
        print(f"Marks for {course_code} updated.")
    else:
        print("No such student found.")


def calculate_and_update_grade(curr_std_roll_number):
    student_data = _student_info_dict[curr_std_roll_number]
    cs101 = float(student_data.get("Marks in CS101", 0))
    cs102 = float(student_data.get("Marks in CS102", 0))
    cs103 = float(student_data.get("Marks in CS103", 0))
    curr_std_percentage = ((cs101 + cs102 + cs103) / 300) * 100

    if curr_std_percentage >= 95:
        grade = "A+"
    elif 90 <= curr_std_percentage < 95:
        grade = "A"
    elif 85 <= curr_std_percentage < 90:
        grade = "B+"
    elif 80 <= curr_std_percentage < 85:
        grade = "B"
    elif 75 <= curr_std_percentage < 80:
        grade = "C+"
    elif 70 <= curr_std_percentage < 75:
        grade = "C"
    elif 65 <= curr_std_percentage < 70:
        grade = "D+"
    elif 50 <= curr_std_percentage < 65:
        grade = "D"
    else:
        grade = "F"

    update_student_info(curr_std_roll_number, "Percentage", "{0:.2f}".format(curr_std_percentage))
    update_student_info(curr_std_roll_number, "Grade", grade)


def display_student_info(curr_std_roll_number, fields):
    retrieve_data()
    if curr_std_roll_number in _student_info_dict:
        student_data = _student_info_dict[curr_std_roll_number]
        print("\n******************************")
        print(f"Details for Roll Number: {curr_std_roll_number}")
        for field in fields:
            print(f"{field}: {student_data.get(field, '0')}")
        print("******************************")
    else:
        print("No such student found.")


def student_section():
    print('\n1. Check your Subject Marks.')
    print('2. Check your Grade.')
    print('3. Retrieve your complete data.')
    print('4. Go Back to Home Screen.')
    print('5. Exit program.')


def admin_section():
    print('\n1. Enter Student Data.')
    print('2. Enter Marks for CS101.')
    print('3. Enter Marks for CS102.')
    print('4. Enter Marks for CS103.')
    print('5. Retrieve Student Data.')
    print('6. Go Back to Home Screen.')
    print('7. Exit program.')


retrieve_data()

while True:
    try:
        print('\n1. Login as Admin.')
        print('2. Login as Student.')
        print('3. Exit program.')

        _login_choice = input('\nSelect an Option: ')

        if _login_choice == '1':
            while True:
                admin_section()
                _admin_choice = input('\nSelect an Option: ')
                if _admin_choice == '1':
                    admin_student_entry()
                elif _admin_choice == '2':
                    marks_entry("CS101")
                elif _admin_choice == '3':
                    marks_entry("CS102")
                elif _admin_choice == '4':
                    marks_entry("CS103")
                elif _admin_choice == '5':
                    std_roll_number = input("Enter Student Roll Number: ")
                    display_student_info(std_roll_number, [
                        "Student Name",
                        "Student Father Name",
                        "Marks in CS101",
                        "Marks in CS102",
                        "Marks in CS103",
                        "Percentage",
                        "Grade"])
                elif _admin_choice == '6':
                    break
                elif _admin_choice == '7':
                    print("\nExiting program. Goodbye!")
                    exit()
                else:
                    print('\nInvalid option! Please select a correct option (1 to 7).')

        elif _login_choice == '2':
            while True:
                student_section()
                _student_choice = input('\nSelect an Option: ')
                if _student_choice == '1':
                    std_roll_number = input("Enter Student Roll Number: ")
                    display_student_info(std_roll_number, [
                        "Marks in CS101",
                        "Marks in CS102",
                        "Marks in CS103"])
                elif _student_choice == '2':
                    std_roll_number = input("Enter Student Roll Number: ")
                    display_student_info(std_roll_number, [
                        "Percentage",
                        "Grade"])
                elif _student_choice == '3':
                    std_roll_number = input("Enter Student Roll Number: ")
                    display_student_info(std_roll_number, [
                        "Student Name",
                        "Student Father Name",
                        "Marks in CS101",
                        "Marks in CS102",
                        "Marks in CS103",
                        "Percentage",
                        "Grade"])
                elif _student_choice == '4':
                    break
                elif _student_choice == '5':
                    print("\nExiting program. Goodbye!")
                    exit()
                else:
                    print('\nInvalid option! Please select a correct option (1 to 5).')

        elif _login_choice == '3':
            print("\nExiting program. Goodbye!")
            break

        else:
            print('\nInvalid option! Please select a correct option (1 to 3).')
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        break
