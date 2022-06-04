for _ in range(int(input())):
    n = int(input())
    s = input()

    r = s.count('P')
    c = 0

    for i in range(2, n-2):
        if (r + c) / n >= 0.75:
            break

        if s[i] != 'P' and 'P' in s[i-1] + s[i-2] and 'P' in s[i+1] + s[i+2]:
            c += 1

    if (r + c) / n < 0.75:
        print(-1)
    else:
        print(c)