for _ in range(int(input())):
    n, x, s = map(int, input().split())
    lis = [i for i in range(n+1)]

    for _ in range(s):
        a, b = map(int, input().split())
        lis[a], lis[b] = lis[b], lis[a]
    print(lis.index(x))