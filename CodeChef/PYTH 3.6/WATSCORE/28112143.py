for _ in range(int(input())):
    n = int(input())
    l = [0] * 11

    for _ in range(n):
        p, s = map(int, input().split())
        l[p-1] = max(l[p-1], s)

    print(sum(l[:8]))
