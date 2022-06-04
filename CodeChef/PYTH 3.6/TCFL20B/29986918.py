for _ in range(int(input())):
    n = int(input())

    l = []

    for _ in range(n):
        s = input()
        t = int(input())

        l.append((t, s))

    l.sort()

    for i in l:
        print(i[1])