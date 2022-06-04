n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

ps = [0] * (n+1)
for i in range(1, n+1):
    ps[i] = ps[i-1] + b[i]

ms = [float('-inf')] * (n+1)
for i in range(1, n+1):
    ms[i] = max(ms[i-1], a[i] - ps[i])

ns = [float('-inf')] * (n+1)
ns[n] = a[n] - ps[n]
for i in range(n-1, 0, -1):
    ns[i] = max(ns[i+1], a[i] - ps[i])

maxi = max(a)

for j in range(2, n+1):
    maxi = max(maxi, a[j] + ps[j-1] + ms[j-1])

for j in range(1, n):
    maxi = max(maxi, a[j] + ps[n] + ps[j-1] + ns[j+1])

print(maxi)
