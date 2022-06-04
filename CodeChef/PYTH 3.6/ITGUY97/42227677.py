from string import ascii_uppercase

for _ in range(int(input())):
    n = int(input())
    s = ['#'] * n

    l = r = n // 2

    d = []

    for i in range(n // 2 + 1):
        s[l] = s[r] = '.'
        l -= 1
        r += 1
        print(*s, sep='')
        d.append(s.copy())

    d.pop()
    d.reverse()

    for i in d:
        print(*i, sep='')