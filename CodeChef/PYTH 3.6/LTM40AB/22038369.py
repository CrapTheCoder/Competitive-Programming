for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(sum(max(0, d - max(c, x + 1) + 1) for x in range(a, b+1)))