for _ in range(int(input())):
    n = int(input())

    if n == 1: print(1, 1)
    else: print(1, 10 ** (n // 2))