for _ in range(int(input())):
    n = int(input())

    print(*range(2, n+2))
    print(*range(2 ** 17 + 2, 2 ** 17 + 2 + n))