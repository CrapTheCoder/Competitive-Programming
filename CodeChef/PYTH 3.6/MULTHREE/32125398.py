for _ in range(int(input())):
    k, d0, d1 = map(int, input().split())

    ss = [d0, d1]

    cs = d0 + d1

    for i in range(200):
        ss.append(cs % 10)
        cs = (cs * 2) % 10

    ss = ss[:200]

    if k < 100:
        print('YES' if sum(ss[:k]) % 3 == 0 else 'NO')
        continue

    k -= 100

    x = ss[:100]
    y = ss[100:]

    s = sum(x) + sum(y) * (k // 100) + sum(y[:k % 100])

    print('YES' if s % 3 == 0 else 'NO')