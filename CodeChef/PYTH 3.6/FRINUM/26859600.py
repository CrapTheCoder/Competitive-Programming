def remrep(a):
    d = {}

    for i in a:
        try: d[i] += 1
        except: d[i] = 1

    for i in d:
        if d[i] == 1:
            return i

    return -1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(remrep(a))

