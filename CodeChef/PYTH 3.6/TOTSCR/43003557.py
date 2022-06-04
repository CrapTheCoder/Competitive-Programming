for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for _ in range(n):
        s = input()

        t = 0
        for i, j in enumerate(s):
            if j == '1':
                t += a[i]

        print(t)