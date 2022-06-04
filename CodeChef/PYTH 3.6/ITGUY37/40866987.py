for _ in range(int(input())):
    n = int(input())

    for i in range(n):
        s = ''
        for j in range(n-i, 0, -1):
            s += str(j)

        print('*' * i + s)
