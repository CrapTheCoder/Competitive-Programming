for _ in range(int(input())):
    n = int(input())
    s = list(input())

    if n == 1:
        print(int(s[0] == '0'))
    else:
        c = 0
        i = 1

        if s[0] == s[1] == '0':
            s[0] = '1'
            c += 1
        if s[-1] == s[-2] == '0':
            s[-1] = '1'
            c += 1

        while i < n-1:
            if s[i+1] == '1': i += 3
            elif s[i-1] == '1': i += 1
            elif s[i] == '1': i += 2
            else:
                c += 1
                i += 2

        print(c)
