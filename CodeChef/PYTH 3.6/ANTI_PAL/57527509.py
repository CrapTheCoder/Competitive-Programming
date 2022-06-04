from random import shuffle
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    s = input()

    if n % 2:
        print('NO')
        continue

    c = Counter(s)

    if max(c.values()) > n // 2:
        print('NO')
        continue

    f = ''.join(i[0] * i[1] for i in sorted(c.items(), key=lambda x: x[1], reverse=True))

    lf = f[:n//2]
    rg = f[n//2:][::-1]

    if any(lf[i] == rg[-i-1] for i in range(n // 2)):
        print('NO')
    else:
        print('YES')
        print(lf + rg)