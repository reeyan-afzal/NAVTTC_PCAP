# Task 3 - Student Management System

print('*' * 29)
print('| Student Management System |')
print('*' * 29, end='\n')

_programRunning = True


def data_entry():
    stdName = input("Enter your name: ")
    stdFName = input("Enter your father name: ")

    print("\nWelcome! " + stdName + ", father name " + stdFName + ".")
    print("How can I help you?", end='\n')


def calculate_marks():
    stdSub1Marks = float(input("Enter your marks in Subject-1(100.0): "))
    stdSub2Marks = float(input("Enter your marks in Subject-2(100.0): "))
    stdSub3Marks = float(input("Enter your marks in Subject-3(100.0): "))

    print("\nYou've got", stdSub1Marks, "in Subject 1,", stdSub2Marks, "in Subject 2 and", stdSub3Marks, "in Subject 3")
    print("You've secured", stdSub1Marks + stdSub2Marks + stdSub3Marks, "marks out of 300")
    print("Your Percentage is: {0:.2f}".format(((stdSub1Marks + stdSub2Marks + stdSub3Marks) / 300) * 100))


def calculate_grade():
    stdPercentage = float(input("Enter your percentage to calculate grade: "))

    if stdPercentage >= 90:
        print('\nCongrats! You\'re grade is A+')
    elif 80 <= stdPercentage < 90:
        print('\nNice! You\'re grade is A')
    elif 70 <= stdPercentage < 80:
        print('\nGood! You\'re grade is B+')
    elif 60 <= stdPercentage < 70:
        print('\nSatisfactory! You\'re grade is B')
    elif 50 <= stdPercentage < 60:
        print('\nNeed-Improvement! You\'re grade is C')
    else:
        print('\nOops! You\'re grade is F, you\'re Failed!')


while _programRunning:
    print('\n1. Enter your data.')
    print('2. Calculate marks for 3 subjects with percentage.')
    print('3. Calculate your grades.')
    print('4. Exit program.')

    try:
        _userChoice = input('\nEnter your choice: ')

        if _userChoice == '1':
            data_entry()

        elif _userChoice == '2':
            calculate_marks()

        elif _userChoice == '3':
            calculate_grade()

        elif _userChoice == '4':
            _programRunning = False

        else:
            print('\nInvalid option! Please select the correct option(4 to exit)')

    except KeyboardInterrupt:
        _programRunning = False
