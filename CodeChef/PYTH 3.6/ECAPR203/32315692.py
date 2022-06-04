from math import sqrt

for _ in range(int(input())):
    n = int(input())

    x = int(sqrt(2 * n))

    while x * (x+1) // 2 <= n:
        x += 1

    while x * (x+1) // 2 > n:
        x -= 1

    n -= x * (x+1) // 2

    print(n)
