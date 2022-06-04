n, k, r = map(int, input().split())
x = r

while k - r >= 0 and n > 0:
    n -= 1
    k -= r
    r += x

print(n)