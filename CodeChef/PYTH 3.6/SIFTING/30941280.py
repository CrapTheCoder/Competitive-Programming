from math import sqrt

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if not n % i:
            return False

    return True

n = int(input())

c = 0

for i in range(n+1):
    if is_prime(i):
        c += 1

print(c)