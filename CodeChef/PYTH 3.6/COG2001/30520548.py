from collections import Counter

for _ in range(int(input())):
    n = int(input())
    p, q = map(int, input().split())

    k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    s = Counter(map(int, input().split()))

    b = input()

    fk = 0
    fa = 0

    dk = 0
    da = 0

    for i in range(n):
        if b[i] == '0':
            x = k[i] + a[i]

            if x in s:
                s[x] -= 1

                if s[x] == 0:
                    s.pop(x)

                fk += k[i]
                fa += a[i]

        if b[i] == '1':
            x = k[i] + a[i]

            if x in s:
                s[x] -= 1

                if s[x] == 0:
                    s.pop(x)

                dk += k[i]
                da += a[i]

    pf = p * fk + q * fa
    pd = p * dk + q * da

    if pf > pd:
        print('Frost')
    else:
        print('DustinKiller')
