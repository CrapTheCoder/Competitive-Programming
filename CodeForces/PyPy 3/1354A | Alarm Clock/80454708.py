for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
 
    if b >= a:
        print(b)
        continue
 
    if c <= d:
        print(-1)
        continue
 
    print(b + -(-(a - b) // (c - d)) * c)