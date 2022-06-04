for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    
    for i in a:
        x = i % k
        c += min(x, k - x) if i >= k else k - x

    print(c)
