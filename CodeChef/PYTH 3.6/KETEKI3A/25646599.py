for _ in range(int(input())):
    n = int(input())

    if n == 1:
        print(1, 1)
    else:
        print(0, n // 2)
