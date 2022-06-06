for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
 
    print(max(x * b, (a - x - 1) * b, a * y, a * (b - y - 1)))