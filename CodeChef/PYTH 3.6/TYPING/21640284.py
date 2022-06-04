l = ['d', 'f']

for _ in range(int(input())):
    n = int(input())
    a = 0

    d = {}

    for x in range(n):
        s = input()
        c = 2 if s else 0

        if s in d:
            c = d[s] // 2
        else:
            for i, j in enumerate(s[1:], 1):
                if (s[i] in l) == (s[i-1] in l):
                    c += 4
                else:
                    c += 2

            d[s] = c

        a += c

    print(a)