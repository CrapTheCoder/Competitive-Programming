from sys import stdin
input = stdin.readline
 
def check(a, b, c):
    return (b - a == c - b) and a > 0 and b > 0 and c > 0 and (a % x == 0) and (b % y == 0) and (c % z == 0)
 
for _ in range(int(input())):
    x, y, z = list(map(int, input().split()))
 
    if check(y - (z - y), y, z) or check(x, (x + z) // 2, z) or check(x, y, y + (y - x)):
        print('YES')
    else:
        print('NO')