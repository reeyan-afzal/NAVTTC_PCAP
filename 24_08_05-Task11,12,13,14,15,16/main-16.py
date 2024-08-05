# Task 16 - Collatz Hypothesis.

c0 = int(input("Enter the value(none and greater than 0): "))
_steps = 0

while c0 > 0 and c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    _steps += 1

    print(c0)
print("Total Steps:", _steps)
