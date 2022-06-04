for _ in range(int(input())):
    n = int(input())

    j = 1

    for i in range(n):
        s = ''

        l = []
        for j in range(j, j+i+1):
            l.append(str(j))

        j += 1

        print(''.join(l[::-1]))