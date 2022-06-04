n = int(input())
a = sorted((int(input()) for _ in range(n)), reverse=True)

s = 0

for i in range(n):
    s = max(s, a[i] * (i+1))

print(s)