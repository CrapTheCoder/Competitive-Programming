for t in range(int(input())):
    a = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    b = [chr(c) for c in range(ord('z'), ord('a') - 1, -1)]

    dum = ''

    i_dont_need_this = input()

    s = input()
    s = list(s)

    for i in range(0, len(s) - 1, 2):
        s[i], s[i + 1] = s[i + 1], s[i]

        j = a.index(s[i])
        s[i] = b[j]

        j = a.index(s[i + 1])
        s[i + 1] = b[j]

    if len(s) % 2 == 1:
        j = a.index(s[-1])
        s[-1] = b[j]

    print(''.join(i for i in s))