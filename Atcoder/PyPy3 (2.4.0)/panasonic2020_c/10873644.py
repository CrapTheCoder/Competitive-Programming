a, b, c = map(int, input().split())

c -= a + b

if 4 * a * b < c ** 2 and 0 < c:
    print('Yes')
else:
    print('No')