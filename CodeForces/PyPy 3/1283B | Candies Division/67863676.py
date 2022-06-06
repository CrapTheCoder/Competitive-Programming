for _ in range(int(input())):
    n, k = map(int, input().split())
 
    t = (n // k) * k
    r = n % k
 
    print(t + min(r, k // 2))