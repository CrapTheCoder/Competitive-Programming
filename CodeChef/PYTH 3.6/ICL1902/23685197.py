from math import sqrt

for _ in range(int(input())):
    k = int(input())
    i = 0

    while k > 0:
        k -= int(sqrt(k)) ** 2
        i += 1

    print(i)