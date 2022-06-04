from math import log2

n = int(input())
a = list(map(int, input().split()))

for x in a:
    if x > 0 and log2(x).is_integer():
        print(1)
        exit()

for i in range(n):
    x = 1

    for j in range(i + 1):
        x *= a[j]

    if x > 0 and log2(x).is_integer():
        print(1)
        exit()

print(0)