for _ in range(int(input())):
    n, c0, c1, h = map(int, input().split())
    s = input()
 
    d0 = s.count('0')
    d1 = s.count('1')
 
    print(min(c0 * n + h * d1, c1 * n + h * d0, c0 * d0 + c1 * d1))