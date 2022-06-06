for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = [0] + [a[i] - a[i-1] for i in range(1, n)]
 
    s = sum(b)
 
    r = 0
    for i in range(1, n):
        s -= i * a[i] - r
        r += a[i]
 
    print(s)