def arrow_pointing_up(rows):
    for i in range(1, rows + 1):
        for _ in range(rows - i):
            print(" ", end='\t')
        for _ in range(i):
            print("*\t", end='')
        for _ in range(i - 1):
            print("*\t", end='')
        print()

    for _ in range(rows * 2):
        print("\t\t" + "\t* " * 3, sep='')


def arrow_pointing_down(rows):
    for _ in range(rows * 2):
        print("\t\t" + "\t* " * 3, sep='')

    for i in range(rows, 0, -1):
        for _ in range(rows - i):
            print("  ", end='\t')
        for _ in range(i - 1):
            print("*\t", end='')
        for _ in range(i):
            print("*\t", end='')
        print()


def arrow_pointing_right(rows):
    for i in range(1, rows + 1):
        for j in range(10):
            if j < 7:
                print("\t  ", end='')
            else:
                print("\t* " * i, end='')
                break
        print()

    for _ in range(rows):
        if _ != 1:
            print("*\t" * 8 + "*\t" * rows + "*\t ")
        else:
            print("*\t" * 9 + "*\t" * rows + "*\t ")

    for i in range(rows, 0, -1):
        for j in range(10):
            if j < 7:
                print("\t  ", end='')
            else:
                print("\t* " * i, end='')
                break
        print()


def arrow_pointing_left(rows):
    for i in range(1, rows + 1):
        for j in range(rows * 2):
            if j < (rows - i) + 1:
                print("\t  ", end='')
            else:
                print("\t* " * i, end='')
                break
        print()

    for _ in range(rows):
        if _ != 1:
            print("\t* " * 8 + "\t* " * rows + "\t*")
        else:
            print("*\t" * 9 + "*\t" * rows + "* ")

    for i in range(rows, 0, -1):
        for j in range(rows * 2):
            if j < (rows - i) + 1:
                print("\t  ", end='')
            else:
                print("\t* " * i, end='')
                break
        print()


print("Arrow Up: ")
arrow_pointing_up(5)
print("\nArrow Down: ")
arrow_pointing_down(5)
print("\nArrow Right: ")
arrow_pointing_right(3)
print("\nArrow left: ")
arrow_pointing_left(3)
