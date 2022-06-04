for _ in range(int(input())):
    s = list(input())
    n = len(s)

    for i in range(len(s) // 2):
        s[i], s[n-i-1] = s[n-i-1], s[i]

    print(*s, sep='')