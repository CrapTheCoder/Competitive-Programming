from sys import setrecursionlimit
setrecursionlimit(10 ** 9)
 
def solve(x):
    if x in s:
        return False
 
    if x >= y:
        return True
 
    s.append(x)
 
    if x % 2:
        return solve(x - 1)
 
    return solve(3 * x // 2)
 
for _ in range(int(input())):
    x, y = map(int, input().split())
 
    s = [0]
 
    print('YES' if solve(x) else 'NO')