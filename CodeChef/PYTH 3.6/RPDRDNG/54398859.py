from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    b = sorted(map(int, input().split()))

    pre = b[:n]
    suf = b[n:][::-1]

    a = [-1] * n

    j = 0
    for i in range(n):
        if (i+1) % 2 == 1:
            a[j] = pre[i]
            j += 1

    j = n-1
    for i in range(n):
        if (i+1) % 2 == 1:
            a[j] = suf[i]
            j -= 1

    # print(a, pre, suf)
    # print(*a)

    nb = []

    pre = []
    for i in range(n):
        pre.append(a[i])
        nb.append(pre[(len(pre) - 1) // 2])

    suf = []
    for i in range(n-1, -1, -1):
        suf.append(a[i])
        nb.append(suf[len(suf) // 2])

    nb.sort()
    # print(nb, a)

    if (nb != b) or (-1 in a) or (a != sorted(a)) or (len(set(a)) != len(a)):
        print(-1)
    else:
        print(*a)