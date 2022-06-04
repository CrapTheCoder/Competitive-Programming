from itertools import permutations

t = int(input())

for x in range(t):
    ans = 0

    c = 'c'
    h = 'h'
    e = 'e'
    f = 'f'

    s = input()

    cc = s.count('c')
    hc = s.count('h')
    ec = s.count('e')
    fc = s.count('f')

    sl = list(s)
    scl = [cc, hc, ec, fc]

    if True:
        m = min(scl)
        if m == 0:
            print("normal")
            continue

        l = [''.join(i) for i in permutations('chef')]

        for y in range(len(l)):
            ans += s.count(l[y])

        if ans == 0:
            print("normal")
            continue
        print("lovely " + str(ans))