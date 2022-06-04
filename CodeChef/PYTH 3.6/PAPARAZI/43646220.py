from sys import setrecursionlimit
setrecursionlimit(10 ** 7)

def solve(i, p=-1):
    if i == 0:
        return 0

    if p == -1:
        d[i] = solve(i-1, i)
        return d[i]

    j = d[i]
    s1 = a[p] - a[i], p - i
    s2 = a[i] - a[j], i - j

    if s1[0] * s2[1] >= s2[0] * s1[1]:
        return solve(j, p)

    return i

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = {0: 0}

    maxi = 1
    for i in range(n):
        maxi = max(maxi, i - solve(i))

    print(maxi)