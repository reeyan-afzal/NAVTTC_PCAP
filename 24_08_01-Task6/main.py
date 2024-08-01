# Task 6 - Simple Boolean Bulb Check

def check_bulb(bulb):
    if bulb == 1:
        print("The bulb is on!")
    elif bulb != 1 and bulb == 0:
        print("The bulb is off!")
    else:
        print("\nInvalid Command!\n")


check_bulb(int(input("Enter the state of the bulb(1/0): ")))
