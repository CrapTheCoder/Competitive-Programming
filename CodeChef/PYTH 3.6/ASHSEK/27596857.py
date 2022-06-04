for _ in range(int(input())):
    n = int(input())

    if n % 2:
        print(0)
    else:
        print((n - 1) // 4)
