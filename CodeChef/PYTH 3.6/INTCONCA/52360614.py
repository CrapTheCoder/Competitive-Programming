from sys import stdin, stdout
input = stdin.readline


for _ in range(int(input())):
    n, L, R = map(int, input().split())
    a = sorted(map(int, input().split()))

    s = 0

    ls = [0] * n
    rs = [0] * n

    l, r = 0, n-1

    for i in range(n-1, -1, -1):
        while l < n and (not L <= int(str(a[l]) + str(a[i]))):
            l += 1

        ls[i] = l

    for i in range(n):
        while r >= 0 and (not int(str(a[r]) + str(a[i])) <= R):
            r -= 1

        d = r - ls[i] + 1
        if d > 0:
            s += d

    stdout.write(str(s) + '\n')