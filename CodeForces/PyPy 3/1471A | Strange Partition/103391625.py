for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
 
    s = 0
    s1 = 0
 
    for i in a:
        s += i
        s1 += -(-i // x)
 
    print(-(-s // x), s1)