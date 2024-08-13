# Find if Number is Prime

def is_prime(n):
    if n <= 1:
        return False

    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False

    return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
