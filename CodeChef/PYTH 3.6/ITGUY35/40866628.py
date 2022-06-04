for _ in range(int(input())):
    n = int(input())

    for i in range(n):
        s = ''

        for j in range(n):
            s += str(j+1)
            s += str(i+1)

        print(s)
