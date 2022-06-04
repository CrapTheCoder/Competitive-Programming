from math import sqrt

tcs, x = map(int, input().split())

for _ in range(tcs):
    n = int(input())

    if n >= 0 and n - int(sqrt(n)) ** 2 <= 0.01 * x * n:
        print('yes')
    else:
        print('no')