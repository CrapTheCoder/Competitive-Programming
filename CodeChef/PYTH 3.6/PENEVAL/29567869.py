for _ in range(int(input())):
    s = list(input().strip())

    i = 0

    while i < len(s) - 1:
        if s[i].isalpha() or s[i] == ')':
            if s[i + 1].isdigit():
                if i + 2 >= len(s) or s[i + 2] == ')':
                    s = s[:i+1] + ['*', s[i+1]] + s[i+2:]
                else:
                    s = s[:i+1] + ['*', s[i+1], '+'] + s[i+2:]
                i += 1
            elif s[i + 1].isalpha() or s[i + 1] == '(':
                s = s[:i+1] + ['+'] + s[i+1:]

        i += 1

    s = ''.join(s)

    s = s.strip('+')

    x = 2
    y = 4
    z = 10

    print(eval(s))
