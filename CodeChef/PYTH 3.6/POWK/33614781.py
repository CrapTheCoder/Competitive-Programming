MOD = 10 ** 9 + 7

for _ in range(int(input())):
    n = int(input())
    m = int(input())

    if m < n - 1:
        print('NO')
        continue

    ks = [f'k{i}' for i in range(1, n+1)]
    occ = {i: 0 for i in ks}
    occx = {i: 0 for i in ks}
    wins = {i: 0 for i in ks}

    qsx = []
    qsy = []

    for _ in range(m):
        x, y = input().strip().split()
        qsx.append(x)
        qsy.append(y)

        occ[x] = occ[y] = occx[x] = 1

    if (0 in occ.values()) or (list(occx.values()).count(0) != 1):
        print('NO')
        continue

    cur = [i for i in ks if occx[i] == 0]
    curs = {cur[0]}

    try:
        while len(curs) < n:
            ke = {}

            for x, y in zip(qsx, qsy):
                if x in curs:
                    continue

                ke[x] = ke.get(x, []) + [y]

            cs = []

            for key, value in ke.items():
                if all(i in curs for i in value):
                    cs.append(key)

            cur.append(cs[0])
            curs.add(cs[0])

        inds = {j: i for i, j in enumerate(cur)}

        for x, y in zip(qsx, qsy):
            if inds[x] < inds[y]:
                raise Exception
    except:
        print('NO')
        continue

    print('YES')
    print(*cur, sep='\n')