from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())

    s = [1] * (n+1)
    t = [1] * (n+1)

    for _ in range(m):
        i, j, k = map(int, input().split())
        i -= 1

        s[i] *= k
        t[j] *= k

    a = [10] * n
    cur = 1

    for i in range(n):
        cur *= s[i]
        cur //= t[i]

        a[i] *= cur

    print(sum(a) // n)