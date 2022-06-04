for _ in range(int(input())):
    n = input()
    l = len(n)

    if l == 1:
        print(l)
    else:
        nn = ''

        for i in range(l - 1):
            nn += str(int(n[i]) ^ int(n[i+1]))

        nn += str(int(n[l-1]) ^ int(n[0]))

        print(nn)
