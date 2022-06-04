from math import ceil

for _ in range(int(input())):
    n = input()
    s = sum(list(map(int, n)))
    r = ceil(s / 10)

    print(n + str(r * 10 - s))