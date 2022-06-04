for _ in range(int(input())):
    p1, p2, k = map(int, input().split())
    p = p1 + p2

    print(['CHEF', 'COOK'][p // k % 2])