for _ in range(int(input())):
    a, b, n = map(int, input().split())
    l = (a, b, a^b)

    print(l[n % 3])