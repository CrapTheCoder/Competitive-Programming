for _ in range(int(input())):
    r, c, k = map(int,input().split())
    a = min(c+k, 8) - max(c-k, 1) + 1
    b = min(r+k, 8) - max(r-k, 1) + 1
    print(a * b)