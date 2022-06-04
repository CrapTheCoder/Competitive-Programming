for _ in range(int(input())):
    n = int(input())
    l = [0, 1]

    for _ in range(n):
        l.append(l[-1] + l[-2])

    s = ''

    for i in range(n):
        s += str(l[i])
        print(s)