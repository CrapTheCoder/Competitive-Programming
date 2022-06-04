for _ in range(int(input())):
    n = int(input())

    for i in range(n):
        s = ''

        for j in range(n):
            if j % 2 == 0:
                s += '1'
            else:
                s += '0'

        print(s)