for _ in range(int(input())):
    n = int(input())
    l = list(range(1, n+1))

    while l:
        if len(l) % 2 == 0:
            print(*l[::-1], sep='')
        else:
            print(*l, sep='')

        l.pop()