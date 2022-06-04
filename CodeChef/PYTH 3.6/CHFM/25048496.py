for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)

    if (s / n) in a:
        print(a.index(s / n) + 1)
    else:
        print('Impossible')
