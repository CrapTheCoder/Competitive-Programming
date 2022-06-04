for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n - 2):
        del a[a.index(sorted(a[:3])[1])]

    print(a[0], a[1])
