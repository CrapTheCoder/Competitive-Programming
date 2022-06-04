k, n = map(int, input().split())
a = list(map(int, input().split()))

maxi = 0

for i in range(1, n):
    x = a[i] - a[i-1]

    maxi = max(maxi, x)

x = a[-1] - a[0]

if k - x < x:
    x = k - x

maxi = max(maxi, x)

print(k - maxi)