for _ in range(int(input())):
    s = input()
    x = s[0]

    for i, j in enumerate(s[1:], 1):
        if j != s[i-1]:
            x += j

    print(min(x.count('U'), x.count('D')))