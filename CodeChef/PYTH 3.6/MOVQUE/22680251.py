from math import log

for _ in range(int(input())):
    n = int(input())
    print(2 ** int(log(n, 2)))
