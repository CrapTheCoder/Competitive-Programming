n, k = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a[:k])
m = s

for i in range(n-k):
    s -= a[i]
    s += a[i+k]

    m = min(m, s)

print(sum(a) - m)