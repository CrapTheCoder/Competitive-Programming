for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    n = p = m = 0

    for i in l:
        if i == 1: p += 1
        elif i == -1: n += 1
        elif i != 0: m += 1

    if (m > 1) or (n > 1 and p == 0) or (n and m):
        print('no')
    else:
        print('yes')
