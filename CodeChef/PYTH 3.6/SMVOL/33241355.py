for _ in range(int(input())):
    n = int(input())

    if n == 1:
        print(1)
        continue

    print(n ** 3 - (n-2) ** 3)