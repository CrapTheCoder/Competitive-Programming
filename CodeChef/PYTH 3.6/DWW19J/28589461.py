from math import sqrt

def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if not n % i:
            return False

    return True

for _ in range(int(input())):
    n = int(input())

    if is_prime(n):
        print('Divesh')
    else:
        print('Tanya')