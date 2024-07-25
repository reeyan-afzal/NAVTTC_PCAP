# Task 3 - Student Management System

print('*' * 29)
print('| Student Management System |')
print('*' * 29, end='\n')

_programRunning = True


def data_entry(name, father_name):
    print("\nWelcome! " + name + ", father name " + father_name + ".")
    print("How can I help you?", end='\n')


def calculate_marks(subject1, subject2, subject3):
    print("\nYou've got", subject1, "in Subject 1,", subject2, "in Subject 2 and", subject3, "in Subject 3")
    print("You've secured", subject1 + subject2 + subject3, "marks out of 300")
    print("Your Percentage is: {0:.2f}".format(((subject1 + subject2 + subject3) / 300) * 100))


def calculate_grade(percentage):
    if percentage >= 90:
        print('\nCongrats! You\'re grade is A+')
    elif 80 <= percentage < 90:
        print('\nNice! You\'re grade is A')
    elif 70 <= percentage < 80:
        print('\nGood! You\'re grade is B+')
    elif 60 <= percentage < 70:
        print('\nSatisfactory! You\'re grade is B')
    elif 50 <= percentage < 60:
        print('\nNeed-Improvement! You\'re grade is C')
    else:
        print('\nOops! You\'re grade is F, you\'re Failed!')


while _programRunning:
    print('\n1. Enter your data.')
    print('2. Calculate marks for 3 subjects with percentage.')
    print('3. Calculate your grades.')
    print('4. Exit program.')

    try:
        _userChoice = int(input('\nEnter your choice: '))

        if _userChoice == 1:
            stdName = input("Enter your name: ")
            stdFName = input("Enter your father name: ")
            data_entry(stdName, stdFName)

        elif _userChoice == 2:
            stdSub1Marks = float(input("Enter your marks in Subject-1(100.0): "))
            stdSub2Marks = float(input("Enter your marks in Subject-2(100.0): "))
            stdSub3Marks = float(input("Enter your marks in Subject-3(100.0): "))
            calculate_marks(stdSub1Marks, stdSub2Marks, stdSub3Marks)

        elif _userChoice == 3:
            stdPercentage = float(input("Enter your percentage to calculate grade: "))
            calculate_grade(stdPercentage)

        elif _userChoice == 4:
            _programRunning = False

        else:
            print('\nInvalid option! Please select the correct option(4 to exit)')

    except ValueError:
        print('\nInvalid option! Please select the correct option(4 to exit)')
