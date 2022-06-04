n, k = map(int, input().split())
a = list(map(int, input().split()))

m = sum(a[:k])
s = m


for i in range(k, n):
    s -= a[i - k] - a[i]
    m = max(m, s)

print(m)