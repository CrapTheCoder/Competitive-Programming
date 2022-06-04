for _ in range(int(input())):
    n = int(input())
    s = input()

    c = 0

    l = len(s)

    for i in range(l - 1):
        if s[i] == s[i + 1] == 'S':
            c += 1

    if n == 1:
        print(c)
        continue

    c1 = 0
    s1 = s + s
    l1 = len(s1)

    for i in range(l1 - 1):
        if s1[i] == s1[i + 1] == 'S':
            c1 += 1

    print(c + (c1 - c) * (n - 1))
