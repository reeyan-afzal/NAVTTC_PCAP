# Task 10 - Random Number Guessing Game
import random

print("""+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I am     |
| guessing. If you pass the test |
| I shall open the door for you  |
+================================+
""")

try:
    while True:
        my_number = random.randint(1, 100)
        try:
            your_guess = int(input("Guess a number from 1 to 100: "))
        except ValueError:
            print("\nDo I have to remind you what a number is now?\n")
            continue

        if your_guess > 100:
            print("\nI said! Guess a number from 1 to 100! You idiot!\n")
            continue

        else:
            if your_guess < my_number:
                print("\nSorry! My number was greater than your guess!")
                print("You're stuck in my loop! Haha\n")
            elif your_guess > my_number:
                print("\nSorry! My number was smaller than your guess!")
                print("You're stuck in my loop! Haha\n")
            else:
                print("\nDamn nation! You beat me! You shall pass through this gate!")
                print("I am lifting this protection charm")
                break
except KeyboardInterrupt:
    print("\n\nDamn! Now that's cheating!")
    exit()
