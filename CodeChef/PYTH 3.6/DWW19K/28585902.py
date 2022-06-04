from math import pi

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print((1 / (10 * n * pi)) * sum(a))