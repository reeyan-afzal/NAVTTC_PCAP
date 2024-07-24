# Task 2

stdName = input("Enter your name: ")
stdFName = input("Enter your father name: ")
stdSub1Marks = float(input("Enter your marks in Subject1(100.0): "))
stdSub2Marks = float(input("Enter your marks in Subject2(100.0): "))

print("\n**************************************************")
print("Welcome! " + stdName + ", father name " + stdFName)
print("You've got", stdSub1Marks, "in Subject 1 and", stdSub2Marks, "in Subject 2")
print("You've secured", stdSub1Marks + stdSub2Marks, "marks out of 200")
print("Your Percentage is: ", ((stdSub1Marks + stdSub2Marks) / 200) * 100)
print("**************************************************\n")
