from math import sqrt

def isPrime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if not n % 2:
        return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if not n % i:
            return False

    return True

for _ in range(int(input())):
    s = input()
    c = s.count('1')

    if isPrime(int(s, 2)):
        print(c, 'Lucky day')
    else:
        print(c, 'Unucky day')
