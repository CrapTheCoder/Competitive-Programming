from itertools import permutations

def count(a):
    s = 0
    for i in range(n):
        s += ((a[i-1] if i-1 >= 0 else 0) + (a[i+1] if i+1 < len(a) else 0)) / 2 - a[i]

    print(a, s, a[0], a[-1])
    return abs(s)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(sum(a[i] * (n-1) for i in range(n)) // (n * (n-1)))