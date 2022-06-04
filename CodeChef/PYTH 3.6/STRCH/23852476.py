for _ in range(int(input())):
    n = int(input())
    s, x = input().split()

    l = []

    for i, j in enumerate(s):
        if j == x:
            l.append(i+1)

    if l:
        a = l[0] * (n - l[0] + 1)

        for i, j in enumerate(l[1:], 1):
            x = l[i] - l[i-1]
            a += (n - l[i-1] - x + 1) * x

        print(a)
    else:
        print(0)