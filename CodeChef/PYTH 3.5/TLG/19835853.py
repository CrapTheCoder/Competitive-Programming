lis = []

n = int(input())

p1, p2 = 0, 0

for i in range(n):
    a, b = map(int, input().split())

    p1 += a
    p2 += b

    lis.append([[2, 1][p1 > p2], abs(p1 - p2)])

res = max(lis, key=lambda x: x[1])

print('{} {}'.format(res[0], res[1]))