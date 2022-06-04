for _ in range(int(input())):
    n = int(input())

    s = 0
    for i in range(1, n):
        s += i ** 3

    for i in range(n, 0, -1):
        s += i ** 3

    print(s)