for _ in range(int(input())):
    n = int(input())
    l = list(range(1, n+1))

    for i in range(n):
        print(*l, sep='')
        l = l[1:] + [l[0]]
