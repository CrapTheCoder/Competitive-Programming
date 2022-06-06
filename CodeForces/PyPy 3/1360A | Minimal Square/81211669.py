for _ in range(int(input())):
    a, b = map(int, input().split())
    x = max(min(a, b) * 2, a, b)
 
    print(x * x)