for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    e = 0
    o = 0

    for i in l:
        if i % 2:
            o += 1
        else:
            e += 1

    print(e * o)