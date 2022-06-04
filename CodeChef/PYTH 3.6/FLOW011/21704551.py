for _ in range(int(input())):
    n = int(input())

    if n < 1500:
        print(n + ((n * 1 / 10) + (n * 9 / 10)))
    else:
        print(n + 500 + (n * 98 / 100))