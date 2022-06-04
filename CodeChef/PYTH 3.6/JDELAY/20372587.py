for _ in range(int(input())):
    n = int(input())

    c = 0

    for x in range(n):
        s, j = map(int, input().split())

        c += j - s > 5

    print(c)