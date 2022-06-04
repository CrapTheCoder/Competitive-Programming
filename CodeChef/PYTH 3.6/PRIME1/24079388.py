from math import sqrt

def isPrime(n):
    if n <= 1: return False
    if n <= 3: return True
    if not n % 2 or not n % 3: return False

    for i in range(5, int(sqrt(n)) + 1, 6):
        if not n % i or not n % (i + 2):
            return False

    return True

for _ in range(int(input())):
    m, n = list(map(int, input().split()))

    for i in range(m, n+1):
        if isPrime(i):
            print(i)

    print()