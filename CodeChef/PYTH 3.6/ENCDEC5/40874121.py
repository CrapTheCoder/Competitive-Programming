for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())

    for i in range(0, n - n%2, 2):
        a[i], a[i+1] = a[i+1], a[i]

    for i in range(n):
        a[i] += a[i] % 3

    a.reverse()

    c1 = float('-inf')
    for i in range(n):
        if x > a[i] > c1:
            c1 = a[i]

    c2 = float('inf')
    for i in range(n):
        if x < a[i] < c2:
            c2 = a[i]

    if c1 == float('-inf'): c1 = -1
    if c2 == float('inf'): c2 = -1

    print(c1, c2)
