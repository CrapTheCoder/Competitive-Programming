for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s1 = m1 = 0
    s2 = m2 = 0

    for i in range(n):
        s1 += a[i]
        s2 += b[i]

        if a[i] > m1: m1 = a[i]
        if b[i] > m2: m2 = b[i]

    if s1 - m1 < s2 - m2: print('Alice')
    elif s1 - m1 > s2 - m2: print('Bob')
    else: print('Draw')
