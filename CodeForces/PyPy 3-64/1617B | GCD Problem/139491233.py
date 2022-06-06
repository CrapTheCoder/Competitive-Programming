for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(n // 2, n // 2 - 1, 1)
    else:
        if (n // 2) % 2 == 0:
            print(n // 2 - 1, n // 2 + 1, 1)
        else:
            print(n // 2 - 2, n // 2 + 2, 1)