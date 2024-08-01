# Task 6 - Simple Boolean Bulb Check

while True:
    bulb = (input("Enter the state of the bulb(1/0): "))

    if bulb == '1':
        print("The bulb is now on!")
        break
    elif bulb != '1' and bulb == '0':
        print("The bulb is now off!")
        break
    else:
        print("\nInvalid Command!\n")
