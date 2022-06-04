for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    a, b = 0, sum(l)

    j = -1
    m = 100000000000000

    for i in range(n):
        e = l[i]

        a += e
        c = a + b

        if c < m:
            m = c
            j = i
        b -= e

    print(j + 1)