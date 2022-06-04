for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if 0 in a:
        x = a.count(0) * 1000
        y = (n - a.index(0)) * 100

        print(x + y)
    else:
        print(0)
