def solve(i):
    if c[i] != 0:
        return c[i]

    maxi = 0

    if i+1 < n and a[i+1] == a[i]: maxi = max(maxi, solve(i+1) + 1)
    if i+2 < n and a[i+2] == a[i]: maxi = max(maxi, solve(i+2) + 1)

    c[i] = maxi
    return c[i]

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    c = [0] * n

    for i in range(n):
        solve(i)

    print(max(c))
