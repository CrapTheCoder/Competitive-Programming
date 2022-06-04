for _ in range(int(input())):
    n = int(input())
    s = list(input())

    r = g = b = 0

    for i in range(n):
        r += s[i] == 'R'
        g += s[i] == 'G'
        b += s[i] == 'B'

    print(n - max(r, g, b))