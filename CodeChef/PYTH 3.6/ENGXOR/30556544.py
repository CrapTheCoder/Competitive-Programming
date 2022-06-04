from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    e = o = 0

    for i in a:
        if bin(i).count('1') % 2:
            o += 1
        else:
            e += 1

    for _ in range(q):
        if bin(int(input())).count('1') % 2:
            print(o, e)
        else:
            print(e, o)
