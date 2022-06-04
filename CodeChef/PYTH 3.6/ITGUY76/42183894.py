for _ in range(int(input())):
    n = int(input())

    s = [0] * (2*n-1)
    l = 0
    r = 2*n-2

    for i in range(n):
        t = s.copy()
        t[l] = t[r] = t[n-1] = '*'
        print(*t, sep='')
        l += 1
        r -= 1