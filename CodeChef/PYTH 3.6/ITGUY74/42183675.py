for _ in range(int(input())):
    n = int(input())
    s = list(range(1, n+1))

    for i in range(n):
        t = s.copy()
        t[n-i-1] = '*'
        print(*t, sep='')