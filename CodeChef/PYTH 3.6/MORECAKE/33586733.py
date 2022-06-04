req = 0
tot = 0

for _ in range(int(input())):
    s, n, k, r = map(int, input().split())

    if r != 1:
        t = k * (1 - pow(r, n)) // (1 - r)
    else:
        t = k * n

    req += t
    tot += s

    if t <= s:
        print('POSSIBLE', s-t)
    else:
        print('IMPOSSIBLE', t-s)

if req < tot:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')