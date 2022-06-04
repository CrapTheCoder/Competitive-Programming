for _ in range(int(input())):
    n = int(input())

    c = int((2*n) ** 0.5) + 10
    while c * (c+1) // 2 > n:
        c -= 1

    d = c * (c+1) // 2

    print(c * (c+1) * (2*c+1) // 6 + (n-d) * (c+1))
