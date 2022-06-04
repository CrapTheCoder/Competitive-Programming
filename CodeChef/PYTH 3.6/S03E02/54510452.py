from string import ascii_uppercase

for _ in range(int(input())):
    n, k = map(int, input().split())
    s2 = input().strip()

    if k == 0:
        if len(set(s2)) == 1:
            print(n)
        else:
            print(-1)

        continue

    maxi = 0
    for ch in set(s2):
        s = s2.strip(ch)
        cur = len(s2) - len(s)
        n = len(s)

        l = []

        d = 0
        for i in range(n):
            if s[i] == ch:
                d += 1
            else:
                if d != 0:
                    l.append(d)
                    d = 0

        if d != 0:
            l.append(d)

        l.sort()
        i = len(l)

        for _ in range(k-1):
            i -= 1
            if i < 0:
                break

            cur += l[i]

        if cur > maxi:
            maxi = cur

    print(maxi)
