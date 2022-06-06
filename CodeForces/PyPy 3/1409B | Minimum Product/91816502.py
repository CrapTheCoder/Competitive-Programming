def solve(a, b, x, y, n):
    na = max(x, a - n)
    n -= a - na
 
    b = max(y, b - n)
    a = na
 
    return a * b
 
for _ in range(int(input())):
    a, b, x, y, n = map(int, input().split())
    print(min(solve(a, b, x, y, n), solve(b, a, y, x, n)))