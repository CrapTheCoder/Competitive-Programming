for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0

    for i, j in enumerate(a):
        if s < 0:
            j = -j
        if i % 2:
            s -= j
        else:
            s += j

    if abs(s) >= k:
        print(1)
    else:
        print(2)