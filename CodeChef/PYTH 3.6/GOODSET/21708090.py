for _ in range(int(input())):
    n = int(input())

    print(*[i for i in range(1, n * 2, 2)])