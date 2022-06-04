for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(input())

    c = 0

    for _ in range(k):
        l = []

        for i in range(n - 1):
            if a[i] == 'G' and a[i + 1] == 'L':
                l.append(i)

        for i in l:
            a[i], a[i + 1] = a[i + 1], a[i]

    print(n)
    print(''.join(a))
