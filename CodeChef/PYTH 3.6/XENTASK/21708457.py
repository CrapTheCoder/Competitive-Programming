for _ in range(int(input())):
    n = int(input())

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    s1 = sum(x)
    s2 = sum(y)

    a = sum(x[0::2])
    b = sum(y[1::2])

    print(min(a + b, (s1 - a) + (s2 - b)))