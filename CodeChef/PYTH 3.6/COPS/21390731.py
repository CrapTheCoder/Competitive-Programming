for _ in range(int(input())):
    m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * 100

    z = x * y

    for i in a:
        l = max( 1 , i - z)
        h = min(100, i + z)

        for i in range(l-1, h):
            b[i] = 1

    print(b.count(0))