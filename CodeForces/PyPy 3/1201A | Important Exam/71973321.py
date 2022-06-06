n, m = map(int, input().split())
 
x = [[0] * 26 for _ in range(m)]
 
for _ in range(n):
    s = input()
 
    for i in range(m):
        x[i][ord(s[i]) - ord('A')] += 1
 
a = list(map(int, input().split()))
 
ans = 0
 
for i in range(m):
    ans += max(x[i]) * a[i]
 
print(ans)