for _ in range(int(input())):
    s = input()

    if s[0] == '0':
        print(0)
        continue

    if '0' not in s:
        print(1)
        continue

    i = 0

    while i < len(s) and s[i] == '1':
        i += 1

    c = 0

    while i < len(s) and s[i] == '0':
        c += 1
        i += 1

    print(c)