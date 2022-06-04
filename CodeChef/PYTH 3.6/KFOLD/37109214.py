from collections import Counter

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    x = n // k

    c = Counter(s)

    tot = ''
    r = ''

    for i in sorted(c.keys()):
        if c[i] % x != 0:
            print('IMPOSSIBLE')
            break

        r += i * (c[i] // x)

    else:
        print(''.join(r if i % 2 == 0 else r[::-1] for i in range(n // k)))

"""

4 4

01100110

"""