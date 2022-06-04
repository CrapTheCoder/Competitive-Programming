primes = [3, 5, 7, 11, 13, 17]

m = ((0, 1), (1, 2), (0, 3), (1, 4), (2, 5), (3, 4),
     (4, 5), (3, 6), (4, 7), (5, 8), (6, 7), (7, 8))

v = {(1, 2, 3, 4, 5, 6, 7, 8, 9): 0}
po = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]

while po:
    d1 = po.pop(0)

    for i in m:
        if d1[i[0]]+d1[i[1]] in primes:
            d2 = d1.copy()
            d2[i[0]], d2[i[1]] = d2[i[1]], d2[i[0]]

            if tuple(d2) not in v:
                v[tuple(d2)] = v[tuple(d1)] + 1
                po.append(d2)

for t in range(int(input())):
    input()
    a = list(map(int, input().split()))
    a += list(map(int, input().split()))
    a += list(map(int, input().split()))
    a = tuple(a)

    if a in v:
        print(v[a])
    else:
        print(-1)
