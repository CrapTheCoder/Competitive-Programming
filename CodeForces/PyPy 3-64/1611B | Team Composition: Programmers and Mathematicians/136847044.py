for _ in range(int(input())):
    a, b = map(int, input().split())
    t = a + b
 
    x = min(t // 4, (a + min(a*3, b)) // 4, (b + min(b*3, a)) // 4)
 
    print(x)