# Exception Handling


while True:
    try:
        num1 = float(input("Enter the nominator: "))
        num2 = float(input("Enter the denominator: "))

        print(f"{num1} divided by {num2} is: {num1 / num2}")

    except ValueError:
        print("Are you sure that's a number you're trying to enter!")

    except ZeroDivisionError:
        print("Seems like your math is terrible!")

    finally:
        print("\nProgram Finished! Go Home now!")
        exit()
