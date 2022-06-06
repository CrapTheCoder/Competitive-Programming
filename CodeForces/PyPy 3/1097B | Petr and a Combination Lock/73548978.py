def solve(i=0, cur=0):
cur %= 360

if i == n:
return cur == 0

return solve(i+1, cur - a[i]) or solve(i+1, cur + a[i])

n = int(input())
a = [int(input()) for _ in range(n)]

print('YES' if solve() else 'NO')