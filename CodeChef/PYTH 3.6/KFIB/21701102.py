n, k = map(int, input().split())
a = [1] * k
a += [k]

s = k

for i in range(n - k - 1):
    s = s - a[i] + a[i+k]
    a.append(s)

print(s % 1000000007 if n > k else '1')