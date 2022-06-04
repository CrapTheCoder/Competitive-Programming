for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    d = {}
    for i in range(n):
        a[i] -= 1
        d[a[i]] = i

    b = sorted(a)

    l = -1
    for i in range(n):
        if a[i] != i:
            l = i
            break

    r = -1
    for i in range(n-1, -1, -1):
        if a[i] != i:
            r = i
            break

    if l == -1 or r == -1:
        print(0)
        continue

    if r - l + 1 <= k:
        print(1)
        continue

    c = a.copy()
    d = a.copy()

    c[l:l+k] = sorted(c[l:l+k])
    if c == b:
        print(1)
        continue

    c[r-k+1:r+1] = sorted(c[r-k+1:r+1])
    if c == b:
        print(2)
        continue

    d[r-k+1:r+1] = sorted(d[r-k+1:r+1])
    if d == b:
        print(1)
        continue

    d[l:l+k] = sorted(d[l:l+k])
    if d == b:
        print(2)
        continue

    print(3)
