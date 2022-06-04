n, k = map(int, input().split())
a = list(map(int, input().split()))

x = sum(a)

r = k - x

if r == 0:
    print('YES')
else:
    if r not in a and min(a) <= k - x <= max(a):
        print('YES')
    else:
        print('NO')
