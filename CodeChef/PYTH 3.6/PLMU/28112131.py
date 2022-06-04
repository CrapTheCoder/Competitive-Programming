for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = a.count(0)
    e = a.count(2)

    print((d * (d - 1) // 2) + (e * (e - 1) // 2))
