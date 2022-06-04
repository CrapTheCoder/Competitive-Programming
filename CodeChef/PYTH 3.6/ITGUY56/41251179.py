for _ in range(int(input())):
    n = int(input())

    for i in range(n):
        s = ''

        for j in range(n):
            if not (i+j) % 2:
                s += '0'
            else:
                s += '1'

        print(s)