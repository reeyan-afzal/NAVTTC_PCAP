def print_spaces(count):
    for _ in range(count):
        print("  ", end='\t')


def print_stars(count):
    for _ in range(count):
        print("\t*", end=' ')


def arrow_head_up(rows):
    for i in range(1, rows):
        print_spaces(rows - i)
        print_stars(i)
        print_stars(i - 1)
        print('\n')


def arrow_head_down(rows):
    for i in range(rows - 1, 0, -1):
        print_spaces(rows - i)
        print_stars(i - 1)
        print_stars(i)
        print('\n')


def arrow_tail_up_down(rows):
    for _ in range(rows):
        print("\t\t\t" + "\t* " * 3)
    print()


def arrow_pattern_up():
    arrow_head_up(5)
    arrow_tail_up_down(10)


def arrow_pattern_down():
    arrow_tail_up_down(10)
    arrow_head_down(5)


print("Arrow Up: ")
arrow_pattern_up()
print("\nArrow Down: ")
arrow_pattern_down()
