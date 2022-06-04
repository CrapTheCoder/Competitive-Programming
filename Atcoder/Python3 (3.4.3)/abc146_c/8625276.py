def f(j):
    return j * a + len(str(j)) * b

a, b, x = map(int, input().split())

m = -1
l, r = 0, 10 ** 9

while l < r - 1:
    m = (l + r) // 2
    d = f(m)

    if d == x:
        break

    if d < x:
        l = m
    else:
        r = m - 1

while r < 10 ** 9 and f(r) < x:
    r += 1

while f(r) > x:
    r -= 1

print(max(0, r))
