for _ in range(int(input())):
    n = int(input())

    cl = {}
    ns = []

    for _ in range(n):
        f, l = input().split()
        cl[f] = cl.get(f, 0) + 1

        ns.append((f, l))

    for f, l in ns:
        if cl[f] > 1:
            print(f + ' ' + l)
        else:
            print(f)